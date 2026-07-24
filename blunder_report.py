"""Collate timestamped chess analysis reports into a blunder trend report."""

import argparse
import csv
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

MISTAKE_THRESHOLD = 5.0
BLUNDER_THRESHOLD = 10.0
DEPTH_BINS = [(1, 6), (7, 12), (13, 20), (21, 30)]
DEPTH_COLORS = ["#d1495b", "#edae49", "#4c8577", "#30638e"]
DEPTH_LABELS = [
    "1-6  (should have seen it)",
    "7-12 (reachable)",
    "13-20 (hard)",
    "21-30 (outside human range)",
]

ERROR_HEADING_RE = re.compile(
    r"^###\s+(?P<label>(?P<move_number>\d+)\.{1,3}[^\n(:]+?)\s*"
    r"(?:\(|:|[-–—])\s*"
    r"(?P<classification>inaccuracy|mistake|blunder)\s*[,;|/ -]+\s*"
    r"(?P<error_type>tactical|positional|unclear)\s*[,;|/ -]+\s*"
    r"(?:wp|win[- ]probability)\s*loss\s*:?\s*(?P<wp_loss>[\d.]+)\s*(?:%|pp|points?)?",
    re.IGNORECASE | re.MULTILINE,
)
DEPTH_RE = re.compile(
    r"(?:engine (?:first prefers|prefers|does not prefer) this move "
    r"(?:from |at |until )?(?:search )?depth|depth(?: to preference| engine prefers another)?\s*:?)"
    r"\s*(\d+)",
    re.IGNORECASE,
)
ERRORS_SECTION_RE = re.compile(
    r"^##\s+Your errors, move by move\s*$",
    re.IGNORECASE | re.MULTILINE,
)
NEXT_SECTION_RE = re.compile(r"^##\s+", re.MULTILINE)
GAME_ID_RE = re.compile(r"^Game ID:\s*(\S+)", re.MULTILINE)
GAME_RE = re.compile(r"^Game:\s*(\S+)", re.MULTILINE)
DATE_RE = re.compile(r"^Date:\s*([^|\n]+)", re.MULTILINE)
TITLE_RE = re.compile(r"^#.*Game analysis:\s*(?P<white>.+?)\s+vs\s+(?P<black>.+?)\s*$", re.MULTILINE)
YOU_PLAYED_RE = re.compile(r"You played:\s*(white|black)", re.IGNORECASE)


@dataclass
class ErrorRow:
    game_index: int
    game_id: str
    game_date: str
    report_path: str
    move_label: str
    move_number: int
    classification: str
    error_type: str
    wp_loss: float
    depth: int


def game_id_from_text(text, path):
    match = GAME_ID_RE.search(text) or GAME_RE.search(text)
    if match:
        return match.group(1).rstrip("/").rsplit("/", 1)[-1]
    stem = path.stem
    for prefix in ("report_", "analysis_"):
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
    return stem


def date_from_text(text, path):
    match = DATE_RE.search(text)
    if match:
        return match.group(1).strip()
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")


def report_is_for_username(text, username):
    """Return True when this perspective report is for username.

    The analyzer writes one report per perspective; each report's "Your errors"
    section belongs to the side named in "You played". Filtering here prevents
    opponent perspective files from being collated as the user's blunders.
    """
    title = TITLE_RE.search(text)
    perspective = YOU_PLAYED_RE.search(text)
    if not title or not perspective:
        return False
    played = perspective.group(1).casefold()
    report_user = title.group(played).strip().casefold()
    return report_user == username.strip().casefold()


def player_error_text(text):
    """Return only the player's error section, excluding critical/full tables."""
    section = ERRORS_SECTION_RE.search(text)
    if not section:
        return text
    next_section = NEXT_SECTION_RE.search(text, section.end())
    end = next_section.start() if next_section else len(text)
    return text[section.end():end]


