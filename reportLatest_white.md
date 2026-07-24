# (free, so lmk) Game analysis: DanielKetterer vs jorgefortunati50

Date: 2026.07.23  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171987878016

## Summary

- Lichess accuracy: you 57.3%, opponent 60.3%
- Opening: C54 Italian Game: Classical Variation, Giuoco Pianissimo, with h6 (theory followed through ply 12)
- First deviation from theory: ply 13, You played 7. Be3
- Your moves: 13 best, 7 excellent, 3 good, 3 inaccuracy, 4 mistake, 3 blunder

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

You played 30.Qf1. Stockfish preferred Bh3+, after which the main line runs 30. Bh3+ Kb8 31. Nd4 Rxb2+ 32. Ka3 Rb6. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bh3+ (+2.85), Rb1 (+0.00), Qh3+ (+0.00).

## Critical positions

- Ply 15 (you), 8.fxe3: -0.01 -> +0.00 [only-move situation]
- Ply 22 (opponent), 11...Bg6: +0.01 -> +0.05 [only-move situation]
- Ply 32 (opponent), 16...Nxg4: -1.13 -> +1.09
- Ply 33 (you), 17.hxg4: +1.09 -> -0.57 [only-move situation]
- Ply 37 (you), 19.Re3: -0.99 -> -5.09 [evaluation crossed equal -> losing]
- Ply 44 (opponent), 22...Nxe5: -3.93 -> +0.05 [only-move situation; evaluation crossed winning -> equal]
- Ply 45 (you), 23.Qh1: +0.05 -> -7.12 [only-move situation; evaluation crossed equal -> losing]
- Ply 48 (opponent), 24...Nd3+: -6.83 -> -0.33 [evaluation crossed winning -> equal]

## Your errors, move by move

### 6.d3 (mistake, positional, wp loss 15%)

You played 6.d3. Stockfish preferred d4, after which the main line runs 6. d4 Bb6 7. Nxe5 Nxe5 8. dxe5 Nxe4. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: motif: fork; creates threat on c5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d4 (+1.95), Re1 (+0.29), b4 (+0.26).

### 11.g4 (inaccuracy, positional, wp loss 6%)

You played 11.g4. Stockfish preferred a4, after which the main line runs 11. a4 Ne7 12. Qe1 O-O 13. a5 Bg6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a4 (+0.64), a3 (+0.44), d4 (+0.39).

### 12.d4 (inaccuracy, positional, wp loss 7%)

You played 12.d4. Stockfish preferred Nh4, after which the main line runs 12. Nh4 Ne7 13. Qf3 Qd7 14. b4 O-O-O. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nh4 (+0.05), a4 (-0.01), Rf2 (-0.26).

### 15.e5 (mistake, positional, wp loss 11%)

You played 15.e5. Stockfish preferred Nh4, after which the main line runs 15. Nh4 h5 16. Nxg6 fxg6 17. g5 Nh7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nh4 (+0.06), b4 (-0.28), d5 (-0.31).

### 17.hxg4 (mistake, tactical, wp loss 15%)

You played 17.hxg4. Stockfish preferred e6, after which the main line runs 17. e6 Qd6 18. hxg4 Qg3+ 19. Kh1 Rxd2. Why it went wrong: left pawn on g4 insufficiently defended; motif: fork; creates threat on d7, g4. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: e6 (+1.09), hxg4 (-0.56), Bxa6 (-2.91).

### 18.Kf2 (inaccuracy, positional, wp loss 6%)

You played 18.Kf2. Stockfish preferred Kh1, after which the main line runs 18. Kh1 Bh5 19. Qc2 Rxd2 20. Nxd2 Qh4+. Why it went wrong: your king's zone came under heavier attack after this move. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Kh1 (-0.64), Kf2 (-1.19), Kf1 (-3.22).

### 19.Re3 (blunder, positional, wp loss 28%)

You played 19.Re3. Stockfish preferred Qc2, after which the main line runs 19. Qc2 Bg6 20. Qa4 Rxd2+ 21. Nxd2 Qh4+. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 11; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Qc2 (-0.99), Rh1 (-2.65), Re2 (-3.89).

