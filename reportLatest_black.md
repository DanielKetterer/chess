# (free, so lmk) Game analysis: alesandro777888 vs DanielKetterer

Date: 2026.07.19  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171795040624

## Summary

- Lichess accuracy: you 73.5%, opponent 77.8%
- Opening: C22 Center Game: Normal Variation (theory followed through ply 6)
- First deviation from theory: ply 7, Opponent played 4. Qd5
- Your moves: 21 best, 15 excellent, 0 good, 7 inaccuracy, 5 mistake, 4 blunder

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

You played 19...g5. Stockfish preferred c6, after which the main line runs 19...c6 20. b4 Bb6 21. Bxc6 Rf6 22. Kf1. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on b7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: c6 (-1.54), Rfe8 (-1.24), a5 (-1.07).

## Critical positions

- Ply 20 (you), 10...Ne5: -3.46 -> -0.12 [evaluation crossed winning -> equal]
- Ply 22 (you), 11...Qxe5: -0.14 -> -0.11 [only-move situation]
- Ply 23 (opponent), 12.h4: -0.11 -> -3.64 [evaluation crossed equal -> losing]
- Ply 27 (opponent), 14.Bg2: -2.74 -> -7.97
- Ply 29 (opponent), 15.c3: -3.21 -> -11.53
- Ply 32 (you), 16...Kh8: -4.33 -> -4.42 [only-move situation]
- Ply 34 (you), 17...Qe7: -4.27 -> -4.52 [only-move situation]
- Ply 38 (you), 19...g5: -1.54 -> +2.80 [evaluation crossed equal -> losing]

## Your errors, move by move

### 5...Qe7 (inaccuracy, positional, wp loss 6%)

You played 5...Qe7. Stockfish preferred Bb4+, after which the main line runs 5...Bb4+ 6. c3 Bc5 7. Be2 Qe7 8. Nf3. Why it went wrong: the best move was a forcing check. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 20; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Bb4+ (-1.28), d5 (-1.18), Bc5 (-1.11).

### 7...dxe4 (inaccuracy, positional, wp loss 5%)

You played 7...dxe4. Stockfish preferred Be6, after which the main line runs 7...Be6 8. Bg5 d4 9. Nd1 O-O-O 10. a3. Why it went wrong: your king's zone came under heavier attack after this move. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 12; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Be6 (-2.34), dxe4 (-1.67), Nb4 (-0.91).

### 8...Nxe4 (mistake, tactical, wp loss 11%)

You played 8...Nxe4. Stockfish preferred Nb4, after which the main line runs 8...Nb4 9. Qe2 Nxe4 10. fxe4 Bg4 11. Qxg4. Why it went wrong: left knight on e4 insufficiently defended; motif: creates threat on d3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nb4 (-3.30), Bf5 (-2.17), Nxe4 (-1.71).

### 9...Bg4 (inaccuracy, positional, wp loss 7%)

You played 9...Bg4. Stockfish preferred Nb4, after which the main line runs 9...Nb4 10. Qe2 Bg4 11. Qxg4 Nxc2+ 12. Kf2. Why it went wrong: motif: creates threat on d3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 14; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nb4 (-3.28), Bf5 (-3.09), Bg4 (-2.26).

### 10...Ne5 (blunder, positional, wp loss 27%)

You played 10...Ne5. Stockfish preferred Rd8, after which the main line runs 10...Rd8 11. Qe3 Bxf3 12. Qxf3 Nd4 13. Qd3. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: motif: creates threat on d3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rd8 (-3.46), Nb4 (-2.41), f5 (-1.73).

### 13...f5 (mistake, positional, wp loss 17%)

You played 13...f5. Stockfish preferred Rd8, after which the main line runs 13...Rd8 14. Bf4 Qe7 15. Bh3 Rxd3 16. cxd3. Why it went wrong: motif: creates threat on d3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rd8 (-6.10), O-O (-5.37), Qe7 (-2.64).

### 14...O-O (mistake, positional, wp loss 18%)

You played 14...O-O. Stockfish preferred Rd8, after which the main line runs 14...Rd8 15. Qb5+ Rd7 16. Bf4 Qd4 17. Rf1. Why it went wrong: motif: creates threat on d3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rd8 (-7.97), fxe4 (-5.61), Rf8 (-5.21).

### 15...Rad8 (mistake, tactical, wp loss 15%)

You played 15...Rad8. Stockfish preferred fxe4, after which the main line runs 15...fxe4 16. Bf4 exd3+ 17. Bxe5 Rad8 18. Bf3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 4; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: fxe4 (-11.53), Bf2+ (-10.73), Kh8 (-5.81).

### 18...h6 (mistake, tactical, wp loss 20%)

