---
name: corner-review
description: Review the SHARP output of the 48x48 icons after corner_processing has run and decide, corner by corner, whether each corner is sharp or round - nothing else. Uses corner_processing/review/next_batch.py for batches, judges each sharp icon the way a person would at 48 px (meaning and balance), and records a round-or-sharp decision per icon with its drawing. The AI decides every icon itself; nothing is left for a human (no needs-user). One rule for every corner: round only where the object is round; 70 deg and wider stays a plain sharp point; a narrow point stays full unless it runs into ink, fills an opening or reads as a stray spike - then its tip is cut flat (--cut), never rounded. Never moves a corner, changes an angle, redraws the input or touches the round output; never publishes. Use when asked to review corner processing results, check the sharp output, or decide which corners are round or sharp. Hand-authored; edit this file directly.
---

# Corner review — round or sharp

`claude_skills/corner_processing/` turns every approved SOLO48 icon into an **all sharp** version
(`sharp_corner_processing.py`, rules in `core/toggle.py`). One setup cannot fit every icon: some corners it makes
sharp should stay round, and some it leaves round could be sharp.

**Your only decision: for each corner of the sharp output, is it sharp or round?** You look at the sharp icon as a
person would at 48 px and decide per corner. That is all.

**You decide every icon. A human takes no action in this review**: there is no needs-user and no "report" for
someone to fix. When you are unsure, the answer is sharp (§2).

You never:
- move a corner, pull a point back or change an angle;
- round a corner unless the object is round there (§2 step 1), cut a corner of 70° or more, or cut a narrow
  point that stands clear (§2 steps 2-4);
