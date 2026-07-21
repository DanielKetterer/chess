# (free, so lmk) Game analysis: DanielKetterer vs DavidManuelPalacios

Date: 2026.07.21  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171880980358

## Summary

- Lichess accuracy: you 74.5%, opponent 80.8%
- Opening: B06 Modern Defense: Two Knights Variation, Suttles Variation (theory followed through ply 8)
- First deviation from theory: ply 9, You played 5. Be3
- Your moves: 7 best, 7 excellent, 5 good, 8 inaccuracy, 6 mistake, 2 blunder

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

You played 27.Rdf1. Stockfish preferred Rd2, after which the main line runs 27. Rd2 Ra1+ 28. Kc2 Rxg1 29. Nxg1 Rg7. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on f3 insufficiently defended; motif: creates threat on a2. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Rd2 (-1.35), Nd2 (-3.84), Rd3 (-4.43).

## Critical positions

- Ply 29 (you), 15.Qd2: +7.62 -> +2.26
- Ply 34 (opponent), 17...Rxg7: +2.51 -> +2.50 [only-move situation]
- Ply 36 (opponent), 18...Rh7: +1.82 -> +1.89 [only-move situation]
- Ply 42 (opponent), 21...Qf8: +2.02 -> +2.02 [only-move situation]
- Ply 43 (you), 22.Qxf8+: +2.02 -> +2.04 [only-move situation]
- Ply 49 (you), 25.cxb3: -0.03 -> -2.01 [only-move situation; evaluation crossed equal -> losing]
- Ply 53 (you), 27.Rdf1: -1.35 -> -5.49 [only-move situation; evaluation crossed equal -> losing]

## Your errors, move by move

### 6.d5 (inaccuracy, positional, wp loss 6%)

You played 6.d5. Stockfish preferred Qd2, after which the main line runs 6. Qd2 Ngf6 7. Bh6 Bxh6 8. Qxh6 e5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qd2 (+0.75), h3 (+0.60), Be2 (+0.58).

### 7.Bb5 (inaccuracy, positional, wp loss 9%)

You played 7.Bb5. Stockfish preferred a4, after which the main line runs 7. a4 Ngf6 8. h3 O-O 9. Bd3 Qc7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a4 (+1.18), h3 (+1.15), Bd3 (+1.01).

### 8.Bxd7+ (inaccuracy, positional, wp loss 9%)

You played 8.Bxd7+. Stockfish preferred Be2, after which the main line runs 8. Be2 a6 9. a4 O-O 10. O-O Rb8. Why it went wrong: left bishop on d7 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 30; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Be2 (+0.79), a4 (+0.76), Bd3 (+0.60).

### 9.Bg5 (mistake, positional, wp loss 11%)

You played 9.Bg5. Stockfish preferred O-O, after which the main line runs 9. O-O Qa5 10. a4 Bxc3 11. bxc3 Qxc3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: O-O (+0.48), a4 (+0.41), Qe2 (+0.16).

### 11.g4 (mistake, positional, wp loss 10%)

You played 11.g4. Stockfish preferred O-O, after which the main line runs 11. O-O Nb6 12. a4 Bg4 13. h3 Bxf3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: O-O (+0.09), a4 (-0.05), h4 (-0.24).

### 15.Qd2 (blunder, positional, wp loss 25%)

You played 15.Qd2. Stockfish preferred Nd4, after which the main line runs 15. Nd4 Qe8 16. Nf5 Nb6 17. Nxd6 Bg4. Why it went wrong: motif: creates threat on h5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 31; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nd4 (+7.62), Nh2 (+7.35), Nd2 (+6.10).

### 16.Bh6 (inaccuracy, positional, wp loss 10%)

You played 16.Bh6. Stockfish preferred O-O-O, after which the main line runs 16. O-O-O Nb6 17. Nh2 Bd7 18. Qe2 Qe8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: O-O-O (+3.71), Nb5 (+3.53), Nh2 (+3.39).

### 18.Qh6+ (inaccuracy, positional, wp loss 5%)

You played 18.Qh6+. Stockfish preferred O-O-O, after which the main line runs 18. O-O-O Nb6 19. Rxg7 Kxg7 20. Rg1+ Kh7. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: O-O-O (+2.50), Qe2 (+2.28), Rxg7 (+2.22).

### 19.Qg6 (inaccuracy, positional, wp loss 6%)

You played 19.Qg6. Stockfish preferred Qe3, after which the main line runs 19. Qe3 Rb8 20. a4 Nb6 21. O-O-O Qe7. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qe3 (+1.89), Qd2 (+1.66), Qg6 (+1.36).

### 20.Ne2 (inaccuracy, positional, wp loss 8%)

You played 20.Ne2. Stockfish preferred Nh2, after which the main line runs 20. Nh2 Nb6 21. Nb5 Bd7 22. Nc7 Rd8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 16; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nh2 (+1.15), a4 (+1.14), Nb5 (+1.07).

### 23.O-O-O (mistake, positional, wp loss 16%)