You played 18...h6. Stockfish preferred Rfe8, after which the main line runs 18...Rfe8 19. a4 Qd6 20. Qe2 Bxe2 21. exd6. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left pawn on b7 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 3; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Rfe8 (-4.44), b5 (-3.87), a5 (-2.78).

### 19...g5 (blunder, positional, wp loss 38%)

You played 19...g5. Stockfish preferred c6, after which the main line runs 19...c6 20. b4 Bb6 21. Bxc6 Rf6 22. Kf1. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on b7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: c6 (-1.54), Rfe8 (-1.24), a5 (-1.07).

### 21...Bd6 (blunder, positional, wp loss 23%)

You played 21...Bd6. Stockfish preferred Rd6, after which the main line runs 21...Rd6 22. Bxd6 Qxd6 23. Qd5 Qxg3+ 24. Kd2. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 11; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rd6 (+0.00), Rfe8 (+0.09), Rg8 (+1.77).

### 23...Kg7 (blunder, positional, wp loss 28%)

You played 23...Kg7. Stockfish preferred c6, after which the main line runs 23...c6 24. Bg2 Rd6 25. O-O Rxe6 26. b4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: motif: creates threat on d5; your king's zone came under heavier attack after this move. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 17; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: c6 (+0.17), Rd6 (+2.00), Qd6 (+2.75).

### 25...Rh8 (inaccuracy, positional, wp loss 7%)

You played 25...Rh8. Stockfish preferred Qd6, after which the main line runs 25...Qd6 26. Qxd6 Rxd6 27. Bc4 Re8 28. Rh2. Why it went wrong: motif: creates threat on g5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qd6 (+3.08), Rb8 (+3.38), Rd6 (+3.50).

### 26...h4 (inaccuracy, positional, wp loss 6%)

You played 26...h4. Stockfish preferred c6, after which the main line runs 26...c6 27. Bc4 a5 28. Rh2 a4 29. Re1. Why it went wrong: motif: creates threat on g5, d5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: c6 (+3.48), Rhe8 (+3.85), a5 (+3.89).

### 30...Kf8 (inaccuracy, positional, wp loss 7%)

You played 30...Kf8. Stockfish preferred Rd6, after which the main line runs 30...Rd6 31. Re1 c6 32. e7 Re8 33. Bh1. Why it went wrong: left bishop on g4, pawn on h3 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rd6 (+3.61), c6 (+3.97), Rhe8 (+4.63).

### 35...Rxh2 (inaccuracy, positional, wp loss 5%)

