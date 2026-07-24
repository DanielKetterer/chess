# (free, so lmk) Game analysis: DanielKetterer vs jorgefortunati50

Date: 2026.07.23  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171987878016

## Summary

- Lichess accuracy: you 60.9%, opponent 60.3%
- Opening: C54 Italian Game: Classical Variation, Giuoco Pianissimo, with h6 (theory followed through ply 12)
- First deviation from theory: ply 13, You played 7. Be3
- Your moves: 15 best, 6 excellent, 2 good, 4 inaccuracy, 2 mistake, 4 blunder

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

You played 30.Qf1. Stockfish preferred Bh3+, after which the main line runs 30. Bh3+ Kb8 31. Nd4 Rxb2+ 32. Ka3 Rb6. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bh3+ (+2.07), Rb1 (+0.00), Qh3+ (+0.00).

## Critical positions

- Ply 15 (you), 8.fxe3: -0.01 -> -0.04 [only-move situation]
- Ply 22 (opponent), 11...Bg6: +0.19 -> +0.35 [only-move situation]
- Ply 37 (you), 19.Re3: -1.06 -> -4.75 [evaluation crossed equal -> losing]
- Ply 44 (opponent), 22...Nxe5: -3.20 -> +0.14 [only-move situation; evaluation crossed winning -> equal]
- Ply 45 (you), 23.Qh1: +0.14 -> -6.83 [only-move situation; evaluation crossed equal -> losing]
- Ply 48 (opponent), 24...Nd3+: -6.54 -> -0.86 [evaluation crossed winning -> equal]
- Ply 49 (you), 25.Ke2: -0.86 -> -0.66 [only-move situation]
- Ply 51 (you), 26.Rxe8: +0.00 -> +0.00 [only-move situation]

## Your errors, move by move

### 6.d3 (mistake, positional, wp loss 12%)

You played 6.d3. Stockfish preferred d4, after which the main line runs 6. d4 Bb6 7. Nxe5 Nxe5 8. dxe5 Nxe4. Why it went wrong: motif: fork; creates threat on c5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d4 (+1.58), b4 (+0.35), Re1 (+0.23).

### 12.d4 (inaccuracy, positional, wp loss 7%)

You played 12.d4. Stockfish preferred Nh4, after which the main line runs 12. Nh4 Qd7 13. Nxg6 fxg6 14. b4 h5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nh4 (+0.35), Rf2 (-0.06), a4 (-0.14).

### 15.e5 (inaccuracy, positional, wp loss 7%)

You played 15.e5. Stockfish preferred Nh4, after which the main line runs 15. Nh4 h5 16. Nxg6 fxg6 17. g5 Nh7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nh4 (-0.03), b4 (-0.33), d5 (-0.49).

### 17.hxg4 (mistake, tactical, wp loss 13%)

You played 17.hxg4. Stockfish preferred e6, after which the main line runs 17. e6 Qd6 18. hxg4 Qg3+ 19. Kh1 h5. Why it went wrong: left pawn on g4 insufficiently defended; motif: fork; creates threat on d7, g4. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: e6 (+0.65), hxg4 (-0.85), Bxa6 (-2.21).

### 18.Kf2 (inaccuracy, positional, wp loss 7%)

You played 18.Kf2. Stockfish preferred Kh1, after which the main line runs 18. Kh1 Bh5 19. Qc2 Rhe8 20. Bf1 Nxe5. Why it went wrong: your king's zone came under heavier attack after this move. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kh1 (-0.71), Kf2 (-1.34), Kf1 (-1.73).

### 19.Re3 (blunder, positional, wp loss 26%)

You played 19.Re3. Stockfish preferred Qc2, after which the main line runs 19. Qc2 Bg6 20. Qa4 Rxd2+ 21. Nxd2 Qh4+. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qc2 (-1.06), Rh1 (-2.60), Bf1 (-3.42).

### 20.Be2 (inaccuracy, positional, wp loss 7%)

You played 20.Be2. Stockfish preferred Bxf7, after which the main line runs 20. Bxf7 Bxf7 21. Qe2 Be6 22. Kg1 Kb8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 16; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Bxf7 (-4.00), e6 (-4.61), Bf1 (-4.76).

