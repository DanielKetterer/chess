# (free, so lmk) Game analysis: kuchabh vs DanielKetterer

Date: 2026.07.23  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171975384914

## Summary

- Lichess accuracy: you 80.1%, opponent 48.7%
- Opening: B10 Caro-Kann Defense: Hillbilly Attack (theory followed through ply 3)
- First deviation from theory: ply 4, Opponent played 2... d5
- Your moves: 6 best, 8 excellent, 4 good, 2 inaccuracy, 0 mistake, 2 blunder

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

You played 6.Bd3. Stockfish preferred Bxc6+, after which the main line runs 6. Bxc6+ bxc6 7. c4 e6 8. O-O Bd6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bxc6+ (-0.13), Ba4 (-0.75), Be2 (-1.17).

## Critical positions

- Ply 11 (you), 6.Bd3: -0.13 -> -3.41 [evaluation crossed equal -> losing]
- Ply 12 (opponent), 6...e5: -3.41 -> -3.42 [only-move situation]
- Ply 19 (you), 10.f3: -0.47 -> -3.64 [evaluation crossed equal -> losing]
- Ply 42 (opponent), 21...Qxc4: -7.35 -> +4.35 [evaluation crossed winning -> losing]
- Ply 43 (you), 22.dxc4: +4.35 -> +4.42 [only-move situation]

## Your errors, move by move

### 2.Bc4 (inaccuracy, positional, wp loss 6%)

You played 2.Bc4. Stockfish preferred d4, after which the main line runs 2. d4 d5 3. e5 Bf5 4. Be2 e6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d4 (+0.30), c4 (+0.29), Nc3 (+0.24).

### 6.Bd3 (blunder, tactical, wp loss 27%)

You played 6.Bd3. Stockfish preferred Bxc6+, after which the main line runs 6. Bxc6+ bxc6 7. c4 e6 8. O-O Bd6. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: the best move was a forcing check. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Bxc6+ (-0.13), Ba4 (-0.75), Be2 (-1.17).

### 10.f3 (blunder, tactical, wp loss 25%)

You played 10.f3. Stockfish preferred dxe4, after which the main line runs 10. dxe4 Nxe4 11. Nf3 Bd6 12. O-O O-O. The evaluation crossed from equal to losing, which matters more than the raw number. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: dxe4 (-0.47), Nd2 (-1.19), a3 (-1.41).

### 14.Qc2 (inaccuracy, positional, wp loss 6%)

You played 14.Qc2. Stockfish preferred f4, after which the main line runs 14. f4 Nd5 15. Nf3 Nxf4 16. O-O O-O. Why it went wrong: left pawn on b4 insufficiently defended. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine first prefers this move at depth 10; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: f4 (-4.93), d4 (-5.27), Nc2 (-5.47).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4* | +0.34 | +0.25 | e4 | 9 | 1% | best |
| 2 | 1...c6 | +0.25 | +0.30 | e5 | 5 | 0% | excellent |
| 3 | 2.Bc4* | +0.30 | -0.37 | d4 | 67 | 6% | inaccuracy |
| 4 | 2...d5 | -0.37 | -0.39 | d5 | 0 | 0% | best |
| 5 | 3.exd5* | -0.39 | -0.43 | exd5 | 4 | 0% | best |
| 6 | 3...cxd5 | -0.43 | -0.37 | cxd5 | 6 | 1% | best |
| 7 | 4.Bb5+* | -0.37 | -0.36 | Bb3 | 0 | 0% | excellent |
| 8 | 4...Nc6 | -0.36 | -0.39 | Bd7 | 0 | 0% | excellent |
| 9 | 5.Nf3* | -0.39 | -0.39 | d4 | 0 | 0% | excellent |
| 10 | 5...a6 | -0.39 | -0.13 | Bg4 | 26 | 2% | good |
| 11 | 6.Bd3* | -0.13 | -3.41 | Bxc6+ | 328 | 27% | blunder |
| 12 | 6...e5 | -3.41 | -3.42 | e5 | 0 | 0% | best |
| 13 | 7.Be2* | -3.42 | -3.47 | Be2 | 5 | 0% | best |
| 14 | 7...e4 | -3.47 | -3.56 | e4 | 0 | 0% | best |
| 15 | 8.Ng1* | -3.56 | -3.51 | Ng1 | 0 | 0% | best |
| 16 | 8...d4 | -3.51 | -0.95 | Bc5 | 256 | 20% | mistake |
| 17 | 9.d3* | -0.95 | -0.98 | d3 | 3 | 0% | best |
| 18 | 9...Nf6 | -0.98 | -0.47 | f5 | 51 | 5% | good |
| 19 | 10.f3* | -0.47 | -3.64 | dxe4 | 317 | 25% | blunder |
| 20 | 10...e3 | -3.64 | -3.93 | e3 | 0 | 0% | best |
| 21 | 11.c3* | -3.93 | -4.37 | f4 | 44 | 2% | good |
| 22 | 11...Bc5 | -4.37 | -3.91 | Nd5 | 46 | 2% | good |
| 23 | 12.b4* | -3.91 | -4.68 | f4 | 77 | 4% | good |
| 24 | 12...Bb6 | -4.68 | -4.65 | Ba7 | 3 | 0% | excellent |
| 25 | 13.Na3* | -4.65 | -5.06 | Bb2 | 41 | 2% | excellent |
| 26 | 13...dxc3 | -5.06 | -4.93 | dxc3 | 13 | 1% | best |
| 27 | 14.Qc2* | -4.93 | -6.68 | f4 | 175 | 6% | inaccuracy |
| 28 | 14...Bd4 | -6.68 | -5.45 | O-O | 123 | 4% | good |
| 29 | 15.b5* | -5.45 | -6.01 | f4 | 56 | 2% | excellent |
| 30 | 15...Nb4 | -6.01 | -5.76 | axb5 | 25 | 1% | excellent |
| 31 | 16.Qb3* | -5.76 | -5.96 | Qa4 | 20 | 1% | excellent |
| 32 | 16...Qd6 | -5.96 | -4.77 | a5 | 119 | 5% | good |
| 33 | 17.Nc4* | -4.77 | -4.99 | bxa6 | 22 | 1% | excellent |
| 34 | 17...Qc5 | -4.99 | -5.22 | Qe7 | 0 | 0% | excellent |
| 35 | 18.Ba3* | -5.22 | -5.96 | a3 | 74 | 3% | good |
| 36 | 18...Nfd5 | -5.96 | -6.00 | Nfd5 | 0 | 0% | best |
| 37 | 19.Nh3* | -6.00 | -6.92 | Rc1 | 92 | 3% | good |
| 38 | 19...axb5 | -6.92 | -6.96 | axb5 | 0 | 0% | best |
| 39 | 20.Bxb4* | -6.96 | -7.24 | O-O | 28 | 1% | excellent |
| 40 | 20...Nxb4 | -7.24 | -7.16 | Nxb4 | 8 | 0% | best |
| 41 | 21.a3* | -7.16 | -7.35 | O-O | 19 | 0% | excellent |
| 42 | 21...Qxc4 | -7.35 | +4.35 | bxc4 | 1170 | 77% | blunder |
| 43 | 22.dxc4* | +4.35 | +4.42 | dxc4 | 0 | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 2 tactical, 2 positional.
- Opening: 3 error(s) (avg wp loss 19%).
- Middlegame: 1 error(s) (avg wp loss 6%).
