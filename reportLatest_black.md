# (free, so lmk) Game analysis: amrsalama22 vs DanielKetterer

Date: 2026.07.16  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171665538456

## Summary

- Lichess accuracy: you 90.3%, opponent 81.2%
- Opening: C44 Scotch Game (theory followed through ply 5)
- First deviation from theory: ply 6, You played 3... d6
- Your moves: 16 best, 7 excellent, 4 good, 5 inaccuracy, 1 mistake, 0 blunder

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

You played 9...Nf6. Stockfish preferred h6, after which the main line runs 9...h6 10. Be3 Nf6 11. Nxf6+ Qxf6 12. c3. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: h6 (+1.27), Nce7 (+1.40), Bg7 (+1.55).

## Critical positions

- Ply 21 (opponent), 11.h3: +3.14 -> -0.02 [only-move situation; evaluation crossed winning -> equal]
- Ply 24 (you), 12...Bxf6: +0.83 -> +0.85 [only-move situation]
- Ply 26 (you), 13...Qxf6: +0.82 -> +0.78 [only-move situation]
- Ply 33 (opponent), 17.Bxa6: +0.53 -> -1.70 [evaluation crossed equal -> losing]
- Ply 34 (you), 17...bxa6: -1.70 -> -1.78 [only-move situation]
- Ply 36 (you), 18...Kc7: -1.74 -> -1.62 [only-move situation; evaluation crossed winning -> equal]
- Ply 42 (you), 21...Nc6: -3.25 -> -3.20 [only-move situation]
- Ply 51 (opponent), 26.Rd1: -3.09 -> -12.58

## Your errors, move by move

### 3...d6 (inaccuracy, positional, wp loss 7%)

You played 3...d6. Stockfish preferred exd4, after which the main line runs 3...exd4 4. Nxd4 Nf6 5. Nxc6 bxc6 6. Bd3. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: exd4 (+0.09), Nxd4 (+0.61), d6 (+0.73).

### 8...g6 (inaccuracy, positional, wp loss 7%)

You played 8...g6. Stockfish preferred h6, after which the main line runs 8...h6 9. Re1 Nf6 10. Bf1 Be7 11. Nd5. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: h6 (+0.58), a6 (+0.77), Rc8 (+0.80).

### 9...Nf6 (mistake, positional, wp loss 12%)

You played 9...Nf6. Stockfish preferred h6, after which the main line runs 9...h6 10. Be3 Nf6 11. Nxf6+ Qxf6 12. c3. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: h6 (+1.27), Nce7 (+1.40), Bg7 (+1.55).

### 11...h6 (inaccuracy, positional, wp loss 9%)

You played 11...h6. Stockfish preferred Nxd5, after which the main line runs 11...Nxd5 12. exd5 Bxg5 13. Nxg5 Qxg5 14. dxc6. Why it went wrong: a favorable capture was available (Nxe4). This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nxd5 (-0.02), h6 (+0.86), Nxe4 (+0.97).

### 15...Qe6 (inaccuracy, positional, wp loss 7%)

You played 15...Qe6. Stockfish preferred g5, after which the main line runs 15...g5 16. Nh2 h5 17. f3 Kb8 18. Bxc6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: g5 (-0.36), Kb8 (-0.06), h5 (+0.00).

### 24...Kd8 (inaccuracy, positional, wp loss 7%)

