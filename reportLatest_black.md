# (free, so lmk) Game analysis: Neuromorphic vs DanielKetterer

Date: 2024.10.22  |  Time control: daily (1/259200)  |  You played: black
Game: https://www.chess.com/game/daily/719246613

## Summary

- Lichess accuracy: you 50.2%, opponent 61.6%
- Opening: C50 Italian Game: Rousseau Gambit (theory followed through ply 6)
- First deviation from theory: ply 7, Opponent played 4. Nc3
- Your moves: 8 best, 0 excellent, 0 good, 2 inaccuracy, 2 mistake, 2 blunder

METRICS:

Best: The played move exactly matches Stockfish's top move

Excellent: A non-best move that loses 2 WP points or less.

Good: WP loss is over 2, but under 5 points; also used for losses under 20 when the position remains already decided.

Inaccuracy: WP loss is at least 5 but under 10 points.

Mistake: WP loss is at least 10 but under 20 points; also generally used when a forced mate is missed with under 10 points of WP loss.

Blunder: WP loss is 20 points or more, or a forced mate is missed with at least 10 points of WP loss.

See: https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-etc 

(Brillint, Great and Miss are rating subjective)
![Evaluation graph](reportLatest_black.png)

## Biggest missed opportunity

You played 4...Qf6. Stockfish preferred fxe4, after which the main line runs 4...fxe4 5. Bxg8 exf3 6. Bd5 fxg2 7. Bxg2. The evaluation crossed from winning to losing, which matters more than the raw number. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 5; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: fxe4 (-1.70), Nf6 (+1.20), Bb4 (+1.27).

## Critical positions

- Ply 7 (opponent), 4.Nc3: +1.20 -> -1.70 [evaluation crossed equal -> losing]
- Ply 8 (you), 4...Qf6: -1.70 -> +3.19 [only-move situation; evaluation crossed winning -> losing]
- Ply 17 (opponent), 9.Nxf6+: +5.02 -> +1.66 [only-move situation; evaluation crossed winning -> equal]
- Ply 22 (you), 11...Kd8: +1.69 -> +1.93 [only-move situation]
- Ply 25 (opponent), 13.O-O: +3.24 -> +3.22 [only-move situation]
- Ply 28 (you), 14...Qe6: +2.27 -> +34.50 [only-move situation]

## Your errors, move by move

### 3...f5 (inaccuracy, positional, wp loss 10%)

You played 3...f5. Stockfish preferred Nf6, after which the main line runs 3...Nf6 4. d3 Bc5 5. O-O d6 6. c3. Why it went wrong: left pawn on f5 insufficiently defended; motif: creates threat on e4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nf6 (+0.14), Bc5 (+0.14), d6 (+0.42).

### 4...Qf6 (blunder, tactical, wp loss 42%)

You played 4...Qf6. Stockfish preferred fxe4, after which the main line runs 4...fxe4 5. Bxg8 exf3 6. Bd5 fxg2 7. Bxg2. The evaluation crossed from winning to losing, which matters more than the raw number. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 5; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: fxe4 (-1.70), Nf6 (+1.20), Bb4 (+1.27).

### 5...Qd6 (inaccuracy, positional, wp loss 10%)

You played 5...Qd6. Stockfish preferred Qd8, after which the main line runs 5...Qd8 6. d4 d6 7. dxe5 fxe4 8. Nd4. Why it went wrong: left pawn on f5 insufficiently defended; motif: creates threat on e4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 11; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Qd8 (+2.98), Qg6 (+3.84), fxe4 (+4.33).

### 10...Ke7 (mistake, positional, wp loss 13%)

You played 10...Ke7. Stockfish preferred Kd8, after which the main line runs 10...Kd8 11. Qxf5 Bb4+ 12. Kf1 d6 13. Qxe5. Why it went wrong: motif: creates threat on e4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kd8 (+1.85), Ke7 (+3.38).

### 12...Qxb2 (mistake, tactical, wp loss 15%)