### 23.Qh1 (blunder, tactical, wp loss 44%)

You played 23.Qh1. Stockfish preferred Qe2, after which the main line runs 23. Qe2 Qf4+ 24. Kg1 Ng4 25. Bh3 f5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on d2 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qe2 (+0.14), Re2 (-2.85), Re4 (-3.33).

### 29.Kb3 (blunder, positional, wp loss 20%)

You played 29.Kb3. Stockfish preferred Nd2, after which the main line runs 29. Nd2 Qb6 30. Bf1 Rd8 31. Bd3 Kb8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nd2 (+5.56), Kb3 (+1.70), Kb1 (-0.18).

### 30.Qf1 (blunder, tactical, wp loss 66%)

You played 30.Qf1. Stockfish preferred Bh3+, after which the main line runs 30. Bh3+ Kb8 31. Nd4 Rxb2+ 32. Ka3 Rb6. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bh3+ (+2.07), Rb1 (+0.00), Qh3+ (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.32 | +0.25 | d4 | 7 | 1% | excellent |
| 2 | 1...e5 | +0.25 | +0.24 | e5 | 0 | 0% | best |
| 3 | 2.Nf3* | +0.24 | +0.25 | Nf3 | 0 | 0% | best |
| 4 | 2...Nc6 | +0.25 | +0.21 | Nc6 | 0 | 0% | best |
| 5 | 3.Bc4* | +0.21 | +0.14 | Bb5 | 7 | 1% | excellent |
| 6 | 3...h6 | +0.14 | +0.62 | Nf6 | 48 | 4% | good |
| 7 | 4.O-O* | +0.62 | +0.42 | d4 | 20 | 2% | excellent |
| 8 | 4...Bc5 | +0.42 | +0.86 | Nf6 | 44 | 4% | good |
| 9 | 5.c3* | +0.86 | +0.82 | c3 | 4 | 0% | best |
| 10 | 5...Nf6 | +0.82 | +1.58 | Bb6 | 76 | 7% | inaccuracy |
| 11 | 6.d3* | +1.58 | +0.25 | d4 | 133 | 12% | mistake |
| 12 | 6...d6 | +0.25 | +0.20 | Bb6 | 0 | 0% | excellent |
| 13 | 7.Be3* | +0.20 | +0.00 | b4 | 20 | 2% | excellent |
| 14 | 7...Bxe3 | +0.00 | -0.01 | Bxe3 | 0 | 0% | best |
| 15 | 8.fxe3* | -0.01 | -0.04 | fxe3 | 3 | 0% | best |
| 16 | 8...Bg4 | -0.04 | +0.36 | O-O | 40 | 4% | good |
| 17 | 9.Nbd2* | +0.36 | +0.25 | a4 | 11 | 1% | excellent |
| 18 | 9...a6 | +0.25 | +0.57 | Na5 | 32 | 3% | good |
| 19 | 10.h3* | +0.57 | +0.51 | h3 | 6 | 1% | best |
| 20 | 10...Bh5 | +0.51 | +0.73 | Bd7 | 22 | 2% | excellent |
| 21 | 11.g4* | +0.73 | +0.19 | a4 | 54 | 5% | good |
| 22 | 11...Bg6 | +0.19 | +0.35 | Bg6 | 16 | 1% | best |
| 23 | 12.d4* | +0.35 | -0.44 | Nh4 | 79 | 7% | inaccuracy |
| 24 | 12...exd4 | -0.44 | +0.18 | h5 | 62 | 6% | inaccuracy |
| 25 | 13.exd4* | +0.18 | +0.18 | exd4 | 0 | 0% | best |
| 26 | 13...Qd7 | +0.18 | +0.50 | O-O | 32 | 3% | good |
| 27 | 14.Re1* | +0.50 | -0.03 | Bb3 | 53 | 5% | good |
| 28 | 14...O-O-O | -0.03 | -0.03 | O-O-O | 0 | 0% | best |
| 29 | 15.e5* | -0.03 | -0.84 | Nh4 | 81 | 7% | inaccuracy |
| 30 | 15...dxe5 | -0.84 | -0.67 | dxe5 | 17 | 2% | best |
| 31 | 16.dxe5* | -0.67 | -0.97 | dxe5 | 30 | 3% | best |
| 32 | 16...Nxg4 | -0.97 | +0.65 | Ne4 | 162 | 15% | mistake |
| 33 | 17.hxg4* | +0.65 | -0.75 | e6 | 140 | 13% | mistake |
| 34 | 17...Qxg4+ | -0.75 | -0.71 | Qxg4+ | 4 | 0% | best |
| 35 | 18.Kf2* | -0.71 | -1.46 | Kh1 | 75 | 7% | inaccuracy |
| 36 | 18...Bh5 | -1.46 | -1.06 | Qf4 | 40 | 3% | good |
| 37 | 19.Re3* | -1.06 | -4.75 | Qc2 | 369 | 26% | blunder |
| 38 | 19...Qf4 | -4.75 | -4.00 | Nxe5 | 75 | 4% | good |
| 39 | 20.Be2* | -4.00 | -5.56 | Bxf7 | 156 | 7% | inaccuracy |
| 40 | 20...Bxf3 | -5.56 | -5.64 | Bxf3 | 0 | 0% | best |
| 41 | 21.Bxf3* | -5.64 | -5.35 | Bxf3 | 0 | 0% | best |
| 42 | 21...Qh2+ | -5.35 | -2.99 | Nxe5 | 236 | 13% | mistake |
| 43 | 22.Bg2* | -2.99 | -3.20 | Bg2 | 21 | 1% | best |
| 44 | 22...Nxe5 | -3.20 | +0.14 | Qf4+ | 334 | 28% | blunder |
| 45 | 23.Qh1* | +0.14 | -6.83 | Qe2 | 697 | 44% | blunder |
| 46 | 23...Qf4+ | -6.83 | -6.10 | Rxd2+ | 73 | 2% | good |
| 47 | 24.Nf3* | -6.10 | -6.54 | Ke2 | 44 | 1% | excellent |
| 48 | 24...Nd3+ | -6.54 | -0.86 | Ng4+ | 568 | 34% | blunder |
| 49 | 25.Ke2* | -0.86 | -0.66 | Ke2 | 0 | 0% | best |
| 50 | 25...Rhe8 | -0.66 | +0.00 | Qc4 | 66 | 6% | inaccuracy |
| 51 | 26.Rxe8* | +0.00 | +0.00 | Rxe8 | 0 | 0% | best |
| 52 | 26...Rxe8+ | +0.00 | +0.00 | Rxe8+ | 0 | 0% | best |
| 53 | 27.Kxd3* | +0.00 | +0.00 | Kxd3 | 0 | 0% | best |
| 54 | 27...Qe3+ | +0.00 | +3.10 | Qe4+ | 310 | 26% | blunder |
| 55 | 28.Kc2* | +3.10 | +3.38 | Kc2 | 0 | 0% | best |
| 56 | 28...Qf2+ | +3.38 | +5.56 | Qe4+ | 218 | 11% | mistake |
| 57 | 29.Kb3* | +5.56 | +2.07 | Nd2 | 349 | 20% | blunder |
| 58 | 29...Re2 | +2.07 | +2.07 | Re2 | 0 | 0% | best |
| 59 | 30.Qf1* | +2.07 | -M6 | Bh3+ |  | 66% | blunder |
| 60 | 30...Rxb2+ | -M6 | -0.64 | Qb6+ |  | 42% | blunder |
| 61 | 31.Kc4* | -0.64 | -0.72 | Kc4 | 8 | 1% | best |
| 62 | 31...b5+ | -0.72 | -0.56 | Qxg2 | 16 | 1% | excellent |
| 63 | 32.Kd5* | -0.56 | -0.56 | Kd5 | 0 | 0% | best |
| 64 | 32...Qc5+ | -0.56 | +43.21 | Qxg2 | 4377 | 53% | blunder |
| 65 | 33.Kxc5* | +43.21 | M18 | Kxc5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 7 positional.
- Opening: 1 error(s) (avg wp loss 12%).
- Middlegame: 9 error(s) (avg wp loss 22%).
