# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 87.8%, opponent 87.1%
- Opening: not matched in the ECO database
- First deviation from theory: ply 1, Opponent played 1. e4
- Your moves: 10 best, 7 excellent, 4 good, 2 inaccuracy, 1 mistake, 1 blunder

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

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qd7 Bf5 23. Be7+ Kg8. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.27), f6 (+11.41).

## Critical positions

- Ply 10 (you), 5...bxc6: -0.70 -> -0.73 [only-move situation]
- Ply 17 (opponent), 9.Nf3: -1.33 -> -1.53 [only-move situation]
- Ply 42 (you), 21...f6: -4.27 -> +8.29 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (opponent), 22.exf6+: +8.29 -> M8 [only-move situation]
- Ply 45 (opponent), 23.Qd7+: M4 -> M3 [only-move situation]
- Ply 47 (opponent), 24.Qxg7+: M3 -> M2 [only-move situation]

## Your errors, move by move

### 9...Nf6 (inaccuracy, positional, wp loss 9%)

You played 9...Nf6. Stockfish preferred e6, after which the main line runs 9...e6 10. Nc3 h5 11. g5 Bf5 12. Nh4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-1.53), h5 (-1.47), Qc8 (-1.19).

### 12...Qb6 (mistake, positional, wp loss 14%)

You played 12...Qb6. Stockfish preferred e6, after which the main line runs 12...e6 13. Nc3 Bf5 14. Rf2 Be7 15. Rg2. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-2.42), Qc8 (-2.00), g6 (-1.86).

### 15...c5 (inaccuracy, positional, wp loss 9%)

You played 15...c5. Stockfish preferred a5, after which the main line runs 15...a5 16. h4 a4 17. Nd2 c5 18. h5. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a5 (-2.76), Be7 (-2.46), Rb8 (-2.18).

### 21...f6 (blunder, positional, wp loss 78%)

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qd7 Bf5 23. Be7+ Kg8. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.27), f6 (+11.41).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.49 | +0.32 | e4 | 17 | 2% | best |
| 2 | 1...c6* | +0.32 | +0.63 | c5 | 31 | 3% | good |
| 3 | 2.Bc4 | +0.63 | -0.21 | d4 | 84 | 8% | inaccuracy |
| 4 | 2...d5* | -0.21 | -0.42 | d5 | 0 | 0% | best |
| 5 | 3.exd5 | -0.42 | -0.37 | exd5 | 0 | 0% | best |
| 6 | 3...cxd5* | -0.37 | -0.24 | cxd5 | 13 | 1% | best |
| 7 | 4.Bb5+ | -0.24 | -0.40 | Bb5+ | 16 | 1% | best |
| 8 | 4...Nc6* | -0.40 | -0.31 | Bd7 | 9 | 1% | excellent |
| 9 | 5.Bxc6+ | -0.31 | -0.70 | Nf3 | 39 | 4% | good |
| 10 | 5...bxc6* | -0.70 | -0.73 | bxc6 | 0 | 0% | best |
| 11 | 6.d4 | -0.73 | -0.78 | d4 | 5 | 0% | best |
| 12 | 6...Bf5* | -0.78 | -0.66 | e6 | 12 | 1% | excellent |
| 13 | 7.g4 | -0.66 | -1.10 | Nf3 | 44 | 4% | good |
| 14 | 7...Bg6* | -1.10 | -1.05 | Bc8 | 5 | 0% | excellent |
| 15 | 8.f4 | -1.05 | -1.69 | Nf3 | 64 | 6% | inaccuracy |
| 16 | 8...Be4* | -1.69 | -1.33 | e6 | 36 | 3% | good |
| 17 | 9.Nf3 | -1.33 | -1.53 | Nf3 | 20 | 2% | best |
| 18 | 9...Nf6* | -1.53 | -0.51 | e6 | 102 | 9% | inaccuracy |
| 19 | 10.O-O | -0.51 | -2.02 | g5 | 151 | 13% | mistake |
| 20 | 10...Nxg4* | -2.02 | -2.02 | Nxg4 | 0 | 0% | best |
| 21 | 11.Ne5 | -2.02 | -2.42 | c4 | 40 | 3% | good |
| 22 | 11...Nxe5* | -2.42 | -2.42 | Nxe5 | 0 | 0% | best |
| 23 | 12.fxe5 | -2.42 | -2.42 | fxe5 | 0 | 0% | best |
| 24 | 12...Qb6* | -2.42 | -0.75 | e6 | 167 | 14% | mistake |
| 25 | 13.c3 | -0.75 | -2.32 | Nc3 | 157 | 13% | mistake |
| 26 | 13...e6* | -2.32 | -2.31 | e6 | 1 | 0% | best |
| 27 | 14.Nd2 | -2.31 | -2.41 | Rf2 | 10 | 1% | excellent |
| 28 | 14...Bg6* | -2.41 | -2.29 | Bf5 | 12 | 1% | excellent |
| 29 | 15.Nb3 | -2.29 | -2.76 | Rf2 | 47 | 4% | good |
| 30 | 15...c5* | -2.76 | -1.58 | a5 | 118 | 9% | inaccuracy |
| 31 | 16.Be3 | -1.58 | -1.68 | Be3 | 10 | 1% | best |
| 32 | 16...c4* | -1.68 | -1.47 | cxd4 | 21 | 2% | excellent |
| 33 | 17.Nc5 | -1.47 | -1.41 | Nc5 | 0 | 0% | best |
| 34 | 17...Bxc5* | -1.41 | -1.36 | Qa5 | 5 | 0% | excellent |
| 35 | 18.dxc5 | -1.36 | -1.61 | Qa4+ | 25 | 2% | good |
| 36 | 18...Qxb2* | -1.61 | -1.43 | Qxb2 | 18 | 2% | best |
| 37 | 19.Rb1 | -1.43 | -3.28 | Qa4+ | 185 | 14% | mistake |
| 38 | 19...Bxb1* | -3.28 | -2.92 | Qxc3 | 36 | 2% | good |
| 39 | 20.Qa4+ | -2.92 | -3.42 | Qa4+ | 50 | 3% | best |
| 40 | 20...Ke7* | -3.42 | -2.79 | Kf8 | 63 | 4% | good |
| 41 | 21.Bg5+ | -2.79 | -4.27 | c6 | 148 | 9% | inaccuracy |
| 42 | 21...f6* | -4.27 | +8.29 | Kf8 | 1256 | 78% | blunder |
| 43 | 22.exf6+ | +8.29 | M8 | exf6+ |  | 0% | best |
| 44 | 22...Kf7* | M8 | M4 | gxf6 |  | 0% | excellent |
| 45 | 23.Qd7+ | M4 | M3 | Qd7+ |  | 0% | best |
| 46 | 23...Kg6* | M3 | M3 | Kg6 |  | 0% | best |
| 47 | 24.Qxg7+ | M3 | M2 | Qxg7+ |  | 0% | best |
| 48 | 24...Kh5* | M2 | M2 | Kh5 |  | 0% | best |
| 49 | 25.Qh6+ | M2 | M1 | Qh6+ |  | 0% | best |
| 50 | 25...Kg4* | M1 | M1 | Kg4 |  | 0% | best |
| 51 | 26.Rf4# | M1 | M1 | Qh4# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 0 tactical, 4 positional.
- Opening: 1 error(s) (avg wp loss 9%).
- Middlegame: 3 error(s) (avg wp loss 34%).
