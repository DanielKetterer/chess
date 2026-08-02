# Chess analysis pipeline ♟️

This repo analyzes Chess.com games with Stockfish 18, writes a coaching report for each game, collates historical data into an error tracker, and attempts to mine from game positions 'puzzles' defined below in the 'Puzzle classification, gates, and attempts' section.


## Running this yourself: fork setup

Everything below is for someone who has forked the repo and wants to use it analyzing
their own games. You do not need a local Python environment for any of it. The
workflows install Stockfish and the dependencies on GitHub's runners.

### 1. Fork and enable Actions

1. Fork the repo.
2. Open the **Actions** tab on your fork. GitHub disables workflows on new forks
   until you confirm; click the button to enable them.
3. Go to **Settings > Actions > General > Workflow permissions** and select
   **Read and write permissions**. Every workflow here commits its output back
   to the branch, and they will all fail at the push step without this. This is
   the single most common reason a fresh fork does nothing.

### 2. Point it at your account

Some code carries a hardcoded default of `DanielKetterer`:

- The `username` input on each .yml workflow file. You can type your own username at
  dispatch time too, but if you edit the `default:` value in the four files under
  `.github/workflows/` you never have to think about it again.

There is no API key and no secret to configure. The Chess.com public API needs
no authentication.

### 3. Clear out the previous owner's data

A fresh fork inherits my games. Before your first run:
Either just delete ( the reports, rendered_puzzle directories and puzzles.json ), or if command line savvy,

```bash
git rm -r --cached reports rendered-puzzles
rm -rf reports rendered-puzzles
echo '[]' > puzzles.json
git add -A && git commit -m "Reset analysis data" && git push
```

Leaving them iin will mix your data with mine, not desired.

### 4. Run it :)

The four workflows, in the order you will meet them:

| Workflow | Trigger | What it does | Runtime |
|---|---|---|---|
| `Analyze Chess Game` | manual | One game. Blank `game_id` means your latest. | 10 to 45 min |
| `Analyze Daily Chess Games` | 3am cron, or manual | Every game from a local day that has no report yet | ~depends on volume |
| `Blunder Report` | automatic after analysis or on any push to `reports/**` | Rebuilds `blunder_report.md`, the CSV, and the scatter | under a minute |
| `Puzzle utilities` | automatic after analysis or a `puzzles.json` push; manual for interactive modes | Renders new cards, or manually lists, renders, and completes puzzles. No Stockfish. | under a minute |

Start with `Analyze Chess Game` on a single game and leave `depth` at `24`. It
confirms the whole chain works, including the commit-back, in one run.

You do not need to run `Blunder Report` by hand. It follows successful analysis
runs directly (GitHub does not fan out workflows from pushes made with the
built-in Actions token) and also fires for ordinary pushes under `reports/`.

### 5. Cost and the depth dial

Depth is the only knob that meaningfully changes runtime, and it is not linear.
Every step up roughly doubles the search.

- `10`: seconds per game. Use it to check that your fork is wired up.
- `18`: a few minutes per game. Fine for volume.
- `24`: the default, and where the reports were tuned. Tens of minutes per game
  with `--findability honest`, which runs a separate search ladder per error.
- `30`: hours. Only worth it for a single game you care about.

Public repos get unlimited free Actions minutes; private forks bill against
your plan's quota, where a nightly depth-24 run will consume it quickly. The
jobs carry `timeout-minutes: 350`, just under GitHub's 6 hour ceiling, so a
runaway analysis fails visibly instead of being killed mid-commit.


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
- `--reports-dir reports` files the outputs into the dated tree described
  below instead of writing to `--out` and `--graph` directly.
- `--reports-timezone <IANA name>` picks which calendar day a game belongs to.

## Where files land

Reports and rendered puzzle cards are organized by date:

```
reports/
  2026/
    07/
      24/
        a1b2c3d4_20260725T013000Z_white.md
        a1b2c3d4_20260725T013000Z_white.png
        a1b2c3d4_20260725T013000Z_white.json
        a1b2c3d4_20260725T013000Z_black.md
        ...
rendered-puzzles/
  2026/
    07/
      24/
        p3f9a12bc4.md
```

Two things are worth knowing about that layout.

**The folder is a local day, the filename stamp is UTC.** A game that ends at
01:30 UTC on July 25 was played on the evening of July 24 in New York, so with
`--reports-timezone America/New_York` it files under `2026/07/24/` while the
filename still reads `20260725T013000Z`. The stamp is a globally unambiguous
identifier; the folder is for finding the games you remember playing. If you
would rather they always agree, set the timezone to `UTC` everywhere.

**Placement is deterministic.** The directory and filename are derived from the
game's own end time, so re-analyzing a game at a different depth overwrites its
old report instead of leaving a near-duplicate somewhere else in the tree.
`chess_analyzer.py` creates the directories it needs; the workflows create the
`reports/` root so a fresh fork has one on the first run.

Nothing needs migrating. `blunder_report.py` walks `reports/` recursively and
still collates flat files from before the tree existed. If you want the old
files tidied anyway:

```bash
python migrate_report_tree.py --reports-dir reports --timezone America/New_York --dry-run
```

