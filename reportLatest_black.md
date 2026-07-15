# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171535977872

## Summary

- Lichess accuracy: you 40.6%, opponent 77.5%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, You played 2... d5
- Your moves: 15 best, 2 excellent, 3 good, 2 inaccuracy, 1 mistake, 2 blunder

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

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-5.66), f6 (M7).

## Critical positions

- Ply 10 (you), 5...bxc6: -0.66 -> -0.64 [only-move situation]
- Ply 17 (opponent), 9.Nf3: -1.39 -> -1.43 [only-move situation]
- Ply 38 (you), 19...Bxb1: -3.43 -> +0.00 [evaluation crossed winning -> equal]
- Ply 39 (opponent), 20.Qa4+: +0.00 -> +0.00 [only-move situation]
- Ply 41 (opponent), 21.Bg5+: +0.00 -> -5.66 [only-move situation; evaluation crossed equal -> losing]
- Ply 42 (you), 21...f6: -5.66 -> M7 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (opponent), 22.exf6+: M7 -> M6 [only-move situation]
- Ply 45 (opponent), 23.Qd7+: M4 -> M3 [only-move situation]

## Your errors, move by move

### 9...Nf6 (inaccuracy, positional, wp loss 5%)

You played 9...Nf6. Stockfish preferred e6, after which the main line runs 9...e6 10. Nbd2 Bd6 11. Nxe4 dxe4 12. Ng5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-1.43), h5 (-1.29), a5 (-1.07).

### 12...Qb6 (mistake, positional, wp loss 18%)

You played 12...Qb6. Stockfish preferred e6, after which the main line runs 12...e6 13. Nc3 Bg6 14. Ne2 Be7 15. Be3. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e6 (-2.56), Qd7 (-2.04), f5 (-1.85).

### 15...c5 (inaccuracy, positional, wp loss 9%)

You played 15...c5. Stockfish preferred a5, after which the main line runs 15...a5 16. Rf2 a4 17. Nd2 c5 18. Nf3. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a5 (-2.76), Be7 (-2.26), h6 (-2.25).

### 19...Bxb1 (blunder, tactical, wp loss 28%)

You played 19...Bxb1. Stockfish preferred Qxc3, after which the main line runs 19...Qxc3 20. Qa4+ Kf8 21. Rf3 Kg8 22. Qxa7. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: a favorable capture was available (Bxb1). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qxc3 (-3.43), Qxa2 (-3.31), Qa3 (-2.91).

### 21...f6 (blunder, positional, wp loss 86%)

You played 21...f6. Stockfish preferred Kf8, after which the main line runs 21...Kf8 22. Qc6 Qb8 23. Qxe6 Bg6 24. Qxd5. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on c3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kf8 (-5.66), f6 (M7).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.27 | +0.18 | Nf3 | 9 | 1% | excellent |
| 2 | 1...c6* | +0.18 | +0.40 | e5 | 22 | 2% | good |
| 3 | 2.Bc4 | +0.40 | -0.35 | d4 | 75 | 7% | inaccuracy |
| 4 | 2...d5* | -0.35 | -0.38 | d5 | 0 | 0% | best |
| 5 | 3.exd5 | -0.38 | -0.35 | exd5 | 0 | 0% | best |
| 6 | 3...cxd5* | -0.35 | -0.31 | cxd5 | 4 | 0% | best |
| 7 | 4.Bb5+ | -0.31 | -0.38 | Bb5+ | 7 | 1% | best |
| 8 | 4...Nc6* | -0.38 | -0.24 | Bd7 | 14 | 1% | excellent |
| 9 | 5.Bxc6+ | -0.24 | -0.66 | Nf3 | 42 | 4% | good |
| 10 | 5...bxc6* | -0.66 | -0.64 | bxc6 | 2 | 0% | best |
| 11 | 6.d4 | -0.64 | -0.75 | Nf3 | 11 | 1% | excellent |
| 12 | 6...Bf5* | -0.75 | -0.42 | Nf6 | 33 | 3% | good |
| 13 | 7.g4 | -0.42 | -1.24 | c4 | 82 | 7% | inaccuracy |
| 14 | 7...Bg6* | -1.24 | -1.23 | Bg6 | 1 | 0% | best |
| 15 | 8.f4 | -1.23 | -1.92 | Nf3 | 69 | 6% | inaccuracy |
| 16 | 8...Be4* | -1.92 | -1.39 | e6 | 53 | 4% | good |
| 17 | 9.Nf3 | -1.39 | -1.43 | Nf3 | 4 | 0% | best |
| 18 | 9...Nf6* | -1.43 | -0.86 | e6 | 57 | 5% | inaccuracy |
| 19 | 10.O-O | -0.86 | -2.39 | g5 | 153 | 13% | mistake |
| 20 | 10...Nxg4* | -2.39 | -2.47 | Nxg4 | 0 | 0% | best |
| 21 | 11.Ne5 | -2.47 | -2.45 | Ne5 | 0 | 0% | best |
| 22 | 11...Nxe5* | -2.45 | -2.52 | Nxe5 | 0 | 0% | best |
| 23 | 12.fxe5 | -2.52 | -2.56 | fxe5 | 4 | 0% | best |
| 24 | 12...Qb6* | -2.56 | -0.39 | e6 | 217 | 18% | mistake |
| 25 | 13.c3 | -0.39 | -2.23 | Nc3 | 184 | 16% | mistake |
| 26 | 13...e6* | -2.23 | -2.00 | e6 | 23 | 2% | best |
| 27 | 14.Nd2 | -2.00 | -2.25 | Nd2 | 25 | 2% | best |
| 28 | 14...Bg6* | -2.25 | -2.15 | Bg6 | 10 | 1% | best |
| 29 | 15.Nb3 | -2.15 | -2.76 | h4 | 61 | 5% | good |
| 30 | 15...c5* | -2.76 | -1.57 | a5 | 119 | 9% | inaccuracy |
| 31 | 16.Be3 | -1.57 | -1.67 | Be3 | 10 | 1% | best |
| 32 | 16...c4* | -1.67 | -1.75 | c4 | 0 | 0% | best |
| 33 | 17.Nc5 | -1.75 | -1.95 | Nc5 | 20 | 2% | best |
| 34 | 17...Bxc5* | -1.95 | -1.79 | Bxc5 | 16 | 1% | best |
| 35 | 18.dxc5 | -1.79 | -1.94 | dxc5 | 15 | 1% | best |
| 36 | 18...Qxb2* | -1.94 | -2.00 | Qxb2 | 0 | 0% | best |
| 37 | 19.Rb1 | -2.00 | -3.43 | Qa4+ | 143 | 10% | mistake |
| 38 | 19...Bxb1* | -3.43 | +0.00 | Qxc3 | 343 | 28% | blunder |
| 39 | 20.Qa4+ | +0.00 | +0.00 | Qa4+ | 0 | 0% | best |
| 40 | 20...Ke7* | +0.00 | +0.00 | Ke7 | 0 | 0% | best |
| 41 | 21.Bg5+ | +0.00 | -5.66 | Rxf7+ | 566 | 39% | blunder |
| 42 | 21...f6* | -5.66 | M7 | Kf8 |  | 86% | blunder |
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
- Opening: 1 error(s) (avg wp loss 5%).
- Middlegame: 4 error(s) (avg wp loss 36%).
