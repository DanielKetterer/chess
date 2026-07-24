"""
Chess.com game analyzer.

Pipeline:
  1. Fetch one game for a Chess.com username, or load games from a move-history CSV.
  2. Replay a selected game position by position.
  3. Ask Stockfish (MultiPV 3) for evaluation, best move, and candidate moves.
  4. Compare played move vs best move using WIN PROBABILITY, not raw centipawns.
  5. Classify moves, detect tactical vs positional errors, find critical positions,
     identify the opening and first deviation from theory.
  6. Emit a human-readable coaching report (markdown) plus an eval graph (PNG).

Usage:
  python chess_analyzer.py --username hikaru                      # most recent game
  python chess_analyzer.py --username hikaru --game-id <game_id>  # one specific game
  python chess_analyzer.py --csv moves.csv                         # newest CSV game
  python chess_analyzer.py --csv moves.csv --game latest:rapid     # legacy CSV selector
  Options: --depth 14  --multipv 3  --out report.md  --graph eval.png
"""

import argparse
import hashlib
import io
import json
import math
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone

import chess
import chess.engine
import chess.pgn
import pandas as pd

STOCKFISH_PATH = os.environ.get("STOCKFISH_PATH", r"C:\Users\admin\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")
CHESSCOM_API_ROOT = "https://api.chess.com/pub"
PIECE_VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
                chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

# --- depth-to-find measurement constants -----------------------------------
# Below MEASUREMENT_FLOOR the search is dominated by qsearch and material
# counting, so "the engine prefers another move" is not evidence about the
# move played. Results at or below the floor are censored, not measured.
MEASUREMENT_FLOOR = 6
# Consecutive agreeing depths required before a depth counts as the answer,
# so a preference that flaps at one depth is not recorded at its first flap.
STABLE_RUN = 3
# Sentinels for censored measurements. Not ints: the report and any
# downstream plot must treat them as categories.
DEPTH_CENSORED_LOW = "<=floor"
DEPTH_CENSORED_HIGH = ">cap"
REFUTE_DEPTH_CENSORED_HIGH = ">18"
REFUTE_DEPTH_CAP = 18
# Classification bands, for labelling moves in the report only.
ERROR_THRESHOLDS = {"inaccuracy": 5.0, "mistake": 10.0, "blunder": 20.0}
# The bar the played move must be seen to cross before it counts as refuted.
#
# Two wrong answers came before this one. Feeding in the per-class threshold
# from ERROR_THRESHOLDS made the number mean something different in every row.
# Replacing it with a flat 10.0 was worse in a way that took a real report to
# see: `classify` calls a move an inaccuracy when it loses at least 5 and
# under 10, so an inaccuracy's full-depth loss sits *below* a 10-point bar and
# the crossing can only ever happen through shallow-search noise. The entire
# inaccuracy band censored high by construction, and the two that did return a
# depth returned depth 1 -- noise crossings, which then routed those moves into
# `attention` and inflated a metric that was about to be trusted.
#
# Scaling the bar to the error asks every move the same question: how deep
# before most of this move's cost is visible? The floor keeps tiny errors from
# being declared refuted by a rounding difference.
REFUTE_THRESHOLD_FLOOR_WP = 5.0
REFUTE_THRESHOLD_FRACTION = 0.6


def refute_threshold_for(wp_loss):
    """Per-move refute bar. See REFUTE_THRESHOLD_FLOOR_WP above."""
    return max(REFUTE_THRESHOLD_FLOOR_WP,
               REFUTE_THRESHOLD_FRACTION * float(wp_loss or 0.0))
PRE_ERROR_BUCKETS = ("winning", "balanced", "losing")

# --- puzzle gates ----------------------------------------------------------
# Kept as named constants so the rejection tally can report which one bound.
PUZZLE_CATEGORIES = ("brilliant_sacrifice", "missed_tactic", "allowed_tactic",
                     "endgame")
PUZZLE_REFUTE_MIN = 3
PUZZLE_REFUTE_MAX = 8
# Uniqueness floor: how much better the best move must be than the second best
# before the position has one right answer worth grading.
#
# This was 10.0, which was a number invented without calibration. Across a
# twelve-error game the observed gaps had a median near 2 and only two rows
# cleared 10, so the gate was passing under a fifth of positions on its own.
# Tying it to the inaccuracy band makes it mean something: if playing the
# second-best move would itself be scored an inaccuracy, the position has a
# unique answer by the same standard the rest of the report uses.
PUZZLE_WP_GAP_MIN = ERROR_THRESHOLDS["inaccuracy"]

# `attention` needs both halves, not just a shallow refutation. A move whose
# refutation is visible at depth 1 but whose replacement takes depth 17 to find
# is a hard position, not inattention -- that shape happens when many moves
# lose and exactly one holds. Counting it as an attention error inflates the
# metric with positions that were genuinely difficult.
ATTENTION_REFUTE_MAX = 2
ATTENTION_REQUIRES_FINDABLE = "obvious"

# --- brilliant sacrifice ---------------------------------------------------
# Two separate questions here, and the second is the strict one.
#
# Whether a move is a sacrifice is a material question, answered by walking
# the principal variation and looking for a trough: material goes down and the
# engine still calls the move best. That subsumes what a static exchange
# evaluation would tell us about the destination square, and it also catches
# quiet sacrifices, where the material is offered somewhere other than where
# the piece moved.
#
# Whether a sacrifice makes a *puzzle* is Spielmann's distinction. A sham
# sacrifice returns the material by force inside the line, so the position is
# calculable to the end and an engine comparison can score an answer right or
# wrong. A real sacrifice buys positional compensation that never resolves
# back into material. That is not gradable, for exactly the reason positional
# errors do not make puzzles: no unique answer, and no way to verify you
# solved it. Real sacrifices are detected and reported, never served.
SAC_EXCHANGE_TROUGH = 1.5      # pawns; exchange-sacrifice territory
SAC_PIECE_TROUGH = 3.0         # a whole minor piece or more
SAC_RECOVERY_TOLERANCE = 0.5   # "material came back" means within half a pawn
SAC_MIN_PV_PLIES = 6           # a shorter line cannot show recovery either way
SAC_MIN_PRE_EVAL_CP = -200     # not already lost
SAC_MAX_PRE_EVAL_CP = 300      # not already crushing; a sac from +5 is decoration
SAC_MIN_PLY = 21               # coarse gambit guard, refined by book_ply later



# ----------------------------------------------------------------------------
# Chess.com game retrieval
# ----------------------------------------------------------------------------

def chesscom_get_json(url, username, retries=4):
    """GET one Chess.com PubAPI JSON object with a descriptive User-Agent."""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"ChessGameAnalyzer/1.1 (username: {username})",
            "Accept": "application/json",
            "Accept-Encoding": "identity",
        },
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                data = json.load(response)
            if not isinstance(data, dict):
                raise RuntimeError(f"Unexpected Chess.com response for {url}")
            return data
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise RuntimeError(f"Chess.com returned invalid JSON for {url}") from exc
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == retries - 1:
                raise RuntimeError(
                    f"Chess.com returned HTTP {exc.code} for {url}"
                ) from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"Could not reach Chess.com: {exc}") from exc
        time.sleep(2 ** attempt)
    raise RuntimeError(f"Could not retrieve {url}")


def game_identifiers(game):
    """Return the UUID, URL, and URL-tail forms by which a game can be selected."""
    values = set()
    for value in (game.get("uuid"), game.get("url")):
        if value:
            text = str(value).strip().casefold().rstrip("/")
            values.add(text)
            values.add(text.rsplit("/", 1)[-1])

    pgn = game.get("pgn")
    if isinstance(pgn, str):
        link = re.search(r'^\s*\[Link\s+"([^"]+)"\]', pgn, re.MULTILINE)
        if link:
            text = link.group(1).strip().casefold().rstrip("/")
            values.add(text)
            values.add(text.rsplit("/", 1)[-1])
    return values


def game_matches_id(game, game_id):
    wanted = str(game_id).strip().casefold().rstrip("/")
    wanted_tail = wanted.rsplit("/", 1)[-1]
    identifiers = game_identifiers(game)
    return wanted in identifiers or wanted_tail in identifiers


def pgn_clock_seconds(node):
    """Read a [%clk ...] annotation using python-chess across supported versions."""
    clock_method = getattr(node, "clock", None)
    if callable(clock_method):
        try:
            value = clock_method()
            if value is not None:
                return float(value)
        except (TypeError, ValueError):
            pass

    match = re.search(r"\[%clk\s+([0-9:.]+)\]", node.comment or "")
    if not match:
        return None
    try:
        parts = [float(part) for part in match.group(1).split(":")]
    except ValueError:
        return None
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] if len(parts) == 1 else None


def game_to_dataframe(game, username):
    """Expand one Chess.com game record into the rows used by the analyzer."""
    pgn_text = game.get("pgn")
    if not isinstance(pgn_text, str) or not pgn_text.strip():
        raise RuntimeError("The selected game does not contain PGN move data.")

    parsed = chess.pgn.read_game(io.StringIO(pgn_text))
    if parsed is None:
        raise RuntimeError("Chess.com returned PGN that could not be parsed.")

    headers = parsed.headers
    board = parsed.board()
    game_id = str(game.get("uuid") or game.get("url") or headers.get("Link") or "")
    game_url = str(game.get("url") or headers.get("Link") or "")
    white = str((game.get("white") or {}).get("username") or headers.get("White") or "")
    black = str((game.get("black") or {}).get("username") or headers.get("Black") or "")
    target = username.casefold()
    player_color = "white" if white.casefold() == target else (
        "black" if black.casefold() == target else ""
    )

    end_time = game.get("end_time")
    try:
        end_time_utc = datetime.fromtimestamp(
            int(end_time), tz=timezone.utc
        ).isoformat()
    except (TypeError, ValueError, OSError):
        end_time_utc = ""

    rows = []
    for ply, node in enumerate(parsed.mainline(), start=1):
        move = node.move
        if move is None:
            continue
        color = "white" if board.turn == chess.WHITE else "black"
        row = {
            "game_id": game_id,
            "game_url": game_url,
            "game_end_time_utc": end_time_utc,
            "game_date": headers.get("UTCDate") or headers.get("Date") or "",
            "time_class": game.get("time_class", ""),
            "time_control": game.get("time_control", ""),
            "white_username": white,
            "black_username": black,
            "player_color": player_color,
            "ply": ply,
            "move_number": board.fullmove_number,
            "color": color,
            "san": board.san(move),
            "uci": board.uci(move),
            "clock_seconds": pgn_clock_seconds(node),
            "seconds_spent": None,
            "fen_before": board.fen(),
        }
        board.push(move)
        row["fen_after"] = board.fen()
        rows.append(row)

    if not rows:
        raise RuntimeError("The selected game contains no analyzable moves.")
    add_seconds_spent(rows, game.get("time_control", ""))
    return pd.DataFrame(rows)



