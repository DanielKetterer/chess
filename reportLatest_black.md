# (free, so lmk) Game analysis: mohammed9413 vs DanielKetterer

Date: 2026.07.21  |  Time control: rapid (600)  |  You played: black
Game: https://www.chess.com/game/live/171886517316

## Summary

- Lichess accuracy: you 85.6%, opponent 92.2%
- Opening: D01 Rapport-Jobava System (theory followed through ply 5)
- First deviation from theory: ply 6, You played 3... Bf5
- Your moves: 16 best, 13 excellent, 5 good, 6 inaccuracy, 1 mistake, 1 blunder

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

You played 18...g5. Stockfish preferred Rad8, after which the main line runs 18...Rad8 19. Qd4 Qxd4 20. exd4 Ne8 21. g4. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Rad8 (-2.04), h6 (-1.95), Rfd8 (-1.91).

## Critical positions

- Ply 8 (you), 4...Na6: +0.00 -> +0.00 [only-move situation]
- Ply 20 (you), 10...Qxd6: -0.14 -> -0.12 [only-move situation]
- Ply 26 (you), 13...Nxe5: -1.74 -> -1.82 [only-move situation]
- Ply 27 (opponent), 14.dxe5: -1.82 -> -1.80 [only-move situation]
- Ply 36 (you), 18...g5: -2.04 -> +1.19 [evaluation crossed winning -> equal]
- Ply 41 (opponent), 21.cxd3: +0.14 -> +0.09 [only-move situation]
- Ply 53 (opponent), 27.Rhg3: +3.66 -> +3.70 [only-move situation]
- Ply 55 (opponent), 28.h4: +3.79 -> +3.79 [only-move situation]

## Your errors, move by move

### 12...Ng4 (inaccuracy, positional, wp loss 5%)

You played 12...Ng4. Stockfish preferred c5, after which the main line runs 12...c5 13. Ne2 Nc6 14. c3 Rac8 15. Ng3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: c5 (-0.19), Rfd8 (-0.09), Na6 (+0.00).

### 17...Nc7 (inaccuracy, positional, wp loss 7%)

You played 17...Nc7. Stockfish preferred Nc5, after which the main line runs 17...Nc5 18. Qd2 a5 19. Qd4 Nd7 20. Qd2. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: motif: creates threat on d3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc5 (-2.18), Rfd8 (-2.03), Rac8 (-1.95).

### 18...g5 (blunder, positional, wp loss 29%)

You played 18...g5. Stockfish preferred Rad8, after which the main line runs 18...Rad8 19. Qd4 Qxd4 20. exd4 Ne8 21. g4. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Rad8 (-2.04), h6 (-1.95), Rfd8 (-1.91).

### 21...e5 (inaccuracy, positional, wp loss 7%)

You played 21...e5. Stockfish preferred f6, after which the main line runs 21...f6 22. Rg3 f5 23. Rf1 e5 24. g6. Why it went wrong: motif: creates threat on g5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: f6 (+0.09), Nb5 (+0.24), f5 (+0.35).

### 23...Kg7 (inaccuracy, positional, wp loss 6%)

You played 23...Kg7. Stockfish preferred Rae8, after which the main line runs 23...Rae8 24. Rxe5 Nc5 25. Rxe8 Rxe8 26. d4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on e5 insufficiently defended; your king's zone came under heavier attack after this move. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rae8 (+1.07), e4 (+1.27), Rfe8 (+1.44).

### 26...Nxg5 (mistake, tactical, wp loss 19%)

You played 26...Nxg5. Stockfish preferred d4, after which the main line runs 26...d4 27. exd4 Nxd4 28. Rf6+ Kxg5 29. Rf1. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: fork; creates threat on g5, c3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: d4 (+1.09), Kg7 (+1.92), a5 (+2.41).

### 28...f4 (inaccuracy, positional, wp loss 10%)

You played 28...f4. Stockfish preferred h6, after which the main line runs 28...h6 29. Ne2 Kh5 30. hxg5 hxg5 31. Rh3+. Why it went wrong: left knight on g5 insufficiently defended; motif: creates threat on f3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: h6 (+3.79), Kg7 (+5.62), Rf6 (+5.62).

### 32...Re6 (inaccuracy, positional, wp loss 7%)

