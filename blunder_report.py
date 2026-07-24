"""Collate timestamped chess analysis reports into a blunder trend report.

Reads JSON sidecars written by chess_analyzer.py. Falls back to parsing the
markdown reports for older runs that predate the sidecar.

Design note, because the previous version got this wrong in a way that was
invisible in the output: rows whose depth measurement is censored (the engine
stably preferred the move at or below the measurement floor, or never settled
on it within the ladder cap) are NOT numbers. Coercing them to integers makes
censored values look measured; dropping them biases the dataset toward errors
that happen to be findable, which is exactly the variable being studied.
They are carried as categories all the way to the plot.
"""

import argparse
import csv
import json
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# Sentinels, matching chess_analyzer.py
CENSORED_LOW = "<=floor"
CENSORED_HIGH = ">cap"
UNMEASURED = "unmeasured"

DEFAULT_FLOOR = 6
DEFAULT_CAP = 24

# Colors are assigned per category below; the numeric bins are derived from
# the ladder cap actually used, not hardcoded to a cap that may have changed.
COLOR_CENSORED_LOW = "#d1495b"   # at or below floor: should have seen it
COLOR_LOW = "#edae49"            # reachable
COLOR_MID = "#4c8577"            # hard
COLOR_HIGH = "#30638e"           # outside human range
COLOR_CENSORED_HIGH = "#6b4a8a"  # never settled within cap
COLOR_UNMEASURED = "#9aa0a6"     # measurement invalid


# ---------------------------------------------------------------------------
# Markdown fallback parsing (pre-sidecar reports)
# ---------------------------------------------------------------------------

ERROR_HEADING_RE = re.compile(
    r"^###\s+(?P<label>(?P<move_number>\d+)\.{1,3}[^\n(:]+?)\s*"
    r"(?:\(|:|[-\u2013\u2014])\s*"
    r"(?P<classification>inaccuracy|mistake|blunder)\s*[,;|/ -]+\s*"
    # 'deep tactic' added: the previous alternation silently dropped every
    # deep-tactic row, which is the category of error most worth seeing.
    r"(?P<error_type>deep tactic|tactical|positional|unclear)\s*[,;|/ -]+\s*"
    r"(?:wp|win[- ]probability)\s*loss\s*:?\s*(?P<wp_loss>[\d.]+)\s*(?:%|pp|points?)?",
    re.IGNORECASE | re.MULTILINE,
)
# Censored-low prose: "from at or below depth 6". Must be tested BEFORE the
# numeric pattern, or it matches the 6 and reports a measured depth of 6.
DEPTH_CENSORED_LOW_RE = re.compile(
    r"at or below depth\s*(\d+)", re.IGNORECASE)
DEPTH_CENSORED_HIGH_RE = re.compile(
    r"never settles on this move within the analysis depth", re.IGNORECASE)
DEPTH_NUM_RE = re.compile(
    r"(?:engine (?:first prefers|prefers|does not settle on|does not prefer) "
    r"this move (?:from |at |until )?(?:search )?depth|"
    r"depth(?: to preference| engine prefers another)?\s*:?)"
    r"\s*(\d+)",
    re.IGNORECASE,
)
ERRORS_SECTION_RE = re.compile(r"^##\s+Your errors, move by move\s*$",
                               re.IGNORECASE | re.MULTILINE)
NEXT_SECTION_RE = re.compile(r"^##\s+", re.MULTILINE)
GAME_ID_RE = re.compile(r"^Game ID:\s*(\S+)", re.MULTILINE)
GAME_RE = re.compile(r"^Game:\s*(\S+)", re.MULTILINE)
DATE_RE = re.compile(r"^Date:\s*([^|\n]+)", re.MULTILINE)
TITLE_RE = re.compile(
    r"^#.*Game analysis:\s*(?P<white>.+?)\s+vs\s+(?P<black>.+?)\s*$",
    re.MULTILINE)
