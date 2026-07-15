# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 85.6%, opponent 85.5%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, Opponent played 2... d5
- Your moves: 12 best, 4 excellent, 3 good, 3 inaccuracy, 3 mistake, 1 blunder

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

You played 21.Bg5+. Stockfish preferred Rxf7+, after which the main line runs 21. Rxf7+ Kxf7 22. Qd7+ Kf8 23. Qd6+ Kg8. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 15; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rxf7+ (+0.00), c6 (-3.89), Qc6 (-4.51).

## Critical positions

- Ply 10 (opponent), 5...bxc6: -0.70 -> -0.60 [only-move situation]
- Ply 17 (you), 9.Nf3: -1.26 -> -1.28 [only-move situation]
- Ply 38 (opponent), 19...Bxb1: -3.08 -> +0.00 [evaluation crossed winning -> equal]
- Ply 39 (you), 20.Qa4+: +0.00 -> +0.00 [only-move situation]
- Ply 41 (you), 21.Bg5+: +0.00 -> -4.68 [only-move situation; evaluation crossed equal -> losing]
- Ply 42 (opponent), 21...f6: -4.68 -> M7 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (you), 22.exf6+: M7 -> M6 [only-move situation]
- Ply 45 (you), 23.Qd7+: M4 -> M3 [only-move situation]

## Your errors, move by move

### 2.Bc4 (inaccuracy, positional, wp loss 8%)

You played 2.Bc4. Stockfish preferred Nf3, after which the main line runs 2. Nf3 d5 3. Nc3 dxe4 4. Nxe4 Nf6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nf3 (+0.42), Nc3 (+0.35), d4 (+0.32).

### 7.g4 (inaccuracy, positional, wp loss 7%)

You played 7.g4. Stockfish preferred c4, after which the main line runs 7. c4 dxc4 8. Nf3 Bd3 9. Qa4 Rc8. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: c4 (-0.47), Ne2 (-0.70), Nf3 (-0.78).

### 8.f4 (inaccuracy, positional, wp loss 8%)

You played 8.f4. Stockfish preferred Nf3, after which the main line runs 8. Nf3 h5 9. Ne5 Be4 10. f3 Bh7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nf3 (-1.09), Ne2 (-1.16), Nc3 (-1.36).

### 10.O-O (mistake, tactical, wp loss 15%)

You played 10.O-O. Stockfish preferred g5, after which the main line runs 10. g5 Nd7 11. Nc3 Bg6 12. Ne2 e6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on g4 insufficiently defended; motif: creates threat on f6. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: g5 (-0.72), Nbd2 (-0.96), Nc3 (-1.14).

### 13.c3 (mistake, positional, wp loss 16%)

You played 13.c3. Stockfish preferred Nc3, after which the main line runs 13. Nc3 g6 14. Nxe4 dxe4 15. c3 Bg7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc3 (-0.35), e6 (-0.78), c4 (-1.84).

### 19.Rb1 (mistake, tactical, wp loss 11%)

You played 19.Rb1. Stockfish preferred Qa4+, after which the main line runs 19. Qa4+ Kf8 20. Qc6 Rd8 21. Qc7 Qb8. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3, pawn on a2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qa4+ (-1.67), Bd4 (-2.56), Rf4 (-2.88).

### 21.Bg5+ (blunder, tactical, wp loss 35%)

