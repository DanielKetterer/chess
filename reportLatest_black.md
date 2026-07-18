# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.18  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171750428224

## Summary

- Lichess accuracy: you 98.1%, opponent 86.2%
- Opening: B18 Caro-Kann Defense: Classical Variation (theory followed through ply 8)
- First deviation from theory: ply 9, Opponent played 5. Qf3
- Your moves: 16 best, 22 excellent, 3 good, 0 inaccuracy, 1 mistake, 0 blunder

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

You played 30...Rxh2. Stockfish preferred R8e3+, after which the main line runs 30...R8e3+ 31. Kf4 g5+ 32. Kf5 Kg7 33. c5. There was a forced mate on the board and this move let it slip. Why it went wrong: the best move was a forcing check; motif: creates threat on h2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: R8e3+ (-M4), Re1 (-M16), R2e3+ (-M18).

## Critical positions

- Ply 11 (opponent), 6.Qxe4: +0.36 -> +0.40 [only-move situation]
- Ply 28 (you), 14...Nxf6: -0.03 -> +0.00 [only-move situation]
- Ply 44 (you), 22...Nxf7: -0.69 -> -0.77 [only-move situation]
- Ply 45 (opponent), 23.Qh5: -0.77 -> -5.90 [only-move situation; evaluation crossed equal -> losing]
- Ply 48 (you), 24...Qxf7: -6.95 -> -6.81 [only-move situation]
- Ply 50 (you), 25...Kxf7: -6.74 -> -7.06 [only-move situation]
- Ply 60 (you), 30...Rxh2: -M4 -> -33.84 [forced mate was on the board]

## Your errors, move by move

### 30...Rxh2 (mistake, positional, wp loss 0%)

