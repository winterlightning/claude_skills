---
name: side-layout-adjust
description: Review and adjust Pictographic 64px side-combination layouts using the existing main and sub drawings. Use for balancing, overlap, position and canvas-keyshape fixes; record each visual verdict and proposed layout. Do not redraw or swap components.
---

Generated from `.claude/skills/side-layout-adjust/SKILL.md` by `icon_set/scripts/generate_skills.py`; edit the source, not this copy.

# Side layout adjust

A side combination is a **main** (a SOLO48 icon) and a **sub** (a SUB32 icon) placed at a **position**
(`tl tr bl br` corners, `ri le bo to` sides) on a 64 x 64 canvas. The sub erases the main where they meet.
The pair is stored in `reference_parts`: the picked `icon`, the sub's `position`, and the `layout`, a
list of boxes `{paths, x, y, w, h}` on the 64 grid. Each box moves and scales a group of that part's elements. This is the
same data the **Edit layout** dialog on `primitives.html?view=side` writes.

You review and propose. You change **only the layout and position**, and only in the local work folder. Never pick another icon, never redraw a part, never edit main.svg or
sub.svg. If a pair cannot look right without redrawing a part, report that and leave the pair alone.

**Approved parts only.** Only approved icons are combined, and only pairs built from them are reviewed. A pair whose main or
sub is not approved in Icon review on its current drawing (pending, needs fix, rejected) is skipped: the review page leaves it
out, `list` (so `--next`) skips it, and `fetch` and `push` refuse it with the part's status. Report such a pair as skipped
(name the part and its status); never review its layout. Parts are approved and disapproved on production all the time, so
refresh the run (`side_audit_refresh.mjs`, below) before working through a review page.

**Keyshape system: never break it (canvas keyshape rule, 2026-10-12).** Two rules, both checked by
`side_keyshape_check.mjs`, the recorder and `push`:
1. **The combined icon sits in one canvas keyshape.** Main + sub together (their painted ink, centerline box + 2) must fit
   inside one keyshape of the 64 canvas, the CONTAINER64 set:

   | Canvas keyshape | Painted box (x0, y0, x1, y1) | Size |
   |---|---|---|
   | SQUARE | 4, 4, 60, 60 | 56 x 56 |
   | HRECT | 2, 8, 62, 56 | 60 x 48 |
   | HRECT_M | 2, 10, 62, 54 | 60 x 44 |
   | VRECT | 8, 2, 56, 62 | 48 x 60 |
   | VRECT_M | 10, 2, 54, 62 | 44 x 60 |

   There is no canvas circle. A corner pair that spans the whole canvas uses SQUARE (its parts sit 4 from the edge, not 2);
   a pair that is wide or tall overall uses an HRECT or VRECT. Production stores the keyshape a build sits in, and Icon
   review shows it; a layout that fits none shows "Keyshape unavailable" there and is never accepted.
2. **Each part keeps its own keyshape.** The main stays on its own SOLO48 keyshape and the sub on its own SUB32 keyshape, at
   a preset size in steps of 4 (main 32 to 64, sub 20 to 44), never stretched, never on another keyshape (a tall drawing
   on the circle). A preset grows or shrinks the keyshape by the same amount on both axes.
   - The **sub** sits at its position's corner or side **of the canvas keyshape** (no longer at the canvas's 2-unit
     padding): at `br` in SQUARE its ink ends at 60, 60.
   - The **main** starts at the opposite corner or side of the same canvas keyshape, and **may move** by whole units at
     its preset size, as long as the pair stays inside the canvas keyshape. The checker accepts a moved main (it reports
     `(moved)`); no need to check it by hand any more.
- `node icon_set/scripts/side_keyshape_check.mjs <dir> --list main` (or `--list sub`; add `--position br` for another
  position, `--frame SQUARE` for one canvas keyshape) prints every preset box as `x,y,w,h` with its canvas keyshape. Pass
  the main and the sub boxes from the **same** canvas keyshape.
- `node icon_set/scripts/side_keyshape_check.mjs <dir>` checks `layout.json` (`--current` for the stored layout, `--fit`
  for the nearest allowed boxes). It prints `canvas SQUARE` (or which keyshape) and each part's preset, or `canvas OFF`
  with the span when the pair fits no canvas keyshape.
- `preview <dir> --position X --auto` now moves the automatic placement into a canvas keyshape by whole units (the
  engine itself places at the padding), so it lands on the system.
- Never let a part's ink run past its canvas keyshape, never stretch a part, never step off the presets to make a check
  pass. *Pharmaceutical Logistics Container* was "fixed" by growing the main to `2,19,34,43`: its ink went out to the
  canvas edge and off its keyshape. That is not accepted, however good the contact looks.
- So the moves are: a bigger or smaller preset size for the main, moving the main (whole units, its preset box kept,
  inside the canvas keyshape), another position for the sub (`--position X --auto`), another canvas keyshape (SQUARE
  for a corner pair, an HRECT or VRECT when the pair is wide or tall), and a preset size for the sub. Move the main only
  for a reason you can see: to give the sub a clean knockout or clear space, to keep a key part out of the sub's cut, or
  to balance the canvas. Do not move it a unit at a time just to make a script number pass.
- **Box numbers written before 2026-10-12 in this skill or in memory notes are on the old padding system** (a corner sub
  at `4,4`, a main at `12,20,48,40`): they now sit 2 units off the SQUARE corner. Never type them; take boxes from
  `--list`.

