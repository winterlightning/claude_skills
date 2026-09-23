---
name: primitive-make-ray
description: Author each given reference SVG file (a TODO reference, usually from icon_set/work/todo-references/) as a complete Pictographic SOLO48 icon, including text, digits, logos, symbols, avatars, wrappers and combinations. Takes one or more file paths; the source UUID and concept come from each filename. Save results and input metadata in a standalone folder without gallery updates. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# $primitive-make-ray — one solo icon on `SOLO48`

Arguments: $ARGUMENTS

Run from the repository containing `icon_set/`. The arguments are one or more reference SVG files, normally from `icon_set/work/todo-references/`. Process them in the order given, one icon per file; do not retrieve, add or substitute other references. If no file is given, say so and stop.

For each file, the brief is the file itself: its filename is `<concept>_<source-uuid>.svg`. The **source UUID** is the UUID at the end of the filename, the **concept** is the text before it, and the **reference path** is the file path as given. Render and inspect the reference, then follow the full authoring workflow below. Skip a file whose `icon_set/work/primitive-make-ray/<source-uuid>/*/result.json` already exists and report it as already done. If a file is missing or has no UUID in its name, report that and continue with the next file. After the last file, report every file's result.

**Folder-only output:** create a fresh result directory at `icon_set/work/primitive-make-ray/<source-uuid>/<unique-run-id>/`. Call it `RESULT_DIR` below. Store all source, exports, reference renders, previews, input metadata and findings there, including unsuccessful attempts. Never overwrite an earlier run. Do not write to `published/`, the registered icon folders, metadata catalogs, galleries, queues or runtime state. Do not run build, finish-icon, publish, release or gallery update commands. This output rule overrides output and registration advice in shared guides. A file counts as done once its run folder holds an authored Python module and a result.json with that source_uuid. Validation failures, warnings, and failed exports still count as attempts; do not retry them automatically. Write result.json last, including failures.

**Generate every input:** author the complete given reference as one SOLO48 icon. Do not skip, split into component briefs, or hand off because it contains text, digits, a logo, a symbol, an avatar, an enclosure or a combination. Preserve its defining features and arrangement.

Letters and digits may be hand-authored to preserve the reference's distinctive shape, including outlined or three-dimensional forms. Existing typeface glyphs are optional construction references, not a required substitute. These scope and text rules override routing and typeface restrictions in the shared guides. All SOLO48 geometry and validation requirements still apply.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `solo` |
| Profile | `SOLO48` |
| Canvas | 48×48, centre (24,24), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `RESULT_DIR/` — one file per icon |
| Subclass | `Solo48` from `icon_set.model.icons.solo._base` |
| Exports to | `RESULT_DIR/` only; no gallery or manifest updates |
| Ink clearance (MIC) | 4 between distinct parts = **8 between centerlines** |
| Interior guide | (6,6)-(42,42) — constrains inner detail only |
| Existing icons to imitate | `a-frame-church`, `a-line-skirt`, `abacus-two-rods-four-beads`, `abdominal-muscles`, `abdominal-torso`, `about-me-logo` |

Every input stays in `RESULT_DIR/`, subclasses `Solo48`, and uses `semantic_role = "MAIN"`, `semantic_kind = "noun"`. Keep the complete composition on the 48×48 canvas; do not reroute it to another family or enlarge the canvas.

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

1. **Name it.** One sentence for what the subject is, then a kebab-case
   `icon_id` (`^[a-z][a-z0-9]*(-[a-z0-9]+)*$`). Synonyms go in `aliases`,
   search terms in `keywords`. Keep a supplied `sym-<id>` at the front.
   Preserve any reference UUID or explicit source ID separately from the name.
   Inspect existing Python files by that ID for context, but author a new
   standalone module inside this run's RESULT_DIR; do not patch registered originals.
   See `icon_set/skills/icon-design/naming.md`.

Inspect the complete reference before reduction. Treat its text, enclosure, main subject and modifiers as parts of the requested composition; do not reject or split combinations. For revisions, preserve the parent and author the revised module in a fresh result directory.

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