### 23.Qh1 (blunder, tactical, wp loss 44%)

You played 23.Qh1. Stockfish preferred Qe2, after which the main line runs 23. Qe2 Qf4+ 24. Kg1 Ng4 25. Bh3 f5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on d2 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qe2 (+0.05), Re2 (-3.01), Rxe5 (-3.66).

### 29.Kb3 (mistake, positional, wp loss 16%)

You played 29.Kb3. Stockfish preferred Nd2, after which the main line runs 29. Nd2 Qb6 30. Rd1 Qb5 31. Bf1 Qd7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nd2 (+5.59), Kb3 (+2.55), Kb1 (-0.60).

### 30.Qf1 (blunder, tactical, wp loss 72%)

You played 30.Qf1. Stockfish preferred Bh3+, after which the main line runs 30. Bh3+ Kb8 31. Nd4 Rxb2+ 32. Ka3 Rb6. The evaluation crossed from winning to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bh3+ (+2.85), Rb1 (+0.00), Qh3+ (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.31 | +0.20 | e4 | 11 | 1% | best |
| 2 | 1...e5 | +0.20 | +0.21 | c6 | 1 | 0% | excellent |
| 3 | 2.Nf3* | +0.21 | +0.20 | Nf3 | 1 | 0% | best |
| 4 | 2...Nc6 | +0.20 | +0.23 | Nc6 | 3 | 0% | best |
| 5 | 3.Bc4* | +0.23 | +0.21 | Bb5 | 2 | 0% | excellent |
| 6 | 3...h6 | +0.21 | +0.64 | Bc5 | 43 | 4% | good |
| 7 | 4.O-O* | +0.64 | +0.50 | d4 | 14 | 1% | excellent |
| 8 | 4...Bc5 | +0.50 | +0.93 | d6 | 43 | 4% | good |
| 9 | 5.c3* | +0.93 | +0.86 | c3 | 7 | 1% | best |
| 10 | 5...Nf6 | +0.86 | +1.95 | d6 | 109 | 9% | inaccuracy |
| 11 | 6.d3* | +1.95 | +0.19 | d4 | 176 | 15% | mistake |
| 12 | 6...d6 | +0.19 | +0.24 | O-O | 5 | 0% | excellent |
| 13 | 7.Be3* | +0.24 | +0.00 | b4 | 24 | 2% | good |
| 14 | 7...Bxe3 | +0.00 | -0.01 | Bxe3 | 0 | 0% | best |
| 15 | 8.fxe3* | -0.01 | +0.00 | fxe3 | 0 | 0% | best |
| 16 | 8...Bg4 | +0.00 | +0.27 | Ne7 | 27 | 2% | good |
| 17 | 9.Nbd2* | +0.27 | +0.14 | a4 | 13 | 1% | excellent |
| 18 | 9...a6 | +0.14 | +0.54 | Na5 | 40 | 4% | good |
| 19 | 10.h3* | +0.54 | +0.48 | Qb3 | 6 | 1% | excellent |
| 20 | 10...Bh5 | +0.48 | +0.64 | Be6 | 16 | 1% | excellent |
| 21 | 11.g4* | +0.64 | +0.01 | a4 | 63 | 6% | inaccuracy |
| 22 | 11...Bg6 | +0.01 | +0.05 | Bg6 | 4 | 0% | best |
| 23 | 12.d4* | +0.05 | -0.69 | Nh4 | 74 | 7% | inaccuracy |
| 24 | 12...exd4 | -0.69 | +0.18 | h5 | 87 | 8% | inaccuracy |
| 25 | 13.exd4* | +0.18 | +0.14 | exd4 | 4 | 0% | best |
| 26 | 13...Qd7 | +0.14 | +0.57 | O-O | 43 | 4% | good |
| 27 | 14.Re1* | +0.57 | +0.06 | Bb3 | 51 | 5% | good |
| 28 | 14...O-O-O | +0.06 | +0.06 | O-O-O | 0 | 0% | best |
| 29 | 15.e5* | +0.06 | -1.19 | Nh4 | 125 | 11% | mistake |
| 30 | 15...dxe5 | -1.19 | -1.23 | dxe5 | 0 | 0% | best |
| 31 | 16.dxe5* | -1.23 | -1.13 | Nxe5 | 0 | 0% | excellent |
| 32 | 16...Nxg4 | -1.13 | +1.09 | Ne4 | 222 | 20% | blunder |
| 33 | 17.hxg4* | +1.09 | -0.57 | e6 | 166 | 15% | mistake |
| 34 | 17...Qxg4+ | -0.57 | -0.64 | Qxg4+ | 0 | 0% | best |
| 35 | 18.Kf2* | -0.64 | -1.31 | Kh1 | 67 | 6% | inaccuracy |
| 36 | 18...Bh5 | -1.31 | -0.99 | Qf4 | 32 | 3% | good |
| 37 | 19.Re3* | -0.99 | -5.09 | Qc2 | 410 | 28% | blunder |
| 38 | 19...Qf4 | -5.09 | -4.80 | Nxe5 | 29 | 1% | excellent |
| 39 | 20.Be2* | -4.80 | -5.52 | e6 | 72 | 3% | good |
| 40 | 20...Bxf3 | -5.52 | -5.70 | Bxf3 | 0 | 0% | best |
| 41 | 21.Bxf3* | -5.70 | -5.65 | Qg1 | 0 | 0% | excellent |
| 42 | 21...Qh2+ | -5.65 | -3.88 | Nxe5 | 177 | 8% | inaccuracy |
| 43 | 22.Bg2* | -3.88 | -3.93 | Bg2 | 5 | 0% | best |
| 44 | 22...Nxe5 | -3.93 | +0.05 | Qf4+ | 398 | 31% | blunder |
| 45 | 23.Qh1* | +0.05 | -7.12 | Qe2 | 717 | 44% | blunder |
| 46 | 23...Qf4+ | -7.12 | -6.56 | Rxd2+ | 56 | 1% | excellent |
| 47 | 24.Nf3* | -6.56 | -6.83 | Ke2 | 27 | 1% | excellent |
| 48 | 24...Nd3+ | -6.83 | -0.33 | Ng4+ | 650 | 39% | blunder |
| 49 | 25.Ke2* | -0.33 | -0.26 | Ke2 | 0 | 0% | best |
| 50 | 25...Rhe8 | -0.26 | +0.00 | Qc4 | 26 | 2% | good |
| 51 | 26.Rxe8* | +0.00 | +0.00 | Rxe8 | 0 | 0% | best |
| 52 | 26...Rxe8+ | +0.00 | +0.00 | Rxe8+ | 0 | 0% | best |
| 53 | 27.Kxd3* | +0.00 | +0.00 | Kxd3 | 0 | 0% | best |
| 54 | 27...Qe3+ | +0.00 | +3.42 | Qe4+ | 342 | 28% | blunder |
| 55 | 28.Kc2* | +3.42 | +3.42 | Kc2 | 0 | 0% | best |
| 56 | 28...Qf2+ | +3.42 | +5.59 | Qe4+ | 217 | 11% | mistake |
| 57 | 29.Kb3* | +5.59 | +2.66 | Nd2 | 293 | 16% | mistake |
| 58 | 29...Re2 | +2.66 | +2.85 | Re2 | 19 | 1% | best |
| 59 | 30.Qf1* | +2.85 | -M6 | Bh3+ |  | 72% | blunder |
| 60 | 30...Rxb2+ | -M6 | -0.65 | Qb6+ |  | 42% | blunder |
| 61 | 31.Kc4* | -0.65 | -0.76 | Kc4 | 11 | 1% | best |
| 62 | 31...b5+ | -0.76 | -0.44 | Qxg2 | 32 | 3% | good |
| 63 | 32.Kd5* | -0.44 | -0.37 | Kd5 | 0 | 0% | best |
| 64 | 32...Qc5+ | -0.37 | M8 | Qxg2 |  | 51% | blunder |
| 65 | 33.Kxc5* | M8 | M7 | Kxc5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 7 positional.
- Opening: 1 error(s) (avg wp loss 15%).
- Middlegame: 9 error(s) (avg wp loss 23%).
