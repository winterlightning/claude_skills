---
name: icon-container
description: Author a container-family icon for the Pictographic icon set on the CONTAINER64 profile (64x64). Use when asked for an enclosure, frame, window, screen, badge outline, bubble, board, card, or any framed device drawn at 64. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
argument-hint: <icon-id> — <one-sentence brief> [references: <paths>]
---

# /icon-container — one container icon on `CONTAINER64`

Request: $ARGUMENTS

This skill authors **exactly one family**. Everything below is fixed by the
family and read from `icon_set/model/contracts/icon-profile.v1.json`:

| | |
|---|---|
| Family | `container` |
| Profile | `CONTAINER64` |
| Canvas | 64×64, centre (32,32), integer grid 1, stroke 4, round caps and joins |
| Module goes in | `icon_set/model/icons/container/` — one file per icon |
| Subclass | `Container64` from `._base` |
| Ships to | `icon_set/dist/container64/` with its own `manifest.json` |
| Ink clearance (MIC) | 2 between distinct parts = **6 between centerlines** |
| Interior guide | (8,8)-(56,56) — constrains inner detail only |
| Existing icons to imitate | `aiming-reticle`, `award-ribbon-container`, `browser-window`, `captive-bead-ring`, `circular-speech-bubble`, `clipboard` and 151 more |

A **container** stands alone as a noun and is the outer half of a `CONTAINER_COMBINE`. Nothing inside its canvas is reserved: draw the subject with the interior furniture it actually has -- a title bar, a lid, a dial face, a keypad. `(16,16)-(48,48)` is the **content region**, where a hosted child would land; the base adds `content-top-left` and `content-bottom-right` anchors marking it. Painting through it is allowed and often necessary; it just means this container will not clear that child, which `compose.py` measures per pair. The protected slot that used to forbid ink there was withdrawn on 2026-09-07 -- it made windows, tab bars and lids undrawable -- and `contracts/composition-templates.v1.json` keeps the record under `withdrawn_slot`.

**Wrong family? Stop.** If the subject reads at 48 and is never framed around anything, use `/icon-solo`. If it is the thing that goes *inside*, use `/icon-sub`. A container icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`Container64` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

- `/icon-sub` — sub family, `SUB32`, 32×32
- `/icon-solo` — solo family, `SOLO48`, 48×48

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
   identity, and nothing that disappears at 64 pixels. With a
   reference in scope, render it and look at it; read the subject, never the
   coordinates. See `icon_set/skills/icon-design/intake.md`.

3. **Choose the keyshape, write down its four extremes, design backwards to
   them.** The rectangle fit is exact (tolerance 0); `CIRCLE` is radial. These are
   the `CONTAINER64` numbers:

| Keyshape | Visible ink | Centerline box (author to this) |
|---|---|---|
| `CIRCLE` | radius 32 about (32,32) | radius 30 |
| `SQUARE` | (0,0)-(64,64) | (2,2)-(62,62) |
| `HRECT_XL` | (0,4)-(64,60) | (2,6)-(62,58) |
| `HRECT_L` | (0,8)-(64,56) | (2,10)-(62,54) |
| `HRECT_M` | (0,12)-(64,52) | (2,14)-(62,50) |
| `HRECT_S` | (0,16)-(64,48) | (2,18)-(62,46) |
| `VRECT_XL` | (4,0)-(60,64) | (6,2)-(58,62) |
| `VRECT_L` | (8,0)-(56,64) | (10,2)-(54,62) |
| `VRECT_M` | (12,0)-(52,64) | (14,2)-(50,62) |
| `VRECT_S` | (16,0)-(48,64) | (18,2)-(46,62) |

   Ask the model instead of doing arithmetic:
   `Keyshape.HRECT_L.bounds_for(Profile.CONTAINER64)`.

4. **Author the module** at `icon_set/model/icons/container/<icon_id_with_underscores>.py`:

   For a supplied reference ID, the new filename must instead be
   `<descriptive_name>_<source_id_with_underscores>.py`. Every generated module
   or one-off Python generation script must include `SOURCE_ICON_ID` (the exact
   original ID) and `SOURCE_PATH` (the supplied source path). Use `None` only
   for missing values; never discard an ID because the input also has a name.
   Follow the UUID example and patch lookup in `icon_set/skills/icon-design/naming.md`.

   ```python
   from ...keyshapes import Keyshape
   from ._base import Container64

   SOURCE_ICON_ID = "<exact-reference-id>"  # None only if no ID was supplied
   SOURCE_PATH = "<source-path>"  # None only if no path was supplied


   class <ClassName>(Container64):
       icon_id = "<icon-id>"
       keyshape = Keyshape.<TOKEN>
       semantic_role = "MAIN"
       semantic_kind = "noun"
       category = "containers"
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

- Design the subject, then measure what it holds -- not the other way round. Ink anywhere in `(16,16)-(48,48)` is legal; it costs hosting for children whose own ink reaches that far, and `mic` reports exactly which.
- A gap that sits exactly on the minimum is only certifiable when both sides are straight. Where a straight run has to hold a minimum gap, emit it as its own path rather than inside a contour that also carries corner arcs -- but only where the parts genuinely still share endpoints, because splitting a corner into two paths that do not touch invents crowding that is not there. See `browser-window`.
- Attached details (a clip, a tab, a handle) share endpoints with the outline and are declared with `relate("connect", ...)`. See `clipboard`.
- After it validates, measure what it hosts: run `python3 icon_set/scripts/compose.py --host <icon_id> --sub plus`, then `--sub heart` and `--sub check`. Record the answer in the docstring. Hosting nothing is a legitimate outcome for a container with a full interior; it is never a reason to empty the drawing out.

7. **Build and look.**

   ```bash
   python3 -m unittest discover -s icon_set/tests -t .
   python3 icon_set/scripts/build.py --family container
   python3 icon_set/scripts/contact_sheet.py --family container --theme dark --png /tmp/container.png
   ```

   Open the PNG and judge it at 64 pixels. Numeric success is not
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
  records the exact `SOURCE_ICON_ID` and `SOURCE_PATH`. Existing matches are
  patched in place, with source metadata preserved or added.
- Tests green; `build.py --family container` exits 0; the icon is in
  `icon_set/dist/container64/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
