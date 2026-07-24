# Chess analysis pipeline

This repo analyzes Chess.com games with Stockfish and writes both a Markdown
coaching report and a JSON sidecar that the trend report can collate later.

## Analyze a game

```bash
python chess_analyzer.py --username <chesscom-user> --depth 14 --out report.md --graph eval_graph.png
```

Useful options:

- `--game-id <id-or-url>` analyzes a specific Chess.com game.
- `--csv moves.csv --game latest:rapid` analyzes an existing move-history CSV.
- `--perspective white|black|both` controls which player reports are written.
- `--findability honest` also measures depth-to-find for the best move.
- `--puzzles-file puzzles.json` chooses the persistent tactics/puzzle file.

## Error enrichment

For each inaccuracy, mistake, or blunder by the report perspective, the analyzer
now records:

- **Refute depth**: the shallowest depth, capped at 18, where Stockfish already
  shows the played move losing at least that class's win-probability threshold
  (`5`, `10`, or `20` points). Values past the cap are recorded as `>18`.
- **Seconds spent**: derived from PGN `%clk` comments as previous clock minus
  current clock plus increment. If clocks or increments are missing, the field is
  left blank instead of failing the run.
- **Pre-error eval bucket**: `winning`, `balanced`, or `losing` from the analyzed
  player's point of view before the error.

The game graph includes the usual win-probability line and a second panel of
seconds spent versus win-probability loss, one point per error.

## Puzzle file

Errors with `refute_depth <= 6` are appended to the persistent puzzle file and
are deduplicated by FEN. Each puzzle contains the FEN before the move, played
move, best move, source game, move number, generation date, and a `completed`
flag defaulting to `false`.

Mark a puzzle completed without hand-editing the JSON:

```bash
python chess_analyzer.py --mark-completed '<fen>' --puzzles-file puzzles.json
```

Reports show the current open vs completed puzzle counts when a puzzle file is
used.

## Collate reports

```bash
python blunder_report.py --reports-dir reports --username <chesscom-user>
```

The collator reads JSON sidecars when present and falls back to older Markdown
reports. New columns are included when available, while older reports keep blank
or `unmeasured` values for missing fields.
