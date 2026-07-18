# (free, so lmk) Game analysis: Mirrorwahl vs DanielKetterer

Date: 2026.07.17  |  Time control: rapid (600)  |  You played: white
Game: https://www.chess.com/game/live/171717445934

## Summary

- Lichess accuracy: you 81.8%, opponent 68.2%
- Opening: D00 Queen's Pawn Game: Accelerated London System (theory followed through ply 3)
- First deviation from theory: ply 4, Opponent played 2... Nc6
- Your moves: 10 best, 3 excellent, 3 good, 0 inaccuracy, 3 mistake, 1 blunder

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

You played 11.c5. Stockfish preferred O-O-O, after which the main line runs 11. O-O-O dxc4 12. d5 Ne5 13. Bxe5 fxe5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on d4 insufficiently defended; motif: creates threat on c7. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: O-O-O (-0.52), Nf3 (-1.10), Rd1 (-1.19).

## Critical positions

- Ply 21 (you), 11.c5: -0.52 -> -3.05 [evaluation crossed equal -> losing]
- Ply 26 (opponent), 13...Bxd4: -4.91 -> -5.02 [only-move situation]
- Ply 28 (opponent), 14...O-O: -5.51 -> -0.03 [evaluation crossed winning -> equal]
- Ply 29 (you), 15.Nxd4: -0.03 -> +0.00 [only-move situation]
- Ply 30 (opponent), 15...Nc6: +0.00 -> +2.60 [evaluation crossed equal -> losing]

## Your errors, move by move

### 8.Qh5+ (mistake, tactical, wp loss 13%)

You played 8.Qh5+. Stockfish preferred Nf3, after which the main line runs 8. Nf3 Nge7 9. Be2 dxc4 10. Bxc4 Bxc3+. Why it went wrong: left pawn on d4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nf3 (+0.62), Ne2 (+0.34), Be2 (+0.19).

### 10.Qxe7+ (mistake, tactical, wp loss 10%)

You played 10.Qxe7+. Stockfish preferred cxd5, after which the main line runs 10. cxd5 Nxd4 11. Qxe7+ Nxe7 12. O-O-O c5. Why it went wrong: left queen on e7, pawn on d4 insufficiently defended; a favorable capture was available (cxd5). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: cxd5 (+0.53), O-O-O (+0.21), Nf3 (+0.00).

### 11.c5 (blunder, tactical, wp loss 21%)

You played 11.c5. Stockfish preferred O-O-O, after which the main line runs 11. O-O-O dxc4 12. d5 Ne5 13. Bxe5 fxe5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on d4 insufficiently defended; motif: creates threat on c7. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: O-O-O (-0.52), Nf3 (-1.10), Rd1 (-1.19).

### 13.Rxd4 (mistake, tactical, wp loss 11%)

You played 13.Rxd4. Stockfish preferred Na4, after which the main line runs 13. Na4 Ne6 14. Nxc5 Nxc5 15. Nf3 Kf7. Why it went wrong: left rook on d4 insufficiently defended; motif: creates threat on c7, c5. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 5; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Na4 (-2.96), h4 (-3.21), Nge2 (-3.21).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.d4* | +0.31 | +0.24 | d4 | 7 | 1% | best |
| 2 | 1...d5 | +0.24 | +0.26 | Nf6 | 2 | 0% | excellent |
| 3 | 2.Bf4* | +0.26 | +0.06 | c4 | 20 | 2% | excellent |
| 4 | 2...Nc6 | +0.06 | +0.42 | c5 | 36 | 3% | good |
| 5 | 3.e3* | +0.42 | +0.36 | e3 | 6 | 1% | best |
| 6 | 3...f6 | +0.36 | +0.73 | Nf6 | 37 | 3% | good |
| 7 | 4.c4* | +0.73 | +0.31 | Bd3 | 42 | 4% | good |
| 8 | 4...e5 | +0.31 | +0.46 | e5 | 15 | 1% | best |
| 9 | 5.Bg3* | +0.46 | -0.01 | cxd5 | 47 | 4% | good |
| 10 | 5...exd4 | -0.01 | +0.00 | Bb4+ | 1 | 0% | excellent |
| 11 | 6.exd4* | +0.00 | +0.00 | exd4 | 0 | 0% | best |
| 12 | 6...Bb4+ | +0.00 | +0.10 | Nge7 | 10 | 1% | excellent |
| 13 | 7.Nc3* | +0.10 | +0.10 | Nc3 | 0 | 0% | best |
| 14 | 7...Bf5 | +0.10 | +0.62 | Nge7 | 52 | 5% | good |
| 15 | 8.Qh5+* | +0.62 | -0.75 | Nf3 | 137 | 13% | mistake |
| 16 | 8...g6 | -0.75 | -0.78 | Bg6 | 0 | 0% | excellent |
| 17 | 9.Qe2+* | -0.78 | -1.07 | Qd1 | 29 | 3% | good |
| 18 | 9...Qe7 | -1.07 | +0.53 | Nge7 | 160 | 15% | mistake |
| 19 | 10.Qxe7+* | +0.53 | -0.56 | cxd5 | 109 | 10% | mistake |
| 20 | 10...Ngxe7 | -0.56 | -0.52 | Ngxe7 | 4 | 0% | best |
| 21 | 11.c5* | -0.52 | -3.05 | O-O-O | 253 | 21% | blunder |
| 22 | 11...Nxd4 | -3.05 | -2.87 | Nxd4 | 18 | 1% | best |
| 23 | 12.O-O-O* | -2.87 | -3.00 | O-O-O | 13 | 1% | best |
| 24 | 12...Bxc5 | -3.00 | -2.96 | Bxc5 | 4 | 0% | best |
| 25 | 13.Rxd4* | -2.96 | -4.91 | Na4 | 195 | 11% | mistake |
| 26 | 13...Bxd4 | -4.91 | -5.02 | Bxd4 | 0 | 0% | best |
| 27 | 14.Nb5* | -5.02 | -5.51 | Nf3 | 49 | 2% | excellent |
| 28 | 14...O-O | -5.51 | -0.03 | Bb6 | 548 | 38% | blunder |
| 29 | 15.Nxd4* | -0.03 | +0.00 | Nxd4 | 0 | 0% | best |
| 30 | 15...Nc6 | +0.00 | +2.60 | Bd7 | 260 | 22% | blunder |
| 31 | 16.Nxf5* | +2.60 | +2.73 | Nxf5 | 0 | 0% | best |
| 32 | 16...gxf5 | +2.73 | +2.69 | gxf5 | 0 | 0% | best |
| 33 | 17.Bd3* | +2.69 | +2.68 | Nf3 | 1 | 0% | excellent |
| 34 | 17...Rfe8 | +2.68 | +2.84 | Rae8 | 16 | 1% | excellent |
| 35 | 18.Nf3* | +2.84 | +2.81 | Nf3 | 3 | 0% | best |
| 36 | 18...Re6 | +2.81 | +3.42 | Re4 | 61 | 4% | good |
| 37 | 19.Bxf5* | +3.42 | +3.43 | Bxf5 | 0 | 0% | best |
| 38 | 19...Rd6 | +3.43 | +5.60 | Re7 | 217 | 11% | mistake |
| 39 | 20.Bxd6* | +5.60 | +5.61 | Bxd6 | 0 | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 4 tactical, 0 positional.
- Opening: 2 error(s) (avg wp loss 11%).
- Middlegame: 2 error(s) (avg wp loss 16%).
