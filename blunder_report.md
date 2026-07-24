# Blunder Report

REAL DATA  |  analysis depth 24  |  ladder floor 6  |  cap 24  |  stable run 3  |  4 games  |  27 errors

Depth column: an integer is a measured depth. `<=floor` means the engine stably preferred the move at or below depth 6, which is as shallow as this measurement resolves. `>cap` means it never settled within depth 24. `unmeasured` means the measurement was invalid and the row is kept but not binned.

![Blunder scatter](blunder_scatter.png)

| Game # | Game ID | Date | Move | Class | Category | WP loss | Depth | Refute | Seconds | Pre-error | Report |
|---:|---|---|---|---|---|---:|---|---|---:|---|---|
| 0 | 0de5037d-86b9-11f1-9aa4-0be2bf01000f | 2026.07.23 | 8...d4 | mistake | positional | 18.0 | 8 | 6 | 95 | winning | reports/171975384914_20260723T173014Z_black.md |
| 0 | 0de5037d-86b9-11f1-9aa4-0be2bf01000f | 2026.07.23 | 9...Nf6 | inaccuracy | positional | 7.0 | 10 | 8 | 42 | balanced | reports/171975384914_20260723T173014Z_black.md |
| 0 | 0de5037d-86b9-11f1-9aa4-0be2bf01000f | 2026.07.23 | 21...Qxc4 | blunder | tactical | 71.0 | >cap | 1 | 145 | winning | reports/171975384914_20260723T173014Z_black.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 7.Nge2 | mistake | tactical | 10.0 | <=floor | 1 | 49 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 12.g4 | mistake | positional | 10.0 | >cap | 3 | 105 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 14.f4 | mistake | positional | 18.0 | <=floor | 4 | 64 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 28.d5 | inaccuracy | positional | 6.0 | <=floor | 1 | 82 | winning | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 30.Rg4 | blunder | tactical | 29.0 | >cap | 11 | 12 | winning | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 31.Rd4 | blunder | tactical | 40.0 | <=floor | 1 | 27 | winning | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 32.Rad1 | mistake | tactical | 16.0 | 12 | >18 | 36 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 34.d6 | inaccuracy | positional | 7.0 | 14 | 7 | 22 | losing | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 36.Kf2 | blunder | tactical | 31.0 | <=floor | 17 | 100 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 1 | 14c29713-86dc-11f1-8e1f-7d7daa01000f | 2026.07.23 | 37.Rxa4 | blunder | tactical | 31.0 | <=floor | 6 | 64 | balanced | reports/171984928774_20260723T215758Z_white.md |
| 2 | 2e868f18-86bc-11f1-bd39-daef7701000f | 2026.07.23 | 6.Bxf7+ | mistake | tactical | 15.0 | 22 | 1 | 34 | balanced | reports/171976324014_20260723T174505Z_white.md |
| 2 | 2e868f18-86bc-11f1-bd39-daef7701000f | 2026.07.23 | 8.O-O | inaccuracy | positional | 5.0 | 10 | 16 | 20 | losing | reports/171976324014_20260723T174505Z_white.md |
| 2 | 2e868f18-86bc-11f1-bd39-daef7701000f | 2026.07.23 | 10.Qh5+ | inaccuracy | positional | 6.0 | <=floor | 2 | 27 | losing | reports/171976324014_20260723T174505Z_white.md |
| 2 | 2e868f18-86bc-11f1-bd39-daef7701000f | 2026.07.23 | 12.Qh6 | mistake | tactical | 16.0 | <=floor | 6 | 62 | losing | reports/171976324014_20260723T174505Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 6.d3 | mistake | positional | 16.0 | <=floor | 5 | 24 | winning | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 11.g4 | inaccuracy | positional | 5.0 | 10 | 3 | 4 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 12.d4 | inaccuracy | positional | 8.0 | <=floor | 1 | 11 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 15.e5 | mistake | positional | 12.0 | <=floor | 1 | 54 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 17.hxg4 | mistake | tactical | 16.0 | <=floor | 10 | 18 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 18.Kf2 | inaccuracy | positional | 8.0 | 11 | 3 | 45 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 19.Re3 | blunder | positional | 23.0 | 14 | 15 | 110 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 23.Qh1 | blunder | tactical | 41.0 | <=floor | 1 | 70 | balanced | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 29.Kb3 | mistake | positional | 13.0 | <=floor | 2 | 12 | winning | reports/171987878016_20260723T233059Z_white.md |
| 3 | 6b5508ea-86ea-11f1-8817-a0dc1301000f | 2026.07.23 | 30.Qf1 | blunder | tactical | 72.0 | <=floor | 1 | 95 | winning | reports/171987878016_20260723T233059Z_white.md |
