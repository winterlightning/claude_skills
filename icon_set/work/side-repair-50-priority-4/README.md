# Side-combination repair batch 4

Reviewed 50 currently failing side SUB32 profiles against their complete sources, enlarged centerlines and native light/dark renders.

- 30 independently editable variants pass model and export checks and are selected for the side role.
- 20 remain unresolved with per-source reasons in audit.json and batch-local primitive status. A skipped source is not counted as repaired.
- 25 repaired profiles also pass container-circle composition. The five wide shared-typeface labels C5, CSS, CSV, PHP and XML preserve 32px ink height and natural width; their eventual side placement must accommodate that width. They are not certified for square container placement.
- Shared A is centered before grid fitting; its existing quadratic apex is preserved instead of clipping the control point. Repeated C, S and P glyphs remain geometrically identical across the labels. The shared glyph catalog is unchanged.
- 30 side role selections and 31 source-profile links were updated. Independent symbol versions, all 50 parent models and all complete original sources are preserved. No human approvals or manual artwork state were changed.
- Current side inventory: 825 total, 734 passing, 81 failing, 10 needing review; 91 still need attention. Of those, 69 have documented unresolved issues and 12 unreviewed failures are next in the queue.
- Existing cached combined SVGs were not regenerated. Legacy pair eligibility is unchanged: 1,626 with a passing sub option, 124 waiting, and 7 legacy mapping issues.

Open index.html for all 50 comparisons. verification.json, composition-checks.json and text-verification.json contain the recorded checks. Test suite: 42 passed. Build output belongs only in icon_set/.local/dist; this work folder is the review evidence, not a production release.
