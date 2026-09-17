# paw-print

- Intended concept: paw print.
- Meaning assessment: **convincing**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1`.
- Python source: [paw_print.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/paw_print.py).
- Reference: `pictographic-primitives/animals/animal print paw_3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1.svg` (rendered).
- SVG SHA-256: `349be3c77a7ea23499030d488fa62a18f0270ee9a39e0c94b2a42c9bba0eea3b`.
- Profile: SOLO48; current FREE visible bounds (1, 2, 47, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A paw print, but the four circular rings are widely spread and the central pad is an angular bell-like shape.

## Actionable observation

pad changes tangent at its two lower outer shoulders, producing matching visible bumps. Circular upper/outer toes read as beads instead of soft pads, and the widely splayed outer toes weaken the compact footprint silhouette.

## Symmetry and expected relationships

Whole-object mirror about x=24, axis (24,0)-(24,48), high confidence. Both toe pairs and pad should remain mirrored. Current symmetry does not excuse identical kinks on both sides.

## Keyshape decision and profile budget

Current FREE bounds (1,2)-(47,46), 46×44. Consider SQUARE bounds (4,4)-(44,44), 40×40, as a reconstruction hypothesis: aspect 1.045→1, centerline envelope 42×40→36×36. Reduce outer spread and rebalance pad height; do not simply scale. Retain the current custom envelope if a rounded-toe candidate cannot meet 8-unit centerline clearance in SQUARE.

## Authoring brief

With icon-solo, rebuild one smooth half of pad and mirror it. Use a rounded top lobe, broad side lobes and a shallow bottom cleft with tangent-continuous joins. Arrange four softly oval toes in a compact arch using shared paired dimensions. Rebudget the pad-to-toe spacing before choosing toe radii. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

The footprint should stay immediately recognizable, with no lower-shoulder nicks and a coherent compact silhouette at 48 px in both themes. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
