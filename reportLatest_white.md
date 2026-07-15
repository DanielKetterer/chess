# (free, so lmk) Game analysis: DanielKetterer vs Mirrorwahl

Date: 2026.07.13  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171535977872

## Summary

- Accuracy: you 87.1%, opponent 87.8%
- Opening: not matched in the ECO database
- First deviation from theory: ply 1, You played 1. e4
- Your moves: 13 best, 2 excellent, 5 good, 3 inaccuracy, 3 mistake, 0 blunder

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

You played 19.Rb1. Stockfish preferred Qa4+, after which the main line runs 19. Qa4+ Kf8 20. Qc6 Re8 21. Rae1 Be4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3, pawn on a2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qa4+ (-1.43), Bd4 (-2.47), Bf2 (-2.79).

## Critical positions

- Ply 10 (opponent), 5...bxc6: -0.70 -> -0.73 [only-move situation]
- Ply 17 (you), 9.Nf3: -1.33 -> -1.53 [only-move situation]
- Ply 42 (opponent), 21...f6: -4.27 -> +8.29 [only-move situation; evaluation crossed winning -> losing]
- Ply 43 (you), 22.exf6+: +8.29 -> M8 [only-move situation]
- Ply 45 (you), 23.Qd7+: M4 -> M3 [only-move situation]
- Ply 47 (you), 24.Qxg7+: M3 -> M2 [only-move situation]

## Your errors, move by move

### 2.Bc4 (inaccuracy, positional, wp loss 8%)

You played 2.Bc4. Stockfish preferred d4, after which the main line runs 2. d4 d5 3. e5 Bf5 4. Nc3 e6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d4 (+0.63), c3 (+0.45), Nf3 (+0.39).

### 8.f4 (inaccuracy, positional, wp loss 6%)

You played 8.f4. Stockfish preferred Nf3, after which the main line runs 8. Nf3 e6 9. Ne5 Bd6 10. Bf4 Ne7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nf3 (-1.05), Nh3 (-1.20), Ne2 (-1.22).

### 10.O-O (mistake, tactical, wp loss 13%)

You played 10.O-O. Stockfish preferred g5, after which the main line runs 10. g5 Nd7 11. Nc3 Bg6 12. Nh4 e6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on g4 insufficiently defended; motif: creates threat on f6. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: g5 (-0.51), Rg1 (-0.88), h3 (-1.00).

### 13.c3 (mistake, positional, wp loss 13%)

You played 13.c3. Stockfish preferred Nc3, after which the main line runs 13. Nc3 g6 14. Nxe4 dxe4 15. c3 Bg7. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc3 (-0.75), e6 (-1.58), c4 (-2.00).

### 19.Rb1 (mistake, tactical, wp loss 14%)

You played 19.Rb1. Stockfish preferred Qa4+, after which the main line runs 19. Qa4+ Kf8 20. Qc6 Re8 21. Rae1 Be4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on c3, pawn on a2 insufficiently defended; the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Qa4+ (-1.43), Bd4 (-2.47), Bf2 (-2.79).

### 21.Bg5+ (inaccuracy, positional, wp loss 9%)