def parse_increment_seconds(time_control):
    """Return increment seconds from Chess.com time_control, if present."""
    if not isinstance(time_control, str):
        return None
    match = re.search(r"\+(\d+)", time_control)
    return float(match.group(1)) if match else 0.0


def add_seconds_spent(rows, time_control):
    """Fill seconds_spent from per-color clock readings, tolerating gaps."""
    increment = parse_increment_seconds(time_control)
    previous = {"white": None, "black": None}
    base = None
    if isinstance(time_control, str):
        match = re.match(r"^(\d+)(?:\+\d+)?$", time_control)
        if match:
            base = float(match.group(1))
    for row in rows:
        clk = row.get("clock_seconds")
        color = row.get("color")
        spent = None
        if clk is not None and increment is not None and color in previous:
            prev = previous[color] if previous[color] is not None else base
            if prev is not None:
                spent = max(0.0, prev - float(clk) + increment)
            previous[color] = float(clk)
        row["seconds_spent"] = spent


def fetch_chesscom_game(username, game_id=None):
    """Fetch a selected completed game, or the user's most recent one."""
    username = username.strip()
    archives_data = chesscom_get_json(
        f"{CHESSCOM_API_ROOT}/player/{username}/games/archives", username
    )
    archives = archives_data.get("archives", [])
    if not isinstance(archives, list) or not archives:
        raise RuntimeError(f"No completed games found for Chess.com user {username!r}.")

    # Search newest months first. This makes the default case a single archive call
    # and makes recent explicit game IDs fast while still supporting old games.
    for archive_url in reversed(archives):
        archive_data = chesscom_get_json(str(archive_url), username)
        games = archive_data.get("games", [])
        if not isinstance(games, list):
            continue
        candidates = [game for game in games if isinstance(game, dict)]
        if game_id is not None:
            for game in reversed(candidates):
                if game_matches_id(game, game_id):
                    return game_to_dataframe(game, username)
        elif candidates:
            def end_time_key(game):
                try:
                    return int(game.get("end_time") or 0)
                except (TypeError, ValueError):
                    return 0

            latest = max(candidates, key=end_time_key)
            return game_to_dataframe(latest, username)

    if game_id is None:
        raise RuntimeError(f"No completed games found for Chess.com user {username!r}.")
    raise RuntimeError(
        f"Game ID {game_id!r} was not found in {username!r}'s Chess.com archives."
    )

# ----------------------------------------------------------------------------
# Win probability model
# ----------------------------------------------------------------------------

def cp_to_winprob(cp, mate=None):
    """Convert a White-POV evaluation to Lichess Win%."""
    if mate is not None:
        cp = 1000 if mate > 0 else -1000
    elif cp is None:
        cp = 0

    cp = max(-1000, min(1000, cp))
    return 50.0 + 50.0 * (
        2.0 / (1.0 + math.exp(-0.00368208 * cp)) - 1.0
    )

def score_to_parts(score: chess.engine.PovScore):
    """Return (cp, mate) from White's perspective."""
    white = score.white()
    if white.is_mate():
        return None, white.mate()
    return white.score(), None


def fmt_eval(cp, mate):
    if mate is not None:
        return f"M{mate}" if mate > 0 else f"-M{abs(mate)}"
    if cp is None:
        # Both unset means the position was never scored. Formatting that as
        # +0.00 would put a fabricated evaluation into the report and the
        # puzzle record; an empty string is the honest rendering.
        return ""
    return f"{cp/100:+.2f}"


# ----------------------------------------------------------------------------
# Data classes
# ----------------------------------------------------------------------------

@dataclass
class MoveAnalysis:
    ply: int
    move_number: int
    color: str                    # 'white' or 'black'
    san: str
    uci: str
    fen_before: str
    fen_after: str
    eval_before_cp: object = None
    eval_before_mate: object = None
    eval_after_cp: object = None
    eval_after_mate: object = None
    best_move_san: str = ""
    best_move_uci: str = ""
    candidates: list = field(default_factory=list)   # [(san, cp, mate, wp)]
    pv_san: str = ""              # best continuation from position before move
    cp_loss: object = None        # from mover's perspective, cp
    wp_loss: float = 0.0          # win-probability loss for the mover, 0..100
    classification: str = "good"
    error_type: str = ""          # legacy: tactical/deep tactic/positional
    error_category: str = ""      # missed_tactic/allowed_tactic/attention/positional/opening/endgame
    puzzle_prompt_type: str = ""  # best_move/refutation
    puzzle_prompt: str = ""
    best_second_wp_gap: object = None
    only_move: bool = False
    crossed: str = ""             # 'winning->equal', 'equal->losing', etc.
    missed_mate: bool = False
    findable: str = ""            # 'obvious', 'moderate', 'hard'
    depth_to_find: object = None  # honest mode: shallowest depth engine prefers best
    notes: list = field(default_factory=list)
    clock_seconds: object = None
    seconds_spent: object = None
    refute_depth: object = None
    pre_error_bucket: str = ""
    sacrifice: object = None       # dict from classify_sacrifice, or None
    refute_threshold_used: object = None   # per-move bar, scales with wp_loss
    refutation_uci: str = ""      # opponent's punishing reply, allowed_tactic only
    refutation_san: str = ""
    puzzle_reject: str = ""       # which gate rejected this error, "" if eligible

    def wp_before_mover(self):
        wp = cp_to_winprob(self.eval_before_cp or 0, self.eval_before_mate)
        return wp if self.color == "white" else 100 - wp

    def wp_after_mover(self):
        wp = cp_to_winprob(self.eval_after_cp or 0, self.eval_after_mate)
        return wp if self.color == "white" else 100 - wp


# ----------------------------------------------------------------------------
# Opening book (lichess ECO tsv -> EPD map)
# ----------------------------------------------------------------------------

def load_opening_book(tsv_dir):
    book = {}
    for letter in "abcde":
        path = os.path.join(tsv_dir, f"{letter}.tsv")
        if not os.path.exists(path):
            continue
        df = pd.read_csv(path, sep="\t")
        for _, row in df.iterrows():
            board = chess.Board()
            try:
                for tok in row["pgn"].split():
                    if tok.endswith("."):
                        continue
                    board.push_san(tok)
            except ValueError:
                continue
            book[board.epd()] = (row["eco"], row["name"])
    return book


def identify_opening(moves, book):
    """Return (eco, name, last_book_ply, deviation_ply)."""
    board = chess.Board()
    last = (None, None, 0)
    in_book_until = 0
    for i, m in enumerate(moves, start=1):
        board.push_uci(m.uci)
        hit = book.get(board.epd())
        if hit:
            last = (hit[0], hit[1], i)
            in_book_until = i
    deviation = in_book_until + 1 if in_book_until < len(moves) else None
    return last[0], last[1], last[2], deviation


# ----------------------------------------------------------------------------
# Position interpretation heuristics
# ----------------------------------------------------------------------------

def hanging_pieces(board, color):
    """Pieces of `color` that are attacked and either undefended or attacked
    by a cheaper piece. Returns [(square_name, piece_symbol)]."""
    out = []
    for sq, piece in board.piece_map().items():
        if piece.color != color or piece.piece_type == chess.KING:
            continue
        attackers = board.attackers(not color, sq)
        if not attackers:
            continue
        defenders = board.attackers(color, sq)
        cheapest_attacker = min(
            PIECE_VALUES[board.piece_at(a).piece_type] for a in attackers)
        if not defenders or cheapest_attacker < PIECE_VALUES[piece.piece_type]:
            out.append((chess.square_name(sq), chess.piece_name(piece.piece_type)))
    return out


def good_captures_available(board):
    """Captures with non-negative static exchange for the side to move."""
    caps = []
    for mv in board.legal_moves:
        if board.is_capture(mv):
            victim = board.piece_at(mv.to_square)
            vval = PIECE_VALUES[victim.piece_type] if victim else 1  # en passant
            attacker = board.piece_at(mv.from_square)
            # crude SEE: is the capture square defended after capture?
            board.push(mv)
            recapturers = board.attackers(board.turn, mv.to_square)
            board.pop()
            aval = PIECE_VALUES[attacker.piece_type]
            gain = vval if not recapturers else vval - aval
            if gain > 0:
                caps.append((board.san(mv), gain))
    return sorted(caps, key=lambda x: -x[1])


def king_attackers(board, color):
    """Number of enemy pieces attacking squares adjacent to `color`'s king."""
    ksq = board.king(color)
    if ksq is None:
        return 0
    zone = chess.SquareSet(chess.BB_KING_ATTACKS[ksq]) | {ksq}
    n = 0
    for sq in zone:
        n += len(board.attackers(not color, sq))
    return n


def passed_pawns(board, color):
    out = []
    for sq in board.pieces(chess.PAWN, color):
        f, r = chess.square_file(sq), chess.square_rank(sq)
        blocked = False
        for df in (-1, 0, 1):
            nf = f + df
            if not 0 <= nf <= 7:
                continue
            ranks = range(r + 1, 8) if color == chess.WHITE else range(0, r)
            for nr in ranks:
                p = board.piece_at(chess.square(nf, nr))
                if p and p.piece_type == chess.PAWN and p.color != color:
                    blocked = True
        if not blocked:
            out.append(chess.square_name(sq))
    return out


def material_balance(board):
    """Positive = White ahead, in pawns."""
    total = 0
    for sq, piece in board.piece_map().items():
        v = PIECE_VALUES[piece.piece_type]
        total += v if piece.color == chess.WHITE else -v
    return total


def is_en_prise(board, square, owner):
    """The piece on `square` is already losing itself: undefended, or attacked
    by something cheaper than it."""
    piece = board.piece_at(square)
    if piece is None:
        return False
    attackers = board.attackers(not owner, square)
    if not attackers:
        return False
    defenders = board.attackers(owner, square)
    values = [PIECE_VALUES[board.piece_at(a).piece_type] for a in attackers
              if board.piece_at(a) is not None]
    if not values:
        return False
    return (not defenders) or min(values) < PIECE_VALUES[piece.piece_type]


