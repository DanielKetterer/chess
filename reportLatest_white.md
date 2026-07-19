# (free, so lmk) Game analysis: alesandro777888 vs DanielKetterer

Date: 2026.07.19  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171795040624

## Summary

- Lichess accuracy: you 77.8%, opponent 73.5%
- Opening: C22 Center Game: Normal Variation (theory followed through ply 6)
- First deviation from theory: ply 7, You played 4. Qd5
- Your moves: 22 best, 12 excellent, 4 good, 5 inaccuracy, 5 mistake, 5 blunder

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

You played 12.h4. Stockfish preferred Qb5+, after which the main line runs 12. Qb5+ Qxb5 13. Bxb5+ c6 14. Be2 Be6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check; motif: fork; creates threat on b7, e5. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qb5+ (-0.11), h3 (-1.40), Be3 (-1.46).

## Critical positions

- Ply 20 (opponent), 10...Ne5: -3.46 -> -0.12 [evaluation crossed winning -> equal]
- Ply 22 (opponent), 11...Qxe5: -0.14 -> -0.11 [only-move situation]
- Ply 23 (you), 12.h4: -0.11 -> -3.64 [evaluation crossed equal -> losing]
- Ply 27 (you), 14.Bg2: -2.74 -> -7.97
- Ply 29 (you), 15.c3: -3.21 -> -11.53
- Ply 32 (opponent), 16...Kh8: -4.33 -> -4.42 [only-move situation]
- Ply 34 (opponent), 17...Qe7: -4.27 -> -4.52 [only-move situation]
- Ply 38 (opponent), 19...g5: -1.54 -> +2.80 [evaluation crossed equal -> losing]

## Your errors, move by move

### 4.Qd5 (inaccuracy, positional, wp loss 8%)

You played 4.Qd5. Stockfish preferred Qe3, after which the main line runs 4. Qe3 Nf6 5. Bd2 Be7 6. Nc3 d5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qe3 (-0.10), Qd3 (-0.15), Qc4 (-0.27).

### 6.f3 (mistake, positional, wp loss 15%)

You played 6.f3. Stockfish preferred Nc3, after which the main line runs 6. Nc3 d5 7. Bg5 Nb4 8. Qe2 d4. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc3 (-0.57), a3 (-1.73), Qe3 (-1.83).

### 8.Nxe4 (mistake, tactical, wp loss 12%)

You played 8.Nxe4. Stockfish preferred fxe4, after which the main line runs 8. fxe4 Bf5 9. Bg5 Bxe4 10. Nxe4 Qxe4+. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: fxe4 (-1.71), Nxe4 (-3.03), Qe3 (-4.26).

### 9.fxe4 (mistake, tactical, wp loss 11%)

You played 9.fxe4. Stockfish preferred Qxe4, after which the main line runs 9. Qxe4 Nb4 10. Bd3 Be6 11. Ne2 O-O-O. Why it went wrong: a favorable capture was available (fxe4). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxe4 (-1.77), fxe4 (-3.16), Be3 (-5.67).

### 10.Nf3 (inaccuracy, positional, wp loss 8%)

You played 10.Nf3. Stockfish preferred Bd2, after which the main line runs 10. Bd2 Rd8 11. Qe3 Qh4+ 12. g3 Qh5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Bd2 (-2.27), Be3 (-3.08), Nf3 (-3.18).

### 12.h4 (blunder, tactical, wp loss 28%)

You played 12.h4. Stockfish preferred Qb5+, after which the main line runs 12. Qb5+ Qxb5 13. Bxb5+ c6 14. Be2 Be6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check; motif: fork; creates threat on b7, e5. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qb5+ (-0.11), h3 (-1.40), Be3 (-1.46).

### 13.g3 (inaccuracy, positional, wp loss 10%)

You played 13.g3. Stockfish preferred Bf4, after which the main line runs 13. Bf4 Bb4+ 14. Bd2 Qxb2 15. Bxb4 Qxa1+. Why it went wrong: motif: creates threat on e5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 12; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Bf4 (-3.85), Bg5 (-4.57), Be3 (-4.85).

### 14.Bg2 (blunder, positional, wp loss 22%)

You played 14.Bg2. Stockfish preferred Bf4, after which the main line runs 14. Bf4 Qxb2 15. Rc1 Bd4 16. Rh2 Bc3+. Why it went wrong: motif: creates threat on e5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Bf4 (-2.74), c3 (-4.19), Rh2 (-4.53).

### 15.c3 (blunder, positional, wp loss 21%)

