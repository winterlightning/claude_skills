---
name: side-layout-adjust-72
description: Review Pictographic icon-72 side combinations (a main-54 icon plus a sub-36 icon at a corner or side, 72 build) and improve their layout exactly as /side-layout-adjust does for 64 - look at the result, the main and the sub, name what the combination means, keep the stored layout when it reads well and shows that meaning, else resize the main -> move the main -> move the sub -> resize the sub (the main may move but must fit the 72x72 keyshape system), always on the 72 keyshape presets - and record each verdict. Every command runs with SIDE_SIZE=72. Arguments are reference ids, or --next N [--offset K] [--hand|--auto] [--unreviewed], or --recheck ids. Use when asked to review or fix the layout of 72 side combinations. Hand-authored; edit this file directly.
---

# Side layout adjust, 72

Read `.claude/skills/side-layout-adjust/SKILL.md` first and follow it **exactly**: every rule there applies here
(approved parts only, the keyshape system, look at the result, the main and the sub before any script, the layout must
show the meaning, keep the stored layout when it reads well, the priority flow resize the main -> move the main -> move the
sub -> resize the sub, the canvas keyshape rule, the main moving only by whole units at a preset size inside the canvas keyshape, search with `side_layout_search.mjs` as a reference, rank the contact by eye, cut or
clear never a nick, side never container, work the batch, finish in one go, record every pair). Only the
differences below change.

## Differences at 72

- **Every command starts with `SIDE_SIZE=72`**, for example
  `SIDE_SIZE=72 node icon_set/scripts/side_layout.mjs fetch <id>`,
  `SIDE_SIZE=72 node icon_set/scripts/side_layout_search.mjs <dir>`,
  `SIDE_SIZE=72 node icon_set/scripts/side_keyshape_check.mjs <dir>`,
  `SIDE_SIZE=72 node icon_set/scripts/side_contact_check.mjs <dir>`,
  `SIDE_SIZE=72 node icon_set/scripts/side_hull.mjs <dir> --current`,
  `SIDE_SIZE=72 node icon_set/scripts/side_review_record.mjs <dir> ...`.
  Without it the tools work on the 64 pairs. Each Bash call is a new shell, so put it in front of every command.
- **Canvas 72.** The main is a `main-54` drawing and the sub a `sub-36` drawing. Work folders are
  `icon_set/work/side-layout-adjust-72/<id>/`.
- **Sizes.** Main presets 38 to 70 (base 54), sub presets 24 to 48 (base 36), in steps of 4. Where the 64 skill says
  the sub stays at 32 and never goes below 28, at 72 the sub stays at **36** and never goes below **32** (one step).
- **The sub is 36 (user rule 2026-10-10).** Every 72 layout keeps the sub at 36, or as drawn on its 36 canvas. Solve
  the layout with the main's sizes and the sub's position first. Shrink the sub to 32 only when it is very necessary:
  the stored layout is visibly broken, and every main size at every sensible position with the sub at 36 was tried and
  failed (say which in `--sub-smaller`). Never grow the sub past 36 either. A pair that only works with a smaller sub
  is rare: if you find yourself shrinking more than one pair in a batch, look again for a main size that works.
- **Canvas keyshapes at 72** (same rule as 64: square padding 4, the long side padding 2, HRECT short side 0.75 x 72,
  M = HRECT - 4). Main + sub together sit in one of them; the parts are anchored at its corners or sides:

  | Canvas keyshape | Painted box (x0, y0, x1, y1) | Size |
  |---|---|---|
  | SQUARE | 4, 4, 68, 68 | 64 x 64 |
  | HRECT | 2, 9, 70, 63 | 68 x 54 |
  | HRECT_M | 2, 11, 70, 61 | 68 x 50 |
  | VRECT | 9, 2, 63, 70 | 54 x 68 |
  | VRECT_M | 11, 2, 61, 70 | 50 x 68 |

  The 72 stored layouts were snapped into these on 2026-10-12 too (all 2,793 pairs).
- **Moving the main.** The same rule on the 72 canvas: a `--list main` box shifted by whole units, the same `w`, `h`,
  inside the canvas keyshape. `side_keyshape_check.mjs` accepts it as `(moved)`.
- **Convex hull.** Run `SIDE_SIZE=72 node icon_set/scripts/side_hull.mjs <dir> --current` on every pair and use it as in
  **Use the hull to adjust** in the main skill. At 72 the good ranges are sub/main 0.37 to 0.60, sub inside the main's hull
  3 to 13%, combined hull 56 to 66% of the canvas, off centre within about 3.5; the direction always equals the position.
- **Keyshapes.** The 72 parts sit on the tracer's 54 / 36 keyshapes (CIRCLE, SQUARE, portrait_L, landscape_L, tall_M,
  wide_M, slim_S, flat_S). `side_keyshape_check.mjs --list main|sub` prints the allowed boxes as before.
- **"As drawn" placement.** At 72 the engine places a part drawn on its own grid as drawn: its whole 54 / 36 canvas
  sits in the corner of the canvas keyshape and the drawing keeps its offset inside it (a flat cloud drawn 8 units down
  its 36 canvas sits 8 below the keyshape's edge). The checker accepts that placement as on the system (`sub as drawn at
  36`), next to the presets. Do not "fix" a sub only because it is not flush to the edge when it sits as drawn.
- **Prefetched folders.** `SIDE_SIZE=72 node icon_set/scripts/side_prefetch.mjs` downloads every unreviewed 72 pair
  ahead of time. A folder with `fetch.json` and no `review.json` is ready: skip `fetch` and read `fetch.json`.
- **No side-overlap review page at 72.** Skip the "Update the review page" step. The 72 review page is
  `icon_set/work/side-72/` (`/opt/homebrew/bin/python3 icon_set/work/side-72/server.py`, http://127.0.0.1:8772/), fed by
  `node icon_set/scripts/side72_fetch.mjs`.
- **The 2026-10-10 rules carry over** with 72 sizes: `lost_feature` and the search ranking that puts damaging layouts
  last; `solo/shopping-cart-empty` keeps its stored layout; a palm-up hand holding/offering the sub puts the sub at
  `tr` with the hand small, about the sub's size (try hand 44 + sub 36 first, then hand 40 + sub 36; the sub stays 36), never `tl`;
  `--gap-ok` (gaps 4.5 to 6) for that hand rule and for a main any touch would damage, resized to stand whole just clear of the sub (the stars, 2026-10-11).
- The 64 examples in the main skill (Pharmaceutical Logistics Container, Cannabis Justice Scale, database badges) show
  the rules; the numbers in them are 64 numbers.