def material_profile(board_before, pv, color):
    """Material shape of the engine's main line, from `color`'s side.

    Everything is in pawns, relative to the material balance before the first
    PV move. `trough` is the deepest deficit reached, `final` is where the
    line ends up.
    """
    sign = 1 if color == "white" else -1
    start = sign * material_balance(board_before)
    board = board_before.copy()
    trough = 0.0
    trough_ply = None
    final = 0.0
    plies = 0
    for i, move in enumerate(pv or []):
        if move not in board.legal_moves:
            break                      # truncated or stale PV; use what we have
        board.push(move)
        plies += 1
        diff = sign * material_balance(board) - start
        if diff < trough:
            trough, trough_ply = diff, i
        final = diff
    mates = board.is_checkmate() and board.turn != (color == "white")
    return {"trough": round(trough, 2), "trough_ply": trough_ply,
            "final": round(final, 2), "plies": plies, "mates": mates}


def classify_sacrifice(board_before, best_move, pv, color):
    """Describe the sacrifice in the engine's best line, or None.

    `kind` is the field that decides whether this can ever be a puzzle:
      "sham"  material returns by force, or the line mates. Gradable.
      "real"  compensation is positional and never resolves. Not gradable.

    See the SAC_ constants for why that distinction is doing the work.
    """
    profile = material_profile(board_before, pv, color)
    # A short PV normally cannot show whether material returns, so it is not
    # judgeable either way. The exception is a line that mates: mate is the
    # strongest possible compensation, and a forced mate in two produces a
    # three-ply PV that would otherwise be discarded. Byrne-Fischer's queen
    # sac resolves slowly and needs the length gate; Morphy's resolves in
    # mate and must be exempt from it.
    if profile["plies"] < SAC_MIN_PV_PLIES and not profile["mates"]:
        return None
    trough = profile["trough"]
    if trough > -SAC_EXCHANGE_TROUGH:
        return None                     # not enough material offered to count

    us = chess.WHITE if color == "white" else chess.BLACK
    recovered = profile["final"] >= -SAC_RECOVERY_TOLERANCE
    return {
        "trough_pawns": trough,
        "final_pawns": profile["final"],
        "trough_ply": profile["trough_ply"],
        "pv_plies": profile["plies"],
        "size": "piece" if trough <= -SAC_PIECE_TROUGH else "exchange",
        "quiet": not board_before.is_capture(best_move),
        "mates": profile["mates"],
        "recovered": recovered,
        "kind": "sham" if (recovered or profile["mates"]) else "real",
        "desperado": is_en_prise(board_before, best_move.from_square, us),
    }


def sacrifice_is_brilliant(ma, sac):
    """Gate a detected sacrifice into the puzzle category.

    Rejections are recorded rather than dropped, so the report can show what
    was found and refused.
    """
    if sac is None:
        return False, "no_sacrifice"
    if sac["kind"] != "sham":
        return False, "real_sacrifice_not_gradable"
    if sac["desperado"]:
        return False, "desperado"       # the piece was already lost
    if ma.ply <= SAC_MIN_PLY:
        return False, "opening_ply"     # likely book; refined against book_ply
    if ma.findable == ATTENTION_REQUIRES_FINDABLE:
        return False, "obvious"         # a sacrifice you would find anyway
    cp = ma.eval_before_cp
    if cp is not None:
        # eval_before_cp is white-relative, as it comes off score_to_parts.
        # The band is about the sacrificing side, so it has to be flipped for
        # Black or every Black sacrifice from a good position reads as
        # out-of-band on the losing end.
        if ma.color == "black":
            cp = -cp
        if not (SAC_MIN_PRE_EVAL_CP <= cp <= SAC_MAX_PRE_EVAL_CP):
            return False, "eval_out_of_band"
    return True, ""


def demote_book_sacrifices(moves, opening):
    """A gambit is a book pawn sacrifice, not one you found over the board.

    Runs after identify_opening, which is the first point where book_ply
    exists. SAC_MIN_PLY is the coarse guard applied during analysis; this is
    the accurate one.
    """
    if not opening:
        return 0
    _, _, book_ply, _ = opening
    if not book_ply:
        return 0
    demoted = 0
    for m in moves:
        if m.error_category == "brilliant_sacrifice" and m.ply <= book_ply:
            m.error_category = "missed_tactic"
            if isinstance(m.sacrifice, dict):
                m.sacrifice = dict(m.sacrifice, rejected="in_book")
            m.puzzle_prompt_type, m.puzzle_prompt = puzzle_prompt_for(
                m.error_category, m.fen_before, m.san)
            demoted += 1
    return demoted


def detect_motifs(board_before, best_move):
    """Cheap tactical-motif tags for the best move in this position."""
    motifs = []
    b = board_before.copy()
    if b.is_capture(best_move):
        motifs.append("capture")
    if b.gives_check(best_move):
        motifs.append("check")
    b.push(best_move)
    mover_color = board_before.turn
    piece = b.piece_at(best_move.to_square)
    if piece:
        targets = []
        for sq in b.attacks(best_move.to_square):
            t = b.piece_at(sq)
            if t and t.color != mover_color and (
                    PIECE_VALUES[t.piece_type] >= PIECE_VALUES[piece.piece_type]
                    or t.piece_type == chess.KING):
                targets.append(t)
        if len(targets) >= 2:
            motifs.append("fork")
    hang = hanging_pieces(b, not mover_color)
    if hang and "capture" not in motifs:
        motifs.append("creates threat on " + ", ".join(s for s, _ in hang[:2]))
    return motifs


def pv_is_forcing(board_before, pv, plies=6, threshold=0.5):
    """True if at least `threshold` of the first `plies` moves of the engine's
    principal variation are checks or captures.

    The one-ply signals below cannot see a combination that only crystallizes
    several moves in: the refutation starts with a quiet move and the tactic
    lands later. Such errors get tagged positional purely because the shape at
    ply one is quiet. Walking the PV catches them.
    """
    if not pv:
        return False
    b = board_before.copy()
    forcing = 0
    counted = 0
    for mv in pv[:plies]:
        if mv not in b.legal_moves:
            break
        if b.is_capture(mv) or b.gives_check(mv):
            forcing += 1
        counted += 1
        b.push(mv)
    return counted > 0 and (forcing / counted) >= threshold


def classify_error_type(board_before, played_move, best_move, wp_loss, pv=None):
    """Tactical vs positional, heuristic.

    Returns 'tactical', 'deep tactic', or 'positional'. 'deep tactic' means
    the one-ply signals were all quiet but the engine's own continuation is
    forcing, which is the signature of a combination missed several moves out
    rather than a judgment error.
    """
    b = board_before.copy()
    tactical_signals = 0
    if b.is_capture(best_move) or b.gives_check(best_move):
        tactical_signals += 1
    if best_move.promotion:
        tactical_signals += 1
    b2 = board_before.copy()
    b2.push(played_move)
    if hanging_pieces(b2, not b2.turn):        # mover just left something hanging
        tactical_signals += 1
    if good_captures_available(board_before):  # there was a capture on offer
        tactical_signals += 1
    if tactical_signals >= 1 and wp_loss >= 10:
        return "tactical"
    if wp_loss >= 25 and pv_is_forcing(board_before, pv):
        return "deep tactic"
    return "positional"



def piece_count(board):
    return sum(1 for piece in board.piece_map().values()
               if piece.piece_type != chess.KING)


def candidate_wp_gap_for_mover(candidates, color):
    if len(candidates) < 2:
        return None
    w1, w2 = candidates[0][3], candidates[1][3]
    return (w1 - w2) if color == "white" else (w2 - w1)


def classify_error_category(ma, board_before, best_move, after_info, best_pv=None):
    """Classify an error for puzzle routing and metrics.

    Requires `ma.findable` to be populated before it is called, since the
    attention branch tests it.

    Also records the opponent's punishing reply on `ma` when the category is
    allowed_tactic. That move is the answer to an allowed_tactic prompt, and
    the previous version computed it and threw it away, which left the study
    card with nothing correct to reveal.
    """
    # Measure first, route second. Computing the sacrifice inside the branch
    # that routes to it meant any sacrifice in a position that routed to
    # `endgame` or `attention` was never detected at all, and vanished from
    # the report rather than being listed and refused.
    brilliant = False
    if best_pv:
        ma.sacrifice = classify_sacrifice(board_before, best_move, best_pv, ma.color)
        brilliant, why = sacrifice_is_brilliant(ma, ma.sacrifice)
        if not brilliant and ma.sacrifice is not None:
            ma.sacrifice = dict(ma.sacrifice, rejected=why)

    if (isinstance(ma.refute_depth, int)
            and ma.refute_depth <= ATTENTION_REFUTE_MAX
            and ma.findable == ATTENTION_REQUIRES_FINDABLE):
        return "attention"
    if brilliant:
        return "brilliant_sacrifice"
    if piece_count(board_before) <= 7:
        return "endgame"
    if ma.error_type in ("tactical", "deep tactic"):
        # A quiet key move with a forcing follow-up is the best puzzle material
        # there is. Requiring the best move itself to be a capture or check
        # excluded exactly that class and dumped it into `positional`.
        quiet_but_tactical = (
            pv_is_forcing(board_before, best_pv)
            or any(mv not in ("capture", "check")
                   for mv in detect_motifs(board_before, best_move))
        )
        if (board_before.is_capture(best_move)
                or board_before.gives_check(best_move)
                or ma.error_type == "deep tactic"
                or quiet_but_tactical):
            return "missed_tactic"
    if after_info and after_info[0].get("pv"):
        after_board = chess.Board(ma.fen_after)
        opp_refutation = after_info[0]["pv"][0]
        if (after_board.is_capture(opp_refutation) or
                after_board.gives_check(opp_refutation) or
                pv_is_forcing(after_board, after_info[0].get("pv"))):
            ma.refutation_uci = opp_refutation.uci()
            try:
                ma.refutation_san = after_board.san(opp_refutation)
            except (ValueError, AssertionError):
                ma.refutation_san = ""
            return "allowed_tactic"
    if ma.ply <= 20:
        return "opening"
    return "positional"


def puzzle_prompt_for(category, fen, played_san):
    """Prompt text, in the same frame as the FEN that gets stored.

    The stored position is `fen_before`, i.e. before the played move. The old
    allowed_tactic wording said "position after my move", so prompt and board
    disagreed by a ply and the solver was looking at the wrong side of the
    move they were being asked about.
    """
    if category == "allowed_tactic":
        return ("refutation",
                f"You want to play {played_san}. What is wrong with it?")
    if category == "endgame":
        return ("best_move", "Find the best move, and name the method.")
    if category == "brilliant_sacrifice":
        # Deliberately the same wording as missed_tactic. Announcing the
        # sacrifice supplies the hard half of the problem.
        return ("best_move", "Find the best move in this position.")
    return ("best_move", "Find the best move in this position.")

