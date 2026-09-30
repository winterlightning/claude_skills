---
name: symbol-24
description: Author a symbol24-family icon for the Pictographic icon set on the SYMBOL24 profile (24x24). Use when asked for a 24x24 icon or symbol, either drawn fresh or redrawn from an existing 32x32 sub or symbol icon. Uniform 4px stroke; validation is advisory and the icon is judged visually at 24 pixels. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# /symbol-24 — one symbol24 icon on `SYMBOL24`

Use the user's request as the brief, including any supplied icon ID, reference paths, and output directory.

Resolve repository paths and run commands from the `claude_skills` directory containing `icon_set/` (three levels above this skill folder). In Codex, invoke these skills with `$icon-brief`, `$icon-sub`, `$icon-solo`, `$icon-combination-main`, `$icon-avatar`, or `$icon-container`; in ChatGPT, select the skill with `@`. Treat slash-style handoffs in generated briefs as references to the corresponding skill.

**Text and numbers:** follow `icon_set/skills/icon-design/typeface.md` and reuse the existing
glyphs in `icon_set/typeface/glyphs.json`. Do not invent new letter/number
geometry, including text components in combined icons or Pending briefs.
This routing rule takes precedence over the primitive-authoring workflow below.

## Two ways in

**Fresh** — a brief with no 32 model: follow the procedure below and author
directly on the 24 grid.

**From 32** — a `sub` or `symbol` icon id (or a module whose 32x32 drawing
should become 24): start from a mechanical draft, then redraw it.

```bash
python3 icon_set/scripts/symbol24.py from32 --icon <32-icon-id> --author <your-model> [--id <new-id>]
```

It writes `icon_set/model/icons/symbol24/<id>[_<source-uuid>].py` with every
coordinate x 3/4 (halves rounded toward the centre, so mirrored parts stay
mirrored), copies `SOURCE_ICON_ID`/`SOURCE_PATH`, records `DERIVED_FROM_32`,
and lists conversion notes (collapsed lines, widened arc radii) as comments.
**The draft is not the result.** The stroke stays 4 while everything else
shrinks by a quarter, so every gap lost a third of its white. Redraw it: pull
details off the outline, straighten arms onto 45°/90°, simplify or drop the
third level of detail, keep the source's parts, count, directions and openings.
Delete each conversion note once it is resolved. Text-sized or non-square 32
sources are refused; redraw those by hand.

## Validation is advisory, quality is not

The contract marks this family's validation **advisory**: `validate_icon()`
and library QA findings (MIC, spacing, holes, symmetry) are information, not
gates, because a 4px stroke on 24 cannot satisfy them for most real subjects.
Only two rules block, and the build enforces them: a 24x24 SVG root and every
stroke 4. That moves the bar to your eyes — the icon must look **good** at
24 px, in both themes, beside its 32 source when there is one:

```bash
python3 icon_set/scripts/symbol24.py check --icon <icon-id>        # strict-24 pass required; advisory lines are notes
python3 icon_set/scripts/symbol24.py preview --icon <icon-id> [--compare <32-icon-id>] --out <scratch-dir>
```

Open the native and x8 PNGs. Judge: does it read as the subject at a glance;
are openings open and parts separate (touching ink that should be apart is a
defect even though it will not block); are strokes evenly spaced and curves
smooth; is it centred and balanced; does it match the 32 source's meaning.
If two candidates are close, render both and keep the stronger. Use the
advisory findings to find the tightest spots, and fix any that you can see.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `symbol24` |
| Profile | `SYMBOL24` |
| Canvas | 24×24, centre (12,12), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/symbol24/` — one file per icon |
| Subclass | `Symbol24` from `._base` |
| Ships to | `published/symbol24/` with its own `manifest.json` |
| Ink clearance (MIC) | 2 between distinct parts = **6 between centerlines** |
| Interior guide | (3,3)-(21,21) — constrains inner detail only |
| Existing icons to imitate | `circle-check-symbol24` |

A **symbol24** icon is a compact symbol read at 24 pixels. It is either drawn fresh on the 24 grid or redrawn from a 32x32 `sub`/`symbol` model. Verbs, states and modifiers declare `semantic_role = "SUB"`; a simple noun shape declares `MAIN` with `semantic_kind = "noun"`.

**Wrong family? Stop.** For the 32x32 side modifier use $icon-sub, for a 32x32 container symbol $icon-symbol, for a standalone 48 subject $icon-solo. A symbol24 icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`Symbol24` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

- `$icon-sub` — sub family, `SUB32`, 32×32
- `$icon-solo` — solo family, `SOLO48`, 48×48
- `$icon-container` — container family, `CONTAINER64`, 64×64
- `$icon-combination-main` — combination_main family, `COMBINATION_MAIN48`, 48×48
- `$icon-symbol` — symbol family, `SYMBOL32`, 32×32

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
   Search existing Python files by that ID before creating a new file; patch the
   matching module for this family for reuse; for review changes create an independent variant instead of overwriting it.
   See `icon_set/skills/icon-design/naming.md`.

Before reduction, apply `icon_set/skills/icon-design/reference-triage.md`. If the reference is a
container combination or side combination, route to `$icon-making` to reject
it as one primitive and queue two component briefs. A Pending component brief
already specifies which single component to isolate. For review revisions,
preserve the parent and edit a new file from `create_variant.py`.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at 24 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

   **Plan symbols before coordinates.** Read `icon_set/skills/icon-design/symbol-construction.md`.
   Identify typed shapes, nesting, repeated definitions/series, intended symmetry,
   and shared attachment points. Record a compact plan in the module; implement
   it with shared Python parameters and the existing geometry API. During repairs,
   change the owning symbol or repeat definition so joins and equality survive.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `SYMBOL24` numbers:

| Keyshape | Visible ink | Centerline box (author to this) |
|---|---|---|
| `CIRCLE` | radius 12 about (12,12) | radius 10 |
| `SQUARE` | (0,0)-(24,24) | (2,2)-(22,22) |
| `HRECT_XL` | (0,2)-(24,22) | (2,4)-(22,20) |
| `HRECT_L` | (0,3)-(24,21) | (2,5)-(22,19) |
| `HRECT_M` | (0,4)-(24,20) | (2,6)-(22,18) |
| `HRECT_S` | (0,6)-(24,18) | (2,8)-(22,16) |
| `VRECT_XL` | (2,0)-(22,24) | (4,2)-(20,22) |
| `VRECT_L` | (3,0)-(21,24) | (5,2)-(19,22) |
| `VRECT_M` | (4,0)-(20,24) | (6,2)-(18,22) |
| `VRECT_S` | (6,0)-(18,24) | (8,2)-(16,22) |

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.SYMBOL24)`.