YOU_PLAYED_RE = re.compile(r"You played:\s*(white|black)", re.IGNORECASE)
PROVENANCE_RE = re.compile(
    r"^Analysis:\s*(?P<kv>.+)$", re.MULTILINE)


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
    depth: object          # int, CENSORED_LOW, CENSORED_HIGH, or UNMEASURED


@dataclass
class GameRecord:
    game_id: str
    game_date: str
    report_path: str
    rows: list = field(default_factory=list)


def parse_provenance(text):
    m = PROVENANCE_RE.search(text)
    if not m:
        return {}
    out = {}
    for token in m.group("kv").split():
        if "=" in token:
            k, v = token.split("=", 1)
            out[k] = v
    return out


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
    title = TITLE_RE.search(text)
    perspective = YOU_PLAYED_RE.search(text)
    if not title or not perspective:
        return False
    played = perspective.group(1).casefold()
    return title.group(played).strip().casefold() == username.strip().casefold()


def player_error_text(text):
    section = ERRORS_SECTION_RE.search(text)
    if not section:
        return ""
    next_section = NEXT_SECTION_RE.search(text, section.end())
    end = next_section.start() if next_section else len(text)
    return text[section.end():end]


def depth_from_section(section):
    """Order matters: censored-low prose contains a number that is NOT a
    measurement, so it has to be recognized before the numeric pattern."""
    if DEPTH_CENSORED_LOW_RE.search(section):
        return CENSORED_LOW
    if DEPTH_CENSORED_HIGH_RE.search(section):
        return CENSORED_HIGH
    m = DEPTH_NUM_RE.search(section)
    if m:
        return int(m.group(1))
    return UNMEASURED