4. **Author the module** at `RESULT_DIR/<icon_id_with_underscores>.py`:

   For a supplied reference ID, the new filename must instead be
   `<descriptive_name>_<source_id_with_underscores>.py`. Every generated module
   or one-off Python generation script must include `SOURCE_ICON_ID` (the exact
   original ID), `SOURCE_PATH` (the supplied source path) and `AUTHOR` (the
   model that drew it). Use `None` only for missing values; never discard an ID
   because the input also has a name. `AUTHOR` is never `None` and never
   guessed: name the model **you** are running as, in lowercase and hyphenated
   -- `astra-chatgpt` labels everything authored before this field existed, so
   use it only if that is you. If you do not know which model you are, ask
   rather than guess. Patching an existing module makes `AUTHOR` yours. Follow
   the UUID example, the author table and the patch lookup in
   `icon_set/skills/icon-design/naming.md`.

   ```python
   from icon_set.model.keyshapes import Keyshape
   from icon_set.model.icons.solo._base import Solo48

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

   Keep the module outside the registry. Load it by file path with
   `importlib.util.spec_from_file_location` from the repository root
   and instantiate its authored class directly.

5. **Validate and repair the model, never the SVG.**

   ```python
   icon = module.<ClassName>()  # module loaded from RESULT_DIR
   report = icon.validate_icon()
   print(report.describe())      # status must be "valid" with zero warnings
   ```

   Eight checks run in order; every failure names the element and coordinates.
   A `review` warning is **not** a pass. Repair ladder for crowding: enlarge the
   opening, rebalance, remove the part — never squeeze. Re-check the keyshape after
   every repair. See `icon_set/skills/icon-design/validation.md`.

6. **Family-specific checks.**

- SOLO48 has six keyshapes: `CIRCLE`, `SQUARE`, `HRECT_L`, `HRECT_M`, `VRECT_L` and `VRECT_M`, with the visible-ink bounds in the table above. Older modules may still name `HRECT_XL`/`_S` or `VRECT_XL`/`_S`; on SOLO48 those resolve to the same bounds as `HRECT_L`/`VRECT_L`, so never choose one for new work. The `_M` rectangles reduce only the short visible-ink side by 4: 44x32 horizontal or 32x44 vertical. If an upright subject cannot fit, try a recognizable diagonal construction on the integer grid. If it still cannot fit, save the validation findings and attempted fit in RESULT_DIR for manual review. Do not request a gallery flag, waive validation, or leave the 48x48 canvas.
- Budget before drawing: centerline boxes are 36x36 on `SQUARE`, 40x32 on `HRECT_L`, 32x40 on `VRECT_L`, 40x28 on `HRECT_M`, and 28x40 on `VRECT_M`. Every gap between distinct parts costs 8 on centerlines. An interior mark between two walls needs a band of 16 between the wall centerlines, 17 if either wall is curved, because the engine cannot certify a curved pair sitting exactly on the minimum. If the band is short, change the keyshape or drop the part; never squeeze.
- Existing solo modules authored before 2026-09-13 were drawn to full-canvas envelopes (ink 0-48) and MIC 2, and many no longer validate. Run `validate_icon()` on any icon before imitating its coordinates; take construction ideas from a failing one, not numbers.
- Traced references: render first, then re-author on this grid. Reconstruct the subject, never the source's coordinates. Put arc centres on integer points and pick radii whose apex *is* the endpoint, so the arc reaches the keyshape edge exactly and cannot overshoot it.
- Split a wall where a part attaches so the two share an endpoint; declare the contact with `relate("connect", ...)`. An arc merely touching a line is not proved as a connection and comes back `review`.
- Parallel straight edges inside the same contour must also meet the profile's ink clearance and centerline minimum. This is an exact blocking MIC check for positive overlapping runs, excluding adjacent segments and shared endpoints. Curved and near-parallel internal edges remain sampled advisories.
- Same concept also wanted at 32 or 64? That is a separately authored icon in another family with a suffix (`bell-sub`, `bell-container`). Never scale.

7. **Export locally and look.**

   Save `icon.to_svg()` as `RESULT_DIR/<icon-id>.svg` and
   save the input metadata beside it as `RESULT_DIR/<icon-id>.metadata.json`.
   Record the input as `concept`, `source_uuid` and `reference_path`,
   taken exactly from the filename and the path as given; do not
   substitute inferred values. Write this JSON before drawing, even if
   drawing fails.
   Save
   `report.describe()` as `RESULT_DIR/validation.txt`. Render that SVG
   directly with CairoSVG into light and dark PNGs at native 48px and
   enlarged size, all inside RESULT_DIR. Inspect both themes. Save a
   `result.json` containing source UUID/path, icon ID, author, validation
   status, visual-review findings, omissions and artifact filenames.
   Retain invalid candidates with their failure findings; do not claim
   they passed. If validation or rendering raises, retain the source and
   save the error in this same folder. No library build is needed.

8. **Report.** Say what the subject is, which keyshape and why, what you dropped
   and why, which references you used and what you took from each, and the
   validation status. If something could not be made to pass, name the check and
   the element and stop — a reported blocker beats a weakened rule.

## Never

- Change a profile constant, keyshape dimension, tolerance or `numeric_epsilon`.
- Put this icon in another family's folder or subclass another base for a
  different canvas.
- Scale a drawing from another family. Every family is authored fresh.
- Declare `connect` on parts that do not touch, add a `FREE` record to dodge a
  repair, or describe a `review` as a pass.
- Hand-write or patch the emitted SVG.

## Definition of done

- Python filename includes the supplied source ID for a new file; the script
  records the exact `SOURCE_ICON_ID`, `SOURCE_PATH` and an `AUTHOR` naming your
  own model. Source metadata is preserved in the standalone result module;
  earlier runs and registered originals remain unchanged.
- Source, SVG, matching input metadata JSON, previews, validation findings
  and result.json are saved
  together in RESULT_DIR; link this directory and its SVG in the final response.
- No gallery, published output, registry, queue or runtime-state updates.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and exact 4-unit detached head-to-body ink gap in the emitted geometry.
