# (free, so lmk) Game analysis: DanielKetterer vs jorgefortunati50

Date: 2026.07.23  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171987878016

## Summary

- Lichess accuracy: you 60.3%, opponent 57.3%
- Opening: C54 Italian Game: Classical Variation, Giuoco Pianissimo, with h6 (theory followed through ply 12)
- First deviation from theory: ply 13, Opponent played 7. Be3
- Your moves: 9 best, 5 excellent, 8 good, 3 inaccuracy, 1 mistake, 6 blunder

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

You played 32...Qc5+. Stockfish preferred Qxg2, after which the main line runs 32...Qxg2 33. Qxg2 Rxg2 34. a4 Rg3 35. Ne5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on c5 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxg2 (-0.37), Qe3 (-0.16), Qg3 (+0.00).

## Critical positions

- Ply 15 (opponent), 8.fxe3: -0.01 -> +0.00 [only-move situation]
- Ply 22 (you), 11...Bg6: +0.01 -> +0.05 [only-move situation]
- Ply 32 (you), 16...Nxg4: -1.13 -> +1.09
- Ply 33 (opponent), 17.hxg4: +1.09 -> -0.57 [only-move situation]
- Ply 37 (opponent), 19.Re3: -0.99 -> -5.09 [evaluation crossed equal -> losing]
- Ply 44 (you), 22...Nxe5: -3.93 -> +0.05 [only-move situation; evaluation crossed winning -> equal]
- Ply 45 (opponent), 23.Qh1: +0.05 -> -7.12 [only-move situation; evaluation crossed equal -> losing]
- Ply 48 (you), 24...Nd3+: -6.83 -> -0.33 [evaluation crossed winning -> equal]

## Your errors, move by move

### 5...Nf6 (inaccuracy, positional, wp loss 9%)

You played 5...Nf6. Stockfish preferred d6, after which the main line runs 5...d6 6. d4 exd4 7. cxd4 Bb6 8. Nc3. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d6 (+0.86), Bb6 (+0.94), Qf6 (+1.18).

### 12...exd4 (inaccuracy, positional, wp loss 8%)

You played 12...exd4. Stockfish preferred h5, after which the main line runs 12...h5 13. g5 Nxe4 14. Nxe4 d5 15. Nc5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: h5 (-0.69), O-O (-0.21), Bh7 (-0.16).

### 16...Nxg4 (blunder, tactical, wp loss 20%)

You played 16...Nxg4. Stockfish preferred Ne4, after which the main line runs 16...Ne4 17. Nxe4 Qxd1 18. Raxd1 Rxd1 19. Nd6+. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 17; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Ne4 (-1.13), Nh7 (-0.88), Nd5 (-0.53).

### 21...Qh2+ (inaccuracy, positional, wp loss 8%)

You played 21...Qh2+. Stockfish preferred Nxe5, after which the main line runs 21...Nxe5 22. Rxe5 Rxd2+ 23. Qxd2 Qxd2+ 24. Re2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nxe5 (-5.65), Qh2+ (-3.97), g5 (-3.33).

### 22...Nxe5 (blunder, tactical, wp loss 31%)

You played 22...Nxe5. Stockfish preferred Qf4+, after which the main line runs 22...Qf4+ 23. Ke2 Nxe5 24. Qg1 Rhe8 25. Rd1. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qf4+ (-3.93), Nxe5 (+0.00), Kb8 (+0.65).

### 24...Nd3+ (blunder, tactical, wp loss 39%)

You played 24...Nd3+. Stockfish preferred Ng4+, after which the main line runs 24...Ng4+ 25. Kf1 Qxe3 26. Qh4 f5 27. Re1. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: the best move was a forcing check; motif: fork; creates threat on e3. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Ng4+ (-6.83), Rd2+ (-5.17), Rhe8 (-4.07).

### 27...Qe3+ (blunder, tactical, wp loss 28%)

You played 27...Qe3+. Stockfish preferred Qe4+, after which the main line runs 27...Qe4+ 28. Kd2 Rd8+ 29. Nd4 Rxd4+ 30. cxd4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on e3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qe4+ (+0.00), Qf5+ (+3.40), Qe3+ (+3.42).

