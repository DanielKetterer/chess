#!/usr/bin/env python3
"""Append an attempt to a puzzle and optionally mark it complete."""
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--puzzles-file', default='puzzles.json')
p.add_argument('--fen', required=True)
p.add_argument('--move', default='')
p.add_argument('--result', choices=['correct','incorrect','completed'], default='completed')
args=p.parse_args()
path=Path(args.puzzles_file)
data=json.loads(path.read_text(encoding='utf-8')) if path.exists() else []
puzzles=data if isinstance(data, list) else data.get('puzzles', [])
for puzzle in puzzles:
    if puzzle.get('fen_before') == args.fen or puzzle.get('fen') == args.fen:
        puzzle.setdefault('attempts', []).append({'attempted_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'move': args.move, 'result': args.result})
        if args.result in ('correct','completed'):
            puzzle['completed'] = True
        path.write_text(json.dumps(data if not isinstance(data, list) else puzzles, indent=2), encoding='utf-8')
        print('updated')
        break
else:
    raise SystemExit('no matching puzzle')
