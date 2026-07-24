#!/usr/bin/env python3
"""Render one puzzle from puzzles.json as a Markdown study card.

Selection is driven by the attempt log rather than a completed flag:
puzzles failed repeatedly come first, then puzzles due for review, then
unattempted ones. Board rendering uses python-chess SVG when available and
falls back to an ASCII board that survives dark mode.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import chess
    import chess.svg
    HAVE_CHESS = True
except ImportError:  # renderer still works, minus SVG, SAN, and mirroring
    chess = None
    HAVE_CHESS = False

PIECES = "pnbrqkPNBRQK"
REVIEW_INTERVALS_DAYS = [7, 30, 90]
RETRY_AFTER_FAILURE_DAYS = 1
KNOWN_TYPES = {"missed_tactic", "allowed_tactic", "endgame"}


# --------------------------------------------------------------------------
# loading and validation
# --------------------------------------------------------------------------

def load_puzzles(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    puzzles = data if isinstance(data, list) else data.get("puzzles", [])
    if not puzzles:
        raise SystemExit(f"No puzzles found in {path}")
    return puzzles


def validate_placement(placement, context=""):
    """Reject malformed boards loudly. A card that renders plausibly but
    wrongly is worse than one that crashes."""
    ranks = placement.split("/")
    if len(ranks) != 8:
        raise SystemExit(f"Malformed FEN {context}: {len(ranks)} ranks, expected 8")
    for i, rank in enumerate(ranks):
        count = 0
        for ch in rank:
            if ch.isdigit():
                count += int(ch)
            elif ch in PIECES:
                count += 1
            else:
                raise SystemExit(f"Malformed FEN {context}: bad character {ch!r}")
        if count != 8:
            raise SystemExit(
                f"Malformed FEN {context}: rank {8 - i} has {count} files, expected 8"
            )
    return ranks


def puzzle_id(puzzle):
    """Stable identity. Index selectors shift on every append and dedupe."""
    if puzzle.get("id"):
        return str(puzzle["id"])
    seed = original_fen(puzzle)
    return "p" + hashlib.sha1(seed.encode("utf-8")).hexdigest()[:10]


def original_fen(puzzle):
    fen = puzzle.get("fen_before") or puzzle.get("fen")
    if not fen:
        raise SystemExit(f"Puzzle {puzzle.get('id', '?')} has no FEN")
    return fen


# --------------------------------------------------------------------------
# attempt log
# --------------------------------------------------------------------------

def attempts_of(puzzle):
    attempts = puzzle.get("attempts")
    if isinstance(attempts, list):
        return attempts
    if puzzle.get("completed"):  # legacy schema
        return [{"timestamp": puzzle.get("completed_at"), "found": True}]
    return []


def parse_ts(value):
    if not value:
        return None
    try:
        stamp = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp


def status_of(attempts):
    if not attempts:
        return "unattempted"
    failures = sum(1 for a in attempts if not a.get("found"))
    if failures >= 2 and not attempts[-1].get("found"):
        return "failed_repeatedly"
    if failures:
        return "solved_after_failure"
    return "solved_first_try"


def due_at(attempts):
    """None means eligible now."""
    if not attempts:
        return None
    last = parse_ts(attempts[-1].get("timestamp"))
    if last is None:
        return None
    if not attempts[-1].get("found"):
        return last + timedelta(days=RETRY_AFTER_FAILURE_DAYS)
    streak = 0
    for attempt in reversed(attempts):
        if not attempt.get("found"):
            break
        streak += 1
    idx = min(streak - 1, len(REVIEW_INTERVALS_DAYS) - 1)
    return last + timedelta(days=REVIEW_INTERVALS_DAYS[idx])


def priority_of(puzzle, now):
    """Lower sorts first. 99 means not due."""
    attempts = attempts_of(puzzle)
    status = status_of(attempts)
    due = due_at(attempts)
    overdue = due is None or now >= due
    if not overdue:
        return 99
    if status == "failed_repeatedly":
        return 0
    if status == "unattempted":
        return 2
    return 1


def select_puzzle(puzzles, selector, include_all, now):
    if selector:
        for puzzle in puzzles:
            if selector in (puzzle_id(puzzle), puzzle.get("id"), original_fen(puzzle)):
                return puzzle
        raise SystemExit(f"No puzzle matched selector {selector!r}")

    ranked = sorted(
        ((priority_of(p, now), parse_ts_sort(p), p) for p in puzzles),
        key=lambda row: (row[0], row[1]),
    )
    if not include_all:
        ranked = [row for row in ranked if row[0] < 99]
    if not ranked:
        raise SystemExit("Nothing due for review. Pass --any to render anyway.")
    return ranked[0][2]


def parse_ts_sort(puzzle):
    """Oldest activity first within a priority band."""
    attempts = attempts_of(puzzle)
    if not attempts:
        return datetime.min.replace(tzinfo=timezone.utc)
    return parse_ts(attempts[-1].get("timestamp")) or datetime.min.replace(
        tzinfo=timezone.utc
    )


def queue_summary(puzzles, now):
    counts = {}
    for puzzle in puzzles:
        key = status_of(attempts_of(puzzle))
        counts[key] = counts.get(key, 0) + 1
    due = sum(1 for p in puzzles if priority_of(p, now) < 99)
    parts = [f"{k}={v}" for k, v in sorted(counts.items())]
    return f"queue: {due} due | " + " ".join(parts)


# --------------------------------------------------------------------------
# board rendering
# --------------------------------------------------------------------------

def side_to_move(fen):
    fields = fen.split()
    return fields[1] if len(fields) > 1 and fields[1] in ("w", "b") else "w"


def ascii_board(fen, orientation_white=True):
    """FEN letters, not Unicode glyphs. U+2654-2659 render hollow and
    U+265A-265F render filled, so on a dark background the two colors read
    backwards. Uppercase is white, lowercase is black, always."""
    ranks = validate_placement(fen.split()[0])
    rows = []
    for idx, rank in enumerate(ranks):
        cells = []
        for ch in rank:
            cells.extend(["."] * int(ch) if ch.isdigit() else [ch])
        rows.append((8 - idx, cells))
    if not orientation_white:
        rows = [(num, list(reversed(cells))) for num, cells in reversed(rows)]
    files = "a b c d e f g h" if orientation_white else "h g f e d c b a"
    lines = [f"    {files}"]
    for num, cells in rows:
        lines.append(f"  {num} " + " ".join(cells) + f" {num}")
    lines.append(f"    {files}")
    return "```\n" + "\n".join(lines) + "\n```"


def svg_board(fen, orientation_white, out_path, size=420):
    if not HAVE_CHESS:
        return None
    board = chess.Board(fen)
    svg = chess.svg.board(
        board,
        orientation=chess.WHITE if orientation_white else chess.BLACK,
        size=size,
        coordinates=True,
        check=board.king(board.turn) if board.is_check() else None,
    )
    out_path.write_text(svg, encoding="utf-8")
    return out_path


# --------------------------------------------------------------------------
# moves and mirroring
# --------------------------------------------------------------------------

def parse_move(board, text):
    if not text or not HAVE_CHESS:
        return None
    try:
        return board.parse_san(str(text))
    except ValueError:
        pass
    try:
        move = chess.Move.from_uci(str(text))
    except ValueError:
        return None
    return move if move in board.legal_moves else None


def mirror_move(move):
    return chess.Move(
        chess.square_mirror(move.from_square),
        chess.square_mirror(move.to_square),
        promotion=move.promotion,
    )


def describe(board, move, raw):
    """SAN plus UCI when we can parse it, raw string when we cannot."""
    if move is None:
        return f"`{raw}`" if raw else "_not recorded_"
    return f"`{board.san(move)}` ({move.uci()})"


def build_frame(puzzle, want_mirror):
    """Returns (display_fen, moves_dict, mirrored_bool).

    The board, the printed FEN, and the answer all come from the same frame.
    Anything grading a submitted move has to read the frame marker in the
    card, or it will score a correct move as wrong.
    """
    fen = original_fen(puzzle)
    validate_placement(fen.split()[0], context="(fen_before)")

    if puzzle.get("fen_display"):
        display = puzzle["fen_display"]
        validate_placement(display.split()[0], context="(fen_display)")
        return display, dict(puzzle), bool(puzzle.get("mirrored"))

    mirrored = want_mirror or bool(puzzle.get("mirrored"))
    if not mirrored:
        return fen, dict(puzzle), False
    if not HAVE_CHESS:
        raise SystemExit("Mirroring needs python-chess. Install it or drop --mirror.")

    board = chess.Board(fen)
    played = parse_move(board, puzzle.get("move_played"))
    best = parse_move(board, puzzle.get("best_move"))
    refutation = None
    if played is not None and puzzle.get("refutation"):
        after = board.copy()
        after.push(played)
        refutation = parse_move(after, puzzle["refutation"])

    flipped = board.mirror()
    moves = dict(puzzle)
    if played is not None:
        moves["move_played"] = flipped.san(mirror_move(played))
    if best is not None:
        moves["best_move"] = flipped.san(mirror_move(best))
    if refutation is not None:
        after_flipped = flipped.copy()
        after_flipped.push(mirror_move(played))
        moves["refutation"] = after_flipped.san(mirror_move(refutation))
    return flipped.fen(), moves, True


# --------------------------------------------------------------------------
# card text
# --------------------------------------------------------------------------

def prompt_text(puzzle, fields, fen):
    ptype = puzzle.get("puzzle_type") or puzzle.get("type")
    if ptype not in KNOWN_TYPES:
        raise SystemExit(
            f"Puzzle {puzzle_id(puzzle)} has puzzle_type {ptype!r}; "
            f"expected one of {sorted(KNOWN_TYPES)}. "
            "No default prompt is used, because the wrong one leaks the answer."
        )
    side = "White" if side_to_move(fen) == "w" else "Black"
    if ptype == "missed_tactic":
        return ptype, f"**{side} to move.** Find the best move."
    if ptype == "endgame":
        return ptype, f"**{side} to move.** Find the best move, and name the method."
    played = fields.get("move_played")
    if not played:
        raise SystemExit(
            f"Puzzle {puzzle_id(puzzle)} is allowed_tactic but has no move_played; "
            "the intended move is the whole prompt for this class."
        )
    return ptype, (
        f"**{side} to move.** You want to play **{played}**. "
        "What is wrong with it?"
    )


def answer_block(ptype, fields, fen):
    lines = ["<details><summary>Answer</summary>", ""]
    board = chess.Board(fen) if HAVE_CHESS else None

    if ptype == "allowed_tactic":
        played_raw = fields.get("move_played")
        played = parse_move(board, played_raw) if board else None
        refutation_raw = fields.get("refutation")
        if not refutation_raw:
            lines += [
                "> No refutation recorded for this puzzle. The generator stores "
                "`best_move` as the move you should have played instead, which is "
                "not the answer to this prompt. Regenerate with a `refutation` field.",
                "",
            ]
            if fields.get("best_move"):
                lines += [f"Better move instead of {played_raw}: `{fields['best_move']}`", ""]
        else:
            after = None
            if board is not None and played is not None:
                after = board.copy()
                after.push(played)
            if after is not None:
                shown = describe(after, parse_move(after, refutation_raw), refutation_raw)
            else:
                shown = f"`{refutation_raw}`"
            lines += [f"After **{played_raw}**, the refutation is {shown}.", ""]
            if fields.get("best_move"):
                best = fields["best_move"]
                shown_best = (describe(board, parse_move(board, best), best)
                              if board is not None else f"`{best}`")
                lines += [f"Play instead: {shown_best}", ""]
    else:
        best_raw = fields.get("best_move")
        shown = (describe(board, parse_move(board, best_raw), best_raw)
                 if board is not None else f"`{best_raw}`")
        lines += [f"Best move: {shown}", ""]
        if fields.get("move_played"):
            lines += [f"You played: `{fields['move_played']}`", ""]

    for label, key in (
        ("Eval before", "eval_before"),
        ("Win probability lost", "wp_loss"),
        ("Refute depth", "refute_depth"),
    ):
        if fields.get(key) is not None:
            lines.append(f"{label}: {fields[key]}")
    if any(fields.get(k) is not None for k in ("eval_before", "wp_loss", "refute_depth")):
        lines.append("")

    source = fields.get("source_game") or fields.get("game")
    if source:
        move_no = fields.get("move_number")
        suffix = f", move {move_no}" if move_no else ""
        lines += [f"Source: {source}{suffix}", ""]
    lines += ["</details>", ""]
    return lines


def render(puzzle, fields, fen, mirrored, out_path, svg_path):
    pid = puzzle_id(puzzle)
    orientation_white = side_to_move(fen) == "w"
    ptype, prompt = prompt_text(puzzle, fields, fen)
    attempts = attempts_of(puzzle)

    lines = [
        f"# Puzzle {pid}",
        "",
        f"<!-- puzzle-id: {pid} | frame: {'mirrored' if mirrored else 'original'} "
        f"| fen: {fen} | type: {ptype} -->",
        "",
        prompt,
        "",
    ]

    if svg_board(fen, orientation_white, svg_path):
        lines += [f"![board]({svg_path.name})", ""]
    lines += [
        ascii_board(fen, orientation_white),
        "",
        f"Board is drawn from {'White' if orientation_white else 'Black'}'s side. "
        "Uppercase is White, lowercase is Black.",
        "",
        f"FEN: `{fen}`",
        "",
    ]
    if mirrored:
        lines += [
            "> This position is color-flipped from the original game. Submit your "
            "move in this frame, not the game's.",
            "",
        ]
    lines += [
        f"Status: {status_of(attempts)} | attempts: {len(attempts)}",
        "",
    ]
    lines += answer_block(ptype, fields, fen)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--puzzles-file", default="puzzles.json")
    ap.add_argument("--selector", help="puzzle id or FEN; default is the top of the review queue")
    ap.add_argument("--out", default="puzzle.md")
    ap.add_argument("--mirror", action="store_true", help="color-flip the position")
    ap.add_argument("--any", dest="include_all", action="store_true",
                    help="ignore the review schedule")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    puzzles = load_puzzles(args.puzzles_file)
    puzzle = select_puzzle(puzzles, args.selector, args.include_all, now)

    fen, fields, mirrored = build_frame(puzzle, args.mirror)
    out_path = Path(args.out)
    svg_path = out_path.with_suffix(".svg")
    render(puzzle, fields, fen, mirrored, out_path, svg_path)

    print(out_path)
    if not HAVE_CHESS:
        print("note: python-chess not installed; SVG, SAN, and mirroring disabled")
    print(queue_summary(puzzles, now))


if __name__ == "__main__":
    main()
