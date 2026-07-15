# (free, so lmk) Game analysis: ugur1997 vs DanielKetterer

Date: 2026.07.14  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171577007110

## Summary

- Lichess accuracy: you 85.5%, opponent 71.7%
- Opening: C50 Italian Game: Giuoco Piano (theory followed through ply 6)
- First deviation from theory: ply 7, Opponent played 4. O-O
- Your moves: 15 best, 9 excellent, 6 good, 1 inaccuracy, 2 mistake, 1 blunder

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

You played 6...O-O. Stockfish preferred Nh6, after which the main line runs 6...Nh6 7. Nc3 d6 8. Na4 O-O 9. Nf3. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nh6 (+1.00), d5 (+1.59), Nxf2 (+2.01).

## Critical positions

- Ply 12 (you), 6...O-O: +1.00 -> +4.15 [evaluation crossed equal -> losing]
- Ply 17 (opponent), 9.Nh3: +5.29 -> +1.33 [evaluation crossed winning -> equal]
- Ply 18 (you), 9...d5: +1.33 -> +1.28 [only-move situation]
- Ply 19 (opponent), 10.Bxh6: +1.28 -> -6.34 [evaluation crossed equal -> losing]
- Ply 20 (you), 10...Bxg4: -6.34 -> -6.54 [only-move situation]

## Your errors, move by move

### 5...Ng4 (inaccuracy, positional, wp loss 9%)

You played 5...Ng4. Stockfish preferred d6, after which the main line runs 5...d6 6. c3 a6 7. Nbd2 O-O 8. Bb3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d6 (+0.16), a6 (+0.16), O-O (+0.17).

### 6...O-O (blunder, tactical, wp loss 23%)

You played 6...O-O. Stockfish preferred Nh6, after which the main line runs 6...Nh6 7. Nc3 d6 8. Na4 O-O 9. Nf3. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nh6 (+1.00), d5 (+1.59), Nxf2 (+2.01).

### 7...Nb4 (mistake, positional, wp loss 11%)

You played 7...Nb4. Stockfish preferred h6, after which the main line runs 7...h6 8. Nxf7 Rxf7 9. Qg6 Qf6 10. Qxf6. Why it went wrong: motif: creates threat on g5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: h6 (+4.16), d5 (+4.78), g6 (+5.02).

### 8...h6 (mistake, positional, wp loss 12%)

