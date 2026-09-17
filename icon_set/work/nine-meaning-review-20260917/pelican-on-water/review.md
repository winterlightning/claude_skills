# pelican-on-water

- Intended concept: pelican on water.
- Meaning assessment: **weak**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `a64f3ff4-3dac-4e77-9941-a21f45a74c31`.
- Python source: [pelican_on_water.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/pelican_on_water.py).
- Reference: `pictographic-primitives/animals/pelican_a64f3ff4-3dac-4e77-9941-a21f45a74c31.svg` (rendered).
- SVG SHA-256: `81994556442690db571f7b0ca73567760e847f07b8e361bc8e812b9f7bec9539`.
- Profile: SOLO48; current FREE visible bounds (2, 2, 46, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A pouch-billed waterbird is suggested, but the dominant silhouette resembles a numeral 2 with a bowl attached and an underline.

## Actionable observation

bird has no eye and an open/incomplete belly. The neck turns directly into a narrow upward-pointing crescent, leaving little distinct torso. bill has a nearly vertical rear edge and oversized bowl-shaped pouch. water is exactly straight, not a ripple.

## Symmetry and expected relationships

Intentional left-facing side-profile asymmetry; no whole-object mirror axis. Review local curve tangencies and bill/neck/body connections instead. Confidence high.

## Keyshape decision and profile budget

Current approved FREE is 44×44 at (2,2)-(46,46). Test HRECT_L (2,6)-(46,42), 44×36, aspect 1→1.222 and centerline space 40×40→40×32. The hypothesis is a lower, longer bird with room allocated horizontally to bill and torso; keep the current custom envelope if the water separation cannot fit.

## Authoring brief

With icon-solo, rebuild a continuous floating belly and broad folded wing/torso. Shorten the upright neck and extend the long flat bill, with a shallower curved pouch hanging beneath it. Add an eye if it survives the spacing budget. Use one shallow water ripple below the belly, keeping its separation real. Preserve left-facing orientation. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

The long bill and hanging pouch should identify a pelican; body and water should read together as floating, and the numeral-2 reading should recede. Compare current and HRECT_L candidates at 48 px. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
