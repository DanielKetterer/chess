# (free, so lmk) Game analysis: mohammed9413 vs DanielKetterer

Date: 2026.07.21  |  Time control: rapid (600)  |  You played: white
Game: https://www.chess.com/game/live/171886517316

## Summary

- Lichess accuracy: you 92.2%, opponent 85.6%
- Opening: D01 Rapport-Jobava System (theory followed through ply 5)
- First deviation from theory: ply 6, Opponent played 3... Bf5
- Your moves: 18 best, 17 excellent, 3 good, 4 inaccuracy, 1 mistake, 0 blunder

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

You played 13.Ne5. Stockfish preferred e4, after which the main line runs 13. e4 Qe7 14. Rfe1 Nf6 15. e5 Nd7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e4 (+0.38), a3 (+0.34), h3 (+0.17).

## Critical positions

- Ply 8 (opponent), 4...Na6: +0.00 -> +0.00 [only-move situation]
- Ply 20 (opponent), 10...Qxd6: -0.14 -> -0.12 [only-move situation]
- Ply 26 (opponent), 13...Nxe5: -1.74 -> -1.82 [only-move situation]
- Ply 27 (you), 14.dxe5: -1.82 -> -1.80 [only-move situation]
- Ply 36 (opponent), 18...g5: -2.04 -> +1.19 [evaluation crossed winning -> equal]
- Ply 41 (you), 21.cxd3: +0.14 -> +0.09 [only-move situation]
- Ply 53 (you), 27.Rhg3: +3.66 -> +3.70 [only-move situation]
- Ply 55 (you), 28.h4: +3.79 -> +3.79 [only-move situation]

## Your errors, move by move

### 13.Ne5 (mistake, positional, wp loss 19%)

You played 13.Ne5. Stockfish preferred e4, after which the main line runs 13. e4 Qe7 14. Rfe1 Nf6 15. e5 Nd7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e4 (+0.38), a3 (+0.34), h3 (+0.17).

### 18.Rf3 (inaccuracy, positional, wp loss 6%)

You played 18.Rf3. Stockfish preferred e4, after which the main line runs 18. e4 Qe7 19. e5 a5 20. Nd1 Na6. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e4 (-1.29), Rad1 (-1.65), h3 (-1.77).

### 19.Rh3 (inaccuracy, positional, wp loss 10%)

You played 19.Rh3. Stockfish preferred fxg5, after which the main line runs 19. fxg5 Qg6 20. Qe2 Ne8 21. Raf1 Kh8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: fxg5 (+1.19), Rg3 (+0.62), Rh3 (+0.17).

### 26.Rff3 (inaccuracy, positional, wp loss 7%)

You played 26.Rff3. Stockfish preferred Rf1, after which the main line runs 26. Rf1 Kg7 27. Ne2 a5 28. Rhf3 Kg8. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left pawn on g5 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 19; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rf1 (+1.97), Rf6+ (+1.81), Rf2 (+1.60).

### 33.g4 (inaccuracy, positional, wp loss 7%)