def parse_markdown_report(path, username):
    """Fallback for reports written before the JSON sidecar existed."""
    text = path.read_text(encoding="utf-8")
    if not report_is_for_username(text, username):
        return None
    game_id = game_id_from_text(text, path)
    rec = GameRecord(game_id=game_id,
                     game_date=date_from_text(text, path),
                     report_path=str(path))
    error_text = player_error_text(text)
    matches = list(ERROR_HEADING_RE.finditer(error_text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(error_text)
        section = error_text[match.start():end]
        rec.rows.append({
            "move_label": match.group("label").strip(),
            "move_number": int(match.group("move_number")),
            "classification": match.group("classification").strip().casefold(),
            "error_type": match.group("error_type").strip().casefold(),
            "wp_loss": float(match.group("wp_loss")),
            # No longer `continue` on a missing number: an unparseable or
            # censored depth is a property of the row, not a reason to
            # delete the row.
            "depth": depth_from_section(section),
        })
    rec.provenance = parse_provenance(text)
    return rec


def parse_sidecar(path, username):
    data = json.loads(path.read_text(encoding="utf-8"))
    color = data.get("player_color", "")
    if data.get(color, "").strip().casefold() != username.strip().casefold():
        return None
    rec = GameRecord(game_id=data["game_id"],
                     game_date=data["game_date"],
                     report_path=str(path.with_suffix(".md")))
    for e in data.get("errors", []):
        rec.rows.append({
            "move_label": e["move_label"],
            "move_number": e["move_number"],
            "classification": e["classification"],
            "error_type": e["error_type"],
            "wp_loss": float(e["wp_loss"]),
            "depth": UNMEASURED if e["depth_to_find"] is None else e["depth_to_find"],
        })
    rec.provenance = data.get("analysis", {})
    return rec


# ---------------------------------------------------------------------------
# Depth categorization
# ---------------------------------------------------------------------------

def build_bins(floor, cap):
    """Numeric bins spanning (floor, cap], split into reachable / hard /
    outside human range. Derived from the cap in use so the labels cannot
    describe a configuration that is no longer running."""
    span = cap - floor
    b1 = floor + max(1, round(span * 0.33))
    b2 = floor + max(2, round(span * 0.66))
    return [
        (floor + 1, b1, COLOR_LOW, f"{floor + 1}-{b1} (reachable)"),
        (b1 + 1, b2, COLOR_MID, f"{b1 + 1}-{b2} (hard)"),
        (b2 + 1, cap, COLOR_HIGH, f"{b2 + 1}-{cap} (outside human range)"),
    ]


def categorize(depth, floor, bins):
    if depth == CENSORED_LOW:
        return "censored_low"
    if depth == CENSORED_HIGH:
        return "censored_high"
    if depth == UNMEASURED or depth is None:
        return "unmeasured"
    d = int(depth)
    if d <= floor:
        # Should be impossible from current analyzer output, but old reports
        # may contain it; treat as censored rather than inventing precision.
        return "censored_low"
    for i, (lo, hi, _c, _l) in enumerate(bins):
        if lo <= d <= hi:
            return f"bin{i}"
    return f"bin{len(bins) - 1}"


def category_style(cat, bins, floor, cap):
    table = {
        "censored_low": (COLOR_CENSORED_LOW, f"at or below {floor} (should have seen it)"),
        "censored_high": (COLOR_CENSORED_HIGH, f"never settled by {cap}"),
        "unmeasured": (COLOR_UNMEASURED, "unmeasured"),
    }
    if cat in table:
        return table[cat]
    i = int(cat[3:])
    return bins[i][2], bins[i][3]


def rolling(values, window=10):
    out = []
    for i in range(len(values)):
        chunk = [v for v in values[max(0, i - window + 1):i + 1] if v is not None]
        out.append(sum(chunk) / len(chunk) if chunk else None)
    return out


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_scatter(rows, n_games, path, floor, cap, provenance, min_games=40):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    import numpy as np

    bins = build_bins(floor, cap)
    order = ["censored_low"] + [f"bin{i}" for i in range(len(bins))] + \
            ["censored_high", "unmeasured"]

    # Blunder counts come from the analyzer's own classification, not from a
    # threshold re-derived here. The previous version counted wp_loss >= 10 as
    # a blunder while the analyzer labelled that a mistake, so the bar chart
    # and the Class column in the same report disagreed.
    counts = [0] * n_games
    first_serious = [None] * n_games
    for r in rows:
        if r.classification == "blunder":
            counts[r.game_index] += 1
            cur = first_serious[r.game_index]
            first_serious[r.game_index] = (
                r.move_number if cur is None else min(cur, r.move_number))

    fig = plt.figure(figsize=(15, 9))
    # Reserve the right margin explicitly. bbox_inches="tight" does not
    # reliably include legends anchored outside the axes, which is why the
    # depth legend was rendering clipped.
    gs = fig.add_gridspec(3, 1, height_ratios=[3, 1, 1], hspace=0.32,
                          left=0.07, right=0.76, top=0.93, bottom=0.07)
    ax = fig.add_subplot(gs[0])

    for cat in order:
        sel = [r for r in rows if categorize(r.depth, floor, bins) == cat]
        if not sel:
            continue
        color, label = category_style(cat, bins, floor, cap)
        ax.scatter([r.game_index for r in sel], [r.move_number for r in sel],
                   s=[r.wp_loss * 6.0 for r in sel], c=color, alpha=0.72,
                   edgecolors="white", linewidths=0.5, zorder=3, label=label)

    # Fixed limits so successive renders overlay. Autoscaling to the data
    # meant a single game produced an x axis of -1 to 1.
    ax.set_xlim(-1, max(min_games, n_games))
    ax.set_ylim(0, 62)
    ax.set_xlabel("game index (chronological)")
    ax.set_ylabel("move number")
    ax.set_title("Serious errors by game and move number\n"
                 "area = win probability loss   |   "
                 "color = depth at which engine prefers another move",
                 fontsize=11, loc="left")
    ax.grid(alpha=0.18, zorder=0)

    color_legend = []
    for cat in order:
        color, label = category_style(cat, bins, floor, cap)
        color_legend.append(Line2D([], [], marker="o", linestyle="none",
                                   markersize=8, markerfacecolor=color,
                                   markeredgecolor="white", label=label))
    size_legend = [Line2D([], [], marker="o", linestyle="none",
                          markersize=(v * 6.0) ** 0.5, markerfacecolor="#999999",
                          markeredgecolor="white", label=f"{v:.0f} pp WP loss")
                   for v in (5, 15, 30)]
    leg1 = ax.legend(handles=color_legend, title="depth to preference",
                     loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8,
                     title_fontsize=8, frameon=False)
    ax.add_artist(leg1)
    ax.legend(handles=size_legend, title="magnitude", loc="upper left",
              bbox_to_anchor=(1.01, 0.38), fontsize=8, title_fontsize=8,
              frameon=False, labelspacing=1.4)

    x = list(range(n_games))
    ax2 = fig.add_subplot(gs[1], sharex=ax)
    ax2.bar(x, counts, color="#c9ccd1", width=0.85, zorder=2)
    ax2.plot(x, rolling(counts), color="#d1495b", lw=2.2, zorder=3)
    ax2.set_ylabel("blunders\nper game", fontsize=9)
    ax2.grid(alpha=0.18, zorder=0)
    ax2.set_title("blunders per game (analyzer classification), "
                  "10-game rolling mean in red", fontsize=9, loc="left")

    ax3 = fig.add_subplot(gs[2], sharex=ax)
    fs = np.array([np.nan if v is None else v for v in first_serious], dtype=float)
    ax3.scatter(x, fs, s=14, color="#c9ccd1", zorder=2)
    roll = rolling(first_serious)
    ax3.plot(x, [np.nan if v is None else v for v in roll],
             color="#30638e", lw=2.2, zorder=3)
    # Games with no blunder have no first-blunder move. Those are the good
    # games, and if they vanish silently the line is conditioned on having
    # blundered at all. Mark them instead.
    clean = [i for i, v in enumerate(first_serious) if v is None]
    if clean:
        ax3.scatter(clean, [0.5] * len(clean), marker="|", s=60,
                    color="#4c8577", zorder=4,
                    label="no blunder this game")
        ax3.legend(fontsize=7, frameon=False, loc="upper right")
    ax3.set_ylim(0, 62)
    ax3.set_ylabel("first blunder\n(move)", fontsize=9)
    ax3.set_xlabel("game index (chronological)")
    ax3.grid(alpha=0.18, zorder=0)
    ax3.set_title("move number of first blunder, 10-game rolling mean in blue",
                  fontsize=9, loc="left")

    prov = provenance_line(provenance, floor, cap, n_games, len(rows))
    fig.suptitle(prov, fontsize=8, color="#666666", x=0.01, ha="left", y=0.985)
    fig.savefig(path, dpi=145, facecolor="white")
    plt.close(fig)


def provenance_line(prov, floor, cap, n_games, n_rows):
    bits = [f"analysis depth {prov.get('depth', '?')}",
            f"ladder floor {floor}", f"cap {cap}",
            f"stable run {prov.get('stable_run', '?')}",
            f"{n_games} games", f"{n_rows} errors"]
    if prov.get("generated_utc"):
        bits.append(f"latest run {prov['generated_utc']}")
    return "REAL DATA  |  " + "  |  ".join(bits)


def write_markdown(rows, n_games, path, image_path, floor, cap, provenance):
    lines = ["# Blunder Report", ""]
    lines.append(provenance_line(provenance, floor, cap, n_games, len(rows)))
    lines.append("")
    lines.append("Depth column: an integer is a measured depth. "
                 f"`{CENSORED_LOW}` means the engine stably preferred the move "
                 f"at or below depth {floor}, which is as shallow as this "
                 f"measurement resolves. `{CENSORED_HIGH}` means it never "
                 f"settled within depth {cap}. `{UNMEASURED}` means the "
                 "measurement was invalid and the row is kept but not binned.")
    lines.append("")
    if image_path:
        lines.extend([f"![Blunder scatter]({os.path.basename(image_path)})", ""])
    lines.extend([
        "| Game # | Game ID | Date | Move | Class | Type | WP loss | Depth | Report |",
        "|---:|---|---|---|---|---|---:|---|---|"])
    for row in rows:
        lines.append(
            f"| {row.game_index} | {row.game_id} | {row.game_date} | "
            f"{row.move_label} | {row.classification} | {row.error_type} | "
            f"{row.wp_loss:.1f} | {row.depth} | {row.report_path} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--out", default="blunder_report.md")
    parser.add_argument("--csv", default="blunder_report.csv")
    parser.add_argument("--graph", default="blunder_scatter.png")
    parser.add_argument("--username", default="DanielKetterer")
    parser.add_argument("--floor", type=int, default=None,
                        help="override measurement floor (default: read from "
                             "report provenance, else 6)")
    parser.add_argument("--cap", type=int, default=None,
                        help="override ladder cap (default: read from report "
                             "provenance, else 24)")
    parser.add_argument("--min-games-axis", type=int, default=40,
                        help="minimum x-axis width so early renders overlay "
                             "with later ones")
    args = parser.parse_args()

    root = Path(args.reports_dir)
    records = []
    seen_md = set()
    # Sidecars first; a markdown file with a sidecar is not parsed twice.
    for p in sorted(root.glob("**/*.json")):
        try:
            rec = parse_sidecar(p, args.username)
        except (json.JSONDecodeError, KeyError) as exc:
            print(f"skipping malformed sidecar {p}: {exc}")
            continue
        if rec:
            records.append(rec)
            seen_md.add(p.with_suffix(".md"))
    for p in sorted(root.glob("**/*.md")):
        if p in seen_md:
            continue
        rec = parse_markdown_report(p, args.username)
        if rec:
            records.append(rec)

    if not records:
        print("no reports found")
        return

    records.sort(key=lambda r: (r.game_date, r.game_id))
    # Every analyzed game gets an index, including games with zero errors.
    # Building the index from error rows alone made a clean game invisible and
    # silently removed it from the denominator.
    game_order = {}
    for rec in records:
        if rec.game_id not in game_order:
            game_order[rec.game_id] = len(game_order)
    n_games = len(game_order)

    prov = {}
    for rec in records:
        prov.update(getattr(rec, "provenance", {}) or {})
    floor = args.floor if args.floor is not None else int(
        prov.get("floor", prov.get("measurement_floor", DEFAULT_FLOOR)))
    cap = args.cap if args.cap is not None else int(
        prov.get("depth", DEFAULT_CAP))

    rows = []
    for rec in records:
        for r in rec.rows:
            rows.append(ErrorRow(
                game_index=game_order[rec.game_id],
                game_id=rec.game_id,
                game_date=rec.game_date,
                report_path=rec.report_path,
                **r))
    rows.sort(key=lambda r: (r.game_index, r.move_number, r.report_path))

    with open(args.csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(ErrorRow.__dataclass_fields__))
        writer.writeheader()
        writer.writerows([row.__dict__ for row in rows])

    image_path = args.graph if rows else ""
    if rows:
        try:
            render_scatter(rows, n_games, args.graph, floor, cap, prov,
                           min_games=args.min_games_axis)
        except ImportError as exc:
            print(f"Could not render scatter plot: {exc}")
            image_path = ""
    write_markdown(rows, n_games, Path(args.out), image_path, floor, cap, prov)

    dropped = sum(1 for r in rows if r.depth == UNMEASURED)
    print(f"{n_games} games, {len(rows)} error rows, "
          f"{dropped} with unmeasured depth")


if __name__ == "__main__":
    main()
