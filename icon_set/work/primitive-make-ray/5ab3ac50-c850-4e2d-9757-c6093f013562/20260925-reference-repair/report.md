# hemisphere-globe-grid

True semicircular half globe, flat right cut, equator and curved meridian. Preserve the source half-circle aspect rather than the previous widened half ellipse.

- Source: `pictographic-primitives/other/half globe_5ab3ac50-c850-4e2d-9757-c6093f013562.svg`
- Source UUID: `5ab3ac50-c850-4e2d-9757-c6093f013562`
- Author: gpt-6
- Keyshape: VRECT_M, expected ink [8, 2, 40, 46]. Narrowest upright rectangle; the faithful half-circle still falls four units inside each horizontal bound.
- Automatic QA: **fail**. Acceptance: **user-approved-exception**.

True semicircle restores the source aspect and vertical cut. Equator and curved meridian remain legible. Spacing, holes and symmetry pass; the exact keyshape width does not.

Construction references: Lucide globe: circular graticule; supplied half-globe silhouette owns the vertical cut. Local Lucide originals and atomic-debug geometry were inspected.

Simplifications: No defining source feature omitted.

The only unresolved strict check is the horizontal keyshape envelope. A true 20-radius semicircle cannot fill the narrowest 28×40 centerline rectangle without changing its aspect. The source vertical cut is retained. The earlier widened drawing is preserved as `before.svg`; the local exception does not alter the validator.

[SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5ab3ac50-c850-4e2d-9757-c6093f013562/20260925-reference-repair/hemisphere-globe-grid.svg) · [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5ab3ac50-c850-4e2d-9757-c6093f013562/20260925-reference-repair/hemisphere_globe_grid_5ab3ac50_c850_4e2d_9757_c6093f013562.py) · [Full QA](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5ab3ac50-c850-4e2d-9757-c6093f013562/20260925-reference-repair/qa.json)

![Light preview](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5ab3ac50-c850-4e2d-9757-c6093f013562/20260925-reference-repair/light-192.png)
