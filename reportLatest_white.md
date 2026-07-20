# (free, so lmk) Game analysis: kmlkrn vs DanielKetterer

Date: 2026.07.20  |  Time control: rapid (1800)  |  You played: white
Game: https://www.chess.com/game/live/171848454352

## Summary

- Lichess accuracy: you 73.7%, opponent 57.4%
- Opening: A45 Indian Defense: Pawn Push Variation (theory followed through ply 3)
- First deviation from theory: ply 4, Opponent played 2... c6
- Your moves: 6 best, 3 excellent, 5 good, 1 inaccuracy, 4 mistake, 1 blunder

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

You played 19.Qe1. Stockfish preferred Qc2, after which the main line runs 19. Qc2 Nd7 20. Nce2 Qh1+ 21. Kf2 Ne4+. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left rook on f1 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qc2 (+2.78), Qd1 (+1.01), Qe1 (+0.00).

## Critical positions

- Ply 28 (opponent), 14...Ne4: +0.12 -> +2.67 [evaluation crossed equal -> losing]
- Ply 30 (opponent), 15...Bxh2+: +0.73 -> +4.11 [evaluation crossed equal -> losing]
- Ply 31 (you), 16.Kxh2: +4.11 -> +4.13 [only-move situation]
- Ply 37 (you), 19.Qe1: +2.78 -> +0.00 [evaluation crossed winning -> equal]
- Ply 38 (opponent), 19...Nxf1: +0.00 -> +7.10 [evaluation crossed equal -> losing]
- Ply 39 (you), 20.Qxh4: +7.10 -> +8.11 [only-move situation]

## Your errors, move by move

### 11.a3 (mistake, positional, wp loss 15%)

You played 11.a3. Stockfish preferred e4, after which the main line runs 11. e4 dxe4 12. Qxd6 exf3 13. Bxf3 Nc6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e4 (+1.23), h3 (+0.00), g3 (+0.00).

### 12.b4 (mistake, tactical, wp loss 14%)

You played 12.b4. Stockfish preferred Nxb5, after which the main line runs 12. Nxb5 axb5 13. Nd4 Ne4 14. g3 Qd7. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxb5 (+1.55), Bxb5 (+1.08), h3 (+0.06).

### 14.Bb2 (inaccuracy, positional, wp loss 6%)

You played 14.Bb2. Stockfish preferred e4, after which the main line runs 14. e4 Nc6 15. exd5 exd5 16. Bg5 h6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: e4 (+0.79), Bb2 (+0.22), Rd1 (+0.11).

### 15.Nd4 (mistake, tactical, wp loss 16%)

You played 15.Nd4. Stockfish preferred Nxe4, after which the main line runs 15. Nxe4 dxe4 16. Nd4 Qe8 17. Qg4 Be5. The evaluation crossed from winning to equal, which matters more than the raw number. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxe4 (+2.67), Rac1 (+1.61), Rfc1 (+1.08).

### 18.f3 (mistake, positional, wp loss 12%)

You played 18.f3. Stockfish preferred Nf3, after which the main line runs 18. Nf3 Rxf3 19. Qxf3 Nd2 20. Qf4 Qxf4. Why it went wrong: motif: creates threat on h4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nf3 (+4.50), Nxe4 (+4.46), f4 (+3.52).

### 19.Qe1 (blunder, tactical, wp loss 24%)

