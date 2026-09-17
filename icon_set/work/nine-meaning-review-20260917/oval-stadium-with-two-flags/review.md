# oval-stadium-with-two-flags

- Intended concept: oval stadium with two flags.
- Meaning assessment: **weak**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `2bedb9d2-a20f-5959-916c-51b7841e2d87`.
- Python source: [oval_stadium_with_two_flags_2bedb9d2_a20f_5959_916c_51b7841e2d87.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/oval_stadium_with_two_flags_2bedb9d2_a20f_5959_916c_51b7841e2d87.py).
- Reference: `pictographic-primitives/building/stadium classic_2bedb9d2-a20f-5959-916c-51b7841e2d87.svg` (rendered).
- SVG SHA-256: `3458fe276c30748058c529f66f5dfebbcb0067c9e85eef5c449d58b5b09e8ce6`.
- Profile: SOLO48; current FREE visible bounds (2, 2, 46, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

An oval bowl or drum with two bent poles; the large enclosure is clearer than the flags or stadium identity.

## Actionable observation

flag-* consists only of a pole and one sloping stroke, so no pennant area exists. The tall poles dominate the shallow rim. rim and wall read like household bowl edges; poles are related to rim without shared attachment endpoints.

## Symmetry and expected relationships

Local mirror for rim and wall about x=24, axis (24,0)-(24,48), high confidence. Flags should be instances of one shared shape with consistent dimensions and placement. Cloth can intentionally point right; do not mirror the entire flag group merely to force symmetry. Preserve exactly two flags.

## Keyshape decision and profile budget

Retain approved FREE (2,2)-(46,46), 44×44, while reconstructing flags and bowl proportions together. Keep 4-unit strokes and 8-unit centerline clearance. Closed pennants require real interior room, so enlarging cloth and shortening exposed pole is preferable to shrinking the same tiny triangle.

## Authoring brief

With icon-solo, use a shared complete pennant definition and exactly two instances. Trial an 8-wide, 16-high triangular cloth, which allocates substantially more opening than the former 6-wide broken stroke; three flags can use a 16-unit horizontal repeat. This is an unvalidated construction proposal. Give every pole a true split/shared attachment on the rear rim. Broaden the arena opening and reduce the front bowl depth; consider one clear inner seating/field arc only if it survives the spacing budget. Avoid a kitchen-bowl silhouette. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

At 48 px, viewers should see two flags, an open arena and a stadium wall. Flag count and cloth must remain legible in both themes. Check closed-flag holes, rim spacing, pole attachment and repeated dimensions without exceptions to those checks. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