You played 8...h6. Stockfish preferred d5, after which the main line runs 8...d5 9. Qh5 h6 10. exd5 hxg5 11. Bxg5. Why it went wrong: motif: fork; creates threat on g4, c4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d5 (+3.13), h6 (+4.97), Qf6 (+5.63).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.35 | +0.35 | Nf3 | 0 | 0% | excellent |
| 2 | 1...e5* | +0.35 | +0.35 | e6 | 0 | 0% | excellent |
| 3 | 2.Nf3 | +0.35 | +0.39 | Nf3 | 0 | 0% | best |
| 4 | 2...Nc6* | +0.39 | +0.34 | Nc6 | 0 | 0% | best |
| 5 | 3.Bc4 | +0.34 | +0.17 | Bb5 | 17 | 2% | excellent |
| 6 | 3...Bc5* | +0.17 | +0.28 | Nf6 | 11 | 1% | excellent |
| 7 | 4.O-O | +0.28 | +0.22 | O-O | 6 | 1% | best |
| 8 | 4...Nf6* | +0.22 | +0.25 | Nf6 | 3 | 0% | best |
| 9 | 5.d3 | +0.25 | +0.16 | d3 | 9 | 1% | best |
| 10 | 5...Ng4* | +0.16 | +1.10 | d6 | 94 | 9% | inaccuracy |
| 11 | 6.Ng5 | +1.10 | +1.00 | Bxf7+ | 10 | 1% | excellent |
| 12 | 6...O-O* | +1.00 | +4.15 | Nh6 | 315 | 23% | blunder |
| 13 | 7.Qxg4 | +4.15 | +4.16 | Qxg4 | 0 | 0% | best |
| 14 | 7...Nb4* | +4.16 | +7.03 | h6 | 287 | 11% | mistake |
| 15 | 8.Na3 | +7.03 | +3.13 | Qh5 | 390 | 17% | mistake |
| 16 | 8...h6* | +3.13 | +5.29 | d5 | 216 | 12% | mistake |
| 17 | 9.Nh3 | +5.29 | +1.33 | Bxf7+ | 396 | 26% | blunder |
| 18 | 9...d5* | +1.33 | +1.28 | d5 | 0 | 0% | best |
| 19 | 10.Bxh6 | +1.28 | -6.34 | Qg3 | 762 | 53% | blunder |
| 20 | 10...Bxg4* | -6.34 | -6.54 | Bxg4 | 0 | 0% | best |
| 21 | 11.Bg5 | -6.54 | -6.60 | Bg5 | 6 | 0% | best |
| 22 | 11...Qd7* | -6.60 | -6.52 | f6 | 8 | 0% | excellent |
| 23 | 12.exd5 | -6.52 | -6.82 | c3 | 30 | 1% | excellent |
| 24 | 12...Bxh3* | -6.82 | -6.56 | Bxh3 | 26 | 1% | best |
| 25 | 13.gxh3 | -6.56 | -6.60 | gxh3 | 4 | 0% | best |
| 26 | 13...Qxh3* | -6.60 | -6.60 | Qxh3 | 0 | 0% | best |
| 27 | 14.c3 | -6.60 | -6.88 | Rae1 | 28 | 1% | excellent |
| 28 | 14...Qg4+* | -6.88 | -6.89 | Qg4+ | 0 | 0% | best |
| 29 | 15.Kh1 | -6.89 | -6.88 | Kh1 | 0 | 0% | best |
| 30 | 15...Qxg5* | -6.88 | -6.06 | Qf3+ | 82 | 2% | good |
| 31 | 16.cxb4 | -6.06 | -6.14 | Rg1 | 8 | 0% | excellent |
| 32 | 16...Bd6* | -6.14 | -6.08 | Bd6 | 6 | 0% | best |
| 33 | 17.Nb5 | -6.08 | -6.20 | Rg1 | 12 | 0% | excellent |
| 34 | 17...e4* | -6.20 | -5.94 | g6 | 26 | 1% | excellent |
| 35 | 18.Rg1 | -5.94 | -6.33 | Nxd6 | 39 | 1% | excellent |
| 36 | 18...Qh4* | -6.33 | -6.01 | Qh5 | 32 | 1% | excellent |
| 37 | 19.Nxd6 | -6.01 | -6.07 | Rg2 | 6 | 0% | excellent |
| 38 | 19...cxd6* | -6.07 | -6.01 | cxd6 | 6 | 0% | best |
| 39 | 20.dxe4 | -6.01 | -6.78 | Rg2 | 77 | 2% | good |
| 40 | 20...Rfe8* | -6.78 | -5.90 | Qxe4+ | 88 | 3% | good |
| 41 | 21.Bd3 | -5.90 | -6.15 | Bd3 | 25 | 1% | best |
| 42 | 21...f5* | -6.15 | -5.37 | Qxf2 | 78 | 3% | good |
| 43 | 22.Rae1 | -5.37 | -6.03 | Rg3 | 66 | 2% | good |
| 44 | 22...Qh3* | -6.03 | -5.33 | fxe4 | 70 | 3% | good |
| 45 | 23.Bb1 | -5.33 | -6.09 | Re3 | 76 | 3% | good |
| 46 | 23...Qf3+* | -6.09 | -6.30 | Qf3+ | 0 | 0% | best |
| 47 | 24.Rg2 | -6.30 | -6.39 | Rg2 | 9 | 0% | best |
| 48 | 24...fxe4* | -6.39 | -6.07 | Rac8 | 32 | 1% | excellent |
| 49 | 25.Re3 | -6.07 | -6.57 | Kg1 | 50 | 1% | excellent |
| 50 | 25...Qd1+* | -6.57 | -6.32 | Qf6 | 25 | 1% | excellent |
| 51 | 26.Rg1 | -6.32 | -6.41 | Rg1 | 9 | 0% | best |
| 52 | 26...Qxd5* | -6.41 | -5.48 | Qd2 | 93 | 3% | good |
| 53 | 27.h4 | -5.48 | -6.38 | Bc2 | 90 | 3% | good |
| 54 | 27...Re6* | -6.38 | -6.25 | Qf5 | 13 | 0% | excellent |
| 55 | 28.Bc2 | -6.25 | -6.89 | Reg3 | 64 | 2% | excellent |
| 56 | 28...Rf8* | -6.89 | -5.56 | Qd2 | 133 | 4% | good |
| 57 | 29.Bb3 | -5.56 | -5.80 | Bb3 | 24 | 1% | best |
| 58 | 29...Qe5* | -5.80 | -5.78 | Qd2 | 2 | 0% | excellent |
| 59 | 30.Bxe6+ | -5.78 | -6.18 | Rg5 | 40 | 1% | excellent |
| 60 | 30...Qxe6* | -6.18 | -6.25 | Qxe6 | 0 | 0% | best |
| 61 | 31.Reg3 | -6.25 | -7.26 | Rg2 | 101 | 3% | good |
| 62 | 31...Rxf2* | -7.26 | -8.22 | Rxf2 | 0 | 0% | best |
| 63 | 32.Rxg7+ | -8.22 | -M21 | R1g2 |  | 2% | good |
| 64 | 32...Kf8* | -M21 | -M19 | Kf8 |  | 0% | best |
| 65 | 33.R7g2 | -M19 | -M2 | R1g4 |  | 0% | excellent |
| 66 | 33...Qh3+* | -M2 | -M1 | Qh3+ |  | 0% | best |
| 67 | 34.Rh2 | -M1 | -M1 | Rh2 |  | 0% | best |
| 68 | 34...Qxh2#* | -M1 | -M1 | Qxh2# |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 1 tactical, 3 positional.
- Opening: 4 error(s) (avg wp loss 13%).