You played 23.O-O-O. Stockfish preferred Nd2, after which the main line runs 23. Nd2 Rh6 24. Nc3 Bd7 25. Nc4 Ng6. The evaluation crossed from winning to equal, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nd2 (+2.06), a4 (+1.45), Rg3 (+1.09).

### 24.b3 (mistake, positional, wp loss 14%)

You played 24.b3. Stockfish preferred Nd2, after which the main line runs 24. Nd2 b5 25. Ng3 a3 26. b3 Ng6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nd2 (+1.56), Nh2 (+1.11), Rde1 (+0.73).

### 25.cxb3 (mistake, tactical, wp loss 17%)

You played 25.cxb3. Stockfish preferred axb3, after which the main line runs 25. axb3 Bg4 26. Rg3 f5 27. exf5 e4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on a2 insufficiently defended; a favorable capture was available (cxb3). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: axb3 (-0.03), Nd2 (-1.75), cxb3 (-1.86).

### 26.Ng3 (mistake, tactical, wp loss 10%)

You played 26.Ng3. Stockfish preferred Nd2, after which the main line runs 26. Nd2 b5 27. Rg3 Ra1+ 28. Nb1 b4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on f2 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nd2 (-0.73), Nc3 (-1.70), Ng3 (-1.81).

### 27.Rdf1 (blunder, tactical, wp loss 26%)

You played 27.Rdf1. Stockfish preferred Rd2, after which the main line runs 27. Rd2 Ra1+ 28. Kc2 Rxg1 29. Nxg1 Rg7. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on f3 insufficiently defended; motif: creates threat on a2. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Rd2 (-1.35), Nd2 (-3.84), Rd3 (-4.43).

### 33.Nb5 (inaccuracy, positional, wp loss 5%)

