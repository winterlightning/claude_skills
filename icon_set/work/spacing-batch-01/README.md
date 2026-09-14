# Spacing batch 01 — 50 original icons

Completed the first 50 entries in the gallery's “Separate parts too close” group, including add-tab. The initial local gallery contained 429 icons in that group.

All 50 original Python modules were repaired in place, with existing icon IDs, class identities and source metadata preserved. No new registered icons or review variants were created. AUTHOR is gpt-6.

All 50 now pass model validation with zero warnings, holes/pinches checks, and the internal spacing advisory. Their released SVGs exactly match the current Python output. The targeted batch build exits 0, and none remains in the failed gallery.

The 48-pixel and enlarged drawings were reviewed in light and dark themes. Rounded corners, curve joins, circular wheels/lenses, repeated parts and negative space were checked visually. Directional features remain directional; the sail, beach parasol, molecular layout and mechanical ornament retain their intentional asymmetry.

Construction references inspected in both local Lucide original and atomic-debug form: tag, plus, door-closed, car, brain, camera, clock, circle-check, cat, umbrella, battery, rotate-cw, shield and chevron-right. These informed coherent rounded outlines, true circular details, connected strokes and balanced repeated parts. No useful exact Lucide match was used for the mechanical ornament. The brain and cat are anatomical/object subjects, not human portraits; no detached human head/body is present in this batch.

## Design decisions

- Add-tab: symmetric smooth outline, equal plus arms and exact tangent joins.
- Cars: reconstruct wheel openings and use round wheels with a shared axle; preserve the compact side-view car subject.
- Camera: restore a circular lens with sufficient room inside the raised-viewfinder body.
- Badge star: broaden the shield to SQUARE to give the outlined star room; keep a curved shield silhouette.
- Square turning arrows and sync arrows: use SQUARE to preserve balanced proportions.
- Double right arrow: remove the cramped hollow ribbon interiors and retain two clear stroked chevrons.
- Battery: remove the redundant middle divider so both polarity marks have sufficient space.
- Apricot: remove a duplicated zero-length path; keep a smooth pointed stone.
- Curved subjects: retain the sail, fruit flanks, brain lobes, cat cheeks, smile, beach canopy/waves and Chinese character sweeps.

## Validation limits

The targeted build passes. The repository-wide suite is not green: 340 tests ran, with 599 failing subtests, 26 errors and one skip. The log includes library failures outside this batch and server-test socket permission errors. No validation constants, tolerances or rules were changed.

The rebuilt group has 377 icons remaining.

## Per-icon record

