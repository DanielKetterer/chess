# (free, so lmk) Game analysis: DanielKetterer vs jorgefortunati50

Date: 2026.07.23  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171987878016

## Summary

- Lichess accuracy: you 60.3%, opponent 60.9%
- Opening: C54 Italian Game: Classical Variation, Giuoco Pianissimo, with h6 (theory followed through ply 12)
- First deviation from theory: ply 13, Opponent played 7. Be3
- Your moves: 10 best, 3 excellent, 8 good, 3 inaccuracy, 3 mistake, 5 blunder

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

You played 32...Qc5+. Stockfish preferred Qxg2, after which the main line runs 32...Qxg2 33. Qxg2 Rxg2 34. a4 Rg3 35. Ne5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on c5 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 3; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxg2 (-0.56), Qe3 (-0.27), Qg3 (+0.00).

## Critical positions

- Ply 15 (opponent), 8.fxe3: -0.01 -> -0.04 [only-move situation]
- Ply 22 (you), 11...Bg6: +0.19 -> +0.35 [only-move situation]
- Ply 37 (opponent), 19.Re3: -1.06 -> -4.75 [evaluation crossed equal -> losing]
- Ply 44 (you), 22...Nxe5: -3.20 -> +0.14 [only-move situation; evaluation crossed winning -> equal]
- Ply 45 (opponent), 23.Qh1: +0.14 -> -6.83 [only-move situation; evaluation crossed equal -> losing]
- Ply 48 (you), 24...Nd3+: -6.54 -> -0.86 [evaluation crossed winning -> equal]
- Ply 49 (opponent), 25.Ke2: -0.86 -> -0.66 [only-move situation]
- Ply 51 (opponent), 26.Rxe8: +0.00 -> +0.00 [only-move situation]

## Your errors, move by move

### 5...Nf6 (inaccuracy, positional, wp loss 7%)

You played 5...Nf6. Stockfish preferred Bb6, after which the main line runs 5...Bb6 6. d4 exd4 7. cxd4 d6 8. h3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Bb6 (+0.82), d6 (+0.83), Qe7 (+1.28).

### 12...exd4 (inaccuracy, positional, wp loss 6%)

You played 12...exd4. Stockfish preferred h5, after which the main line runs 12...h5 13. g5 Nxe4 14. Nxe4 d5 15. Nc5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: h5 (-0.44), O-O (-0.19), Bh7 (-0.16).

### 16...Nxg4 (mistake, tactical, wp loss 15%)

You played 16...Nxg4. Stockfish preferred Ne4, after which the main line runs 16...Ne4 17. Nxe4 Qxd1 18. Raxd1 Rxd1 19. Nd6+. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 16; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Ne4 (-0.97), Nh7 (-0.65), Nd5 (-0.62).

### 21...Qh2+ (mistake, tactical, wp loss 13%)

You played 21...Qh2+. Stockfish preferred Nxe5, after which the main line runs 21...Nxe5 22. Rxe5 Rxd2+ 23. Qxd2 Qxd2+ 24. Re2. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxe5 (-5.35), g5 (-3.08), Qh2+ (-3.03).

### 22...Nxe5 (blunder, tactical, wp loss 28%)

You played 22...Nxe5. Stockfish preferred Qf4+, after which the main line runs 22...Qf4+ 23. Ke2 Nxe5 24. Qg1 Rhe8 25. Bh3+. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qf4+ (-3.20), Nxe5 (+0.29), h5 (+0.74).

### 24...Nd3+ (blunder, tactical, wp loss 34%)

You played 24...Nd3+. Stockfish preferred Ng4+, after which the main line runs 24...Ng4+ 25. Kf1 Nxe3+ 26. Kg1 Nxg2 27. Qh3+. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: the best move was a forcing check; motif: fork; creates threat on e3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Ng4+ (-6.54), Rd2+ (-5.11), Rhe8 (-3.82).

### 25...Rhe8 (inaccuracy, positional, wp loss 6%)

You played 25...Rhe8. Stockfish preferred Qc4, after which the main line runs 25...Qc4 26. Kf1 Nb4+ 27. Kf2 Nc2 28. Nd4. Why it went wrong: left knight on d3 insufficiently defended; motif: creates threat on b2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qc4 (-0.66), Kb8 (-0.11), Qa4 (+0.00).

### 27...Qe3+ (blunder, tactical, wp loss 26%)