def findability(board_before, best_move):
    """Heuristic mode: how realistic was it to find the best move?"""
    b = board_before.copy()
    if b.is_capture(best_move) or b.gives_check(best_move):
        return "obvious"        # forcing move: checks and captures first
    from_piece = b.piece_at(best_move.from_square)
    if from_piece and b.attackers(not b.turn, best_move.from_square):
        return "moderate"       # saving an attacked piece
    return "hard"               # quiet move


def depth_to_find(engine, board, best_move, cap=14, restore_threads=None):
    """Honest mode: the shallowest search depth at which the engine's top
    choice is best_move and stays best_move for STABLE_RUN consecutive
    depths.

    Three things this has to get right, all of which are easy to get wrong:

    1. Threads must be 1. Under Lazy SMP, `go depth d` returns when the MAIN
       thread finishes depth d, while helper threads have been searching
       deeper in parallel and sharing their results through the transposition
       table. With Threads > 1, nominal depth stops corresponding to search
       depth and a "depth 1" probe can be answered with depth-15 knowledge.
       This is the difference between measuring findability and measuring
       your CPU's core count.
    2. The hash must actually be cleared. The deep main-pass analysis of this
       same position is still in the TT; if the clear fails, the root entry
       hands the deep best move to the depth-1 probe. A failed clear
       invalidates the measurement, so it returns None rather than a number.
    3. Agreement must be stable. First-match semantics record a preference
       that appears at depth d and vanishes at d + 1.

    Returns:
      int                  measured depth, MEASUREMENT_FLOOR < d <= cap
      DEPTH_CENSORED_LOW   stably preferred at or below the floor
      DEPTH_CENSORED_HIGH  never stably preferred within cap
      None                 measurement invalid (hash clear failed)

    restore_threads: Threads value to restore afterwards, since the main
    analysis pass runs multithreaded. Pass the value used in analyze_game.
    """
    engine.configure({"Threads": 1})
    try:
        engine.configure({"Clear Hash": None})
    except chess.engine.EngineError:
        if restore_threads:
            engine.configure({"Threads": restore_threads})
        return None

    try:
        # One iterative-deepening search, reading the PV at each iteration,
        # instead of one fresh search per rung.
        #
        # Two reasons, and the second matters more than the first:
        #  - Speed. N separate `go depth d` calls each redo iterative
        #    deepening from 1, so the per-rung ladder costs several times a
        #    single search. Measured 2.7x on a depth-20 ladder.
        #  - Correctness. Between rungs the transposition table carries over,
        #    so rung d is answered partly from tables built by rungs 1..d-1,
        #    each of which ran its own full deepening. That is a milder form
        #    of the leak the Threads fix addressed, and it is not small: on a
        #    test position the per-rung ladder reported stable agreement from
        #    depth 5 while a clean single pass reported depth 9.
        agree = [False] * cap
        with engine.analysis(board, chess.engine.Limit(depth=cap)) as an:
            for info in an:
                d = info.get("depth")
                pv = info.get("pv")
                if d and 1 <= d <= cap and pv:
                    agree[d - 1] = (pv[0] == best_move)

        result = DEPTH_CENSORED_HIGH
        for d in range(1, cap + 1):
            run = agree[d - 1: min(d - 1 + STABLE_RUN, cap)]
            if run and all(run):
                result = d
                break

        if isinstance(result, int) and result <= MEASUREMENT_FLOOR:
            return DEPTH_CENSORED_LOW
        return result
    finally:
        if restore_threads:
            engine.configure({"Threads": restore_threads})



def eval_for_move(engine, board, move, depth):
    info = engine.analyse(board, chess.engine.Limit(depth=depth), root_moves=[move])
    return score_to_parts(info["score"])


def mover_winprob_from_eval(cp, mate, color):
    wp = cp_to_winprob(cp or 0, mate)
    return wp if color == "white" else 100.0 - wp


def _wp_by_depth(engine, board, color, cap, root_moves=None):
    """One iterative-deepening pass; mover-relative WP at each iteration.

    Returns a list of length `cap`, entries None where no info arrived.
    Returns None if the hash could not be cleared, which invalidates the
    measurement rather than silently answering from the previous pass.
    """
    try:
        engine.configure({"Clear Hash": None})
    except chess.engine.EngineError:
        return None
    out = [None] * cap
    kwargs = {"root_moves": root_moves} if root_moves else {}
    with engine.analysis(board, chess.engine.Limit(depth=cap), **kwargs) as an:
        for info in an:
            d = info.get("depth")
            score = info.get("score")
            if d and 1 <= d <= cap and score is not None:
                cp, mate = score_to_parts(score)
                out[d - 1] = mover_winprob_from_eval(cp, mate, color)
    return out


def refute_depth(engine, board, played_move, color,
                 threshold, cap=REFUTE_DEPTH_CAP,
                 restore_threads=None):
    """Shallowest depth at which the played move is already visibly losing at
    least `threshold` WP points, and stays that way for STABLE_RUN consecutive
    depths.

    This function previously violated both of the correctness requirements
    that depth_to_find's docstring spells out, twenty lines above it:

    1. First-match semantics. It returned the first depth where the loss
       crossed the bar, with no stability requirement, so a crossing that
       appeared at depth d and vanished at d + 1 was recorded as the answer.
    2. Transposition-table carryover. It cleared the hash once and then ran a
       fresh `engine.analyse` per rung inside that single clear, so rung d was
       answered partly from tables built by rungs 1..d-1. depth_to_find
       measured that same leak as reporting depth 5 where a clean pass
       reported 9.

    Both biases point downward. Errors were being assigned depths shallower
    than they deserved, which routed them into `attention` and under the
    puzzle floor of PUZZLE_REFUTE_MIN. The empty puzzle file was partly
    manufactured by the measurement.

    The fix mirrors depth_to_find: Threads = 1 so nominal depth means search
    depth, one iterative-deepening pass per side of the comparison with a
    hash clear between them, and a stable run before a depth counts.

    Unlike depth_to_find, a run that would extend past the cap is not
    accepted short. A crossing first seen at cap - 1 is not evidence of a
    stable crossing, and treating it as one would reintroduce the first-match
    problem at the top of the ladder.

    `threshold` is required rather than defaulted, because the right bar
    depends on the size of the error being measured. A flat bar asks a harder
    question of small errors than large ones: an inaccuracy loses under 10 WP
    by definition, so a 10-point bar could only be crossed by shallow-search
    noise and the whole band censored high. Use refute_threshold_for.

    Returns:
      int                        measured depth, 1 <= d <= cap
      REFUTE_DEPTH_CENSORED_HIGH never stably crossed within cap
      None                       measurement invalid (hash clear failed)
    """
    engine.configure({"Threads": 1})
    try:
        best_wp = _wp_by_depth(engine, board, color, cap)
        if best_wp is None:
            return None
        played_wp = _wp_by_depth(engine, board, color, cap,
                                 root_moves=[played_move])
        if played_wp is None:
            return None

        crossed = [
            best_wp[i] is not None and played_wp[i] is not None
            and (best_wp[i] - played_wp[i]) >= threshold
            for i in range(cap)
        ]
        for d in range(1, cap - STABLE_RUN + 2):
            if all(crossed[d - 1: d - 1 + STABLE_RUN]):
                return d
        return REFUTE_DEPTH_CENSORED_HIGH
    finally:
        if restore_threads:
            engine.configure({"Threads": restore_threads})


def pre_error_bucket(move):
    wp = move.wp_before_mover()
    if wp >= 65:
        return "winning"
    if wp <= 35:
        return "losing"
    return "balanced"


def findability_from_depth(d, cap=14):
    """Map a possibly-censored depth measurement to a coaching label."""
    if d is None:
        return "unmeasured"
    if d == DEPTH_CENSORED_LOW:
        return "obvious"
    if d == DEPTH_CENSORED_HIGH:
        return "beyond analysis depth"
    if d <= 10:
        return "moderate"
    if d <= 20:
        return "hard"
    return "outside human range"


# ----------------------------------------------------------------------------
# Classification from win probability
# ----------------------------------------------------------------------------

def classify(wp_before, wp_after, played_is_best, missed_mate, dead_position):
    loss = max(0.0, wp_before - wp_after)

    if played_is_best:
        return "best"

    if missed_mate:
        return "blunder" if loss >= 10 else "mistake"

    if loss <= 2:
        return "excellent"

    if dead_position and loss < 20:
        # Both sides remain in an already-decided position.
        return "good"

    if loss >= 20:
        return "blunder"
    if loss >= 10:
        return "mistake"
    if loss >= 5:
        return "inaccuracy"

    return "good"


def crossing(wp_before, wp_after):
    def band(wp):
        if wp >= 65: return "winning"
        if wp <= 35: return "losing"
        return "equal"
    a, b = band(wp_before), band(wp_after)
    return f"{a} -> {b}" if a != b else ""


def lichess_move_accuracy(wp_before, wp_after):
    """Lichess accuracy for one move."""
    if wp_after >= wp_before:
        return 100.0

    loss = wp_before - wp_after
    raw = (
        103.1668100711649
        * math.exp(-0.04354415386753951 * loss)
        - 3.166924740191411
    )

    # Lichess's uncertainty bonus for imperfect engine analysis.
    return max(0.0, min(100.0, raw + 1.0))