You played 21.Bg5+. Stockfish preferred c6, after which the main line runs 21. c6 Bc2 22. Qa5 Kf8 23. Qc7 Bg6. Why it went wrong: left pawn on c3 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: c6 (-2.79), Qc6 (-2.98), Qa6 (-2.99).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.49 | +0.32 | e4 | 17 | 2% | best |
| 2 | 1...c6 | +0.32 | +0.63 | c5 | 31 | 3% | good |
| 3 | 2.Bc4* | +0.63 | -0.21 | d4 | 84 | 8% | inaccuracy |
| 4 | 2...d5 | -0.21 | -0.42 | d5 | 0 | 0% | best |
| 5 | 3.exd5* | -0.42 | -0.37 | exd5 | 0 | 0% | best |
| 6 | 3...cxd5 | -0.37 | -0.24 | cxd5 | 13 | 1% | best |
| 7 | 4.Bb5+* | -0.24 | -0.40 | Bb5+ | 16 | 1% | best |
| 8 | 4...Nc6 | -0.40 | -0.31 | Bd7 | 9 | 1% | excellent |
| 9 | 5.Bxc6+* | -0.31 | -0.70 | Nf3 | 39 | 4% | good |
| 10 | 5...bxc6 | -0.70 | -0.73 | bxc6 | 0 | 0% | best |
| 11 | 6.d4* | -0.73 | -0.78 | d4 | 5 | 0% | best |
| 12 | 6...Bf5 | -0.78 | -0.66 | e6 | 12 | 1% | excellent |
| 13 | 7.g4* | -0.66 | -1.10 | Nf3 | 44 | 4% | good |
| 14 | 7...Bg6 | -1.10 | -1.05 | Bc8 | 5 | 0% | excellent |
| 15 | 8.f4* | -1.05 | -1.69 | Nf3 | 64 | 6% | inaccuracy |
| 16 | 8...Be4 | -1.69 | -1.33 | e6 | 36 | 3% | good |
| 17 | 9.Nf3* | -1.33 | -1.53 | Nf3 | 20 | 2% | best |
| 18 | 9...Nf6 | -1.53 | -0.51 | e6 | 102 | 9% | inaccuracy |
| 19 | 10.O-O* | -0.51 | -2.02 | g5 | 151 | 13% | mistake |
| 20 | 10...Nxg4 | -2.02 | -2.02 | Nxg4 | 0 | 0% | best |
| 21 | 11.Ne5* | -2.02 | -2.42 | c4 | 40 | 3% | good |
| 22 | 11...Nxe5 | -2.42 | -2.42 | Nxe5 | 0 | 0% | best |
| 23 | 12.fxe5* | -2.42 | -2.42 | fxe5 | 0 | 0% | best |
| 24 | 12...Qb6 | -2.42 | -0.75 | e6 | 167 | 14% | mistake |
| 25 | 13.c3* | -0.75 | -2.32 | Nc3 | 157 | 13% | mistake |
| 26 | 13...e6 | -2.32 | -2.31 | e6 | 1 | 0% | best |
| 27 | 14.Nd2* | -2.31 | -2.41 | Rf2 | 10 | 1% | excellent |
| 28 | 14...Bg6 | -2.41 | -2.29 | Bf5 | 12 | 1% | excellent |
| 29 | 15.Nb3* | -2.29 | -2.76 | Rf2 | 47 | 4% | good |
| 30 | 15...c5 | -2.76 | -1.58 | a5 | 118 | 9% | inaccuracy |
| 31 | 16.Be3* | -1.58 | -1.68 | Be3 | 10 | 1% | best |
| 32 | 16...c4 | -1.68 | -1.47 | cxd4 | 21 | 2% | excellent |
| 33 | 17.Nc5* | -1.47 | -1.41 | Nc5 | 0 | 0% | best |
| 34 | 17...Bxc5 | -1.41 | -1.36 | Qa5 | 5 | 0% | excellent |
| 35 | 18.dxc5* | -1.36 | -1.61 | Qa4+ | 25 | 2% | good |
| 36 | 18...Qxb2 | -1.61 | -1.43 | Qxb2 | 18 | 2% | best |
| 37 | 19.Rb1* | -1.43 | -3.28 | Qa4+ | 185 | 14% | mistake |
| 38 | 19...Bxb1 | -3.28 | -2.92 | Qxc3 | 36 | 2% | good |
| 39 | 20.Qa4+* | -2.92 | -3.42 | Qa4+ | 50 | 3% | best |
| 40 | 20...Ke7 | -3.42 | -2.79 | Kf8 | 63 | 4% | good |
| 41 | 21.Bg5+* | -2.79 | -4.27 | c6 | 148 | 9% | inaccuracy |
| 42 | 21...f6 | -4.27 | +8.29 | Kf8 | 1256 | 78% | blunder |
| 43 | 22.exf6+* | +8.29 | M8 | exf6+ |  | 0% | best |
| 44 | 22...Kf7 | M8 | M4 | gxf6 |  | 0% | excellent |
| 45 | 23.Qd7+* | M4 | M3 | Qd7+ |  | 0% | best |
| 46 | 23...Kg6 | M3 | M3 | Kg6 |  | 0% | best |
| 47 | 24.Qxg7+* | M3 | M2 | Qxg7+ |  | 0% | best |
| 48 | 24...Kh5 | M2 | M2 | Kh5 |  | 0% | best |
| 49 | 25.Qh6+* | M2 | M1 | Qh6+ |  | 0% | best |
| 50 | 25...Kg4 | M1 | M1 | Kg4 |  | 0% | best |
| 51 | 26.Rf4#* | M1 | M1 | Qh4# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 2 tactical, 4 positional.
- Opening: 3 error(s) (avg wp loss 9%).
- Middlegame: 3 error(s) (avg wp loss 12%).
