---
name: icon-avatar
description: Author a solo-family avatar for the Pictographic icon set on the SOLO48 profile (48x48). Use for a standalone user avatar, profile bust, or head-and-body portrait drawn at 48. A head and its own body form one natural subject. Generated from the contracts by icon_set/scripts/generate_skills.py; do not edit by hand.
argument-hint: <icon-id> — <one-sentence brief> [references: <paths>]
---

# /icon-avatar — one avatar icon on `SOLO48`

Request: $ARGUMENTS

**Text and numbers:** follow `icon_set/skills/icon-design/typeface.md` and reuse the existing
glyphs in `icon_set/typeface/glyphs.json`. Do not invent new letter/number
geometry, including text components in combined icons or Pending briefs.
This routing rule takes precedence over the primitive-authoring workflow below.

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
| Existing icons to imitate | `user-avatar`, `woman-store-clerk-3-avatar`, `boxer-avatar` |

This is the specialized avatar skill for the **solo family**, not a separate family. An **avatar** combines a head and its own body into one standalone human subject. Author directly on 48x48; it hosts nothing and has no container content slot. Use `icon_set/references/human_ref/user.svg` for the circular head, rounded shoulders, and open bottom. The current avatar rule supersedes its detached layout: head ink touches body ink, with no visible gap.

**Wrong family? Stop.** For an isolated head or a full-body action scene intended at 48, use `/icon-solo`. For an enclosure, use `/icon-container`; for a hosted glyph, use `/icon-sub`. An avatar icon cannot be authored on
another canvas: the base has no profile to override, the registry refuses a
`Solo48` in another folder, and the validator rejects the profile. Do not widen
this skill's scope to "just draw it bigger"; name the right skill and hand over.

- `/icon-sub` — sub family, `SUB32`, 32×32
- `/icon-container` — container family, `CONTAINER64`, 64×64
- `/icon-combination-main` — combination_main family, `COMBINATION_MAIN48`, 48×48
- `/icon-symbol` — symbol family, `SYMBOL32`, 32×32

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
avatar heads touch the body with zero visible gap and use circular face arcs.

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
   matching module in place, including review corrections. Preserve its icon_id, filename, and source metadata; create a variant only when the user explicitly requests alternatives.
   See `icon_set/skills/icon-design/naming.md`.

Before reduction, apply `icon_set/skills/icon-design/reference-triage.md`. If the reference is a
container combination or side combination, route to `/icon-making` to reject
it as one primitive and queue two component briefs. A Pending component brief
already specifies which single component to isolate. For avatar corrections,
update the original module and rebuild its SVG, PNG, manifest and review previews.
Do not leave a v2 beside an outdated original unless alternatives were requested.

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
       category = "avatars"
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

   **Check the exported stroke too.** `validate_icon()` covers vector rules;
   it does not establish that holes/pinches pass. Run the release checker:

   ```python
   from icon_set.validation.library_qa import inspect_icon
   qa = inspect_icon(create("<icon-id>"))
   print(qa["status"], qa["errors"], qa["warnings"])
   print(qa["negative_space"])
   ```

   Require `status == "pass"`, no errors/warnings, and passing negative-space
   checks, including authored-stroke holes. Thinning a stroke can open a tiny
   trapped pocket and hide it inside a larger region; inspect the actual
   4-unit SVG stroke, especially fringe/crown junctions, lapels and collars.
   Enlarge or rebalance a failing opening. Do not ink it over, weaken the
   threshold, or assume a minimum-spacing pass proves the hole is safe.

6. **Family-specific checks.**

