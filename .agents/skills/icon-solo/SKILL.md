---
name: icon-solo
description: Author a solo-family icon for the Pictographic icon set on the SOLO48 profile (48x48). Use when asked for a standalone subject -- a device, object, badge, tool, figure, or a traced reference drawing -- that is read on its own at 48 pixels and neither hosts nor is hosted. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
---

# $icon-solo — one solo icon on `SOLO48`

Use the user's request as the brief, including any supplied icon ID, reference paths, and output directory.

Resolve repository paths and run commands from the `claude_skills` directory containing `icon_set/` (three levels above this skill folder). In Codex, invoke these skills with `$icon-brief`, `$icon-sub`, `$icon-solo`, or `$icon-container`; in ChatGPT, select the skill with `@`. Treat slash-style handoffs in generated briefs as references to the corresponding skill.

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts$icon-profile.v1.json`:

| | |
|---|---|
| Family | `solo` |
| Profile | `SOLO48` |
| Canvas | 48×48, centre (24,24), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/solo/` — one file per icon |
| Subclass | `Solo48` from `._base` |
| Ships to | `icon_set/dist/solo48/` with its own `manifest.json` |
| Ink clearance (MIC) | 2 between distinct parts = **6 between centerlines** |
| Interior guide | (6,6)-(42,42) — constrains inner detail only |
| Existing icons to imitate | `a-frame-church`, `academic-graduation-cap`, `analogue-wristwatch`, `ant`, `ant-head`, `anteater` and 568 more |

A **solo** icon is one independently readable subject. The whole 48 canvas belongs to it: there is nothing it must fit inside. It is always `semantic_role = "MAIN"`, `semantic_kind = "noun"`.

**Wrong family? Stop.** If the brief is a small glyph, operator or modifier meant to be hosted, stop and use `$icon-sub`. If it is an enclosure meant to hold a sub icon, use `$icon-container`. A solo icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`Solo48` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

- `$icon-sub` — sub family, `SUB32`, 32×32
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
   identity, and nothing that disappears at 48 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `SOLO48` numbers:

| Keyshape | Visible ink | Centerline box (author to this) |
|---|---|---|
| `CIRCLE` | radius 24 about (24,24) | radius 22 |
| `SQUARE` | (0,0)-(48,48) | (2,2)-(46,46) |
| `HRECT_XL` | (0,3)-(48,45) | (2,5)-(46,43) |
| `HRECT_L` | (0,6)-(48,42) | (2,8)-(46,40) |
| `HRECT_M` | (0,9)-(48,39) | (2,11)-(46,37) |
| `HRECT_S` | (0,12)-(48,36) | (2,14)-(46,34) |
| `VRECT_XL` | (3,0)-(45,48) | (5,2)-(43,46) |
| `VRECT_L` | (6,0)-(42,48) | (8,2)-(40,46) |
| `VRECT_M` | (9,0)-(39,48) | (11,2)-(37,46) |
| `VRECT_S` | (12,0)-(36,48) | (14,2)-(34,46) |

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.SOLO48)`.

4. **Author the module** at `icon_set/model/icons/solo/<icon_id_with_underscores>.py`:

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

- Twelve stroke widths across the canvas: one more feature than a sub icon, no more. Between a curved outline and an interior part you need the 8-unit minimum *plus* a unit of margin, because the engine cannot certify a curved pair sitting exactly on the minimum. `film-frame` moved from `SQUARE` to `VRECT_XL` for exactly this reason: a 15-deep band cannot hold a 4-unit mark with 8 on both sides.
- Traced references: render first, then re-author on this grid. Reconstruct the subject, never the source's coordinates. Pick arc radii whose apex *is* the endpoint so the arc cannot overshoot the keyshape (`smartwatch`: r 15 from (10,11) to (22,5)).
- Split a wall where a part attaches so the two share an endpoint; declare the contact with `relate("connect", ...)`. An arc merely touching a line is not proved as a connection and comes back `review`.
- Same concept also wanted at 32 or 64? That is a separately authored icon in another family with a suffix (`bell-sub`, `bell-container`). Never scale.

7. **Build and look.**

   ```bash
   python3 -m unittest discover -s icon_set/tests -t .
   python3 icon_set/scripts/build.py --family solo
   python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo.png
   ```

   Open the PNG and judge it at 48 pixels. Numeric success is not
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
- Tests green; `build.py --family solo` exits 0; the icon is in
  `icon_set/dist/solo48/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
