---
name: side-sub-make-thuan
description: Retrieve the next missing side-combination sub (gallery side-subs page) without parameters and author it as a Pictographic SUB32 icon exactly like its reference, with no classification or routing. Save results and retrieval metadata in a standalone folder without gallery updates. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# /side-sub-make-thuan — one sub icon on `SUB32`

Invoke this skill without parameters. Run from the repository containing `icon_set/`.

Retrieve the next missing side-combination sub (the Missing bucket of `gallery/side-subs.html`: no drawing yet, not marked text/number) by running this command without parameters:

```bash
python3 icon_set/scripts/next_side_sub.py
```

Use its output as the brief, including the source ID and reference path, then follow the full authoring workflow below.

**Folder-only output:** create a fresh result directory at `icon_set/work/side-sub-make-thuan/<source-uuid>/<unique-run-id>/`. Call it `RESULT_DIR` below. Store all source, exports, reference renders, previews, retrieval metadata and findings there, including unsuccessful attempts. Never overwrite an earlier run. Do not write to `published/`, the registered icon folders, metadata catalogs, contracts, galleries, queues or runtime state. Do not run build, compose, finish-icon, publish, release or gallery update commands. This output rule overrides output and registration advice in shared guides. The next-side-sub helper skips a source UUID once a run contains an authored Python module and a readable result.json with that source_uuid. Validation failures, warnings, and failed exports still count as attempts; do not retry them automatically. Write result.json last, including failures. Only attempts without a saved result remain eligible for automatic retry. If retrieval fails or no missing side sub remains, report that result and stop.

**Draw the reference as it is:** author the retrieved sub `reference` as one SUB32 icon that follows the reference. Do not classify, triage, route, skip or split it into component briefs. Preserve every visible part of the reference: frames, badges, secondary marks, holes, and their positions, directions and counts. The `combination context` SVGs only show how this sub sits beside its main; never draw that main. Inventory the reference parts before drawing, and afterwards compare reference and result side by side at native and enlarged sizes.

Keep the strict 32×32 canvas and the 4px stroke: side combinations need a sub that passes SUB32 as is. Do not enlarge the canvas, thin strokes, or produce an exact resized original. If the complete reference cannot pass, keep every part, save the validation findings and attempted fit in RESULT_DIR, and record the failure in result.json; do not drop parts to force a pass.

Letters or digits inside the reference: reuse the matching glyphs in `icon_set/typeface/glyphs.json` when they fit the reference; hand-author them only when needed to preserve the reference's shape. These scope and text rules override routing, skip and typeface restrictions in the shared guides. All SUB32 geometry and validation requirements still apply.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `sub` |
| Profile | `SUB32` |
| Canvas | 32×32, centre (16,16), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `RESULT_DIR/` — one file per icon |
| Subclass | `Sub32` from `icon_set.model.icons.sub._base` |
| Exports to | `RESULT_DIR/` only; no gallery or manifest updates |
| Ink clearance (MIC) | 2 between distinct parts = **6 between centerlines** |
| Interior guide | (4,4)-(28,28) — constrains inner detail only |
| Existing icons to imitate | `a-frame-church-sub32`, `a-frame-church-sub32-v2`, `ab-text`, `ab-text-v2`, `access-key-card-sub32`, `add-location-map-pin-sub32` |

Every input stays in `RESULT_DIR/` and subclasses `Sub32`. Modifiers, states and verbs declare `semantic_role = "SUB"`; a simple noun shape (`heart`, `star`) declares `MAIN` with `semantic_kind = "noun"`. Keep the complete reference on the 32×32 canvas; do not reroute it to another family or enlarge the canvas.

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

Inspect the complete reference before reduction, then glance at the (at most two) combination-context SVGs to confirm which part is the sub. Draw only the reference; do not reject, reroute or split it. For revisions, preserve the parent and author the revised module in a fresh result directory.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at 32 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

   **Plan symbols before coordinates.** Read `icon_set/skills/icon-design/symbol-construction.md`.
   Identify typed shapes, nesting, repeated definitions/series, intended symmetry,
   and shared attachment points. Record a compact plan in the module; implement
   it with shared Python parameters and the existing geometry API. During repairs,
   change the owning symbol or repeat definition so joins and equality survive.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `SUB32` numbers:

