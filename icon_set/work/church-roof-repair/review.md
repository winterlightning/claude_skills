# Church roof centerline correction

The previous `a-frame-church-sub32-v2` passed bounds and symmetry checks but had a visible kink on both roof slopes. On the left, `(4,22) → (8,19)` had slope −3/4 while `(8,19) → (16,10)` had slope −9/8. Rounded joins concealed this structural defect in the earlier small preview. The supplied original uses straight roof slopes.

The corrected v3 model derives the roof apex, wall attachments and eaves from one 45-degree roof construction. Moving the wall attachment up one unit gives `(4,22) → (8,18) → (16,10)`, with both segment slopes exactly −1; the right side is its mirror. The walls still join at their actual roof endpoints. The cross, doorway, base, stroke, keyshape and source identity are retained.

[Centerline and artwork comparison](centerlines.png) shows actual model geometry in blue with roof junctions marked red, alongside enlarged and native-size light/dark artwork. These were visually inspected. Cross products verify exact collinearity and positive dot products verify forward continuity; a dedicated regression test checks this relationship.

Full artwork QA passes without errors or warnings. The standard circular-container composition also passes. Earlier variants remain preserved, and active sub pairings and the SOLO48 relationship now point to v3. No gallery approval, profile constant or validator threshold was changed.
