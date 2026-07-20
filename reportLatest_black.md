# (free, so lmk) Game analysis: kmlkrn vs DanielKetterer

Date: 2026.07.20  |  Time control: rapid (1800)  |  You played: black
Game: https://www.chess.com/game/live/171848454352

## Summary

- Lichess accuracy: you 57.4%, opponent 73.7%
- Opening: A45 Indian Defense: Pawn Push Variation (theory followed through ply 3)
- First deviation from theory: ply 4, You played 2... c6
- Your moves: 5 best, 6 excellent, 1 good, 2 inaccuracy, 2 mistake, 3 blunder

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

You played 19...Nxf1. Stockfish preferred Rg6, after which the main line runs 19...Rg6 20. Nxe6 Rxe6 21. Nxd5 Qh1+ 22. Kf2. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on h4, knight on f1 insufficiently defended; motif: creates threat on f1. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 13; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rg6 (+0.00), Nd7 (+0.00), Qh1+ (+1.72).

## Critical positions

- Ply 28 (you), 14...Ne4: +0.12 -> +2.67 [evaluation crossed equal -> losing]
- Ply 30 (you), 15...Bxh2+: +0.73 -> +4.11 [evaluation crossed equal -> losing]
- Ply 31 (opponent), 16.Kxh2: +4.11 -> +4.13 [only-move situation]
- Ply 37 (opponent), 19.Qe1: +2.78 -> +0.00 [evaluation crossed winning -> equal]
- Ply 38 (you), 19...Nxf1: +0.00 -> +7.10 [evaluation crossed equal -> losing]
- Ply 39 (opponent), 20.Qxh4: +7.10 -> +8.11 [only-move situation]

## Your errors, move by move

### 9...Bd7 (inaccuracy, positional, wp loss 8%)

You played 9...Bd7. Stockfish preferred Nc6, after which the main line runs 9...Nc6 10. O-O a6 11. b3 Qe7 12. Bb2. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc6 (-0.52), h6 (-0.38), a6 (-0.32).

### 10...a6 (mistake, positional, wp loss 12%)

You played 10...a6. Stockfish preferred Qe7, after which the main line runs 10...Qe7 11. e4 dxe4 12. Ng5 Be5 13. Ngxe4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 5; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qe7 (-0.08), Bc6 (+0.00), Qc7 (+0.11).

### 11...Bb5 (mistake, positional, wp loss 17%)

You played 11...Bb5. Stockfish preferred Qc7, after which the main line runs 11...Qc7 12. Bd2 Nc6 13. Rc1 Be8 14. b4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 4; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qc7 (-0.39), Bc6 (-0.24), Qe7 (-0.17).

### 13...b5 (inaccuracy, positional, wp loss 7%)

You played 13...b5. Stockfish preferred Nc6, after which the main line runs 13...Nc6 14. Bb2 Qe8 15. b5 Na5 16. bxa6. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc6 (+0.00), Nbd7 (+0.00), Qc7 (+0.03).

### 14...Ne4 (blunder, positional, wp loss 22%)

You played 14...Ne4. Stockfish preferred Nc6, after which the main line runs 14...Nc6 15. Rad1 Qc7 16. h3 Ne5 17. Nxe5. The evaluation crossed from equal to losing, which matters more than the raw number. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 3; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nc6 (+0.12), Nbd7 (+0.36), Re8 (+0.60).

### 15...Bxh2+ (blunder, tactical, wp loss 25%)

You played 15...Bxh2+. Stockfish preferred Nxc3, after which the main line runs 15...Nxc3 16. Bxc3 Re8 17. Qg4 Qc7 18. Rac1. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left pawn on e6, bishop on h2 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine first prefers this move at depth 7; findable, but it takes a deliberate look rather than a scan. Candidates considered by the engine: Nxc3 (+0.73), Qh4 (+1.66), Qe7 (+2.68).

### 19...Nxf1 (blunder, tactical, wp loss 43%)

