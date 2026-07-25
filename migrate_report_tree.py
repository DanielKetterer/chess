#!/usr/bin/env python3
"""Move flat reports/ files into the reports/YYYY/MM/DD tree.

Nothing depends on this. blunder_report.py globs recursively and counts flat
reports either way, so this is tidying, not repair. Run it once on a repo that
predates the dated tree.

    python migrate_report_tree.py --reports-dir reports --dry-run
    python migrate_report_tree.py --reports-dir reports --timezone America/New_York

Filenames are expected to look like:

    <game-id>_<YYYYMMDDTHHMMSSZ>_<color>.md

The timestamp in the name is UTC and stays untouched; only the folder is
derived, using the same timezone rule as chess_analyzer.py so a migrated file
lands where a re-analysis of the same game would put it. Anything that does not
match the pattern is reported and left alone rather than guessed at.
"""

import argparse
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

STAMP = re.compile(r"_(\d{8})T(\d{6})Z_(white|black)\.[A-Za-z0-9]+$")


def local_day(stamp_date, stamp_time, tz_name):
    dt = datetime.strptime(stamp_date + stamp_time, "%Y%m%d%H%M%S").replace(
        tzinfo=timezone.utc)
    tz = timezone.utc
    if tz_name and tz_name.upper() != "UTC":
        try:
            from zoneinfo import ZoneInfo
            tz = ZoneInfo(tz_name)
        except Exception:
            print(f"Unknown timezone {tz_name!r}; using UTC.", file=sys.stderr)
    local = dt.astimezone(tz)
    return f"{local.year:04d}", f"{local.month:02d}", f"{local.day:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports-dir", default="reports")
    ap.add_argument("--timezone", default="UTC",
                    help="must match --reports-timezone in the workflows")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.reports_dir)
    if not root.is_dir():
        raise SystemExit(f"{root} is not a directory")

    moved = skipped = collided = 0
    for path in sorted(p for p in root.iterdir() if p.is_file()):
        m = STAMP.search(path.name)
        if not m:
            print(f"skip (name does not carry a timestamp): {path}")
            skipped += 1
            continue
        year, month, day = local_day(m.group(1), m.group(2), args.timezone)
        dest = root / year / month / day / path.name
        if dest.exists():
            print(f"skip (destination exists): {path} -> {dest}")
            collided += 1
            continue
        print(f"{'would move' if args.dry_run else 'move'}: {path} -> {dest}")
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest))
        moved += 1

    print(f"\n{moved} moved, {skipped} unrecognized, {collided} collisions")
    if args.dry_run:
        print("dry run: nothing was written")


if __name__ == "__main__":
    main()