def game_accuracy(moves, color):
    """Lichess game accuracy for one color."""
    if not moves:
        return 100.0

    # Lichess uses +0.15 as the standard initial-position evaluation.
    white_wps = [cp_to_winprob(15)]

    for move in moves:
        white_wps.append(
            cp_to_winprob(move.eval_after_cp, move.eval_after_mate)
        )

    # Lichess uses sliding windows of between 2 and 8 positions.
    window_size = max(2, min(8, len(moves) // 10))
    window_size = min(window_size, len(white_wps))

    first_window = white_wps[:window_size]

    # Repeating the first window aligns one volatility weight with every ply.
    windows = [
        first_window
        for _ in range(max(0, window_size - 2))
    ]

    windows.extend(
        white_wps[i:i + window_size]
        for i in range(len(white_wps) - window_size + 1)
    )

    weights = []

    for window in windows:
        mean = sum(window) / len(window)
        variance = sum((value - mean) ** 2 for value in window) / len(window)
        volatility = math.sqrt(variance)

        # Lichess constrains volatility weights to this interval.
        weights.append(max(0.5, min(12.0, volatility)))

    selected = []

    for i, move in enumerate(moves):
        wp_before_white = white_wps[i]
        wp_after_white = white_wps[i + 1]

        if move.color == "white":
            wp_before = wp_before_white
            wp_after = wp_after_white
        else:
            wp_before = 100.0 - wp_before_white
            wp_after = 100.0 - wp_after_white

        accuracy = lichess_move_accuracy(wp_before, wp_after)

        if move.color == color:
            selected.append((accuracy, weights[i]))

    if not selected:
        return 100.0

    weighted_mean = (
        sum(accuracy * weight for accuracy, weight in selected)
        / sum(weight for _, weight in selected)
    )

    accuracies = [accuracy for accuracy, _ in selected]

    if any(accuracy <= 0.0 for accuracy in accuracies):
        harmonic_mean = 0.0
    else:
        harmonic_mean = (
            len(accuracies)
            / sum(1.0 / accuracy for accuracy in accuracies)
        )

    return (weighted_mean + harmonic_mean) / 2.0

# ----------------------------------------------------------------------------
# Engine analysis of one game
# ----------------------------------------------------------------------------

def fmt_dur(seconds):
    s = int(seconds)
    if s < 60:
        return f"{s}s"
    m, s = divmod(s, 60)
    if m < 60:
        return f"{m}m{s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m"


class MinuteProgress:
    """Prints a progress line to stderr once per wall-clock minute.

    Runs on a daemon thread so the heartbeat still fires when a single
    high-depth position blocks the main thread for longer than a minute.
    Phase-aware: the analysis pass and the honest-mode findability pass
    report separately, each with a live ETA from the current phase's rate.
    """

    def __init__(self, interval=60):
        self.interval = interval
        self.phase = "starting"
        self.done = 0
        self.total = 1
        self.start = time.time()
        self.phase_start = self.start
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def set_phase(self, phase, total):
        with self._lock:
            self.phase = phase
            self.total = max(1, total)
            self.done = 0
            self.phase_start = time.time()

    def update(self, done):
        with self._lock:
            self.done = done

    def _run(self):
        while not self._stop.wait(self.interval):
            self._emit()

    def _emit(self):
        with self._lock:
            phase, done, total, pstart = (
                self.phase, self.done, self.total, self.phase_start)
        elapsed = time.time() - self.start
        if done <= 0:
            print(f"  [{fmt_dur(elapsed)}] {phase}: still on item 1/{total}...",
                  file=sys.stderr, flush=True)
            return
        rate = (time.time() - pstart) / done
        eta = (total - done) * rate
        print(f"  [{fmt_dur(elapsed)}] {phase}: {done}/{total} "
              f"({100 * done / total:.0f}%), ~{rate:.1f}s/item, "
              f"ETA {fmt_dur(eta)}", file=sys.stderr, flush=True)

    def close(self):
        self._stop.set()
        self._thread.join(timeout=2)


def analyze_game(game_df, depth=14, multipv=3, progress=True,
                 findability_mode="heuristic", threads=1, hash_mb=256,
                 engine_info=None):
    game_df = game_df.sort_values("ply")
    moves = []
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    # Threads defaults to 1, not to core count. Under Lazy SMP the helper
    # threads race, so a fixed-depth search is not reproducible run to run:
    # evaluations drift by a point or two and rows sitting near a
    # classification threshold appear and disappear between runs. Anything
    # above 1 trades reproducibility for wall time.
    #
    # Hash is pinned for the same reason: table size changes what survives
    # eviction, which changes fixed-depth results.
    n_threads = max(1, int(threads))
    engine.configure({"Threads": n_threads, "Hash": int(hash_mb)})
    # The engine build is part of the measurement. Two Stockfish versions do
    # not agree at the same depth, and an unpinned `apt-get install stockfish`
    # will upgrade underneath you without changing anything in this repo.
    if engine_info is not None:
        engine_info["engine_id"] = engine.id.get("name", "unknown")
        engine_info["threads"] = n_threads
        engine_info["hash_mb"] = int(hash_mb)
    limit = chess.engine.Limit(depth=depth)
    reporter = MinuteProgress() if progress else None
    try:
        rows = list(game_df.itertuples())
        # evaluate every position once; eval_after of ply i = eval_before of ply i+1
        evals = []          # (cp, mate) White POV per fen_before, plus final fen_after
        infos = []          # multipv info per fen_before
        fens = [r.fen_before for r in rows] + [rows[-1].fen_after]
        if reporter:
            reporter.set_phase(f"engine analysis (depth {depth})", len(fens))
        for i, fen in enumerate(fens):
            board = chess.Board(fen)
            if board.is_game_over():
                if board.is_checkmate():
                    mate = -0 if board.turn else 0
                    # side to move is mated
                    cp, m = None, (-1 if board.turn == chess.WHITE else 1) * 0
                    evals.append((None, (1 if board.turn == chess.BLACK else -1) * 1))
                else:
                    evals.append((0, None))
                infos.append(None)
                continue
            info = engine.analyse(board, limit, multipv=multipv)
            infos.append(info)
            cp, mate = score_to_parts(info[0]["score"])
            evals.append((cp, mate))
            if reporter:
                reporter.update(i + 1)

        if reporter:
            reporter.set_phase("interpreting moves", len(rows))
        for i, r in enumerate(rows):
            ma = MoveAnalysis(
                ply=r.ply, move_number=r.move_number, color=r.color,
                san=r.san, uci=r.uci,
                fen_before=r.fen_before, fen_after=r.fen_after,
                clock_seconds=getattr(r, "clock_seconds", None),
                seconds_spent=getattr(r, "seconds_spent", None))
            ma.eval_before_cp, ma.eval_before_mate = evals[i]
            ma.eval_after_cp, ma.eval_after_mate = evals[i + 1]
            board = chess.Board(r.fen_before)
            info = infos[i]
            if info:
                best = info[0]["pv"][0]
                ma.best_move_uci = best.uci()
                ma.best_move_san = board.san(best)
                pv = info[0]["pv"][:6]
                ma.pv_san = chess.Board(r.fen_before).variation_san(pv)
                for line in info:
                    if "pv" not in line or not line["pv"]:
                        continue
                    csan = board.san(line["pv"][0])
                    ccp, cmate = score_to_parts(line["score"])
                    cwp = cp_to_winprob(ccp or 0, cmate)
                    ma.candidates.append((csan, ccp, cmate, cwp))
                # only-move: best clearly better than 2nd best, for the mover
                if len(ma.candidates) >= 2:
                    w1 = ma.candidates[0][3]; w2 = ma.candidates[1][3]
                    gap = candidate_wp_gap_for_mover(ma.candidates, r.color)
                    ma.best_second_wp_gap = None if gap is None else round(gap, 2)
                    ma.only_move = gap is not None and gap >= 15

            wp_b, wp_a = ma.wp_before_mover(), ma.wp_after_mover()
            ma.wp_loss = max(0.0, wp_b - wp_a)
            if ma.eval_before_cp is not None and ma.eval_after_cp is not None:
                sign = 1 if r.color == "white" else -1
                ma.cp_loss = max(0, sign * (ma.eval_before_cp - ma.eval_after_cp))
            ma.missed_mate = (ma.eval_before_mate is not None
                              and ((r.color == "white" and ma.eval_before_mate > 0)
                                   or (r.color == "black" and ma.eval_before_mate < 0))
                              and ma.eval_after_mate is None)
            dead = (wp_b > 95 and wp_a > 95) or (wp_b < 5 and wp_a < 5)
            ma.classification = classify(
                wp_b, wp_a, r.uci == ma.best_move_uci, ma.missed_mate, dead)
            ma.crossed = crossing(wp_b, wp_a)
            if ma.classification in ("inaccuracy", "mistake", "blunder") and info:
                best_mv = chess.Move.from_uci(ma.best_move_uci)
                played_mv = chess.Move.from_uci(r.uci)
                ma.error_type = classify_error_type(
                    board, played_mv, best_mv, ma.wp_loss,
                    pv=info[0].get("pv"))
                ma.pre_error_bucket = pre_error_bucket(ma)
                # Findability is measured before the category is assigned, because
                # the attention branch now needs both halves: a shallow refutation
                # AND an easy replacement move.
                if findability_mode == "honest":
                    ma.depth_to_find = depth_to_find(
                        engine, board, best_mv, cap=depth,
                        restore_threads=n_threads)
                    ma.findable = findability_from_depth(ma.depth_to_find, cap=depth)
                else:
                    ma.findable = findability(board, best_mv)
                ma.refute_threshold_used = refute_threshold_for(ma.wp_loss)
                ma.refute_depth = refute_depth(
                    engine, board, played_mv, ma.color,
                    ma.refute_threshold_used,
                    restore_threads=n_threads)
                ma.error_category = classify_error_category(
                    ma, board, best_mv, infos[i + 1], best_pv=info[0].get("pv"))
                ma.puzzle_prompt_type, ma.puzzle_prompt = puzzle_prompt_for(ma.error_category, ma.fen_before, ma.san)
                # interpretation notes
                b_after = chess.Board(r.fen_after)
                hang = hanging_pieces(b_after, chess.WHITE if r.color == "white" else chess.BLACK)
                if hang:
                    ma.notes.append("left " + ", ".join(
                        f"{p} on {s}" for s, p in hang[:2]) + " insufficiently defended")
                caps = good_captures_available(board)
                if caps and board.is_capture(best_mv):
                    ma.notes.append(f"a favorable capture was available ({caps[0][0]})")
                if board.gives_check(best_mv):
                    ma.notes.append("the best move was a forcing check")
                motifs = detect_motifs(board, best_mv)
                real = [m for m in motifs if m not in ("capture", "check")]
                if real:
                    ma.notes.append("motif: " + "; ".join(real))
                ka_before = king_attackers(board, board.turn)
                ka_after = king_attackers(b_after,
                                          chess.WHITE if r.color == "white" else chess.BLACK)
                if ka_after - ka_before >= 2:
                    ma.notes.append("your king's zone came under heavier attack after this move")
            moves.append(ma)
            if reporter:
                reporter.update(i + 1)
    finally:
        if reporter:
            reporter.close()
        engine.quit()
    return moves


# ----------------------------------------------------------------------------
# Report generation
# ----------------------------------------------------------------------------

def phase_of(ply):
    if ply <= 20: return "opening"
    if ply <= 60: return "middlegame"
    return "endgame"


def build_report(meta, moves, opening, player_color, graph_path=None,
                 analysis_params=None, puzzle_stats=None):
    eco, name, book_ply, deviation_ply = opening
    lines = []
    L = lines.append
    white, black = meta["white_username"], meta["black_username"]
    L(f"# (free, so lmk) Game analysis: {white} vs {black}")
    L("")
    L(f"Date: {meta['game_date']}  |  Time control: {meta['time_class']} "
      f"({meta['time_control']})  |  You played: {player_color}")
    L(f"Game ID: {meta['game_id']}")
    if analysis_params:
        # Provenance, in a form both a human and the collator can read.
        # Without this the collator cannot know the ladder cap, and its depth
        # bin labels silently describe a cap that is no longer in use.
        L(f"Analysis: depth={analysis_params['depth']} "
          f"multipv={analysis_params['multipv']} "
          f"findability={analysis_params['findability']} "
          f"floor={MEASUREMENT_FLOOR} stable_run={STABLE_RUN} "
          f"threads={analysis_params.get('threads', '?')} "
          f"hash_mb={analysis_params.get('hash_mb', '?')} "
          f"deterministic={analysis_params.get('deterministic', False)} "
          f"engine_id={analysis_params.get('engine_id', 'unknown').replace(' ', '_')} "
          f"generated={analysis_params['generated_utc']}")
    if meta.get("game_end_time_utc"):
        L(f"Game end time UTC: {meta['game_end_time_utc']}")
    L(f"Game: {meta['game_url']}")
    L("")

    player_moves = [m for m in moves if m.color == player_color]
    opp_moves = [m for m in moves if m.color != player_color]

    opponent_color = "black" if player_color == "white" else "white"

    acc_player = game_accuracy(moves, player_color)
    acc_opp = game_accuracy(moves, opponent_color)
    L("## Summary")
    L("")
    L(f"- Lichess accuracy: you {acc_player:.1f}%, opponent {acc_opp:.1f}%")
    if name:
        L(f"- Opening: {eco} {name} (theory followed through ply {book_ply})")
    else:
        L("- Opening: not matched in the ECO database")
    if deviation_ply and deviation_ply <= len(moves):
        d = moves[deviation_ply - 1]
        who = "You" if d.color == player_color else "Opponent"
        L(f"- First deviation from theory: ply {d.ply}, {who} played "
          f"{d.move_number}.{'..' if d.color=='black' else ''} {d.san}")
    counts = {}
    for m in player_moves:
        counts[m.classification] = counts.get(m.classification, 0) + 1
    L("- Your moves: " + ", ".join(
        f"{counts.get(k,0)} {k}" for k in ("best", "excellent", "good", "inaccuracy", "mistake", "blunder")))
    L("")
    L("METRICS:\n")
    L("Best: The played move exactly matches Stockfish's top move\n")
    L("Excellent: A non-best move that loses 2 WP points or less.\n")
    L("Good: WP loss is over 2, but under 5 points; also used for losses under 20 when the position remains already decided.\n")
    L("Inaccuracy: WP loss is at least 5 but under 10 points.\n")
    L("Mistake: WP loss is at least 10 but under 20 points; also generally used when a forced mate is missed with under 10 points of WP loss.\n")
    L("Blunder: WP loss is 20 points or more, or a forced mate is missed with at least 10 points of WP loss.\n")
    L("See: https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-etc \n")
    L("(Brillint, Great and Miss are rating subjective)")
    if puzzle_stats:
        L(f"- Puzzles: {puzzle_stats[0]} open, {puzzle_stats[1]} solved")
        tally = puzzle_stats[2] if len(puzzle_stats) > 2 else None
        if tally:
            L("")
            L("### Puzzle gate tally (this game)")
            L("")
            L(f"Gates: category in {list(PUZZLE_CATEGORIES)}, "
              f"refute depth in [{PUZZLE_REFUTE_MIN}, {PUZZLE_REFUTE_MAX}], "
              f"best-vs-second WP gap >= {PUZZLE_WP_GAP_MIN:.0f}. "
              f"Refute bar per move: max({REFUTE_THRESHOLD_FLOOR_WP:.0f}, "
              f"{REFUTE_THRESHOLD_FRACTION:g} x WP loss).")
            L("")
            L("| outcome | errors |")
            L("|---|---|")
            for key in sorted(tally, key=lambda k: (k != "accepted", k)):
                L(f"| {key} | {tally[key]} |")
            L("")
            L("Four gates pass at once or nothing is generated, so a zero here "
              "is a product of four pass rates rather than a fault. Read the "
              "binding gate off this table before changing any threshold.")
            L("")

    sacs = [m for m in player_moves if isinstance(m.sacrifice, dict)]
    if sacs:
        L("### Sacrifices in the engine's line")
        L("")
        L("Real sacrifices are listed but never served as puzzles: compensation "
          "that never resolves back into material has no gradable answer.")
        L("")
        L("| Move | Offered | Kind | Quiet | Line ends | Verdict |")
        L("|---|---|---|---|---|---|")
        for m in sacs:
            sac = m.sacrifice
            ends = ("mate" if sac["mates"]
                    else f"{sac['final_pawns']:+.1f} pawns")
            verdict = sac.get("rejected") or "puzzle"
            L(f"| {m.move_label} | {sac['trough_pawns']:.1f} ({sac['size']}) "
              f"| {sac['kind']} | {'yes' if sac['quiet'] else 'no'} "
              f"| {ends} | {verdict} |")
        L("")
    if graph_path:
        L(f"![Evaluation graph]({os.path.basename(graph_path)})")
        L("")

    # biggest missed opportunity
    missed = [m for m in player_moves
              if m.classification in ("mistake", "blunder") and m.best_move_san]
    if missed:
        big = max(missed, key=lambda m: m.wp_loss)
        L("## Biggest missed opportunity")
        L("")
        L(coach_paragraph(big, player_color))
        L("")

    # critical positions
    criticals = [m for m in moves if m.only_move or m.wp_loss >= 20 or m.missed_mate]
    if criticals:
        L("## Critical positions")
        L("")
        for m in criticals[:8]:
            tag = []
            if m.only_move: tag.append("only-move situation")
            if m.missed_mate: tag.append("forced mate was on the board")
            if m.crossed: tag.append(f"evaluation crossed {m.crossed}")
            who = "you" if m.color == player_color else "opponent"
            L(f"- Ply {m.ply} ({who}), {mv_label(m)}: "
              f"{fmt_eval(m.eval_before_cp, m.eval_before_mate)} -> "
              f"{fmt_eval(m.eval_after_cp, m.eval_after_mate)}"
              + (f" [{'; '.join(tag)}]" if tag else ""))
        L("")

    # move-by-move table for the player's non-good moves
    errors = [m for m in player_moves if m.classification in
              ("inaccuracy", "mistake", "blunder")]
    if errors:
        L("## Your errors, move by move")
        L("")
        L("| Move | Class | Category | WP loss | Refute depth | Seconds spent | Pre-error eval |")
        L("|---|---|---|---:|---|---:|---|")
        for m in errors:
            spent = "" if m.seconds_spent is None or pd.isna(m.seconds_spent) else f"{float(m.seconds_spent):.0f}"
            L(f"| {mv_label(m)} | {m.classification} | {m.error_category or m.error_type or 'unclear'} | "
              f"{m.wp_loss:.0f}% | {m.refute_depth or ''} | {spent} | "
              f"{m.pre_error_bucket or ''} |")
        L("")
        for m in errors:
            L(f"### {mv_label(m)} ({m.classification}, "
              f"{m.error_type or 'unclear'}, wp loss {m.wp_loss:.0f}%)")
            L("")
            L(coach_paragraph(m, player_color))
            L("")

    # full move table
    L("## Full move table")
    L("")
    L("| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |")
    L("|-----|------|-------------|------------|------|---------|---------|-------|")
    for m in moves:
        star = "*" if m.color == player_color else ""
        L(f"| {m.ply} | {mv_label(m)}{star} | "
          f"{fmt_eval(m.eval_before_cp, m.eval_before_mate)} | "
          f"{fmt_eval(m.eval_after_cp, m.eval_after_mate)} | "
          f"{m.best_move_san} | "
          f"{'' if m.cp_loss is None else m.cp_loss} | "
          f"{m.wp_loss:.0f}% | {m.classification} |")
    L("")
    L("Rows marked * are your moves. WP loss is win-probability loss; "
      "it is the primary signal, CP loss is shown for reference.")
    L("")

    # habits
    L("## Patterns in this game")
    L("")
    by_category = {}
    for m in errors:
        by_category[m.error_category or "unclear"] = by_category.get(m.error_category or "unclear", 0) + 1
    attention_rate = 100 * by_category.get("attention", 0) / max(1, len(player_moves))
    L("- Error categories: " + ", ".join(f"{v} {k}" for k, v in sorted(by_category.items())) + ".")
    L(f"- Attention errors per 100 moves: {attention_rate:.1f}.")
    by_bucket = {bucket: sum(1 for m in errors if m.pre_error_bucket == bucket)
                 for bucket in PRE_ERROR_BUCKETS}
    if errors:
        L("- Pre-error eval buckets: " + ", ".join(
            f"{by_bucket[b]} {b}" for b in PRE_ERROR_BUCKETS) + ".")
    by_phase = {}
    for m in errors:
        by_phase.setdefault(phase_of(m.ply), []).append(m)
    for ph, ms in by_phase.items():
        L(f"- {ph.capitalize()}: {len(ms)} error(s) "
          f"(avg wp loss {sum(x.wp_loss for x in ms)/len(ms):.0f}%).")
    tt = [m for m in errors if m.clock_seconds is not None and m.clock_seconds < 60]
    if tt:
        L(f"- {len(tt)} of your errors came with under a minute on the clock.")
    L("")
    return "\n".join(lines)


def mv_label(m):
    dots = "..." if m.color == "black" else "."
    return f"{m.move_number}{dots}{m.san}"


def coach_paragraph(m, player_color):
    """The layer-3 output: explanation, not just engine dump."""
    parts = []
    parts.append(
        f"You played {mv_label(m)}. Stockfish preferred {m.best_move_san}, "
        f"after which the main line runs {m.pv_san}.")
    if m.missed_mate:
        parts.append("There was a forced mate on the board and this move let it slip.")
    if m.crossed:
        parts.append(f"The evaluation crossed from {m.crossed.replace('->', 'to')}, "
                     "which matters more than the raw number.")
    if m.notes:
        parts.append("Why it went wrong: " + "; ".join(m.notes) + ".")
    if m.error_type == "tactical":
        parts.append("Before committing to a quiet move here, the checklist is "
                     "checks, captures, threats, in that order.")
    elif m.error_type == "deep tactic":
        parts.append("Nothing was hanging and no capture was on offer, but the "
                     "engine's continuation is forcing: this was a combination "
                     "landing several moves out, not a judgment error.")
    elif m.error_type == "positional":
        parts.append("This was a judgment error rather than a missed tactic; "
                     "compare the pawn structure and piece activity after both moves.")
    if m.depth_to_find is not None:
        if m.depth_to_find == DEPTH_CENSORED_LOW:
            forcing = ("a forcing move, the kind a checks-and-captures scan "
                       "catches" if m.error_type in ("tactical", "deep tactic")
                       else "a quiet move, but one whose point shows at a glance")
            parts.append(f"The engine prefers this move from at or below depth "
                         f"{MEASUREMENT_FLOOR}, which is as shallow as this "
                         f"measurement resolves; it sits near the surface, {forcing}.")
        elif m.depth_to_find == DEPTH_CENSORED_HIGH:
            parts.append("The engine never settles on this move within the "
                         "analysis depth, so how findable it was is not "
                         "measured here; weigh this one lightly.")
        elif m.findable == "moderate":
            parts.append(f"The engine first prefers this move at depth "
                         f"{m.depth_to_find} and holds it; findable, but it "
                         "takes a deliberate look rather than a scan.")
        elif m.findable == "hard":
            parts.append(f"The engine does not settle on this move until depth "
                         f"{m.depth_to_find}; reachable with real calculation, "
                         "but not on a scan.")
        else:
            parts.append(f"The engine does not settle on this move until depth "
                         f"{m.depth_to_find}, which is outside what a human "
                         "reasonably calculates over the board; this is not a "
                         "training target.")
    elif m.findable == "obvious":
        parts.append("The better move was a forcing move, the kind a "
                     "checks-and-captures scan catches.")
    elif m.findable == "hard":
        parts.append("The engine's choice was a quiet move; missing it is "
                     "forgivable, so weigh this one lightly.")
    if m.candidates and len(m.candidates) >= 2:
        alts = ", ".join(f"{c[0]} ({fmt_eval(c[1], c[2])})" for c in m.candidates[:3])
        parts.append(f"Candidates considered by the engine: {alts}.")
    return " ".join(parts)



def load_puzzles(path):
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data if isinstance(data, list) else data.get("puzzles", [])


def save_puzzles(path, puzzles):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(puzzles, f, indent=2)


def puzzle_attempts(puzzle):
    """Attempt log, migrating the legacy `completed` boolean on read."""
    attempts = puzzle.get("attempts")
    if isinstance(attempts, list) and attempts:
        return attempts
    if puzzle.get("completed"):
        return [{"timestamp": puzzle.get("completed_at"), "found": True}]
    return []


def mark_puzzle_attempt(path, fen, found=True, seconds=None):
    """Append to the attempt log. A boolean cannot distinguish solved-first-try
    from solved-after-three-failures, and the second list is the one worth
    studying."""
    puzzles = load_puzzles(path)
    changed = False
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for puzzle in puzzles:
        if puzzle.get("fen_before") == fen or puzzle.get("fen") == fen:
            attempts = puzzle_attempts(puzzle)
            attempts.append({"timestamp": stamp, "found": bool(found),
                             "seconds": seconds})
            puzzle["attempts"] = attempts
            puzzle.pop("completed", None)       # single schema from here on
            puzzle.pop("completed_at", None)
            changed = True
    save_puzzles(path, puzzles)
    return changed, len(puzzles)


def puzzle_counts(path):
    puzzles = load_puzzles(path)
    solved = sum(1 for p in puzzles
                 if any(a.get("found") for a in puzzle_attempts(p)))
    return len(puzzles) - solved, solved


def puzzle_rejection_reason(m):
    """None if the error becomes a puzzle, else the name of the first gate
    that stopped it.

    Four gates have to pass at once, so the yield per game is a product of
    four pass rates and can sit near zero without anything being broken. The
    tally is what distinguishes an over-tight gate from a broken measurement,
    and those need opposite fixes.
    """
    if m.error_category not in PUZZLE_CATEGORIES:
        return f"category:{m.error_category or 'unclassified'}"
    if m.refute_depth is None:
        return "refute_unmeasured"
    if not isinstance(m.refute_depth, int):
        return "refute_censored_high"
    if m.refute_depth < PUZZLE_REFUTE_MIN:
        return "refute_too_shallow"
    if m.refute_depth > PUZZLE_REFUTE_MAX:
        return "refute_too_deep"
    if m.best_second_wp_gap is None:
        return "wp_gap_unmeasured"
    if m.best_second_wp_gap < PUZZLE_WP_GAP_MIN:
        return "wp_gap_too_small"
    if m.error_category == "allowed_tactic" and not m.refutation_uci:
        return "no_refutation_recorded"
    return None


def puzzle_eligible(m):
    return puzzle_rejection_reason(m) is None


def append_puzzles(path, meta, moves, player_color, generated_utc):
    """Returns (open, solved, tally). The tally counts every error against the
    gate that rejected it, plus `accepted` and `duplicate_fen`."""
    puzzles = load_puzzles(path)
    seen = {p.get("fen_before") or p.get("fen") for p in puzzles}
    tally = {}

    def bump(reason):
        tally[reason] = tally.get(reason, 0) + 1

    for m in moves:
        if m.color != player_color or m.classification not in ("inaccuracy", "mistake", "blunder"):
            continue
        reason = puzzle_rejection_reason(m)
        m.puzzle_reject = reason or ""
        if reason:
            bump(reason)
            continue
        if m.fen_before in seen:
            bump("duplicate_fen")
            m.puzzle_reject = "duplicate_fen"
            continue
        bump("accepted")
        puzzles.append({
            "id": puzzle_id_for(m, meta),
            "fen_before": m.fen_before,
            "move_played": m.uci,
            "move_played_san": m.san,
            "best_move": m.best_move_uci,
            "best_move_san": m.best_move_san,
            "refutation": m.refutation_uci or None,
            "refutation_san": m.refutation_san or None,
            "puzzle_type": m.error_category,
            "category": m.error_category,          # back-compat
            "prompt_type": m.puzzle_prompt_type,
            "prompt": m.puzzle_prompt,
            "best_second_wp_gap": m.best_second_wp_gap,
            "refute_depth": m.refute_depth,
            "wp_loss": round(m.wp_loss, 1),
            "eval_before": fmt_eval(m.eval_before_cp, m.eval_before_mate),
            "pre_error_bucket": m.pre_error_bucket,
            "sacrifice": m.sacrifice,
            "attempts": [],
            "source_game": meta.get("game_url") or meta.get("game_id", ""),
            "move_number": m.move_number,
            "date_generated": generated_utc,
        })
        seen.add(m.fen_before)
    save_puzzles(path, puzzles)
    open_count, solved = puzzle_counts(path)
    return open_count, solved, tally


def puzzle_id_for(m, meta):
    """Stable id. Index selectors shift on every append and dedupe."""
    seed = f"{meta.get('game_id', '')}|{m.fen_before}"
    return "p" + hashlib.sha1(seed.encode("utf-8")).hexdigest()[:10]


def write_sidecar(path, meta, moves, player_color, analysis_params,
                  puzzle_tally=None):
    """Emit a machine-readable sidecar next to the markdown report.

    The collator previously recovered its numbers by regexing the coaching
    prose. That coupled the data pipeline to sentence wording: any phrasing
    change silently dropped rows, and censored measurements (which have no
    number in the prose at all) were dropped entirely, biasing the dataset
    toward findable errors. Structured output removes that whole class of bug.

    depth_to_find is written as-is, so the censoring sentinels survive as
    strings rather than being coerced to integers that look measured.
    """
    errors = []
    for m in moves:
        if m.color != player_color:
            continue
        if m.classification not in ("inaccuracy", "mistake", "blunder"):
            continue
        errors.append({
            "ply": m.ply,
            "move_number": m.move_number,
            "color": m.color,
            "san": m.san,
            "move_label": f"{m.move_number}{'...' if m.color == 'black' else '.'}{m.san}",
            "classification": m.classification,
            "error_type": m.error_type or "unclear",
            "error_category": m.error_category or "",
            "wp_loss": round(m.wp_loss, 2),
            "cp_loss": m.cp_loss,
            "depth_to_find": m.depth_to_find,
            "refute_depth": m.refute_depth,
            "refute_threshold_wp": (None if m.refute_threshold_used is None
                                    else round(m.refute_threshold_used, 2)),
            "refutation": m.refutation_uci or None,
            "sacrifice": m.sacrifice,
            "puzzle_reject": m.puzzle_reject or None,
            "findable": m.findable,
            "seconds_spent": None if m.seconds_spent is None or pd.isna(m.seconds_spent) else round(float(m.seconds_spent), 2),
            "pre_error_eval": fmt_eval(m.eval_before_cp, m.eval_before_mate),
            "pre_error_bucket": m.pre_error_bucket,
            "fen_before": m.fen_before,
            "uci": m.uci,
            "best_move_san": m.best_move_san,
            "best_move_uci": m.best_move_uci,
            "best_second_wp_gap": m.best_second_wp_gap,
        })
    payload = {
        "schema_version": 2,
        "game_id": meta["game_id"],
        "game_date": meta["game_date"],
        "game_url": meta.get("game_url", ""),
        "white": meta["white_username"],
        "black": meta["black_username"],
        "time_class": meta.get("time_class", ""),
        "player_color": player_color,
        "analysis": {
            "depth": analysis_params["depth"],
            "multipv": analysis_params["multipv"],
            "findability": analysis_params["findability"],
            "measurement_floor": MEASUREMENT_FLOOR,
            "stable_run": STABLE_RUN,
            "refute_threshold_rule": {
                "floor_wp": REFUTE_THRESHOLD_FLOOR_WP,
                "fraction_of_wp_loss": REFUTE_THRESHOLD_FRACTION,
            },
            "refute_depth_cap": REFUTE_DEPTH_CAP,
            "sacrifice_gates": {
                "exchange_trough_pawns": SAC_EXCHANGE_TROUGH,
                "piece_trough_pawns": SAC_PIECE_TROUGH,
                "recovery_tolerance_pawns": SAC_RECOVERY_TOLERANCE,
                "min_pv_plies": SAC_MIN_PV_PLIES,
                "pre_eval_band_cp": [SAC_MIN_PRE_EVAL_CP, SAC_MAX_PRE_EVAL_CP],
                "min_ply": SAC_MIN_PLY,
            },
            "attention_requires": {
                "refute_depth_max": ATTENTION_REFUTE_MAX,
                "findable": ATTENTION_REQUIRES_FINDABLE,
            },
            "puzzle_gates": {
                "categories": list(PUZZLE_CATEGORIES),
                "refute_min": PUZZLE_REFUTE_MIN,
                "refute_max": PUZZLE_REFUTE_MAX,
                "wp_gap_min": PUZZLE_WP_GAP_MIN,
            },
            "censored_low": DEPTH_CENSORED_LOW,
            "censored_high": DEPTH_CENSORED_HIGH,
            "engine": analysis_params.get("engine", "stockfish"),
            "engine_id": analysis_params.get("engine_id", "unknown"),
            "threads": analysis_params.get("threads"),
            "hash_mb": analysis_params.get("hash_mb"),
            "deterministic": analysis_params.get("deterministic", False),
            "generated_utc": analysis_params["generated_utc"],
        },
        "puzzle_gate_tally": puzzle_tally or {},
        "metrics": {
            "player_moves": sum(1 for m in moves if m.color == player_color),
            "attention_errors": sum(1 for m in moves if m.color == player_color and m.error_category == "attention"),
            "attention_errors_per_100_moves": round(
                100 * sum(1 for m in moves if m.color == player_color and m.error_category == "attention") /
                max(1, sum(1 for m in moves if m.color == player_color)), 2),
        },
        # Written even when empty: a game with no errors is a real observation
        # and belongs in the denominator.
        "errors": errors,
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)


def make_graph(moves, path, player_color):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    xs, ys = [], []
    for m in moves:
        wp = cp_to_winprob(m.eval_after_cp or 0, m.eval_after_mate)
        xs.append(m.ply)
        ys.append(wp if player_color == "white" else 100 - wp)  # changed

    fig, (ax, ax_time) = plt.subplots(2, 1, figsize=(10, 5.4), height_ratios=[3, 2])
    ax.plot(xs, ys, lw=1.6)
    ax.axhline(50, color="gray", lw=0.7, ls="--")
    ax.fill_between(xs, 50, ys, where=[y >= 50 for y in ys], alpha=0.15)
    ax.fill_between(xs, ys, 50, where=[y < 50 for y in ys],
                    alpha=0.15, color="tab:red")

    for m in moves:
        if m.classification == "blunder":
            ax.axvline(m.ply, color="red", lw=0.6, alpha=0.5)

    ax.set_xlabel("ply")
    ax.set_ylabel(f"{player_color.title()} win probability %")  # changed
    ax.set_ylim(0, 100)
    ax.set_title("Evaluation (win probability). Red lines mark blunders.")

    errors = [m for m in moves if m.color == player_color and
              m.classification in ("inaccuracy", "mistake", "blunder") and
              m.seconds_spent is not None]
    if errors:
        ax_time.scatter([m.seconds_spent for m in errors], [m.wp_loss for m in errors],
                        s=32, alpha=0.75)
    ax_time.set_xlabel("seconds spent")
    ax_time.set_ylabel("WP loss")
    ax_time.set_title("Error clock use: time spent vs win-probability loss")
    ax_time.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)

# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def pick_game(df, selector):
    selector = selector or "latest"
    games = df.groupby("game_id").agg(
        date=("game_end_time_utc", "first"),
        tc=("time_class", "first")).sort_values("date")
    if selector.startswith("latest"):
        tc = selector.split(":")[1] if ":" in selector else None
        pool = games[games.tc == tc] if tc else games
        if pool.empty:
            raise ValueError(f"No games match selector {selector!r}.")
        return pool.index[-1]
    return selector


def main():
    ap = argparse.ArgumentParser()
    source = ap.add_mutually_exclusive_group(required=False)
    source.add_argument("--username", help="Chess.com username to fetch")
    source.add_argument("--csv", help="existing Chess.com move-history CSV")
    ap.add_argument(
        "--game-id", "--game", dest="game_id",
        help=("Chess.com game UUID, full URL, or URL's numeric ID. With --csv, "
              "latest / latest:rapid / latest:daily are also accepted. If omitted, "
              "the most recent completed game is analyzed."),
    )
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--depth", type=int, default=14)
    ap.add_argument("--multipv", type=int, default=3)
    ap.add_argument("--threads", type=int, default=1,
                    help="engine threads. Default 1, which is required for "
                         "reproducible fixed-depth results: Lazy SMP makes "
                         "multithreaded searches nondeterministic. Raise only "
                         "if you accept that re-analysis will not reproduce.")
    ap.add_argument("--hash-mb", type=int, default=256,
                    help="engine hash in MB. Part of the measurement; "
                         "changing it changes fixed-depth results.")
    ap.add_argument("--findability", choices=["heuristic", "honest"],
                    default="heuristic",
                    help="heuristic: cheap move-shape buckets. honest: measure "
                         "the shallowest depth at which the engine stably "
                         "prefers the best move, single-threaded with a cleared "
                         "hash (adds a search ladder per error; results at or "
                         f"below depth {MEASUREMENT_FLOOR} are reported as "
                         "censored rather than as a number)")
    ap.add_argument("--out", default="report.md")
    ap.add_argument("--graph", default="eval_graph.png")
    ap.add_argument("--perspective", choices=["white", "black", "both"],
                    default="both",
                    help="whose report to write. both (default) writes one file "
                         "per color; the engine analysis runs once and is shared. "
                         "with --out report.md, both mode writes report_white.md "
                         "and report_black.md")
    ap.add_argument("--openings-dir", default="")
    ap.add_argument("--puzzles-file", default="puzzles.json",
                    help=(f"persistent JSON puzzle file for errors with refute "
                          f"depth in [{PUZZLE_REFUTE_MIN}, {PUZZLE_REFUTE_MAX}]"))
    ap.add_argument("--mark-completed", "--mark-solved", dest="mark_completed",
                    metavar="FEN",
                    help="record a successful attempt on a puzzle by FEN and exit")
    ap.add_argument("--mark-missed", metavar="FEN",
                    help="record a failed attempt on a puzzle by FEN and exit")
    ap.add_argument("--attempt-seconds", type=float, default=None,
                    help="seconds taken, stored with --mark-completed/--mark-missed")
    args = ap.parse_args()

    if args.mark_completed or args.mark_missed:
        fen = args.mark_completed or args.mark_missed
        changed, total = mark_puzzle_attempt(
            args.puzzles_file, fen, found=bool(args.mark_completed),
            seconds=args.attempt_seconds)
        open_count, solved_count = puzzle_counts(args.puzzles_file)
        print(f"{'recorded attempt on' if changed else 'no matching'} puzzle; "
              f"{open_count} open, {solved_count} solved, {total} total")
        return

    if not args.username and not args.csv:
        ap.error("one of --username or --csv is required unless "
                 "--mark-completed or --mark-missed is used")

    if args.username:
        args.username = args.username.strip()
        if not args.username:
            ap.error("--username cannot be empty")
        if args.game_id and args.game_id.strip().casefold().startswith("latest"):
            ap.error("latest selectors are only needed with --csv; omit --game-id "
                     "to fetch the user's most recent Chess.com game")
        try:
            df = fetch_chesscom_game(args.username, args.game_id)
        except RuntimeError as exc:
            ap.error(str(exc))
    else:
        df = pd.read_csv(args.csv, dtype={"game_id": str})
        if "seconds_spent" not in df.columns and "clock_seconds" in df.columns:
            rows = df.sort_values("ply").to_dict("records")
            add_seconds_spent(rows, str(rows[0].get("time_control", "")) if rows else "")
            spent = {row.get("ply"): row.get("seconds_spent") for row in rows}
            df["seconds_spent"] = df["ply"].map(spent)

    if args.list:
        g = df.groupby("game_id").agg(
            date=("game_date", "first"), tc=("time_class", "first"),
            white=("white_username", "first"), black=("black_username", "first"),
            plies=("ply", "max")).sort_values("date")
        print(g.to_string())
        return

    # Direct retrieval already reduced the data to the matched game. In
    # particular, a numeric URL-tail selector may differ from Chess.com's UUID,
    # which is the canonical game_id stored in the fetched rows.
    gid = str(df.iloc[0]["game_id"]) if args.username else pick_game(df, args.game_id)
    gdf = df[df.game_id == gid]
    if gdf.empty:
        ap.error(f"Game ID {args.game_id!r} was not found in {args.csv!r}.")
    meta = gdf.iloc[0].to_dict()
    print(f"Analyzing {meta['white_username']} vs {meta['black_username']} "
          f"({meta['game_date']}, {meta['time_class']}), "
          f"{len(gdf)} plies at depth {args.depth}...", file=sys.stderr)

    engine_info = {}
    moves = analyze_game(gdf, depth=args.depth, multipv=args.multipv,
                         findability_mode=args.findability,
                         threads=args.threads, hash_mb=args.hash_mb,
                         engine_info=engine_info)
    analysis_params = {
        "depth": args.depth,
        "multipv": args.multipv,
        "findability": args.findability,
        "engine": os.path.basename(STOCKFISH_PATH),
        # Everything below is required to reproduce a row. Without the engine
        # build and thread count recorded, "same depth" is not the same
        # measurement across runs.
        "engine_id": engine_info.get("engine_id", "unknown"),
        "threads": engine_info.get("threads", args.threads),
        "hash_mb": engine_info.get("hash_mb", args.hash_mb),
        "deterministic": engine_info.get("threads", args.threads) == 1,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    book = load_opening_book(args.openings_dir)
    opening = identify_opening(moves, book)
    demoted = demote_book_sacrifices(moves, opening)
    if demoted:
        print(f"Demoted {demoted} book sacrifice(s) to missed_tactic",
              file=sys.stderr)
    colors = ["white", "black"] if args.perspective == "both" else [args.perspective]
    for color in colors:
        if args.perspective == "both":
            base, ext = os.path.splitext(args.out)
            out_path = f"{base}_{color}{ext}"

            graph_base, graph_ext = os.path.splitext(args.graph)
            graph_path = f"{graph_base}_{color}{graph_ext}"
        else:
            out_path = args.out
            graph_path = args.graph

        make_graph(moves, graph_path, color)

        puzzle_stats = append_puzzles(args.puzzles_file, meta, moves, color,
                                      analysis_params["generated_utc"])
        report = build_report(
            meta, moves, opening, color, graph_path=graph_path,
            analysis_params=analysis_params, puzzle_stats=puzzle_stats
        )
        with open(out_path, "w") as f:
            f.write(report)
        sidecar_path = os.path.splitext(out_path)[0] + ".json"
        write_sidecar(sidecar_path, meta, moves, color, analysis_params,
                      puzzle_tally=puzzle_stats[2])
        tally = puzzle_stats[2]
        if tally:
            print(f"Puzzle gates ({color}): " + ", ".join(
                f"{k}={v}" for k, v in sorted(
                    tally.items(), key=lambda kv: (kv[0] != "accepted", kv[0]))),
                  file=sys.stderr)
        else:
            print(f"Puzzle gates ({color}): no errors to evaluate",
                  file=sys.stderr)
        print(f"Report ({color}) written to {out_path}", file=sys.stderr)
        print(f"Sidecar ({color}) written to {sidecar_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