You played 32...Re6. Stockfish preferred Re7, after which the main line runs 32...Re7 33. Kg3 Rg7 34. Ne2 Rg6 35. Kf3. Why it went wrong: motif: creates threat on g5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 20; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Re7 (+6.21), a5 (+6.79), b5 (+6.82).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.d4 | +0.31 | +0.25 | Nf3 | 6 | 1% | excellent |
| 2 | 1...Nf6* | +0.25 | +0.27 | Nf6 | 2 | 0% | best |
| 3 | 2.Bf4 | +0.27 | +0.08 | Nf3 | 19 | 2% | excellent |
| 4 | 2...d5* | +0.08 | +0.24 | d5 | 16 | 1% | best |
| 5 | 3.Nc3 | +0.24 | +0.00 | Nf3 | 24 | 2% | good |
| 6 | 3...Bf5* | +0.00 | +0.12 | g6 | 12 | 1% | excellent |
| 7 | 4.Nb5 | +0.12 | +0.00 | e3 | 12 | 1% | excellent |
| 8 | 4...Na6* | +0.00 | +0.00 | Na6 | 0 | 0% | best |
| 9 | 5.e3 | +0.00 | -0.05 | e3 | 5 | 0% | best |
| 10 | 5...c6* | -0.05 | +0.00 | c6 | 5 | 0% | best |
| 11 | 6.Nc3 | +0.00 | +0.00 | Nc3 | 0 | 0% | best |
| 12 | 6...e6* | +0.00 | -0.04 | e6 | 0 | 0% | best |
| 13 | 7.Bd3 | -0.04 | +0.00 | Bxa6 | 0 | 0% | excellent |
| 14 | 7...Bxd3* | +0.00 | +0.00 | Be7 | 0 | 0% | excellent |
| 15 | 8.Qxd3 | +0.00 | -0.31 | cxd3 | 31 | 3% | good |
| 16 | 8...Nb4* | -0.31 | -0.05 | Qb6 | 26 | 2% | good |
| 17 | 9.Qd2 | -0.05 | -0.21 | Qe2 | 16 | 1% | excellent |
| 18 | 9...Bd6* | -0.21 | -0.07 | c5 | 14 | 1% | excellent |
| 19 | 10.Bxd6 | -0.07 | -0.14 | a3 | 7 | 1% | excellent |
| 20 | 10...Qxd6* | -0.14 | -0.12 | Qxd6 | 2 | 0% | best |
| 21 | 11.Nf3 | -0.12 | -0.20 | a3 | 8 | 1% | excellent |
| 22 | 11...O-O* | -0.20 | -0.13 | O-O | 7 | 1% | best |
| 23 | 12.O-O | -0.13 | -0.19 | O-O | 6 | 1% | best |
| 24 | 12...Ng4* | -0.19 | +0.38 | c5 | 57 | 5% | inaccuracy |
| 25 | 13.Ne5 | +0.38 | -1.74 | e4 | 212 | 19% | mistake |
| 26 | 13...Nxe5* | -1.74 | -1.82 | Nxe5 | 0 | 0% | best |
| 27 | 14.dxe5 | -1.82 | -1.80 | dxe5 | 0 | 0% | best |
| 28 | 14...Qxe5* | -1.80 | -1.75 | Qxe5 | 5 | 0% | best |
| 29 | 15.f4 | -1.75 | -1.82 | Rad1 | 7 | 1% | excellent |
| 30 | 15...Qf6* | -1.82 | -1.47 | Qc7 | 35 | 3% | good |
| 31 | 16.a3 | -1.47 | -1.59 | a3 | 12 | 1% | best |
| 32 | 16...Na6* | -1.59 | -1.60 | Na6 | 0 | 0% | best |
| 33 | 17.Qd3 | -1.60 | -2.18 | e4 | 58 | 5% | good |
| 34 | 17...Nc7* | -2.18 | -1.29 | Nc5 | 89 | 7% | inaccuracy |
| 35 | 18.Rf3 | -1.29 | -2.04 | e4 | 75 | 6% | inaccuracy |
| 36 | 18...g5* | -2.04 | +1.19 | Rad8 | 323 | 29% | blunder |
| 37 | 19.Rh3 | +1.19 | +0.11 | fxg5 | 108 | 10% | inaccuracy |
| 38 | 19...Qg6* | +0.11 | +0.12 | Qg6 | 1 | 0% | best |
| 39 | 20.fxg5 | +0.12 | +0.08 | fxg5 | 4 | 0% | best |
| 40 | 20...Qxd3* | +0.08 | +0.14 | f6 | 6 | 1% | excellent |
| 41 | 21.cxd3 | +0.14 | +0.09 | cxd3 | 5 | 0% | best |
| 42 | 21...e5* | +0.09 | +0.81 | f6 | 72 | 7% | inaccuracy |
| 43 | 22.Rf1 | +0.81 | +0.62 | Rf1 | 19 | 2% | best |
| 44 | 22...Ne6* | +0.62 | +1.07 | Rad8 | 45 | 4% | good |
| 45 | 23.Rf5 | +1.07 | +1.07 | Rf5 | 0 | 0% | best |
| 46 | 23...Kg7* | +1.07 | +1.77 | Rae8 | 70 | 6% | inaccuracy |
| 47 | 24.Rxe5 | +1.77 | +1.88 | Rxe5 | 0 | 0% | best |
| 48 | 24...Rae8* | +1.88 | +1.85 | Rae8 | 0 | 0% | best |
| 49 | 25.Rf5 | +1.85 | +1.63 | d4 | 22 | 2% | excellent |
| 50 | 25...Kg6* | +1.63 | +1.97 | d4 | 34 | 3% | good |
| 51 | 26.Rff3 | +1.97 | +1.09 | Rf1 | 88 | 7% | inaccuracy |
| 52 | 26...Nxg5* | +1.09 | +3.66 | d4 | 257 | 19% | mistake |
| 53 | 27.Rhg3 | +3.66 | +3.70 | Rhg3 | 0 | 0% | best |
| 54 | 27...f5* | +3.70 | +3.79 | f6 | 9 | 1% | excellent |
| 55 | 28.h4 | +3.79 | +3.79 | h4 | 0 | 0% | best |
| 56 | 28...f4* | +3.79 | +5.96 | h6 | 217 | 10% | inaccuracy |
| 57 | 29.Rxg5+ | +5.96 | +5.90 | Rxg5+ | 6 | 0% | best |
| 58 | 29...Kh6* | +5.90 | +6.00 | Kf6 | 10 | 0% | excellent |
| 59 | 30.Rxf4 | +6.00 | +5.77 | e4 | 23 | 1% | excellent |
| 60 | 30...Rxf4* | +5.77 | +5.91 | Rg8 | 14 | 0% | excellent |
| 61 | 31.exf4 | +5.91 | +6.30 | exf4 | 0 | 0% | best |
| 62 | 31...Re1+* | +6.30 | +6.49 | Re1+ | 19 | 1% | best |
| 63 | 32.Kh2 | +6.49 | +6.21 | Kf2 | 28 | 1% | excellent |
| 64 | 32...Re6* | +6.21 | +11.00 | Re7 | 479 | 7% | inaccuracy |
| 65 | 33.g4 | +11.00 | +6.02 | f5 | 498 | 7% | inaccuracy |
| 66 | 33...Rg6* | +6.02 | +6.66 | Rg6 | 64 | 2% | best |
| 67 | 34.Rxg6+ | +6.66 | +6.29 | Kg3 | 37 | 1% | excellent |
| 68 | 34...Kxg6* | +6.29 | +7.01 | Kxg6 | 72 | 2% | best |
| 69 | 35.f5+ | +7.01 | +7.24 | f5+ | 0 | 0% | best |
| 70 | 35...Kf6* | +7.24 | +7.31 | Kg7 | 7 | 0% | excellent |
| 71 | 36.Kg3 | +7.31 | +7.39 | d4 | 0 | 0% | excellent |
| 72 | 36...h6* | +7.39 | +11.35 | Ke5 | 396 | 4% | good |
| 73 | 37.Kf4 | +11.35 | +34.13 | Kf4 | 0 | 0% | best |
| 74 | 37...b5* | +34.13 | +38.50 | d4 | 437 | 0% | excellent |
| 75 | 38.g5+ | +38.50 | +39.32 | Nxb5 | 0 | 0% | excellent |
| 76 | 38...hxg5+* | +39.32 | +43.91 | Kg7 | 459 | 0% | excellent |
| 77 | 39.hxg5+ | +43.91 | +43.96 | hxg5+ | 0 | 0% | best |
| 78 | 39...Kg7* | +43.96 | M14 | Kf7 |  | 0% | excellent |
| 79 | 40.f6+ | M14 | M13 | f6+ |  | 0% | best |
| 80 | 40...Kg6* | M13 | M12 | Kg6 |  | 0% | best |
| 81 | 41.Ne2 | M12 | M11 | Ke5 |  | 0% | excellent |
| 82 | 41...Kf7* | M11 | M10 | b4 |  | 0% | excellent |
| 83 | 42.Ng3 | M10 | M21 | Ke5 |  | 0% | excellent |
| 84 | 42...Kg6* | M21 | M11 | Ke6 |  | 0% | excellent |
| 85 | 43.Ne2 | M11 | M10 | Ke5 |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 1 tactical, 7 positional.
- Middlegame: 7 error(s) (avg wp loss 12%).
- Endgame: 1 error(s) (avg wp loss 7%).
- 2 of your errors came with under a minute on the clock.