- Avatar is a specialized authoring skill within the solo family, using SOLO48 and its six exact inset keyshapes: `CIRCLE` (44×44), `SQUARE` (40×40), `HRECT_L` (44×36), `HRECT_M` (44×32), `VRECT_L` (36×44), and `VRECT_M` (32×44). Fit the whole avatar, including head, hair/headwear and body, to that envelope. Use family `solo`, profile `SOLO48`, base `Solo48`, folder `model/icons/solo/`, and exports `published/solo48/`. Do not introduce an avatar family, profile, base class, registry folder, or export folder. Legacy `_XL` and `_S` rectangle size tokens resolve to their orientation's `_L` bounds and must not be chosen for new work.
- Center the head/face circle on the canvas vertical axis: head_cx = 24 on SOLO48. Measure the face itself, excluding hair, buns and hats; asymmetric accessories must not shift the face off-axis. Fit accessories within the keyshape by rebalancing them. For tall headwear, shorten the body and simplify clothing while preserving a circular face, curved shoulders and head/body contact.
- Read `HEAD_BODY_INK_GAP` and `HEAD_BODY_CENTERLINE_GAP` from this family's `._base`. These derive from `authoring.avatar.head_body_ink_gap` in the profile contract. Head ink must touch body ink: 0 visible gap, or 4 centerline separation for tangent stroke contact with stroke 4. Declare a scoped `connect` only for the actually touching head/body paths; keep the normal MIC for other separate parts. Derive `body_top = head_cy + head_radius + HEAD_BODY_CENTERLINE_GAP`; measure the nearest painted edges for angled poses.
- Body silhouettes must follow `human_ref/user.svg`: broad curved shoulders with smooth tangent joins and short rounded sides. Use arcs or coherent Bezier curves, not straight diagonal shoulders, trapezoids, or boxy sleeve outlines. Differentiate avatars with clothing, collars, seams, and natural arm poses while preserving that curved construction.
- For a set of avatars, plan one recognizable body cue per subject before drawing: an apron, wrap collar, coat fastening, scarf, or natural arm pose. Compare neighboring avatars at native size, especially those sharing similar heads. Do not reuse an identical generic torso for every named subject or invent arbitrary costume details just to make it different; retain the simple bust for a generic user.
- Budget the round head, touching shoulder junction, and torso together inside the inset keyshape. Keep hair/headwear within the same whole-avatar envelope. Leave enough torso height for broad readable clothing openings; simplify details instead of crowding collars, widening the gap, or replacing curved shoulders with angular clothing outlines.
- Head and body are natural parts of one avatar: do not split them into Pending component briefs. A separate badge, enclosure, or state modifier still follows the shared combination triage.
- Use the 48-unit keyshape table above and re-author the reference on the integer grid. The supplied user.svg uses the same 48x48 canvas; use its construction while fitting the chosen keyshape. Keep round caps, tangent shoulder curves, and coherent head/body proportions.
- Verify painted head/body contact in emitted geometry and record the measured zero gap. Face and jaw outlines must use circular arcs with equal radius_x and radius_y, or a full circle; do not stretch or flatten the face into an oval. Hair and headwear may retain subject-specific outlines. Never add false connect relationships or disable holes/pinches to obtain a pass.

7. **Build and look.**

   ```bash
   python3 -m unittest icon_set.tests.test_avatar icon_set.tests.test_profiles_keyshapes
   python3 icon_set/scripts/build.py --family solo --icon icon_set/model/icons/solo/<module_filename>.py --no-report
   python3 icon_set/scripts/contact_sheet.py --family solo --category avatars --theme light --png /tmp/avatar-light.png
   python3 icon_set/scripts/contact_sheet.py --family solo --category avatars --theme dark --png /tmp/avatar.png
   ```

   Replace `<module_filename>` with the original avatar module; repeat `--icon`
   for a batch. This rebuilds those solo icons; `--no-report` skips only
   the library-wide report, not release validation. If shared validation code
   changes, run its relevant regression tests too. Report unrelated test failures
   separately; do not claim the entire suite passed.

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
  `published/solo48/manifest.json`.
- `validate_icon()` is `valid` with no warnings.
- Release QA passes, including holes measured at the actual 4-unit stroke; report its result separately from vector validation.
- Named avatars have recognizable body cues while retaining curved reference shoulders; compare the set at native size.
- Reviewed at native size in both themes for smooth joins, consistent radii,
  balanced negative space, and symmetry wherever the subject supports it.
- State which Lucide construction informed the drawing, or that no useful match
  was found; explain any deliberate asymmetry.
- For human figures, name the shared human reference and verify its proportions
  and zero-gap head/body contact and circular face arcs in the emitted geometry.
