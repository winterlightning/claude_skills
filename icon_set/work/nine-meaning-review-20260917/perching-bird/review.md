# perching-bird

- Intended concept: perching bird.
- Meaning assessment: **convincing**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `0f8fae80-7c30-4fdb-9d48-8b632249f687`.
- Python source: [wild_bird_0f8fae80_7c30_4fdb_9d48_8b632249f687.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/wild_bird_0f8fae80_7c30_4fdb_9d48_8b632249f687.py).
- Reference: `pictographic-primitives/animals/wild bird_0f8fae80-7c30-4fdb-9d48-8b632249f687.svg` (rendered).
- SVG SHA-256: `a0691e068727fa23a6fb91beab93f6297af0dc143186cbc8719f25a0c7b02cd0`.
- Profile: SOLO48; current FREE visible bounds (2, 2, 46, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A bird on a perch, with an eye and beak, but its back/tail form a triangular slab and its single leg resembles a pedestal.

## Actionable observation

bird uses a long straight diagonal from the crown area to the tail tip. wing is only a tiny bent dab. leg meets the breast at a visible bump and continues as one thick support into a long branch.

## Symmetry and expected relationships

Intentional left-facing profile asymmetry. No whole-object mirror axis. If two legs are used, derive their thickness, stance and branch contact from shared dimensions; do not mirror the entire bird. Confidence high.

## Keyshape decision and profile budget

Retain approved FREE (2,2)-(46,46), 44×44. The envelope permits a rounded breast, shorter tail and clearer perch relationship; no further enlargement is needed.

## Authoring brief

With icon-solo, soften the back into the head, shorten and separate the tail projection from the rounded breast, and replace wing with a coherent curved folded-wing boundary. Rebuild the leg/branch attachment without a spur; use two short legs if 8-unit centerline separation fits, or one clearly articulated gripping foot instead of a pedestal. Retain eye and leftward beak. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

Keep the already recognizable bird-on-perch meaning, while removing the wedge silhouette, wing dab and attachment bump. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
