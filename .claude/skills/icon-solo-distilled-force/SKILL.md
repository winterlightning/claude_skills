---
name: icon-solo-distilled-force
description: Author or revise any requested input as a Pictographic SOLO48 icon using condensed icon-design-distilled guidance. Use when solo output is required regardless of input family, including combinations, wrappers, modifiers, symbols, and avatars, without intake classification or rerouting. Hand-authored; edit this file directly.
---

# /icon-solo-distilled-force — always author SOLO48

Request: $ARGUMENTS

Use `icon_set/skills/icon-design-distilled/` for the shared technique below.
Run commands from the repository root containing `icon_set/`. The current
contracts in `icon_set/model/contracts/` own numeric rules; the repository
workflow owns output paths. Some distilled cross-family examples are stale:
this skill uses SOLO48, ink clearance 4, centerline clearance 8, and `published/`.

## Forced solo intake

Create one solo-family SOLO48 icon for each requested input, regardless of its
supplied family, saved classification, or apparent combination structure.
Wrappers with hosted symbols, subjects with corner badges, standalone modifiers,
text, avatars, and natural groups all use `Solo48` in
`icon_set/model/icons/solo/` in this workflow.

Do not perform an intake eligibility review, recategorize the source, skip it
because of its family, split it into component briefs, or hand it to another
icon skill. Do not write classification changes, SKIP statuses, or deferred
component briefs to the gallery. Existing source classifications remain source
metadata; they do not control the output family.

Preserve the whole requested composition in one Python original. For example,
a screen with an upload arrow includes both screen and arrow; a folder with a
plus badge includes both folder and badge. If the request explicitly targets
one isolated component, draw that component alone, still as SOLO48. Simplify
nonessential detail to fit while preserving the intended meaning and arrangement.
For an ambiguous input, choose a reasonable interpretation and state it instead
of deferring generation for classification.

This forced-family rule overrides routing, triage, splitting, and deferral advice
in the shared references below. Do not load `reference-triage.md` for this
workflow. Reference viewing is for understanding and reconstructing the artwork,
not for deciding whether it qualifies as solo. Keep the construction, validation,
and final render checks: forcing the family does not waive geometry requirements
or make an unresolved drawing a valid result.

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
  reuse `icon_set/typeface/glyphs.json`, never redraw letterforms. Incorporate
  reused glyphs into the requested solo composition rather than saving a separate
  deferred text brief. Report missing glyphs as unresolved; keep the output solo.
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
python3 icon_set/scripts/contact_sheet.py --family solo --theme light --png /tmp/solo-distilled-force-light.png
python3 icon_set/scripts/contact_sheet.py --family solo --theme dark --png /tmp/solo-distilled-force-dark.png
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
