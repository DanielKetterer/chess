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

Eligible classified errors are appended to the persistent puzzle file and
are deduplicated by FEN. Each puzzle contains the FEN before the move, played
move, best move, category, prompt fields, source game, move number, generation
date, attempts, and a `completed` flag defaulting to `false`.

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

## Puzzle classification, gates, and attempts

Puzzle generation is no longer a pure difficulty filter. Every report-side error
is assigned an `error_category`:

- `attention`: the played move is refuted at depth `1` or `2`. These are tracked
  as a rate, not made into puzzles.
- `missed_tactic`: the position before the move contained a forcing best move
  (check, capture, promotion, or a forcing principal variation) and the analyzed
  player chose something else.
- `allowed_tactic`: the analyzed player's move gives the opponent a forcing
  reply; puzzle prompts show the played move and ask for its refutation.
- `endgame`: all non-attention, non-tactical errors with seven or fewer
  non-king pieces on the board.
- `opening`: remaining errors through ply 20.
- `positional`: all other errors.

Only `missed_tactic`, `allowed_tactic`, and `endgame` can become puzzles. A
candidate is still discarded unless all quality gates pass:

1. `refute_depth` is an integer from `3` through `6`, inclusive.
2. The engine returned at least two candidate moves.
3. The mover-perspective win-probability gap between the best and second-best
   move is at least `10` points, so the puzzle has one right answer.
4. The FEN has not already been stored in the puzzle file.

Puzzle prompt format is stored on each puzzle:

- `missed_tactic` and `endgame`: `prompt_type: best_move`, with a best-move
  prompt for the position before the played move.
- `allowed_tactic`: `prompt_type: refutation`, with a prompt that includes the
  move played and asks what refutes it. These are deliberately not phrased as
  “find the best move.”

Attempt schema:

```json
{
  "fen_before": "...",
  "move_played": "e2e4",
  "best_move": "e7e5",
  "category": "allowed_tactic",
  "prompt_type": "refutation",
  "prompt": "Position after my move ... What refutes that move?",
  "best_second_wp_gap": 12.4,
  "attempts": [
    {
      "attempted_utc": "2026-07-24T00:00:00Z",
      "move": "...",
      "result": "correct"
    }
  ],
  "completed": true
}
```

Attention errors are written to sidecar `metrics` as `attention_errors`,
`player_moves`, and `attention_errors_per_100_moves`. `blunder_report.py` plots
that per-100-moves series over time.

## GitHub Action puzzle tools

The `Puzzle tools` workflow can be started manually with `workflow_dispatch`.
It supports:

- `generate-any`: analyze the latest Chess.com game, or a supplied `game_id`, at
  the selected depth (default `24`) and append eligible puzzles.
- `generate-unprocessed`: analyze the latest Chess.com game at depth `24` by
  default; the puzzle file deduplicates already-seen FENs.
- `list`: run `scripts/render_puzzle_md.py` to render a chessboard and stored
  prompt to `puzzle.md`.
- `complete`: run `scripts/mark_puzzle_attempt.py` to append a completion
  attempt and mark the puzzle complete.