You played 27...Qe3+. Stockfish preferred Qe4+, after which the main line runs 27...Qe4+ 28. Kd2 Rd8+ 29. Nd4 Rxd4+ 30. cxd4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on e3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qe4+ (+0.00), Qe3+ (+3.01), Qf5+ (+3.05).

### 28...Qf2+ (mistake, tactical, wp loss 11%)

You played 28...Qf2+. Stockfish preferred Qe4+, after which the main line runs 28...Qe4+ 29. Kc1 Qf4+ 30. Kd1 Rd8+ 31. Ke1. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qe4+ (+3.38), c6 (+5.20), Kb8 (+5.20).

### 30...Rxb2+ (blunder, tactical, wp loss 42%)

You played 30...Rxb2+. Stockfish preferred Qb6+, after which the main line runs 30...Qb6+ 31. Kc4 Qc6+ 32. Kb3 Qb5+ 33. Ka3. There was a forced mate on the board and this move let it slip. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left rook on b2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qb6+ (-M6), Rxb2+ (-0.66), Qxg2 (-0.01).

### 32...Qc5+ (blunder, tactical, wp loss 53%)

You played 32...Qc5+. Stockfish preferred Qxg2, after which the main line runs 32...Qxg2 33. Qxg2 Rxg2 34. a4 Rg3 35. Ne5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on c5 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 3; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxg2 (-0.56), Qe3 (-0.27), Qg3 (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.32 | +0.25 | d4 | 7 | 1% | excellent |
| 2 | 1...e5* | +0.25 | +0.24 | e5 | 0 | 0% | best |
| 3 | 2.Nf3 | +0.24 | +0.25 | Nf3 | 0 | 0% | best |
| 4 | 2...Nc6* | +0.25 | +0.21 | Nc6 | 0 | 0% | best |
| 5 | 3.Bc4 | +0.21 | +0.14 | Bb5 | 7 | 1% | excellent |
| 6 | 3...h6* | +0.14 | +0.62 | Nf6 | 48 | 4% | good |
| 7 | 4.O-O | +0.62 | +0.42 | d4 | 20 | 2% | excellent |
| 8 | 4...Bc5* | +0.42 | +0.86 | Nf6 | 44 | 4% | good |
| 9 | 5.c3 | +0.86 | +0.82 | c3 | 4 | 0% | best |
| 10 | 5...Nf6* | +0.82 | +1.58 | Bb6 | 76 | 7% | inaccuracy |
| 11 | 6.d3 | +1.58 | +0.25 | d4 | 133 | 12% | mistake |
| 12 | 6...d6* | +0.25 | +0.20 | Bb6 | 0 | 0% | excellent |
| 13 | 7.Be3 | +0.20 | +0.00 | b4 | 20 | 2% | excellent |
| 14 | 7...Bxe3* | +0.00 | -0.01 | Bxe3 | 0 | 0% | best |
| 15 | 8.fxe3 | -0.01 | -0.04 | fxe3 | 3 | 0% | best |
| 16 | 8...Bg4* | -0.04 | +0.36 | O-O | 40 | 4% | good |
| 17 | 9.Nbd2 | +0.36 | +0.25 | a4 | 11 | 1% | excellent |
| 18 | 9...a6* | +0.25 | +0.57 | Na5 | 32 | 3% | good |
| 19 | 10.h3 | +0.57 | +0.51 | h3 | 6 | 1% | best |
| 20 | 10...Bh5* | +0.51 | +0.73 | Bd7 | 22 | 2% | excellent |
| 21 | 11.g4 | +0.73 | +0.19 | a4 | 54 | 5% | good |
| 22 | 11...Bg6* | +0.19 | +0.35 | Bg6 | 16 | 1% | best |
| 23 | 12.d4 | +0.35 | -0.44 | Nh4 | 79 | 7% | inaccuracy |
| 24 | 12...exd4* | -0.44 | +0.18 | h5 | 62 | 6% | inaccuracy |
| 25 | 13.exd4 | +0.18 | +0.18 | exd4 | 0 | 0% | best |
| 26 | 13...Qd7* | +0.18 | +0.50 | O-O | 32 | 3% | good |
| 27 | 14.Re1 | +0.50 | -0.03 | Bb3 | 53 | 5% | good |
| 28 | 14...O-O-O* | -0.03 | -0.03 | O-O-O | 0 | 0% | best |
| 29 | 15.e5 | -0.03 | -0.84 | Nh4 | 81 | 7% | inaccuracy |
| 30 | 15...dxe5* | -0.84 | -0.67 | dxe5 | 17 | 2% | best |
| 31 | 16.dxe5 | -0.67 | -0.97 | dxe5 | 30 | 3% | best |
| 32 | 16...Nxg4* | -0.97 | +0.65 | Ne4 | 162 | 15% | mistake |
| 33 | 17.hxg4 | +0.65 | -0.75 | e6 | 140 | 13% | mistake |
| 34 | 17...Qxg4+* | -0.75 | -0.71 | Qxg4+ | 4 | 0% | best |
| 35 | 18.Kf2 | -0.71 | -1.46 | Kh1 | 75 | 7% | inaccuracy |
| 36 | 18...Bh5* | -1.46 | -1.06 | Qf4 | 40 | 3% | good |
| 37 | 19.Re3 | -1.06 | -4.75 | Qc2 | 369 | 26% | blunder |
| 38 | 19...Qf4* | -4.75 | -4.00 | Nxe5 | 75 | 4% | good |
| 39 | 20.Be2 | -4.00 | -5.56 | Bxf7 | 156 | 7% | inaccuracy |
| 40 | 20...Bxf3* | -5.56 | -5.64 | Bxf3 | 0 | 0% | best |
| 41 | 21.Bxf3 | -5.64 | -5.35 | Bxf3 | 0 | 0% | best |
| 42 | 21...Qh2+* | -5.35 | -2.99 | Nxe5 | 236 | 13% | mistake |
| 43 | 22.Bg2 | -2.99 | -3.20 | Bg2 | 21 | 1% | best |
| 44 | 22...Nxe5* | -3.20 | +0.14 | Qf4+ | 334 | 28% | blunder |
| 45 | 23.Qh1 | +0.14 | -6.83 | Qe2 | 697 | 44% | blunder |
| 46 | 23...Qf4+* | -6.83 | -6.10 | Rxd2+ | 73 | 2% | good |
| 47 | 24.Nf3 | -6.10 | -6.54 | Ke2 | 44 | 1% | excellent |
| 48 | 24...Nd3+* | -6.54 | -0.86 | Ng4+ | 568 | 34% | blunder |
| 49 | 25.Ke2 | -0.86 | -0.66 | Ke2 | 0 | 0% | best |
| 50 | 25...Rhe8* | -0.66 | +0.00 | Qc4 | 66 | 6% | inaccuracy |
| 51 | 26.Rxe8 | +0.00 | +0.00 | Rxe8 | 0 | 0% | best |
| 52 | 26...Rxe8+* | +0.00 | +0.00 | Rxe8+ | 0 | 0% | best |
| 53 | 27.Kxd3 | +0.00 | +0.00 | Kxd3 | 0 | 0% | best |
| 54 | 27...Qe3+* | +0.00 | +3.10 | Qe4+ | 310 | 26% | blunder |
| 55 | 28.Kc2 | +3.10 | +3.38 | Kc2 | 0 | 0% | best |
| 56 | 28...Qf2+* | +3.38 | +5.56 | Qe4+ | 218 | 11% | mistake |
| 57 | 29.Kb3 | +5.56 | +2.07 | Nd2 | 349 | 20% | blunder |
| 58 | 29...Re2* | +2.07 | +2.07 | Re2 | 0 | 0% | best |
| 59 | 30.Qf1 | +2.07 | -M6 | Bh3+ |  | 66% | blunder |
| 60 | 30...Rxb2+* | -M6 | -0.64 | Qb6+ |  | 42% | blunder |
| 61 | 31.Kc4 | -0.64 | -0.72 | Kc4 | 8 | 1% | best |
| 62 | 31...b5+* | -0.72 | -0.56 | Qxg2 | 16 | 1% | excellent |
| 63 | 32.Kd5 | -0.56 | -0.56 | Kd5 | 0 | 0% | best |
| 64 | 32...Qc5+* | -0.56 | +43.21 | Qxg2 | 4377 | 53% | blunder |
| 65 | 33.Kxc5 | +43.21 | M18 | Kxc5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 8 tactical, 3 positional.
- Opening: 1 error(s) (avg wp loss 7%).
- Middlegame: 9 error(s) (avg wp loss 20%).
- Endgame: 1 error(s) (avg wp loss 53%).
