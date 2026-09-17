# paw-print-small-outer-toes

- Intended concept: paw print small outer toes.
- Meaning assessment: **convincing**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `193cadb3-56bf-56a6-8cdf-a6db99d7d95e`.
- Python source: [paw_print_small_outer_toes.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/paw_print_small_outer_toes.py).
- Reference: `pictographic-primitives/animals/animal print_193cadb3-56bf-56a6-8cdf-a6db99d7d95e.svg` (rendered).
- SVG SHA-256: `c01885d68e17434c4ea438fc73b586eaefee7bb005a8da9e56e39430cc8c9b3a`.
- Profile: SOLO48; current FREE visible bounds (2, 2, 46, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A paw print with small outer dots and ring-shaped inner toes; the requested size distinction is visible, but the rendering styles differ.

## Actionable observation

The two radius-2 outer circles have zero nominal hole diameter under the 4-unit stroke and therefore read solid. The radius-3 inner circles retain tiny holes. pad has the same mirrored tangent kinks as paw-print.

## Symmetry and expected relationships

Whole-object mirror about x=24, axis (24,0)-(24,48), high confidence. Mirror left/right toes while preserving the intentional inner-versus-outer size difference.

## Keyshape decision and profile budget

Retain the approved FREE 44×44 envelope (2,2)-(46,46) for the first reconstruction; there is more room than standard SQUARE 40×40. This is a local radius and pad-proportion problem. Larger outlined outer toes will require rebalancing the upper pair and pad, not crowding.

## Authoring brief

With icon-solo, share the smooth pad construction with paw-print. Keep outer toes smaller but large enough to preserve visible openings consistent with the inner pair; trial outer radius 3 and inner radius 4, with explicit spacing/layout budgeting before committing. Reduce pad height or adjust arch positions if necessary. Do not keep small-circle exceptions as evidence of a visually good toe. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

Both pairs should look like the same type of rounded pad, with clear size hierarchy and smooth central pad. The trial radii are unvalidated until a candidate is rendered and checked. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
