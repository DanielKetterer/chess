# (free, so lmk) Game analysis: Neuromorphic vs DanielKetterer

Date: 2024.10.22  |  Time control: daily (1/259200)  |  You played: white
Game: https://www.chess.com/game/daily/719246613

## Summary

- Lichess accuracy: you 61.6%, opponent 50.2%
- Opening: C50 Italian Game: Rousseau Gambit (theory followed through ply 6)
- First deviation from theory: ply 7, You played 4. Nc3
- Your moves: 6 best, 3 excellent, 0 good, 2 inaccuracy, 1 mistake, 2 blunder

METRICS:

Best: The played move exactly matches Stockfish's top move

Excellent: A non-best move that loses 2 WP points or less.

Good: WP loss is over 2, but under 5 points; also used for losses under 20 when the position remains already decided.

Inaccuracy: WP loss is at least 5 but under 10 points.

Mistake: WP loss is at least 10 but under 20 points; also generally used when a forced mate is missed with under 10 points of WP loss.

Blunder: WP loss is 20 points or more, or a forced mate is missed with at least 10 points of WP loss.

See: https://support.chess.com/en/articles/8572705-how-are-moves-classified-what-is-a-blunder-or-brilliant-etc 

(Brillint, Great and Miss are rating subjective)
![Evaluation graph](reportLatest_white.png)

## Biggest missed opportunity

You played 4.Nc3. Stockfish preferred d4, after which the main line runs 4. d4 exd4 5. e5 d5 6. exd6 cxd6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on f5. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 3; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: d4 (+1.20), d3 (+1.11), Bxg8 (-0.06).

## Critical positions

- Ply 7 (you), 4.Nc3: +1.20 -> -1.70 [evaluation crossed equal -> losing]
- Ply 8 (opponent), 4...Qf6: -1.70 -> +3.19 [only-move situation; evaluation crossed winning -> losing]
- Ply 17 (you), 9.Nxf6+: +5.02 -> +1.66 [only-move situation; evaluation crossed winning -> equal]
- Ply 22 (opponent), 11...Kd8: +1.69 -> +1.93 [only-move situation]
- Ply 25 (you), 13.O-O: +3.24 -> +3.22 [only-move situation]
- Ply 28 (opponent), 14...Qe6: +2.27 -> +34.50 [only-move situation]

## Your errors, move by move

### 4.Nc3 (blunder, tactical, wp loss 26%)

You played 4.Nc3. Stockfish preferred d4, after which the main line runs 4. d4 exd4 5. e5 d5 6. exd6 cxd6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on f5. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 3; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: d4 (+1.20), d3 (+1.11), Bxg8 (-0.06).

### 9.Nxf6+ (blunder, tactical, wp loss 22%)

You played 9.Nxf6+. Stockfish preferred O-O, after which the main line runs 9. O-O fxe4 10. Bf4 Qf5 11. Nxc7+ Kd8. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left knight on f6 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: O-O (+5.02), Nxf6+ (+1.70), Be3 (+0.64).

### 11.Qf7+ (mistake, tactical, wp loss 15%)

You played 11.Qf7+. Stockfish preferred O-O, after which the main line runs 11. O-O f4 12. Qf3 Bh6 13. Rd1 Qg5. Why it went wrong: left queen on f7, pawn on e4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: O-O (+3.74), Bd2 (+3.47), Qxf5 (+1.79).

### 12.Be3 (inaccuracy, positional, wp loss 5%)

You played 12.Be3. Stockfish preferred Bd2, after which the main line runs 12. Bd2 Qxe4+ 13. Kf1 Qe7 14. Qh5 Qe4. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left pawn on e4, pawn on b2 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Bd2 (+1.93), Bf4 (+1.84), O-O (+1.67).

### 14.Bf4 (inaccuracy, positional, wp loss 8%)

You played 14.Bf4. Stockfish preferred Rad1, after which the main line runs 14. Rad1 Qe7 15. Qh5 fxe4 16. Rfe1 Bg7. Why it went wrong: left bishop on f4, pawn on e4 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rad1 (+3.38), exf5 (+2.92), Bf4 (+2.07).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.29 | +0.19 | e4 | 10 | 1% | best |
| 2 | 1...e5 | +0.19 | +0.17 | e5 | 0 | 0% | best |
| 3 | 2.Nf3* | +0.17 | +0.19 | Nf3 | 0 | 0% | best |
| 4 | 2...Nc6 | +0.19 | +0.20 | Nc6 | 1 | 0% | best |
| 5 | 3.Bc4* | +0.20 | +0.14 | Bb5 | 6 | 1% | excellent |
| 6 | 3...f5 | +0.14 | +1.20 | Nf6 | 106 | 10% | inaccuracy |
| 7 | 4.Nc3* | +1.20 | -1.70 | d4 | 290 | 26% | blunder |
| 8 | 4...Qf6 | -1.70 | +3.19 | fxe4 | 489 | 42% | blunder |
| 9 | 5.Nd5* | +3.19 | +2.98 | O-O | 21 | 1% | excellent |
| 10 | 5...Qd6 | +2.98 | +4.69 | Qd8 | 171 | 10% | inaccuracy |
| 11 | 6.d4* | +4.69 | +4.88 | d4 | 0 | 0% | best |
| 12 | 6...Nf6 | +4.88 | +4.90 | Nf6 | 2 | 0% | best |
| 13 | 7.dxe5* | +4.90 | +5.01 | O-O | 0 | 0% | excellent |
| 14 | 7...Nxe5 | +5.01 | +4.97 | Nxe5 | 0 | 0% | best |
| 15 | 8.Nxe5* | +4.97 | +5.08 | Nxe5 | 0 | 0% | best |
| 16 | 8...Qxe5 | +5.08 | +5.02 | Qxe5 | 0 | 0% | best |
| 17 | 9.Nxf6+* | +5.02 | +1.66 | O-O | 336 | 22% | blunder |
| 18 | 9...gxf6 | +1.66 | +1.77 | gxf6 | 11 | 1% | best |
| 19 | 10.Qh5+* | +1.77 | +1.85 | Qh5+ | 0 | 0% | best |
| 20 | 10...Ke7 | +1.85 | +3.74 | Kd8 | 189 | 13% | mistake |
| 21 | 11.Qf7+* | +3.74 | +1.69 | O-O | 205 | 15% | mistake |
| 22 | 11...Kd8 | +1.69 | +1.93 | Kd8 | 24 | 2% | best |
| 23 | 12.Be3* | +1.93 | +1.32 | Bd2 | 61 | 5% | inaccuracy |
| 24 | 12...Qxb2 | +1.32 | +3.24 | f4 | 192 | 15% | mistake |
| 25 | 13.O-O* | +3.24 | +3.22 | O-O | 2 | 0% | best |
| 26 | 13...Qe5 | +3.22 | +3.38 | Qe5 | 16 | 1% | best |
| 27 | 14.Bf4* | +3.38 | +2.27 | Rad1 | 111 | 8% | inaccuracy |
| 28 | 14...Qe6 | +2.27 | +34.50 | Qe7 | 3223 | 28% | blunder |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 2 positional.
- Opening: 2 error(s) (avg wp loss 24%).
- Middlegame: 3 error(s) (avg wp loss 9%).
