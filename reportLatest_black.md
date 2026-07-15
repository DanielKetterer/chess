# (free, so lmk) Game analysis: ugur1997 vs DanielKetterer

Date: 2026.07.14  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171577007110

## Summary

- Accuracy: you 88.4%, opponent 86.3%
- Opening: C50 Italian Game: Giuoco Piano (theory followed through ply 6)
- First deviation from theory: ply 7, Opponent played 4. O-O
- Your moves: 13 best, 10 excellent, 6 good, 1 inaccuracy, 3 mistake, 1 blunder

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

You played 6...O-O. Stockfish preferred Nh6, after which the main line runs 6...Nh6 7. Kh1 O-O 8. Nh3 Kh8 9. Bxh6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nh6 (+1.05), d5 (+1.92), Nxf2 (+2.15).

## Critical positions

- Ply 12 (you), 6...O-O: +1.05 -> +3.79 [evaluation crossed equal -> losing]
- Ply 15 (opponent), 8.Na3: +8.63 -> +2.35
- Ply 17 (opponent), 9.Nh3: +4.36 -> +0.88 [evaluation crossed winning -> equal]
- Ply 18 (you), 9...d5: +0.88 -> +1.28 [only-move situation]
- Ply 19 (opponent), 10.Bxh6: +1.28 -> -6.27 [evaluation crossed equal -> losing]
- Ply 20 (you), 10...Bxg4: -6.27 -> -6.56 [only-move situation]

## Your errors, move by move

### 5...Ng4 (mistake, positional, wp loss 10%)

You played 5...Ng4. Stockfish preferred d6, after which the main line runs 5...d6 6. c3 O-O 7. a4 a5 8. h3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d6 (+0.12), a6 (+0.18), O-O (+0.24).

### 6...O-O (blunder, tactical, wp loss 21%)

You played 6...O-O. Stockfish preferred Nh6, after which the main line runs 6...Nh6 7. Kh1 O-O 8. Nh3 Kh8 9. Bxh6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on g4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nh6 (+1.05), d5 (+1.92), Nxf2 (+2.15).

### 7...Nb4 (mistake, positional, wp loss 16%)

You played 7...Nb4. Stockfish preferred h6, after which the main line runs 7...h6 8. Nxf7 Rxf7 9. Qh5 Qf6 10. Qxf7+. Why it went wrong: motif: creates threat on g5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: h6 (+3.69), d5 (+4.17), Qf6 (+5.28).

### 8...h6 (mistake, positional, wp loss 13%)

You played 8...h6. Stockfish preferred d5, after which the main line runs 8...d5 9. Qh4 h6 10. exd5 Be7 11. Nxf7. Why it went wrong: motif: fork; creates threat on g4, c4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d5 (+2.35), h6 (+4.75), Qf6 (+5.29).

### 28...Rf8 (inaccuracy, positional, wp loss 6%)