You played 35...Rxh2. Stockfish preferred Rd4, after which the main line runs 35...Rd4 36. Bd5 Rxf4 37. Rd2 Rg8 38. Kh2. Why it went wrong: left rook on h2 insufficiently defended; motif: creates threat on e6, f4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Rd4 (+4.88), Rd3 (+5.36), Rhd8 (+5.43).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.31 | +0.19 | d4 | 12 | 1% | excellent |
| 2 | 1...e5* | +0.19 | +0.20 | e5 | 1 | 0% | best |
| 3 | 2.d4 | +0.20 | -0.16 | Nf3 | 36 | 3% | good |
| 4 | 2...exd4* | -0.16 | -0.05 | exd4 | 11 | 1% | best |
| 5 | 3.Qxd4 | -0.05 | -0.16 | Nf3 | 11 | 1% | excellent |
| 6 | 3...Nc6* | -0.16 | -0.10 | Nc6 | 6 | 1% | best |
| 7 | 4.Qd5 | -0.10 | -1.03 | Qe3 | 93 | 8% | inaccuracy |
| 8 | 4...Nf6* | -1.03 | -1.05 | Nf6 | 0 | 0% | best |
| 9 | 5.Qd3 | -1.05 | -1.28 | Qc4 | 23 | 2% | good |
| 10 | 5...Qe7* | -1.28 | -0.57 | Bb4+ | 71 | 6% | inaccuracy |
| 11 | 6.f3 | -0.57 | -2.28 | Nc3 | 171 | 15% | mistake |
| 12 | 6...d5* | -2.28 | -2.31 | d5 | 0 | 0% | best |
| 13 | 7.Nc3 | -2.31 | -2.34 | Nc3 | 3 | 0% | best |
| 14 | 7...dxe4* | -2.34 | -1.71 | Be6 | 63 | 5% | inaccuracy |
| 15 | 8.Nxe4 | -1.71 | -3.30 | fxe4 | 159 | 12% | mistake |
| 16 | 8...Nxe4* | -3.30 | -1.77 | Nb4 | 153 | 11% | mistake |
| 17 | 9.fxe4 | -1.77 | -3.28 | Qxe4 | 151 | 11% | mistake |
| 18 | 9...Bg4* | -3.28 | -2.27 | Nb4 | 101 | 7% | inaccuracy |
| 19 | 10.Nf3 | -2.27 | -3.46 | Bd2 | 119 | 8% | inaccuracy |
| 20 | 10...Ne5* | -3.46 | -0.12 | Rd8 | 334 | 27% | blunder |
| 21 | 11.Nxe5 | -0.12 | -0.14 | Nxe5 | 2 | 0% | best |
| 22 | 11...Qxe5* | -0.14 | -0.11 | Qxe5 | 3 | 0% | best |
| 23 | 12.h4 | -0.11 | -3.64 | Qb5+ | 353 | 28% | blunder |
| 24 | 12...Bc5* | -3.64 | -3.85 | Bc5 | 0 | 0% | best |
| 25 | 13.g3 | -3.85 | -6.10 | Bf4 | 225 | 10% | inaccuracy |
| 26 | 13...f5* | -6.10 | -2.74 | Rd8 | 336 | 17% | mistake |
| 27 | 14.Bg2 | -2.74 | -7.97 | Bf4 | 523 | 22% | blunder |
| 28 | 14...O-O* | -7.97 | -3.21 | Rd8 | 476 | 18% | mistake |
| 29 | 15.c3 | -3.21 | -11.53 | Bf4 | 832 | 21% | blunder |
| 30 | 15...Rad8* | -11.53 | -4.31 | fxe4 | 722 | 15% | mistake |
| 31 | 16.Qc4+ | -4.31 | -4.33 | Qc4+ | 2 | 0% | best |
| 32 | 16...Kh8* | -4.33 | -4.42 | Kh8 | 0 | 0% | best |
| 33 | 17.Bf4 | -4.42 | -4.27 | Bf4 | 0 | 0% | best |
| 34 | 17...Qe7* | -4.27 | -4.52 | Qe7 | 0 | 0% | best |
| 35 | 18.e5 | -4.52 | -4.44 | e5 | 0 | 0% | best |
| 36 | 18...h6* | -4.44 | -1.56 | Rfe8 | 288 | 20% | mistake |
| 37 | 19.Bxb7 | -1.56 | -1.54 | Bxb7 | 0 | 0% | best |
| 38 | 19...g5* | -1.54 | +2.80 | c6 | 434 | 38% | blunder |
| 39 | 20.hxg5 | +2.80 | +2.76 | hxg5 | 4 | 0% | best |
| 40 | 20...h5* | +2.76 | +3.15 | h5 | 39 | 3% | best |
| 41 | 21.e6 | +3.15 | +0.00 | b4 | 315 | 26% | blunder |
| 42 | 21...Bd6* | +0.00 | +2.68 | Rd6 | 268 | 23% | blunder |
| 43 | 22.Bd5 | +2.68 | +0.26 | O-O | 242 | 20% | blunder |
| 44 | 22...Bxf4* | +0.26 | +0.13 | Bxf4 | 0 | 0% | best |
| 45 | 23.gxf4 | +0.13 | +0.17 | gxf4 | 0 | 0% | best |
| 46 | 23...Kg7* | +0.17 | +3.65 | c6 | 348 | 28% | blunder |
| 47 | 24.Qd4+ | +3.65 | +2.75 | O-O | 90 | 6% | inaccuracy |
| 48 | 24...Kg6* | +2.75 | +3.03 | Kh7 | 28 | 2% | excellent |
| 49 | 25.Qe5 | +3.03 | +3.08 | Qe5 | 0 | 0% | best |
| 50 | 25...Rh8* | +3.08 | +4.28 | Qd6 | 120 | 7% | inaccuracy |
| 51 | 26.Kf2 | +4.28 | +3.48 | c4 | 80 | 5% | good |
| 52 | 26...h4* | +3.48 | +4.46 | c6 | 98 | 6% | inaccuracy |
| 53 | 27.Rh2 | +4.46 | +4.63 | Rae1 | 0 | 0% | excellent |
| 54 | 27...h3* | +4.63 | +4.96 | a5 | 33 | 2% | excellent |
| 55 | 28.Kg3 | +4.96 | +4.73 | Re1 | 23 | 1% | excellent |
| 56 | 28...Qg7* | +4.73 | +4.96 | c6 | 23 | 1% | excellent |
| 57 | 29.Qxg7+ | +4.96 | +4.78 | Re1 | 18 | 1% | excellent |
| 58 | 29...Kxg7* | +4.78 | +4.52 | Kxg7 | 0 | 0% | best |
| 59 | 30.c4 | +4.52 | +3.61 | Bc4 | 91 | 5% | inaccuracy |
| 60 | 30...Kf8* | +3.61 | +4.89 | Rd6 | 128 | 7% | inaccuracy |
| 61 | 31.Re1 | +4.89 | +5.16 | Re1 | 0 | 0% | best |
| 62 | 31...Ke7* | +5.16 | +5.29 | Ke7 | 13 | 1% | best |
| 63 | 32.b4 | +5.29 | +4.33 | Re3 | 96 | 4% | good |
| 64 | 32...c6* | +4.33 | +4.60 | c6 | 27 | 1% | best |
| 65 | 33.Bxc6 | +4.60 | +4.71 | Bxc6 | 0 | 0% | best |
| 66 | 33...Rd3+* | +4.71 | +4.64 | Rd3+ | 0 | 0% | best |
| 67 | 34.Kf2 | +4.64 | +4.36 | Kf2 | 28 | 1% | best |
| 68 | 34...Rd2+* | +4.36 | +4.87 | Rd2+ | 51 | 2% | best |
| 69 | 35.Kg1 | +4.87 | +4.88 | Kg1 | 0 | 0% | best |
| 70 | 35...Rxh2* | +4.88 | +6.36 | Rd4 | 148 | 5% | inaccuracy |
| 71 | 36.Kxh2 | +6.36 | +6.93 | Kxh2 | 0 | 0% | best |
| 72 | 36...Rc8* | +6.93 | +7.64 | Bh5 | 71 | 2% | excellent |
| 73 | 37.b5 | +7.64 | +8.10 | b5 | 0 | 0% | best |
| 74 | 37...a6* | +8.10 | +8.25 | Rc7 | 15 | 0% | excellent |
| 75 | 38.a4 | +8.25 | +8.71 | g6 | 0 | 0% | excellent |
| 76 | 38...a5* | +8.71 | +8.96 | Bh5 | 25 | 0% | excellent |
| 77 | 39.Re5 | +8.96 | +9.78 | Bd5 | 0 | 0% | excellent |
| 78 | 39...Kd6* | +9.78 | M14 | Rb8 |  | 0% | excellent |
| 79 | 40.g6 | M14 | +30.71 | e7 |  | 0% | mistake |
| 80 | 40...Bh5* | +30.71 | M18 | Ke7 |  | 0% | excellent |
| 81 | 41.e7 | M18 | M15 | e7 |  | 0% | best |
| 82 | 41...Bxg6* | M15 | M14 | Bxg6 |  | 0% | best |
| 83 | 42.Kxh3 | M14 | +34.35 | e8=N+ |  | 0% | mistake |
| 84 | 42...Be8* | +34.35 | M40 | Rh8+ |  | 0% | excellent |
| 85 | 43.Bxe8 | M40 | M22 | c5+ |  | 0% | excellent |
| 86 | 43...Rxe8* | M22 | M17 | Rxe8 |  | 0% | best |
| 87 | 44.Rd5+ | M17 | M26 | c5+ |  | 0% | excellent |
| 88 | 44...Kxe7* | M26 | M26 | Ke6 |  | 0% | excellent |
| 89 | 45.Re5+ | M26 | +37.24 | Re5+ |  | 0% | best |
| 90 | 45...Kd7* | +37.24 | M25 | Kd8 |  | 0% | excellent |
| 91 | 46.Rxe8 | M25 | M19 | Rxe8 |  | 0% | best |
| 92 | 46...Kxe8* | M19 | M18 | Kxe8 |  | 0% | best |
| 93 | 47.b6 | M18 | M22 | Kh4 |  | 0% | excellent |
| 94 | 47...Kd8* | M22 | M19 | Kd8 |  | 0% | best |
| 95 | 48.c5 | M19 | M17 | Kg3 |  | 0% | excellent |
| 96 | 48...Kc8* | M17 | M12 | Kd7 |  | 0% | excellent |
| 97 | 49.c6 | M12 | M11 | c6 |  | 0% | best |
| 98 | 49...Kb8* | M11 | M10 | Kd8 |  | 0% | excellent |
| 99 | 50.c7+ | M10 | M11 | Kh4 |  | 0% | excellent |
| 100 | 50...Kb7* | M11 | M10 | Kc8 |  | 0% | excellent |
| 101 | 51.Kh4 | M10 | M9 | Kh4 |  | 0% | best |
| 102 | 51...Kc8* | M9 | M9 | Kxb6 |  | 0% | excellent |
| 103 | 52.Kg5 | M9 | M8 | Kg5 |  | 0% | best |
| 104 | 52...Kb7* | M8 | M8 | Kb7 |  | 0% | best |
| 105 | 53.Kxf5 | M8 | M7 | Kxf5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 13 positional.
- Opening: 5 error(s) (avg wp loss 11%).
- Middlegame: 10 error(s) (avg wp loss 18%).
- Endgame: 1 error(s) (avg wp loss 5%).