You played 33.g4. Stockfish preferred f5, after which the main line runs 33. f5 Re5 34. Nd1 Rxf5 35. Rxf5 Kg6. Why it went wrong: left rook on g5 insufficiently defended; motif: creates threat on e6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: f5 (+11.00), Kg3 (+6.17), Nd1 (+5.82).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.d4* | +0.31 | +0.25 | Nf3 | 6 | 1% | excellent |
| 2 | 1...Nf6 | +0.25 | +0.27 | Nf6 | 2 | 0% | best |
| 3 | 2.Bf4* | +0.27 | +0.08 | Nf3 | 19 | 2% | excellent |
| 4 | 2...d5 | +0.08 | +0.24 | d5 | 16 | 1% | best |
| 5 | 3.Nc3* | +0.24 | +0.00 | Nf3 | 24 | 2% | good |
| 6 | 3...Bf5 | +0.00 | +0.12 | g6 | 12 | 1% | excellent |
| 7 | 4.Nb5* | +0.12 | +0.00 | e3 | 12 | 1% | excellent |
| 8 | 4...Na6 | +0.00 | +0.00 | Na6 | 0 | 0% | best |
| 9 | 5.e3* | +0.00 | -0.05 | e3 | 5 | 0% | best |
| 10 | 5...c6 | -0.05 | +0.00 | c6 | 5 | 0% | best |
| 11 | 6.Nc3* | +0.00 | +0.00 | Nc3 | 0 | 0% | best |
| 12 | 6...e6 | +0.00 | -0.04 | e6 | 0 | 0% | best |
| 13 | 7.Bd3* | -0.04 | +0.00 | Bxa6 | 0 | 0% | excellent |
| 14 | 7...Bxd3 | +0.00 | +0.00 | Be7 | 0 | 0% | excellent |
| 15 | 8.Qxd3* | +0.00 | -0.31 | cxd3 | 31 | 3% | good |
| 16 | 8...Nb4 | -0.31 | -0.05 | Qb6 | 26 | 2% | good |
| 17 | 9.Qd2* | -0.05 | -0.21 | Qe2 | 16 | 1% | excellent |
| 18 | 9...Bd6 | -0.21 | -0.07 | c5 | 14 | 1% | excellent |
| 19 | 10.Bxd6* | -0.07 | -0.14 | a3 | 7 | 1% | excellent |
| 20 | 10...Qxd6 | -0.14 | -0.12 | Qxd6 | 2 | 0% | best |
| 21 | 11.Nf3* | -0.12 | -0.20 | a3 | 8 | 1% | excellent |
| 22 | 11...O-O | -0.20 | -0.13 | O-O | 7 | 1% | best |
| 23 | 12.O-O* | -0.13 | -0.19 | O-O | 6 | 1% | best |
| 24 | 12...Ng4 | -0.19 | +0.38 | c5 | 57 | 5% | inaccuracy |
| 25 | 13.Ne5* | +0.38 | -1.74 | e4 | 212 | 19% | mistake |
| 26 | 13...Nxe5 | -1.74 | -1.82 | Nxe5 | 0 | 0% | best |
| 27 | 14.dxe5* | -1.82 | -1.80 | dxe5 | 0 | 0% | best |
| 28 | 14...Qxe5 | -1.80 | -1.75 | Qxe5 | 5 | 0% | best |
| 29 | 15.f4* | -1.75 | -1.82 | Rad1 | 7 | 1% | excellent |
| 30 | 15...Qf6 | -1.82 | -1.47 | Qc7 | 35 | 3% | good |
| 31 | 16.a3* | -1.47 | -1.59 | a3 | 12 | 1% | best |
| 32 | 16...Na6 | -1.59 | -1.60 | Na6 | 0 | 0% | best |
| 33 | 17.Qd3* | -1.60 | -2.18 | e4 | 58 | 5% | good |
| 34 | 17...Nc7 | -2.18 | -1.29 | Nc5 | 89 | 7% | inaccuracy |
| 35 | 18.Rf3* | -1.29 | -2.04 | e4 | 75 | 6% | inaccuracy |
| 36 | 18...g5 | -2.04 | +1.19 | Rad8 | 323 | 29% | blunder |
| 37 | 19.Rh3* | +1.19 | +0.11 | fxg5 | 108 | 10% | inaccuracy |
| 38 | 19...Qg6 | +0.11 | +0.12 | Qg6 | 1 | 0% | best |
| 39 | 20.fxg5* | +0.12 | +0.08 | fxg5 | 4 | 0% | best |
| 40 | 20...Qxd3 | +0.08 | +0.14 | f6 | 6 | 1% | excellent |
| 41 | 21.cxd3* | +0.14 | +0.09 | cxd3 | 5 | 0% | best |
| 42 | 21...e5 | +0.09 | +0.81 | f6 | 72 | 7% | inaccuracy |
| 43 | 22.Rf1* | +0.81 | +0.62 | Rf1 | 19 | 2% | best |
| 44 | 22...Ne6 | +0.62 | +1.07 | Rad8 | 45 | 4% | good |
| 45 | 23.Rf5* | +1.07 | +1.07 | Rf5 | 0 | 0% | best |
| 46 | 23...Kg7 | +1.07 | +1.77 | Rae8 | 70 | 6% | inaccuracy |
| 47 | 24.Rxe5* | +1.77 | +1.88 | Rxe5 | 0 | 0% | best |
| 48 | 24...Rae8 | +1.88 | +1.85 | Rae8 | 0 | 0% | best |
| 49 | 25.Rf5* | +1.85 | +1.63 | d4 | 22 | 2% | excellent |
| 50 | 25...Kg6 | +1.63 | +1.97 | d4 | 34 | 3% | good |
| 51 | 26.Rff3* | +1.97 | +1.09 | Rf1 | 88 | 7% | inaccuracy |
| 52 | 26...Nxg5 | +1.09 | +3.66 | d4 | 257 | 19% | mistake |
| 53 | 27.Rhg3* | +3.66 | +3.70 | Rhg3 | 0 | 0% | best |
| 54 | 27...f5 | +3.70 | +3.79 | f6 | 9 | 1% | excellent |
| 55 | 28.h4* | +3.79 | +3.79 | h4 | 0 | 0% | best |
| 56 | 28...f4 | +3.79 | +5.96 | h6 | 217 | 10% | inaccuracy |
| 57 | 29.Rxg5+* | +5.96 | +5.90 | Rxg5+ | 6 | 0% | best |
| 58 | 29...Kh6 | +5.90 | +6.00 | Kf6 | 10 | 0% | excellent |
| 59 | 30.Rxf4* | +6.00 | +5.77 | e4 | 23 | 1% | excellent |
| 60 | 30...Rxf4 | +5.77 | +5.91 | Rg8 | 14 | 0% | excellent |
| 61 | 31.exf4* | +5.91 | +6.30 | exf4 | 0 | 0% | best |
| 62 | 31...Re1+ | +6.30 | +6.49 | Re1+ | 19 | 1% | best |
| 63 | 32.Kh2* | +6.49 | +6.21 | Kf2 | 28 | 1% | excellent |
| 64 | 32...Re6 | +6.21 | +11.00 | Re7 | 479 | 7% | inaccuracy |
| 65 | 33.g4* | +11.00 | +6.02 | f5 | 498 | 7% | inaccuracy |
| 66 | 33...Rg6 | +6.02 | +6.66 | Rg6 | 64 | 2% | best |
| 67 | 34.Rxg6+* | +6.66 | +6.29 | Kg3 | 37 | 1% | excellent |
| 68 | 34...Kxg6 | +6.29 | +7.01 | Kxg6 | 72 | 2% | best |
| 69 | 35.f5+* | +7.01 | +7.24 | f5+ | 0 | 0% | best |
| 70 | 35...Kf6 | +7.24 | +7.31 | Kg7 | 7 | 0% | excellent |
| 71 | 36.Kg3* | +7.31 | +7.39 | d4 | 0 | 0% | excellent |
| 72 | 36...h6 | +7.39 | +11.35 | Ke5 | 396 | 4% | good |
| 73 | 37.Kf4* | +11.35 | +34.13 | Kf4 | 0 | 0% | best |
| 74 | 37...b5 | +34.13 | +38.50 | d4 | 437 | 0% | excellent |
| 75 | 38.g5+* | +38.50 | +39.32 | Nxb5 | 0 | 0% | excellent |
| 76 | 38...hxg5+ | +39.32 | +43.91 | Kg7 | 459 | 0% | excellent |
| 77 | 39.hxg5+* | +43.91 | +43.96 | hxg5+ | 0 | 0% | best |
| 78 | 39...Kg7 | +43.96 | M14 | Kf7 |  | 0% | excellent |
| 79 | 40.f6+* | M14 | M13 | f6+ |  | 0% | best |
| 80 | 40...Kg6 | M13 | M12 | Kg6 |  | 0% | best |
| 81 | 41.Ne2* | M12 | M11 | Ke5 |  | 0% | excellent |
| 82 | 41...Kf7 | M11 | M10 | b4 |  | 0% | excellent |
| 83 | 42.Ng3* | M10 | M21 | Ke5 |  | 0% | excellent |
| 84 | 42...Kg6 | M21 | M11 | Ke6 |  | 0% | excellent |
| 85 | 43.Ne2* | M11 | M10 | Ke5 |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 0 tactical, 5 positional.
- Middlegame: 4 error(s) (avg wp loss 11%).
- Endgame: 1 error(s) (avg wp loss 7%).