| Keyshape | Visible ink | Centerline box (author to this) |
|---|---|---|
| `CIRCLE` | radius 16 about (16,16) | radius 14 |
| `SQUARE` | (0,0)-(32,32) | (2,2)-(30,30) |
| `HRECT_XL` | (0,2)-(32,30) | (2,4)-(30,28) |
| `HRECT_L` | (0,4)-(32,28) | (2,6)-(30,26) |
| `HRECT_M` | (0,6)-(32,26) | (2,8)-(30,24) |
| `HRECT_S` | (0,8)-(32,24) | (2,10)-(30,22) |
| `VRECT_XL` | (2,0)-(30,32) | (4,2)-(28,30) |
| `VRECT_L` | (4,0)-(28,32) | (6,2)-(26,30) |
| `VRECT_M` | (6,0)-(26,32) | (8,2)-(24,30) |
| `VRECT_S` | (8,0)-(24,32) | (10,2)-(22,30) |

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.SUB32)`.

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
   from icon_set.model.icons.sub._base import Sub32

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied
   AUTHOR = "<your-model>"  # the model authoring this file; never None


   class <ClassName>(Sub32):
       icon_id = "<icon-id>"
       keyshape = Keyshape.<TOKEN>
       semantic_role = "SUB"
       semantic_kind = "modifier"
       category = "primitives/<operator|mark|shape|arrow|chevron|control>"
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
   opening, rebalance — never squeeze or remove a reference part. Re-check the keyshape after
   every repair. See `icon_set/skills/icon-design/validation.md`.

6. **Family-specific checks.**

- Use the profile-wide 4px stroke for every ordinary path. Do not set `STROKE_WIDTH = 2` or add `PATH_STROKE_WIDTHS` merely to rescue crowded detail, enlarge an opening, or force a 32px fit. Existing named compact exceptions remain scoped to their already approved records; do not create a new compact exception without explicit user approval.
- Intentional enclosed negative space is acceptable when it defines the concept. The triangular openings in Bluetooth and the inner opening of a crescent moon are reference examples: preserve their count, direction, and readable separation instead of filling, collapsing, or removing them just to avoid a hole finding. Verify each opening at native size in light and dark themes. If validation still flags an expected opening, report that finding honestly; visual acceptance of the hole does not waive an unrelated MIC, keyshape, or spacing failure.
- Eight stroke widths across the canvas. Keep the smallest recognizable silhouette and one identifying feature; a third level of detail does not survive at 32 pixels.
- The stroke-defined glyphs (`minus`, `bar`, `dot`, `exclamation`, `ellipsis`, `dots-vertical`) use `FREE` with an approved record. A new 4-unit-axis glyph needs a proposed record; write the proposal into result.json instead of editing `icon_set/model/contracts/exceptions.v1.json`, and report it. See `icon_set/skills/icon-design/keyshape-fitting.md`.
- Curved parts need margin unless the distance engine certifies exact axis separation. Preserve the exact human head-to-body gap from `icon_set/skills/icon-design/human-reference.md`.
- The module is not registered, so skip `compose.py`; the result is judged on its own at 32 pixels.

7. **Export locally and look.**

   Save `icon.to_svg()` as `RESULT_DIR/<icon-id>.svg` and
   save the retrieval metadata beside it as `RESULT_DIR/<icon-id>.metadata.json`.
   Preserve the helper's concept, source UUID, reference path, category,
   `aliases`, `uses` and `combination_context` (a list of the context lines) as
   `concept`, `source_uuid`, `reference_path`, `category`, `aliases`, `uses` and
   `combination_context`. Keep the exact strings; do not substitute inferred values.
   Include the complete original stdout as `retrieval_stdout` to retain
   any additional fields, and stderr warnings as `retrieval_stderr`.
   Write this JSON as soon as retrieval succeeds, even if drawing fails.
   Save
   `report.describe()` as `RESULT_DIR/validation.txt`. Render that SVG
   directly with CairoSVG into light and dark PNGs at native 32px and
   enlarged size, all inside RESULT_DIR. Inspect both themes. Save a
   `result.json` containing source UUID/path, icon ID, author, validation
   status, visual-review findings, reference-part coverage, omissions and
   artifact filenames. Retain invalid candidates with their failure findings;
   do not claim they passed. If validation or rendering raises, retain the
   source and save the error in this same folder. No library build is needed.

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
- Source, SVG, matching retrieval metadata JSON, previews, validation findings
  and result.json are saved
  together in RESULT_DIR; link this directory and its SVG in the final response.
- No gallery, published output, registry, contract, queue or runtime-state updates.
- Every visible part of the reference is present on the 32×32 canvas with the 4px stroke.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and exact 4-unit detached head-to-body ink gap in the emitted geometry.
