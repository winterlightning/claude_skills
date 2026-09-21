---
name: icon-solo-distilled
description: Author or revise a standalone Pictographic SOLO48 icon using the condensed icon-design-distilled guidance. Use for objects, figures, or reference reconstructions read independently at 48 pixels. Hand-authored; edit this file directly.
---

# /icon-solo-distilled — one standalone subject

Request: $ARGUMENTS

Use `icon_set/skills/icon-design-distilled/` for the shared technique below.
Run commands from the repository root containing `icon_set/`. The current
contracts in `icon_set/model/contracts/` own numeric rules; the repository
workflow owns output paths. Some distilled cross-family examples are stale:
this skill uses SOLO48, ink clearance 4, centerline clearance 8, and `published/`.

## Scope and intake

Author one independently readable subject, including natural groups and scenes.
A cup with its saucer or a person holding a tool remains one subject.

### Review the reference before generation

Render and inspect the reference **before choosing geometry or creating a Python
original**. Classify by meaning and placement, not the supplied `family: solo`
or an automatically prepared brief:

- **Container combination:** a meaningful main wrapper containing a separate,
  centered sub icon (for example, a screen containing an upload arrow). Update
  the source's gallery classification to **container** for later generation.
  Stop generation for this reference in the solo run; do not draw the complete
  combination, extract and draw the wrapper, or start either component now.
- **Side combination:** a main subject with a separate reusable sub icon on its
  side or corner (for example, a folder with a corner plus badge). Record the
  side-combination classification and skip generation for this reference.
- **Standalone:** continue the solo workflow. Intrinsic parts, held objects,
  and natural groups/scenes are not combinations just because they contain
  multiple shapes. Apply `icon_set/skills/icon-design-distilled/reference-triage.md`
  when deciding whether the second element is independent.

Persist the decision against the original source UUID through the gallery's
existing `POST /api/primitives/status` endpoint. In the current schema,
classification uses `status: "skip"` plus `reason: "container"` for a container
combination, or `reason: "combination"` for a side combination. Here SKIP means
excluded from solo generation, not deleted or discarded. Do not merely change
`family` in the exported brief; that does not update the gallery classification.

**Save both component briefs as part of this intake.** Skipping drawing does
not mean skipping preparation. Read the source's current status and reference
brief first, then update the actual reference data used by
`/gallery/primitives.html?view=todo`; a chat report, exported JSON, or a local
handoff file alone does not complete this step.

1. Send one `POST /api/primitives/status` per source UUID containing the
   classification, review note, `main_brief`, and `sub_brief`. Each component
   brief needs `name`, `family`, and `description`. For containers, main family
   is `container` and sub family is `sub`. For side combinations, main family
   is `solo` (or `container` if the main is itself a wrapper), sub family is
   `sub`, and `sub_position` records the observed side/corner.
2. Update the source's saved reference family through
   `POST /api/primitives/briefs` with `uuid`, `family`, and `brief`. Use
   `family: "container"` for container combinations; for side combinations use
   the main component's family. Amend the reference brief to explain the split
   and deferred generation, retaining useful editorial instructions and exact
   source UUID/path. Do not leave an old instruction to draw the whole source
   as a solo icon. The `reason` records the combination type; saved `family`
   records the main's authoring family. There is no `side` family.
3. Read back `/api/primitives/status` and `/api/primitives/briefs` for that UUID.
   Verify the classification, saved family and both component briefs before
   reporting it prepared. It should leave the TODO view and remain available
   under the corresponding skipped classification for later component work.

Container status example (replace placeholders and descriptions with the
actual reference; do not send `sub_position` for containers):

```json
{
  "uuids": ["<source UUID>"],
  "status": "skip",
  "reason": "container",
  "note": "Screen wrapper with a centered upload arrow; generation deferred.",
  "main_brief": {
    "name": "Screen wrapper",
    "family": "container",
    "description": "Draw the empty screen wrapper alone. Exclude the centered upload arrow; leave its interior available for later composition."
  },
  "sub_brief": {
    "name": "Upload arrow",
    "family": "sub",
    "description": "Draw the upload arrow alone. Exclude the screen wrapper. It belongs centered inside the wrapper in the later composition."
  }
}
```

Write concept-specific descriptions from the inspected reference: identify
what each component includes and excludes, its distinguishing features, and
its placement in the future composition. Preserve valid existing component
content and revise it where necessary; do not replace editorial detail with
empty boilerplate. Typeface components specify glyph reuse rather than newly
drawn letters. Keep the original reference artwork unchanged.

Use the existing authorized gallery session or local persistence workflow.
If either save or readback fails, report the UUID and the unsaved fields with
the prepared payload for retry; do not report triage complete. Still skip
drawing that reference and continue the batch. Never fabricate source UUIDs.

This solo intake classifies references and saves their family and two briefs;
it does not start component generation or generation jobs. Later drawing is a
separate task.
An explicitly requested Pending component already identifies one isolated
component: review that component, not the whole combined source, for routing.
For an ambiguous reference, record the uncertainty and skip drawing it in this
run rather than force a container or side classification.

Route hosted modifiers to `/icon-sub`, enclosures to `/icon-container`, content
symbols to `/icon-symbol`, combination main subjects to `/icon-combination-main`,
and standalone profile busts to `/icon-avatar`.

Read `icon_set/skills/icon-design-distilled/intake.md` and
`icon_set/skills/icon-design-distilled/naming.md`. State the subject in one
sentence. Render supplied references and inspect their silhouette, essential
parts and arrangement; reconstruct the subject rather than transcribing SVG
coordinates. Inspect a useful local Lucide original and its atomic geometry,
then re-author its construction principle on this grid. Record what each
reference contributed, or that no useful match was found.

