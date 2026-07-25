#!/usr/bin/env python3
"""Append an attempt to a puzzle using the shared attempt-log schema."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--puzzles-file", default="puzzles.json")
    parser.add_argument("--fen", required=True)
    parser.add_argument("--move", default="")
    parser.add_argument(
        "--result",
        choices=["correct", "incorrect", "completed"],
        default="completed",
    )
    return parser.parse_args()


def mark_attempt(path, fen, move="", result="completed", now=None):
    """Record an attempt and return True when *fen* matched a puzzle.

    ``timestamp``/``found`` is the canonical schema consumed by the renderer
    and analyzer.  The former utility wrote ``attempted_utc``/``result`` and a
    ``completed`` flag, which made its successful attempts look like failures
    everywhere else in the pipeline.
    """
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    puzzles = data if isinstance(data, list) else data.get("puzzles", [])
    stamp = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")

    for puzzle in puzzles:
        if puzzle.get("fen_before") != fen and puzzle.get("fen") != fen:
            continue
        attempt = {"timestamp": stamp, "found": result != "incorrect"}
        if move:
            attempt["move"] = move
        puzzle.setdefault("attempts", []).append(attempt)
        # Once an attempt log exists it is the sole source of completion state.
        puzzle.pop("completed", None)
        puzzle.pop("completed_at", None)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        return True
    return False


def main():
    args = parse_args()
    if not mark_attempt(args.puzzles_file, args.fen, args.move, args.result):
        raise SystemExit("no matching puzzle")
    print("updated")


if __name__ == "__main__":
    main()
