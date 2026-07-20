# (free, so lmk) Game analysis: DanielKetterer vs Candongas47

Date: 2026.07.19  |  Time control: daily (1/259200)  |  You played: black
Game: https://www.chess.com/game/daily/1001249768

## Summary

- Lichess accuracy: you 69.3%, opponent 79.4%
- Opening: B02 Alekhine Defense: Mokele Mbembe, Vavra Defense (theory followed through ply 6)
- First deviation from theory: ply 7, Opponent played 4. Bd3
- Your moves: 5 best, 3 excellent, 5 good, 3 inaccuracy, 2 mistake, 1 blunder

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

You played 14...Bb7. Stockfish preferred Nxe5, after which the main line runs 14...Nxe5 15. Qe2 Rb8 16. Rad1 Bd6 17. Bd4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: a favorable capture was available (Nxe5). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxe5 (-1.49), Bb7 (+2.63), Nd4 (+3.72).

## Critical positions

- Ply 9 (opponent), 5.Kxf2: +3.01 -> +3.04 [only-move situation]
- Ply 23 (opponent), 12.Nd4: +4.71 -> +0.01 [evaluation crossed winning -> equal]
- Ply 24 (you), 12...Nxd4: +0.01 -> +0.00 [only-move situation]
- Ply 26 (you), 13...Nc6: +0.00 -> +0.08 [only-move situation]
- Ply 28 (you), 14...Bb7: -1.49 -> +2.86 [only-move situation; evaluation crossed equal -> losing]

## Your errors, move by move

### 2...Nf6 (inaccuracy, positional, wp loss 5%)

You played 2...Nf6. Stockfish preferred d5, after which the main line runs 2...d5 3. Nc3 Nf6 4. Bg5 dxe4 5. Nxe4. Why it went wrong: motif: creates threat on e4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: d5 (+0.39), a6 (+0.53), c5 (+0.69).

### 4...Nxf2 (mistake, tactical, wp loss 12%)

You played 4...Nxf2. Stockfish preferred d5, after which the main line runs 4...d5 5. Nh3 h6 6. O-O c5 7. c3. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: left knight on f2 insufficiently defended. Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: d5 (+1.47), f5 (+1.80), Nxf2 (+3.10).

### 5...Nc6 (inaccuracy, positional, wp loss 5%)

You played 5...Nc6. Stockfish preferred Qh4+, after which the main line runs 5...Qh4+ 6. Ke3 Qg5+ 7. Kf3 Qh4 8. Be3. Why it went wrong: the best move was a forcing check; motif: creates threat on d4. This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Qh4+ (+3.04), d6 (+3.81), c5 (+3.86).

### 14...Bb7 (blunder, tactical, wp loss 38%)

You played 14...Bb7. Stockfish preferred Nxe5, after which the main line runs 14...Nxe5 15. Qe2 Rb8 16. Rad1 Bd6 17. Bd4. The evaluation crossed from equal to losing, which matters more than the raw number. Why it went wrong: a favorable capture was available (Nxe5). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxe5 (-1.49), Bb7 (+2.63), Nd4 (+3.72).

### 15...Bxh4+ (mistake, tactical, wp loss 14%)

You played 15...Bxh4+. Stockfish preferred Nxe5, after which the main line runs 15...Nxe5 16. Qg3 Bd6 17. Bxb7 Rd8 18. Bf4. Why it went wrong: left queen on d7, bishop on h4 insufficiently defended; a favorable capture was available (Nxe5). Before committing to a quiet move here, the checklist is checks, captures, threats, in that order. The engine prefers this move from search depth 1; it sits near the surface, a forcing move, the kind a checks-and-captures scan catches. Candidates considered by the engine: Nxe5 (+3.10), Bd6 (+4.88), Qxd1 (+5.58).

### 16...Qe7 (inaccuracy, positional, wp loss 8%)

You played 16...Qe7. Stockfish preferred Nxe5, after which the main line runs 16...Nxe5 17. Qh1 Qe7 18. Bxb7 Rd8 19. Rxd8+. Why it went wrong: a favorable capture was available (Nxe5). This was a judgment error rather than a missed tactic; compare the pawn structure and piece activity after both moves. The engine prefers this move from search depth 1; it sits near the surface, a quiet move, but one whose point shows at a glance. Candidates considered by the engine: Nxe5 (+5.95), Qxd1 (+6.70), Rf8 (+7.06).

## Full move table

