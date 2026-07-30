#!/usr/bin/env python3
"""Build the dependency-free data file used by the GitHub Pages opening explorer."""

from __future__ import annotations

import csv
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_RE = re.compile(r"\|\s*(\d+)\s*\|\s*([^|*]+)\*?\s*\|[^|]*\|\s*([^|]+)")


def initial_board():
    rows = ["rnbqkbnr", "pppppppp", "8", "8", "8", "8", "PPPPPPPP", "RNBQKBNR"]
    board = {}
    for rank, row in zip(range(8, 0, -1), rows):
        file = 0
        for char in row:
            if char.isdigit():
                file += int(char)
            else:
                board[f"abcdefgh"[file] + str(rank)] = char
                file += 1
    return board


def path_clear(board, source, target):
    sf, sr = ord(source[0]), int(source[1]); tf, tr = ord(target[0]), int(target[1])
    df = (tf > sf) - (tf < sf); dr = (tr > sr) - (tr < sr)
    sf += df; sr += dr
    while (sf, sr) != (tf, tr):
        if chr(sf) + str(sr) in board:
            return False
        sf += df; sr += dr
    return True


def apply_san(board, san, white):
    """Apply ordinary opening SAN and return UCI (sufficient for the ECO corpus)."""
    san = re.sub(r"[+#?!]", "", san.strip()).replace("0", "O")
    if san in ("O-O", "O-O-O"):
        rank = "1" if white else "8"
        source = "e" + rank; target = ("g" if san == "O-O" else "c") + rank
        rook_from = ("h" if san == "O-O" else "a") + rank
        rook_to = ("f" if san == "O-O" else "d") + rank
        board[target] = board.pop(source); board[rook_to] = board.pop(rook_from)
        return source + target
    match = re.match(r"(?P<piece>[KQRBN])?(?P<hint>[a-h1-8]{0,2})x?(?P<to>[a-h][1-8])(?:=(?P<promo>[QRBN]))?", san)
    if not match:
        raise ValueError(f"Unsupported SAN: {san}")
    piece = match["piece"] or "P"; wanted = piece if white else piece.lower()
    target, hint = match["to"], match["hint"]
    tf, tr = ord(target[0]), int(target[1])
    candidates = []
    for source, value in board.items():
        if value != wanted or any(c not in source for c in hint):
            continue
        sf, sr = ord(source[0]), int(source[1]); df, dr = abs(tf-sf), abs(tr-sr)
        ok = ((piece == "P" and df == 0 and target not in board and dr in (1, 2)) or
              (piece == "P" and df == 1 and dr == 1 and (target in board or hint)) or
              (piece == "N" and (df, dr) in ((1, 2), (2, 1))) or
              (piece == "B" and df == dr and path_clear(board, source, target)) or
              (piece == "R" and (df == 0 or dr == 0) and path_clear(board, source, target)) or
              (piece == "Q" and (df == dr or df == 0 or dr == 0) and path_clear(board, source, target)) or
              (piece == "K" and max(df, dr) == 1))
        if ok and (piece != "P" or (tr > sr) == white):
            candidates.append(source)
    if not candidates:
        raise ValueError(f"Cannot place {san}")
    source = candidates[0]
    # En passant and double-pawn ambiguity are resolved by the SAN file hint.
    if piece == "P" and target not in board and source[0] != target[0]:
        board.pop(target[0] + source[1], None)
    board[target] = board.pop(source)
    if match["promo"]:
        board[target] = match["promo"] if white else match["promo"].lower()
    return source + target + (match["promo"] or "").lower()


def parse_pgn_moves(text):
    return [token for token in re.sub(r"\d+\.(?:\.\.)?", " ", text).split()
            if token not in ("1-0", "0-1", "1/2-1/2")]


def theory_prefixes():
    prefixes, names = set(), {}
    for path in ROOT.glob("[a-e].tsv"):
        with path.open() as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                moves = parse_pgn_moves(row["pgn"])
                key = " ".join(moves)
                prefixes.add(key); names[key] = f'{row["eco"]} · {row["name"]}'
    return prefixes, names


def probability(cp):
    try:
        value = float(cp)
    except ValueError:
        return 100.0 if "+M" in cp else 0.0 if "-M" in cp else 50.0
    return round(100 / (1 + math.exp(-0.00368208 * value * 100)), 1)


def build():
    theory, opening_names = theory_prefixes(); games = []
    for path in sorted((ROOT / "reports").rglob("*_white.md")):
        text = path.read_text(errors="replace")
        header = re.search(r"# .*Game analysis: (.+?) vs (.+)\n", text)
        date = re.search(r"Date:\s*(\d{4}\.\d{2}\.\d{2})", text)
        game_id = re.search(r"Game ID:\s*(\S+)", text)
        if not (header and date and game_id): continue
        rows = []
        in_table = False
        for line in text.splitlines():
            if line.startswith("## Full move table"): in_table = True
            elif in_table and line.startswith("## "): break
            if not in_table: continue
            m = REPORT_RE.match(line)
            if m and not line.startswith("|-----"):
                san = re.sub(r"^\d+\.(?:\.\.)?", "", m.group(2)).strip()
                rows.append((san, m.group(3).strip()))
        board = initial_board(); positions = [] ; sans = []; failed = False
        for ply, (san, eval_after) in enumerate(rows, 1):
            try: uci = apply_san(board, san, ply % 2 == 1)
            except ValueError: failed = True; break
            sans.append(san); key = " ".join(sans)
            positions.append({"san": san, "uci": uci, "board": dict(board), "turn": "black" if ply % 2 else "white",
                              "whiteWin": probability(eval_after), "book": key in theory,
                              "opening": opening_names.get(key)})
            if key not in theory: break
        if positions and not failed:
            games.append({"id": game_id.group(1), "date": date.group(1).replace(".", "-"),
                          "white": header.group(1), "black": header.group(2), "moves": positions})
    return {"generatedFrom": "reports/**/*.md", "games": games}


if __name__ == "__main__":
    target = ROOT / "docs" / "openings-data.js"; target.parent.mkdir(exist_ok=True)
    target.write_text("window.OPENING_DATA = " + json.dumps(build(), separators=(",", ":")) + ";\n")
    print(f"Wrote {target.relative_to(ROOT)}")