- redraw or propose redrawing the input drawing;
- review or change the round output (its plate on the sheet is only a reference);
- edit the outputs, the inputs, `core/toggle.py` or `status.json` by hand, or publish (`core/publish.py` is the
  user's step).

## 1. Take a batch

Everything runs from `claude_skills/corner_processing` with `/opt/homebrew/bin/python3`. Set `CORNER_REVIEWER` to
your model ID.

```bash
cd corner_processing
export CORNER_REVIEWER=<your model id>
/opt/homebrew/bin/python3 review/next_batch.py --count 10            # the next todo icons
/opt/homebrew/bin/python3 review/next_batch.py --icons north-east.svg  # or named icons
```

For each icon it writes `review/batches/<batch>/<icon>.png`, the **sheet** (input · round · sharp at 256 px, the
same at 48 px, and mirror overlays for symmetric icons), and an entry in `batch.json` with `sharp_log` (each corner
of the sharp output: `sharpened`, `kept round` with why, `kept sharp`, `tip cut`) and `paths.sharp`.

## 2. Decide each corner: one rule for every icon

Read the sheet (Read tool): the 48 px sharp icon first, then the big sharp plate, always against the input. Take the
angle of each corner from `sharp_log` (or measure it). Then give **every corner** of the sharp output one of four
answers by the steps below, **in order - the first step that applies decides**. The sharp output exists to be
sharp: when no step clearly applies, the answer is **sharp**.

| Step | When | Answer |
|---|---|---|
| 1. Meaning | the real object is round there (list below) | **round** (`--round`, or `ok` if the processing kept it) |
| 2. Wide | the corner is **70° or wider** | **sharp**, a plain point: never cut, never round |
| 3. Narrow and it misbehaves | under 70° **and** the full point does one of (a)-(c) below | **cut** the tip flat (`--cut`) |
| 4. Everything else | under 70°, standing clear | **sharp**, a full point |

**Step 1, meaning - round only when a sharp corner would change what the object is.** The round output already
exists; a round in the sharp output that only repeats it is pointless (user, 2026-10-09, empty-rounded-square-shape:
"the sharp output is already good, why make it round - there is no point making the sharp corner the same as the
round"). Round is needed only for: a book's spine and page curl (book-close); a scroll's or paper's roll curl; a line that bends as a path or tube (a winding or S arrow, a
cable, smoke or steam curl, a rope loop, a trunk, a neck, an intestine), where sharp corners turn the bend into
steps. **Not a reason:** a name that says "rounded" or "soft"; rounded squares and rectangles; phones, consoles,
bottles, jars, pouches, socks, soap, chairs, vehicles, buildings; clouds; avatar shoulders and bodies; "organic";
hiding a spike; balance; "it was round in the input"; bags of any kind (user, 2026-10-09, handmade-bag: "this
looks the same as the round, we don't want this kind of identical"); phones (phone-with-down-arrow). When in doubt,
sharp. **A sharp icon that looks the same as the round one is worth a second look, not an automatic fix:** where the
processing kept a corner round ("too large for a corner", "curved side", ...), make it a point with `--sharp X,Y` only
when the icon still looks right and keeps its meaning - a box, frame, die, plain square, device, bag, bell, bed or
vehicle side. Leave it as it is when the curve is part of what the object is or sharpening breaks it (user,
2026-10-09: "not everything needs to be sharp; only sharpen if the icon looks ok and does not break its meaning"):
cups and mugs (wide-coffee-mug-with-rounded-base keeps its round base), jars, bottles, sacks, a file's dog-ear,
curved arrows, people and avatars (woman-figure), faces (winking-smiling-face), animals, logos, books and scrolls.
`reports/compare_round_sharp.py` lists every icon sorted by how identical its sharp and round outputs are.
**Decide per point, not per icon:** a round goes only on the corner whose own meaning needs it; every other corner of
the same icon stays sharp (user, 2026-10-09: "only make round if the icon needs it for the meaning of that point" -
elephant-spraying-water keeps its trunk curve but its back-to-leg corner goes sharp).

**Step 3, narrow points - cut only when the full point:**
- (a) **runs into other ink**: touches, or comes within about 1 u of, a stroke, dot or ring it did not touch in the
  input (the ribbon's V into the medal ring, an ECG peak into its ring, a play triangle at its frame);
- (b) **fills an opening**: closes a counter, a curl or the space between lobes (the wedges in flexing-torso's
  curls, cusps that close a flower's centre, the chamomile's petal cusps);
- (c) **reads as a spike that is not part of the object**: a spur, fang or flame where the object is soft (the
  penguin's head join, the tsunami's curl, the dog-poop swirl, a moustache's centre cusp).

A point that pokes into a hole or ring is cut **flush with the hole's edge** (`--cut X,Y:0`), not the default 2 u,
and this holds even for a join of 70° or more: a default cut still leaves a nub inside the hole (user, 2026-10-09,
holly-leaves-and-berries: "wrong cut tips near the circle hole" - the 31°, 45° and 79.6° joins on the top berry are
all cut flush). A point standing in clear space inside the keyshape is the object's own tip and stays full
(browser-window-bookmark's ribbon tails, V-notches, zigzags, crotches, noses, flares).

A point that **is** the object's own tip stays full however long it is: ears, tails, beaks, arrow and cursor heads,
bolts, crown, star and merlon points, moon horns, blades, ECG peaks standing clear. A point past the keyshape is
already cut by the processing (`tip cut` in `sharp_log`).

**Groups get one answer.** Mirrored corners (both barbs, both ears, both shoulders) and joins repeated around one
shape (petal cusps, scallops, star points) are decided together: all round, all sharp, or all cut - never one barb
cut and its partner full, never one shoulder round. When the keyshape shaved one of a pair flat and left the other a
full point, shave the other the same way (`--slice X,Y:A,B`; `:rot` for point symmetry, `:move` for a repeated
shape). The one exception to step 2: in a repeated group where the narrow members must be cut, siblings just over
70° may be cut alike (flower-b31296d9).

**Never:** round a corner to fix a sharp problem (cut it, step 3); cut a corner of 70° or more unless it pokes into a
hole (above); give mirrored
corners different answers; move a corner or change an angle. A big round (more than r 6) is a designed curve: it
stays round unless it clearly reads as a corner of the object.

Things that are not corners are not your decision and do not stop one: dots drawn as zero-length strokes that
rsvg drops at 48 px (look at the 256 px plate), and a keyshape sliver you cannot fix by making a corner round or
sharp. Mention them in the note and decide the corners.

## 3. Reference examples (decided)

They show the kind of result wanted, not a template; decide each icon from its own drawing.

- `examples/book-spine.png`: **book-close** (manager, 2026-10-08). The spine side stays **round** (the top-left
  corner and the curl where cover and pages meet); the fore-edge corners are **sharp**. All four sharp read as a box;
  only the curl round looked like a leftover.
- `examples/handbag-with-clasp.png`: **handbag-with-clasp** (user, 2026-10-08). The soft body's four big corners stay
  **round**; only the small hard clasp is **sharp**. The processing already did this: `ok`. Rejected: a flat bottom
  (bottom corners sharp), which reads as a shopping bag.
- `examples/award-ribbon-cut-tip.png`: **award-ribbon-badge** (user, 2026-10-08). The ribbons' inner V at 24,30 drawn
  sharp spikes up into the medal ring. Wanted: keep it sharp and **cut the tip flat** (`--cut 24,30`), leaving a
  clean gap under the ring; tails and outer corners stay as processed. Rejected: the V rounded back to the input's
  round join ("in sharp we should not round").
- `examples/chamomile-cut-tips.png`: **chamomile-flower** (user, 2026-10-08). The eight cusps between petals drawn
  sharp grow inward until the petals' inner edge becomes a square. Wanted: all eight kept sharp with their tips
  **cut flat** (`--cut` on each cusp, all alike), so the petals read separate again. Rejected: all eight rounded.
- `examples/flower-cut-group.png`: **flower-b31296d9** (user, 2026-10-08). Five cusps between the petals: the bottom one
  (53°) spikes, the other four are wider. Wanted: all five kept sharp with their tips **cut flat alike**
  (`--cut` on each). Rejected: only the bottom one cut and the four wider ones rounded ("not fixed").
- `examples/buckingham-keep-sharp.png`: **buckingham-palace-reference** (user, 2026-10-09). The merlon points of the
  two side towers grow when sharp but stay inside the keyshape and clear of other strokes. Wanted: all **full
  sharp points** (`ok`, the processing's output). Rejected: the four tips cut flat.
- `examples/broccoli-all-sharp.png`: **broccoli-crown-and-stalk** (user, 2026-10-09). Four cusps where the florets
  meet: wanted all four **full sharp points** (`ok`). Rejected: the top two cut and the bottom two left round -
  no meaning makes them round, and a cut is not needed where the point stands clear.
- `examples/arrows-even-barbs.png`: **opposing-angular-corner-arrows** (user, 2026-10-09). The small arrowhead's two
  barbs: wanted both **full sharp points** (`ok`). Rejected: one barb cut, the other full ("not the same cut
  tips").
- `examples/flexing-torso-no-rounds.png`: **flexing-torso** (user, 2026-10-09). The arm joins under the fists drawn
  sharp become wedges that fill the curl openings. Wanted: every corner **sharp**, the two wedges **cut flat**
  (`--cut 13,20 35,20`). Rejected: four joins rounded ("a sharp icon with a lot of round corners is bad").
- `examples/sharp-first-decisions.png`: seven icons decided with the user on 2026-10-09, one rule each (input |
  rejected | wanted): **koala-head** cheek joins (90°) sharp, not round; **gamer-with-controller** 90° body corners
  plain sharp, never cut; **plain-glue-bottle-with-rounded-nozzle** one shoulder round broke the symmetry, both
  sharp; **penguin-looking-down** 37° head join and **tsunami-waves** 44° curl cusp spike, so their tips are cut, not
  rounded; **woolly-lamb-front** 106° legs sharp and the 60° joins cut, no rounds; **seated-kitten** the cat's round
  back is a meaning, the round stays.
- `examples/arrow-shaved-pair.png`: **arrow-broad-rounded-bend-down** (manager, 2026-10-08). The keyshape shaved the
  right wing flat and left the left wing a full point. Wanted: the left wing shaved flat the same way
  (`--slice 22,32:42,32`), so both wings are sharp and even. Rejected: both wings round, "rounding stuff instead of
  just flat slicing".

## 4. Record it

```bash
# the processing already chose right for every corner
/opt/homebrew/bin/python3 review/record.py <batch> <icon> --status ok --note "<what you saw>"

# some corners should change: build the drawing, then record it
/opt/homebrew/bin/python3 ../.claude/skills/corner-review/round_or_sharp.py \
    review/batches/<batch>/batch.json <icon> --round 8,4 8,44 --sharp 40,4 --cut 24,30 --slice 22,32:42,32
# -> {"paths": {...}, "missing": []}    missing must be empty
/opt/homebrew/bin/python3 review/record.py <batch> <icon> --status proposed --decision "round or sharp" \
    --paths '<paths from round_or_sharp.py>' \
    --corners '[{"p":[8,4],"decision":"keep","why":"spine, round"}, {"p":[40,4],"decision":"corner","why":"fore-edge, sharp"}]' \
    --note "<which corners are round, which sharp, why it reads and is balanced>"

```

- `--round X,Y` puts a corner the sharp output made sharp back to the input's own round (same radius, same end
  points); at a plain line join (no arc in the input, not in `sharp_log`) it draws a small round fillet, the
  input's round join. `--sharp X,Y` turns a corner the sharp output kept round into a point at its apex. X,Y is the
  corner's apex as the sheet and `sharp_log` give it, or the join point in the path.
- `--cut X,Y[:R]` keeps the join at X,Y sharp but cuts its point flat, square to the corner's bisector, R u past the
  join (default 2, where the input's round join reached; the shortest cut is 1.6 u). It works on straight, arc
  and curve arms (the arms are trimmed a little and joined by a short straight edge), so a cusp between two arcs
  is cut too. Use it for every point that grows too far (rule 4).
- `--slice X,Y:A,B` shaves the point at X,Y flat with a copy of the keyshape cut on its partner A,B (the `tip cut`
  in `sharp_log`), mirrored so the pair matches; `X,Y:A,B:rot` for a point-symmetric pair (a parallelogram),
  `X,Y:A,B:move` for a repeated shape (a second triangle). It changes the keyshape clip (`keyshape-cut` in the
  paths), not the strokes. Example: arrow-broad-rounded-bend-down `--slice 22,32:42,32`.
- In `--corners`, `keep` = round, `corner` = sharp, `cut` = sharp with its tip cut flat, `slice` = shaved like its
  partner; one entry per corner you
  change.
- Look at the new drawing before recording: `preview.py` (same arguments plus an output PNG) draws input · sharp
  now · proposed and prints the same JSON:
  `python3 ../.claude/skills/corner-review/preview.py review/batches/<batch>/batch.json <icon> /tmp/x.png --round 8,4`.
  The review page shows it beside the current sharp plate.

Release an unfinished batch with
`python3 review/next_batch.py --release <batch>`.

## 5. Report

Rebuild the page: `/opt/homebrew/bin/python3 reports/make_toggle48_report.py` (served at
http://127.0.0.1:8749/toggle48_report.html; filter **AI proposed**). End with a short summary: the batch, how many
`ok` / `proposed`, and for each proposed icon which corners are round and which sharp.
