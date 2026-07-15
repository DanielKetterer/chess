# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 86.0%, opponent 85.9%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, Opponent played 2... d5
- Your moves: 13 best, 4 excellent, 1 good, 4 inaccuracy, 3 mistake, 1 blunder

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

You played 21.Bg5+. Stockfish preferred Rxf7+, after which the main line runs 21. Rxf7+ Kxf7 22. Qd7+ Kf8 23. Qd6+ Kf7. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Rxf7+ (+0.00), c6 (-2.96), Qc6 (-4.39).

## Critical positions

- Ply 10 (opponent), 5...bxc6: -0.73 -> -0.71 [only-move situation]
- Ply 17 (you), 9.Nf3: -1.16 -> -1.22 [only-move situation]
- Ply 38 (opponent), 19...Bxb1: -3.24 -> +0.00 [evaluation crossed winning -> equal]
- Ply 39 (you), 20.Qa4+: +0.00 -> +0.00 [only-move situation]
- Ply 41 (you), 21.Bg5+: +0.00 -> -4.85 [only-move situation; evaluation crossed equal -> losing]
- Ply 42 (opponent), 21...f6: -4.85 -> M7 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (you), 22.exf6+: M7 -> M6 [only-move situation]
- Ply 45 (you), 23.Qd7+: M4 -> M3 [only-move situation]

## Your errors, move by move

### 2.Bc4 (inaccuracy, positional, wp loss 8%)

You played 2.Bc4. Stockfish preferred d4, after which the main line runs 2. d4 d5 3. e5 Bf5 4. Nf3 e6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d4 (+0.43), Nf3 (+0.38), Nc3 (+0.29).

### 7.g4 (inaccuracy, positional, wp loss 5%)

You played 7.g4. Stockfish preferred c4, after which the main line runs 7. c4 dxc4 8. Qa4 Rc8 9. Nf3 Bd3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine does not prefer this move until depth 14; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: c4 (-0.57), Nf3 (-0.70), Ne2 (-0.71).

### 8.f4 (inaccuracy, positional, wp loss 7%)

You played 8.f4. Stockfish preferred Nf3, after which the main line runs 8. Nf3 e6 9. Ne5 Bd6 10. Bf4 Bxe5. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nf3 (-1.11), Ne2 (-1.22), Nh3 (-1.37).

### 10.O-O (mistake, tactical, wp loss 13%)

You played 10.O-O. Stockfish preferred g5, after which the main line runs 10. g5 Nd7 11. Nc3 Bg6 12. Nh4 e6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on g4 insufficiently defended; motif: creates threat on f6. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: g5 (-0.82), Nc3 (-0.91), Nbd2 (-0.99).

### 13.c3 (mistake, positional, wp loss 17%)

You played 13.c3. Stockfish preferred Nc3, after which the main line runs 13. Nc3 g6 14. Nxe4 dxe4 15. c3 Bg7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc3 (-0.26), e6 (-0.94), c4 (-1.95).

### 15.Nb3 (inaccuracy, positional, wp loss 6%)

You played 15.Nb3. Stockfish preferred h4, after which the main line runs 15. h4 Qd8 16. Qg4 Be7 17. h5 Bf5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: h4 (-1.95), Rf2 (-2.12), Qg4 (-2.26).

### 19.Rb1 (mistake, tactical, wp loss 12%)

You played 19.Rb1. Stockfish preferred Qa4+, after which the main line runs 19. Qa4+ Kf8 20. Qc6 Rd8 21. Qc7 Qb8. Why it went wrong: left pawn on c3, pawn on a2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qa4+ (-1.70), Bd4 (-2.54), Qe1 (-2.96).

### 21.Bg5+ (blunder, tactical, wp loss 36%)

