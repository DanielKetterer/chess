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
            "fen_before": board.fen(),
        }
        board.push(move)
        row["fen_after"] = board.fen()
        rows.append(row)

    if not rows:
        raise RuntimeError("The selected game contains no analyzable moves.")
    return pd.DataFrame(rows)


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
    """Convert an evaluation (White's perspective) to White's win probability 0..100.
    Uses the lichess logistic model. Mate scores map to ~0/100."""
    if mate is not None:
        return 100.0 if mate > 0 else 0.0
    cp = max(-1000, min(1000, cp))
    return 50.0 + 50.0 * (2.0 / (1.0 + math.exp(-0.00368208 * cp)) - 1.0)


def score_to_parts(score: chess.engine.PovScore):
    """Return (cp, mate) from White's perspective."""
    white = score.white()
    if white.is_mate():
        return None, white.mate()
    return white.score(), None


def fmt_eval(cp, mate):
    if mate is not None:
        return f"M{mate}" if mate > 0 else f"-M{abs(mate)}"
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
    error_type: str = ""          # 'tactical' | 'positional' | ''
    only_move: bool = False
    crossed: str = ""             # 'winning->equal', 'equal->losing', etc.
    missed_mate: bool = False
    findable: str = ""            # 'obvious', 'moderate', 'hard'
    depth_to_find: object = None  # honest mode: shallowest depth engine prefers best
    notes: list = field(default_factory=list)
    clock_seconds: object = None

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


def classify_error_type(board_before, played_move, best_move, wp_loss):
    """Tactical vs positional, heuristic."""
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
    return "positional"


def findability(board_before, best_move):
    """Heuristic mode: how realistic was it to find the best move?"""
    b = board_before.copy()
    if b.is_capture(best_move) or b.gives_check(best_move):
        return "obvious"        # forcing move: checks and captures first
    from_piece = b.piece_at(best_move.from_square)
    if from_piece and b.attackers(not b.turn, best_move.from_square):
        return "moderate"       # saving an attacked piece
    return "hard"               # quiet move


def depth_to_find(engine, board, best_move, cap=14):
    """Honest mode: the shallowest search depth at which the engine's top
    choice is best_move. Hash is cleared first so the earlier deep search of
    this same position cannot leak into the shallow ladder. Returns cap + 1
    if the move is only preferred at the full analysis depth."""
    try:
        engine.configure({"Clear Hash": None})
    except Exception:
        pass
    for d in range(1, cap + 1):
        info = engine.analyse(board, chess.engine.Limit(depth=d))
        pv = info.get("pv")
        if pv and pv[0] == best_move:
            return d
    return cap + 1


def findability_from_depth(d, cap=14):
    if d <= 5:
        return "obvious"
    if d <= 10:
        return "moderate"
    return "hard"


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


def game_accuracy(wp_losses):
    """Lichess-style accuracy from per-move win-probability losses."""
    if not wp_losses:
        return 100.0
    accs = [max(0.0, min(100.0,
            103.1668 * math.exp(-0.04354 * loss) - 3.1669)) for loss in wp_losses]
    return sum(accs) / len(accs)


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
                 findability_mode="heuristic"):
    game_df = game_df.sort_values("ply")
    moves = []
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    engine.configure({"Threads": max(1, os.cpu_count() - 1), "Hash": 256})
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
                clock_seconds=getattr(r, "clock_seconds", None))
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
                    gap = (w1 - w2) if r.color == "white" else (w2 - w1)
                    ma.only_move = gap >= 15

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
                ma.error_type = classify_error_type(board, played_mv, best_mv, ma.wp_loss)
                if findability_mode == "honest":
                    ma.depth_to_find = depth_to_find(engine, board, best_mv, cap=depth)
                    ma.findable = findability_from_depth(ma.depth_to_find, cap=depth)
                else:
                    ma.findable = findability(board, best_mv)
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


def build_report(meta, moves, opening, player_color, graph_path=None):
    eco, name, book_ply, deviation_ply = opening
    lines = []
    L = lines.append
    white, black = meta["white_username"], meta["black_username"]
    L(f"# (free, so lmk) Game analysis: {white} vs {black}")
    L("")
    L(f"Date: {meta['game_date']}  |  Time control: {meta['time_class']} "
      f"({meta['time_control']})  |  You played: {player_color}")
    L(f"Game: {meta['game_url']}")
    L("")

    player_moves = [m for m in moves if m.color == player_color]
    opp_moves = [m for m in moves if m.color != player_color]
    acc_player = game_accuracy([m.wp_loss for m in player_moves])
    acc_opp = game_accuracy([m.wp_loss for m in opp_moves])

    L("## Summary")
    L("")
    L(f"- Accuracy: you {acc_player:.1f}%, opponent {acc_opp:.1f}%")
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
    tact = sum(1 for m in errors if m.error_type == "tactical")
    pos = sum(1 for m in errors if m.error_type == "positional")
    L(f"- Error mix: {tact} tactical, {pos} positional.")
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
    elif m.error_type == "positional":
        parts.append("This was a judgment error rather than a missed tactic; "
                     "compare the pawn structure and piece activity after both moves.")
    if m.depth_to_find is not None:
        if m.findable == "obvious":
            forcing = ("a forcing move, the kind a checks-and-captures scan "
                       "catches" if m.error_type == "tactical"
                       else "a quiet move, but one whose point shows at a glance")
            parts.append(f"The engine prefers this move from search depth "
                         f"{m.depth_to_find}; it sits near the surface, {forcing}.")
        elif m.findable == "moderate":
            parts.append(f"The engine first prefers this move at depth "
                         f"{m.depth_to_find}; findable, but it takes a "
                         "deliberate look rather than a scan.")
        else:
            parts.append(f"The engine does not prefer this move until depth "
                         f"{m.depth_to_find}; missing it is forgivable, so "
                         "weigh this one lightly.")
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


def make_graph(moves, path, player_color):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    xs, ys = [], []
    for m in moves:
        wp = cp_to_winprob(m.eval_after_cp or 0, m.eval_after_mate)
        xs.append(m.ply)
        ys.append(wp if player_color == "white" else 100 - wp)  # changed

    fig, ax = plt.subplots(figsize=(10, 3.4))
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
    source = ap.add_mutually_exclusive_group(required=True)
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
    ap.add_argument("--findability", choices=["heuristic", "honest"],
                    default="heuristic",
                    help="heuristic: cheap move-shape buckets. honest: measure "
                         "the shallowest depth at which the engine prefers the "
                         "best move (adds a shallow search ladder per error)")
    ap.add_argument("--out", default="report.md")
    ap.add_argument("--graph", default="eval_graph.png")
    ap.add_argument("--perspective", choices=["white", "black", "both"],
                    default="both",
                    help="whose report to write. both (default) writes one file "
                         "per color; the engine analysis runs once and is shared. "
                         "with --out report.md, both mode writes report_white.md "
                         "and report_black.md")
    ap.add_argument("--openings-dir", default="")
    args = ap.parse_args()

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

    moves = analyze_game(gdf, depth=args.depth, multipv=args.multipv,
                         findability_mode=args.findability)
    book = load_opening_book(args.openings_dir)
    opening = identify_opening(moves, book)
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
    
        report = build_report(
            meta, moves, opening, color, graph_path=graph_path
        )
        with open(out_path, "w") as f:
            f.write(report)
        print(f"Report ({color}) written to {out_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
