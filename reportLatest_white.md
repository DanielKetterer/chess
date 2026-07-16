# (free, so lmk) Game analysis: amrsalama22 vs DanielKetterer

Date: 2026.07.16  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171665538456

## Summary

- Lichess accuracy: you 81.2%, opponent 90.3%
- Opening: C44 Scotch Game (theory followed through ply 5)
- First deviation from theory: ply 6, Opponent played 3... d6
- Your moves: 12 best, 9 excellent, 7 good, 0 inaccuracy, 2 mistake, 3 blunder

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

You played 11.h3. Stockfish preferred Nxf6+, after which the main line runs 11. Nxf6+ Bxf6 12. Qxd6 Be7 13. Bxe7 Qxe7. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left pawn on e4 insufficiently defended; the best move was a forcing check; motif: fork. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 12; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nxf6+ (+3.14), Bh6 (+1.00), Nxe7 (+0.93).

## Critical positions

- Ply 21 (you), 11.h3: +3.14 -> -0.02 [only-move situation; evaluation crossed winning -> equal]
- Ply 24 (opponent), 12...Bxf6: +0.83 -> +0.85 [only-move situation]
- Ply 26 (opponent), 13...Qxf6: +0.82 -> +0.78 [only-move situation]
- Ply 33 (you), 17.Bxa6: +0.53 -> -1.70 [evaluation crossed equal -> losing]
- Ply 34 (opponent), 17...bxa6: -1.70 -> -1.78 [only-move situation]
- Ply 36 (opponent), 18...Kc7: -1.74 -> -1.62 [only-move situation; evaluation crossed winning -> equal]
- Ply 42 (opponent), 21...Nc6: -3.25 -> -3.20 [only-move situation]
- Ply 51 (you), 26.Rd1: -3.09 -> -12.58

## Your errors, move by move

### 11.h3 (blunder, tactical, wp loss 26%)

You played 11.h3. Stockfish preferred Nxf6+, after which the main line runs 11. Nxf6+ Bxf6 12. Qxd6 Be7 13. Bxe7 Qxe7. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left pawn on e4 insufficiently defended; the best move was a forcing check; motif: fork. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 12; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nxf6+ (+3.14), Bh6 (+1.00), Nxe7 (+0.93).

### 15.Qc4 (mistake, positional, wp loss 12%)

You played 15.Qc4. Stockfish preferred a4, after which the main line runs 15. a4 g5 16. a5 Kb8 17. a6 b6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: a4 (+0.92), Rfd1 (+0.57), Rad1 (+0.55).

### 17.Bxa6 (blunder, tactical, wp loss 20%)

You played 17.Bxa6. Stockfish preferred Bc4, after which the main line runs 17. Bc4 Qf6 18. Qa3 g5 19. Rad1 Kc7. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left bishop on a6 insufficiently defended; motif: creates threat on e6. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bc4 (+0.53), Be2 (-0.04), Bd3 (-0.29).

### 19.b4 (mistake, tactical, wp loss 12%)

You played 19.b4. Stockfish preferred Nd2, after which the main line runs 19. Nd2 Ra8 20. Qd3 Rhb8 21. b3 Nd4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on b4 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 31; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Nd2 (-1.62), c3 (-1.67), a4 (-1.81).

### 26.Rd1 (blunder, positional, wp loss 22%)