def parse_report(path, username):
    text = path.read_text(encoding="utf-8")
    if not report_is_for_username(text, username):
        return []
    game_id = game_id_from_text(text, path)
    game_date = date_from_text(text, path)
    title = TITLE_RE.search(text)
    game_label = (
        f"{title.group('white').strip()} vs {title.group('black').strip()}"
        if title else game_id
    )
    error_text = player_error_text(text)
    rows = []
    matches = list(ERROR_HEADING_RE.finditer(error_text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(error_text)
        section = error_text[match.start():end]
        depth_match = DEPTH_RE.search(section)
        if not depth_match:
            continue
        rows.append({
            "game_id": game_id,
            "game_date": game_date,
            "game_label": game_label,
            "report_path": str(path),
            "move_label": match.group("label").strip(),
            "move_number": int(match.group("move_number")),
            "classification": match.group("classification").strip().casefold(),
            "error_type": match.group("error_type").strip().casefold(),
            "wp_loss": float(match.group("wp_loss")),
            "depth": int(depth_match.group(1)),
        })
    return rows


def depth_bin(depth):
    for i, (lo, hi) in enumerate(DEPTH_BINS):
        if lo <= depth <= hi:
            return i
    return len(DEPTH_BINS) - 1


def rolling(values, window=10):
    out = []
    for i in range(len(values)):
        chunk = [v for v in values[max(0, i - window + 1):i + 1] if v is not None]
        out.append(sum(chunk) / len(chunk) if chunk else None)
    return out


def render_scatter(rows, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    if not rows:
        return
    n_games = max(row.game_index for row in rows) + 1
    counts = [0] * n_games
    first_serious = [None] * n_games
    for row in rows:
        if row.wp_loss >= BLUNDER_THRESHOLD:
            counts[row.game_index] += 1
            first_serious[row.game_index] = row.move_number if first_serious[row.game_index] is None else min(first_serious[row.game_index], row.move_number)

    fig = plt.figure(figsize=(13, 9))
    gs = fig.add_gridspec(3, 1, height_ratios=[3, 1, 1], hspace=0.32)
    ax = fig.add_subplot(gs[0])
    for i, color in enumerate(DEPTH_COLORS):
        sel = [row for row in rows if depth_bin(row.depth) == i]
        ax.scatter([r.game_index for r in sel], [r.move_number for r in sel],
                   s=[r.wp_loss * 6.0 for r in sel], c=color, alpha=0.72,
                   edgecolors="white", linewidths=0.5, zorder=3)
    ax.set_xlim(-1, n_games)
    ax.set_ylim(0, max(62, max(r.move_number for r in rows) + 3))
    ax.set_xlabel("game index (chronological)")
    ax.set_ylabel("move number")
    ax.set_title("Serious errors by game and move number\narea = win probability loss   |   color = depth at which engine prefers another move", fontsize=11, loc="left")
    ax.grid(alpha=0.18, zorder=0)
    color_legend = [Line2D([], [], marker="o", linestyle="none", markersize=8, markerfacecolor=c, markeredgecolor="white", label=l) for c, l in zip(DEPTH_COLORS, DEPTH_LABELS)]
    size_legend = [Line2D([], [], marker="o", linestyle="none", markersize=(v * 6.0) ** 0.5, markerfacecolor="#999999", markeredgecolor="white", label=f"{v:.0f} pp WP loss") for v in (5, 15, 30)]
    leg1 = ax.legend(handles=color_legend, title="depth to preference", loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8, title_fontsize=8, frameon=False)
    ax.add_artist(leg1)
    ax.legend(handles=size_legend, title="magnitude", loc="upper left", bbox_to_anchor=(1.01, 0.42), fontsize=8, title_fontsize=8, frameon=False, labelspacing=1.4)

    x = list(range(n_games))
    ax2 = fig.add_subplot(gs[1], sharex=ax)
    ax2.bar(x, counts, color="#c9ccd1", width=0.85, zorder=2)
    ax2.plot(x, rolling(counts), color="#d1495b", lw=2.2, zorder=3)
    ax2.set_ylabel("blunders\nper game", fontsize=9)
    ax2.grid(alpha=0.18, zorder=0)
    ax2.set_title("blunders per game, 10-game rolling mean in red", fontsize=9, loc="left")

    ax3 = fig.add_subplot(gs[2], sharex=ax)
    ax3.scatter(x, first_serious, s=14, color="#c9ccd1", zorder=2)
    ax3.plot(x, rolling(first_serious), color="#30638e", lw=2.2, zorder=3)
    ax3.set_ylabel("first serious\nerror (move)", fontsize=9)
    ax3.set_xlabel("game index (chronological)")
    ax3.grid(alpha=0.18, zorder=0)
    ax3.set_title("move number of first serious error, 10-game rolling mean in blue", fontsize=9, loc="left")
    fig.suptitle(f"REAL DATA  |  mistake >= {MISTAKE_THRESHOLD:.0f} pp, blunder >= {BLUNDER_THRESHOLD:.0f} pp", fontsize=9, color="#666666", x=0.01, ha="left", y=0.985)
    fig.savefig(path, dpi=145, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def write_markdown(rows, path, image_path):
    lines = ["# Blunder Report", "", f"Generated from {len(set(r.game_id for r in rows))} analyzed game(s).", ""]
    if image_path:
        lines.extend([f"![Blunder scatter]({os.path.basename(image_path)})", ""])
    lines.extend(["| Game # | Game ID | Date | Move | Class | Type | WP loss | Depth | Report |", "|---:|---|---|---|---|---|---:|---:|---|"])
    for row in rows:
        lines.append(f"| {row.game_index} | {row.game_id} | {row.game_date} | {row.move_label} | {row.classification} | {row.error_type} | {row.wp_loss:.0f} | {row.depth} | {row.report_path} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--out", default="blunder_report.md")
    parser.add_argument("--csv", default="blunder_report.csv")
    parser.add_argument("--graph", default="blunder_scatter.png")
    parser.add_argument("--username", default="DanielKetterer",
                        help="Only include perspective reports whose 'You played' side is this Chess.com user.")
    args = parser.parse_args()

    paths = sorted(Path(args.reports_dir).glob("**/*.md"))
    raw_rows = []
    for path in paths:
        raw_rows.extend(parse_report(path, args.username))
    game_order = {gid: i for i, gid in enumerate(dict.fromkeys(row["game_id"] for row in sorted(raw_rows, key=lambda r: (r["game_date"], r["game_id"]))))}
    rows = [ErrorRow(game_index=game_order[row["game_id"]], **{k: v for k, v in row.items() if k != "game_label"}) for row in raw_rows]
    rows.sort(key=lambda r: (r.game_index, r.move_number, r.report_path))

    with open(args.csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(ErrorRow.__dataclass_fields__))
        writer.writeheader()
        writer.writerows([row.__dict__ for row in rows])
    image_path = args.graph if rows else ""
    if rows:
        try:
            render_scatter(rows, args.graph)
        except ImportError as exc:
            print(f"Could not render scatter plot: {exc}")
            image_path = ""
    write_markdown(rows, Path(args.out), image_path)


if __name__ == "__main__":
    main()