4. **Author the module** at `icon_set/model/icons/symbol24/<icon_id_with_underscores>.py`:

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
   from ...keyshapes import Keyshape
   from ._base import Symbol24

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied
   AUTHOR = "<your-model>"  # the model authoring this file; never None


   class <ClassName>(Symbol24):
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

   Nothing to register. The folder is the registry.

5. **Validate and repair the model, never the SVG.**

   ```python
   from icon_set.model.icons.registry import create
   report = create("<icon-id>").validate_icon()
   print(report.describe())      # advisory for symbol24: read it, do not chase it
   ```

   Findings name the element and coordinates; use them to locate crowding you
   can see. Repair ladder for visible crowding: enlarge the opening, rebalance,
   remove the part. Then run `python3 icon_set/scripts/symbol24.py check --icon <icon-id>`;
   its strict-24 result (canvas and stroke) must pass. See `icon_set/skills/icon-design/validation.md`.

6. **Family-specific checks.**

- Every path uses the profile-wide 4px stroke. Never set `STROKE_WIDTH` or `PATH_STROKE_WIDTHS`, and never leave the 24x24 canvas: these two are the only blocking rules, and `symbol24.py check` enforces them.
- Six stroke widths across the canvas. Budget for one silhouette plus at most one identifying detail; drop secondary detail before crowding it.
- Openings that carry meaning (a crescent's inner curve, a gauge's gap, a check circle's opening) must stay visibly open at 24 px in both themes. Aim for 2 units of visible ink between parts (6 between centerlines); where that is impossible, keep the gap that looks cleanest, since 1 unit of white can still read.
- Text and digits: reuse `icon_set/typeface/glyphs.json`; if the glyphs cannot fit 24 with their meaning intact, say so and stop rather than inventing letterforms.

7. **Build and look.**

   ```bash
   python3 -m unittest discover -s icon_set/tests -t .
   python3 icon_set/scripts/build.py --family symbol24
   python3 icon_set/scripts/contact_sheet.py --family symbol24 --theme dark --png /tmp/symbol24.png
   ```

   Also run `symbol24.py preview` (above). Open the PNGs and judge them at 24 pixels. Numeric success is not
   visual approval; if two candidates are close, render both and keep the stronger.

8. **Report.** Say what the subject is, which keyshape and why, what you dropped
   and why, which references you used and what you took from each, and the
   strict-24 result, the advisory findings you accepted and why, and — for a
   redraw — what changed from the 3/4 draft. If the subject cannot look good
   at 24, say so and stop rather than shipping a muddy icon.

## Never

- Change a profile constant, keyshape dimension, tolerance or `numeric_epsilon`.
- Put this icon in another family's folder or subclass another base for a
  different canvas.
- Ship the `from32` draft unrevised, or scale a 48/64 drawing: redraw on the 24 grid.
- Declare `connect` on parts that do not touch, add a `FREE` record to dodge a
  repair, or thin the stroke / enlarge the canvas to make something fit.
- Hand-write or patch the emitted SVG.

## Definition of done

- Python filename includes the supplied source ID for a new file; the script
  records the exact `SOURCE_ICON_ID`, `SOURCE_PATH` and an `AUTHOR` naming your
  own model. Existing matches are patched in place, with source metadata
  preserved or added and `AUTHOR` updated to you.
- Tests green; `build.py --family symbol24` exits 0; the icon is in
  `published/symbol24/manifest.json`.
- `symbol24.py check` is strict-24 `pass`; advisory findings are listed in the report.
- For a redraw: `DERIVED_FROM_32` names the 32 icon and the conversion notes are gone.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and exact 4-unit detached head-to-body ink gap in the emitted geometry.