You played 15.c3. Stockfish preferred Bf4, after which the main line runs 15. Bf4 Qxb2 16. Qb3+ Qxb3 17. axb3 fxe4. Why it went wrong: motif: creates threat on e5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Bf4 (-3.21), Qc4+ (-3.67), Rf1 (-5.07).

### 21.e6 (blunder, positional, wp loss 26%)

You played 21.e6. Stockfish preferred b4, after which the main line runs 21. b4 Bb6 22. Bc6 Rg8 23. Kf1 Rxg5. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: motif: creates threat on c5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: b4 (+3.15), Rh2 (+2.67), Bc6 (+2.48).

### 22.Bd5 (blunder, positional, wp loss 20%)

You played 22.Bd5. Stockfish preferred O-O, after which the main line runs 22. O-O Kh7 23. Bc6 Rh8 24. Rae1 Kg6. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: O-O (+2.68), Bc6 (+1.35), b4 (+1.00).

### 24.Qd4+ (inaccuracy, positional, wp loss 6%)

You played 24.Qd4+. Stockfish preferred O-O, after which the main line runs 24. O-O Rd6 25. Qc5 c6 26. Bc4 Kg6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 2; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: O-O (+3.65), Kf2 (+3.15), Qd4+ (+2.44).

### 30.c4 (inaccuracy, positional, wp loss 5%)

You played 30.c4. Stockfish preferred Bc4, after which the main line runs 30. Bc4 Kf8 31. Re1 Ke7 32. Bf1 Rh7. Why it went wrong: motif: creates threat on g4, h3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Bc4 (+4.52), c4 (+3.78), Bc6 (+0.20).

### 40.g6 (mistake, positional, wp loss 0%)

You played 40.g6. Stockfish preferred e7, after which the main line runs 40. e7 Bh5 41. c5+ Kc7 42. e8=R Bxe8. There was a forced mate on the board and this move let it slip. Why it went wrong: left pawn on e6, bishop on c6 insufficiently defended; motif: creates threat on h3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e7 (M14), c5+ (+32.71), Bd5 (+14.01).

### 42.Kxh3 (mistake, positional, wp loss 0%)

