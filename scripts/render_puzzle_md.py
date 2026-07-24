#!/usr/bin/env python3
"""Render one puzzle from puzzles.json as a Markdown study card."""
import argparse
import json
from pathlib import Path


UNICODE = {
    "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
    "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚",
}


def load_puzzles(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("puzzles", [])


def board_markdown(fen):
    placement = fen.split()[0]
    rows = placement.split("/")
    lines = ["|  | a | b | c | d | e | f | g | h |", "|---|---|---|---|---|---|---|---|---|"]
    for idx, row in enumerate(rows):
        cells = []
        for ch in row:
            if ch.isdigit():
                cells.extend([" "] * int(ch))
            else:
                cells.append(UNICODE.get(ch, " "))
        cells = (cells + [" "] * 8)[:8]
        lines.append(f"| {8 - idx} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def select_puzzle(puzzles, selector):
    if selector is None:
        return next((p for p in puzzles if not p.get("completed")), puzzles[0] if puzzles else None)
    if selector.isdigit():
        return puzzles[int(selector)]
    for p in puzzles:
        if p.get("fen_before") == selector or p.get("fen") == selector:
            return p
    raise SystemExit(f"No puzzle matched selector {selector!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puzzles-file", default="puzzles.json")
    ap.add_argument("--selector", help="0-based index or FEN; default is first open puzzle")
    ap.add_argument("--out", default="puzzle.md")
    args = ap.parse_args()
    puzzle = select_puzzle(load_puzzles(args.puzzles_file), args.selector)
    if not puzzle:
        raise SystemExit("No puzzles found")
    fen = puzzle.get("fen_before") or puzzle.get("fen")
    lines = ["# Chess puzzle", "", puzzle.get("prompt", "Find the best move in this position."), "",
             board_markdown(fen), "", f"FEN: `{fen}`", "", "<details><summary>Answer</summary>", "",
             f"Best move: `{puzzle.get('best_move', '')}`", "", "</details>", ""]
    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    print(args.out)


if __name__ == "__main__":
    main()
