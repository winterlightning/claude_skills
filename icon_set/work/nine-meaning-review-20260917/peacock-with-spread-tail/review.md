# peacock-with-spread-tail

- Intended concept: peacock with spread tail.
- Meaning assessment: **weak**. Visual verdict: **repair**.
- Numeric QA: **pass**, separate from the visual verdict.
- Original source ID: `9e421611-5f19-400d-8a51-23357e8cb95c`.
- Python source: [peacock_with_spread_tail_9e421611_5f19_400d_8a51_23357e8cb95c.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/peacock_with_spread_tail_9e421611_5f19_400d_8a51_23357e8cb95c.py).
- Reference: `pictographic-primitives/animals/peacock feathers up_9e421611-5f19-400d-8a51-23357e8cb95c.svg` (rendered).
- SVG SHA-256: `241cf18635cd26de75f18a0d25b0a7d5e649053615778dcae5d6423a3ef7227b`.
- Profile: SOLO48; current FREE visible bounds (0, 2, 48, 46); 48×48 canvas, integer grid, stroke 4, round caps/joins, minimum distinct-part ink clearance 4 (8 on centerlines).

[Fresh light/dark render](sheet.png) · [Source reference](reference.png) · [Measured evidence](evidence.json)

## What it currently communicates

A small ring-bodied bird or stick figure inside a rounded frame; the outline can also resemble headphones.

## Actionable observation

fan has a flat upper stretch and stepped shoulders instead of a radiating feather fan. body is a perfect ring, neck a straight stalk, feet an X-like fork. eye-l=(11,22) and eye-r=(37,24) are two units out of level despite symmetric fan geometry.

## Symmetry and expected relationships

Local mirror/radial organization: fan, feather pattern, body and feet centered on x=24; head/beak intentionally face right. The feather eyes should form mirrored pairs or an explicitly spaced radial series. High confidence. Current unequal dot heights have no visible perspective justification.

## Keyshape decision and profile budget

Keep the authorized FREE (0,2)-(48,46), 48×44, to spend the width on a broad tail. The main defect is internal construction, not lack of canvas. A fan and small bird body must share the width without becoming concentric outlines.

## Authoring brief

With icon-solo, construct a broad semicircular or gently scalloped fan from a single center, with a sparse mirrored radial feather pattern. Replace the body ring with a tapered pear-shaped bird torso, a curved neck, readable small head/beak and separated short feet. Use a shared axis for the body/tail and shared polar or mirrored parameters for feather marks; omit surplus detail before reducing clearance. Preserve the original registered ID and edit it in place per the user's standing instruction. Do not change checker thresholds, invent contacts, or patch generated SVGs.

## Acceptance evidence

At native size, the dominant read should be a bird in front of a spread feather fan, not a figure in a frame. Confirm feather pairing geometrically and visually; keep head direction intentional. Render a before/after comparison in light/dark at native size; rerun the unchanged model and full build QA and verify source/export hashes. A candidate must improve meaning as well as pass the checks.