You played 28...Rf8. Stockfish preferred Qf5, after which the main line runs 28...Qf5 29. Bb3 d5 30. Reg3 Kf8 31. Bc2. Why it went wrong: motif: creates threat on f2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 11; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Qf5 (-5.77), Qh5 (-5.29), Kf8 (-5.24).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.38 | +0.46 | e4 | 0 | 0% | best |
| 2 | 1...e5* | +0.46 | +0.46 | c5 | 0 | 0% | excellent |
| 3 | 2.Nf3 | +0.46 | +0.35 | Nf3 | 11 | 1% | best |
| 4 | 2...Nc6* | +0.35 | +0.50 | Nc6 | 15 | 1% | best |
| 5 | 3.Bc4 | +0.50 | +0.19 | Bb5 | 31 | 3% | good |
| 6 | 3...Bc5* | +0.19 | +0.30 | Nf6 | 11 | 1% | excellent |
| 7 | 4.O-O | +0.30 | +0.16 | c3 | 14 | 1% | excellent |
| 8 | 4...Nf6* | +0.16 | +0.30 | Nf6 | 14 | 1% | best |
| 9 | 5.d3 | +0.30 | +0.12 | Nc3 | 18 | 2% | excellent |
| 10 | 5...Ng4* | +0.12 | +1.25 | d6 | 113 | 10% | mistake |
| 11 | 6.Ng5 | +1.25 | +1.05 | Bxf7+ | 20 | 2% | excellent |
| 12 | 6...O-O* | +1.05 | +3.79 | Nh6 | 274 | 21% | blunder |
| 13 | 7.Qxg4 | +3.79 | +3.69 | Qxg4 | 10 | 1% | best |
| 14 | 7...Nb4* | +3.69 | +8.63 | h6 | 494 | 16% | mistake |
| 15 | 8.Na3 | +8.63 | +2.35 | Qf5 | 628 | 26% | blunder |
| 16 | 8...h6* | +2.35 | +4.36 | d5 | 201 | 13% | mistake |
| 17 | 9.Nh3 | +4.36 | +0.88 | Bxf7+ | 348 | 25% | blunder |
| 18 | 9...d5* | +0.88 | +1.28 | d5 | 40 | 4% | best |
| 19 | 10.Bxh6 | +1.28 | -6.27 | Qg3 | 755 | 53% | blunder |
| 20 | 10...Bxg4* | -6.27 | -6.56 | Bxg4 | 0 | 0% | best |
| 21 | 11.Bg5 | -6.56 | -6.84 | Be3 | 28 | 1% | excellent |
| 22 | 11...Qd7* | -6.84 | -6.22 | Qd7 | 62 | 2% | best |
| 23 | 12.exd5 | -6.22 | -6.50 | exd5 | 28 | 1% | best |
| 24 | 12...Bxh3* | -6.50 | -6.01 | Nxd5 | 49 | 1% | excellent |
| 25 | 13.gxh3 | -6.01 | -6.34 | gxh3 | 33 | 1% | best |
| 26 | 13...Qxh3* | -6.34 | -6.29 | Qxh3 | 5 | 0% | best |
| 27 | 14.c3 | -6.29 | -7.15 | c3 | 86 | 2% | best |
| 28 | 14...Qg4+* | -7.15 | -7.07 | Nxd3 | 8 | 0% | excellent |
| 29 | 15.Kh1 | -7.07 | -6.76 | Kh1 | 0 | 0% | best |
| 30 | 15...Qxg5* | -6.76 | -6.01 | Qf3+ | 75 | 2% | good |
| 31 | 16.cxb4 | -6.01 | -6.51 | cxb4 | 50 | 2% | best |
| 32 | 16...Bd6* | -6.51 | -5.97 | Bb6 | 54 | 2% | excellent |
| 33 | 17.Nb5 | -5.97 | -6.25 | Rg1 | 28 | 1% | excellent |
| 34 | 17...e4* | -6.25 | -5.74 | Qh6 | 51 | 2% | excellent |
| 35 | 18.Rg1 | -5.74 | -6.21 | Rg1 | 47 | 2% | best |
| 36 | 18...Qh4* | -6.21 | -5.65 | Qh6 | 56 | 2% | excellent |
| 37 | 19.Nxd6 | -5.65 | -5.89 | Nxd6 | 24 | 1% | best |
| 38 | 19...cxd6* | -5.89 | -5.65 | cxd6 | 24 | 1% | best |
| 39 | 20.dxe4 | -5.65 | -6.26 | Rae1 | 61 | 2% | good |
| 40 | 20...Rfe8* | -6.26 | -5.64 | Rfc8 | 62 | 2% | good |
| 41 | 21.Bd3 | -5.64 | -5.91 | Bd3 | 27 | 1% | best |
| 42 | 21...f5* | -5.91 | -5.03 | Re5 | 88 | 3% | good |
| 43 | 22.Rae1 | -5.03 | -5.65 | Rg3 | 62 | 2% | good |
| 44 | 22...Qh3* | -5.65 | -4.53 | Qf4 | 112 | 5% | good |
| 45 | 23.Bb1 | -4.53 | -5.57 | Re3 | 104 | 4% | good |
| 46 | 23...Qf3+* | -5.57 | -5.69 | Qf3+ | 0 | 0% | best |
| 47 | 24.Rg2 | -5.69 | -5.52 | Rg2 | 0 | 0% | best |
| 48 | 24...fxe4* | -5.52 | -5.65 | fxe4 | 0 | 0% | best |
| 49 | 25.Re3 | -5.65 | -5.86 | Re3 | 21 | 1% | best |
| 50 | 25...Qd1+* | -5.86 | -5.68 | Qf4 | 18 | 1% | excellent |
| 51 | 26.Rg1 | -5.68 | -5.74 | Rg1 | 6 | 0% | best |
| 52 | 26...Qxd5* | -5.74 | -4.71 | Qd4 | 103 | 4% | good |
| 53 | 27.h4 | -4.71 | -6.28 | Bc2 | 157 | 6% | inaccuracy |
| 54 | 27...Re6* | -6.28 | -5.43 | Qh5 | 85 | 3% | good |
| 55 | 28.Bc2 | -5.43 | -5.77 | Rg5 | 34 | 1% | excellent |
| 56 | 28...Rf8* | -5.77 | -4.35 | Qf5 | 142 | 6% | inaccuracy |
| 57 | 29.Bb3 | -4.35 | -4.42 | Bb3 | 7 | 0% | best |
| 58 | 29...Qe5* | -4.42 | -3.63 | Qe5 | 79 | 4% | best |
| 59 | 30.Bxe6+ | -3.63 | -5.39 | Rg5 | 176 | 9% | inaccuracy |
| 60 | 30...Qxe6* | -5.39 | -5.38 | Qxe6 | 1 | 0% | best |
| 61 | 31.Reg3 | -5.38 | -5.39 | Rc3 | 1 | 0% | excellent |
| 62 | 31...Rxf2* | -5.39 | -5.42 | Kh8 | 0 | 0% | excellent |
| 63 | 32.Rxg7+ | -5.42 | -5.91 | Rg4 | 49 | 2% | excellent |
| 64 | 32...Kf8* | -5.91 | -6.07 | Kf8 | 0 | 0% | best |
| 65 | 33.R7g2 | -6.07 | -M2 | R1g2 |  | 10% | inaccuracy |
| 66 | 33...Qh3+* | -M2 | -M1 | Qh3+ |  | 0% | best |
| 67 | 34.Rh2 | -M1 | -M1 | Rh2 |  | 0% | best |
| 68 | 34...Qxh2#* | -M1 | -M1 | Rxh2# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 1 tactical, 4 positional.
- Opening: 4 error(s) (avg wp loss 15%).
- Middlegame: 1 error(s) (avg wp loss 6%).