You played 12...Qxb2. Stockfish preferred f4, after which the main line runs 12...f4 13. Bd2 Qxe4+ 14. Be2 Qe6 15. Qh5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on f5 insufficiently defended; motif: creates threat on e4, e3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: f4 (+1.32), Bb4+ (+1.51), Ba3 (+1.78).

### 14...Qe6 (blunder, tactical, wp loss 28%)

You played 14...Qe6. Stockfish preferred Qe7, after which the main line runs 14...Qe7 15. Qh5 Qc5 16. Qh4 Be7 17. Bb3. Why it went wrong: left queen on e6 insufficiently defended; motif: creates threat on e4. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qe7 (+2.27), Qc3 (+6.14), Be7 (+7.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.29 | +0.19 | e4 | 10 | 1% | best |
| 2 | 1...e5* | +0.19 | +0.17 | e5 | 0 | 0% | best |
| 3 | 2.Nf3 | +0.17 | +0.19 | Nf3 | 0 | 0% | best |
| 4 | 2...Nc6* | +0.19 | +0.20 | Nc6 | 1 | 0% | best |
| 5 | 3.Bc4 | +0.20 | +0.14 | Bb5 | 6 | 1% | excellent |
| 6 | 3...f5* | +0.14 | +1.20 | Nf6 | 106 | 10% | inaccuracy |
| 7 | 4.Nc3 | +1.20 | -1.70 | d4 | 290 | 26% | blunder |
| 8 | 4...Qf6* | -1.70 | +3.19 | fxe4 | 489 | 42% | blunder |
| 9 | 5.Nd5 | +3.19 | +2.98 | O-O | 21 | 1% | excellent |
| 10 | 5...Qd6* | +2.98 | +4.69 | Qd8 | 171 | 10% | inaccuracy |
| 11 | 6.d4 | +4.69 | +4.88 | d4 | 0 | 0% | best |
| 12 | 6...Nf6* | +4.88 | +4.90 | Nf6 | 2 | 0% | best |
| 13 | 7.dxe5 | +4.90 | +5.01 | O-O | 0 | 0% | excellent |
| 14 | 7...Nxe5* | +5.01 | +4.97 | Nxe5 | 0 | 0% | best |
| 15 | 8.Nxe5 | +4.97 | +5.08 | Nxe5 | 0 | 0% | best |
| 16 | 8...Qxe5* | +5.08 | +5.02 | Qxe5 | 0 | 0% | best |
| 17 | 9.Nxf6+ | +5.02 | +1.66 | O-O | 336 | 22% | blunder |
| 18 | 9...gxf6* | +1.66 | +1.77 | gxf6 | 11 | 1% | best |
| 19 | 10.Qh5+ | +1.77 | +1.85 | Qh5+ | 0 | 0% | best |
| 20 | 10...Ke7* | +1.85 | +3.74 | Kd8 | 189 | 13% | mistake |
| 21 | 11.Qf7+ | +3.74 | +1.69 | O-O | 205 | 15% | mistake |
| 22 | 11...Kd8* | +1.69 | +1.93 | Kd8 | 24 | 2% | best |
| 23 | 12.Be3 | +1.93 | +1.32 | Bd2 | 61 | 5% | inaccuracy |
| 24 | 12...Qxb2* | +1.32 | +3.24 | f4 | 192 | 15% | mistake |
| 25 | 13.O-O | +3.24 | +3.22 | O-O | 2 | 0% | best |
| 26 | 13...Qe5* | +3.22 | +3.38 | Qe5 | 16 | 1% | best |
| 27 | 14.Bf4 | +3.38 | +2.27 | Rad1 | 111 | 8% | inaccuracy |
| 28 | 14...Qe6* | +2.27 | +34.50 | Qe7 | 3223 | 28% | blunder |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 3 positional.
- Opening: 4 error(s) (avg wp loss 19%).
- Middlegame: 2 error(s) (avg wp loss 21%).
- 3 of your errors came with under a minute on the clock.