You played 33.Nb5. Stockfish preferred Nc8, after which the main line runs 33. Nc8 Bxb3+ 34. Kc3 Be6 35. Ra8 Kg7. Why it went wrong: left pawn on b3 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nc8 (-6.82), Ra8 (-7.04), Nb5 (-7.83).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.31 | +0.27 | e4 | 4 | 0% | best |
| 2 | 1...c6 | +0.27 | +0.35 | e5 | 8 | 1% | excellent |
| 3 | 2.d4* | +0.35 | +0.22 | Nc3 | 13 | 1% | excellent |
| 4 | 2...d6 | +0.22 | +0.76 | d5 | 54 | 5% | good |
| 5 | 3.Nc3* | +0.76 | +0.63 | c4 | 13 | 1% | excellent |
| 6 | 3...g6 | +0.63 | +0.76 | e5 | 13 | 1% | excellent |
| 7 | 4.Nf3* | +0.76 | +0.71 | h3 | 5 | 0% | excellent |
| 8 | 4...Bg7 | +0.71 | +0.60 | Nf6 | 0 | 0% | excellent |
| 9 | 5.Be3* | +0.60 | +0.51 | h3 | 9 | 1% | excellent |
| 10 | 5...Nd7 | +0.51 | +0.75 | Nf6 | 24 | 2% | good |
| 11 | 6.d5* | +0.75 | +0.13 | Qd2 | 62 | 6% | inaccuracy |
| 12 | 6...c5 | +0.13 | +1.18 | Bxc3+ | 105 | 9% | inaccuracy |
| 13 | 7.Bb5* | +1.18 | +0.17 | a4 | 101 | 9% | inaccuracy |
| 14 | 7...Nf6 | +0.17 | +0.79 | a6 | 62 | 6% | inaccuracy |
| 15 | 8.Bxd7+* | +0.79 | -0.15 | Be2 | 94 | 9% | inaccuracy |
| 16 | 8...Nxd7 | -0.15 | +0.48 | Bxd7 | 63 | 6% | inaccuracy |
| 17 | 9.Bg5* | +0.48 | -0.70 | O-O | 118 | 11% | mistake |
| 18 | 9...f6 | -0.70 | +0.25 | b5 | 95 | 9% | inaccuracy |
| 19 | 10.Be3* | +0.25 | +0.00 | Bc1 | 25 | 2% | good |
| 20 | 10...O-O | +0.00 | +0.09 | b5 | 9 | 1% | excellent |
| 21 | 11.g4* | +0.09 | -1.01 | O-O | 110 | 10% | mistake |
| 22 | 11...e5 | -1.01 | +1.18 | b5 | 219 | 20% | mistake |
| 23 | 12.h4* | +1.18 | +0.91 | Rg1 | 27 | 2% | good |
| 24 | 12...h5 | +0.91 | +2.77 | b5 | 186 | 15% | mistake |
| 25 | 13.gxh5* | +2.77 | +2.95 | gxh5 | 0 | 0% | best |
| 26 | 13...gxh5 | +2.95 | +3.05 | gxh5 | 10 | 1% | best |
| 27 | 14.Rg1* | +3.05 | +3.21 | Rg1 | 0 | 0% | best |
| 28 | 14...Kh8 | +3.21 | +7.62 | Rf7 | 441 | 18% | mistake |
| 29 | 15.Qd2* | +7.62 | +2.26 | Nd4 | 536 | 25% | blunder |
| 30 | 15...a5 | +2.26 | +3.71 | Nb6 | 145 | 10% | inaccuracy |
| 31 | 16.Bh6* | +3.71 | +2.28 | O-O-O | 143 | 10% | inaccuracy |
| 32 | 16...Rf7 | +2.28 | +2.49 | Rf7 | 21 | 2% | best |
| 33 | 17.Bxg7+* | +2.49 | +2.51 | O-O-O | 0 | 0% | excellent |
| 34 | 17...Rxg7 | +2.51 | +2.50 | Rxg7 | 0 | 0% | best |
| 35 | 18.Qh6+* | +2.50 | +1.82 | O-O-O | 68 | 5% | inaccuracy |
| 36 | 18...Rh7 | +1.82 | +1.89 | Rh7 | 7 | 1% | best |
| 37 | 19.Qg6* | +1.89 | +1.21 | Qe3 | 68 | 6% | inaccuracy |
| 38 | 19...Qf8 | +1.21 | +1.15 | Qf8 | 0 | 0% | best |
| 39 | 20.Ne2* | +1.15 | +0.21 | Nh2 | 94 | 8% | inaccuracy |
| 40 | 20...Qg7 | +0.21 | +2.49 | b5 | 228 | 20% | mistake |
| 41 | 21.Qe8+* | +2.49 | +2.02 | Nd2 | 47 | 4% | good |
| 42 | 21...Qf8 | +2.02 | +2.02 | Qf8 | 0 | 0% | best |
| 43 | 22.Qxf8+* | +2.02 | +2.04 | Qxf8+ | 0 | 0% | best |
| 44 | 22...Nxf8 | +2.04 | +2.06 | Nxf8 | 2 | 0% | best |
| 45 | 23.O-O-O* | +2.06 | +0.27 | Nd2 | 179 | 16% | mistake |
| 46 | 23...a4 | +0.27 | +1.56 | Bg4 | 129 | 11% | mistake |
| 47 | 24.b3* | +1.56 | -0.04 | Nd2 | 160 | 14% | mistake |
| 48 | 24...axb3 | -0.04 | -0.03 | Bg4 | 1 | 0% | excellent |
| 49 | 25.cxb3* | -0.03 | -2.01 | axb3 | 198 | 17% | mistake |
| 50 | 25...Rxa2 | -2.01 | -0.73 | Bg4 | 128 | 11% | mistake |
| 51 | 26.Ng3* | -0.73 | -1.91 | Nd2 | 118 | 10% | mistake |
| 52 | 26...Bg4 | -1.91 | -1.35 | Rxf2 | 56 | 5% | good |
| 53 | 27.Rdf1* | -1.35 | -5.49 | Rd2 | 414 | 26% | blunder |
| 54 | 27...Bxf3 | -5.49 | -5.52 | Bxf3 | 0 | 0% | best |
| 55 | 28.Nf5* | -5.52 | -6.13 | Kb1 | 61 | 2% | good |
| 56 | 28...Ra1+ | -6.13 | -5.82 | Bxe4 | 31 | 1% | excellent |
| 57 | 29.Kd2* | -5.82 | -5.93 | Kb2 | 11 | 0% | excellent |
| 58 | 29...Rxf1 | -5.93 | -5.97 | Rxf1 | 0 | 0% | best |
| 59 | 30.Rxf1* | -5.97 | -5.94 | Rxf1 | 0 | 0% | best |
| 60 | 30...Bxe4 | -5.94 | -5.84 | Bxe4 | 10 | 0% | best |
| 61 | 31.Nxd6* | -5.84 | -5.96 | Nxd6 | 12 | 0% | best |
| 62 | 31...Bxd5 | -5.96 | -5.85 | Bxd5 | 11 | 0% | best |
| 63 | 32.Ra1* | -5.85 | -6.64 | Kc3 | 79 | 2% | good |
| 64 | 32...Rd7 | -6.64 | -6.82 | Rd7 | 0 | 0% | best |
| 65 | 33.Nb5* | -6.82 | -11.36 | Nc8 | 454 | 5% | inaccuracy |
| 66 | 33...Bc4+ | -11.36 | -13.18 | Bc4+ | 0 | 0% | best |
| 67 | 34.Kc3* | -13.18 | -32.45 | Kc3 | 1927 | 0% | best |
| 68 | 34...Bxb5 | -32.45 | -16.24 | Bxb5 | 1621 | 0% | best |
| 69 | 35.Ra8* | -16.24 | -32.45 | Ra5 | 1621 | 0% | excellent |
| 70 | 35...Kg8 | -32.45 | -12.26 | Kg7 | 2019 | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 13 positional.
- Opening: 4 error(s) (avg wp loss 9%).
- Middlegame: 11 error(s) (avg wp loss 13%).
- Endgame: 1 error(s) (avg wp loss 5%).
