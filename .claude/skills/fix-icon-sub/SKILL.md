---
name: fix-icon-sub
description: Repair Pictographic sub icons that were already generated with /icon-sub but still fail validation, producing a new variant that passes the strict 32x32 SUB32 gate while keeping the original reference's meaning and core visualization. Use when given an original reference plus one or more current sub icons that fail validation. Records a "cannot-fix" in the Python model when no meaning-preserving 32x32 drawing passes. Hand-authored; edit this file directly.
argument-hint: <original reference SVG path or UUID> <current sub icon IDs or Python files>
---

# /fix-icon-sub — make a failing sub icon pass the strict 32×32 gate

Request: $ARGUMENTS

The maintained source is `.claude/skills/fix-icon-sub/SKILL.md`; regenerate its
Codex and portable copies with `icon_set/scripts/generate_skills.py`. Run every
command from the `claude_skills` directory containing `icon_set/`.

## What you get and what you must return

**Input:** one original reference (an SVG path or source UUID) and the current
sub icon(s) generated from it (icon IDs, Python module paths or published SVGs).
Work per **original**, not per icon ID: one original often has several sub
models (`-v2`, `-v3`, ...), all sharing its `SOURCE_ICON_ID`. Always gather
all of them with `check --source <uuid>`, even when only one icon ID was given.
When only an icon is supplied, read the UUID from its module's
`SOURCE_ICON_ID`. If neither the reference nor the icon can be resolved, ask.
Models of the same original in other families (e.g. `symbol/`) are ignored.

**Output, one of two per original:**

1. **Fixed** — a new sub variant that passes
   `python3 icon_set/scripts/fix_icon_sub.py check --icon <new-id>` (exit 0),
   is published by `build.py --family sub`, and still shows the original's
   meaning. The outcome is recorded on every reviewed current icon.