### 28...Qf2+ (mistake, tactical, wp loss 11%)

You played 28...Qf2+. Stockfish preferred Qe4+, after which the main line runs 28...Qe4+ 29. Kc1 Qf4+ 30. Kd1 Rd8+ 31. Ke1. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qe4+ (+3.42), Qb6 (+5.36), Kb8 (+5.38).

### 30...Rxb2+ (blunder, tactical, wp loss 42%)

You played 30...Rxb2+. Stockfish preferred Qb6+, after which the main line runs 30...Qb6+ 31. Kc4 Qc6+ 32. Kb3 Qb5+ 33. Ka3. There was a forced mate on the board and this move let it slip. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left rook on b2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qb6+ (-M6), Rxb2+ (-0.76), Qxg2 (-0.11).

### 32...Qc5+ (blunder, tactical, wp loss 51%)

You played 32...Qc5+. Stockfish preferred Qxg2, after which the main line runs 32...Qxg2 33. Qxg2 Rxg2 34. a4 Rg3 35. Ne5. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on c5 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 2; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qxg2 (-0.37), Qe3 (-0.16), Qg3 (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.31 | +0.20 | e4 | 11 | 1% | best |
| 2 | 1...e5* | +0.20 | +0.21 | c6 | 1 | 0% | excellent |
| 3 | 2.Nf3 | +0.21 | +0.20 | Nf3 | 1 | 0% | best |
| 4 | 2...Nc6* | +0.20 | +0.23 | Nc6 | 3 | 0% | best |
| 5 | 3.Bc4 | +0.23 | +0.21 | Bb5 | 2 | 0% | excellent |
| 6 | 3...h6* | +0.21 | +0.64 | Bc5 | 43 | 4% | good |
| 7 | 4.O-O | +0.64 | +0.50 | d4 | 14 | 1% | excellent |
| 8 | 4...Bc5* | +0.50 | +0.93 | d6 | 43 | 4% | good |
| 9 | 5.c3 | +0.93 | +0.86 | c3 | 7 | 1% | best |
| 10 | 5...Nf6* | +0.86 | +1.95 | d6 | 109 | 9% | inaccuracy |
| 11 | 6.d3 | +1.95 | +0.19 | d4 | 176 | 15% | mistake |
| 12 | 6...d6* | +0.19 | +0.24 | O-O | 5 | 0% | excellent |
| 13 | 7.Be3 | +0.24 | +0.00 | b4 | 24 | 2% | good |
| 14 | 7...Bxe3* | +0.00 | -0.01 | Bxe3 | 0 | 0% | best |
| 15 | 8.fxe3 | -0.01 | +0.00 | fxe3 | 0 | 0% | best |
| 16 | 8...Bg4* | +0.00 | +0.27 | Ne7 | 27 | 2% | good |
| 17 | 9.Nbd2 | +0.27 | +0.14 | a4 | 13 | 1% | excellent |
| 18 | 9...a6* | +0.14 | +0.54 | Na5 | 40 | 4% | good |
| 19 | 10.h3 | +0.54 | +0.48 | Qb3 | 6 | 1% | excellent |
| 20 | 10...Bh5* | +0.48 | +0.64 | Be6 | 16 | 1% | excellent |
| 21 | 11.g4 | +0.64 | +0.01 | a4 | 63 | 6% | inaccuracy |
| 22 | 11...Bg6* | +0.01 | +0.05 | Bg6 | 4 | 0% | best |
| 23 | 12.d4 | +0.05 | -0.69 | Nh4 | 74 | 7% | inaccuracy |
| 24 | 12...exd4* | -0.69 | +0.18 | h5 | 87 | 8% | inaccuracy |
| 25 | 13.exd4 | +0.18 | +0.14 | exd4 | 4 | 0% | best |
| 26 | 13...Qd7* | +0.14 | +0.57 | O-O | 43 | 4% | good |
| 27 | 14.Re1 | +0.57 | +0.06 | Bb3 | 51 | 5% | good |
| 28 | 14...O-O-O* | +0.06 | +0.06 | O-O-O | 0 | 0% | best |
| 29 | 15.e5 | +0.06 | -1.19 | Nh4 | 125 | 11% | mistake |
| 30 | 15...dxe5* | -1.19 | -1.23 | dxe5 | 0 | 0% | best |
| 31 | 16.dxe5 | -1.23 | -1.13 | Nxe5 | 0 | 0% | excellent |
| 32 | 16...Nxg4* | -1.13 | +1.09 | Ne4 | 222 | 20% | blunder |
| 33 | 17.hxg4 | +1.09 | -0.57 | e6 | 166 | 15% | mistake |
| 34 | 17...Qxg4+* | -0.57 | -0.64 | Qxg4+ | 0 | 0% | best |
| 35 | 18.Kf2 | -0.64 | -1.31 | Kh1 | 67 | 6% | inaccuracy |
| 36 | 18...Bh5* | -1.31 | -0.99 | Qf4 | 32 | 3% | good |
| 37 | 19.Re3 | -0.99 | -5.09 | Qc2 | 410 | 28% | blunder |
| 38 | 19...Qf4* | -5.09 | -4.80 | Nxe5 | 29 | 1% | excellent |
| 39 | 20.Be2 | -4.80 | -5.52 | e6 | 72 | 3% | good |
| 40 | 20...Bxf3* | -5.52 | -5.70 | Bxf3 | 0 | 0% | best |
| 41 | 21.Bxf3 | -5.70 | -5.65 | Qg1 | 0 | 0% | excellent |
| 42 | 21...Qh2+* | -5.65 | -3.88 | Nxe5 | 177 | 8% | inaccuracy |
| 43 | 22.Bg2 | -3.88 | -3.93 | Bg2 | 5 | 0% | best |
| 44 | 22...Nxe5* | -3.93 | +0.05 | Qf4+ | 398 | 31% | blunder |
| 45 | 23.Qh1 | +0.05 | -7.12 | Qe2 | 717 | 44% | blunder |
| 46 | 23...Qf4+* | -7.12 | -6.56 | Rxd2+ | 56 | 1% | excellent |
| 47 | 24.Nf3 | -6.56 | -6.83 | Ke2 | 27 | 1% | excellent |
| 48 | 24...Nd3+* | -6.83 | -0.33 | Ng4+ | 650 | 39% | blunder |
| 49 | 25.Ke2 | -0.33 | -0.26 | Ke2 | 0 | 0% | best |
| 50 | 25...Rhe8* | -0.26 | +0.00 | Qc4 | 26 | 2% | good |
| 51 | 26.Rxe8 | +0.00 | +0.00 | Rxe8 | 0 | 0% | best |
| 52 | 26...Rxe8+* | +0.00 | +0.00 | Rxe8+ | 0 | 0% | best |
| 53 | 27.Kxd3 | +0.00 | +0.00 | Kxd3 | 0 | 0% | best |
| 54 | 27...Qe3+* | +0.00 | +3.42 | Qe4+ | 342 | 28% | blunder |
| 55 | 28.Kc2 | +3.42 | +3.42 | Kc2 | 0 | 0% | best |
| 56 | 28...Qf2+* | +3.42 | +5.59 | Qe4+ | 217 | 11% | mistake |
| 57 | 29.Kb3 | +5.59 | +2.66 | Nd2 | 293 | 16% | mistake |
| 58 | 29...Re2* | +2.66 | +2.85 | Re2 | 19 | 1% | best |
| 59 | 30.Qf1 | +2.85 | -M6 | Bh3+ |  | 72% | blunder |
| 60 | 30...Rxb2+* | -M6 | -0.65 | Qb6+ |  | 42% | blunder |
| 61 | 31.Kc4 | -0.65 | -0.76 | Kc4 | 11 | 1% | best |
| 62 | 31...b5+* | -0.76 | -0.44 | Qxg2 | 32 | 3% | good |
| 63 | 32.Kd5 | -0.44 | -0.37 | Kd5 | 0 | 0% | best |
| 64 | 32...Qc5+* | -0.37 | M8 | Qxg2 |  | 51% | blunder |
| 65 | 33.Kxc5 | M8 | M7 | Kxc5 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 7 tactical, 3 positional.
- Opening: 1 error(s) (avg wp loss 9%).
- Middlegame: 8 error(s) (avg wp loss 23%).
- Endgame: 1 error(s) (avg wp loss 51%).
