---
name: icon-sub
description: Author a sub-family icon for the Pictographic icon set on the SUB32 profile (32x32). Use when asked for a small glyph, mark, operator, arrow, chevron, state, modifier, or a simple shape meant to sit inside a container or beside another icon -- anything that must read at 32 pixels. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# $icon-sub — one sub icon on `SUB32`

Use the user's request as the brief, including any supplied icon ID, reference paths, and output directory.

Resolve repository paths and run commands from the `claude_skills` directory containing `icon_set/` (three levels above this skill folder). In Codex, invoke these skills with `$icon-brief`, `$icon-sub`, `$icon-solo`, or `$icon-container`; in ChatGPT, select the skill with `@`. Treat slash-style handoffs in generated briefs as references to the corresponding skill.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts$icon-profile.v1.json`:

| | |
|---|---|
| Family | `sub` |
| Profile | `SUB32` |
| Canvas | 32×32, centre (16,16), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/sub/` — one file per icon |
| Subclass | `Sub32` from `._base` |
| Ships to | `icon_set/dist/sub32/` with its own `manifest.json` |
| Ink clearance (MIC) | 2 between distinct parts = **6 between centerlines** |
| Interior guide | (4,4)-(28,28) — constrains inner detail only |
| Existing icons to imitate | `arrow-down`, `arrow-down-left`, `arrow-down-right`, `arrow-left`, `arrow-right`, `arrow-up` and 46 more |

A **sub** icon is read small and hosted by others. Its whole canvas is the container's content region, so anything valid here can be placed in one. Verbs, states and modifiers declare `semantic_role = "SUB"`; a simple noun shape (`heart`, `circle`, `star`) declares `MAIN` with `semantic_kind = "noun"` and is still a sub icon -- the role describes the subject, the family decides the canvas.

**Wrong family? Stop.** If the brief is a standalone subject with its own silhouette (a device, an object, a badge), stop and use `$icon-solo`. If it is an enclosure meant to hold something, use `$icon-container`. A sub icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`Sub32` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

- `$icon-solo` — solo family, `SOLO48`, 48×48
- `$icon-container` — container family, `CONTAINER64`, 64×64

## Visual priorities

Prioritize **Lucide-style geometric construction and smooth curves**.
Prefer mirrored geometry and visual balance only where they preserve the icon's
meaning, recognizability, and natural shape. These are optional design choices,
not requirements: skip mirroring or forced balance when they would distort the
subject. A palm tree, for example, may retain uneven fronds and a leaning trunk;
mirror only the parts where it helps the drawing read clearly.

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
   matching module for this family when it already exists.
   See `icon_set/skills/icon-design/naming.md`.

2. **Reduce.** Keep the smallest recognizable silhouette, the features that carry
   identity, and nothing that disappears at 32 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

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

4. **Author the module** at `icon_set/model/icons/sub/<icon_id_with_underscores>.py`:

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
   from ._base import Sub32

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

- Eight stroke widths across the canvas. Keep the smallest recognizable silhouette and one identifying feature; a third level of detail does not survive at 32 pixels.
- The stroke-defined glyphs (`minus`, `bar`, `dot`, `exclamation`, `ellipsis`, `dots-vertical`) use `FREE` with an approved record. A new 4-unit-axis glyph needs its own record in `icon_set/model/contracts/exceptions.v1.json` with `status: "proposed"`; see `icon_set/skills/icon-design/keyshape-fitting.md`.
- Straight parts may sit exactly on the 7-unit centerline minimum. Curved parts need a unit of margin or the engine returns `review`.
- After it validates, prove it composes: `python3 icon_set/scripts/compose.py --host container-circle --sub <icon_id>`.

7. **Build and look.**

   ```bash
   python3 -m unittest discover -s icon_set/tests -t .
   python3 icon_set/scripts/build.py --family sub
   python3 icon_set/scripts/contact_sheet.py --family sub --theme dark --png /tmp/sub.png
   ```

   Open the PNG and judge it at 32 pixels. Numeric success is not
   visual approval; if two candidates are close, render both and keep the stronger.

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
  own model. Existing matches are patched in place, with source metadata
  preserved or added and `AUTHOR` updated to you.
- Tests green; `build.py --family sub` exits 0; the icon is in
  `icon_set/dist/sub32/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
