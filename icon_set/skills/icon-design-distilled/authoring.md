# Authoring technique

**Reduce.** One sentence for the subject. Keep the smallest recognizable silhouette, the identity-carrying features, nothing that dies at native size. Detail budget: 32 px is eight stroke widths (two levels of detail), 48 is twelve (one more feature), 64 is sixteen (interior furniture expected).

**Keyshape first, design backwards.** Choose from the subject's proportions, write the four centerline extremes, place geometry to reach exactly those.

**Aesthetic: Lucide geometry, smooth curves, balance where it helps.** Inspect a related Lucide original and its atoms when one exists (people: human reference first). Take the construction principle, re-author on this grid. Mirror and balance only where they preserve meaning; a palm tree keeps its lean.

Before placing points:
- Pick the symmetry axis if any. Derive the other side: `x_right = 2*axis_x - x_left`. Share paired radii, heights, spacing. Check negative space symmetry too.
- Rotated symmetric parts: reason on the local axis, land on integers. Explain deliberate asymmetry.
- Few coherent runs and arcs. Consistent radii for equivalent features. Matching tangents where curves flow. Keep purposeful corners; do not round everything.

**Tangent-continuous joins.** Curve to curve: match tangents. Curve to line: aim the line along the tangent. A kink mid-contour is the commonest reason a valid icon looks wrong. Two tools: put a shared axis extreme at the junction so both parts are horizontal or vertical there; give a straight run the angle of the tangent it leaves.

**Spacing.** Ink clearance 2 / 4 / 2 for SUB32 / SOLO48 / CONTAINER64, i.e. 6 / 8 / 6 on centerlines. Straight pairs may sit exactly on the minimum. Curved pairs need margin unless exact axis separation can be certified (cardinal quarter/half ellipses, control hulls). A contour with curved corners makes the whole pair "curved". Declare true contacts with `relate("connect", a, b)`; that excuses that pair only.

**Gap too small, in order, stop at the first that keeps recognition:** 1 enlarge the opening; 2 rebalance (dominant part down, crowded detail up, recentre); 3 remove the part and record it. Never squeeze, never shrink a detail past measurability, never nudge a crossing so a wedge inks over. Every rung moves paint: re-check the keyshape after each.

**Optical judgment.** Inspect paint, not centerlines. If two candidates are close, render both and keep the stronger. Good icons have one dominant mass, clear symmetry or deliberate asymmetry, few internal relationships, negative space that survives.

**Native-size review is mandatory** in both themes via `contact_sheet.py --family <fam>`. Validators prove rules; only looking proves legibility.