You played 24...Kd8. Stockfish preferred Rhb8, after which the main line runs 24...Rhb8 25. Nb3 Ra4 26. Qd2 g5 27. Rd1. Why it went wrong: left pawn on e4 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 6; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Rhb8 (-3.96), d5 (-3.68), Qd5 (-3.58).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.38 | +0.24 | d4 | 14 | 1% | excellent |
| 2 | 1...e5* | +0.24 | +0.30 | e5 | 6 | 1% | best |
| 3 | 2.Nf3 | +0.30 | +0.24 | Nf3 | 6 | 1% | best |
| 4 | 2...Nc6* | +0.24 | +0.27 | Nc6 | 3 | 0% | best |
| 5 | 3.d4 | +0.27 | +0.09 | Bb5 | 18 | 2% | excellent |
| 6 | 3...d6* | +0.09 | +0.81 | exd4 | 72 | 7% | inaccuracy |
| 7 | 4.d5 | +0.81 | +0.73 | d5 | 8 | 1% | best |
| 8 | 4...Nce7* | +0.73 | +0.74 | Nce7 | 1 | 0% | best |
| 9 | 5.Nc3 | +0.74 | +0.43 | c4 | 31 | 3% | good |
| 10 | 5...c6* | +0.43 | +0.71 | g6 | 28 | 3% | good |
| 11 | 6.dxc6 | +0.71 | +0.68 | Bc4 | 3 | 0% | excellent |
| 12 | 6...Nxc6* | +0.68 | +0.53 | Nxc6 | 0 | 0% | best |
| 13 | 7.Bb5 | +0.53 | +0.40 | Bg5 | 13 | 1% | excellent |
| 14 | 7...Bd7* | +0.40 | +0.84 | h6 | 44 | 4% | good |
| 15 | 8.O-O | +0.84 | +0.58 | Bg5 | 26 | 2% | good |
| 16 | 8...g6* | +0.58 | +1.39 | h6 | 81 | 7% | inaccuracy |
| 17 | 9.Nd5 | +1.39 | +1.27 | Bg5 | 12 | 1% | excellent |
| 18 | 9...Nf6* | +1.27 | +2.80 | h6 | 153 | 12% | mistake |
| 19 | 10.Bg5 | +2.80 | +2.87 | Bg5 | 0 | 0% | best |
| 20 | 10...Be7* | +2.87 | +3.14 | Bg7 | 27 | 2% | excellent |
| 21 | 11.h3 | +3.14 | -0.02 | Nxf6+ | 316 | 26% | blunder |
| 22 | 11...h6* | -0.02 | +0.93 | Nxd5 | 95 | 9% | inaccuracy |
| 23 | 12.Bxf6 | +0.93 | +0.83 | Bxf6 | 10 | 1% | best |
| 24 | 12...Bxf6* | +0.83 | +0.85 | Bxf6 | 2 | 0% | best |
| 25 | 13.Nxf6+ | +0.85 | +0.82 | c3 | 3 | 0% | excellent |
| 26 | 13...Qxf6* | +0.82 | +0.78 | Qxf6 | 0 | 0% | best |
| 27 | 14.Qe2 | +0.78 | +0.38 | Qd3 | 40 | 4% | good |
| 28 | 14...O-O-O* | +0.38 | +0.92 | g5 | 54 | 5% | good |
| 29 | 15.Qc4 | +0.92 | -0.36 | a4 | 128 | 12% | mistake |
| 30 | 15...Qe6* | -0.36 | +0.35 | g5 | 71 | 7% | inaccuracy |
| 31 | 16.Qa4 | +0.35 | +0.00 | Qc3 | 35 | 3% | good |
| 32 | 16...a6* | +0.00 | +0.53 | g5 | 53 | 5% | good |
| 33 | 17.Bxa6 | +0.53 | -1.70 | Bc4 | 223 | 20% | blunder |
| 34 | 17...bxa6* | -1.70 | -1.78 | bxa6 | 0 | 0% | best |
| 35 | 18.Qxa6+ | -1.78 | -1.74 | Qxa6+ | 0 | 0% | best |
| 36 | 18...Kc7* | -1.74 | -1.62 | Kc7 | 12 | 1% | best |
| 37 | 19.b4 | -1.62 | -3.21 | Nd2 | 159 | 12% | mistake |
| 38 | 19...Ra8* | -3.21 | -3.12 | Ra8 | 9 | 1% | best |
| 39 | 20.Qd3 | -3.12 | -3.20 | Qd3 | 8 | 1% | best |
| 40 | 20...Nxb4* | -3.20 | -3.33 | Nxb4 | 0 | 0% | best |
| 41 | 21.Qc3+ | -3.33 | -3.25 | Qc3+ | 0 | 0% | best |
| 42 | 21...Nc6* | -3.25 | -3.20 | Nc6 | 5 | 0% | best |
| 43 | 22.Rab1 | -3.20 | -3.67 | Rfd1 | 47 | 3% | good |
| 44 | 22...f5* | -3.67 | -3.42 | Rhb8 | 25 | 2% | excellent |
| 45 | 23.Rb2 | -3.42 | -4.06 | Nd2 | 64 | 4% | good |
| 46 | 23...fxe4* | -4.06 | -3.80 | Rhb8 | 26 | 1% | excellent |
| 47 | 24.Nd2 | -3.80 | -3.96 | Nd2 | 16 | 1% | best |
| 48 | 24...Kd8* | -3.96 | -2.79 | Rhb8 | 117 | 7% | inaccuracy |
| 49 | 25.Nc4 | -2.79 | -3.22 | Re1 | 43 | 3% | good |
| 50 | 25...Nd4* | -3.22 | -3.09 | Ke7 | 13 | 1% | excellent |
| 51 | 26.Rd1 | -3.09 | -12.58 | Re1 | 949 | 22% | blunder |
| 52 | 26...Ne2+* | -12.58 | -12.90 | Ne2+ | 0 | 0% | best |
| 53 | 27.Kf1 | -12.90 | -21.51 | Kh2 | 861 | 0% | excellent |
| 54 | 27...Nxc3* | -21.51 | -19.10 | Nxc3 | 241 | 0% | best |
| 55 | 28.Rxd6 | -19.10 | -M18 | Rxd6 |  | 0% | best |
| 56 | 28...Qxc4+* | -M18 | -M17 | Qxc4+ |  | 0% | best |
| 57 | 29.Kg1 | -M17 | -M12 | Kg1 |  | 0% | best |
| 58 | 29...Ne2+* | -M12 | -M10 | Qc5 |  | 0% | excellent |
| 59 | 30.Kh2 | -M10 | -M10 | Kh2 |  | 0% | best |
| 60 | 30...e3* | -M10 | -M9 | Qf7 |  | 0% | excellent |
| 61 | 31.Rb7 | -M9 | -M9 | Rf6 |  | 0% | excellent |
| 62 | 31...Qf4+* | -M9 | -M8 | Qf4+ |  | 0% | best |
| 63 | 32.g3 | -M8 | -M2 | Kh1 |  | 0% | excellent |
| 64 | 32...Qxf2+* | -M2 | -M1 | Qxf2+ |  | 0% | best |
| 65 | 33.Kh1 | -M1 | -M1 | Kh1 |  | 0% | best |
| 66 | 33...Qg1#* | -M1 | -M1 | Nxg3# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 0 tactical, 6 positional.
- Opening: 3 error(s) (avg wp loss 9%).
- Middlegame: 3 error(s) (avg wp loss 8%).
