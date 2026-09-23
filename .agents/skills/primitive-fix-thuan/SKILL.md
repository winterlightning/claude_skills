---
name: primitive-fix-thuan
description: Claim a number of disapproved Pictographic solo icons from the shared production fix queue, repair each registered Python module in place with the SOLO48 rules, keep the first version in history, upload the before and after drawings to production and report done or cannot-fix. Arguments: count, optional --offset, --disapprove-status and --worker. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# $primitive-fix-thuan — fix claimed solo icons in place on `SOLO48`

Arguments: $ARGUMENTS

Run from the repository containing `icon_set/`. The first number in the arguments is the
**count** of icons to claim (required; ask when it is missing). `--offset N` skips that many
claimable icons, `--disapprove-status` keeps one disapproval reason (`bad-stroke`, `meaning`,
`manual-fix-request`, `other`). The **worker name** identifies your machine on every call: take
it from `--worker`, else from `$PICTOGRAPHIC_WORKER`, else ask (for example `thuan-mac`).

**Claim first.** Retrieve and claim the icons with one command built from those arguments:

```bash
python3 icon_set/scripts/primitive_fix.py start --worker <name> --limit <count> [--offset N] [--disapprove-status R]
```

It claims the icons on production (so no other machine fixes them), creates one result
directory per icon at `icon_set/work/primitive-fix-thuan/<icon-key>/<run-id>/` with
`brief.txt`, `claim.json` and a `before/` copy of the registered module and the displayed SVG,
uploads that first version to production, and prints one block per icon: the icon key, the
**module** path to edit, the result directory, the disapproval reason and the reviewer's
feedback. Exit code 3 means nothing was claimable: report that and stop. Treat each block as
one job and the feedback as its specification; then follow the full authoring workflow below
for every claimed icon.

**Fix in place:** every job is a registered solo icon that a reviewer disapproved. Edit the
module named in its block directly; do not create a variant, a new file or a copy, and do not
touch any other icon. Its first version is already saved in `RESULT_DIR/before/` and on
production, so the history survives your edit. Preserve the icon's concept and `icon_id`;
change the geometry the feedback asks for, and repair whatever keeps validation from passing.
Set `AUTHOR` to yourself: you drew the geometry that ships.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `solo` |
| Profile | `SOLO48` |
| Canvas | 48×48, centre (24,24), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/solo/` — one file per icon |
| Subclass | `Solo48` from `._base` |
| Ships to | `published/solo48/` with its own `manifest.json` |
| Ink clearance (MIC) | 4 between distinct parts = **8 between centerlines** |
| Interior guide | (6,6)-(42,42) — constrains inner detail only |
| Existing icons to imitate | `a-frame-church`, `a-line-skirt`, `abacus-two-rods-four-beads`, `abdominal-muscles`, `abdominal-torso`, `about-me-logo` |

Every job stays in `icon_set/model/icons/solo/`, subclasses `Solo48`, and keeps its
`semantic_role`, `semantic_kind`, `icon_id`, `SOURCE_ICON_ID` and `SOURCE_PATH`. Keep the
complete composition on the 48×48 canvas; do not reroute it to another family or enlarge
the canvas.

## Visual priorities

Prioritize **Lucide-style geometric construction and smooth curves**.
Prefer mirrored geometry and visual balance only where they preserve the icon's
meaning, recognizability, and natural shape. These are optional design choices,
not requirements: skip mirroring or forced balance when they would distort the
subject. A palm tree, for example, may retain uneven fronds and a leaning trunk;
mirror only the parts where it helps the drawing read clearly.

For any human subject or human part in a scene, first read
`icon_set/skills/icon-design/human-reference.md` and inspect the relevant files in
`icon_set/references/human_ref/`. These own human proportions and construction;
detached heads require exactly 4 units of visible head-to-body clearance.
For each stick figure, call `self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")` after creating those parts. The head flag names its outline primitive or contour; the torso flag names the upper torso primitive, with `start` or `end` identifying its actual neck junction. Use a unique figure ID for each person. The required gap is exactly 8 units between stroke centerlines / 4 units between ink edges. See the shared human reference for the full example and measurement rules. These flags support future validation; they do not certify spacing or declare contact.

Before authoring, inspect a relevant local Lucide original and its atomic-debug
geometry when a useful match exists. Use its construction principles with this
family's own grid, stroke and keyshape; preserve the requested subject.

Build symmetric subjects from a shared axis and mirrored coordinates, with
matching radii and spacing. Preserve intentional asymmetry in directional,
perspective, or naturally asymmetric subjects. Make curve-to-curve and
curve-to-line joins tangent-continuous where the silhouette should be smooth;
round stroke caps alone do not repair a kink. Prefer fewer coherent curves over
many short segments. Preserve deliberate corners and recognizable features.