| Ply | Move | Eval before | Eval after | Best | CP loss | WP loss | Class |
|-----|------|-------------|------------|------|---------|---------|-------|
| 1 | 1.e4 | +0.34 | +0.18 | d4 | 16 | 1% | excellent |
| 2 | 1...e6* | +0.18 | +0.56 | c6 | 38 | 3% | good |
| 3 | 2.d4 | +0.56 | +0.39 | d4 | 17 | 2% | best |
| 4 | 2...Nf6* | +0.39 | +0.97 | d5 | 58 | 5% | inaccuracy |
| 5 | 3.e5 | +0.97 | +0.86 | e5 | 11 | 1% | best |
| 6 | 3...Ne4* | +0.86 | +1.42 | Nd5 | 56 | 5% | good |
| 7 | 4.Bd3 | +1.42 | +1.47 | Nh3 | 0 | 0% | excellent |
| 8 | 4...Nxf2* | +1.47 | +3.01 | d5 | 154 | 12% | mistake |
| 9 | 5.Kxf2 | +3.01 | +3.04 | Kxf2 | 0 | 0% | best |
| 10 | 5...Nc6* | +3.04 | +3.87 | Qh4+ | 83 | 5% | inaccuracy |
| 11 | 6.Be3 | +3.87 | +3.85 | Nf3 | 2 | 0% | excellent |
| 12 | 6...d6* | +3.85 | +4.00 | Nxd4 | 15 | 1% | excellent |
| 13 | 7.Nf3 | +4.00 | +3.95 | Nf3 | 5 | 0% | best |
| 14 | 7...dxe5* | +3.95 | +4.24 | Nb4 | 29 | 2% | excellent |
| 15 | 8.dxe5 | +4.24 | +4.19 | dxe5 | 5 | 0% | best |
| 16 | 8...Be7* | +4.19 | +4.81 | Qe7 | 62 | 3% | good |
| 17 | 9.h4 | +4.81 | +4.00 | Qe2 | 81 | 4% | good |
| 18 | 9...Qd5* | +4.00 | +4.05 | Qd5 | 5 | 0% | best |
| 19 | 10.Nc3 | +4.05 | +4.06 | Nc3 | 0 | 0% | best |
| 20 | 10...Qd7* | +4.06 | +4.86 | Qa5 | 80 | 4% | good |
| 21 | 11.g4 | +4.86 | +4.33 | h5 | 53 | 3% | good |
| 22 | 11...b6* | +4.33 | +4.71 | Nb4 | 38 | 2% | excellent |
| 23 | 12.Nd4 | +4.71 | +0.01 | Be4 | 470 | 35% | blunder |
| 24 | 12...Nxd4* | +0.01 | +0.00 | Nxd4 | 0 | 0% | best |
| 25 | 13.Be4 | +0.00 | +0.00 | Be4 | 0 | 0% | best |
| 26 | 13...Nc6* | +0.00 | +0.08 | Nc6 | 8 | 1% | best |
| 27 | 14.Qf3 | +0.08 | -1.49 | Qxd7+ | 157 | 14% | mistake |
| 28 | 14...Bb7* | -1.49 | +2.86 | Nxe5 | 435 | 38% | blunder |
| 29 | 15.Rad1 | +2.86 | +3.10 | Rad1 | 0 | 0% | best |
| 30 | 15...Bxh4+* | +3.10 | +5.86 | Nxe5 | 276 | 14% | mistake |
| 31 | 16.Rxh4 | +5.86 | +5.95 | Rxh4 | 0 | 0% | best |
| 32 | 16...Qe7* | +5.95 | +9.89 | Nxe5 | 394 | 8% | inaccuracy |
| 33 | 17.Bxc6+ | +9.89 | +11.25 | Bxc6+ | 0 | 0% | best |
| 34 | 17...Kf8* | +11.25 | +9.90 | Kf8 | 0 | 0% | best |
| 35 | 18.g5 | +9.90 | +8.88 | Rdh1 | 102 | 1% | excellent |
| 36 | 18...Bxc6* | +8.88 | +8.88 | Bxc6 | 0 | 0% | best |
| 37 | 19.Qxc6 | +8.88 | +8.06 | Qxc6 | 82 | 1% | best |
| 38 | 19...Re8* | +8.06 | M14 | Rd8 |  | 2% | good |
| 39 | 20.Rd7 | M14 | M12 | Rd7 |  | 0% | best |

Rows marked * are your moves. WP loss is win-probability loss; it is the primary signal, CP loss is shown for reference.

## Patterns in this game

- Error mix: 3 tactical, 3 positional.
- Opening: 3 error(s) (avg wp loss 7%).
- Middlegame: 3 error(s) (avg wp loss 20%).
- 3 of your errors came with under a minute on the clock.
