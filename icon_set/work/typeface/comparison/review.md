# Original versus authored typeface

Scope: all 37 sources in `Letters/`, freshly rendered against their current registered Python models. Uppercase A–Z has no supplied uppercase reference and is excluded from source-fidelity claims.

The comparison panels normalize visible ink height while preserving aspect ratio. This isolates silhouette/proportion differences; it is not a comparison of original canvas placement or composed x-height. The source generally has heavier strokes relative to its visible letter height. Changing the text composer's stroke width can address weight, but cannot restore changed shapes.

Overall finding: the redraws are recognizable, but several are not faithful enough to the supplied typeface. Priority repairs: j, r, s, c, e, f, m and digit 2. Baseline normalization does not repair these underlying drawings.

All 37 current models pass full numeric build QA. Those passes certify the geometric rules, not fidelity. Current SOLO48 is 48×48, stroke 4, MIC 4, round caps/joins. Relevant visible envelopes: VRECT_M (8,2)–(40,46), SQUARE (4,4)–(44,44), HRECT_L (2,6)–(46,42), CIRCLE radius 22 around (24,24).

## Inspected evidence

- [Comparison 1](comparison-1.png): digits and a–f.
- [Comparison 2](comparison-2.png): g–u, including both o references.
- [Comparison 3](comparison-3.png): v–z.
- [Detailed r evidence](letter-r/sheet.png) and [original](letter-r/reference.png).
- [Detailed j evidence](letter-j/sheet.png) and [original](letter-j/reference.png).
- [Per-source hashes and numeric findings](evidence.json).

## Individual findings