**Stored layouts were snapped on 2026-10-12: review every pair again.** Every stored 64 layout was moved into a canvas
keyshape (`icon_set/scripts/side_keyshape_snap.mjs`, pushed to production): the main and the sub kept their sizes and
moved by whole units. A pair that already fitted a keyshape moved as one piece, centred; a corner pair spanning the canvas
had each part moved 2 units in, into SQUARE, so **the parts now sit closer and the sub often cuts deeper into the main**.
About 1,500 pairs gained a flag that way (`heavy_cut`, `lost_part`, `shaved`, a failed contact). The earlier reviews judged
the old layouts, so they were archived (`icon_set/work/side-layout-adjust-archive-2026-10-12-before-canvas-keyshape/`,
and in each folder's `review-history.json`) and every pair counts as unreviewed. `fetch.json` carries `snap`, what the snap
did to the pair (class, keyshape, the move, a part re-picked or placed automatically); read it in **Look**. Judge the
snapped stored layout exactly like any stored layout: keep it when it reads well, otherwise fix it in the priority flow,
inside a canvas keyshape.

**Keep the stored layout when it reads well.** Judge the stored layout by eye first. A script flag on it (a small graze,
`shaved`, `lost_part` or `erased_whole_piece` where a badge knocks out part of a repeated shape such as a database's
disks or a server's racks) is not a reason to change it. If it reads well at 64 px, it is `ok`: record it with
`--keep-stored "<what you saw>"` when a check flags it. On 2026-10-09 the user marked 38 AI fixes "stored was better":
almost all of them shrank the sub (32 to 28) to clear a script flag on a stored layout that already looked right, for
example *Baby Bottle and Medical Cross*, *Herbal Medicine Capsule* and the database and server badges.
**Engine fixes, 2026-10-11 (local combine-side.js).** The engine now draws filled dots (a wifi source dot, a
price-tag hole, eyes, a sun's dot rays) and cuts around them, keeps round parts (dots, heads) round, and draws rotated
drawings (`transform="rotate(...)"`) as drawn. A missing dot, an oval dot or an upright capsule is no longer a reason
for `redraw`: fetch the pair again (the folder is rebuilt with the fixed engine) and lay it out like any other pair.
A drawing with a transform still cannot be re-laid out (`Artwork with transforms cannot be adjusted`); keep its stored
layout if it reads well.

**The top position (`to`), user check 2026-10-11.** Of 134 pairs laid out with the sub at the top, 35 read wrong.
Before you keep or propose `to`, check by eye that:
- the sub does not sit inside the main (a person, plug, bill or helmet inside a monitor, TV or board is a container,
  never a side pair): put it at a corner beside the main (`br`/`tr`), or biting the main's corner;
- it does not erase the top of the main (a head, a roof apex, a camera body, a brain): resize the main smaller to stand
  clear below the sub, or move the sub to `tr`;
- on open or cupped hands it does not cut a fingertip: make the hands smaller so the sub sits just above them;
- on a shopping cart the sub never sits on the cart: move it to `tl` (cart 52, or 56 when nothing is cut).

**A stored layout that reads well stays, even slightly off the presets (user rule 2026-10-11).** If the stored
layout reads well by eye, record `ok --keep-stored "<what you saw>"` whatever the scripts say, and add
`--off-system-ok "<why>"` when its boxes sit a few units off the presets. Never record `redraw` or a fix only because a
check or the keyshape gate complains: the user looked at 30 such "no layout found" pairs and said most bottom-right
badges, corner suns and Wi-Fi arcs were fine as stored ("dont trust the helper script").
**`solo/shopping-cart-empty`: keep the stored layout.** On 2026-10-10 the user said the stored pairs with this main
are already good when `rebuild_change` is `main` (built from the older cart drawing): record those `ok --keep-stored`
and never propose a fix. When the pair is built from the current flat platform cart (`rebuild_change: none`) and its
`to` sub's cut erases the cart's handle (a stray dash or dot left) or the sub floats above the platform, fix it: sub to
`tl` at 32 (4,4,28,28), cart main 56 (12,20,48,40), clear 4 with the whole cart intact (*Luggage Cart with Suitcase*,
*Shopping Cart with Up Arrow*, user-approved 2026-10-10). Other cart mains are reviewed as usual: the user agreed with
the AI fixes that moved their badges to `tl`/`tr`.

**A hand that holds or offers the sub: sub top right, hand small.** For a palm-up hand main (*Hand Holding …*, *Hand
Offering …*, *Hand Supporting …*; the open hand with fingertips to the right) the sub goes at **`tr`**, never `tl`
(top-left fixes cut the hand), and the hand is **small, about the sub's size**, so the combination reads (user rule
2026-10-10). Do not grow the hand so the sub knocks out its fingertips. At 64: hand 40 + sub 32 at `tr` (the sub floats
about 4.6 above the fingertips); if the sub then floats too far (a round or pointed sub), try hand 36 + sub 36 or hand
40 + sub 36. A gap of 4.5 to 6 with nothing else wrong is recorded with `--gap-ok "<why>"` (see Record). Only when no
`tr` layout keeps the hand whole, use `ri` (*Hand Holding a Padlock*: ri, hand 40 + lock 32).

**Main first, then the sub. Keep the sub's size.** Subs are already small, so the sub keeps its stored size. *Cannabis
Justice Scale* was "fixed" by moving the leaf to `bo` at sub 24 and main 44, and the leaf's middle closed up so it no
longer read as cannabis. Only change a stored layout that is visibly wrong (a part floating apart, a real nick or graze
you can see, a key part cut away, a layout that does not show the meaning), and try in this order. Stop at the first
layout that passes the checks, reads well and shows the meaning:
The user's priority flow (2026-10-10, main moves added 2026-10-12) is **resize the main → move the main → move the sub →
resize the sub**. The main stays on its keyshape at a preset size, and may move inside the canvas keyshape the pair sits in.
1. **Resize the main.** Keep the sub at its stored size and position, and try the main's preset sizes (`--list main`):
   bigger for a real knockout, smaller to stand clear.
1b. **Move the main.** Keep the sub where it is. Move the main (at a preset size from step 1) away from or toward the sub
   by whole units, so the knockout falls on a plain part or the parts stand clear, and the whole icon looks balanced.
   The search does not try this; preview it by hand (`preview <dir> --main x,y,w,h` with a shifted `--list main` box),
   and check it with `side_keyshape_check.mjs <dir>` (a moved main passes as `(moved)` while the pair stays in its canvas keyshape).
2. **Move the sub.** Keep both sizes and try the sub at the other positions (the other corners and the sides
   `ri le to bo`), where the meaning allows it. A sub at full size on a side is fine.
3. **Move the sub and resize the main.** The sub at another position, still at its stored size, with the main's preset
   sizes for that position.
4. **Resize the sub, hard case only.** Only when the stored layout is visibly broken *and* steps 1 to 3 found nothing,
   one preset step smaller (for example 32 to 28). Never below 28, never more than one step, never to clear a script
   flag on a layout that looks right. Look at it at real size: its holes and inner details must stay open and readable.
   If it reads worse than the stored layout, keep the stored layout. A sub the AI shrank slightly without such a reason
   goes back to its stored size (32).
5. Otherwise keep the stored layout (`ok --keep-stored` if it reads well, else **No layout fits**).
`side_layout_search.mjs` ranks its candidates in exactly this order and lists smaller-sub layouts only when steps 1 to 3
found nothing.
Among layouts that pass, prefer the one closest to the stored layout: the same sizes, and the sub at full size.
`side_review_record.mjs` refuses a fix that shrinks the sub more than one step or below 28, and a one-step shrink needs
`--sub-smaller "<which positions and main sizes you tried at full size and why each failed>"`.

All work goes through `icon_set/scripts/side_layout.mjs` (Node). It composes with the same engine as the page
(`combine-side.js`), so what you preview is exactly what the page would build.

## Arguments

- `<reference_id> ...`: those pairs.
- A side-overlap review page link, such as
  `file:///…/icon_set/work/side-overlap-audit/run-2026-10-07/review.html#p3&det=problem`: the 10 pairs on that page
  of the review, in its order. Resolve it with `node icon_set/scripts/side_review_page.mjs '<link>'`. It prints the ids
  one per line and the page's names and flags on stderr. Quote the link, because it contains `&`. A link filtered by the
  reviewer's own marks (`mark=`) cannot be resolved; ask for the page's "Copy for skill" command instead.
  The page is a snapshot of production. To download every pair's current main, sub, layout and stored icon again
  (people redraw parts there), run `node icon_set/scripts/side_audit_refresh.mjs icon_set/work/side-overlap-audit/<run>`.
  It rewrites only the changed pairs (`--force` for all of them), rebuilds the page, and lists in `changed-since-review.txt` the
  reviewed pairs whose parts changed since. The page flags those as `changed since AI review`; review them again.
- `--next N [--offset K] [--hand | --auto] [--unreviewed]`: the first N built pairs from
  `node icon_set/scripts/side_layout.mjs list --limit N --offset K [--hand|--auto] [--unreviewed]`. `--hand` limits the list to pairs someone already
  adjusted by hand, and `--auto` to pairs still on automatic placement. `--unreviewed` skips pairs that already have a
  `review.json` in `icon_set/work/side-layout-adjust/<id>/`, so `--next 10 --unreviewed` always gives the next 10 pairs no one
  has reviewed, with no offset to track. Without it the list is a fixed order over every built pair, so the same offset
  always returns the same pairs, reviewed or not. Do not fetch a pair that already has a `review.json` unless the user asks to
  review it again: `fetch` resets `layout.json` to the stored layout and loses a recorded fix proposal.
- `--recheck <reference_id> ...`: review these pairs again from scratch even though they have a `review.json` (an earlier
  review broke a rule, such as the keyshape system). Fetch each one again, judge it as if it were new, and record a new
  verdict. `side_review_record.mjs` keeps the earlier reviews in `review-history.json`.

**Work the batch, not the pair.** Each step costs a round trip, so do each stage for all pairs in one command: read
every `fetch.json` together, run `side_contact_check.mjs --current` on every folder in one loop, run
`side_layout_search.mjs` on all the pairs that need a fix in one loop, look at the pictures together, and record the
verdicts in one command. Do not write or edit memory notes during a batch; report anything new in the final message.

**Finish in one go.** Work through every pair in the foreground and record each one before you end your turn. Do
not start searches or previews as background jobs and end the turn to wait for them: the batch launcher
(`side_review_terminals.sh`) takes the end of a turn as a sign the batch may be over, and pairs left unrecorded are
not reviewed. Run trial loops directly, in a shell function (see the memory notes on zsh), and wait for them.

## Per pair

1. **Fetch.** If the pair's folder already has a `fetch.json` and no `review.json`, it was downloaded in advance by
   `icon_set/scripts/side_prefetch.mjs`: do **not** fetch again, read `fetch.json` (the same summary fetch prints) and go on.
   Read all the batch's `fetch.json` files in one command. Otherwise run `node icon_set/scripts/side_layout.mjs fetch <id>`.
   It writes `icon_set/work/side-layout-adjust/<id>/` and prints the metrics. Read `snap` in `fetch.json` (what the
   2026-10-12 canvas keyshape snap did: `keyshape`, `move`, `note`, `new_flags` it added, a part `swapped` or
   `layout_reset`): `new_flags` / a contact that went from pass to fail point at where the parts now sit too close.
   Earlier reviews of the pair are in `review-history.json` (marked `superseded`); they judged the old layout.
   Check `rebuild_change`:
   - `none`: the rebuild equals the stored icon.
   - `sub`: only the drawn sub differs. Since 2026-10-07 the engine publishes the sub's original drawing instead of its
     SUB32-snapped copy, which lumped curves such as the "?" hook. The cut in the main is unchanged. Continue; a push
     also brings that fix to production.
   - `main`: the main's cut differs, so the stored icon was built some other way or from older drawings. Stop, report it,
     and do not push.
2. **Look, before any script.** Open three pictures and look at each:
   - the combination: `current@4x.png`, and `current.png` at real size (judge at 64 px);
   - the main on its own: `main@4x.png`, what it is and which parts make it readable (a jar's lip, a cart's handle);
   - the sub on its own: `sub@4x.png`, what it is and which way it points or acts (a magnifier's lens and handle, an
     arrow's head).
   (A folder fetched before 2026-10-10 may lack `main@4x.png` / `sub@4x.png`: render them with
   `rsvg-convert -w 256 -h 256 -b white -o <dir>/main@4x.png <dir>/main.svg`, the same for the sub.)
   Then say in one line **what the combination means** and how the two parts relate: the sub acts on the main
   (a magnifier inspects a document, a pencil edits it), the main holds or offers the sub (a hand with a heart), the sub
   is a status or badge of the main (a check, a lock, a plus), the sub comes out of or goes into the main (an arrow, a
   cloud upload), or the two simply belong together. Judge the stored layout against that: does it show this relation,
   or are the parts just placed at random?
   `overlap-current.png` shows how the parts meet: the kept main is black, the main ink the sub erased is red, the sub is blue,
   and cut-off crumbs are orange.
   **Convex hull: how the two parts sit together.** Run `node icon_set/scripts/side_hull.mjs <dir> --current` on every
   pair (all the batch's folders in one command). It draws each part's convex hull, the outline a rubber band would make
   around it, on `hull-current.png`: main red, sub blue, their overlap purple, both together dashed, centroids as dots,
   the canvas centre as a cross. Look at it next to `current@4x.png`. It is helper data for the layout, never the judge,
   but it shows placement problems the contact numbers miss. See **Use the hull to adjust** below.
3. **Review.** Your eye has judged; now use the scripts as a reference, not as the judge. Run
   `node icon_set/scripts/side_contact_check.mjs <dir> --current` (a failure means the pair needs a fix, see **Cut or clear,
   never a nick** below), then read the `overlap` numbers in `fetch.json` (from `icon_set/scripts/side_overlap.mjs`).
   Where a number disagrees with what you saw, look again at the picture; the picture wins, within the hard gates the
   recorder enforces:

   | Number | Meaning | Good |
   |---|---|---|
   | `flags` | `detached`, `fragmented`, `stub`, `heavy_cut`, `erased_whole_piece`, `lost_part`, `lost_feature`, `shaved`, `container` | none |
   | `penalty` | all flags added up, used to compare layouts | 0 (lower is better) |
   | `reach` | clear space from the uncut main to the sub | -4 (the sub sits on the main, a real knockout) or 4 to 4.5 (clean clear space, nothing erased). Anything between 0 and 4 nicks the main (`shaved`), even when `erased_pct` rounds to 0. Above 4.5 it floats apart (`detached`) |
   | `gap` | clear space from the kept main to the sub | 4, the clean knockout the engine makes |
   | `erased_pct` | share of the main's ink the sub erased | about 5 to 25. Above 30 it cuts too deep (`heavy_cut`) |
   | `fragments.new` | pieces of the main cut loose by the sub | 0. Any new piece is `fragmented` |
   | `fragments.stubs` | cut pieces shorter than 6 units (crumbs) | 0 |
   | `fragments.removed` | whole parts of the main erased completely | 0 |
   | `parts.cut` | each drawn element of the main (by its id in `main.svg`: `lip`, `seat`, `page`, `walls`) the sub cut into, with the share of that element erased | small shares on big outlines. `parts.lost` names every element erased 40% or more (`lost_part`) |
   | `opened` | closed outlines the sub cut open | context only, normal for a knockout |
   | `main_to_sub` | kept main ink over sub ink | about 1 to 2. Below about 0.8 the sub takes over the icon (no flag yet; judge by eye) |
   | `inside_pct` | share of the sub's ink inside the uncut main's ink box | low. 80 or more flags `container`: the main surrounds the sub |
   | `shaved` | the sub's ink does not touch the main (`reach` > 0), yet it sits inside the 4-unit cut margin (`reach` < 4) or the cut erased 1% or more | the main looks broken for no visible reason |

   Every flag is a problem to fix. A standalone fragment or crumb looks broken, and a sub that does not touch the main
   reads as two separate icons.

   **Lost parts** (`lost_part`, for example *Money Savings Jar*). `erased_pct` is the whole main, and `erased_whole_piece`
   counts only pieces that stood apart, so a part joined to the rest can vanish unflagged: the coin on top of the jar
   erased the whole `lip` and most of the neck at 27% erased with no other flag, and what was left was a round bulb,
   not a jar. Read `parts.cut` for every pair. A part erased 40% or more is lost; that layout is not `ok` unless the eye says the main
   still reads (a badge on a repeated disk or rack: `--keep-stored` or `--part-ok`), and a
   proposal that still loses it is not a fix. Shrinking the sub a little rarely saves the part; instead
   - move the sub off that part so the knockout falls somewhere harmless: another position (`--position tr --auto`,
     then adjust) puts the coin on the jar's shoulder instead of its mouth;
   - only if no low-damage knockout keeps the part, stand them clear (`reach` 4 to 4.5), shrinking the main and the sub as needed;
   - or, if no layout keeps the part, record `redraw`.
   Only when the part is meant to go (the selection-box dash the cursor points at) record it with
   `--part-ok "<why that part may go>"`. `side_review_record.mjs` refuses `ok` and `fix` with a `lost_part` otherwise.
   A fix whose parts float a little wider than clear (reach 4.5 to 5.5, `detached` the only flag) is refused unless you
   pass `--gap-ok "<why>"` (4.5 to 6). Use it where a rule here asks for it (the small palm-up hand), and for
   **a main whose shape any touch would damage** (below), never to skip a search.

   **Resize the main before giving up (user rule 2026-10-11).** When every knockout cuts a key part (a star's point, an
   ATV's wheel, a person's head) and no size lands in 4 to 4.5, shrink the main at the stored position until it stands
   whole and just clear of the sub, and record that with `--gap-ok`: a gap of 4.5 to 6 with the whole main reads far
   better than a cut one. *Add Favorite Star*: the plus badge nicked the star's arm at 54 and chopped a point off at 58
   and 62; the star at 50 stands whole 5.1 to 5.6 from the badge, which the user accepted ("just resize the main").
   Try a bigger main too, but keep it only if nothing that makes the main readable is cut.
   Before the verdict, name the parts that make the main readable (a jar's lip and neck, a bike's saddle, a phone's
   body, a house's walls) and check each one is still there in `current@4x.png` or `proposed@4x.png`.

   **The script does not decide. Your eye does.** The numbers catch contact and cuts. They miss composition, jagged
   cut edges and lost meaning, so a pair with no flags can still be bad. Never record a verdict without opening and
   looking at the pictures. Check every pair by eye against the list below, and write a verdict: `ok` or a short list
   of concrete problems.

   **Shaved cuts** (`shaved`, for example *CCPA Folded Map* or *Cloud Camera*). The engine erases the main up to about
   4 units past the sub's ink. When the sub sits *next to* the main instead of on it, that margin shaves the main's edge:
   the map's peaks are clipped under "CCPA", and the cloud's bottom line is opened above the camera. Only two layouts read
   clean: a real overlap, where the sub sits on the main and the cut is plainly a knockout, or clear space of 4 to 4.5
   units (`reach` 4, `erased_pct` 0). Fix it in the order of **Main first, then the sub**: the main's preset sizes
   first (a bigger main for a real overlap, see **Rank the contact** below, or a smaller one to stand clear), then moving
   the main, then another position for the sub, and the sub's size only as the last step. Never shift the sub, and
   never nudge the main a unit at a time only to tune `reach`.

   **Cut or clear, never a nick.** Tiny overlap and tiny clearance are not allowed. Every pair must pass
   `node icon_set/scripts/side_contact_check.mjs <dir> [<dir> ...]` (add `--current` for the stored layout). It
   passes in only two cases:
   - `knockout`: the sub sits plainly on the main. Its ink reaches at least 2 units (half a stroke) into the main's
     ink (`reach` ≤ -2), and every erased patch is a real chunk cut through the full stroke.
   - `clear`: nothing is erased, and the parts are **at least 4** and at most 4.5 units apart. 3.9-something is not
     accepted, even when nothing shows: the engine's cut margin is 4, so below it the main is shaved. "Nothing erased" is
     strict too: when the sub does not reach the main, any erased sliver of 0.1 unit² or more fails as a nick, even one
     pixel deep. On the presets, `reach` moves in steps (one size step is 4 units), so try each nearby main and sub size,
     and moving the main by whole units; never trim a part or shift the sub to land in 4 to 4.5.

   Everything else fails:
   - a nick: a speck or a sliver shaved off a stroke's edge;
   - tiny clearance: the sub does not touch the main (`reach` > 0), but the cut margin erases it anyway;
   - tiny overlap: the sub only grazes the main (-2 < `reach` ≤ 0);
   - `detached`: the parts are more than 4.5 apart.

   **Rank the contact: low-damage knockout, then clear, then never a damaging knockout.** Overlap is not good in itself.
   It is good only when the main loses almost nothing.

   **You rank it by looking, not from the script.** Do not trust the numbers to find damage. `flags`, `erased_pct`,
   `parts.cut` and a passing `side_contact_check.mjs` are hints and hard gates only. A pair with no flags and a passing
   check can still be rank 3, and the script cannot see jagged edges, a cut through the one detail that carries the
   meaning, or a main that no longer reads. For every pair, stored layout and every proposal alike:
   - Open the pictures and look: `current@4x.png` (or `proposed@4x.png`) for the shape, `overlap-current.png`
     (or `overlap.png`) for exactly what was erased (red) and the crumbs (orange), `contact.png` for the cut edges, and
     `current.png` / `proposed.png` at real size, as a person sees it at 64 px.
   - Find the damage yourself: follow every stroke of the main where the sub meets it. Name what was cut (which part,
     how much of it) and how each cut edge looks: one clean bite, or notches, stair-steps, several small bites, thin
     slivers left between the sub and the main, a stroke ending in a crumb.
   - Cover the sub in your mind and ask whether the main alone still reads as the same thing at 64 px. If it does not,
     the knockout is rank 3, whatever the numbers say.
   - Write what you saw in the note. A note that only repeats the numbers ("no flags, erased 12%") is not a review.

   Judge every layout in this order:
   1. **Best: touching with low damage.** The sub overlaps the main in a real knockout (`reach` ≤ -2), and the main
      keeps its meaning and its clean look. The cut takes a small, plain chunk: the end of a stroke, a corner, or a
      stretch of a long plain side. Nothing that makes the main recognizable is touched (a screen, a face, a lip, a
      handle, a key detail). Only a small share of the main's ink is gone, and every cut edge looks deliberate. Try to reach this first by
      moving or resizing the sub (and the main if needed), and by trying another position where the knockout falls on a
      plain part.
   2. **Next: separate.** If no knockout stays low-damage, stand the parts clear at 4 to 4.5 units with nothing erased.
      A clean separation is better than any overlap that hurts the main.
   3. **Worst: a damaging knockout.** The parts combine, but the main loses meaning or looks jagged. A key part is cut
      or gone, the main breaks into pieces, too much ink is erased, or the cut leaves ragged edges: notches, stair-steps,
      several small bites, or slivers between the sub and the main. Never record this as `ok` or `fix`, even when the
      contact check passes and no flag shows. Move to rank 2 instead.
   - A stored `clear` is `ok` unless a rank-1 knockout clearly exists. Then record `fix` with that knockout. A stored
     knockout that is rank 3 gets `fix` with a rank-1 knockout if you find one, otherwise with clear space.
   - The note names the rank and why, for example "rank 1: the cloud bites the monitor's top corner, screen intact" or
     "rank 2: every knockout cut the jar's lip, stood clear at 4.2".

   **No layout fits.** Search only the presets: the main and sub sizes from `--list`, and the other sensible positions.
   - If the stored layout is on the system and reads well by eye, it is `ok` (`--keep-stored` when a check flags it), or a
     `fix` to a clearly better preset layout that keeps the sub's size.
   - Otherwise, record `fix` with the best preset layout that passes the contact check and is rank 1 or 2, found in the
     order of **Main first, then the sub**.
   - If no preset layout passes and reads well, first resize the main to stand just clear with `--gap-ok` (above). Only
     if that also fails, keep the stored layout: record `redraw` with the note "no preset layout
     works:" and what each try did (for example "main 48 nicks the corner, main 44 floats at 5.9, br erases the lip").
     Never step off the presets to make it pass.

   `contact.png` shows the erased chunks in red and the nicks in magenta. A stored layout that fails is `ok` only with
   `--keep-stored`, when it reads well by eye and every fix would read worse (see **Keep the stored layout when it reads well**).
   When the sub only grazes or shaves the main, first push it into a real overlap. Shrink or move the parts apart to
   clear space only if no low-damage knockout exists. Never stop halfway. `side_review_record.mjs` refuses `ok` for a stored layout that fails the check
   and `fix` for a proposal that fails it.
   - **Hierarchy.** The main reads first and stays large. Its ink is usually 40 to 46 on its long side. The sub is clearly
     secondary, with `sub_to_main` about 0.55 to 0.75. A sub as big as the main, or a sub too small to read, is a problem.
   - **Placement.** The sub sits in its position's corner or side, flush to its canvas keyshape's edge (at `br` in SQUARE
     its ink ends at 60, 60). The main shifts toward the opposite corner or side, so the empty canvas is not all on one side.
   - **Overlap.** The sub may cut into the main, and the engine knocks the main out around the sub. The cut must not destroy
     a part of the main that the meaning needs (a screen, a face, a key detail). If it does, shrink or move the
     main away, or move the sub.
   - **Balance.** The combined ink looks centred overall and no large empty pocket appears. Neither part is squeezed
     out of proportion: each part stays on its own keyshape (see **Keyshape system**).
   - **Bounds.** Main + sub stay inside one canvas keyshape (`side_keyshape_check.mjs` prints `canvas SQUARE` or another;
     `canvas OFF` is never accepted).
   - **Clean contact.** Where the parts meet, there is a clear knockout (the sub on the main), or clear space when no knockout stays low-damage. A knockout that costs the main its meaning or leaves it jagged is worse than clear space.
     A main that is clipped where the sub does not touch it looks like a mistake (`shaved`). So does a tiny nick, even
     where the sub does touch: a cut is either plainly a knockout or absent.
   - **Side, never container.** A side combination stays a side combination: the sub sits at its corner or side and
     reaches the canvas edge, with the main beside it. Never move or scale the sub into the main's interior (a symbol
     inside a shield, a box, a screen, a bubble), and never grow the main around the sub, so that the main reads as a
     container hosting the sub. That is a container combination, a different family built another way. If a pair only
     reads well that way, record `redraw` with a note that it should be a container combination; never propose it as a fix.
     `side_overlap.mjs` flags it as `container` (80% or more of the sub's ink inside the main's ink box), and
     `side_contact_check.mjs` fails it, so `side_review_record.mjs` refuses it as `ok` or `fix`. Usual way out: a corner
     position with the main whole beside the sub and 4 to 4.5 units clear (the remote under a house goes to `br`, the
     diagram on a head goes to `tr` as its thought). To find reviewed pairs laid out as containers, run
     `node icon_set/scripts/side_container_scan.mjs` (every reviewed folder, or the folders you name). It lists stored
     layouts and proposals that are containers and marks `WRONG` an `ok` or `fix` review that keeps one; review those again.
   - **Meaning: the layout must show what the combination means.** This is the first thing the layout is for, not a
     tie-breaker. Lay the parts out so the relation you named in **Look** reads at a glance, never just where they fit:
     - **Overlap only when it means something**: the sub sits on or acts on the main (a magnifier over the document it
       inspects, a pencil on the page it edits, a badge pinned on the item). The overlap is a clean knockout on a plain
       part of the main. If the relation is not "on top of" or "acting on", stand the parts clear (4 to 4.5) instead:
       no overlap at all is better than an overlap that means nothing.
     - **Direction and role**: a sub that acts points its working end at the main (the lens over the main, the handle
       pointing away, never the handle stuck into it); a held or offered sub sits above the palm (sub `tr`, hand small);
       an arrow sits on the side it points to; a status or badge sits bottom right; a notification top right.
     - **Hierarchy**: the main reads first; the sub is clearly secondary but big enough to read.
     Change the position when another one shows the meaning clearly better, and say in the note how the chosen layout
     shows the meaning (for example "the lens sits over the page's text, handle out to the corner: reads as search
     this document").
   **Use the hull to adjust (helper data, 2026-10-12).** Stored layouts the user's reviews kept as `ok` (about 360 pairs
   at 64 and 72) sit in these ranges, 10th to 90th percentile. A number outside them is a hint to look again, and it
   tells you which way to adjust; it is not a verdict on its own:

   | `side_hull.mjs` number | Good layouts | Outside the range, try (in the priority flow) |
   |---|---|---|
   | `direction` (sub from the main's centroid) | equals the position, always | the sub reads from the wrong side: check the meaning, move the main so the sub sits at its position |
   | `sub_to_main` (hull areas) | 0.40 to 0.65 (72: 0.37 to 0.60) | below: the sub looks lost, try a smaller main first (never grow the sub past its size); above: the sub competes, try a bigger main |
   | `sub_in_main_pct` (sub hull inside the main hull) | 3 to 14 | above about 20: the sub sinks into the main's silhouette, drifting to a container, so shrink or move the main away; 0 with a `hull_gap`: the parts read apart |
   | `hull_gap` | 0 (the hulls touch or overlap, even for a clear layout) | any gap reads as two icons: grow or move the main toward the sub |
   | `combined.canvas_pct` | 54 to 66 | below about 50 the pair looks small and sparse: a bigger main; above about 68 it is crowded: a smaller main |
   | `combined.off_centre` (x, y) | each within about 3.5 | the pair leans to one side and leaves an empty side: move the main toward the centre by whole units, or resize it |
   | `main.solidity` / `sub.solidity` | main about 0.35 to 0.55 | low solidity (a hand, a cart, an open book) has a pocket in its hull: a sub may sit in the pocket without touching ink; that is fine when it means holding or carrying |

   How to use it:
   - Read the stored layout's hull numbers with the contact numbers, and note which are out of range and which way they
     point (for example "sub/main 0.24, off centre -3,-3: the sub is lost and the pair leans top-left").
   - Choose the adjustment the hull points to, inside the priority flow: resize the main, move the main, move the sub,
     resize the sub. A hull that says "sub too small" means a smaller main, never a bigger one, even when the search ranks
     a bigger main first. *Electric Vehicle Engine Symbol* (72): the search's main 58 knocks out cleanly but leaves sub/main
     0.24 and the pair leaning top-left (off centre -2.6,-3); main 50 floats apart at every sub box, while main 54 moved
     +4,+4 (8,8,46,34) knocks out just as cleanly, sub/main 0.29, off centre -0.7,-1.1, and reads more balanced.
   - A slim or thin sub (a bolt, a pencil, an exclamation mark, a slim_S keyshape) has a small hull, so its sub/main stays
     below the range at every main size. Judge it against the sub's own shape, not the table, and use the hull mainly for
     balance and the gap.
   - For a fix, preview the two or three best candidates from the search (and any moved-main layout you try), run
     `side_hull.mjs <dir>` after each preview, and pick the one that reads best by eye with the most hull numbers in range.
     Name the hull numbers before and after in the note.
   - Never break a hard rule to bring a hull number into range: the keyshape presets, cut or clear, the lost-part check and
     the sub's size rules still come first. A pair can read well with one number outside (a long flat main, a tall bottle);
     then keep it and say so in the note.

4. **Adjust.** Do this only if the stored layout is visibly wrong. **Search first, do not preview by hand:**
   `node icon_set/scripts/side_layout_search.mjs <dir>` tries every preset layout in one run (every canvas keyshape, every
   main size, every sub position, the sub at its stored size and one step smaller; about a minute a pair). Each candidate
   line names its canvas keyshape. It keeps those that pass the contact
   and keyshape checks and ranks them in the order of **Main first, then the sub** (main resized, then sub moved, then sub moved with the
   main resized, then sub smaller, which comes last). It writes `search.png`, the stored layout and the best candidates side by side and numbered.
   Look at `search.png` once, pick the candidate that best shows the meaning you named in **Look** and keeps the
   main whole (the ranking is a hint from the numbers; the first one is not always right). A candidate that damages the main (`lost_feature`, `lost_part`, `erased_whole_piece`, `fragmented`,
   `stub`) ranks after every candidate that keeps the main whole, even a resized one: `lost_feature` means the sub
   chopped off a run of a stroke between turns, such as a cart's handle and riser (*Luggage Cart with Suitcase*: the `tr`
   knockout took the handle; the right fix was `tl` with the cart at 56). Still judge by eye what no number sees: a sub
   whose handle or arrow points into the main (*Shopping Cart with Magnifying Glass*: `tl` pushed the magnifier's handle
   into the basket; the right fix kept it `br` and resized the cart to 40). Then preview it with the command the search printed (and the next one or two when the hull numbers
   disagree with the ranking, see **Use the hull to adjust**), run `side_hull.mjs <dir>`, look at `proposed@4x.png` and
   `hull.png`, and record. If no candidate reads better than the stored layout, keep the stored layout. Do not run your own loops over
   positions and sizes; the search already did. Previewing by hand (below) is only for checking the pick.
   Each preview edits `layout.json` and renders `proposed@4x.png` and `compare.png` (current | proposed):
   - Resize a whole part to a preset: `preview <dir> --main x,y,w,h` and/or `--sub x,y,w,h`, with boxes copied from
     `side_keyshape_check.mjs <dir> --list main` / `--list sub` (for the position in `layout.json`). They always scale the
     part's stored groups (`base-layout.json`) in one step. Never type a sub box that is not in the list.
   - Move the main: `preview <dir> --main x,y,w,h` with a `--list main` box whose `x` / `y` you shifted by whole units
     (keep `w`, `h`), staying inside the canvas keyshape. `side_keyshape_check.mjs` accepts it as `(moved)`.
   - Change the position: `preview <dir> --position br --auto` (automatic placement, moved into a canvas keyshape), then
     list the boxes for the new position with `--list main --position br` and pick sizes from it (main and sub from the
     same canvas keyshape).
   - Never edit `layout.json` by hand and never move single groups inside a part: that breaks the keyshape system.
   - After every preview, run `side_keyshape_check.mjs <dir>` (must pass, except for a moved main, see above) and `side_contact_check.mjs <dir>` and read its `overlap` numbers, `contact.png`, `overlap.png`, `compare.png` and `proposed.png`. The check must pass. Aim for no flags and
     a `penalty` lower than the stored one. A lower penalty never excuses a layout that looks worse. To fix
     `shaved`, follow **Main first, then the sub** as described above. To fix `detached`, grow the main by a preset step into a
     real overlap, then try another position for the sub; only if no low-damage knockout exists, use the size that stands
     them clear. To fix `fragmented` or `stub`, try another position so the knockout falls on the end of a stroke or a
     whole side, not across a thin part. `heavy_cut` and `erased_whole_piece` mean a smaller main preset or another sub
     position first, the sub's size last. `lost_part` means another position or the clear size (see **Lost parts**).
   - The search covers the order of **Main first, then the sub**; pick from it before you give up. If nothing is clearly better than
     current, follow **No layout fits**.
5. **Record the review.** Record every pair you reviewed, including the ones that look fine:
   - The recorder checks the keyshape system as well as the contact: it refuses an off-system layout.
   - Looks fine: `node icon_set/scripts/side_review_record.mjs <dir> --verdict ok --model <your model id> --note "<what you saw>"`.
     The note says briefly why it is fine, for example "The leaf tucks into the cupcake with a clean knockout." `layout.json`
     must still be the stored layout, so record before any preview, or preview the stored boxes back first.
   - Needs a fix: after the final preview, `… --verdict fix --model <id> --note "<what was wrong, what the fix does and how it shows the meaning>"`.
     The script measures before and after from `base-layout.json` and `layout.json`, and points at `compare.png` and
     `proposed@4x.png`.
   - Cannot be fixed by layout: `… --verdict redraw --note "<which part needs redrawing and why>"`. Leave the layout as stored.
   It writes `<dir>/review.json`, which the side-overlap review page shows on the pair's card: "Reviewed: looks OK", or
   "Reviewed: needs a fix" with the stored and proposed pictures and the before and after numbers.

At the end of the run:
- **Update the review page.** For each side-overlap run folder whose `review-pairs.json` lists one of these pairs (for example the
  run the link came from), run `/opt/homebrew/bin/python3 icon_set/work/side-overlap-audit/<run>/review.py`. Tell the user to reload the page.
- Give a table of the pairs: concept, flags and penalty before → after, verdict (looks OK / needs fix / needs redraw), and the
  change proposed (or none).

To review the next 10 pairs no one has looked at yet, use `--next 10 --unreviewed`, or a link filtered to unreviewed pairs:
`review.html#p1&ai=none`. Pairs drop out of that filter as they are recorded, so page 1 is always the next batch.

To check contact on any work folders, run `node icon_set/scripts/side_contact_check.mjs <dir> ...` (`--current` for the stored layout, `--json` for the details). It exits 1 if any folder fails, and accepts `--clear-min`, `--clear-max`, `--overlap-min`, `--chunk`, `--noise` (edge peel for knockouts) and `--speck` (smallest sliver counted when the parts stand clear).

To see the two parts' convex hulls (placement, direction, hierarchy, balance), run
`node icon_set/scripts/side_hull.mjs <dir> ... [--current] [--json]`.

To measure any work folder on its own, run `node icon_set/scripts/side_overlap.mjs <dir>`. It accepts `--min-piece`, `--detach`, `--heavy-cut`
and `--lost-part` (default 40) to change the limits.

## Do not

- Do not propose fixes for pairs whose fetch failed or whose `rebuild_change` is `main`.
- Do not change pairs whose state is `unbuilt` or `stale`, or that have a part with no icon. Report them instead.
- Do not shrink the sub to clear a script flag on a stored layout that reads well; keep it (`ok --keep-stored`). Never
  shrink it more than one step or below 28, and only after other positions and main sizes failed on a visibly broken layout.
- Do not move or nudge the sub off its preset box, and do not stretch or re-shape either part off its keyshape (see
  **Keyshape system**). The main may move by whole units at a preset size, inside the canvas keyshape.
- Do not let main + sub spread past every canvas keyshape (`canvas OFF`), and do not type box numbers from before
  2026-10-12 (old padding system); take boxes from `--list`.
- Do not turn a side combination into a container combination: the sub never moves inside the main's outline, and the main
  never wraps around the sub (see **Side, never container**).