2. **Cannot fix** — no meaning-preserving drawing passes. The blocker is written
   into each current icon's Python module with `fix_icon_sub.py record
   --status cannot-fix`. Nothing is weakened, deleted, or published as passing.

## The strict 32×32 gate

This skill's target is the plain `SUB32` system and it overrides, for this
task only, the larger-canvas and compact-stroke allowances in
`icon_set/skills/icon-design/sub-reference-policy.md`. A fix passes only when
all of these hold (the `check` subcommand tests every one):

- family `sub`, profile `SUB32`, canvas and SVG root exactly 32×32
  (`viewBox="0 0 32 32"`); no `canvas_width`/`canvas_height`, tall base, or
  natural-width text canvas;
- every stroke is 4 — no `STROKE_WIDTH = 2`, `PATH_STROKE_WIDTHS`, or new
  `COMPACT_EXCEPTION`;
- a real keyshape (not `FREE`), matched exactly per
  `Keyshape.<TOKEN>.bounds_for(Profile.SUB32)`;
- the library QA row is `pass`: `validate_icon()` valid with zero warnings,
  plus symmetry, spacing (MIC 6 between centerlines / 2 ink), internal
  spacing (no `review`), and negative space (no undersized holes or pinches).

Never change validators, contracts, tolerances, profile constants, or add
exception records to reach a pass. A `review` is not a pass.

## Meaning lock: what may change and what may not

You may redraw the art freely: new coordinates, a different keyshape,
simplified construction, merged or re-proportioned parts, straightened curves,
fewer repeated marks, and dropped decoration. The **meaning and core
visualization** of the original must survive. Before touching geometry, write
a short *meaning lock* in the new module's `REPAIR_PLAN`:

- **Concept** — one sentence naming what the original communicates.
- **Core parts** — the parts that carry identity and must remain recognisable
  (for example: the can body, the nozzle and a spray cue; the two letters "AB";
  the enclosing circle when the reference uses it to mean a badge or state).
  Keep their relationship: direction, which part holds which, left/right order,
  up/down, inside/outside.
- **Flexible parts** — detail you may simplify, merge or drop, each with the
  reason (the 32px readability or clearance limit it hits).

The fixed icon must be read as the same concept by someone who sees the
original. A generic mark sharing only the name is a mismatch, not a fix. Text
and digits still reuse `icon_set/typeface/glyphs.json` per
`icon_set/skills/icon-design/typeface.md`; keep the original characters, case
and order. Human figures follow `icon_set/skills/icon-design/human-reference.md`
(exact 4-unit detached head-to-body gap).

## Procedure

### 1. Intake and evidence

```bash
python3 icon_set/scripts/fix_icon_sub.py check --source <source-uuid>
python3 icon_set/scripts/prepare_icon_review.py --icon <current-id> --out icon_set/work/fix-icon-sub/<current-id>/before
```

`check` prints each icon's module, source UUID/path, keyshape and every failing
rule. Open `reference.png` and `sheet.png` from the evidence folder; if the
helper could not render the reference, render the SVG yourself (cairosvg) and
look at it. Read the module source. Open the original SVG, not only the
previous generation: the current icons may already have lost or distorted a
part.

If any sub model of this original already passes `check` and preserves the
meaning lock (confirm visually against the reference), do not draw anything
new: record it as the fix on each failing model (step 6, skipping the build)
and report. Only when none passes, or the passing one lost the meaning, draw.

### 2. Diagnose each failure

Group the findings by rule and locate the element and coordinates each names:

| Finding | Usual cause | First repair |
|---|---|---|
| `canvas/keyshape bounds` | ink misses or overshoots the envelope | move the extreme centerlines to the keyshape box (`bounds_for`), or pick the keyshape that fits the silhouette |
| `mic [...]` between parts | two unconnected parts < 6 apart on centerlines | move apart, join them with a shared endpoint and a scoped `connect`, or drop a flexible part |
| parallel straight edges | parallel strokes < 8 centerline | widen the shape, reduce repeats, or merge the two strokes |
| holes / pinches | enclosed opening too small, narrow wedge | enlarge the opening, remove the inner part, or open the contour |
| internal spacing `review` | a contour folds back near itself | open up the fold or shorten it |
| symmetry | a near-symmetric subject is off-axis | mirror from a shared axis, or make the asymmetry clearly intentional |
| canvas / stroke | earlier 2px or enlarged-canvas workaround | redraw at 32×32 with stroke 4 |

Also read `icon_set/skills/icon-design/validation.md`, `geometry.md` and
`authoring.md` in the same folder before repairing.

### 3. Plan the fix, smallest change first

Work the ladder and stop at the first rung that passes and keeps the lock:

1. **Correct** — snap coordinates to the keyshape box and grid; fix arcs,
   tangent joins, `connect` declarations that are wrong or missing.
2. **Rebalance** — move and resize parts to free clearance; change the keyshape
   if the silhouette really fits another one better.
3. **Simplify** — reduce flexible parts: fewer repeated marks, merge strokes
   into one contour, replace a fiddly curve with a clean arc or line.
4. **Redesign** — rebuild the core parts with a different, simpler
   construction at 32px (find a matching Lucide construction with
   `python3 icon_set/scripts/lucide_reference.py find <subject>` and
   `show <name> --profile SUB32` when useful) while keeping every core
   part and relationship.

Never squeeze below clearance, thin a stroke, grow the canvas, or declare
`connect` on parts that do not touch.

### 4. Scaffold and draw the variant

```bash
python3 icon_set/scripts/fix_icon_sub.py scaffold --icon <best-current-id> \
    --label "SUB32 fix: <what changed>" --author <your-model>
