"""Print Chess.com game IDs from a local date that do not have saved reports."""

import argparse
import json
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

API_ROOT = "https://api.chess.com/pub"
GAME_RE = re.compile(r"^Game:\s*(\S+)", re.MULTILINE)


def get_json(url, username):
    req = urllib.request.Request(url, headers={"User-Agent": f"ChessGameAnalyzer/1.1 (username: {username})", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as response:
        return json.load(response)


def known_game_ids(reports_dir):
    ids = set()
    for path in Path(reports_dir).glob("**/*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = GAME_RE.search(text)
        if match:
            ids.add(match.group(1).rstrip("/").rsplit("/", 1)[-1].casefold())
            continue
        ids.add(path.stem.split("_", 1)[0].casefold())
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--date", help="Local YYYY-MM-DD. Defaults to yesterday so a 3am run sees the completed day.")
    parser.add_argument("--timezone", default="America/New_York")
    parser.add_argument("--reports-dir", default="reports")
    args = parser.parse_args()

    tz = ZoneInfo(args.timezone)
    local_date = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else (datetime.now(tz).date() - timedelta(days=1))
    start = datetime.combine(local_date, datetime.min.time(), tzinfo=tz).astimezone(timezone.utc).timestamp()
    end = datetime.combine(local_date + timedelta(days=1), datetime.min.time(), tzinfo=tz).astimezone(timezone.utc).timestamp()
    month_url = f"{API_ROOT}/player/{args.username}/games/{local_date.year}/{local_date.month:02d}"
    games = get_json(month_url, args.username).get("games", [])
    known = known_game_ids(args.reports_dir)
    for game in games:
        game_id = str(game.get("url") or game.get("uuid") or "").rstrip("/").rsplit("/", 1)[-1]
        try:
            ended = int(game.get("end_time") or 0)
        except (TypeError, ValueError):
            ended = 0
        if game_id and start <= ended < end and game_id.casefold() not in known:
            print(game_id)


if __name__ == "__main__":
    main()
