# cough

- Intended concept: cough.
- Meaning assessment: **weak**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `bc3ea9f7-36ca-4b3a-a099-e36c89039b41`.
- Python source: [cough_bc3ea9f7_36ca_4b3a_a099_e36c89039b41.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/cough_bc3ea9f7_36ca_4b3a_a099_e36c89039b41.py).
- Reference: `pictographic-primitives/health/cough_bc3ea9f7-36ca-4b3a-a099-e36c89039b41.svg` (rendered).
- SVG SHA-256: `cdba2ead03a9ef0a9afe8e3fe22389bc46c85e52f163acad2441f2076db6e758`.
- Profile: SOLO48; current FREE visible bounds (2, 2, 46, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A head in profile with two detached emphasis/breath marks; speaking or exhaling is as plausible as coughing.

## Actionable observation

The head has no identifiable open mouth. cough-upper and cough-lower do not visibly originate from a mouth; the face/nose/jaw are an angular staircase.

## Symmetry and expected relationships

Intentional left-facing asymmetry. No whole-object mirror axis. The two breath strokes form a local fan around mouth height, not a symmetric head. Confidence high.

## Keyshape decision and profile budget

Retain the approved FREE visible bounds (2,2)-(46,46), 44×44. The envelope is adequate; the missing mouth/action relationship is the problem.

## Authoring brief

With icon-solo, retain the left-facing head and rounded cranium. Rebuild the mouth section of head as an open-mouth notch around the emission origin; soften the chin transition. Derive two or three outward-diverging cough marks from that mouth location, giving them space by narrowing/repositioning the head within the same envelope. Do not add a hand unless the action still reads ambiguously and a candidate can retain the required clearances. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

At 48 px, the marks should read as an abrupt expulsion from an identifiable mouth. Compare with the present talking/exhaling reading. Preserve the existing stroke and spacing rules. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