You played 21.Bg5+. Stockfish preferred Rxf7+, after which the main line runs 21. Rxf7+ Kxf7 22. Qd7+ Kf8 23. Qd6+ Kg8. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 15; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rxf7+ (+0.00), c6 (-3.89), Qc6 (-4.51).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.28 | +0.31 | d4 | 0 | 0% | excellent |
| 2 | 1...c6 | +0.31 | +0.42 | c6 | 11 | 1% | best |
| 3 | 2.Bc4* | +0.42 | -0.40 | Nf3 | 82 | 8% | inaccuracy |
| 4 | 2...d5 | -0.40 | -0.37 | d5 | 3 | 0% | best |
| 5 | 3.exd5* | -0.37 | -0.36 | exd5 | 0 | 0% | best |
| 6 | 3...cxd5 | -0.36 | -0.29 | cxd5 | 7 | 1% | best |
| 7 | 4.Bb5+* | -0.29 | -0.34 | Bb3 | 5 | 0% | excellent |
| 8 | 4...Nc6 | -0.34 | -0.29 | Nc6 | 5 | 0% | best |
| 9 | 5.Bxc6+* | -0.29 | -0.70 | d4 | 41 | 4% | good |
| 10 | 5...bxc6 | -0.70 | -0.60 | bxc6 | 10 | 1% | best |
| 11 | 6.d4* | -0.60 | -0.79 | Nf3 | 19 | 2% | excellent |
| 12 | 6...Bf5 | -0.79 | -0.47 | Ba6 | 32 | 3% | good |
| 13 | 7.g4* | -0.47 | -1.24 | c4 | 77 | 7% | inaccuracy |
| 14 | 7...Bg6 | -1.24 | -1.09 | Bg6 | 15 | 1% | best |
| 15 | 8.f4* | -1.09 | -1.98 | Nf3 | 89 | 8% | inaccuracy |
| 16 | 8...Be4 | -1.98 | -1.26 | e6 | 72 | 6% | inaccuracy |
| 17 | 9.Nf3* | -1.26 | -1.28 | Nf3 | 2 | 0% | best |
| 18 | 9...Nf6 | -1.28 | -0.72 | e6 | 56 | 5% | good |
| 19 | 10.O-O* | -0.72 | -2.47 | g5 | 175 | 15% | mistake |
| 20 | 10...Nxg4 | -2.47 | -2.28 | Nxg4 | 19 | 1% | best |
| 21 | 11.Ne5* | -2.28 | -2.57 | Nc3 | 29 | 2% | good |
| 22 | 11...Nxe5 | -2.57 | -2.46 | Nxe5 | 11 | 1% | best |
| 23 | 12.fxe5* | -2.46 | -2.53 | fxe5 | 7 | 1% | best |
| 24 | 12...Qb6 | -2.53 | -0.35 | e6 | 218 | 19% | mistake |
| 25 | 13.c3* | -0.35 | -2.25 | Nc3 | 190 | 16% | mistake |
| 26 | 13...e6 | -2.25 | -2.03 | e6 | 22 | 2% | best |
| 27 | 14.Nd2* | -2.03 | -2.21 | Nd2 | 18 | 1% | best |
| 28 | 14...Bg6 | -2.21 | -2.05 | Bf5 | 16 | 1% | excellent |
| 29 | 15.Nb3* | -2.05 | -2.67 | h4 | 62 | 5% | good |
| 30 | 15...c5 | -2.67 | -1.67 | a5 | 100 | 8% | inaccuracy |
| 31 | 16.Be3* | -1.67 | -1.65 | Be3 | 0 | 0% | best |
| 32 | 16...c4 | -1.65 | -1.60 | cxd4 | 5 | 0% | excellent |
| 33 | 17.Nc5* | -1.60 | -1.58 | Nc5 | 0 | 0% | best |
| 34 | 17...Bxc5 | -1.58 | -1.44 | Bxc5 | 14 | 1% | best |
| 35 | 18.dxc5* | -1.44 | -1.64 | dxc5 | 20 | 2% | best |
| 36 | 18...Qxb2 | -1.64 | -1.67 | Qxb2 | 0 | 0% | best |
| 37 | 19.Rb1* | -1.67 | -3.08 | Qa4+ | 141 | 11% | mistake |
| 38 | 19...Bxb1 | -3.08 | +0.00 | Qxa2 | 308 | 26% | blunder |
| 39 | 20.Qa4+* | +0.00 | +0.00 | Qa4+ | 0 | 0% | best |
| 40 | 20...Ke7 | +0.00 | +0.00 | Ke7 | 0 | 0% | best |
| 41 | 21.Bg5+* | +0.00 | -4.68 | Rxf7+ | 468 | 35% | blunder |
| 42 | 21...f6 | -4.68 | M7 | Kf8 |  | 85% | blunder |
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

- Error mix: 3 tactical, 4 positional.
- Opening: 4 error(s) (avg wp loss 9%).
- Middlegame: 3 error(s) (avg wp loss 21%).