```

This wraps `create_variant.py`: the parent stays unchanged, the new file is
named `<new_id>_<source_uuid>.py`, `AUTHOR` becomes yours (lowercase, hyphenated
model name; ask if unsure) and `SOURCE_ICON_ID` / `SOURCE_PATH` are kept. Choose
the current icon closest to the original as the parent. If the scaffold refuses
(for example a `FREE` parent), author a new `Sub32` module by hand following
`/icon-sub` step 4, with `variant_of` pointing at the current icon.

Edit only the new module's `build()` and class attributes (`keyshape`,
`variant_label`). Remove any `canvas_width`/`canvas_height`, text-canvas,
`STROKE_WIDTH` or `PATH_STROKE_WIDTHS` override inherited from the parent and
subclass plain `Sub32`. Set `REPAIR_PLAN` to the meaning lock plus the ladder
rung used.

### 5. Validate and look, in a loop

```bash
python3 icon_set/scripts/fix_icon_sub.py check --icon <new-id>
python3 icon_set/scripts/prepare_icon_review.py --icon <new-id> --out icon_set/work/fix-icon-sub/<current-id>/after
```

Repeat step 3 → 5 until `check` exits 0. Then open the `after` sheet next to
`reference.png` and judge at native 32px in both themes: every core part
present and readable, relationships intact, curves smooth, negative space
balanced. A numeric pass that loses the concept is not a fix — go back up the
ladder or treat it as a failed attempt.

Try at least **two genuinely different constructions** (different ladder rungs
or layouts, not two nudges of the same one) before concluding the concept
cannot fit. Keep a one-line note of each attempt and the rule it hit.

### 6. Publish and record

On success:

```bash
python3 icon_set/scripts/build.py --family sub
python3 icon_set/scripts/compose.py --host container-circle --sub <new-id>
python3 icon_set/scripts/fix_icon_sub.py record --icon <current-id> --status fixed \
    --variant <new-id> --author <your-model> --evidence icon_set/work/fix-icon-sub/<current-id>
```

Confirm `<new-id>` is listed with status `pass` in
`published/sub32/manifest.json`. Record on every supplied current icon of this
original. Do not delete or edit the geometry of the failing icons. Wait for a
running build to finish before starting another (parallel builds republish
stale snapshots).

When no attempt passes while keeping the meaning lock:

```bash
python3 icon_set/scripts/fix_icon_sub.py record --icon <current-id> --status cannot-fix \
    --author <your-model> \
    --blocker "<rule> on <core parts>: <why every 32x32, stroke-4 drawing that keeps them fails>" \
    --attempt "<attempt 1 and the rule it hit>" --attempt "<attempt 2 and the rule it hit>" \
    --evidence icon_set/work/fix-icon-sub/<current-id>
```

This writes `SUB32_FIX_RECORDS['<current-id>']` into the icon's own module
(metadata only; geometry and `AUTHOR` untouched) with the failures seen, the
blocker and the attempts. Do not leave failing attempts registered: save each
attempt's rendered SVG in the evidence folder, then delete the scaffolded
module you created for it (never a module you did not create).
`python3 icon_set/scripts/fix_icon_sub.py list --status cannot-fix` lists all
recorded blockers.

## Batches

Given several originals, handle them one at a time with the full procedure;
a cannot-fix on one never stops the rest. Build the queue with:

```bash
python3 icon_set/scripts/fix_icon_sub.py backlog --jobs 8   # ~1-2 min
```

It strict-checks every sub model of each original that has a failing sub icon
in `published/failed/sub32/manifest.json` and writes
`icon_set/work/fix-icon-sub/backlog.json`: `has-strict-pass` originals only
need the visual confirmation and a `fixed` record; `needs-fix` originals need
a drawing. Rerun it after a sub build; it reads the latest failed manifest.

## Report

Per original, give one row: original UUID, current icon(s), outcome (`fixed →
<new-id>` or `cannot-fix`), failing rules before, the meaning lock's core
parts, what changed or was dropped and why, and the evidence folder. For a
cannot-fix, name the rule, the element and the attempts. Say plainly if the
build or `check` failed; never describe an unverified icon as passing.

## Never

- Relax a validator, contract, tolerance, keyshape dimension or profile constant.
- Use a larger canvas, a stroke other than 4, `FREE`, or a new exception record.
- Hand-edit an emitted SVG, or overwrite the geometry of the icons under review.
- Change the concept, drop a core part, or swap the original for a generic icon.
- Record `fixed` for a variant that has not passed `check`.
