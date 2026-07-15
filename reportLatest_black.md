# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 85.5%, opponent 85.6%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, You played 2... d5
- Your moves: 15 best, 3 excellent, 2 good, 2 inaccuracy, 1 mistake, 2 blunder

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

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.68), f6 (M7).

## Critical positions

- Ply 10 (you), 5...bxc6: -0.70 -> -0.60 [only-move situation]
- Ply 17 (opponent), 9.Nf3: -1.26 -> -1.28 [only-move situation]
- Ply 38 (you), 19...Bxb1: -3.08 -> +0.00 [evaluation crossed winning -> equal]
- Ply 39 (opponent), 20.Qa4+: +0.00 -> +0.00 [only-move situation]
- Ply 41 (opponent), 21.Bg5+: +0.00 -> -4.68 [only-move situation; evaluation crossed equal -> losing]
- Ply 42 (you), 21...f6: -4.68 -> M7 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (opponent), 22.exf6+: M7 -> M6 [only-move situation]
- Ply 45 (opponent), 23.Qd7+: M4 -> M3 [only-move situation]

## Your errors, move by move

### 8...Be4 (inaccuracy, positional, wp loss 6%)

You played 8...Be4. Stockfish preferred e6, after which the main line runs 8...e6 9. Nf3 Bd6 10. Nc3 h5 11. g5. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-1.98), h5 (-1.83), Be4 (-1.21).

### 12...Qb6 (mistake, positional, wp loss 19%)

You played 12...Qb6. Stockfish preferred e6, after which the main line runs 12...e6 13. Nc3 Bg6 14. Ne2 Be7 15. Nf4. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-2.53), Qd7 (-2.10), Qc8 (-1.75).

### 15...c5 (inaccuracy, positional, wp loss 8%)

You played 15...c5. Stockfish preferred a5, after which the main line runs 15...a5 16. h4 a4 17. h5 Bf5 18. Nd2. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a5 (-2.67), Be7 (-2.17), h6 (-2.11).

### 19...Bxb1 (blunder, tactical, wp loss 26%)

You played 19...Bxb1. Stockfish preferred Qxa2, after which the main line runs 19...Qxa2 20. Ra1 Qb3 21. Ra6 O-O 22. Qd2. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: a favorable capture was available (Bxb1). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxa2 (-3.08), Qxc3 (-2.86), Qa3 (-2.81).

