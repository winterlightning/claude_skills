# Side-combination sub repair batch 3

50 failed side sub-icons reviewed against original SVGs, enlarged centerlines, and native light/dark renders. 39 independent repairs pass model and exported-SVG validation. 11 remain unresolved; specific reasons and the complete source are shown in the review.

37 repaired models also pass container-circle composition. CC and CCPA are the two exceptions to square placement: the user requested 32-unit ink height and natural width for text. Their shared-glyph geometry passes, but circle-container placement does not; an eventual side layout must accommodate their full width. No text was squeezed or resized during combination. The shared C geometry is identical in CC and CCPA. Dollar uses symbol-dollar. The 0% attempt retains a spacing failure and is not activated.

39 side profiles, 57 source-profile links and 30 legacy pair rows updated. Original Python models and all 50 source SVGs preserved. Independent container symbols and manual review state unchanged. Cached combined SVG previews were not regenerated.

Side-library progress: 704 of 825 passing; 111 failed checks and 10 review warnings remain (121 total needing attention). Of 1,757 legacy pairs, 1,626 have a passing sub option, 124 await one, and 7 require mapping. These are geometry eligibility counts, not rendered-placement approvals.

All 42 regression tests passed. See verification.json for source-preservation and linkage checks, text-verification.json for shared-glyph and repeated-letter checks, and composition-checks.json for the separate placement results.

Keyshapes: each square-profile repair is constructed to the named model envelope at 4px stroke, preserving the source orientation and primary aspect. CIRCLE is used for the enclosing circular arrow icon. Narrow vertical subjects use VRECT_XL, wider horizontal subjects HRECT_XL, and full-envelope subjects SQUARE. Typeface layouts use the explicit natural-width text specialization. Per-icon construction references and complete part inventories are in audit.json and the Python variants. No human approval is implied.
