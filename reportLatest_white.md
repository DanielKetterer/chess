# (free, so lmk) Game analysis: DanielKetterer vs BlessTheBoard

Date: 2026.07.19  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171778732108

## Summary

- Lichess accuracy: you 88.6%, opponent 66.1%
- Opening: C50 Italian Game: Giuoco Pianissimo, Normal (theory followed through ply 8)
- First deviation from theory: ply 9, You played 5. Be3
- Your moves: 4 best, 8 excellent, 1 good, 0 inaccuracy, 1 mistake, 0 blunder

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

You played 6.d4. Stockfish preferred O-O, after which the main line runs 6. O-O O-O 7. Nc3 d6 8. a4 Bg4. Why it went wrong: left pawn on e4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 17; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: O-O (+0.10), Bxb6 (+0.00), Nc3 (+0.00).

## Critical positions

- Ply 16 (opponent), 8...exd4: +0.18 -> +0.16 [only-move situation]
- Ply 26 (opponent), 13...Rac8: +0.92 -> +5.89 [evaluation crossed equal -> losing]

## Your errors, move by move

### 6.d4 (mistake, tactical, wp loss 10%)

You played 6.d4. Stockfish preferred O-O, after which the main line runs 6. O-O O-O 7. Nc3 d6 8. a4 Bg4. Why it went wrong: left pawn on e4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 17; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: O-O (+0.10), Bxb6 (+0.00), Nc3 (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.35 | +0.25 | d4 | 10 | 1% | excellent |
| 2 | 1...e5 | +0.25 | +0.26 | e5 | 1 | 0% | best |
| 3 | 2.Nf3* | +0.26 | +0.18 | Nf3 | 8 | 1% | best |
| 4 | 2...Nc6 | +0.18 | +0.21 | Nc6 | 3 | 0% | best |
| 5 | 3.Bc4* | +0.21 | +0.18 | Bb5 | 3 | 0% | excellent |
| 6 | 3...Nf6 | +0.18 | +0.16 | Bc5 | 0 | 0% | excellent |
| 7 | 4.d3* | +0.16 | +0.20 | d3 | 0 | 0% | best |
| 8 | 4...Bc5 | +0.20 | +0.24 | Bc5 | 4 | 0% | best |
| 9 | 5.Be3* | +0.24 | +0.05 | O-O | 19 | 2% | excellent |
| 10 | 5...Bb6 | +0.05 | +0.10 | Bxe3 | 5 | 0% | excellent |
| 11 | 6.d4* | +0.10 | -1.03 | O-O | 113 | 10% | mistake |
| 12 | 6...d6 | -1.03 | +0.13 | exd4 | 116 | 11% | mistake |
| 13 | 7.d5* | +0.13 | -0.20 | dxe5 | 33 | 3% | good |
| 14 | 7...Nd4 | -0.20 | +0.29 | Bxe3 | 49 | 5% | good |
| 15 | 8.Nxd4* | +0.29 | +0.18 | Nxd4 | 11 | 1% | best |
| 16 | 8...exd4 | +0.18 | +0.16 | exd4 | 0 | 0% | best |
| 17 | 9.Bxd4* | +0.16 | +0.25 | Bxd4 | 0 | 0% | best |
| 18 | 9...Nxe4 | +0.25 | +0.11 | Nxe4 | 0 | 0% | best |
| 19 | 10.Qd3* | +0.11 | -0.04 | Bxb6 | 15 | 1% | excellent |
| 20 | 10...Bf5 | -0.04 | +0.00 | Bf5 | 4 | 0% | best |
| 21 | 11.O-O* | +0.00 | -0.02 | Bb5+ | 2 | 0% | excellent |
| 22 | 11...Qg5 | -0.02 | +0.25 | O-O | 27 | 2% | good |
| 23 | 12.Bb5+* | +0.25 | +0.05 | Bxb6 | 20 | 2% | excellent |
| 24 | 12...Ke7 | +0.05 | +0.96 | Kd8 | 91 | 8% | inaccuracy |
| 25 | 13.Re1* | +0.96 | +0.92 | Bxb6 | 4 | 0% | excellent |
| 26 | 13...Rac8 | +0.92 | +5.89 | Kf8 | 497 | 31% | blunder |
| 27 | 14.Nc3* | +5.89 | +5.77 | Nd2 | 12 | 0% | excellent |
| 28 | 14...Qf4 | +5.77 | +5.98 | Bxd4 | 21 | 1% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 1 tactical, 0 positional.
- Opening: 1 error(s) (avg wp loss 10%).