### 21...f6 (blunder, positional, wp loss 85%)

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.68), f6 (M7).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.28 | +0.31 | d4 | 0 | 0% | excellent |
| 2 | 1...c6* | +0.31 | +0.42 | c6 | 11 | 1% | best |
| 3 | 2.Bc4 | +0.42 | -0.40 | Nf3 | 82 | 8% | inaccuracy |
| 4 | 2...d5* | -0.40 | -0.37 | d5 | 3 | 0% | best |
| 5 | 3.exd5 | -0.37 | -0.36 | exd5 | 0 | 0% | best |
| 6 | 3...cxd5* | -0.36 | -0.29 | cxd5 | 7 | 1% | best |
| 7 | 4.Bb5+ | -0.29 | -0.34 | Bb3 | 5 | 0% | excellent |
| 8 | 4...Nc6* | -0.34 | -0.29 | Nc6 | 5 | 0% | best |
| 9 | 5.Bxc6+ | -0.29 | -0.70 | d4 | 41 | 4% | good |
| 10 | 5...bxc6* | -0.70 | -0.60 | bxc6 | 10 | 1% | best |
| 11 | 6.d4 | -0.60 | -0.79 | Nf3 | 19 | 2% | excellent |
| 12 | 6...Bf5* | -0.79 | -0.47 | Ba6 | 32 | 3% | good |
| 13 | 7.g4 | -0.47 | -1.24 | c4 | 77 | 7% | inaccuracy |
| 14 | 7...Bg6* | -1.24 | -1.09 | Bg6 | 15 | 1% | best |
| 15 | 8.f4 | -1.09 | -1.98 | Nf3 | 89 | 8% | inaccuracy |
| 16 | 8...Be4* | -1.98 | -1.26 | e6 | 72 | 6% | inaccuracy |
| 17 | 9.Nf3 | -1.26 | -1.28 | Nf3 | 2 | 0% | best |
| 18 | 9...Nf6* | -1.28 | -0.72 | e6 | 56 | 5% | good |
| 19 | 10.O-O | -0.72 | -2.47 | g5 | 175 | 15% | mistake |
| 20 | 10...Nxg4* | -2.47 | -2.28 | Nxg4 | 19 | 1% | best |
| 21 | 11.Ne5 | -2.28 | -2.57 | Nc3 | 29 | 2% | good |
| 22 | 11...Nxe5* | -2.57 | -2.46 | Nxe5 | 11 | 1% | best |
| 23 | 12.fxe5 | -2.46 | -2.53 | fxe5 | 7 | 1% | best |
| 24 | 12...Qb6* | -2.53 | -0.35 | e6 | 218 | 19% | mistake |
| 25 | 13.c3 | -0.35 | -2.25 | Nc3 | 190 | 16% | mistake |
| 26 | 13...e6* | -2.25 | -2.03 | e6 | 22 | 2% | best |
| 27 | 14.Nd2 | -2.03 | -2.21 | Nd2 | 18 | 1% | best |
| 28 | 14...Bg6* | -2.21 | -2.05 | Bf5 | 16 | 1% | excellent |
| 29 | 15.Nb3 | -2.05 | -2.67 | h4 | 62 | 5% | good |
| 30 | 15...c5* | -2.67 | -1.67 | a5 | 100 | 8% | inaccuracy |
| 31 | 16.Be3 | -1.67 | -1.65 | Be3 | 0 | 0% | best |
| 32 | 16...c4* | -1.65 | -1.60 | cxd4 | 5 | 0% | excellent |
| 33 | 17.Nc5 | -1.60 | -1.58 | Nc5 | 0 | 0% | best |
| 34 | 17...Bxc5* | -1.58 | -1.44 | Bxc5 | 14 | 1% | best |
| 35 | 18.dxc5 | -1.44 | -1.64 | dxc5 | 20 | 2% | best |
| 36 | 18...Qxb2* | -1.64 | -1.67 | Qxb2 | 0 | 0% | best |
| 37 | 19.Rb1 | -1.67 | -3.08 | Qa4+ | 141 | 11% | mistake |
| 38 | 19...Bxb1* | -3.08 | +0.00 | Qxa2 | 308 | 26% | blunder |
| 39 | 20.Qa4+ | +0.00 | +0.00 | Qa4+ | 0 | 0% | best |
| 40 | 20...Ke7* | +0.00 | +0.00 | Ke7 | 0 | 0% | best |
| 41 | 21.Bg5+ | +0.00 | -4.68 | Rxf7+ | 468 | 35% | blunder |
| 42 | 21...f6* | -4.68 | M7 | Kf8 |  | 85% | blunder |
| 43 | 22.exf6+ | M7 | M6 | exf6+ |  | 0% | best |
| 44 | 22...Kf7* | M6 | M4 | gxf6 |  | 0% | excellent |
| 45 | 23.Qd7+ | M4 | M3 | Qd7+ |  | 0% | best |
| 46 | 23...Kg6* | M3 | M3 | Kg6 |  | 0% | best |
| 47 | 24.Qxg7+ | M3 | M2 | Qxg7+ |  | 0% | best |
| 48 | 24...Kh5* | M2 | M2 | Kh5 |  | 0% | best |
| 49 | 25.Qh6+ | M2 | M1 | Qh6+ |  | 0% | best |
| 50 | 25...Kg4* | M1 | M1 | Kg4 |  | 0% | best |
| 51 | 26.Rf4# | M1 | M1 | Qh4# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 1 tactical, 4 positional.
- Opening: 1 error(s) (avg wp loss 6%).
- Middlegame: 4 error(s) (avg wp loss 34%).