Apply `icon_set/skills/icon-design/authoring.md` for the construction and visual
review checklist. A numeric pass alone is not enough: inspect curve flow,
paired proportions, and negative space at native size in both themes. Repair
tight areas by rebalancing geometry, without weakening validation rules.

## Procedure

1. **Keep its name.** The `icon_id`, `aliases` and `keywords` stay unless the feedback asks
   otherwise. For reference, a new id would be a kebab-case
   `icon_id` (`^[a-z][a-z0-9]*(-[a-z0-9]+)*$`). Synonyms go in `aliases`,
   search terms in `keywords`. Keep a supplied `sym-<id>` at the front.
   Preserve any reference UUID or explicit source ID separately from the name.
   Patch the module named in the job block; that file is the deliverable. Never create
   a variant or a second module for a fix.
   See `icon_set/skills/icon-design/naming.md`.

Read `RESULT_DIR/brief.txt` and render `RESULT_DIR/before/<icon-id>.svg` before touching the
module: the feedback names what is wrong, the drawing shows what the reviewer saw. Keep what
was not criticised unless validation forces a change.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at 48 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

   **Plan symbols before coordinates.** Read `icon_set/skills/icon-design/symbol-construction.md`.
   Identify typed shapes, nesting, repeated definitions/series, intended symmetry,
   and shared attachment points. Record a compact plan in the module; implement
   it with shared Python parameters and the existing geometry API. During repairs,
   change the owning symbol or repeat definition so joins and equality survive.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `SOLO48` numbers:

| Keyshape | Visible ink | Centerline box (author to this) |
|---|---|---|
| `CIRCLE` | radius 22 about (24,24) | radius 20 |
| `SQUARE` | (4,4)-(44,44) | (6,6)-(42,42) |
| `HRECT_L` | (2,6)-(46,42) | (4,8)-(44,40) |
| `HRECT_M` | (2,8)-(46,40) | (4,10)-(44,38) |
| `VRECT_L` | (6,2)-(42,46) | (8,4)-(40,44) |
| `VRECT_M` | (8,2)-(40,46) | (10,4)-(38,44) |

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.SOLO48)`.

4. **Edit the module** at the path printed in the job block. Its `SOURCE_ICON_ID`,
   `SOURCE_PATH` and class stay; set `AUTHOR` to the model you are running as, lowercase and
   hyphenated, never guessed. The shape of a solo module, for orientation:

   ```python
   from ...keyshapes import Keyshape
   from ._base import Solo48

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied
   AUTHOR = "<your-model>"  # the model authoring this file; never None


   class <ClassName>(Solo48):
       icon_id = "<icon-id>"
       keyshape = Keyshape.<TOKEN>
       semantic_role = "MAIN"
       semantic_kind = "noun"
       category = "objects/<device|media|award|...>"
       aliases = ()
       keywords = ()

       def build(self) -> None:
           # add_line / add_arc / add_dot / add_polyline / add_contour / relate
           ...
   ```

   Contour members paint as round joins; loose primitives as round caps. Where two
   parts genuinely touch, share an endpoint and declare it:
   `self.relate("connect", "a", "b")` — that pair only. Technique, arcs and
   tangent-continuous joins: `icon_set/skills/icon-design/geometry.md`, `icon_set/skills/icon-design/authoring.md`.

   Nothing to register. The folder is the registry.

5. **Validate and repair the model, never the SVG.**

   ```python
   from icon_set.model.icons.registry import create
   report = create("<icon-id>").validate_icon()
   print(report.describe())      # status must be "valid" with zero warnings
   ```

   Eight checks run in order; every failure names the element and coordinates.
   A `review` warning is **not** a pass. Repair ladder for crowding: enlarge the
   opening, rebalance, remove the part — never squeeze. Re-check the keyshape after
   every repair. See `icon_set/skills/icon-design/validation.md`.

6. **Family-specific checks.**

- SOLO48 has six keyshapes: `CIRCLE`, `SQUARE`, `HRECT_L`, `HRECT_M`, `VRECT_L` and `VRECT_M`, with the visible-ink bounds in the table above. Older modules may still name `HRECT_XL`/`_S` or `VRECT_XL`/`_S`; on SOLO48 those resolve to the same bounds as `HRECT_L`/`VRECT_L`, so never choose one for new work. The `_M` rectangles reduce only the short visible-ink side by 4: 44x32 horizontal or 32x44 vertical. If an upright subject cannot fit, try a recognizable diagonal construction on the integer grid. If it still cannot fit, retain the validation findings and request the gallery's exception flag for manual review; record the reason and attempted fit. The flag is not a validation waiver or permission to leave the 48x48 canvas.
- Budget before drawing: centerline boxes are 36x36 on `SQUARE`, 40x32 on `HRECT_L`, 32x40 on `VRECT_L`, 40x28 on `HRECT_M`, and 28x40 on `VRECT_M`. Every gap between distinct parts costs 8 on centerlines. An interior mark between two walls needs a band of 16 between the wall centerlines, 17 if either wall is curved, because the engine cannot certify a curved pair sitting exactly on the minimum. If the band is short, change the keyshape or drop the part; never squeeze.
- Existing solo modules authored before 2026-09-13 were drawn to full-canvas envelopes (ink 0-48) and MIC 2, and many no longer validate. Run `validate_icon()` on any icon before imitating its coordinates; take construction ideas from a failing one, not numbers.
- Traced references: render first, then re-author on this grid. Reconstruct the subject, never the source's coordinates. Put arc centres on integer points and pick radii whose apex *is* the endpoint, so the arc reaches the keyshape edge exactly and cannot overshoot it.
- Split a wall where a part attaches so the two share an endpoint; declare the contact with `relate("connect", ...)`. An arc merely touching a line is not proved as a connection and comes back `review`.
- Parallel straight edges inside the same contour must also meet the profile's ink clearance and centerline minimum. This is an exact blocking MIC check for positive overlapping runs, excluding adjacent segments and shared endpoints. Curved and near-parallel internal edges remain sampled advisories.
- Same concept also wanted at 32 or 64? That is a separately authored icon in another family with a suffix (`bell-sub`, `bell-container`). Never scale.

7. **Finish the job.** When the model validates with zero warnings and looks right at
   native size in both themes, record and report it:

   ```bash
   python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> --outcome done --note "<what changed>"
   ```

   `finish` validates the registered module again through the registry, writes
   `RESULT_DIR/after/` (module copy, SVG, light/dark previews at 48 and 384 px),
   `validation.txt` and `result.json`, uploads the after drawing, module and validation to
   production, and reports **done**: the revision returns to Ready for the reviewer with its
   feedback kept. It refuses `done` (exit 2, nothing uploaded or reported) while the model is
   invalid or has warnings; fix the model and run it again. When no meaning-preserving
   drawing can pass, stop and report instead:

   ```bash
   python3 icon_set/scripts/primitive_fix.py finish --worker <name> --icon <icon-key> --outcome cannot-fix --note "<the blocking check and element>"
   ```

   Then restore the module to its `before/` copy so an unfinished attempt does not ship.

   **After every claimed icon is finished**, publish only the fixed icons; never run a full
   library build or a plain `publish` for fixes:

   ```bash
   python3 -m icon_set build --icon <module> --no-png --no-report   # once per fixed module
   python3 -m icon_set publish --no-build
   git add <fixed modules> published/solo48 published/gallery/icons.json published/release.json icon_set/work/primitive-fix-thuan
   git commit -m "Fix <icon keys>" && git push origin icon-lib
   ```

   Production shows the new drawings after its next pull; the Fix queue page already shows
   the uploaded before/after.

8. **Report.** For every claimed icon say the key, what the feedback asked for, what you
   changed, which keyshape and why, the validation status, the outcome you reported (done or
   cannot-fix) and the result directory. Say which modules were built and pushed. If something could not be made to pass, name the check and
   the element and stop — a reported blocker beats a weakened rule.

## Never

- Fix an icon you did not claim, or claim more than the requested count.
- Create a variant, a copy or a new module for a fix, or edit any icon that is not one of
  the claimed jobs.
- Report `done` on a model that is invalid, has warnings, or that you did not run
  `finish` on; never change the production status through `/api/reviews` instead.
- Change a profile constant, keyshape dimension, tolerance or `numeric_epsilon`.
- Put this icon in another family's folder or subclass another base for a
  different canvas.
- Declare `connect` on parts that do not touch, add a `FREE` record to dodge a
  repair, or describe a `review` as a pass.
- Hand-write or patch the emitted SVG.
- Run a full library build or a plain `publish`.

## Definition of done

- Every claimed icon has `RESULT_DIR/before/`, `RESULT_DIR/after/` (or a cannot-fix
  `result.json`), `validation.txt` and `result.json`, and `finish` reported its outcome;
  link each result directory and its after SVG in the final response.
- The registered module keeps its `icon_id`, `SOURCE_ICON_ID` and `SOURCE_PATH`, and
  records an `AUTHOR` naming your own model.
- `validate_icon()` is `valid` with no warnings for every icon reported done.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- Only the fixed icons were built; `publish --no-build` ran once; the modules, the touched
  `published/` files and the result directories are committed and pushed.
