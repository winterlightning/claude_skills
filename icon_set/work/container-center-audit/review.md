# Container center audit

Audited all 210 current exported container SVGs, including 174 mapped main containers. Source identities and all 207 safe-zone buffer exclusions verified. Three overlays retain center (32,32), without a safe-zone claim.

Center is the area centroid of the chosen usable face, rounded to half a unit; this is different from the outer icon bounds or the largest fitting-circle center. Prior hand-picked anchors were not consistently centered. 136 points changed by more than 0.5 units.

Confidence: 158 High, 44 Medium, 8 Low. Scores are reproducible evidence ratings, not calibrated probabilities. A 100/100 rubric score does not certify optical placement for every sub icon. See index.html for the formula and each component.

Evidence: per-icon source hashes, before/after coordinates, centroid, bounds midpoint, maximum-circle comparison (equal-radius ties favor centroid), zone-edge distances, mirror overlap, seven enlarged review sheets, and two native-size sheets. Distances are in 64-unit canvas coordinates. Raster safety is separate from later vector validation of actual pairs.

## Largest corrections

- heart-shaped-leaf: [32, 32] → [32.0, 23.0]; moved 9.0 units.
- takeaway-cup-with-straw-container: [32, 32] → [32.0, 39.0]; moved 7.0 units.
- simple-folded-booklet: [27, 42] → [32.0, 38.0]; moved 6.403 units.
- water-droplet-container: [32, 32] → [32.0, 38.0]; moved 6.0 units.
- target-crosshair-symbol: [32, 38] → [32.0, 32.0]; moved 6.0 units.
- tnt-detonator-plunger: [26, 44] → [21.0, 41.0]; moved 5.831 units.
- round-bottom-chemistry-flask: [32, 42] → [32.0, 36.5]; moved 5.5 units.
- soft-boiled-egg-in-cup: [32, 30] → [32.0, 24.5]; moved 5.5 units.
- network-folder-container: [32, 31] → [30.5, 26.0]; moved 5.22 units.
- tnt-detonator-plunger-v2: [25, 44] → [20.0, 43.0]; moved 5.099 units.
- zoom-in-magnifying-glass: [27, 32] → [26.5, 27.0]; moved 5.025 units.
- clipboard: [32, 32] → [32.0, 37.0]; moved 5.0 units.

## Lower-confidence decisions

- network-folder-container (73/100): The folder tab makes the area centroid and largest circular fit disagree. Keep the area-balance point; inspect the actual sub icon before publishing.
- payment-card-container (70/100): The lower-right mark requires an asymmetric exclusion. The chosen point balances that usable area, not the outer card rectangle.
- refresh-magnifier-container (73/100): Open circular arrows and the handle imply competing centers. The bounded interior is a design choice, so confidence stays low.
- reply-message-bubble (65/100): Reply arrow and tail make the manually bounded area asymmetric. The centroid is reproducible, but final optical placement depends on sub-icon shape.
- rotating-circular-sync-arrows (73/100): Opposed arrowheads divide the free space into competing large-circle positions. The area centroid preserves the overall circular center.
- teacher-presenting-at-whiteboard (72/100): The teacher and raised hand reduce the usable right-hand board area. The centroid balances this remaining area; it is intentionally not the whole-board midpoint.
- wavy-flag-container (71/100): The waving outline has unequal curved lobes and no strong mirror axis. Area balance is defined, but optical balance needs a paired preview.
- hand-holding-smartphone (62/100): The gripping hand intrudes into the display. The remaining concave area has substantially different centroid and maximum-clearance points; inspect each paired icon.

Nine focused tests passed, including known rectangle/triangle centers, a concave-centroid fallback, exact padding, overlap rejection, source identity, and center-only placement. Icon shapes and existing pair placements were not changed.