Drop `--dry-run` to actually move them. Files whose names do not carry a
`_YYYYMMDDTHHMMSSZ_<color>` stamp are left where they are.

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
or `unmeasured` values for missing fields. The scan is recursive, so the dated
tree and any flat leftovers are both picked up, and the Report column links to
each report relative to wherever `--out` was written.

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
  "find the best move."

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
      "timestamp": "2026-07-24T00:00:00+00:00",
      "move": "...",
      "found": true
    }
  ]
}
```

The attempt log is the completion state: a puzzle is solved once any attempt
has `found: true`. Failed attempts remain useful for review scheduling, and a
successful puzzle is offered again after progressively longer intervals rather
than being permanently removed from the queue.

Attention errors and both players' game accuracy are written to sidecar
`metrics`. `blunder_report.py` plots the per-100-moves attention series over
time, as well as your accuracy in red and your opponents' accuracy in blue.

## GitHub Action puzzle tools

Puzzle creation is wired into the normal `Analyze Chess Game` and `Analyze Daily
Chess Games` workflows. Those workflows already pay the Stockfish cost, so they
pass `--puzzles-file puzzles.json`, commit the updated puzzle file, and keep the
JSON sidecars alongside the Markdown reports for later trend reporting.

The separate `Puzzle utilities` workflow is intentionally lightweight and does
not run Stockfish. A successful analysis run or an ordinary push that changes
`puzzles.json` automatically renders every puzzle without a card. Manual runs
additionally support:

- `list`: run `scripts/render_puzzle_md.py` to render a chessboard and stored
  prompt to `puzzle.md`, uncommitted, for reading in the run log.
- `render`: write a committed card to
  `rendered-puzzles/YYYY/MM/DD/<puzzle-id>.md`, dated by when the puzzle was
  generated. Set `render_all_unrendered: true` to catch up every puzzle that
  has no card yet; a card found at any depth counts as rendered, so cards
  written before the tree existed are not duplicated.
- `complete`: run `scripts/mark_puzzle_attempt.py` to append a successful
  attempt (`timestamp`, `found`, and the optional move) and commit the updated
  puzzle file. The renderer consumes that same log for status and scheduling.

Rendering is deliberately separate from submitting a move. Cards are for reading
the position; lines get played out on your own analysis board.

---


## What each file does

| File | Role |
|---|---|
| `chess_analyzer.py` | Fetches a game, runs Stockfish, writes the Markdown report, PNG graph, and JSON sidecar. Appends new puzzles. |
| `unanalyzed_games.py` | Lists game IDs from a given local day that have no report in `reports/` yet. |
| `blunder_report.py` | Collates every sidecar into `blunder_report.md`, `blunder_report.csv`, and the scatter image. |
| `scripts/render_puzzle_md.py` | Renders one stored puzzle to a Markdown card with a board diagram. |
| `scripts/mark_puzzle_attempt.py` | Appends an attempt to a puzzle and marks it complete. |
| `migrate_report_tree.py` | One-off tidy-up for flat reports predating the dated tree. |

`unanalyzed_games.py` scans `reports/` to decide what is already done, so it has
to walk the tree recursively. If it ever starts re-analyzing your whole archive
every night, that scan is the thing to check first.

## Reading the output

`blunder_report.md` at the repo root is the summary: a provenance line, a
scatter image, and one row per error linking back to the report it came from.
Individual game reports under `reports/YYYY/MM/DD/` are the coaching prose, one
per color, with an evaluation graph beside them.

The Depth column is the one worth understanding. An integer is a measured
depth-to-find. `<=floor` means the engine already preferred the better move at
the shallowest depth this measurement resolves, so the error was findable and
the number would be noise. `>cap` means it never settled inside the analysis
depth. `unmeasured` means the measurement was invalid; the row is kept but left
out of the depth bins.

## Opening Grove (GitHub Pages)

https://danielketterer.github.io/chess/

The interactive opening explorer lives in `docs/` and is ready to publish with
GitHub Pages (Settings → Pages → deploy from the branch's `/docs` folder). It
combines the repository's report archive with the bundled ECO tables, keeps
only book moves plus each game's first deviation, and supports color/date
filters, collapsible branches, constrained board moves, and continuation
arrows.

The `Refresh opening explorer` workflow regenerates and commits the dataset
whenever reports, the ECO tables, or the builder change. It can also be run
manually from the Actions tab. To rebuild it locally, run:

```bash
python scripts/build_opening_explorer.py
```

## Puzzle Canopy (GitHub Pages)

The puzzle trainer is published at
https://danielketterer.github.io/chess/puzzles.html. It faces each board toward
the solver, checks click-to-move choices for legality, grades immediately, and
uses the same failed-first/due/oldest scheduling rules as the Markdown puzzle
renderer. Category, due-state, side-to-move, and previous-failure filters are
available above the board.

After an attempt, download its JSON record or copy the displayed
`scripts/mark_puzzle_attempt.py` command and run it from the repository root.
The command updates `puzzles.json`; rebuild the Pages payload with:

```bash
python scripts/build_puzzle_dataset.py
```

A static GitHub Pages site cannot commit an attempt directly without an
authenticated API/backend. The `Refresh puzzle trainer` workflow regenerates
and commits `docs/puzzles-data.js` whenever the source puzzles or builder
changes, while intentionally excluding bulky analysis/report fields from the
browser payload.