| Icon | Keyshape | Repair |
|---|---|---|
| add-tab | HRECT_L | Add tab: smooth, symmetric rounded tab and equal plus arms. Lucide tag and plus inform coherent corners and centered construction. |
| amazon-lightsail | CIRCLE | Lightsail mark: preserve the curved asymmetric sail within its circular rim; replace fragmented conversion arcs with flowing curves. |
| apricot-slice | CIRCLE | Apricot half: round fruit, symmetric pointed stone with smooth flanks; removed duplicate zero-length path. |
| architecture-door-retro | VRECT_L | Retro arched door: matching vertical walls and one true semicircle; handle moved inward. Lucide door-closed informs the structural sill. |
| arrow-badge-bottom | VRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-bottom-2 | VRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-left-2 | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-right | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-right-2 | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-top-2 | VRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-x-left | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-x-right | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-badge-x-top | VRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-double-right-1 | HRECT_L | Double right arrow: two equal, widely separated stroked chevrons; removed cramped hollow ribbon interiors while preserving direction. Lucide chevron-right reference. |
| arrow-rectangle-left | HRECT_L | Left chevron in a rounded rectangle: equal corner radii and centered chevron; Lucide chevron construction. |
| arrow-rectangle-left-84253ba9 | HRECT_L | Directional badge: shared mirrored outline, smoothly rounded tip and balanced internal mark. Lucide tag and chevron construction. |
| arrow-square | SQUARE | Square turning arrows: matched quarter-circle corners and arrowheads, rebuilt on a square envelope to remove vertical stretch. |
| arrow-thick-circle-bottom-left-corner | CIRCLE | Directional arrow: equal-angle head with an explicit shared shaft endpoint and comfortable inset from its frame. |
| arrow-thick-left | SQUARE | Directional arrow: equal-angle head with an explicit shared shaft endpoint and comfortable inset from its frame. |
| arrow-thick-left-bottom-corner | SQUARE | Directional arrow: equal-angle head with an explicit shared shaft endpoint and comfortable inset from its frame. |
| avocado-slice | VRECT_L | Avocado half: smooth symmetric pear-shaped outline with a circular stone and balanced flesh around it. |
| badge-star-2 | SQUARE | Star shield: broader balanced shoulders make room for a readable outlined star; preserve the smooth pointed shield. Lucide shield reference. |
| battery-2 | VRECT_L | Battery: rounded housing, integrated top terminal, balanced plus and minus. Removed the redundant divider to make room without squeezing the marks. Lucide battery informs the shell. |
| beach-parasol-water | SQUARE | Beach parasol and sea: preserve the intentional tilt and flowing canopy; replace jagged waves with repeated smooth curves and separate the shoreline. Lucide umbrella informs the canopy. |
| blood-bag-cross | VRECT_L | Blood bag: consistent rounded shoulders and broad integral outlet; centered medical cross with explicit intersection. |
| brain-artificial-intelligence | SQUARE | Brain: smooth paired lobes and a shared central fissure; retain a small fold in each hemisphere. Lucide brain informs rounded lobe construction. |
| building-929733e7 | VRECT_L | Two office blocks: clean shared roof and baseline, a centered window replacing an off-center short fragment. |
| button-syncing | SQUARE | Sync arrows: two matched curved turns and open arrowheads, with rotational balance. Lucide rotate-cw informs the construction. |
| camera-photography | HRECT_L | Camera: preserve raised viewfinder and circular lens; replace stretched ellipse and uneven body corners. Lucide camera reference. |
| car-4ecb7b0f | HRECT_L | Compact car: round wheels, shared axle, smooth body and clear glazing. Reconstructed wheel openings remove the converted overlaps; Lucide car informs the body and wheel joins. |
| car-c02dbb47 | HRECT_L | Compact car: round wheels, shared axle, smooth body and clear glazing. Reconstructed wheel openings remove the converted overlaps; Lucide car informs the body and wheel joins. |
| car-edd4874e | HRECT_L | Compact car: round wheels, shared axle, smooth body and clear glazing. Reconstructed wheel openings remove the converted overlaps; Lucide car informs the body and wheel joins. |
| car-f903e1a1 | HRECT_L | Compact car: round wheels, shared axle, smooth body and clear glazing. Reconstructed wheel openings remove the converted overlaps; Lucide car informs the body and wheel joins. |
| card | HRECT_L | Card: four identical tangent quarter-circle corners; short identifying mark inset with clear space. |
| card-b42901ee | HRECT_L | Card: four identical tangent quarter-circle corners; short identifying mark inset with clear space. |
| card-business | HRECT_L | Card: four identical tangent quarter-circle corners; short identifying mark inset with clear space. |
| card-ea0b88fe | HRECT_L | Card: four identical tangent quarter-circle corners; short identifying mark inset with clear space. |
| carplay-connect | CIRCLE | Play control: round rim and triangular play mark with balanced radial clearance. |
| cat-head | SQUARE | Cat face: matched ears, curved cheeks, symmetric eyes and a small connected muzzle. Lucide cat informs the expressive silhouette. |
| cellar | SQUARE | Cellar doors: symmetrical semicircular arch, shared center seam, and paired round handles. |
| check-button | HRECT_L | Check button: centered check with a longer rising stroke and consistent rounded corners. Lucide circle-check informs the mark. |
| check-circle | CIRCLE | Checked circle: concentric rim and optically centered check, retaining the rising diagonal. Lucide circle-check reference. |
| cheeky | CIRCLE | Cheeky smile: round face with paired smiling eyes and a continuous elliptical mouth curve. |
| chemical-hexagon | HRECT_L | Chemical structure: balanced six-sided rings, clear bond lengths and exact branch junctions, preserving the molecular topology. |
| chinese-alphabet | SQUARE | Chinese character: preserve balanced sweeping curves, replacing the near-miss crossing with one shared node. |
| circular-steampunk-ornament | CIRCLE | Circular ornament: retain the intentional asymmetric hub and wavy trace; rebalance trace and shorten the loose spoke for rim clearance. No useful exact Lucide match. |
| clip | HRECT_L | Binder clip: balanced body and symmetric wire handle, preserving curved wire corners and exact attachment points. |
| clock | CIRCLE | Clock: concentric circular rim and joined hands centered at (24,24). Lucide clock informs clear, restrained hand lengths. |
| clock-64e20f3b | CIRCLE | Clock: concentric circular rim and joined hands centered at (24,24). Lucide clock informs clear, restrained hand lengths. |
| clock-9f37004b | CIRCLE | Clock: concentric circular rim and joined hands centered at (24,24). Lucide clock informs clear, restrained hand lengths. |