You played 19.Qe1. Stockfish preferred Qc2, after which the main line runs 19. Qc2 Nd7 20. Nce2 Qh1+ 21. Kf2 Ne4+. The evaluation crossed from winning to equal, which matters more than the raw number. Why it went wrong: left rook on f1 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 9; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Qc2 (+2.78), Qd1 (+1.01), Qe1 (+0.00).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.d4* | +0.35 | +0.20 | Nf3 | 15 | 1% | excellent |
| 2 | 1...Nf6 | +0.20 | +0.24 | d5 | 4 | 0% | excellent |
| 3 | 2.d5* | +0.24 | -0.25 | Nf3 | 49 | 5% | good |
| 4 | 2...c6 | -0.25 | -0.24 | e6 | 1 | 0% | excellent |
| 5 | 3.c4* | -0.24 | -0.23 | c4 | 0 | 0% | best |
| 6 | 3...cxd5 | -0.23 | -0.22 | e6 | 1 | 0% | excellent |
| 7 | 4.cxd5* | -0.22 | -0.18 | cxd5 | 0 | 0% | best |
| 8 | 4...e6 | -0.18 | -0.17 | Qa5+ | 1 | 0% | excellent |
| 9 | 5.dxe6* | -0.17 | -0.44 | Nc3 | 27 | 2% | good |
| 10 | 5...fxe6 | -0.44 | -0.35 | fxe6 | 9 | 1% | best |
| 11 | 6.Nc3* | -0.35 | -0.57 | Nf3 | 22 | 2% | good |
| 12 | 6...d5 | -0.57 | -0.49 | d5 | 8 | 1% | best |
| 13 | 7.e3* | -0.49 | -0.80 | Nf3 | 31 | 3% | good |
| 14 | 7...Bd6 | -0.80 | -0.44 | Nc6 | 36 | 3% | good |
| 15 | 8.Nf3* | -0.44 | -0.64 | e4 | 20 | 2% | excellent |
| 16 | 8...O-O | -0.64 | -0.47 | e5 | 17 | 2% | excellent |
| 17 | 9.Be2* | -0.47 | -0.52 | Be2 | 5 | 0% | best |
| 18 | 9...Bd7 | -0.52 | +0.32 | Nc6 | 84 | 8% | inaccuracy |
| 19 | 10.O-O* | +0.32 | -0.08 | e4 | 40 | 4% | good |
| 20 | 10...a6 | -0.08 | +1.23 | Qe7 | 131 | 12% | mistake |
| 21 | 11.a3* | +1.23 | -0.39 | e4 | 162 | 15% | mistake |
| 22 | 11...Bb5 | -0.39 | +1.55 | Qc7 | 194 | 17% | mistake |
| 23 | 12.b4* | +1.55 | +0.00 | Nxb5 | 155 | 14% | mistake |
| 24 | 12...Bxe2 | +0.00 | +0.00 | Bxe2 | 0 | 0% | best |
| 25 | 13.Qxe2* | +0.00 | +0.00 | Nxe2 | 0 | 0% | excellent |
| 26 | 13...b5 | +0.00 | +0.79 | Nc6 | 79 | 7% | inaccuracy |
| 27 | 14.Bb2* | +0.79 | +0.12 | e4 | 67 | 6% | inaccuracy |
| 28 | 14...Ne4 | +0.12 | +2.67 | Nc6 | 255 | 22% | blunder |
| 29 | 15.Nd4* | +2.67 | +0.73 | Nxe4 | 194 | 16% | mistake |
| 30 | 15...Bxh2+ | +0.73 | +4.11 | Nxc3 | 338 | 25% | blunder |
| 31 | 16.Kxh2* | +4.11 | +4.13 | Kxh2 | 0 | 0% | best |
| 32 | 16...Qh4+ | +4.13 | +4.30 | Qh4+ | 17 | 1% | best |
| 33 | 17.Kg1* | +4.30 | +4.38 | Kg1 | 0 | 0% | best |
| 34 | 17...Rf6 | +4.38 | +4.50 | Nf6 | 12 | 1% | excellent |
| 35 | 18.f3* | +4.50 | +2.57 | Nf3 | 193 | 12% | mistake |
| 36 | 18...Ng3 | +2.57 | +2.78 | Ng3 | 21 | 2% | best |
| 37 | 19.Qe1* | +2.78 | +0.00 | Qc2 | 278 | 24% | blunder |
| 38 | 19...Nxf1 | +0.00 | +7.10 | Rg6 | 710 | 43% | blunder |
| 39 | 20.Qxh4* | +7.10 | +8.11 | Qxh4 | 0 | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 3 positional.
- Middlegame: 6 error(s) (avg wp loss 14%).