- Humans: first read `icon_set/skills/icon-design-distilled/human-reference.md`
  and inspect the relevant `icon_set/references/human_ref/` artwork. Detached
  heads have exactly 4 units of visible clearance to their own torso/neck,
  with the head aligned to the upper torso axis. Mark each stick figure using
  `self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")`
  with the actual primitive IDs and neck endpoint. Flags do not prove the gap.
- Text or digits: follow `icon_set/skills/icon-design-distilled/typeface.md`;
  reuse `icon_set/typeface/glyphs.json`, never redraw letterforms. Record text
  in combined references as a reuse/layout brief.
- Review revisions: preserve the parent and use
  `icon_set/scripts/create_variant.py` for an independent revision. Otherwise
  search the solo folder for supplied source IDs before creating a duplicate.

## Construction

Read `icon_set/skills/icon-design-distilled/authoring.md`,
`icon_set/skills/icon-design-distilled/symbol-construction.md`, and
`icon_set/skills/icon-design-distilled/geometry.md` before drawing. Keep the
smallest recognizable silhouette and identity-carrying features. Plan typed
shapes, ownership, repeated definitions, shared attachment nodes, and meaningful
symmetry in a compact module comment or docstring. Derive repeats and mirrors
from shared parameters; repair the owner instead of nudging individual points.
Preserve natural asymmetry. Use few coherent curves, consistent radii, and
matching tangents where the silhouette flows smoothly.

SOLO48 is a 48×48 canvas centred at (24,24), integer grid 1, stroke 4,
round caps and joins. Distinct parts need 4 ink / 8 centerline clearance.
The interior guide (6,6)–(42,42) constrains inner details only.

Choose the keyshape before coordinates and design backwards from its extremes.
Read `icon_set/skills/icon-design-distilled/keyshape-fitting.md` when fitting.

| Keyshape | Centerline envelope |
|---|---|
| `CIRCLE` | radius 20 about (24,24); visible radius 22 |
| `SQUARE` | (6,6)–(42,42) |
| `HRECT_L` | (4,8)–(44,40) |
| `HRECT_M` | (4,10)–(44,38) |
| `VRECT_L` | (8,4)–(40,44) |
| `VRECT_M` | (10,4)–(38,44) |

Rectangle ink bounds must match exactly; circle fitting is radial. Query
`Keyshape.HRECT_L.bounds_for(Profile.SOLO48)` for visible bounds. Do not choose
legacy `_XL` or `_S` aliases for new solo work. Budget gaps before detail: a mark
between two walls needs 16 centerline units, normally 17 with curved walls.
Use certifiable exact separation or give curves margin. Human head gaps remain
exact; report unresolved `review` rather than widening them.

Write one Python original in `icon_set/model/icons/solo/`, subclassing `Solo48`
from `._base`, importing `Keyshape` from `...keyshapes`. Set `icon_id`, `keyshape`,
`semantic_role = "MAIN"`, `semantic_kind = "noun"`, `category`, `aliases`, and
`keywords`; implement geometry in `build(self)`. The folder is the registry.

Use a descriptive kebab-case ID; retain supplied `sym-<id>` prefixes. Record
`SOURCE_ICON_ID`, `SOURCE_PATH` (`None` only when absent), and `AUTHOR` as your
actual model in lowercase-hyphenated form. With a source ID, the filename is
`<descriptive_name>_<source_id_with_underscores>.py`; otherwise use the icon ID
with underscores. Preserve editorial metadata and update authorship on edits.

Group contiguous primitives into contours where they should paint as one path.
Circles use two semicircles or four quarters in a closed contour. Split receiving
strokes at genuine shared attachment points and declare only those contacts
with `self.relate("connect", "a", "b")`. A declaration never moves geometry;
crossings are not joins. Keep openings measurable, including within a contour.

## Validate, build, inspect

Read `icon_set/skills/icon-design-distilled/validation.md`. Run
`create("<icon-id>").validate_icon()` using `create` from
`icon_set.model.icons.registry`; inspect `report.describe()`. Completion requires
`valid` with zero warnings. A `review` is unresolved, even if visually approved.

Repair crowding in order: enlarge the opening, rebalance, remove the detail.
Revalidate the whole drawing after each repair, including keyshape fit, repeats,
shared nodes and parallel runs inside contours. Never change profile constants,
tolerances or validation, invent contacts, misuse `FREE`, scale another family,
or patch emitted SVG. If no recognizable fit works, try a suitable diagonal
layout on integer points; otherwise report the failed checks and attempted
layouts for manual review. An exception flag does not waive validation.

Build only the requested original:

```bash
python3 -m icon_set build --icon icon_set/model/icons/solo/<module>.py --no-png --no-report
python3 icon_set/scripts/contact_sheet.py --family solo --theme light --png /tmp/solo-distilled-light.png
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo-distilled-dark.png
```

Inspect the actual renders at 48 pixels in both themes: recognition, curve flow,
relative proportions, negative space, and intentional symmetry or asymmetry.
Numeric success alone is not visual approval. Confirm the icon's export in
`published/solo48/manifest.json`. Do not seed library metadata, overwrite browser
edits, or run a full-library build as a side effect. Before an authorized icon
commit, run `python3 -m icon_set publish` and include source and output together.

Report the subject, keyshape rationale, omitted details, references used,
validation status, visual findings, and output paths. Name unresolved checks and
elements explicitly; do not claim completion or visual review without evidence.