You played 30...Rxh2. Stockfish preferred R8e3+, after which the main line runs 30...R8e3+ 31. Kf4 g5+ 32. Kf5 Kg7 33. c5. There was a forced mate on the board and this move let it slip. Why it went wrong: the best move was a forcing check; motif: creates threat on h2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: R8e3+ (-M4), Re1 (-M16), R2e3+ (-M18).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.32 | +0.26 | e4 | 6 | 1% | best |
| 2 | 1...c6* | +0.26 | +0.26 | e5 | 0 | 0% | excellent |
| 3 | 2.d4 | +0.26 | +0.23 | Nf3 | 3 | 0% | excellent |
| 4 | 2...d5* | +0.23 | +0.28 | d5 | 5 | 0% | best |
| 5 | 3.Nc3 | +0.28 | +0.25 | Nc3 | 3 | 0% | best |
| 6 | 3...dxe4* | +0.25 | +0.31 | dxe4 | 6 | 1% | best |
| 7 | 4.Nxe4 | +0.31 | +0.27 | Nxe4 | 4 | 0% | best |
| 8 | 4...Bf5* | +0.27 | +0.31 | Bf5 | 4 | 0% | best |
| 9 | 5.Qf3 | +0.31 | +0.19 | Ng3 | 12 | 1% | excellent |
| 10 | 5...Bxe4* | +0.19 | +0.36 | e6 | 17 | 2% | excellent |
| 11 | 6.Qxe4 | +0.36 | +0.40 | Qxe4 | 0 | 0% | best |
| 12 | 6...Nf6* | +0.40 | +0.46 | Nf6 | 6 | 1% | best |
| 13 | 7.Qe3 | +0.46 | +0.36 | Qe3 | 10 | 1% | best |
| 14 | 7...e6* | +0.36 | +0.47 | e6 | 11 | 1% | best |
| 15 | 8.Nf3 | +0.47 | +0.40 | Nf3 | 7 | 1% | best |
| 16 | 8...Bd6* | +0.40 | +0.49 | Nd5 | 9 | 1% | excellent |
| 17 | 9.Bc4 | +0.49 | +0.13 | g3 | 36 | 3% | good |
| 18 | 9...Nbd7* | +0.13 | +0.20 | Qc7 | 7 | 1% | excellent |
| 19 | 10.O-O | +0.20 | +0.10 | Qe2 | 10 | 1% | excellent |
| 20 | 10...Nd5* | +0.10 | +0.46 | O-O | 36 | 3% | good |
| 21 | 11.Qe2 | +0.46 | +0.35 | Qe2 | 11 | 1% | best |
| 22 | 11...O-O* | +0.35 | +0.39 | Qc7 | 4 | 0% | excellent |
| 23 | 12.Bg5 | +0.39 | +0.07 | c3 | 32 | 3% | good |
| 24 | 12...N5f6* | +0.07 | +0.31 | Nf4 | 24 | 2% | good |
| 25 | 13.Ne5 | +0.31 | +0.27 | Bb3 | 4 | 0% | excellent |
| 26 | 13...h6* | +0.27 | +0.56 | Qc7 | 29 | 3% | good |
| 27 | 14.Bxf6 | +0.56 | -0.03 | Bh4 | 59 | 5% | inaccuracy |
| 28 | 14...Nxf6* | -0.03 | +0.00 | Nxf6 | 3 | 0% | best |
| 29 | 15.Ng4 | +0.00 | -0.16 | Nxf7 | 16 | 1% | excellent |
| 30 | 15...Nh7* | -0.16 | +0.05 | Nxg4 | 21 | 2% | excellent |
| 31 | 16.f4 | +0.05 | +0.00 | f4 | 5 | 0% | best |
| 32 | 16...Re8* | +0.00 | +0.17 | Qb6 | 17 | 2% | excellent |
| 33 | 17.Ne5 | +0.17 | +0.00 | Rae1 | 17 | 2% | excellent |
| 34 | 17...Qb6* | +0.00 | +0.21 | Re7 | 21 | 2% | excellent |
| 35 | 18.Rad1 | +0.21 | -0.09 | Kh1 | 30 | 3% | good |
| 36 | 18...Qxb2* | -0.09 | -0.01 | Bxe5 | 8 | 1% | excellent |
| 37 | 19.f5 | -0.01 | +0.00 | f5 | 0 | 0% | best |
| 38 | 19...Bxe5* | +0.00 | +0.00 | Bxe5 | 0 | 0% | best |
| 39 | 20.dxe5 | +0.00 | +0.00 | dxe5 | 0 | 0% | best |
| 40 | 20...exf5* | +0.00 | -0.01 | Re7 | 0 | 0% | excellent |
| 41 | 21.Rxf5 | -0.01 | +0.00 | Rxf5 | 0 | 0% | best |
| 42 | 21...Ng5* | +0.00 | +0.00 | Re7 | 0 | 0% | excellent |
| 43 | 22.Bxf7+ | +0.00 | -0.69 | h4 | 69 | 6% | inaccuracy |
| 44 | 22...Nxf7* | -0.69 | -0.77 | Nxf7 | 0 | 0% | best |
| 45 | 23.Qh5 | -0.77 | -5.90 | Rxf7 | 513 | 33% | blunder |
| 46 | 23...Qxa2* | -5.90 | -5.65 | Nxe5 | 25 | 1% | excellent |
| 47 | 24.Qxf7+ | -5.65 | -6.95 | Rd7 | 130 | 4% | good |
| 48 | 24...Qxf7* | -6.95 | -6.81 | Qxf7 | 14 | 0% | best |
| 49 | 25.Rxf7 | -6.81 | -6.74 | Rxf7 | 0 | 0% | best |
| 50 | 25...Kxf7* | -6.74 | -7.06 | Kxf7 | 0 | 0% | best |
| 51 | 26.Rf1+ | -7.06 | -9.11 | Rb1 | 205 | 4% | good |
| 52 | 26...Kg8* | -9.11 | -10.27 | Kg8 | 0 | 0% | best |
| 53 | 27.g4 | -10.27 | -12.10 | Ra1 | 183 | 0% | excellent |
| 54 | 27...Rxe5* | -12.10 | -14.66 | a5 | 0 | 0% | excellent |
| 55 | 28.c4 | -14.66 | -33.52 | h4 | 1886 | 0% | excellent |
| 56 | 28...Rae8* | -33.52 | -32.82 | a5 | 70 | 0% | excellent |
| 57 | 29.Kg2 | -32.82 | -96.05 | Rf3 | 6323 | 0% | excellent |
| 58 | 29...Re2+* | -96.05 | -M29 | Re2+ |  | 0% | best |
| 59 | 30.Kf3 | -M29 | -M4 | Kg3 |  | 0% | excellent |
| 60 | 30...Rxh2* | -M4 | -33.84 | R8e3+ |  | 0% | mistake |
| 61 | 31.Kf4 | -33.84 | -M14 | Rd1 |  | 0% | excellent |
| 62 | 31...Rf8+* | -M14 | -M13 | Rhe2 |  | 0% | excellent |
| 63 | 32.Kg3 | -M13 | -M13 | Kg3 |  | 0% | best |
| 64 | 32...Rxf1* | -M13 | -M12 | Rxf1 |  | 0% | best |
| 65 | 33.Kxh2 | -M12 | -M10 | Kxh2 |  | 0% | best |
| 66 | 33...Rc1* | -M10 | -M12 | a5 |  | 0% | excellent |
| 67 | 34.Kh3 | -M12 | -M12 | Kg3 |  | 0% | excellent |
| 68 | 34...Rxc4* | -M12 | -M11 | Rc3+ |  | 0% | excellent |
| 69 | 35.Kh4 | -M11 | -M11 | Kh4 |  | 0% | best |
| 70 | 35...a5* | -M11 | -M9 | a5 |  | 0% | best |
| 71 | 36.Kh5 | -M9 | -M9 | Kh5 |  | 0% | best |
| 72 | 36...a4* | -M9 | -M8 | Kh7 |  | 0% | excellent |
| 73 | 37.Kg6 | -M8 | -M2 | g5 |  | 0% | excellent |
| 74 | 37...a3* | -M2 | -M6 | Rc5 |  | 0% | excellent |
| 75 | 38.Kf5 | -M6 | -M6 | Kf5 |  | 0% | best |
| 76 | 38...a2* | -M6 | -M5 | a2 |  | 0% | best |
| 77 | 39.Ke6 | -M5 | -M5 | Ke6 |  | 0% | best |
| 78 | 39...a1=Q* | -M5 | -M5 | Rd4 |  | 0% | excellent |
| 79 | 40.Ke7 | -M5 | -M3 | Kd7 |  | 0% | excellent |
| 80 | 40...Qe1+* | -M3 | -M4 | Rd4 |  | 0% | excellent |
| 81 | 41.Kd6 | -M4 | -M4 | Kd8 |  | 0% | excellent |
| 82 | 41...Qd2+* | -M4 | -M5 | Rd4+ |  | 0% | excellent |
| 83 | 42.Ke7 | -M5 | -M1 | Kc7 |  | 0% | excellent |
| 84 | 42...Re4#* | -M1 | -M1 | Re4# |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 0 tactical, 1 positional.
- Middlegame: 1 error(s) (avg wp loss 0%).