You played 26.Rd1. Stockfish preferred Re1, after which the main line runs 26. Re1 Ke7 27. Nb6 Bc6 28. Nxa8 Rxa8. Why it went wrong: motif: creates threat on e4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 8; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Re1 (-3.09), Qb4 (-3.41), Kh2 (-4.38).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.38 | +0.24 | d4 | 14 | 1% | excellent |
| 2 | 1...e5 | +0.24 | +0.30 | e5 | 6 | 1% | best |
| 3 | 2.Nf3* | +0.30 | +0.24 | Nf3 | 6 | 1% | best |
| 4 | 2...Nc6 | +0.24 | +0.27 | Nc6 | 3 | 0% | best |
| 5 | 3.d4* | +0.27 | +0.09 | Bb5 | 18 | 2% | excellent |
| 6 | 3...d6 | +0.09 | +0.81 | exd4 | 72 | 7% | inaccuracy |
| 7 | 4.d5* | +0.81 | +0.73 | d5 | 8 | 1% | best |
| 8 | 4...Nce7 | +0.73 | +0.74 | Nce7 | 1 | 0% | best |
| 9 | 5.Nc3* | +0.74 | +0.43 | c4 | 31 | 3% | good |
| 10 | 5...c6 | +0.43 | +0.71 | g6 | 28 | 3% | good |
| 11 | 6.dxc6* | +0.71 | +0.68 | Bc4 | 3 | 0% | excellent |
| 12 | 6...Nxc6 | +0.68 | +0.53 | Nxc6 | 0 | 0% | best |
| 13 | 7.Bb5* | +0.53 | +0.40 | Bg5 | 13 | 1% | excellent |
| 14 | 7...Bd7 | +0.40 | +0.84 | h6 | 44 | 4% | good |
| 15 | 8.O-O* | +0.84 | +0.58 | Bg5 | 26 | 2% | good |
| 16 | 8...g6 | +0.58 | +1.39 | h6 | 81 | 7% | inaccuracy |
| 17 | 9.Nd5* | +1.39 | +1.27 | Bg5 | 12 | 1% | excellent |
| 18 | 9...Nf6 | +1.27 | +2.80 | h6 | 153 | 12% | mistake |
| 19 | 10.Bg5* | +2.80 | +2.87 | Bg5 | 0 | 0% | best |
| 20 | 10...Be7 | +2.87 | +3.14 | Bg7 | 27 | 2% | excellent |
| 21 | 11.h3* | +3.14 | -0.02 | Nxf6+ | 316 | 26% | blunder |
| 22 | 11...h6 | -0.02 | +0.93 | Nxd5 | 95 | 9% | inaccuracy |
| 23 | 12.Bxf6* | +0.93 | +0.83 | Bxf6 | 10 | 1% | best |
| 24 | 12...Bxf6 | +0.83 | +0.85 | Bxf6 | 2 | 0% | best |
| 25 | 13.Nxf6+* | +0.85 | +0.82 | c3 | 3 | 0% | excellent |
| 26 | 13...Qxf6 | +0.82 | +0.78 | Qxf6 | 0 | 0% | best |
| 27 | 14.Qe2* | +0.78 | +0.38 | Qd3 | 40 | 4% | good |
| 28 | 14...O-O-O | +0.38 | +0.92 | g5 | 54 | 5% | good |
| 29 | 15.Qc4* | +0.92 | -0.36 | a4 | 128 | 12% | mistake |
| 30 | 15...Qe6 | -0.36 | +0.35 | g5 | 71 | 7% | inaccuracy |
| 31 | 16.Qa4* | +0.35 | +0.00 | Qc3 | 35 | 3% | good |
| 32 | 16...a6 | +0.00 | +0.53 | g5 | 53 | 5% | good |
| 33 | 17.Bxa6* | +0.53 | -1.70 | Bc4 | 223 | 20% | blunder |
| 34 | 17...bxa6 | -1.70 | -1.78 | bxa6 | 0 | 0% | best |
| 35 | 18.Qxa6+* | -1.78 | -1.74 | Qxa6+ | 0 | 0% | best |
| 36 | 18...Kc7 | -1.74 | -1.62 | Kc7 | 12 | 1% | best |
| 37 | 19.b4* | -1.62 | -3.21 | Nd2 | 159 | 12% | mistake |
| 38 | 19...Ra8 | -3.21 | -3.12 | Ra8 | 9 | 1% | best |
| 39 | 20.Qd3* | -3.12 | -3.20 | Qd3 | 8 | 1% | best |
| 40 | 20...Nxb4 | -3.20 | -3.33 | Nxb4 | 0 | 0% | best |
| 41 | 21.Qc3+* | -3.33 | -3.25 | Qc3+ | 0 | 0% | best |
| 42 | 21...Nc6 | -3.25 | -3.20 | Nc6 | 5 | 0% | best |
| 43 | 22.Rab1* | -3.20 | -3.67 | Rfd1 | 47 | 3% | good |
| 44 | 22...f5 | -3.67 | -3.42 | Rhb8 | 25 | 2% | excellent |
| 45 | 23.Rb2* | -3.42 | -4.06 | Nd2 | 64 | 4% | good |
| 46 | 23...fxe4 | -4.06 | -3.80 | Rhb8 | 26 | 1% | excellent |
| 47 | 24.Nd2* | -3.80 | -3.96 | Nd2 | 16 | 1% | best |
| 48 | 24...Kd8 | -3.96 | -2.79 | Rhb8 | 117 | 7% | inaccuracy |
| 49 | 25.Nc4* | -2.79 | -3.22 | Re1 | 43 | 3% | good |
| 50 | 25...Nd4 | -3.22 | -3.09 | Ke7 | 13 | 1% | excellent |
| 51 | 26.Rd1* | -3.09 | -12.58 | Re1 | 949 | 22% | blunder |
| 52 | 26...Ne2+ | -12.58 | -12.90 | Ne2+ | 0 | 0% | best |
| 53 | 27.Kf1* | -12.90 | -21.51 | Kh2 | 861 | 0% | excellent |
| 54 | 27...Nxc3 | -21.51 | -19.10 | Nxc3 | 241 | 0% | best |
| 55 | 28.Rxd6* | -19.10 | -M18 | Rxd6 |  | 0% | best |
| 56 | 28...Qxc4+ | -M18 | -M17 | Qxc4+ |  | 0% | best |
| 57 | 29.Kg1* | -M17 | -M12 | Kg1 |  | 0% | best |
| 58 | 29...Ne2+ | -M12 | -M10 | Qc5 |  | 0% | excellent |
| 59 | 30.Kh2* | -M10 | -M10 | Kh2 |  | 0% | best |
| 60 | 30...e3 | -M10 | -M9 | Qf7 |  | 0% | excellent |
| 61 | 31.Rb7* | -M9 | -M9 | Rf6 |  | 0% | excellent |
| 62 | 31...Qf4+ | -M9 | -M8 | Qf4+ |  | 0% | best |
| 63 | 32.g3* | -M8 | -M2 | Kh1 |  | 0% | excellent |
| 64 | 32...Qxf2+ | -M2 | -M1 | Qxf2+ |  | 0% | best |
| 65 | 33.Kh1* | -M1 | -M1 | Kh1 |  | 0% | best |
| 66 | 33...Qg1# | -M1 | -M1 | Nxg3# |  | 0% | excellent |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 2 positional.
- Middlegame: 5 error(s) (avg wp loss 18%).
