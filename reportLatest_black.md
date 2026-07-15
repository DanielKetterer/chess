# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 85.9%, opponent 86.0%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, You played 2... d5
- Your moves: 14 best, 5 excellent, 1 good, 2 inaccuracy, 1 mistake, 2 blunder

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

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.85), f6 (M7).

## Critical positions

- Ply 10 (you), 5...bxc6: -0.73 -> -0.71 [only-move situation]
- Ply 17 (opponent), 9.Nf3: -1.16 -> -1.22 [only-move situation]
- Ply 38 (you), 19...Bxb1: -3.24 -> +0.00 [evaluation crossed winning -> equal]
- Ply 39 (opponent), 20.Qa4+: +0.00 -> +0.00 [only-move situation]
- Ply 41 (opponent), 21.Bg5+: +0.00 -> -4.85 [only-move situation; evaluation crossed equal -> losing]
- Ply 42 (you), 21...f6: -4.85 -> M7 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (opponent), 22.exf6+: M7 -> M6 [only-move situation]
- Ply 45 (opponent), 23.Qd7+: M4 -> M3 [only-move situation]

## Your errors, move by move

### 8...Be4 (inaccuracy, positional, wp loss 7%)

You played 8...Be4. Stockfish preferred e6, after which the main line runs 8...e6 9. Nf3 Bd6 10. O-O h5 11. g5. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-1.95), h5 (-1.84), Be4 (-1.16).

### 12...Qb6 (mistake, positional, wp loss 19%)

You played 12...Qb6. Stockfish preferred e6, after which the main line runs 12...e6 13. Nc3 Bg6 14. Ne2 Be7 15. Be3. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-2.43), Qd7 (-1.99), Qc8 (-1.88).

### 15...c5 (inaccuracy, positional, wp loss 9%)

You played 15...c5. Stockfish preferred a5, after which the main line runs 15...a5 16. Rf2 a4 17. Nd2 c5 18. Nf3. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a5 (-2.75), Be7 (-2.29), h6 (-2.24).

### 19...Bxb1 (blunder, tactical, wp loss 27%)

You played 19...Bxb1. Stockfish preferred Qxa2, after which the main line runs 19...Qxa2 20. Rb7 O-O 21. Qa1 Qc2 22. Bd4. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: a favorable capture was available (Bxb1). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxa2 (-3.24), Qxc3 (-2.88), Qa3 (-2.83).

### 21...f6 (blunder, positional, wp loss 86%)

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-4.85), f6 (M7).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.40 | +0.36 | e4 | 4 | 0% | best |
| 2 | 1...c6* | +0.36 | +0.43 | e5 | 7 | 1% | excellent |
| 3 | 2.Bc4 | +0.43 | -0.45 | d4 | 88 | 8% | inaccuracy |
| 4 | 2...d5* | -0.45 | -0.34 | d5 | 11 | 1% | best |
| 5 | 3.exd5 | -0.34 | -0.41 | exd5 | 7 | 1% | best |
| 6 | 3...cxd5* | -0.41 | -0.30 | cxd5 | 11 | 1% | best |
| 7 | 4.Bb5+ | -0.30 | -0.38 | Bb5+ | 8 | 1% | best |
| 8 | 4...Nc6* | -0.38 | -0.22 | Bd7 | 16 | 1% | excellent |
| 9 | 5.Bxc6+ | -0.22 | -0.73 | Nf3 | 51 | 5% | good |
| 10 | 5...bxc6* | -0.73 | -0.71 | bxc6 | 2 | 0% | best |
| 11 | 6.d4 | -0.71 | -0.76 | Nf3 | 5 | 0% | excellent |
| 12 | 6...Bf5* | -0.76 | -0.57 | Ba6 | 19 | 2% | excellent |
| 13 | 7.g4 | -0.57 | -1.14 | c4 | 57 | 5% | inaccuracy |
| 14 | 7...Bg6* | -1.14 | -1.11 | Bg6 | 3 | 0% | best |
| 15 | 8.f4 | -1.11 | -1.95 | Nf3 | 84 | 7% | inaccuracy |
| 16 | 8...Be4* | -1.95 | -1.16 | e6 | 79 | 7% | inaccuracy |
| 17 | 9.Nf3 | -1.16 | -1.22 | Nf3 | 6 | 1% | best |
| 18 | 9...Nf6* | -1.22 | -0.82 | Qc8 | 40 | 4% | good |
| 19 | 10.O-O | -0.82 | -2.41 | g5 | 159 | 13% | mistake |
| 20 | 10...Nxg4* | -2.41 | -2.33 | Nxg4 | 8 | 1% | best |
| 21 | 11.Ne5 | -2.33 | -2.42 | Nc3 | 9 | 1% | excellent |
| 22 | 11...Nxe5* | -2.42 | -2.56 | Nxe5 | 0 | 0% | best |
| 23 | 12.fxe5 | -2.56 | -2.43 | fxe5 | 0 | 0% | best |
| 24 | 12...Qb6* | -2.43 | -0.26 | e6 | 217 | 19% | mistake |
| 25 | 13.c3 | -0.26 | -2.24 | Nc3 | 198 | 17% | mistake |
| 26 | 13...e6* | -2.24 | -2.11 | e6 | 13 | 1% | best |
| 27 | 14.Nd2 | -2.11 | -2.06 | Nd2 | 0 | 0% | best |
| 28 | 14...Bg6* | -2.06 | -1.95 | Bg6 | 11 | 1% | best |
| 29 | 15.Nb3 | -1.95 | -2.75 | h4 | 80 | 6% | inaccuracy |
| 30 | 15...c5* | -2.75 | -1.59 | a5 | 116 | 9% | inaccuracy |
| 31 | 16.Be3 | -1.59 | -1.61 | Be3 | 2 | 0% | best |
| 32 | 16...c4* | -1.61 | -1.39 | cxd4 | 22 | 2% | excellent |
| 33 | 17.Nc5 | -1.39 | -1.45 | Nc5 | 6 | 1% | best |
| 34 | 17...Bxc5* | -1.45 | -1.72 | Bxc5 | 0 | 0% | best |
| 35 | 18.dxc5 | -1.72 | -1.76 | Qa4+ | 4 | 0% | excellent |
| 36 | 18...Qxb2* | -1.76 | -1.70 | Qxb2 | 6 | 0% | best |
| 37 | 19.Rb1 | -1.70 | -3.24 | Qa4+ | 154 | 12% | mistake |
| 38 | 19...Bxb1* | -3.24 | +0.00 | Qxa2 | 324 | 27% | blunder |
| 39 | 20.Qa4+ | +0.00 | +0.00 | Qa4+ | 0 | 0% | best |
| 40 | 20...Ke7* | +0.00 | +0.00 | Ke7 | 0 | 0% | best |
| 41 | 21.Bg5+ | +0.00 | -4.85 | Rxf7+ | 485 | 36% | blunder |
| 42 | 21...f6* | -4.85 | M7 | Kf8 |  | 86% | blunder |
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
- Opening: 1 error(s) (avg wp loss 7%).
- Middlegame: 4 error(s) (avg wp loss 35%).