You played 19...Nxf1. Stockfish preferred Rg6, after which the main line runs 19...Rg6 20. Nxe6 Rxe6 21. Nxd5 Qh1+ 22. Kf2. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left queen on h4, knight on f1 insufficiently defended; motif: creates threat on f1. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine does not prefer this move until depth 13; missing it is forgivable, so weigh this one lightly. Candidates considered by the engine: Rg6 (+0.00), Nd7 (+0.00), Qh1+ (+1.72).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.d4 | +0.35 | +0.20 | Nf3 | 15 | 1% | excellent |
| 2 | 1...Nf6* | +0.20 | +0.24 | d5 | 4 | 0% | excellent |
| 3 | 2.d5 | +0.24 | -0.25 | Nf3 | 49 | 5% | good |
| 4 | 2...c6* | -0.25 | -0.24 | e6 | 1 | 0% | excellent |
| 5 | 3.c4 | -0.24 | -0.23 | c4 | 0 | 0% | best |
| 6 | 3...cxd5* | -0.23 | -0.22 | e6 | 1 | 0% | excellent |
| 7 | 4.cxd5 | -0.22 | -0.18 | cxd5 | 0 | 0% | best |
| 8 | 4...e6* | -0.18 | -0.17 | Qa5+ | 1 | 0% | excellent |
| 9 | 5.dxe6 | -0.17 | -0.44 | Nc3 | 27 | 2% | good |
| 10 | 5...fxe6* | -0.44 | -0.35 | fxe6 | 9 | 1% | best |
| 11 | 6.Nc3 | -0.35 | -0.57 | Nf3 | 22 | 2% | good |
| 12 | 6...d5* | -0.57 | -0.49 | d5 | 8 | 1% | best |
| 13 | 7.e3 | -0.49 | -0.80 | Nf3 | 31 | 3% | good |
| 14 | 7...Bd6* | -0.80 | -0.44 | Nc6 | 36 | 3% | good |
| 15 | 8.Nf3 | -0.44 | -0.64 | e4 | 20 | 2% | excellent |
| 16 | 8...O-O* | -0.64 | -0.47 | e5 | 17 | 2% | excellent |
| 17 | 9.Be2 | -0.47 | -0.52 | Be2 | 5 | 0% | best |
| 18 | 9...Bd7* | -0.52 | +0.32 | Nc6 | 84 | 8% | inaccuracy |
| 19 | 10.O-O | +0.32 | -0.08 | e4 | 40 | 4% | good |
| 20 | 10...a6* | -0.08 | +1.23 | Qe7 | 131 | 12% | mistake |
| 21 | 11.a3 | +1.23 | -0.39 | e4 | 162 | 15% | mistake |
| 22 | 11...Bb5* | -0.39 | +1.55 | Qc7 | 194 | 17% | mistake |
| 23 | 12.b4 | +1.55 | +0.00 | Nxb5 | 155 | 14% | mistake |
| 24 | 12...Bxe2* | +0.00 | +0.00 | Bxe2 | 0 | 0% | best |
| 25 | 13.Qxe2 | +0.00 | +0.00 | Nxe2 | 0 | 0% | excellent |
| 26 | 13...b5* | +0.00 | +0.79 | Nc6 | 79 | 7% | inaccuracy |
| 27 | 14.Bb2 | +0.79 | +0.12 | e4 | 67 | 6% | inaccuracy |
| 28 | 14...Ne4* | +0.12 | +2.67 | Nc6 | 255 | 22% | blunder |
| 29 | 15.Nd4 | +2.67 | +0.73 | Nxe4 | 194 | 16% | mistake |
| 30 | 15...Bxh2+* | +0.73 | +4.11 | Nxc3 | 338 | 25% | blunder |
| 31 | 16.Kxh2 | +4.11 | +4.13 | Kxh2 | 0 | 0% | best |
| 32 | 16...Qh4+* | +4.13 | +4.30 | Qh4+ | 17 | 1% | best |
| 33 | 17.Kg1 | +4.30 | +4.38 | Kg1 | 0 | 0% | best |
| 34 | 17...Rf6* | +4.38 | +4.50 | Nf6 | 12 | 1% | excellent |
| 35 | 18.f3 | +4.50 | +2.57 | Nf3 | 193 | 12% | mistake |
| 36 | 18...Ng3* | +2.57 | +2.78 | Ng3 | 21 | 2% | best |
| 37 | 19.Qe1 | +2.78 | +0.00 | Qc2 | 278 | 24% | blunder |
| 38 | 19...Nxf1* | +0.00 | +7.10 | Rg6 | 710 | 43% | blunder |
| 39 | 20.Qxh4 | +7.10 | +8.11 | Qxh4 | 0 | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 2 tactical, 5 positional.
- Opening: 2 error(s) (avg wp loss 10%).
- Middlegame: 5 error(s) (avg wp loss 23%).