You played 42.Kxh3. Stockfish preferred e8=N+, after which the main line runs 42. e8=N+ Bxe8 43. c5+ Kc7 44. Rxe8 Rxe8. There was a forced mate on the board and this move let it slip. Why it went wrong: left pawn on e7, bishop on c6 insufficiently defended; the best move was a forcing check; motif: creates threat on h3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 31; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: e8=N+ (M14), e8=Q (M14), c5+ (M14).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.31 | +0.19 | d4 | 12 | 1% | excellent |
| 2 | 1...e5 | +0.19 | +0.20 | e5 | 1 | 0% | best |
| 3 | 2.d4* | +0.20 | -0.16 | Nf3 | 36 | 3% | good |
| 4 | 2...exd4 | -0.16 | -0.05 | exd4 | 11 | 1% | best |
| 5 | 3.Qxd4* | -0.05 | -0.16 | Nf3 | 11 | 1% | excellent |
| 6 | 3...Nc6 | -0.16 | -0.10 | Nc6 | 6 | 1% | best |
| 7 | 4.Qd5* | -0.10 | -1.03 | Qe3 | 93 | 8% | inaccuracy |
| 8 | 4...Nf6 | -1.03 | -1.05 | Nf6 | 0 | 0% | best |
| 9 | 5.Qd3* | -1.05 | -1.28 | Qc4 | 23 | 2% | good |
| 10 | 5...Qe7 | -1.28 | -0.57 | Bb4+ | 71 | 6% | inaccuracy |
| 11 | 6.f3* | -0.57 | -2.28 | Nc3 | 171 | 15% | mistake |
| 12 | 6...d5 | -2.28 | -2.31 | d5 | 0 | 0% | best |
| 13 | 7.Nc3* | -2.31 | -2.34 | Nc3 | 3 | 0% | best |
| 14 | 7...dxe4 | -2.34 | -1.71 | Be6 | 63 | 5% | inaccuracy |
| 15 | 8.Nxe4* | -1.71 | -3.30 | fxe4 | 159 | 12% | mistake |
| 16 | 8...Nxe4 | -3.30 | -1.77 | Nb4 | 153 | 11% | mistake |
| 17 | 9.fxe4* | -1.77 | -3.28 | Qxe4 | 151 | 11% | mistake |
| 18 | 9...Bg4 | -3.28 | -2.27 | Nb4 | 101 | 7% | inaccuracy |
| 19 | 10.Nf3* | -2.27 | -3.46 | Bd2 | 119 | 8% | inaccuracy |
| 20 | 10...Ne5 | -3.46 | -0.12 | Rd8 | 334 | 27% | blunder |
| 21 | 11.Nxe5* | -0.12 | -0.14 | Nxe5 | 2 | 0% | best |
| 22 | 11...Qxe5 | -0.14 | -0.11 | Qxe5 | 3 | 0% | best |
| 23 | 12.h4* | -0.11 | -3.64 | Qb5+ | 353 | 28% | blunder |
| 24 | 12...Bc5 | -3.64 | -3.85 | Bc5 | 0 | 0% | best |
| 25 | 13.g3* | -3.85 | -6.10 | Bf4 | 225 | 10% | inaccuracy |
| 26 | 13...f5 | -6.10 | -2.74 | Rd8 | 336 | 17% | mistake |
| 27 | 14.Bg2* | -2.74 | -7.97 | Bf4 | 523 | 22% | blunder |
| 28 | 14...O-O | -7.97 | -3.21 | Rd8 | 476 | 18% | mistake |
| 29 | 15.c3* | -3.21 | -11.53 | Bf4 | 832 | 21% | blunder |
| 30 | 15...Rad8 | -11.53 | -4.31 | fxe4 | 722 | 15% | mistake |
| 31 | 16.Qc4+* | -4.31 | -4.33 | Qc4+ | 2 | 0% | best |
| 32 | 16...Kh8 | -4.33 | -4.42 | Kh8 | 0 | 0% | best |
| 33 | 17.Bf4* | -4.42 | -4.27 | Bf4 | 0 | 0% | best |
| 34 | 17...Qe7 | -4.27 | -4.52 | Qe7 | 0 | 0% | best |
| 35 | 18.e5* | -4.52 | -4.44 | e5 | 0 | 0% | best |
| 36 | 18...h6 | -4.44 | -1.56 | Rfe8 | 288 | 20% | mistake |
| 37 | 19.Bxb7* | -1.56 | -1.54 | Bxb7 | 0 | 0% | best |
| 38 | 19...g5 | -1.54 | +2.80 | c6 | 434 | 38% | blunder |
| 39 | 20.hxg5* | +2.80 | +2.76 | hxg5 | 4 | 0% | best |
| 40 | 20...h5 | +2.76 | +3.15 | h5 | 39 | 3% | best |
| 41 | 21.e6* | +3.15 | +0.00 | b4 | 315 | 26% | blunder |
| 42 | 21...Bd6 | +0.00 | +2.68 | Rd6 | 268 | 23% | blunder |
| 43 | 22.Bd5* | +2.68 | +0.26 | O-O | 242 | 20% | blunder |
| 44 | 22...Bxf4 | +0.26 | +0.13 | Bxf4 | 0 | 0% | best |
| 45 | 23.gxf4* | +0.13 | +0.17 | gxf4 | 0 | 0% | best |
| 46 | 23...Kg7 | +0.17 | +3.65 | c6 | 348 | 28% | blunder |
| 47 | 24.Qd4+* | +3.65 | +2.75 | O-O | 90 | 6% | inaccuracy |
| 48 | 24...Kg6 | +2.75 | +3.03 | Kh7 | 28 | 2% | excellent |
| 49 | 25.Qe5* | +3.03 | +3.08 | Qe5 | 0 | 0% | best |
| 50 | 25...Rh8 | +3.08 | +4.28 | Qd6 | 120 | 7% | inaccuracy |
| 51 | 26.Kf2* | +4.28 | +3.48 | c4 | 80 | 5% | good |
| 52 | 26...h4 | +3.48 | +4.46 | c6 | 98 | 6% | inaccuracy |
| 53 | 27.Rh2* | +4.46 | +4.63 | Rae1 | 0 | 0% | excellent |
| 54 | 27...h3 | +4.63 | +4.96 | a5 | 33 | 2% | excellent |
| 55 | 28.Kg3* | +4.96 | +4.73 | Re1 | 23 | 1% | excellent |
| 56 | 28...Qg7 | +4.73 | +4.96 | c6 | 23 | 1% | excellent |
| 57 | 29.Qxg7+* | +4.96 | +4.78 | Re1 | 18 | 1% | excellent |
| 58 | 29...Kxg7 | +4.78 | +4.52 | Kxg7 | 0 | 0% | best |
| 59 | 30.c4* | +4.52 | +3.61 | Bc4 | 91 | 5% | inaccuracy |
| 60 | 30...Kf8 | +3.61 | +4.89 | Rd6 | 128 | 7% | inaccuracy |
| 61 | 31.Re1* | +4.89 | +5.16 | Re1 | 0 | 0% | best |
| 62 | 31...Ke7 | +5.16 | +5.29 | Ke7 | 13 | 1% | best |
| 63 | 32.b4* | +5.29 | +4.33 | Re3 | 96 | 4% | good |
| 64 | 32...c6 | +4.33 | +4.60 | c6 | 27 | 1% | best |
| 65 | 33.Bxc6* | +4.60 | +4.71 | Bxc6 | 0 | 0% | best |
| 66 | 33...Rd3+ | +4.71 | +4.64 | Rd3+ | 0 | 0% | best |
| 67 | 34.Kf2* | +4.64 | +4.36 | Kf2 | 28 | 1% | best |
| 68 | 34...Rd2+ | +4.36 | +4.87 | Rd2+ | 51 | 2% | best |
| 69 | 35.Kg1* | +4.87 | +4.88 | Kg1 | 0 | 0% | best |
| 70 | 35...Rxh2 | +4.88 | +6.36 | Rd4 | 148 | 5% | inaccuracy |
| 71 | 36.Kxh2* | +6.36 | +6.93 | Kxh2 | 0 | 0% | best |
| 72 | 36...Rc8 | +6.93 | +7.64 | Bh5 | 71 | 2% | excellent |
| 73 | 37.b5* | +7.64 | +8.10 | b5 | 0 | 0% | best |
| 74 | 37...a6 | +8.10 | +8.25 | Rc7 | 15 | 0% | excellent |
| 75 | 38.a4* | +8.25 | +8.71 | g6 | 0 | 0% | excellent |
| 76 | 38...a5 | +8.71 | +8.96 | Bh5 | 25 | 0% | excellent |
| 77 | 39.Re5* | +8.96 | +9.78 | Bd5 | 0 | 0% | excellent |
| 78 | 39...Kd6 | +9.78 | M14 | Rb8 |  | 0% | excellent |
| 79 | 40.g6* | M14 | +30.71 | e7 |  | 0% | mistake |
| 80 | 40...Bh5 | +30.71 | M18 | Ke7 |  | 0% | excellent |
| 81 | 41.e7* | M18 | M15 | e7 |  | 0% | best |
| 82 | 41...Bxg6 | M15 | M14 | Bxg6 |  | 0% | best |
| 83 | 42.Kxh3* | M14 | +34.35 | e8=N+ |  | 0% | mistake |
| 84 | 42...Be8 | +34.35 | M40 | Rh8+ |  | 0% | excellent |
| 85 | 43.Bxe8* | M40 | M22 | c5+ |  | 0% | excellent |
| 86 | 43...Rxe8 | M22 | M17 | Rxe8 |  | 0% | best |
| 87 | 44.Rd5+* | M17 | M26 | c5+ |  | 0% | excellent |
| 88 | 44...Kxe7 | M26 | M26 | Ke6 |  | 0% | excellent |
| 89 | 45.Re5+* | M26 | +37.24 | Re5+ |  | 0% | best |
| 90 | 45...Kd7 | +37.24 | M25 | Kd8 |  | 0% | excellent |
| 91 | 46.Rxe8* | M25 | M19 | Rxe8 |  | 0% | best |
| 92 | 46...Kxe8 | M19 | M18 | Kxe8 |  | 0% | best |
| 93 | 47.b6* | M18 | M22 | Kh4 |  | 0% | excellent |
| 94 | 47...Kd8 | M22 | M19 | Kd8 |  | 0% | best |
| 95 | 48.c5* | M19 | M17 | Kg3 |  | 0% | excellent |
| 96 | 48...Kc8 | M17 | M12 | Kd7 |  | 0% | excellent |
| 97 | 49.c6* | M12 | M11 | c6 |  | 0% | best |
| 98 | 49...Kb8 | M11 | M10 | Kd8 |  | 0% | excellent |
| 99 | 50.c7+* | M10 | M11 | Kh4 |  | 0% | excellent |
| 100 | 50...Kb7 | M11 | M10 | Kc8 |  | 0% | excellent |
| 101 | 51.Kh4* | M10 | M9 | Kh4 |  | 0% | best |
| 102 | 51...Kc8 | M9 | M9 | Kxb6 |  | 0% | excellent |
| 103 | 52.Kg5* | M9 | M8 | Kg5 |  | 0% | best |
| 104 | 52...Kb7 | M8 | M8 | Kb7 |  | 0% | best |
| 105 | 53.Kxf5* | M8 | M7 | Kxf5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 12 positional.
- Opening: 5 error(s) (avg wp loss 11%).
- Middlegame: 8 error(s) (avg wp loss 17%).
- Endgame: 2 error(s) (avg wp loss 0%).