| Icon | Concept match | Visual verdict | Current keyshape | Finding / owning repair | Symmetry intent |
|---|---|---|---|---|---|
| digit-0 | convincing | keep | VRECT_M | Close capsule silhouette; keep. | vertical local bowl/spine balance |
| digit-1 | convincing | repair | VRECT_M | Baseline and top flag are proportionally wider; restore a narrower footprint before text use. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-2 | convincing | repair | VRECT_M | Rounded lower turn was replaced by a sharp diagonal-to-baseline corner; rebuild the lower turn with a tangent arc. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-3 | convincing | repair | VRECT_M | Bowls became wider and flatter; restore rounder lobes with matched dimensions. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-4 | convincing | keep | VRECT_M | Narrower overall; the open four remains convincing. Keep unless strict source proportions are required. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-5 | convincing | repair | VRECT_M | Upper arm and lower bowl widened; restore the more compact source proportion. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-6 | convincing | keep | VRECT_M | Close overall; bowl and upper stem have modest proportion changes. Keep. | vertical local bowl/spine balance |
| digit-7 | convincing | keep | VRECT_M | Close overall; keep the diagonal direction and open form. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| digit-8 | convincing | repair | VRECT_M | Source has rounded rectangular counters; redraw uses elliptical counters. Rebuild the repeated counter shape rather than simply changing weight. | vertical local bowl/spine balance |
| digit-9 | convincing | repair | VRECT_M | Upper counter became rounder and more prominent relative to the tail. Rebalance bowl and lower terminal. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-a | convincing | repair | SQUARE | Rounder counter and lower stem attachment replace the source upper-right straight section. Recognizable, but restore the source bowl-to-stem relationship for fidelity. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-b | convincing | repair | VRECT_M | Bowl became a full circle attached at its side midpoint. Source has a flatter left junction. Restore that local transition if retaining the source design. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-c | convincing | repair | SQUARE | Wider and flatter, with more horizontal top/bottom contours and a larger opening. Rebuild the bowl with rounder shoulders and inward-facing terminals. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-d | convincing | repair | VRECT_M | The circular bowl simplified the flat right-side junction; same issue as b, mirrored. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-e | convincing | repair | SQUARE | Lower bowl and right opening became wide and flat. Rebuild a rounder lower curve while preserving the attached crossbar. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-f | convincing | repair | VRECT_M | Shoulder and crossbar extended sideways substantially. Shorten the shoulder terminal and narrow the crossbar together. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-g | convincing | repair | VRECT_M | Descender hook is wider and flatter, and the closed bowl is more circular. Restore the tighter hook and source proportions. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-h | convincing | keep | VRECT_M | Close structural match, with a slightly larger, rounder shoulder. Keep. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-i | convincing | repair | CIRCLE | Identity retained; dot-to-stem gap increased relative to the body. Review the gap alongside j at the text x-height. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-j | convincing | repair | VRECT_M | Hook is dramatically wider and rounder; relative stem length is reduced. Rebuild a narrow stem and compact hook; then re-establish its body band for text composition. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-k | convincing | keep | VRECT_M | Close structural match. Keep its intentional diagonal asymmetry. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-l | convincing | keep | CIRCLE | Same plain upright form. Keep; its narrow radial envelope is appropriate. | vertical stem axis x=24 |
| letter-m | convincing | repair | HRECT_L | Narrower relative to height, with taller pointed-looking arches. Restore two lower, wider matching shoulders. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-n | convincing | keep | SQUARE | Close structural match; keep the shared arch and two equal stems. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-o | convincing | keep | SQUARE | Circular form preserved. Keep; lighter weight relative to the source is a separate styling difference. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-o-large | convincing | keep | CIRCLE | Circular form preserved. Keep; original alternate source remains distinct. | radial symmetry around (24,24) |
| letter-p | convincing | repair | VRECT_M | Full circular bowl replaces the source flatter left join. Coordinate the repair with b/d/q. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-q | convincing | repair | VRECT_M | Full circular bowl replaces the source flatter right join. Coordinate the repair with b/d/p. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-r | weak | repair | VRECT_M | The upright now flows into an oversized corner-shaped shoulder, losing the short rising stem above the branch. Weak match: restore a visible stem top and a compact separate shoulder. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-s | convincing | repair | SQUARE | Much wider and flatter, with near-horizontal lobes. Restore a narrower silhouette and diagonal flow through the waist. | rotational lobe relationship around (24,24) |
| letter-t | convincing | repair | VRECT_M | Crossbar and bottom foot widened. Shorten both while retaining the distinct upper extension. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-u | convincing | repair | SQUARE | Wider lower bowl; restore a narrower footprint while preserving the mirrored stems. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-v | convincing | repair | SQUARE | Bottom is sharper and footprint wider. Restore a rounded vertex with tangent transitions. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-w | convincing | repair | HRECT_L | Lower vertices are sharper and the broad source rhythm changed. Rebuild paired rounded valleys together. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-x | convincing | keep | SQUARE | Same crossed-diagonal structure. Keep symmetry about both axes; source is heavier. | vertical mirror of paired stems/curves, centered on x=24 |
| letter-y | convincing | keep | VRECT_M | Close recognizable structure; terminal hook geometry has small changes. Keep. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |
| letter-z | convincing | repair | SQUARE | Noticeably wider, with sharper corners. Restore narrower proportions and rounded turns. | Intentional character asymmetry; preserve local matching bowl radii where applicable. |

## Repair brief (not executed)

Use `$icon-solo` and create independent variants, preserving the reviewed parents. Start with j/r: their authored `stroke-0` owns the excessive hook/shoulder width. Restore the original compact form and r's stem/branch distinction. The VRECT_M envelope is already the narrowest upright rectangle (32×44 visible); a CIRCLE radial-envelope candidate may retain a naturally narrow glyph without extending its terminal to reach a rectangle edge. This needs a fresh candidate and exact radial-fit validation, not a token change.

For c/e/s, SQUARE's 40×40 envelope contributes to a wider silhouette, especially s. Compare a VRECT_M (32×44 visible) reconstruction for s and rounder local bowl construction for c/e. Rebuild the owning lobes from shared radii and smooth tangent transitions; preserve e's crossbar and the open terminals. For digit 2, replace the lower corner within `stroke-0` with a tangent curve while retaining the cap line and baseline. Other repairs are specified per row above. No candidate is yet demonstrated or validated.

Acceptance: compare native-size light/dark views with the source, then equal-visible-height panels. Confirm recognizable characters, more faithful width/height and curve rhythm, smooth joins, and unchanged grid/envelope/MIC/negative-space checks. Re-evaluate text body metrics after a shape repair. Do not relax profile constraints or patch exported SVGs.

No icon geometry or approval status was changed by this review.