You played 21.Bg5+. Stockfish preferred Rxf7+, after which the main line runs 21. Rxf7+ Kxf7 22. Qd7+ Kf8 23. Qd6+ Kf7. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Rxf7+ (+0.00), c6 (-2.96), Qc6 (-4.39).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.40 | +0.36 | e4 | 4 | 0% | best |
| 2 | 1...c6 | +0.36 | +0.43 | e5 | 7 | 1% | excellent |
| 3 | 2.Bc4* | +0.43 | -0.45 | d4 | 88 | 8% | inaccuracy |
| 4 | 2...d5 | -0.45 | -0.34 | d5 | 11 | 1% | best |
| 5 | 3.exd5* | -0.34 | -0.41 | exd5 | 7 | 1% | best |
| 6 | 3...cxd5 | -0.41 | -0.30 | cxd5 | 11 | 1% | best |
| 7 | 4.Bb5+* | -0.30 | -0.38 | Bb5+ | 8 | 1% | best |
| 8 | 4...Nc6 | -0.38 | -0.22 | Bd7 | 16 | 1% | excellent |
| 9 | 5.Bxc6+* | -0.22 | -0.73 | Nf3 | 51 | 5% | good |
| 10 | 5...bxc6 | -0.73 | -0.71 | bxc6 | 2 | 0% | best |
| 11 | 6.d4* | -0.71 | -0.76 | Nf3 | 5 | 0% | excellent |
| 12 | 6...Bf5 | -0.76 | -0.57 | Ba6 | 19 | 2% | excellent |
| 13 | 7.g4* | -0.57 | -1.14 | c4 | 57 | 5% | inaccuracy |
| 14 | 7...Bg6 | -1.14 | -1.11 | Bg6 | 3 | 0% | best |
| 15 | 8.f4* | -1.11 | -1.95 | Nf3 | 84 | 7% | inaccuracy |
| 16 | 8...Be4 | -1.95 | -1.16 | e6 | 79 | 7% | inaccuracy |
| 17 | 9.Nf3* | -1.16 | -1.22 | Nf3 | 6 | 1% | best |
| 18 | 9...Nf6 | -1.22 | -0.82 | Qc8 | 40 | 4% | good |
| 19 | 10.O-O* | -0.82 | -2.41 | g5 | 159 | 13% | mistake |
| 20 | 10...Nxg4 | -2.41 | -2.33 | Nxg4 | 8 | 1% | best |
| 21 | 11.Ne5* | -2.33 | -2.42 | Nc3 | 9 | 1% | excellent |
| 22 | 11...Nxe5 | -2.42 | -2.56 | Nxe5 | 0 | 0% | best |
| 23 | 12.fxe5* | -2.56 | -2.43 | fxe5 | 0 | 0% | best |
| 24 | 12...Qb6 | -2.43 | -0.26 | e6 | 217 | 19% | mistake |
| 25 | 13.c3* | -0.26 | -2.24 | Nc3 | 198 | 17% | mistake |
| 26 | 13...e6 | -2.24 | -2.11 | e6 | 13 | 1% | best |
| 27 | 14.Nd2* | -2.11 | -2.06 | Nd2 | 0 | 0% | best |
| 28 | 14...Bg6 | -2.06 | -1.95 | Bg6 | 11 | 1% | best |
| 29 | 15.Nb3* | -1.95 | -2.75 | h4 | 80 | 6% | inaccuracy |
| 30 | 15...c5 | -2.75 | -1.59 | a5 | 116 | 9% | inaccuracy |
| 31 | 16.Be3* | -1.59 | -1.61 | Be3 | 2 | 0% | best |
| 32 | 16...c4 | -1.61 | -1.39 | cxd4 | 22 | 2% | excellent |
| 33 | 17.Nc5* | -1.39 | -1.45 | Nc5 | 6 | 1% | best |
| 34 | 17...Bxc5 | -1.45 | -1.72 | Bxc5 | 0 | 0% | best |
| 35 | 18.dxc5* | -1.72 | -1.76 | Qa4+ | 4 | 0% | excellent |
| 36 | 18...Qxb2 | -1.76 | -1.70 | Qxb2 | 6 | 0% | best |
| 37 | 19.Rb1* | -1.70 | -3.24 | Qa4+ | 154 | 12% | mistake |
| 38 | 19...Bxb1 | -3.24 | +0.00 | Qxa2 | 324 | 27% | blunder |
| 39 | 20.Qa4+* | +0.00 | +0.00 | Qa4+ | 0 | 0% | best |
| 40 | 20...Ke7 | +0.00 | +0.00 | Ke7 | 0 | 0% | best |
| 41 | 21.Bg5+* | +0.00 | -4.85 | Rxf7+ | 485 | 36% | blunder |
| 42 | 21...f6 | -4.85 | M7 | Kf8 |  | 86% | blunder |
| 43 | 22.exf6+* | M7 | M6 | exf6+ |  | 0% | best |
| 44 | 22...Kf7 | M6 | M4 | gxf6 |  | 0% | excellent |
| 45 | 23.Qd7+* | M4 | M3 | Qd7+ |  | 0% | best |
| 46 | 23...Kg6 | M3 | M3 | Kg6 |  | 0% | best |
| 47 | 24.Qxg7+* | M3 | M2 | Qxg7+ |  | 0% | best |
| 48 | 24...Kh5 | M2 | M2 | Kh5 |  | 0% | best |
| 49 | 25.Qh6+* | M2 | M1 | Qh6+ |  | 0% | best |
| 50 | 25...Kg4 | M1 | M1 | Kg4 |  | 0% | best |
| 51 | 26.Rf4#* | M1 | M1 | Qh4# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 5 positional.
- Opening: 4 error(s) (avg wp loss 8%).
- Middlegame: 4 error(s) (avg wp loss 18%).
