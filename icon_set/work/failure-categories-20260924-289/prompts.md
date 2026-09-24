### batch-01

```
Run $primitive-make-ray to repair failed icons, batch 1 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_01/adjustable lamp 1_afa0c105-3fb7-4c77-b44d-80888cf292ec.svg
     icon_id: adjustable-brightness-light-bulb
     current drawing: published/failed/solo48/adjustable-brightness-light-bulb.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  2. pictographic-primitives/_uncategorized_01/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg
     icon_id: aerial-yoga-bow-pose
     current drawing: published/failed/solo48/aerial-yoga-bow-pose.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  3. pictographic-primitives/_uncategorized_02/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg
     icon_id: amazon-emr
     current drawing: published/failed/solo48/amazon-emr.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [hub]: hub and plus-horizontal are 6.999 apart on centerlines nearest (6.001, 23.914)<->(13, 24); (needs 8) | mic [plus-vertical]: plus-vertical and upper-link are 7.810 apart on centerlines nearest (15, 22)<->(21, 17); (needs 8) | mic [plus-horizontal]: plus-horizontal and right-upper-link are 7.280 apart on centerlines nearest (17, 24)<->(24, 22); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [upper-node]: parallel straight edges upper-node-3 and right-upper-node-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [right-upper-node]: parallel straight edges right-upper-node-3 and right-lower-node-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  4. pictographic-primitives/_uncategorized_02/amazon mq_14a3a91e-9beb-47ca-9999-bd7a4d5e5429.svg
     icon_id: square-centered-ring-network
     current drawing: published/failed/solo48/square-centered-ring-network.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [ring-0]: ring-0 and ring-1 are 8 apart on centerlines nearest (40, 20)<->(40, 28); (needs 8)
  5. pictographic-primitives/_uncategorized_02/amazon web service code commit_e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41.svg
     icon_id: code-version-control-and-branching
     current drawing: published/failed/solo48/code-version-control-and-branching.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  6. pictographic-primitives/_uncategorized_02/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg
     icon_id: amazon-elemental-medialive
     current drawing: published/failed/solo48/amazon-elemental-medialive.svg
     violates 3 rules: keyshape bounds, part spacing under 8, parallel straight edges under 8
       - keyshape bounds: canvas/keyshape bounds: visible ink (4, 3, 44, 46) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 1.0, 0.0, 2.0], tolerance 0.0)
       - part spacing under 8: mic [play]: play and top are 5.813 apart on centerlines nearest (21.4, 18.2)<->(24, 13); (needs 8) | mic [play]: play and lower-left are 7.071 apart on centerlines nearest (19, 31)<->(14, 36); (needs 8) | mic [lower-left]: lower-left and scan-bottom are 5 apart on centerlines nearest (14, 40)<->(19, 40); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [top]: parallel straight edges top-6 and top-3 are 7.155 apart on centerlines (ink gap 3.155); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [lower-left]: parallel straight edges lower-left-6 and lower-left-3 are 7.155 apart on centerlines (ink gap 3.155); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [lower-right]: parallel straight edges lower-right-6 and lower-right-3 are 7.155 apart on centerlines (ink gap 3.155); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
  7. pictographic-primitives/_uncategorized_03/amber_3ccf997d-67a6-4970-9541-a4835906cdba.svg
     icon_id: fossilized-bug-in-amber
     current drawing: published/failed/solo48/fossilized-bug-in-amber.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 5 undersized holes; 4 pinches
       - undersized holes: holes/pinches: 5 undersized holes; 4 pinches
  8. pictographic-primitives/_uncategorized_03/american football ball 1_a9f0b51b-1232-4e6f-922b-648cbe4c0f54.svg
     icon_id: diagonal-american-football
     current drawing: published/failed/solo48/diagonal-american-football.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [outline / end-band-high]: cap-upper and end-band-high have 1.831 units of ink clearance over 10.471 units; requires 4; review required | internal-spacing [outline / end-band-low]: cap-lower and end-band-low have 1.953 units of ink clearance over 10.222 units; requires 4; review required
  9. pictographic-primitives/_uncategorized_03/amphibian frog body_b274b037-6061-4c72-b6f8-f750487d883c.svg
     icon_id: front-facing-seated-frog
     current drawing: published/failed/solo48/front-facing-seated-frog.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [frog / right-haunch]: frog-4 and right-haunch-0 have -0.889 units of ink clearance over 3.019 units; requires 4; review required | internal-spacing [frog / right-haunch]: frog-5 and right-haunch-0 have 3.434 units of ink clearance over 2.916 units; requires 4; review required | internal-spacing [frog / right-haunch]: frog-5 and right-haunch-1 have -0.011 units of ink clearance over 10.850 units; requires 4; review required (+3 more)
  10. pictographic-primitives/_uncategorized_03/amusement park ferris wheel 1_504a0510-ec03-4633-a8b4-a32a2b49ce54.svg
     icon_id: spoked-ferris-wheel-with-round-cabins
     current drawing: published/failed/solo48/spoked-ferris-wheel-with-round-cabins.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  11. pictographic-primitives/_uncategorized_03/anaconda_22672d31-d164-4dfa-a6e8-c5a29193cea8.svg
     icon_id: s-curved-snake
     current drawing: published/failed/solo48/s-curved-snake.svg
     violates 2 rules: parallel straight edges under 8, undersized holes
       - parallel straight edges under 8: mic [snake]: parallel straight edges snake-2 and snake-4 are 6.363 apart on centerlines (ink gap 2.363); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  12. pictographic-primitives/_uncategorized_03/ankle tracker_09ba7447-8f77-4033-ba06-5bf4e4d39449.svg
     icon_id: electronic-ankle-tracking-device
     current drawing: published/failed/solo48/electronic-ankle-tracking-device.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [foot-outline]: foot-outline-3 and foot-outline-5 have 0.163 units of ink clearance over 3.726 units; requires 4; review required | internal-spacing [foot-outline]: foot-outline-6 and foot-outline-9 have 2.976 units of ink clearance over 2.5 units; requires 4; review required
  13. pictographic-primitives/_uncategorized_03/aquarium_4fb53005-bb60-46fd-bc0e-7ea549f599e9.svg
     icon_id: fish-in-an-aquarium-tank
     current drawing: published/failed/solo48/fish-in-an-aquarium-tank.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 2 undersized holes; 4 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 4 pinches
  14. pictographic-primitives/_uncategorized_04/arch linux logo_7f1ad0e2-4f9e-423b-9473-4df26eae6fed.svg
     icon_id: pointed-arch-linux-emblem
     current drawing: published/failed/solo48/pointed-arch-linux-emblem.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [left / base]: left-1 and base-1 have 3.116 units of ink clearance over 10.957 units; requires 4; review required | internal-spacing [left / base]: left-2 and base-1 have 3.308 units of ink clearance over 4.236 units; requires 4; review required
  15. pictographic-primitives/_uncategorized_04/archaeologist_434aebe0-5637-41b2-ba5b-e41942db8485.svg
     icon_id: archaeologist-beside-a-spade
     current drawing: published/failed/solo48/archaeologist-beside-a-spade.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [brim / jaw]: brim and jaw have 3.028 units of ink clearance over 8.211 units; requires 4; review required | internal-spacing [jaw / shoulders]: jaw and shoulders have 0.037 units of ink clearance over 2.646 units; requires 4; review required
```

### batch-02

```
Run $primitive-make-ray to repair failed icons, batch 2 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg
     icon_id: archive-books
     current drawing: published/failed/solo48/archive-books.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [binder-0]: binder-0 and label-0 are 3 apart on centerlines nearest (14, 14)<->(11, 14); (needs 8) | mic [binder-0]: binder-0 and hole-0 are 3 apart on centerlines nearest (4, 33)<->(7, 33); (needs 8) | mic [binder-0]: binder-0 and binder-1 are 5 apart on centerlines nearest (14, 10)<->(19, 10); (needs 8) (+8 more)
       - parallel straight edges under 8: mic [binder-2]: parallel straight edges binder-2-2 and label-2-2 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [binder-2]: parallel straight edges binder-2-2 and label-2-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [label-2]: parallel straight edges label-2-2 and label-2-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+17 more)
       - pinches: holes/pinches: 9 undersized holes; 3 pinches
       - undersized holes: holes/pinches: 9 undersized holes; 3 pinches
  2. pictographic-primitives/_uncategorized_04/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg
     icon_id: infinity-loop-with-plus-and-minus
     current drawing: published/failed/solo48/infinity-loop-with-plus-and-minus.svg
     violates 2 rules: keyshape bounds, part spacing under 8
       - keyshape bounds: canvas/keyshape bounds: visible ink (2.25, 8, 45.75, 40) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.25, 0.0, 0.25, 0.0], tolerance 0.0)
       - part spacing under 8: mic [infinity]: infinity and minus are 5.749 apart on centerlines nearest (4.250, 23.971)<->(10, 24); (needs 8) | mic [infinity]: infinity and plus-h are 5.749 apart on centerlines nearest (43.749, 23.971)<->(38, 24); (needs 8)
  3. pictographic-primitives/_uncategorized_04/astronomy eclipse_6d179933-acab-43ec-bf9b-e0d73eebedfc.svg
     icon_id: overlapping-eclipse-disks
     current drawing: published/failed/solo48/overlapping-eclipse-disks.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [front]: front and rear are 1.888 apart on centerlines nearest (27.161, 38.307)<->(28, 40); (needs 8)
  4. pictographic-primitives/_uncategorized_04/audio book headphones_b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a.svg
     icon_id: audiobook-with-headphones
     current drawing: published/failed/solo48/audiobook-with-headphones.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [left-ear]: left-ear and book are 5 apart on centerlines nearest (10, 23)<->(15, 23); (needs 8)
       - parallel straight edges under 8: mic [right-ear]: parallel straight edges right-inner and book-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [book]: parallel straight edges book-6 and left-inner are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  5. pictographic-primitives/_uncategorized_04/auto pilot car signal 1_148a6d3d-6e93-44b0-ad9c-3c3c30856f29.svg
     icon_id: autonomous-domed-car-with-signal
     current drawing: published/failed/solo48/autonomous-domed-car-with-signal.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [left-base]: left-base and center-base are 6 apart on centerlines nearest (9, 38)<->(15, 38); (needs 8) | mic [left-base]: left-base and left-wheel are 0.163 apart on centerlines nearest (9, 38)<->(9.154, 38.051); (needs 8) | mic [right-base]: right-base and right-wheel are 0.163 apart on centerlines nearest (39, 38)<->(38.845, 38.051); (needs 8) (+18 more)
       - parallel straight edges under 8: mic [beacon-right]: parallel straight edges beacon-right and beacon-stem-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [window-divider]: parallel straight edges window-divider and center-base are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  6. pictographic-primitives/_uncategorized_05/avatar carpenter_0a473297-da88-4e1f-8691-703bcbdef5cb.svg
     icon_id: capped-carpenter-beside-a-hand-saw
     current drawing: published/failed/solo48/capped-carpenter-beside-a-hand-saw.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [saw]: saw-1 and saw-3 have 0.277 units of ink clearance over 7.950 units; requires 4; review required | internal-spacing [saw]: saw-1 and saw-4 have 0.277 units of ink clearance over 7.950 units; requires 4; review required | internal-spacing [saw]: saw-1 and saw-5 have 0.277 units of ink clearance over 7.950 units; requires 4; review required (+1 more)
  7. pictographic-primitives/_uncategorized_05/avatar piracy laptop_aa4f64c4-a374-44b3-9890-7cd9bfe00eab.svg
     icon_id: bearded-pirate-behind-a-laptop
     current drawing: published/failed/solo48/bearded-pirate-behind-a-laptop.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [hat]: hat and beard are 7.588 apart on centerlines nearest (30.722, 20)<->(30.722, 27.588); (needs 8)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  8. pictographic-primitives/_uncategorized_05/babe_4601d69f-9445-41fa-8190-2bd52b395af7.svg
     icon_id: smiling-woman-with-shoulder-length-hair
     current drawing: published/failed/solo48/smiling-woman-with-shoulder-length-hair.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [face]: face and smile are 6.156 apart on centerlines nearest (20.320, 16.076)<->(22, 22); (needs 8)
  9. pictographic-primitives/_uncategorized_05/baby care pacifier_fcf2e80c-06a5-42d9-a45c-b4984bad2541.svg
     icon_id: diagonal-pacifier-with-a-round-handle
     current drawing: published/failed/solo48/diagonal-pacifier-with-a-round-handle.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  10. pictographic-primitives/_uncategorized_05/band saw_f8387852-af8b-4221-a8f7-998fc1b24294.svg
     icon_id: band-saw
     current drawing: published/failed/solo48/band-saw.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [base]: base and hub are 2 apart on centerlines nearest (31, 34)<->(31, 32); (needs 8)
       - parallel straight edges under 8: mic [inner]: parallel straight edges inner-1 and frame-left-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [inner]: parallel straight edges inner-2 and wheel-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 4 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 2 pinches
  11. pictographic-primitives/_uncategorized_06/bhudda hand finger citron 1_76411d38-aca5-4268-9511-bc3205689722.svg
     icon_id: upright-hand-with-curled-fingers
     current drawing: published/failed/solo48/upright-hand-with-curled-fingers.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: thumb and thumb have 1.904 units of ink clearance over 4.334 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_06/bicycle person_816c0a6d-a6b1-4041-9b3e-aa2bb963535f.svg
     icon_id: cyclist-on-a-fully-framed-bicycle
     current drawing: published/failed/solo48/cyclist-on-a-fully-framed-bicycle.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  13. pictographic-primitives/_uncategorized_06/bike parking 2_7eea5c25-9b41-4dec-ba5e-91b557120a37.svg
     icon_id: angled-handlebar-road-bicycle
     current drawing: published/failed/solo48/angled-handlebar-road-bicycle.svg
     violates 3 rules: part spacing under 8, pinches, undersized holes
       - part spacing under 8: mic [wheel-36]: wheel-36 and frame are 3.803 apart on centerlines nearest (28.768, 28.579)<->(25.314, 26.985); (needs 8)
       - pinches: holes/pinches: 3 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 1 pinches
  14. pictographic-primitives/_uncategorized_06/bilibili logo_967f7cba-3409-4e70-8a1c-ac8501b16e27.svg
     icon_id: smiling-television-mascot
     current drawing: published/failed/solo48/smiling-television-mascot.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [tv / aerial]: tv-0 and aerial-1 have -3.746 units of ink clearance over 9.75 units; requires 4; review required | internal-spacing [tv / aerial]: tv-0 and aerial-2 have -3.746 units of ink clearance over 9.75 units; requires 4; review required
  15. pictographic-primitives/_uncategorized_07/bower logo_ff183e37-2bed-4312-ad52-11655fc8a512.svg
     icon_id: bower-logo
     current drawing: published/failed/solo48/bower-logo.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
```

### batch-03

```
Run $primitive-make-ray to repair failed icons, batch 3 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_08/breeding gender symbols_d98a91a3-2cf0-4bb4-a37a-26d5ea8781e0.svg
     icon_id: breeding-gender-symbols
     current drawing: published/failed/solo48/breeding-gender-symbols.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  2. pictographic-primitives/_uncategorized_08/buggy_f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072.svg
     icon_id: rounded-passenger-car-profile
     current drawing: published/failed/solo48/rounded-passenger-car-profile.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [roof / body]: roof-1 and body-3 have 3.617 units of ink clearance over 2.235 units; requires 4; review required | internal-spacing [roof / body]: roof-3 and body-3 have 3.617 units of ink clearance over 2.235 units; requires 4; review required | internal-spacing [body / wheel-14]: body-1 and wheel-14-0 have 0.064 units of ink clearance over 4.75 units; requires 4; review required (+1 more)
  3. pictographic-primitives/_uncategorized_10/caviar_e625a592-a7be-4a88-9cc8-1a1640f52612.svg
     icon_id: pyramid-of-round-caviar-eggs
     current drawing: published/failed/solo48/pyramid-of-round-caviar-eggs.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [egg-0]: egg-0 and egg-1 are 2.422 apart on centerlines nearest (20.666, 16.988)<->(19.333, 19.011); (needs 8) | mic [egg-0]: egg-0 and egg-2 are 2.422 apart on centerlines nearest (27.333, 16.988)<->(28.666, 19.011); (needs 8) | mic [egg-1]: egg-1 and egg-2 are 4 apart on centerlines nearest (22, 24)<->(26, 24); (needs 8) (+2 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  4. pictographic-primitives/_uncategorized_11/chef gear tea cookies_8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7.svg
     icon_id: chef-gear-tea-cookies
     current drawing: published/failed/solo48/chef-gear-tea-cookies.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  5. pictographic-primitives/_uncategorized_11/chinchilla_df04551f-f9b1-422f-a44f-8a7dfd1d0dda.svg
     icon_id: seated-chinchilla-with-curved-tail
     current drawing: published/failed/solo48/seated-chinchilla-with-curved-tail.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [chinchilla]: chinchilla-1 and chinchilla-3 have 3.703 units of ink clearance over 2.152 units; requires 4; review required
  6. pictographic-primitives/_uncategorized_11/cloister_19554f1f-19e3-4b9e-87c9-d610d1b7dcb6.svg
     icon_id: arched-facade-with-upper-arcade
     current drawing: published/failed/solo48/arched-facade-with-upper-arcade.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [facade / door]: facade-4 and door-1 have 3.127 units of ink clearance over 7.303 units; requires 4; review required | internal-spacing [window-0 / floor]: window-0-1 and floor have 3.522 units of ink clearance over 4.188 units; requires 4; review required | internal-spacing [window-1 / floor]: window-1-1 and floor have 3.522 units of ink clearance over 4.188 units; requires 4; review required
  7. pictographic-primitives/_uncategorized_12/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg
     icon_id: cog-double-1
     current drawing: published/failed/solo48/cog-double-1.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [gear-0]: gear-0 and hub-0 are 4.156 apart on centerlines nearest (11.858, 26.570)<->(13.717, 30.288); (needs 8) | mic [gear-0]: gear-0 and gear-1 are 7.071 apart on centerlines nearest (21, 26)<->(26, 21); (needs 8) | mic [gear-1]: gear-1 and hub-1 are 4.156 apart on centerlines nearest (36.141, 8.570)<->(34.282, 12.288); (needs 8)
       - parallel straight edges under 8: mic [gear-1]: parallel straight edges gear-1-2 and gear-1-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-1]: parallel straight edges gear-1-16 and gear-1-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-0]: parallel straight edges gear-0-2 and gear-0-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  8. pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg
     icon_id: cog-double
     current drawing: published/failed/solo48/cog-double.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [gear-0]: gear-0 and hub-0 are 4.156 apart on centerlines nearest (11.858, 26.570)<->(13.717, 30.288); (needs 8) | mic [gear-0]: gear-0 and gear-1 are 7.071 apart on centerlines nearest (21, 26)<->(26, 21); (needs 8) | mic [gear-1]: gear-1 and hub-1 are 4.156 apart on centerlines nearest (36.141, 8.570)<->(34.282, 12.288); (needs 8)
       - parallel straight edges under 8: mic [gear-1]: parallel straight edges gear-1-2 and gear-1-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-1]: parallel straight edges gear-1-16 and gear-1-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-0]: parallel straight edges gear-0-2 and gear-0-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  9. pictographic-primitives/_uncategorized_12/concert microphone_a37d9a40-16b7-4abd-b2f5-962b0ceb5244.svg
     icon_id: concert-stage-with-singer
     current drawing: published/failed/solo48/concert-stage-with-singer.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 3 undersized holes; 3 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 3 pinches
  10. pictographic-primitives/_uncategorized_12/conversation smile type 1_32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c.svg
     icon_id: round-smiling-speech-bubble-pair
     current drawing: published/failed/solo48/round-smiling-speech-bubble-pair.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [back]: back and smile are 6.716 apart on centerlines nearest (21.362, 32.883)<->(20.561, 26.214); (needs 8) | mic [front]: front and eye-24 are 6.811 apart on centerlines nearest (27.853, 21.617)<->(24, 16); (needs 8) | mic [front]: front and smile are 1.296 apart on centerlines nearest (25.135, 24.625)<->(24, 24); (needs 8)
  11. pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg
     icon_id: crawdad
     current drawing: published/failed/solo48/crawdad.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 2 pinches
  12. pictographic-primitives/_uncategorized_13/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg
     icon_id: crayfish
     current drawing: published/failed/solo48/crayfish.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 4 undersized holes; 6 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 6 pinches
  13. pictographic-primitives/_uncategorized_14/daytum logo_13398523-c61f-487e-93bd-5e12bc1429a6.svg
     icon_id: four-ascending-chart-columns
     current drawing: published/failed/solo48/four-ascending-chart-columns.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [column-0]: column-0 and column-1 are 4 apart on centerlines nearest (11, 29)<->(15, 29); (needs 8) | mic [column-1]: column-1 and column-2 are 4 apart on centerlines nearest (22, 22)<->(26, 22); (needs 8) | mic [column-2]: column-2 and column-3 are 4 apart on centerlines nearest (33, 15)<->(37, 15); (needs 8)
       - parallel straight edges under 8: mic [column-3]: parallel straight edges column-3-3 and column-3-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [column-3]: parallel straight edges column-3-1 and column-2-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [column-2]: parallel straight edges column-2-3 and column-2-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
  14. pictographic-primitives/_uncategorized_15/disability hearing t_42121486-14f6-4035-afad-601034d0d354.svg
     icon_id: hearing-assistance-symbol
     current drawing: published/failed/solo48/hearing-assistance-symbol.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  15. pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg
     icon_id: earthquake-hiding-proof-table
     current drawing: published/failed/solo48/earthquake-hiding-proof-table.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [tabletop]: tabletop and tremor--1 are 6 apart on centerlines nearest (13, 16)<->(13, 10); (needs 8) | mic [tabletop]: tabletop and tremor-1 are 6 apart on centerlines nearest (35, 16)<->(35, 10); (needs 8) | mic [tabletop]: tabletop and crouched-body are 3 apart on centerlines nearest (27, 24)<->(27, 27); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [tabletop]: parallel straight edges tabletop-5 and crouched-body-4 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [crouched-body]: parallel straight edges crouched-body-4 and crouched-body-12 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [crouched-body]: parallel straight edges crouched-body-7 and crouched-body-9 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
```

### batch-04

```
Run $primitive-make-ray to repair failed icons, batch 4 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_16/eel_f644d4c1-b881-4092-96b4-a643877d65a5.svg
     icon_id: eel-with-narrow-raised-tail
     current drawing: published/failed/solo48/eel-with-narrow-raised-tail.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [eel]: eel-2 and eel-5 have 3.251 units of ink clearance over 10.390 units; requires 4; review required | internal-spacing [eel]: eel-4 and eel-8 have 0.649 units of ink clearance over 2.405 units; requires 4; review required | internal-spacing [eel]: eel-4 and eel-9 have 0.625 units of ink clearance over 12.962 units; requires 4; review required (+3 more)
  2. pictographic-primitives/_uncategorized_16/elf_2a1d8754-4e2e-4a0a-b2fe-427b85f1964c.svg
     icon_id: smiling-elf-with-drooping-bobble-hat
     current drawing: published/failed/solo48/smiling-elf-with-drooping-bobble-hat.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  3. pictographic-primitives/_uncategorized_16/emoji gaming lover hug 1_b0db5c05-63ca-4bad-830f-6a24ddb21cb3.svg
     icon_id: smiling-face-behind-game-controller
     current drawing: published/failed/solo48/smiling-face-behind-game-controller.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [face]: face and eye-19 are 7.323 apart on centerlines nearest (14.424, 8.758)<->(18.304, 14.969); (needs 8) | mic [face]: face and eye-29 are 7.323 apart on centerlines nearest (33.575, 8.758)<->(29.695, 14.969); (needs 8) | mic [eye-19]: eye-19 and eye-29 are 6 apart on centerlines nearest (21, 17)<->(27, 17); (needs 8)
  4. pictographic-primitives/_uncategorized_17/face awesome_236451ca-3512-494c-8c17-87481ad251f8.svg
     icon_id: smiling-star-eyed-face
     current drawing: published/failed/solo48/smiling-star-eyed-face.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [head]: head and star-0 are 7.469 apart on centerlines nearest (6.434, 14.438)<->(13, 18); (needs 8) | mic [head]: head and star-1 are 7.469 apart on centerlines nearest (41.566, 14.438)<->(35, 18); (needs 8) | mic [star-0]: star-0 and star-1 are 6 apart on centerlines nearest (21, 18)<->(27, 18); (needs 8) (+2 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  5. pictographic-primitives/_uncategorized_17/face dizzy_aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a.svg
     icon_id: dizzy-face-with-spiral-eyes
     current drawing: published/failed/solo48/dizzy-face-with-spiral-eyes.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [head]: head and spiral-0 are 1.744 apart on centerlines nearest (4.582, 19.209)<->(6.277, 19.623); (needs 8) | mic [head]: head and spiral-1 are 1.744 apart on centerlines nearest (43.417, 19.209)<->(41.722, 19.623); (needs 8) | mic [head]: head and mouth are 4.999 apart on centerlines nearest (23.969, 43.999)<->(24, 39); (needs 8) (+3 more)
  6. pictographic-primitives/_uncategorized_17/face grin stars_3e7a0a74-079b-41a7-abfe-d06129db8361.svg
     icon_id: smiling-face-with-star-eyes;smiling-face-with-star-eyes-v2;smiling-face-with-star-eyes-v3
     current drawing: published/failed/solo48/smiling-face-with-star-eyes.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [face]: face and star-0 are 2.535 apart on centerlines nearest (5.675, 15.986)<->(8, 17); (needs 8) | mic [face]: face and star-1 are 2.535 apart on centerlines nearest (42.324, 15.986)<->(40, 17); (needs 8) | mic [star-0]: star-0 and star-1 are 4 apart on centerlines nearest (22, 17)<->(26, 17); (needs 8) (+7 more)
       - parallel straight edges under 8: mic [star-1]: parallel straight edges star-1-4 and star-1-7 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [star-0]: parallel straight edges star-0-4 and star-0-7 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches | holes/pinches: 2 undersized holes; 0 pinches
  7. pictographic-primitives/_uncategorized_18/face smile hearts_9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg
     icon_id: heart-shaped-face-with-heart-eyes
     current drawing: published/failed/solo48/heart-shaped-face-with-heart-eyes.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [heart]: heart and eye-0 are 5.733 apart on centerlines nearest (23.239, 12.243)<->(19.207, 16.319); (needs 8) | mic [heart]: heart and eye-1 are 5.733 apart on centerlines nearest (24.760, 12.243)<->(28.792, 16.319); (needs 8) | mic [heart]: heart and smile are 6.564 apart on centerlines nearest (29.569, 36.343)<->(25.968, 30.854); (needs 8) (+2 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  8. pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg
     icon_id: dizzy-hypnotized-face
     current drawing: published/failed/solo48/dizzy-hypnotized-face.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [head]: head and spiral-0 are 1.744 apart on centerlines nearest (4.582, 19.209)<->(6.277, 19.623); (needs 8) | mic [head]: head and spiral-1 are 1.744 apart on centerlines nearest (43.417, 19.209)<->(41.722, 19.623); (needs 8) | mic [spiral-0]: spiral-0 and spiral-1 are 4 apart on centerlines nearest (22, 22)<->(26, 22); (needs 8) (+1 more)
  9. pictographic-primitives/_uncategorized_20/gesture swipe vertical 3_db37e620-1eb0-4c99-bce3-2c53b5c5fa76.svg
     icon_id: one-finger-vertical-swipe-gesture
     current drawing: published/failed/solo48/one-finger-vertical-swipe-gesture.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: hand-6 and hand-9 have 2.987 units of ink clearance over 2.5 units; requires 4; review required
  10. pictographic-primitives/_uncategorized_20/gesture tap swipe right 1_3b0fa0d0-112f-4a7d-9586-70fd5b30cbaa.svg
     icon_id: hand-swipe-right-gesture
     current drawing: published/failed/solo48/hand-swipe-right-gesture.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: hand-3 and hand-11 have 2.338 units of ink clearance over 6.216 units; requires 4; review required | internal-spacing [hand]: hand-8 and hand-10 have 0.624 units of ink clearance over 5 units; requires 4; review required
  11. pictographic-primitives/_uncategorized_20/gesture two finger flip right_3808dced-acba-4c34-8f9f-05ba44dfe152.svg
     icon_id: two-finger-swipe-right
     current drawing: published/failed/solo48/two-finger-swipe-right.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: hand-3 and hand-18 have 2.088 units of ink clearance over 6.987 units; requires 4; review required | internal-spacing [hand]: hand-4 and hand-8 have 3.004 units of ink clearance over 7.246 units; requires 4; review required | internal-spacing [hand]: hand-9 and hand-13 have 2.029 units of ink clearance over 5.967 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_21/graffiti_c6d7f6d7-a700-4894-830b-9788ba0a2a17.svg
     icon_id: interlocking-graffiti-cloud
     current drawing: published/failed/solo48/interlocking-graffiti-cloud.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [cloud / seam]: cloud and seam have 2.755 units of ink clearance over 3.853 units; requires 4; review required
  13. pictographic-primitives/_uncategorized_23/infancy care_a8c124ba-bd78-456b-87fd-6763a1095d57.svg
     icon_id: hand-protecting-swaddled-baby
     current drawing: published/failed/solo48/hand-protecting-swaddled-baby.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: hand-slope and hand-under have 0.277 units of ink clearance over 5.714 units; requires 4; review required | internal-spacing [hand]: hand-slope and hand-thumb have 2.412 units of ink clearance over 5.465 units; requires 4; review required
  14. pictographic-primitives/_uncategorized_23/insurance hands_66883e78-cb13-4f81-a6f8-a7ec339ba917.svg
     icon_id: hands-holding-medical-cross
     current drawing: published/failed/solo48/hands-holding-medical-cross.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand-left]: hand-left-1 and hand-left-5 have 2.946 units of ink clearance over 4.75 units; requires 4; review required | internal-spacing [hand-left]: hand-left-1 and hand-left-6 have 3.287 units of ink clearance over 3.689 units; requires 4; review required | internal-spacing [hand-right]: hand-right-1 and hand-right-5 have 2.946 units of ink clearance over 4.75 units; requires 4; review required (+1 more)
  15. pictographic-primitives/_uncategorized_24/labor worker_5e90a983-c6c8-4780-99a7-53d2101f43e0.svg
     icon_id: construction-worker-with-wrench
     current drawing: published/failed/solo48/construction-worker-with-wrench.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [head-and-hat / hat-brim]: hard-hat-dome and hat-brim have 3.028 units of ink clearance over 8.211 units; requires 4; review required | internal-spacing [head-and-hat / hard-hat-rib]: hard-hat-dome and hard-hat-rib have 2.968 units of ink clearance over 3.732 units; requires 4; review required | internal-spacing [head-and-hat / hat-brim]: face-lower and hat-brim have 3.028 units of ink clearance over 8.211 units; requires 4; review required
```

### batch-05

```
Run $primitive-make-ray to repair failed icons, batch 5 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_25/linguist_d3d86e97-b873-48ff-bd6b-fc4456184a6e.svg
     icon_id: speaking-profile-with-empty-bubble
     current drawing: published/failed/solo48/speaking-profile-with-empty-bubble.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [face / skull]: face-6 and skull have 2.017 units of ink clearance over 5.248 units; requires 4; review required
  2. pictographic-primitives/_uncategorized_26/love boat_74aefd26-5ecb-469f-857a-7b635d067fa7.svg
     icon_id: couple-in-bed-with-hearts
     current drawing: published/failed/solo48/couple-in-bed-with-hearts.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  3. pictographic-primitives/_uncategorized_26/love heart ranking_23d9de33-2d15-4372-8f12-18cd47ea7ba3.svg
     icon_id: heart-ranking-podium
     current drawing: published/failed/solo48/heart-ranking-podium.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [heart]: heart-1 and heart-4 have 2.754 units of ink clearance over 6.726 units; requires 4; review required | internal-spacing [heart]: heart-5 and heart-8 have 2.754 units of ink clearance over 6.726 units; requires 4; review required
  4. pictographic-primitives/_uncategorized_26/male star_9d16496d-3f1e-497f-acc5-d87ece1bf0c8.svg
     icon_id: person-with-three-stars
     current drawing: published/failed/solo48/person-with-three-stars.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 3 undersized holes; 3 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 3 pinches
  5. pictographic-primitives/_uncategorized_26/mantel_cd0e91bf-8014-4487-8310-916da006a67a.svg
     icon_id: fireplace-with-burning-flame
     current drawing: published/failed/solo48/fireplace-with-burning-flame.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [flame]: flame-1 and flame-5 have 2.452 units of ink clearance over 4 units; requires 4; review required | internal-spacing [flame]: flame-2 and flame-6 have 3.378 units of ink clearance over 2.185 units; requires 4; review required
  6. pictographic-primitives/_uncategorized_26/map marks_4a6fa657-5f3d-4ab6-8949-77cda8ee6030.svg
     icon_id: map-with-two-location-pins
     current drawing: published/failed/solo48/map-with-two-location-pins.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [pin-1 / map]: pin-right-1 and map-5 have 2.617 units of ink clearance over 2.25 units; requires 4; review required
  7. pictographic-primitives/_uncategorized_26/mastodon logo 2_5728b0bd-4ca7-4880-8dd9-2620444de10e.svg
     icon_id: mastodon-social-network-logo
     current drawing: published/failed/solo48/mastodon-social-network-logo.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [outline]: underbody and tail-return have 2.490 units of ink clearance over 5.5 units; requires 4; review required
  8. pictographic-primitives/_uncategorized_27/mastodon logo 3_0ab8e84d-e705-47dc-805d-8eeccbcc900b.svg
     icon_id: mastodon-social-network-icon
     current drawing: published/failed/solo48/mastodon-social-network-icon.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [outline]: underbody and tail-return have 2.490 units of ink clearance over 5.5 units; requires 4; review required
  9. pictographic-primitives/_uncategorized_27/maya logo_adef874c-e298-460c-b8fd-7d6806bd6e51.svg
     icon_id: outlined-capital-m
     current drawing: published/failed/solo48/outlined-capital-m.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [letter-outline]: letter-outline-2 and letter-outline-10 have 2.472 units of ink clearance over 8.656 units; requires 4; review required | internal-spacing [letter-outline]: letter-outline-2 and letter-outline-11 have 2.736 units of ink clearance over 3 units; requires 4; review required | internal-spacing [letter-outline]: letter-outline-3 and letter-outline-7 have 2.736 units of ink clearance over 3 units; requires 4; review required (+1 more)
  10. pictographic-primitives/_uncategorized_27/medical app smartphone listen_811410b0-f597-4cad-ad05-e3c48b6e64b7.svg
     icon_id: smartphone-with-stethoscope
     current drawing: published/failed/solo48/smartphone-with-stethoscope.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [stethoscope-u / lower-tube]: u-right-bend and lower-tube-2 have 1.018 units of ink clearance over 10.75 units; requires 4; review required
  11. pictographic-primitives/_uncategorized_27/microsoft internet explorer logo_ff53feac-62ae-4745-9bd7-4e08ad72f21a.svg
     icon_id: internet-explorer-e
     current drawing: published/failed/solo48/internet-explorer-e.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [e-main]: middle-bar and lower-bowl-right have 1.602 units of ink clearance over 14.534 units; requires 4; review required | internal-spacing [e-main]: lower-bowl-left and outer-bottom-left have 3.981 units of ink clearance over 10.222 units; requires 4; review required | internal-spacing [e-main]: lower-bowl-right and outer-bottom-right have -0.999 units of ink clearance over 17.556 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_27/microsoft powerpoint logo_1a770dd1-2225-4204-b85f-81e18d91cca2.svg
     icon_id: presentation-pie-chart-badge
     current drawing: published/failed/solo48/presentation-pie-chart-badge.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  13. pictographic-primitives/_uncategorized_27/modern music monitor speaker_ddfc1e41-af2e-4f27-a89f-8cb60796155a.svg
     icon_id: music-monitor-and-speaker
     current drawing: published/failed/solo48/music-monitor-and-speaker.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [monitor-bezel]: monitor-bezel and music-notes are 3.884 apart on centerlines nearest (12.996, 27)<->(12.996, 23.115); (needs 8) | mic [speaker]: speaker and speaker-tweeter are 5 apart on centerlines nearest (36, 16)<->(36, 21); (needs 8) | mic [speaker]: speaker and speaker-woofer are 3 apart on centerlines nearest (36, 40)<->(36, 37); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [music-notes]: parallel straight edges right-note-stem and left-note-stem are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [monitor-bezel]: parallel straight edges monitor-bezel and monitor-bottom are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [monitor]: parallel straight edges monitor-bottom and stand-foot are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  14. pictographic-primitives/_uncategorized_27/monetization tablet_e64a63c8-c12a-4dd2-90a5-e6fbd2b163fb.svg
     icon_id: smartphone-with-dollar-sign
     current drawing: published/failed/solo48/smartphone-with-dollar-sign.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  15. pictographic-primitives/_uncategorized_27/moving walkway_b13ef0ee-32e3-468d-876a-7e9b08b10fa2.svg
     icon_id: person-on-rising-escalator
     current drawing: published/failed/solo48/person-on-rising-escalator.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
```

### batch-06

```
Run $primitive-make-ray to repair failed icons, batch 6 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_28/music box_b9c25347-4f61-49ed-b94b-bdbb23fd2b5e.svg
     icon_id: music-box
     current drawing: published/failed/solo48/music-box.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [note-right / beam]: note-right-a and beam-1 have 2.195 units of ink clearance over 3.25 units; requires 4; review required | internal-spacing [note-right / second-beam]: note-right-a and second-beam have -0.997 units of ink clearance over 5.5 units; requires 4; review required
  2. pictographic-primitives/_uncategorized_28/music making_8fed7998-a482-495d-a5a5-6b6237429d87.svg
     icon_id: music-making
     current drawing: published/failed/solo48/music-making.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [note-right / beam]: note-right-a and beam-2 have 3.216 units of ink clearance over 7.246 units; requires 4; review required
  3. pictographic-primitives/_uncategorized_28/muskrat_763a2d28-4b32-458f-8301-cf3ad514b5a1.svg
     icon_id: crouching-muskrat
     current drawing: published/failed/solo48/crouching-muskrat.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [muskrat / tail]: muskrat-4 and tail-1 have 1.015 units of ink clearance over 18.771 units; requires 4; review required | internal-spacing [muskrat / tail]: muskrat-5 and tail-1 have 1.595 units of ink clearance over 3.75 units; requires 4; review required
  4. pictographic-primitives/_uncategorized_28/natural disaster hurricane house_3f984823-804b-4a87-b5c2-3f6d4596f2d2.svg
     icon_id: natural-disaster-hurricane-house
     current drawing: published/failed/solo48/natural-disaster-hurricane-house.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hurricane]: tail and inner-coil have 1.601 units of ink clearance over 23.085 units; requires 4; review required | internal-spacing [hurricane]: outer-coil and core have 1.624 units of ink clearance over 29.669 units; requires 4; review required | internal-spacing [house]: house-2 and house-4 have 2.277 units of ink clearance over 3.975 units; requires 4; review required (+1 more)
  5. pictographic-primitives/_uncategorized_28/nectar_74f05c03-957b-4b86-b062-d7cbbb568098.svg
     icon_id: nectar
     current drawing: published/failed/solo48/nectar.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 7 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 7 undersized holes; 2 pinches
  6. pictographic-primitives/_uncategorized_28/netsuke_caf0865b-e1c7-4007-9994-158b89caccc0.svg
     icon_id: netsuke
     current drawing: published/failed/solo48/netsuke.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  7. pictographic-primitives/_uncategorized_28/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg
     icon_id: right-profile-with-folded-brain
     current drawing: published/failed/solo48/right-profile-with-folded-brain.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  8. pictographic-primitives/_uncategorized_28/nightclub_4f2adf74-2b0c-4983-8567-ce3c6c50bff8.svg
     icon_id: nightclub
     current drawing: published/failed/solo48/nightclub.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [cornice / door]: cornice-2 and door-top have 2.001 units of ink clearance over 11.25 units; requires 4; review required | internal-spacing [building / door]: building-3 and door-top have 3.522 units of ink clearance over 4.188 units; requires 4; review required | internal-spacing [note-0-right / beam-0]: note-0-right-a and beam-0-2 have 2.246 units of ink clearance over 7.246 units; requires 4; review required (+1 more)
  9. pictographic-primitives/_uncategorized_29/office desk 1_57237fb8-d140-4fc2-97bb-fe24ab1c7285.svg
     icon_id: office-desk-1
     current drawing: published/failed/solo48/office-desk-1.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [monitor]: monitor and clock are 6 apart on centerlines nearest (26, 14)<->(32, 14); (needs 8) | mic [clock]: clock and hands are 1.999 apart on centerlines nearest (37.975, 8.000)<->(38, 10); (needs 8)
       - parallel straight edges under 8: mic [cup]: parallel straight edges cup-3 and cup-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cup]: parallel straight edges cup-2 and desk-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  10. pictographic-primitives/_uncategorized_29/olympic rings_3c672b26-42c9-4289-a407-8947e0d6a086.svg
     icon_id: five-interlocking-olympic-rings
     current drawing: published/failed/solo48/five-interlocking-olympic-rings.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 7 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 7 undersized holes; 2 pinches
  11. pictographic-primitives/_uncategorized_29/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg
     icon_id: outdoors-dog-house
     current drawing: published/failed/solo48/outdoors-dog-house.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [dog]: dog-6 and dog-8 have 0.941 units of ink clearance over 4 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_29/paintbrush_f6746ee9-8a45-44c8-81ef-7d3da12c0bca.svg
     icon_id: pointed-artist-paintbrush
     current drawing: published/failed/solo48/pointed-artist-paintbrush.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  13. pictographic-primitives/_uncategorized_29/paintwork_6c8a1385-af01-4783-b140-1d97d33064f1.svg
     icon_id: broad-tipped-artist-brush
     current drawing: published/failed/solo48/broad-tipped-artist-brush.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [handle-outline]: handle and handle have 1.707 units of ink clearance over 20.411 units; requires 4; review required | internal-spacing [handle-outline / ferrule]: handle-base and ferrule-2 have 2.843 units of ink clearance over 6.25 units; requires 4; review required
  14. pictographic-primitives/_uncategorized_29/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg
     icon_id: pantyhose
     current drawing: published/failed/solo48/pantyhose.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [bent-leg]: outer-thigh and toe-2 have 0.435 units of ink clearance over 5.310 units; requires 4; review required | internal-spacing [bent-leg]: outer-calf and toe-2 have 0.410 units of ink clearance over 13.897 units; requires 4; review required
  15. pictographic-primitives/_uncategorized_29/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg
     icon_id: parking-p
     current drawing: published/failed/solo48/parking-p.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [badge]: badge and p-stem are 3.291 apart on centerlines nearest (27.556, 24.957)<->(29, 22); (needs 8) | mic [badge]: badge and roof are 2.206 apart on centerlines nearest (23.819, 21.751)<->(22, 23); (needs 8) | mic [badge]: badge and car are 4 apart on centerlines nearest (32, 26)<->(32, 30); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [p-stem]: parallel straight edges p-stem-3 and p-return are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [roof]: parallel straight edges roof-2 and car-0 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
```

### batch-07

```
Run $primitive-make-ray to repair failed icons, batch 7 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_30/passport hand_b569bafc-f80a-44b7-a43f-233891818936.svg
     icon_id: passport-hand
     current drawing: published/failed/solo48/passport-hand.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 4 undersized holes; 0 pinches
  2. pictographic-primitives/_uncategorized_30/passport ticket_4813164b-bbb2-498a-aa24-70f1ec279cb1.svg
     icon_id: passport-ticket
     current drawing: published/failed/solo48/passport-ticket.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [passport]: passport and globe are 4 apart on centerlines nearest (6, 29)<->(10, 29); (needs 8) | mic [passport]: passport and ticket-text-0 are 4.071 apart on centerlines nearest (25.967, 20.559)<->(30, 20); (needs 8) | mic [ticket]: ticket and ticket-text-1 are 3.530 apart on centerlines nearest (38.461, 29.692)<->(35, 29); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [ticket-text-0]: parallel straight edges ticket-text-0 and ticket-text-1 are 7.844 apart on centerlines (ink gap 3.844); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 6 undersized holes; 6 pinches
       - undersized holes: holes/pinches: 6 undersized holes; 6 pinches
  3. pictographic-primitives/_uncategorized_30/path logo_34127b46-eb99-4c72-abde-13c6d20da3f3.svg
     icon_id: path-logo
     current drawing: published/failed/solo48/path-logo.svg
     violates 2 rules: parallel straight edges under 8, pinches
       - parallel straight edges under 8: mic [logo]: parallel straight edges stem-left and left-return are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 0 undersized holes; 1 pinches
  4. pictographic-primitives/_uncategorized_30/pencil edit desktop_242c5167-10ea-4717-a24b-bd22d2cf9483.svg
     icon_id: pencil-edit-desktop
     current drawing: published/failed/solo48/pencil-edit-desktop.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [screen / pencil]: screen-3 and pencil-b-2 have 0.171 units of ink clearance over 11.25 units; requires 4; review required
  5. pictographic-primitives/_uncategorized_30/people conflict 1_ede2fe9e-b299-44e2-90dd-71980708f31f.svg
     icon_id: people-conflict-1
     current drawing: published/failed/solo48/people-conflict-1.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [skull-0]: skull-0 and skull-1 are 4 apart on centerlines nearest (22, 30)<->(26, 30); (needs 8) | mic [skull-1]: skull-1 and spark-2 are 6.560 apart on centerlines nearest (36.172, 22.301)<->(38, 16); (needs 8)
       - parallel straight edges under 8: mic [right-back]: parallel straight edges right-back and left-back are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [spark-0]: parallel straight edges spark-0-1 and spark-0-3 are 2.828 apart on centerlines (ink gap -1.171); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [spark-1]: parallel straight edges spark-1-1 and spark-1-3 are 2.828 apart on centerlines (ink gap -1.171); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  6. pictographic-primitives/_uncategorized_30/performance increase mail_15cdcedc-403b-4401-be0b-ba02e4b22811.svg
     icon_id: performance-increase-mail
     current drawing: published/failed/solo48/performance-increase-mail.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [envelope]: envelope and bar-0 are 0.291 apart on centerlines nearest (11.858, 29.254)<->(12, 29); (needs 8) | mic [envelope]: envelope and bar-2 are 0.291 apart on centerlines nearest (36.141, 29.254)<->(36, 29); (needs 8) | mic [bar-1]: bar-1 and trend are 4.123 apart on centerlines nearest (24, 18)<->(23, 14); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [envelope]: parallel straight edges envelope-3 and bar-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [bar-0]: parallel straight edges bar-0 and envelope-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  7. pictographic-primitives/_uncategorized_30/performance tablet increase_2db6cf72-5f8c-42a8-a787-67d6ad07a91f.svg
     icon_id: performance-tablet-increase
     current drawing: published/failed/solo48/performance-tablet-increase.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [tablet]: tablet and trend are 6 apart on centerlines nearest (26, 6)<->(26, 12); (needs 8) | mic [tablet]: tablet and bar-0 are 4 apart on centerlines nearest (14, 42)<->(14, 38); (needs 8) | mic [tablet]: tablet and bar-1 are 4 apart on centerlines nearest (22, 42)<->(22, 38); (needs 8)
       - parallel straight edges under 8: mic [thumb]: parallel straight edges thumb-2 and bar-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tablet]: parallel straight edges tablet-3 and arrow-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  8. pictographic-primitives/_uncategorized_30/pest busters_326bdd17-1f70-4f59-8cfb-654489aa053d.svg
     icon_id: pest-busters
     current drawing: published/failed/solo48/pest-busters.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [head]: head and slash are 5.899 apart on centerlines nearest (26.828, 12.828)<->(31, 17); (needs 8) | mic [body]: body and left0 are 0.714 apart on centerlines nearest (15.646, 20.304)<->(15, 20); (needs 8) | mic [body]: body and right0 are 0.714 apart on centerlines nearest (32.353, 20.304)<->(33, 20); (needs 8) (+6 more)
       - parallel straight edges under 8: mic [right-antenna]: parallel straight edges right-antenna-1 and slash are 7.071 apart on centerlines (ink gap 3.071); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [right0]: parallel straight edges right0-1 and right1-1 are 7.589 apart on centerlines (ink gap 3.589); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [right1]: parallel straight edges right1-1 and right2-1 are 7.589 apart on centerlines (ink gap 3.589); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  9. pictographic-primitives/_uncategorized_30/pickup_dd459eaf-90a6-4872-a777-772bcbc71cdf.svg
     icon_id: compact-pickup-side-view
     current drawing: published/failed/solo48/compact-pickup-side-view.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  10. pictographic-primitives/_uncategorized_30/pillbox_da7fc73f-7180-4170-9161-a6c525c99704.svg
     icon_id: pillbox
     current drawing: published/failed/solo48/pillbox.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [box / lid]: box-1 and lid have 3.215 units of ink clearance over 2.728 units; requires 4; review required | internal-spacing [box / lid]: box-7 and lid have 3.215 units of ink clearance over 2.728 units; requires 4; review required
  11. pictographic-primitives/_uncategorized_31/pinworm_12ed033b-94af-439b-9775-23fdba88d590.svg
     icon_id: curving-pinworm
     current drawing: published/failed/solo48/curving-pinworm.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [worm]: worm-1 and worm-3 have 2.682 units of ink clearance over 2.164 units; requires 4; review required | internal-spacing [worm]: worm-5 and worm-7 have 3.298 units of ink clearance over 9.799 units; requires 4; review required | internal-spacing [worm]: worm-7 and worm-9 have 2.877 units of ink clearance over 3.206 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_31/plane trip cocktail service_102607c1-25ef-426c-be86-bf3e263e4a81.svg
     icon_id: plane-trip-cocktail-service
     current drawing: published/failed/solo48/plane-trip-cocktail-service.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [aircraft]: aircraft and divider are 6 apart on centerlines nearest (23, 20)<->(23, 26); (needs 8) | mic [divider]: divider and bowl are 6 apart on centerlines nearest (15, 26)<->(15, 32); (needs 8) | mic [divider]: divider and citrus are 2 apart on centerlines nearest (29, 26)<->(29, 28); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [aircraft]: parallel straight edges aircraft-12 and divider are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [divider]: parallel straight edges divider and rim are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [aircraft]: parallel straight edges aircraft-1 and aircraft-14 are 7.033 apart on centerlines (ink gap 3.033); requires at least 8 centerline / 4 ink (overlap-fallback)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  13. pictographic-primitives/_uncategorized_31/plane trip food service_373ac967-90cc-46ee-9b78-f2b3cc4a75c9.svg
     icon_id: plane-trip-food-service
     current drawing: published/failed/solo48/plane-trip-food-service.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [aircraft]: aircraft and divider are 6 apart on centerlines nearest (23, 20)<->(23, 26); (needs 8) | mic [divider]: divider and fork are 6 apart on centerlines nearest (12, 26)<->(12, 32); (needs 8) | mic [divider]: divider and fork-stem are 6 apart on centerlines nearest (16, 26)<->(16, 32); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [fork]: parallel straight edges fork-right and fork-stem-1, fork-stem-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [fork-stem]: parallel straight edges fork-stem-1, fork-stem-2 and fork-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [aircraft]: parallel straight edges aircraft-12 and divider are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  14. pictographic-primitives/_uncategorized_31/plane trip person_5ba1d1e1-9400-4baf-a55c-e0c11aabf158.svg
     icon_id: plane-trip-person
     current drawing: published/failed/solo48/plane-trip-person.svg
     violates 1 rule: parallel straight edges under 8
       - parallel straight edges under 8: mic [torso]: parallel straight edges torso and bag-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  15. pictographic-primitives/_uncategorized_31/playroom_c6ecc684-688c-443b-ae9b-74c5652fb4fa.svg
     icon_id: playroom
     current drawing: published/failed/solo48/playroom.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [house / toy-knob]: house-2 and toy-knob-1 have 3.261 units of ink clearance over 6.940 units; requires 4; review required | internal-spacing [house / toy-knob]: house-3 and toy-knob-1 have 2.195 units of ink clearance over 2.75 units; requires 4; review required | internal-spacing [house / toy-knob]: house-3 and toy-knob-2 have 2.195 units of ink clearance over 3.25 units; requires 4; review required (+6 more)
```

### batch-08

```
Run $primitive-make-ray to repair failed icons, batch 8 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_31/plug circle xmark_2fa2e764-f653-4eb6-b13a-4c6d7b198877.svg
     icon_id: plug-circle-xmark
     current drawing: published/failed/solo48/plug-circle-xmark.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [plug-top / plug-bowl]: plug-top-2 and bowl-right have 2.215 units of ink clearance over 2.728 units; requires 4; review required | internal-spacing [plug-top / plug-bowl]: plug-top-2 and bowl-left have 2.215 units of ink clearance over 2.728 units; requires 4; review required
  2. pictographic-primitives/_uncategorized_31/polyester_7a069c80-678a-480c-a3ff-5da10f209d9c.svg
     icon_id: polyester
     current drawing: published/failed/solo48/polyester.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [fold]: fold and vertical-2 are 0.707 apart on centerlines nearest (31.5, 15.5)<->(31, 16); (needs 8)
       - parallel straight edges under 8: mic [sheet]: parallel straight edges sheet-8 and fold-2 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  3. pictographic-primitives/_uncategorized_31/pound_4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9.svg
     icon_id: pound
     current drawing: published/failed/solo48/pound.svg
     violates 1 rule: parallel straight edges under 8
       - parallel straight edges under 8: mic [pound]: parallel straight edges bar-right-1 and foot-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  4. pictographic-primitives/_uncategorized_31/prescription drug px 2_5a9d43a5-7519-4e64-81a0-64a7c06298cc.svg
     icon_id: prescription-drug-px-2
     current drawing: published/failed/solo48/prescription-drug-px-2.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [paper]: paper and rx-down are 5 apart on centerlines nearest (34, 28)<->(29, 28); (needs 8) | mic [paper]: paper and writing-0 are 7 apart on centerlines nearest (12, 33)<->(19, 33); (needs 8) | mic [paper]: paper and writing-1 are 3 apart on centerlines nearest (19, 42)<->(19, 39); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [writing-0]: parallel straight edges writing-0 and writing-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [writing-1]: parallel straight edges writing-1 and paper-bottom are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  5. pictographic-primitives/_uncategorized_31/programming hold code 2_f5badc78-84c0-4392-89e1-d9fa0712f0cb.svg
     icon_id: programming-hold-code-2
     current drawing: published/failed/solo48/programming-hold-code-2.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [cupped-left]: hand-left and palm-left have 3.155 units of ink clearance over 4.952 units; requires 4; review required | internal-spacing [cupped-left]: hand-left and finger-left have 0 units of ink clearance over 3.067 units; requires 4; review required | internal-spacing [cupped-left]: hand-left and palm-left have 0.117 units of ink clearance over 3.067 units; requires 4; review required (+5 more)
  6. pictographic-primitives/_uncategorized_31/protocol open id logo_962c33a0-eaf5-4a99-9127-a5fd1da5870b.svg
     icon_id: protocol-open-id-logo
     current drawing: published/failed/solo48/protocol-open-id-logo.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [arrow-upper / arrow-lower]: arrow-upper-1 and arrow-lower-2 have 0.277 units of ink clearance over 8.447 units; requires 4; review required | internal-spacing [outer-loop / inner-loop]: outer-loop and inner-loop have 1.574 units of ink clearance over 22.531 units; requires 4; review required | internal-spacing [outer-loop / inner-loop]: outer-loop and inner-loop have 1.551 units of ink clearance over 20.693 units; requires 4; review required
  7. pictographic-primitives/_uncategorized_31/psycho analysis 5_fc8e8b95-766a-4f15-a80b-5e30979a5fc8.svg
     icon_id: psycho-analysis-5
     current drawing: published/failed/solo48/psycho-analysis-5.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [head-bowl / shoulders]: jaw and shoulders have 0.018 units of ink clearance over 6.010 units; requires 4; review required | internal-spacing [head-bowl / shoulders]: jaw and shoulders have 0.018 units of ink clearance over 6.010 units; requires 4; review required
  8. pictographic-primitives/_uncategorized_32/quote left_bbf400c0-4ed9-481e-8643-979aa728bc9d.svg
     icon_id: quote-left
     current drawing: published/failed/solo48/quote-left.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [quote-0]: quote-0-outer and quote-0-inner have 2.341 units of ink clearance over 19.617 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer and quote-1-inner have 2.341 units of ink clearance over 19.617 units; requires 4; review required
  9. pictographic-primitives/_uncategorized_32/quote right_a669591d-8405-49c2-be0a-5d69af49a20c.svg
     icon_id: quote-right
     current drawing: published/failed/solo48/quote-right.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [quote-0]: quote-0-outer and quote-0-inner have 2.341 units of ink clearance over 19.617 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer and quote-1-inner have 2.341 units of ink clearance over 19.617 units; requires 4; review required
  10. pictographic-primitives/_uncategorized_32/quotes_d8e178df-75a7-436c-99cf-7f7c90cf866a.svg
     icon_id: quotes
     current drawing: published/failed/solo48/quotes.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [quote-0]: quote-0-outer-tail and quote-0-inner-tail have 1.830 units of ink clearance over 17.537 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer-tail and quote-1-inner-tail have 1.830 units of ink clearance over 17.537 units; requires 4; review required
  11. pictographic-primitives/_uncategorized_32/rating booklet_d9776d01-07f9-402d-ac77-fc73a405a509.svg
     icon_id: rating-booklet
     current drawing: published/failed/solo48/rating-booklet.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [cover]: cover and rating-star are 6 apart on centerlines nearest (24, 12)<->(24, 18); (needs 8) | mic [cover]: cover and text-0 are 6 apart on centerlines nearest (20, 44)<->(20, 38); (needs 8) | mic [cover]: cover and text-1 are 3 apart on centerlines nearest (20, 44)<->(20, 41); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [text-0]: parallel straight edges text-0 and text-1 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [text-0]: parallel straight edges text-0 and cover-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [text-1]: parallel straight edges text-1 and cover-4 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal)
  12. pictographic-primitives/_uncategorized_32/real estate deal shake_490f19a8-c170-4914-bea1-18cbfb479033.svg
     icon_id: real-estate-deal-shake
     current drawing: published/failed/solo48/real-estate-deal-shake.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [handshake-outline]: left-hand-top-1 and thumb-1 have -0.899 units of ink clearance over 2.189 units; requires 4; review required | internal-spacing [handshake-outline]: left-hand-top-2 and thumb-return have 1.352 units of ink clearance over 2.220 units; requires 4; review required | internal-spacing [handshake-outline]: thumb-return and fingers-bottom have 3.138 units of ink clearance over 7.901 units; requires 4; review required (+1 more)
  13. pictographic-primitives/_uncategorized_32/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg
     icon_id: real-estate-favorite-house-rating
     current drawing: published/failed/solo48/real-estate-favorite-house-rating.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [main-star]: main-star and star-0 are 4.438 apart on centerlines nearest (18.378, 19.729)<->(14, 19); (needs 8) | mic [main-star]: main-star and star-1 are 4.438 apart on centerlines nearest (29.621, 19.729)<->(34, 19); (needs 8) | mic [main-star]: main-star and roof are 4.472 apart on centerlines nearest (22, 20)<->(24, 24); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [house]: parallel straight edges walls-right-3 and walls-right-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [house]: parallel straight edges walls-right-1 and walls-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [house]: parallel straight edges walls-3 and walls-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  14. pictographic-primitives/_uncategorized_32/real estate market calculator house_110df7d0-d83c-4e1f-a771-57b0adb39e09.svg
     icon_id: real-estate-market-calculator-house
     current drawing: published/failed/solo48/real-estate-market-calculator-house.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [roof]: roof and house-wall are 4.472 apart on centerlines nearest (42, 16)<->(40, 20); (needs 8) | mic [roof]: roof and calculator are 2 apart on centerlines nearest (18, 16)<->(18, 18); (needs 8) | mic [house-wall]: house-wall and calculator are 2 apart on centerlines nearest (34, 28)<->(32, 28); (needs 8) (+6 more)
       - parallel straight edges under 8: mic [vertical-divider]: parallel straight edges vertical-divider-1, vertical-divider-2 and plus-bottom are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [vertical-divider]: parallel straight edges vertical-divider-1, vertical-divider-2 and plus-top are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [plus-bottom]: parallel straight edges plus-bottom and calculator-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+10 more)
       - undersized holes: holes/pinches: 3 undersized holes; 0 pinches
  15. pictographic-primitives/_uncategorized_32/real estate market house_1228a3cf-b0ac-41b8-a4db-2d272fbe1241.svg
     icon_id: real-estate-market-house
     current drawing: published/failed/solo48/real-estate-market-house.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [segment]: segment and house are 3.654 apart on centerlines nearest (34, 24)<->(31.572, 26.731); (needs 8)
       - parallel straight edges under 8: mic [house]: parallel straight edges house-3 and door-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-1 and house-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
```

### batch-09

```
Run $primitive-make-ray to repair failed icons, batch 9 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_32/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg
     icon_id: real-estate-message-couple-building
     current drawing: published/failed/solo48/real-estate-message-couple-building.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [bubble]: bubble and house are 2 apart on centerlines nearest (30, 20)<->(30, 18); (needs 8) | mic [bubble]: bubble and left-head are 6 apart on centerlines nearest (12, 20)<->(12, 26); (needs 8) | mic [bubble]: bubble and right-head are 6 apart on centerlines nearest (36, 20)<->(36, 26); (needs 8)
       - parallel straight edges under 8: mic [house]: parallel straight edges house-4 and bubble-6 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [house]: parallel straight edges house-4 and bubble-3 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap-fallback)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  2. pictographic-primitives/_uncategorized_32/real estate search house 2_eb4e4433-41fd-4f9e-9779-df93d4b8c025.svg
     icon_id: real-estate-search-house-2
     current drawing: published/failed/solo48/real-estate-search-house-2.svg
     violates 1 rule: parallel straight edges under 8
       - parallel straight edges under 8: mic [house]: parallel straight edges house-3 and door-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-1 and house-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  3. pictographic-primitives/_uncategorized_32/recruiting resume document_37ae4172-af70-4ae7-8de2-52970a6302ab.svg
     icon_id: recruiting-resume-document
     current drawing: published/failed/solo48/recruiting-resume-document.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [document]: document and text1 are 4 apart on centerlines nearest (14, 42)<->(14, 38); (needs 8) | mic [document]: document and body are 5.918 apart on centerlines nearest (24, 42)<->(29.837, 41.027); (needs 8) | mic [text0]: text0 and shoulders are 5.871 apart on centerlines nearest (22, 30)<->(26.854, 33.302); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [text1]: parallel straight edges text1 and document-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  4. pictographic-primitives/_uncategorized_32/rectangle code_0efa564f-5fe3-43ba-904f-a0826782e979.svg
     icon_id: rectangle-code
     current drawing: published/failed/solo48/rectangle-code.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [frame]: frame and tr are 6 apart on centerlines nearest (42, 14)<->(36, 14); (needs 8) | mic [frame]: frame and bl are 6 apart on centerlines nearest (22, 42)<->(22, 36); (needs 8) | mic [frame]: frame and dash are 4 apart on centerlines nearest (32, 42)<->(32, 38); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [frame]: parallel straight edges frame-2 and tr-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [corner]: parallel straight edges corner-1 and bl-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tr]: parallel straight edges tr-4 and tl-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
  5. pictographic-primitives/_uncategorized_32/rectangle vertical history_69099a2e-0b2c-47a9-931c-af42c66da3a2.svg
     icon_id: rectangle-vertical-history
     current drawing: published/failed/solo48/rectangle-vertical-history.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [panel]: panel and history are 6 apart on centerlines nearest (40, 24)<->(34, 24); (needs 8) | mic [history]: history and hands are 3.999 apart on centerlines nearest (23.987, 14.000)<->(24, 18); (needs 8)
       - parallel straight edges under 8: mic [panel]: parallel straight edges panel-2 and arrow-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [arrow]: parallel straight edges arrow-1 and hands-2 are 7.071 apart on centerlines (ink gap 3.071); requires at least 8 centerline / 4 ink (midpoint-normal)
  6. pictographic-primitives/_uncategorized_32/recycling label_aec06f81-4835-4b96-93f1-57f1ca360f5e.svg
     icon_id: recycling-label
     current drawing: published/failed/solo48/recycling-label.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [tag-outline]: tag-outline and eyelet are 4.778 apart on centerlines nearest (35.5, 19.5)<->(32.121, 16.121); (needs 8) | mic [tag-outline]: tag-outline and leaf are 4.936 apart on centerlines nearest (27.346, 27.653)<->(30.836, 31.144); (needs 8)
  7. pictographic-primitives/_uncategorized_32/refugee immigration war 2_922ba268-0492-4ece-8f41-54253b52949a.svg
     icon_id: refugee-immigration-war-2
     current drawing: published/failed/solo48/refugee-immigration-war-2.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [explosion]: explosion and capsule are 3.038 apart on centerlines nearest (12, 16)<->(14.689, 17.414); (needs 8) | mic [explosion]: explosion and roof are 2.494 apart on centerlines nearest (29.706, 26.982)<->(32, 26); (needs 8)
       - parallel straight edges under 8: mic [house]: parallel straight edges house-3 and door-right are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-right and door-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-left and house-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  8. pictographic-primitives/_uncategorized_32/religion cao dai_77937bbd-92c4-4b29-ac40-52719ed0b6cd.svg
     icon_id: religion-cao-dai
     current drawing: published/failed/solo48/religion-cao-dai.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [triangle]: triangle and eye are 1.788 apart on centerlines nearest (11.4, 31.2)<->(13, 32); (needs 8) | mic [triangle]: triangle and iris are 7 apart on centerlines nearest (24, 42)<->(24, 35); (needs 8) | mic [eye]: eye and iris are 2.999 apart on centerlines nearest (23.976, 37.999)<->(24, 35); (needs 8)
  9. pictographic-primitives/_uncategorized_32/remains_7c0ac5c3-a514-484c-9bdf-404c88d05eb7.svg
     icon_id: remains
     current drawing: published/failed/solo48/remains.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [bone]: shaft-upper and shaft-lower have 1.934 units of ink clearance over 4.712 units; requires 4; review required
  10. pictographic-primitives/_uncategorized_32/remote access_c9953fdc-3825-4f26-8597-533126256825.svg
     icon_id: remote-access
     current drawing: published/failed/solo48/remote-access.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [inner]: inner and center are 5 apart on centerlines nearest (24, 16)<->(24, 21); (needs 8)
  11. pictographic-primitives/_uncategorized_33/rogue_4eebbb0e-3d47-4014-a9b8-95819896ada8.svg
     icon_id: hooded-person-with-blank-face
     current drawing: published/failed/solo48/hooded-person-with-blank-face.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [face / shoulders]: face-1 and shoulders have 0.026 units of ink clearance over 3.506 units; requires 4; review required | internal-spacing [face / shoulders]: face-1 and shoulders have 0.026 units of ink clearance over 3.506 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_33/route interstate_65d8507f-531a-4e81-bd3e-1e2516aebe33.svg
     icon_id: route-interstate
     current drawing: published/failed/solo48/route-interstate.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [shield / header]: left-top and header have 3.686 units of ink clearance over 7 units; requires 4; review required | internal-spacing [shield / header]: right-top and header have 3.686 units of ink clearance over 7 units; requires 4; review required
  13. pictographic-primitives/_uncategorized_33/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg
     icon_id: rupee-sign
     current drawing: published/failed/solo48/rupee-sign.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [bowl-leg / top]: bowl-top and top have -3.983 units of ink clearance over 6.25 units; requires 4; review required
  14. pictographic-primitives/_uncategorized_33/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg
     icon_id: saving-bull
     current drawing: published/failed/solo48/saving-bull.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [animal]: animal and trend are 2.431 apart on centerlines nearest (27.849, 20.142)<->(29, 18); (needs 8)
       - parallel straight edges under 8: mic [tail]: parallel straight edges tail-2 and legs-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 2 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 1 pinches
  15. pictographic-primitives/_uncategorized_33/seeker_eebf9355-e5dd-4833-b849-ec1865cc85fe.svg
     icon_id: seeker
     current drawing: published/failed/solo48/seeker.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [head]: head and lens are 5.261 apart on centerlines nearest (19.983, 16.486)<->(23.468, 20.427); (needs 8) | mic [body]: body and arm-edge are 5.999 apart on centerlines nearest (6.000, 33.926)<->(12, 34); (needs 8) | mic [body-right]: body-right and lens are 2.165 apart on centerlines nearest (28, 40)<->(28.347, 37.862); (needs 8)
       - parallel straight edges under 8: mic [arm-edge]: parallel straight edges arm-edge and body-side-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
```

### batch-10

```
Run $primitive-make-ray to repair failed icons, batch 10 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_33/self driving car_7a8b5b6b-d72f-42df-9379-3389fd1e33fd.svg
     icon_id: self-driving-car
     current drawing: published/failed/solo48/self-driving-car.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [body]: body and headlight-0 are 5 apart on centerlines nearest (14, 26)<->(14, 31); (needs 8) | mic [body]: body and headlight-1 are 5 apart on centerlines nearest (34, 26)<->(34, 31); (needs 8) | mic [roof]: roof and radio-inner are 4 apart on centerlines nearest (18, 18)<->(18, 14); (needs 8) (+1 more)
  2. pictographic-primitives/_uncategorized_33/sense of stability_0257fd69-7a18-40fc-a7d2-903d1b421449.svg
     icon_id: sense-of-stability
     current drawing: published/failed/solo48/sense-of-stability.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [bottom]: bottom and legs are 3.907 apart on centerlines nearest (21.645, 41.891)<->(22, 38); (needs 8)
       - parallel straight edges under 8: mic [wall-right]: parallel straight edges wall-right-1, wall-right-2 and window-right-1, window-right-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [window-left]: parallel straight edges window-left-1, window-left-2 and wall-left-1, wall-left-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  3. pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg
     icon_id: seo-search-eye
     current drawing: published/failed/solo48/seo-search-eye.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [lens]: lens and eye are 3.999 apart on centerlines nearest (6.000, 21.034)<->(10, 21); (needs 8) | mic [eye]: eye and iris are 2.749 apart on centerlines nearest (20.975, 27.749)<->(21, 25); (needs 8)
  4. pictographic-primitives/_uncategorized_34/shipment approve smartphone_59f997a9-32d8-436a-ae34-06535681b16e.svg
     icon_id: shipment-approve-smartphone
     current drawing: published/failed/solo48/shipment-approve-smartphone.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [box-edge]: box-edge and phone are 5 apart on centerlines nearest (30, 16)<->(30, 21); (needs 8) | mic [phone]: phone and check are 4 apart on centerlines nearest (42, 27)<->(38, 27); (needs 8) | mic [phone]: phone and home are 5 apart on centerlines nearest (32, 42)<->(32, 37); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [home]: parallel straight edges home and phone-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  5. pictographic-primitives/_uncategorized_34/shipment fragile_6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f.svg
     icon_id: shipment-fragile
     current drawing: published/failed/solo48/shipment-fragile.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [tape]: tape and glass are 7 apart on centerlines nearest (18, 17)<->(18, 24); (needs 8) | mic [box]: box and stem are 5 apart on centerlines nearest (19, 42)<->(19, 37); (needs 8) | mic [box]: box and arrow-head are 5 apart on centerlines nearest (42, 28)<->(37, 28); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [foot]: parallel straight edges foot and box-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  6. pictographic-primitives/_uncategorized_34/shopping pay hide advertising_59b04c40-2006-4e31-a230-a6be869385d4.svg
     icon_id: shopping-pay-hide-advertising
     current drawing: published/failed/solo48/shopping-pay-hide-advertising.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 4 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 1 pinches
  7. pictographic-primitives/_uncategorized_34/side road angle left 2_d0d6406a-6c7c-431f-a9b8-ee87990c2cf2.svg
     icon_id: side-road-angle-left-2
     current drawing: published/failed/solo48/side-road-angle-left-2.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [diamond]: diamond and road are 4.242 apart on centerlines nearest (15, 33)<->(18, 30); (needs 8)
       - parallel straight edges under 8: mic [diamond]: parallel straight edges diamond-1 and head-1 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal)
  8. pictographic-primitives/_uncategorized_34/side road angle right 2_d19fe7af-bf3f-4193-8210-2e69b664727e.svg
     icon_id: side-road-angle-right-2
     current drawing: published/failed/solo48/side-road-angle-right-2.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [diamond]: diamond and branch are 2.828 apart on centerlines nearest (32, 34)<->(30, 32); (needs 8)
       - parallel straight edges under 8: mic [diamond]: parallel straight edges diamond-4 and head-1 are 7.071 apart on centerlines (ink gap 3.071); requires at least 8 centerline / 4 ink (midpoint-normal)
  9. pictographic-primitives/_uncategorized_34/single woman hierachy_868652f3-4bc5-4fe0-96a0-1bc2494937b3.svg
     icon_id: single-woman-hierachy
     current drawing: published/failed/solo48/single-woman-hierachy.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [spine / node-0]: spine-1 and node-0-3 have 0.135 units of ink clearance over 2.25 units; requires 4; review required | internal-spacing [spine / node-1]: spine-1 and node-1-0 have 0.135 units of ink clearance over 2.75 units; requires 4; review required | internal-spacing [spine / node-1]: spine-2 and node-1-3 have 0.135 units of ink clearance over 2.25 units; requires 4; review required (+1 more)
  10. pictographic-primitives/_uncategorized_34/smart induction stove_cc0f870e-e6f6-426d-9d3f-73d669be714f.svg
     icon_id: smart-induction-stove
     current drawing: published/failed/solo48/smart-induction-stove.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [top]: top and wifi-outer are 6 apart on centerlines nearest (24, 6)<->(24, 12); (needs 8) | mic [front-top]: front-top and wifi-inner are 5 apart on centerlines nearest (20, 28)<->(20, 23); (needs 8) | mic [wifi-outer]: wifi-outer and wifi-inner are 7.517 apart on centerlines nearest (32, 16)<->(27.379, 21.93); (needs 8)
       - parallel straight edges under 8: mic [front]: parallel straight edges front-5, front-4, front-3 and base-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  11. pictographic-primitives/_uncategorized_34/smart refrigerator device_30cd9303-dbd1-4ff5-9b6d-c3de44b1a7e4.svg
     icon_id: smart-refrigerator-device
     current drawing: published/failed/solo48/smart-refrigerator-device.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [fridge]: fridge and handle-0 are 6 apart on centerlines nearest (6, 12)<->(12, 12); (needs 8) | mic [fridge]: fridge and handle-1 are 6 apart on centerlines nearest (6, 30)<->(12, 30); (needs 8) | mic [fridge]: fridge and wireless-inner are 2.246 apart on centerlines nearest (28, 16)<->(28.542, 18.179); (needs 8) (+4 more)
       - parallel straight edges under 8: mic [handle-0]: parallel straight edges handle-0 and fridge-left-upper, fridge-left-lower are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [handle-1]: parallel straight edges handle-1 and fridge-left-upper, fridge-left-lower are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  12. pictographic-primitives/_uncategorized_34/smiley bright_d25557be-d198-406c-ac40-686ab3f61c2a.svg
     icon_id: sparkle-eyed-face-with-uneven-smile
     current drawing: published/failed/solo48/sparkle-eyed-face-with-uneven-smile.svg
     violates 3 rules: part spacing under 8, pinches, undersized holes
       - part spacing under 8: mic [face]: face and eye-16 are 7.469 apart on centerlines nearest (6.434, 14.438)<->(13, 18); (needs 8) | mic [face]: face and eye-32 are 7.469 apart on centerlines nearest (41.566, 14.438)<->(35, 18); (needs 8)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  13. pictographic-primitives/_uncategorized_34/smiley decode_2421c5d7-2ff1-480c-8526-9252cbdd43cf.svg
     icon_id: angry-face-with-broad-mouth-cover
     current drawing: published/failed/solo48/angry-face-with-broad-mouth-cover.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [dome]: dome and eye-left are 7.704 apart on centerlines nearest (15.243, 8.273)<->(19, 15); (needs 8) | mic [dome]: dome and eye-right are 7.704 apart on centerlines nearest (32.756, 8.273)<->(29, 15); (needs 8)
  14. pictographic-primitives/_uncategorized_34/smiley shine big eyes_58fdbda2-95d4-42f4-b93e-df89f627bc82.svg
     icon_id: large-sparkle-eyed-smiling-face
     current drawing: published/failed/solo48/large-sparkle-eyed-smiling-face.svg
     violates 3 rules: part spacing under 8, pinches, undersized holes
       - part spacing under 8: mic [face]: face and eye-16 are 7.469 apart on centerlines nearest (6.434, 14.438)<->(13, 18); (needs 8) | mic [face]: face and eye-32 are 7.469 apart on centerlines nearest (41.566, 14.438)<->(35, 18); (needs 8)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  15. pictographic-primitives/_uncategorized_34/snake_793e902f-88a8-4473-bf76-f80306c7a173.svg
     icon_id: upright-snake-with-curled-lower-body
     current drawing: published/failed/solo48/upright-snake-with-curled-lower-body.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [snake]: snake-0 and snake-13 have 1.219 units of ink clearance over 6.244 units; requires 4; review required | internal-spacing [snake]: snake-0 and snake-14 have 1.259 units of ink clearance over 5.793 units; requires 4; review required | internal-spacing [snake]: snake-1 and snake-13 have 0.999 units of ink clearance over 12.720 units; requires 4; review required (+10 more)
```

### batch-11

```
Run $primitive-make-ray to repair failed icons, batch 11 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_34/snarl_47ddf223-ee29-448c-9235-3145f69bc3fa.svg
     icon_id: snarling-face-with-two-fangs
     current drawing: published/failed/solo48/snarling-face-with-two-fangs.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  2. pictographic-primitives/_uncategorized_34/soccer kick ball_7637106f-a796-4b5a-8382-ddbd48faa5f0.svg
     icon_id: football-boot-kicking-panelled-ball
     current drawing: published/failed/solo48/football-boot-kicking-panelled-ball.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [boot]: boot-2 and boot-4 have 3.068 units of ink clearance over 15.147 units; requires 4; review required
  3. pictographic-primitives/_uncategorized_35/sonic 1_eb2aefc1-7636-41c6-9f3f-921141c93aab.svg
     icon_id: sonic-head-with-swept-spines
     current drawing: published/failed/solo48/sonic-head-with-swept-spines.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [head]: head-1 and head-3 have 2.312 units of ink clearance over 2.447 units; requires 4; review required | internal-spacing [head]: head-3 and head-5 have 1.592 units of ink clearance over 4.445 units; requires 4; review required
  4. pictographic-primitives/_uncategorized_35/spasm_c67c9f34-aa4a-4561-aba3-e1d5e5f4f809.svg
     icon_id: spasm
     current drawing: published/failed/solo48/spasm.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [bolt]: bolt-5 and bolt-7 have 3.374 units of ink clearance over 2.467 units; requires 4; review required
  5. pictographic-primitives/_uncategorized_35/spork_af4b0bcf-b76c-4768-8a09-e4eb2d20860e.svg
     icon_id: three-tined-spork-with-rounded-handle
     current drawing: published/failed/solo48/three-tined-spork-with-rounded-handle.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [spork]: spork-0 and spork-11 have -0.343 units of ink clearance over 3.284 units; requires 4; review required | internal-spacing [spork]: spork-6 and spork-8 have -0.343 units of ink clearance over 3.886 units; requires 4; review required
  6. pictographic-primitives/_uncategorized_35/spreadsheet data analysis_25858b73-169f-47b3-b602-412321f8cd10.svg
     icon_id: spreadsheet-data-analysis
     current drawing: published/failed/solo48/spreadsheet-data-analysis.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [axes / curve]: axes-2 and curve have 0.036 units of ink clearance over 4.25 units; requires 4; review required
  7. pictographic-primitives/_uncategorized_35/square fragile_611bc604-f296-4d2b-bb5f-5565ddcd7e36.svg
     icon_id: square-fragile
     current drawing: published/failed/solo48/square-fragile.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [foot / bowl-bottom]: foot-1 and bowl-bottom have 0.016 units of ink clearance over 4 units; requires 4; review required | internal-spacing [foot / bowl-bottom]: foot-2 and bowl-bottom have 0.016 units of ink clearance over 4 units; requires 4; review required
  8. pictographic-primitives/_uncategorized_35/square phone hangup_48b58407-6e7b-4cf9-b629-9742f8a963af.svg
     icon_id: square-phone-hangup
     current drawing: published/failed/solo48/square-phone-hangup.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [handset]: handset and handset have -2.065 units of ink clearance over 13.147 units; requires 4; review required
  9. pictographic-primitives/_uncategorized_35/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg
     icon_id: square-phone
     current drawing: published/failed/solo48/square-phone.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [handset]: handset and handset have -2.065 units of ink clearance over 13.147 units; requires 4; review required
  10. pictographic-primitives/_uncategorized_36/station wagon_11bcc694-f1a4-49f8-94dc-9d171a957687.svg
     icon_id: station-wagon-reference-11bcc694
     current drawing: published/failed/solo48/station-wagon-reference-11bcc694.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  11. pictographic-primitives/_uncategorized_36/step uncle_eb0291a2-d110-4e0e-9cb6-552c49ef98d5.svg
     icon_id: step-uncle
     current drawing: published/failed/solo48/step-uncle.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [badge / hem]: badge-lower and hem have -3.966 units of ink clearance over 3 units; requires 4; review required
  12. pictographic-primitives/_uncategorized_36/street view_6498afd8-8355-4072-b42d-b96eef9111b1.svg
     icon_id: street-view
     current drawing: published/failed/solo48/street-view.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [arms / legs]: arms-1 and legs-2 have 0.751 units of ink clearance over 4 units; requires 4; review required | internal-spacing [arms / legs]: arms-2 and legs-3 have 2.183 units of ink clearance over 3.689 units; requires 4; review required
  13. pictographic-primitives/_uncategorized_37/tandem bike_bf66e761-47e7-4f37-adf7-8e87414c6db8.svg
     icon_id: single-rider-road-bicycle
     current drawing: published/failed/solo48/single-rider-road-bicycle.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 3 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 1 pinches
  14. pictographic-primitives/_uncategorized_37/task list pin 1_5de932db-9cc5-44c6-b9d7-4ae36e88165f.svg
     icon_id: task-list-pin-1
     current drawing: published/failed/solo48/task-list-pin-1.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  15. pictographic-primitives/_uncategorized_38/truck medical_c14f0462-1a4f-4fce-8591-b63fddf2fa6d.svg
     icon_id: truck-medical
     current drawing: published/failed/solo48/truck-medical.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [cargo / wheel-left]: cargo-2 and wheel-left-top have 0.079 units of ink clearance over 3.5 units; requires 4; review required | internal-spacing [cab / wheel-right]: cab-3 and wheel-right-top have 0.079 units of ink clearance over 3 units; requires 4; review required
```

### batch-12

```
Run $primitive-make-ray to repair failed icons, batch 12 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/_uncategorized_39/type cursor_54b02242-5568-41c3-a69f-a06ca068bbf9.svg
     icon_id: type-cursor
     current drawing: published/failed/solo48/type-cursor.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [field / hook]: field-bottom-2 and hook have 3.215 units of ink clearance over 2.728 units; requires 4; review required
  2. pictographic-primitives/_uncategorized_39/user cash scale 1_79fff0c7-26d4-4146-b968-24705c1e7d4a.svg
     icon_id: user-cash-scale-1
     current drawing: published/failed/solo48/user-cash-scale-1.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 4 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 2 pinches
  3. pictographic-primitives/_uncategorized_39/user signal_2000d10a-a193-4355-bf76-3a121de4ad3f.svg
     icon_id: user-signal
     current drawing: published/failed/solo48/user-signal.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  4. pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg
     icon_id: valve-logo
     current drawing: published/failed/solo48/valve-logo.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [v-first]: v-first and a-sides are 5.965 apart on centerlines nearest (10, 10)<->(15.931, 10.635); (needs 8) | mic [v-first]: v-first and a-bar are 6.001 apart on centerlines nearest (8.032, 28.360)<->(14, 29); (needs 8) | mic [a-sides]: a-sides and a-bar are 0.035 apart on centerlines nearest (13.964, 28.996)<->(14, 29); (needs 8) (+4 more)
       - parallel straight edges under 8: mic [v-first]: parallel straight edges v-first-2 and a-sides-1 are 5.965 apart on centerlines (ink gap 1.965); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  5. pictographic-primitives/_uncategorized_40/wave square_23bded82-26fd-41b4-9b35-3c4566fa527a.svg
     icon_id: wave-square
     current drawing: published/failed/solo48/wave-square.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [wave]: wave-rise and wave-curl have -0.896 units of ink clearance over 10.609 units; requires 4; review required
  6. pictographic-primitives/_uncategorized_40/zcool logo_14555301-7f11-43db-978e-a383d12a3b27.svg
     icon_id: zcool-logo
     current drawing: published/failed/solo48/zcool-logo.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [flame]: flame-upper and flame-upper have 1.377 units of ink clearance over 2.103 units; requires 4; review required
  7. pictographic-primitives/design/design pen tool_cd921e04-704d-5a6b-a478-676cad6d9f2e.svg
     icon_id: design-pen-tool
     current drawing: published/failed/solo48/design-pen-tool.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [control]: control and handle-left are 4 apart on centerlines nearest (20, 10)<->(16, 10); (needs 8) | mic [control]: control and handle-right are 4 apart on centerlines nearest (28, 10)<->(32, 10); (needs 8) | mic [control]: control and nib are 4 apart on centerlines nearest (24, 14)<->(24, 18); (needs 8)
       - parallel straight edges under 8: mic [control]: parallel straight edges control-4 and control-2 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [control]: parallel straight edges control-1 and control-3 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  8. pictographic-primitives/ecology/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg
     icon_id: noise-pollution-car
     current drawing: published/failed/solo48/noise-pollution-car.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 3 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 2 pinches
  9. pictographic-primitives/entertainment/concert rock_3a11e17f-1153-59b2-b135-910a41a584c7.svg
     icon_id: concert-rock
     current drawing: published/failed/solo48/concert-rock.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [hand]: hand and left-bolt are 2 apart on centerlines nearest (12, 14)<->(12, 12); (needs 8) | mic [hand]: hand and top-bolt are 7.313 apart on centerlines nearest (33.171, 15.171)<->(28, 10); (needs 8) | mic [hand]: hand and right-bolt are 2 apart on centerlines nearest (36, 14)<->(36, 12); (needs 8)
       - parallel straight edges under 8: mic [top-bolt]: parallel straight edges top-bolt-1 and top-bolt-3 are 4.242 apart on centerlines (ink gap 0.242); requires at least 8 centerline / 4 ink (midpoint-normal)
  10. pictographic-primitives/finance/virtual coin crypto 0x zrx_24bf1d97-6037-5919-9f14-530a400a7d7a.svg
     icon_id: virtual-coin-crypto-0x-zrx
     current drawing: published/failed/solo48/virtual-coin-crypto-0x-zrx.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [coin]: coin and diagonal-low are 0.201 apart on centerlines nearest (9.857, 38.141)<->(10, 38); (needs 8)
       - parallel straight edges under 8: mic [x-outline]: parallel straight edges x-outline-10 and x-outline-8 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [x-outline]: parallel straight edges x-outline-2 and x-outline-4 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [x-outline]: parallel straight edges x-outline-1 and x-outline-11 are 5.656 apart on centerlines (ink gap 1.656); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  11. pictographic-primitives/food/symbol fork cross knife_aba5bfb7-5990-4b45-9606-e4cfe58ad1ea.svg
     icon_id: crossed-fork-and-chef-knife
     current drawing: published/failed/solo48/crossed-fork-and-chef-knife.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [fork-head / knife-handle]: fork-left-curve and knife-handle-1 have 1.673 units of ink clearance over 8.734 units; requires 4; review required | internal-spacing [fork-head / knife-handle]: fork-right-curve and knife-handle-2 have 1.673 units of ink clearance over 7.237 units; requires 4; review required
  12. pictographic-primitives/food/symbol spoon cross fork_53cd4f82-ae5a-4f7a-8ddd-de64747944f4.svg
     icon_id: crossed-fork-with-spoon
     current drawing: published/failed/solo48/crossed-fork-with-spoon.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [fork-head / spoon-handle]: fork-left-curve and spoon-handle-1 have 1.673 units of ink clearance over 8.734 units; requires 4; review required | internal-spacing [fork-head / spoon-bowl]: fork-right-curve and spoon-upper have 1.268 units of ink clearance over 4.081 units; requires 4; review required | internal-spacing [fork-head / spoon-handle]: fork-right-curve and spoon-handle-2 have 1.673 units of ink clearance over 7.237 units; requires 4; review required
  13. pictographic-primitives/health/heart rate_8a7bb75e-fc55-5c1f-9e7a-6055f25d511f.svg
     icon_id: heart-rate
     current drawing: published/failed/solo48/heart-rate.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [heart / pulse]: point-2 and pulse-4 have 0.663 units of ink clearance over 6.427 units; requires 4; review required
  14. pictographic-primitives/health/heart rate_a954f676-1cce-4e19-81eb-ec067ec52edc.svg
     icon_id: heart-with-pulse-wave-solo
     current drawing: published/failed/solo48/heart-with-pulse-wave-solo.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [outline / pulse]: right-side and pulse-4 have 1.644 units of ink clearance over 7.439 units; requires 4; review required
  15. pictographic-primitives/health/monitor heart beat touch_effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1.svg
     icon_id: monitor-heart-beat-touch
     current drawing: published/failed/solo48/monitor-heart-beat-touch.svg
     violates 2 rules: parallel straight edges under 8, undersized holes
       - parallel straight edges under 8: mic [hand]: parallel straight edges finger and thumb-6, thumb-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [sensor]: parallel straight edges sensor-bottom-right and hand-top are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [hand]: parallel straight edges thumb-4 and thumb-1 are 4.242 apart on centerlines (ink gap 0.242); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
```

### batch-13

```
Run $primitive-make-ray to repair failed icons, batch 13 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/health/monitoring heart beat hand_f238b6ea-82d0-5437-a344-0ec38b16a28d.svg
     icon_id: monitoring-heart-beat-hand
     current drawing: published/failed/solo48/monitoring-heart-beat-hand.svg
     violates 2 rules: parallel straight edges under 8, undersized holes
       - parallel straight edges under 8: mic [hand-inner]: parallel straight edges finger-1, finger-2 and wrist-inner-3 are 4.949 apart on centerlines (ink gap 0.949); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [hand-inner]: parallel straight edges wrist-inner-3 and heart-lower-2 are 6.363 apart on centerlines (ink gap 2.363); requires at least 8 centerline / 4 ink (overlap-fallback)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  2. pictographic-primitives/health/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg
     icon_id: oxygen-tank-timer
     current drawing: published/failed/solo48/oxygen-tank-timer.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [tank]: tank and timer are 5.592 apart on centerlines nearest (20.220, 23.042)<->(25.119, 20.346); (needs 8) | mic [hose]: hose and timer are 0.487 apart on centerlines nearest (24, 13)<->(24.460, 13.158); (needs 8) | mic [timer]: timer and hands are 3.999 apart on centerlines nearest (32.950, 7.000)<->(33, 11); (needs 8)
       - parallel straight edges under 8: mic [valve]: parallel straight edges valve-3 and valve-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [valve-top]: parallel straight edges valve-top-1, valve-top-2 and hose are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [valve-top]: parallel straight edges valve-top-1, valve-top-2 and valve-2 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  3. pictographic-primitives/holidays/snow globe_6c2435e0-bbe9-5122-8cf7-2b3eb32963f3.svg
     icon_id: snow-globe
     current drawing: published/failed/solo48/snow-globe.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [globe / base]: globe-b and base-1 have -3.999 units of ink clearance over 18.5 units; requires 4; review required
  4. pictographic-primitives/holidays/vaisakhi harvest_a0865ae5-c028-46f5-ade5-f26da83b22c2.svg
     icon_id: vaisakhi-harvest
     current drawing: published/failed/solo48/vaisakhi-harvest.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [beater-left]: beater-left and drum are 6 apart on centerlines nearest (16, 12)<->(16, 18); (needs 8) | mic [beater-right]: beater-right and drum are 6 apart on centerlines nearest (26, 12)<->(26, 18); (needs 8) | mic [drum]: drum and hoop-0 are 0.573 apart on centerlines nearest (10.437, 23.891)<->(11, 24); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [grain-high]: parallel straight edges grain-high and grain-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [drum]: parallel straight edges drum-top and hoop-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [hoop-1]: parallel straight edges hoop-1 and drum-bottom are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  5. pictographic-primitives/hotels/room service do not disturb_be992ed2-ade4-5f64-a515-8f186d7ca8e3.svg
     icon_id: room-service-do-not-disturb
     current drawing: published/failed/solo48/room-service-do-not-disturb.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [tag]: hook-return and mouth have 3.523 units of ink clearance over 2.25 units; requires 4; review required
  6. pictographic-primitives/interface-essential/dial finger_ac8740e0-9a7e-4e67-901d-18b0353d7000.svg
     icon_id: dial-finger
     current drawing: published/failed/solo48/dial-finger.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hand]: palm-left and thumb-return have 2.877 units of ink clearance over 4.181 units; requires 4; review required
  7. pictographic-primitives/interface-essential/multiple tags 2_da3a18cb-9766-5ab1-b651-eb447e6f30a2.svg
     icon_id: multiple-tags-2
     current drawing: published/failed/solo48/multiple-tags-2.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [front]: front and hole are 6.485 apart on centerlines nearest (24, 10)<->(28.585, 14.585); (needs 8)
       - parallel straight edges under 8: mic [rear]: parallel straight edges rear-upper-2 and front-right-1, front-right-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap-fallback)
  8. pictographic-primitives/interface-essential/web form progress_93ee9247-04b8-4aa1-b24d-f007fa02d450.svg
     icon_id: web-form-progress
     current drawing: published/failed/solo48/web-form-progress.svg
     violates 1 rule: keyshape bounds
       - keyshape bounds: canvas/keyshape bounds: visible ink (2, 16, 46, 32) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.0, 8.0, 0.0, 8.0], tolerance 0.0)
  9. pictographic-primitives/messages/sign language thank you_98f6fd32-ffa9-4713-85d4-721b3399c95c.svg
     icon_id: sign-language-thank-you
     current drawing: published/failed/solo48/sign-language-thank-you.svg
     violates 3 rules: keyshape bounds, part spacing under 8, undersized holes
       - keyshape bounds: canvas/keyshape bounds: visible ink (3.781, 4, 48, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.218, 0.0, 4.0, 0.0], tolerance 0.0)
       - part spacing under 8: mic [index-side]: index-side and middle-left are 0.196 apart on centerlines nearest (19.807, 15.961)<->(20, 16); (needs 8) | mic [palm]: palm and ring-right are 5 apart on centerlines nearest (36, 31)<->(33, 27); (needs 8) | mic [palm]: palm and little-side are 3.605 apart on centerlines nearest (36, 31)<->(39, 29); (needs 8) (+6 more)
       - undersized holes: holes/pinches: 3 undersized holes; 0 pinches
  10. pictographic-primitives/mobile/force touch press_c167b0e7-d4ac-469d-8f57-09582e267096.svg
     icon_id: force-touch-press
     current drawing: published/failed/solo48/force-touch-press.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [finger]: finger and finger have 1.729 units of ink clearance over 13.703 units; requires 4; review required
  11. pictographic-primitives/mobile/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg
     icon_id: squeeze-sides
     current drawing: published/failed/solo48/squeeze-sides.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [finger-0]: finger-0 and left-arrow are 3.211 apart on centerlines nearest (7.777, 18.674)<->(6, 16); (needs 8) | mic [phone]: phone and right-arrow are 4 apart on centerlines nearest (34, 12)<->(38, 12); (needs 8)
       - parallel straight edges under 8: mic [thumb]: parallel straight edges thumb-2 and phone-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  12. pictographic-primitives/office/co working space plug users_2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4.svg
     icon_id: co-working-space-plug-users
     current drawing: published/failed/solo48/co-working-space-plug-users.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [socket]: socket and socket-hole are 5 apart on centerlines nearest (42, 12)<->(37, 12); (needs 8)
       - parallel straight edges under 8: mic [plug]: parallel straight edges plug-6-1, plug-6-0 and cord-left-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [plug]: parallel straight edges plug-4-0 and cord-left-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [socket]: parallel straight edges socket-4-0 and cord-right-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  13. pictographic-primitives/other/box pen_a89e6154-b80a-49dd-8449-f86a088a5c81.svg
     icon_id: box-pen
     current drawing: published/failed/solo48/box-pen.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [box-edge / rim]: box-edge-2 and rim-1 have 0.028 units of ink clearance over 16.955 units; requires 4; review required | internal-spacing [box-edge / rim]: box-edge-3 and rim-2 have 3.063 units of ink clearance over 4.983 units; requires 4; review required
  14. pictographic-primitives/other/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg
     icon_id: briefcase-dollar
     current drawing: published/failed/solo48/briefcase-dollar.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [dollar]: dollar and dollar have 0.608 units of ink clearance over 3.071 units; requires 4; review required | internal-spacing [dollar]: dollar and dollar have 0.608 units of ink clearance over 3.071 units; requires 4; review required
  15. pictographic-primitives/other/browser dollar sign right_150d4701-3c3f-45a7-a26d-8c580a891da1.svg
     icon_id: browser-dollar-sign-right
     current drawing: published/failed/solo48/browser-dollar-sign-right.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [dollar]: dollar and dollar have 1.626 units of ink clearance over 3.071 units; requires 4; review required | internal-spacing [dollar]: dollar and dollar have 1.626 units of ink clearance over 3.071 units; requires 4; review required
```

### batch-14

```
Run $primitive-make-ray to repair failed icons, batch 14 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg
     icon_id: browser-with-18-plus-text
     current drawing: published/failed/solo48/browser-with-18-plus-text.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [calendar-body]: calendar-body and one are 6 apart on centerlines nearest (6, 26)<->(12, 26); (needs 8) | mic [header]: header and eight-top are 5 apart on centerlines nearest (23, 18)<->(23, 23); (needs 8) | mic [calendar-body]: calendar-body and eight-bottom are 7 apart on centerlines nearest (23, 42)<->(23, 35); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [calendar-body]: parallel straight edges calendar-body-0 and plus-vertical-1, plus-vertical-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  2. pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg
     icon_id: bubble-message-pm-text
     current drawing: published/failed/solo48/bubble-message-pm-text.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [bubble]: bubble and p-stem are 4.963 apart on centerlines nearest (10.498, 31.518)<->(14, 28); (needs 8) | mic [bubble]: bubble and m are 4.905 apart on centerlines nearest (38.902, 30.972)<->(35, 28); (needs 8)
       - parallel straight edges under 8: mic [m]: parallel straight edges m-4 and m-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  3. pictographic-primitives/other/calendar math_14b5dacf-2ae7-4b43-b032-7129b3d49037.svg
     icon_id: calendar-math
     current drawing: published/failed/solo48/calendar-math.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [calendar-body]: calendar-body and one are 5 apart on centerlines nearest (44, 20)<->(39, 20); (needs 8) | mic [two]: two and plus-horizontal are 7.369 apart on centerlines nearest (19.852, 24.203)<->(27, 26); (needs 8) | mic [plus-horizontal]: plus-horizontal and one are 7.211 apart on centerlines nearest (31, 26)<->(37, 22); (needs 8)
       - parallel straight edges under 8: mic [calendar-body]: parallel straight edges calendar-body-0 and one-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  4. pictographic-primitives/other/calendar pie_8c9afa4f-6b92-41b3-8bcd-f538c69afde6.svg
     icon_id: calendar-pie
     current drawing: published/failed/solo48/calendar-pie.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [pie / spoke-diagonal]: pie-br and spoke-diagonal have 2.737 units of ink clearance over 3.997 units; requires 4; review required | internal-spacing [pie / spoke-diagonal]: pie-tl and spoke-diagonal have 2.737 units of ink clearance over 3.997 units; requires 4; review required
  5. pictographic-primitives/other/car flash_3cb36a1f-8edb-4e21-9623-b8c8fac724c3.svg
     icon_id: car-flash
     current drawing: published/failed/solo48/car-flash.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [flash]: flash-1 and flash-3 have -0.170 units of ink clearance over 5.857 units; requires 4; review required
  6. pictographic-primitives/other/gdpr text in rectangle_06655b8e-39ad-4051-aafc-316a27ffb14a.svg
     icon_id: gdpr-text-in-rectangle
     current drawing: published/failed/solo48/gdpr-text-in-rectangle.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [frame]: frame and g are 4 apart on centerlines nearest (4, 21)<->(8, 21); (needs 8) | mic [frame]: frame and r-leg are 3 apart on centerlines nearest (44, 30)<->(41, 30); (needs 8) | mic [g]: g and d-stem are 5 apart on centerlines nearest (13, 19)<->(18, 19); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [d-stem]: parallel straight edges d-stem and g-6 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [g]: parallel straight edges g-6 and g-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [g]: parallel straight edges g-3 and frame-6 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 4 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 2 pinches
  7. pictographic-primitives/other/house lock_a7f1734e-4fae-4c0a-9d33-80bf4a3da78f.svg
     icon_id: house-lock
     current drawing: published/failed/solo48/house-lock.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [lock-body / shackle]: lock-body-2 and shackle-top have 3.389 units of ink clearance over 5.235 units; requires 4; review required
  8. pictographic-primitives/other/house music_3640f2f0-b0c0-4dbd-9d92-86762ff6cfbb.svg
     icon_id: house-music
     current drawing: published/failed/solo48/house-music.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [right-note / beam]: right-note-a and beam-1 have 2.195 units of ink clearance over 3.25 units; requires 4; review required | internal-spacing [right-note / beam]: right-note-a and beam-2 have -0.997 units of ink clearance over 5.5 units; requires 4; review required
  9. pictographic-primitives/other/house phone_7c7ae497-e683-4449-9d47-32e2c0e677e7.svg
     icon_id: house-phone
     current drawing: published/failed/solo48/house-phone.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [house]: house and phone are 6.656 apart on centerlines nearest (14.307, 12.461)<->(18, 18); (needs 8)
       - parallel straight edges under 8: mic [phone]: parallel straight edges end-left-3 and end-left-1 are 4.949 apart on centerlines (ink gap 0.949); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  10. pictographic-primitives/other/house thermometer_c6485cd4-824d-44f8-a250-201a66d4bd70.svg
     icon_id: house-thermometer
     current drawing: published/failed/solo48/house-thermometer.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [thermometer]: thermometer and mercury are 3.682 apart on centerlines nearest (24.905, 33.569)<->(24, 30); (needs 8)
       - parallel straight edges under 8: mic [thermometer]: parallel straight edges tube-right and mercury are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [mercury]: parallel straight edges mercury and tube-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  11. pictographic-primitives/other/house unlock_d9e732b9-6854-4fe7-b39f-365bfd54abee.svg
     icon_id: house-unlock
     current drawing: published/failed/solo48/house-unlock.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [lock-body / open-shackle]: lock-body-2 and shackle-top have 3.349 units of ink clearance over 2.208 units; requires 4; review required
  12. pictographic-primitives/other/house ventilator_adc26099-d55f-405e-935e-9a654dc938e4.svg
     icon_id: house-ventilator
     current drawing: published/failed/solo48/house-ventilator.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [hub / blade-0]: hub-a and blade-0 have 1.504 units of ink clearance over 4.117 units; requires 4; review required | internal-spacing [hub / blade-3]: hub-a and blade-3 have 2.014 units of ink clearance over 2.175 units; requires 4; review required | internal-spacing [hub / blade-1]: hub-b and blade-1 have 2.014 units of ink clearance over 2.175 units; requires 4; review required (+5 more)
  13. pictographic-primitives/other/laptop skull_44a8272b-04c4-4a7c-b200-ee122a35ef32.svg
     icon_id: laptop-skull
     current drawing: published/failed/solo48/laptop-skull.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [screen]: screen and cranium are 4.394 apart on centerlines nearest (24, 8)<->(24, 12.394); (needs 8) | mic [screen]: screen and tooth are 5 apart on centerlines nearest (24, 32)<->(24, 27); (needs 8) | mic [cranium]: cranium and eye-21 are 3.973 apart on centerlines nearest (17.063, 18.463)<->(21, 19); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [jaw-right]: parallel straight edges jaw-right and tooth are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tooth]: parallel straight edges tooth and jaw-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  14. pictographic-primitives/other/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg
     icon_id: laptop-small-squares
     current drawing: published/failed/solo48/laptop-small-squares.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [screen]: screen and tile-0 are 4 apart on centerlines nearest (16, 8)<->(16, 12); (needs 8)
       - parallel straight edges under 8: mic [screen]: parallel straight edges screen-top and tile-0-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tile-0]: parallel straight edges tile-0-3 and tile-1-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  15. pictographic-primitives/other/lock person_ca0b86cd-f823-4251-8d27-7775eddb1f7a.svg
     icon_id: lock-person
     current drawing: published/failed/solo48/lock-person.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
```

### batch-15

```
Run $primitive-make-ray to repair failed icons, batch 15 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/other/Mobile Phone Cube_23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be.svg
     icon_id: mobile-phone-cube
     current drawing: published/failed/solo48/mobile-phone-cube.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [footer]: footer and cube are 7 apart on centerlines nearest (24, 36)<->(24, 29); (needs 8)
       - parallel straight edges under 8: mic [cube]: parallel straight edges cube-2 and cube-front-seam are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cube-front-seam]: parallel straight edges cube-front-seam and cube-5 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cube]: parallel straight edges cube-6 and cube-top-seam-2 are 6.945 apart on centerlines (ink gap 2.945); requires at least 8 centerline / 4 ink (overlap-fallback) (+3 more)
  2. pictographic-primitives/other/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg
     icon_id: mobile-phone-euro-sign
     current drawing: published/failed/solo48/mobile-phone-euro-sign.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [euro-curve / euro-bar]: euro-curve and euro-bar have 1.274 units of ink clearance over 2.715 units; requires 4; review required
  3. pictographic-primitives/other/mobile phone headphone_e65c555e-8915-44b9-98b2-344d81aac941.svg
     icon_id: mobile-phone-headphone
     current drawing: published/failed/solo48/mobile-phone-headphone.svg
     violates 3 rules: parallel straight edges under 8, pinches, undersized holes
       - parallel straight edges under 8: mic [ear-right]: parallel straight edges ear-right-2 and ear-right-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [ear-right]: parallel straight edges ear-right-4 and ear-left-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [ear-left]: parallel straight edges ear-left-2 and ear-left-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  4. pictographic-primitives/other/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg
     icon_id: mobile-phone-lock
     current drawing: published/failed/solo48/mobile-phone-lock.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [lock-body / shackle]: lock-body-0 and shackle-top have 2.522 units of ink clearance over 4.188 units; requires 4; review required
  5. pictographic-primitives/other/mobile phone music note_9541eb00-a034-4794-a052-1575ee33b845.svg
     icon_id: mobile-phone-music-note
     current drawing: published/failed/solo48/mobile-phone-music-note.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [note-head / flag]: note-head-a and flag have 3.150 units of ink clearance over 7.397 units; requires 4; review required
  6. pictographic-primitives/other/mobile phone phone_13ea825f-ae04-4150-a4b6-56b3bed9dc5d.svg
     icon_id: mobile-phone-phone
     current drawing: published/failed/solo48/mobile-phone-phone.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 2 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 1 pinches
  7. pictographic-primitives/other/mobile phone plane_0a850f90-2953-422f-b95d-65062508b5a1.svg
     icon_id: mobile-phone-plane
     current drawing: published/failed/solo48/mobile-phone-plane.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [fuselage / wing]: fuselage and wing have 2.491 units of ink clearance over 2.747 units; requires 4; review required
  8. pictographic-primitives/other/mobile phone pound sign_a70db137-a446-4f4c-b656-4fea14660981.svg
     icon_id: mobile-phone-pound-sign
     current drawing: published/failed/solo48/mobile-phone-pound-sign.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [pound / bar]: pound and bar have 3.402 units of ink clearance over 2.824 units; requires 4; review required
  9. pictographic-primitives/other/mobile phone skull_079086c7-cfbe-4c2b-a1d3-438ec4146466.svg
     icon_id: mobile-phone-skull
     current drawing: published/failed/solo48/mobile-phone-skull.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [separator]: separator and skull are 7 apart on centerlines nearest (20, 36)<->(20, 29); (needs 8) | mic [separator]: separator and jaw-center are 7 apart on centerlines nearest (24, 36)<->(24, 29); (needs 8) | mic [skull]: skull and jaw-center are 4 apart on centerlines nearest (20, 29)<->(24, 29); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [skull]: parallel straight edges jaw-right and jaw-center are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [jaw-center]: parallel straight edges jaw-center and jaw-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 3 undersized holes; 0 pinches
  10. pictographic-primitives/other/mobile phone unlock_b0d42cd4-6acc-4018-ae89-490f3eb333a9.svg
     icon_id: mobile-phone-unlock
     current drawing: published/failed/solo48/mobile-phone-unlock.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [separator]: separator and lock-body are 5 apart on centerlines nearest (28, 36)<->(28, 31); (needs 8)
       - parallel straight edges under 8: mic [lock-body]: parallel straight edges lock-body-4 and separator are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  11. pictographic-primitives/other/module file_e715b082-2f7d-4370-a969-0707c7e743f2.svg
     icon_id: module-file
     current drawing: published/failed/solo48/module-file.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [document]: document and module-1 are 6 apart on centerlines nearest (8, 28)<->(14, 28); (needs 8) | mic [document]: document and module-2 are 4 apart on centerlines nearest (40, 28)<->(36, 28); (needs 8) | mic [module-0]: module-0 and module-1 are 6 apart on centerlines nearest (20, 22)<->(20, 28); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [document]: parallel straight edges document-3 and module-2-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [module-2]: parallel straight edges module-2-4 and module-1-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [module-1]: parallel straight edges module-1-4 and document-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  12. pictographic-primitives/other/money bill pound_a2425a69-d3ed-4c10-8e19-41a99038d49e.svg
     icon_id: money-bill-pound
     current drawing: published/failed/solo48/money-bill-pound.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [note / corner-0]: note-1 and corner-0 have 2.988 units of ink clearance over 3.695 units; requires 4; review required | internal-spacing [note / corner-1]: note-1 and corner-1 have 2.988 units of ink clearance over 3.695 units; requires 4; review required | internal-spacing [note / corner-1]: note-2 and corner-1 have 2.988 units of ink clearance over 3.695 units; requires 4; review required (+5 more)
  13. pictographic-primitives/other/money bill_57a71ef9-0c30-4a25-a290-84a6666d4f6e.svg
     icon_id: money-bill
     current drawing: published/failed/solo48/money-bill.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [note / corner-0]: note-1 and corner-0 have 2.988 units of ink clearance over 3.695 units; requires 4; review required | internal-spacing [note / corner-1]: note-1 and corner-1 have 2.988 units of ink clearance over 3.695 units; requires 4; review required | internal-spacing [note / corner-1]: note-2 and corner-1 have 2.988 units of ink clearance over 3.695 units; requires 4; review required (+5 more)
  14. pictographic-primitives/other/monitor graduation hat_25a4cb19-9e79-49d4-b5af-74c85495cf76.svg
     icon_id: monitor-graduation-hat
     current drawing: published/failed/solo48/monitor-graduation-hat.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [screen]: screen and crown are 6 apart on centerlines nearest (24, 34)<->(24, 28); (needs 8) | mic [mortarboard]: mortarboard and crown are 0.371 apart on centerlines nearest (29.862, 20.655)<->(30, 21); (needs 8)
       - parallel straight edges under 8: mic [mortarboard]: parallel straight edges mortarboard-1 and mortarboard-3 are 7.427 apart on centerlines (ink gap 3.427); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [mortarboard]: parallel straight edges mortarboard-2 and mortarboard-4 are 7.427 apart on centerlines (ink gap 3.427); requires at least 8 centerline / 4 ink (overlap-fallback)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  15. pictographic-primitives/other/monitor laboratory_6ac9826c-356d-4f89-843e-a1caf6908626.svg
     icon_id: monitor-laboratory
     current drawing: published/failed/solo48/monitor-laboratory.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [screen]: screen and flask are 6 apart on centerlines nearest (32, 34)<->(32, 28); (needs 8)
       - parallel straight edges under 8: mic [liquid]: parallel straight edges liquid and flask-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [flask]: parallel straight edges flask-4 and bottom-left, bottom-right are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
```

### batch-16

```
Run $primitive-make-ray to repair failed icons, batch 16 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg
     icon_id: monitor-letters
     current drawing: published/failed/solo48/monitor-letters.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [screen]: screen and a are 6 apart on centerlines nearest (6, 26)<->(12, 26); (needs 8) | mic [screen]: screen and c are 4 apart on centerlines nearest (42, 16)<->(38, 16); (needs 8) | mic [a]: a and b-stem are 4 apart on centerlines nearest (18, 26)<->(22, 26); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [b-top]: parallel straight edges b-top and b-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b-middle]: parallel straight edges b-middle and b-bottom are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 3 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 1 pinches
  2. pictographic-primitives/other/monitor math_6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13.svg
     icon_id: monitor-math
     current drawing: published/failed/solo48/monitor-math.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [screen]: screen and plus-v are 5 apart on centerlines nearest (19, 34)<->(19, 29); (needs 8) | mic [screen]: screen and divide-bar are 7 apart on centerlines nearest (42, 16)<->(35, 16); (needs 8) | mic [screen]: screen and divide-dot-0 are 6 apart on centerlines nearest (31, 6)<->(31, 12); (needs 8) (+2 more)
  3. pictographic-primitives/other/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg
     icon_id: monitor-painting
     current drawing: published/failed/solo48/monitor-painting.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [screen]: screen and palette are 5.192 apart on centerlines nearest (20.449, 34)<->(20.449, 28.807); (needs 8) | mic [screen]: screen and brush-head are 3 apart on centerlines nearest (42, 18)<->(39, 18); (needs 8) | mic [palette]: palette and paint-0 are 3.908 apart on centerlines nearest (17.578, 13.359)<->(19, 17); (needs 8) (+5 more)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  4. pictographic-primitives/other/monitor small squares_1aef3c2a-6d0d-43a2-9616-698d70dc5298.svg
     icon_id: monitor-small-squares
     current drawing: published/failed/solo48/monitor-small-squares.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [screen]: screen and square-0 are 7 apart on centerlines nearest (15, 6)<->(15, 13); (needs 8) | mic [screen]: screen and square-1 are 4 apart on centerlines nearest (23, 34)<->(23, 30); (needs 8) | mic [square-0]: square-0 and square-1 are 5 apart on centerlines nearest (23, 19)<->(23, 24); (needs 8)
       - parallel straight edges under 8: mic [screen]: parallel straight edges screen-0 and square-0-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [square-0]: parallel straight edges square-0-1 and square-0-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [square-0]: parallel straight edges square-0-3 and square-1-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
  5. pictographic-primitives/other/monitor spoon and folk_84f3f807-398a-4f6c-9d2e-58805a5192a4.svg
     icon_id: monitor-spoon-and-folk
     current drawing: published/failed/solo48/monitor-spoon-and-folk.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  6. pictographic-primitives/other/monitor unlock_045a0447-9d31-4ac4-8345-6b457d6d7fdb.svg
     icon_id: monitor-unlock
     current drawing: published/failed/solo48/monitor-unlock.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [screen]: screen and lock are 5 apart on centerlines nearest (24, 34)<->(24, 29); (needs 8)
       - parallel straight edges under 8: mic [lock]: parallel straight edges lock-4 and screen-5, screen-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  7. pictographic-primitives/other/monitor with a_fe4e3f6c-b05b-4d47-b62a-141f6676b4fe.svg
     icon_id: monitor-with-a
     current drawing: published/failed/solo48/monitor-with-a.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  8. pictographic-primitives/other/note dollar sign_d6e3d9b9-b561-4ac3-8008-110d0dfc61d6.svg
     icon_id: note-dollar-sign
     current drawing: published/failed/solo48/note-dollar-sign.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [dollar-s]: dollar-top-bar and dollar-lower have 1.021 units of ink clearance over 3.75 units; requires 4; review required | internal-spacing [dollar-s]: dollar-upper and dollar-bottom-bar have 1.021 units of ink clearance over 3.75 units; requires 4; review required
  9. pictographic-primitives/other/passwords correct_602e570f-55c9-4a0a-85e7-806684d11f77.svg
     icon_id: passwords-correct
     current drawing: published/failed/solo48/passwords-correct.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [field]: field and x-0-0 are 5 apart on centerlines nearest (4, 21)<->(9, 21); (needs 8) | mic [field]: field and x-2-1 are 5 apart on centerlines nearest (44, 27)<->(39, 27); (needs 8) | mic [x-0-1]: x-0-1 and x-1-2 are 6 apart on centerlines nearest (15, 27)<->(21, 27); (needs 8) (+1 more)
  10. pictographic-primitives/other/person magnifying glass_8d4aec38-b440-43a0-b4f2-b3a846ae4cb1.svg
     icon_id: person-magnifying-glass-solo
     current drawing: published/failed/solo48/person-magnifying-glass-solo.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [lens]: lens and person-head are 5.999 apart on centerlines nearest (21.004, 6.000)<->(21, 12); (needs 8) | mic [lens]: lens and body-right are 1.071 apart on centerlines nearest (26.384, 34.999)<->(26, 34); (needs 8)
  11. pictographic-primitives/other/preferences_fea7afa8-61b7-411c-860f-fcb3e2894cf6.svg
     icon_id: preferences
     current drawing: published/failed/solo48/preferences.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [gear / gear-hub]: gear-1 and gear-hub have 3.582 units of ink clearance over 2.182 units; requires 4; review required | internal-spacing [gear / gear-hub]: gear-11 and gear-hub have -0.297 units of ink clearance over 2.667 units; requires 4; review required
  12. pictographic-primitives/other/prescription px square_83ea3f1d-dfb5-4247-948a-2314faaff6ad.svg
     icon_id: prescription-px-square
     current drawing: published/failed/solo48/prescription-px-square.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [rx-up / r-bowl]: rx-up-2 and r-bowl have 0.192 units of ink clearance over 4.673 units; requires 4; review required
  13. pictographic-primitives/other/rectangle buy text_7ecac39c-d98d-4ff3-af33-ae4cbc274cb3.svg
     icon_id: rectangle-buy-text
     current drawing: published/failed/solo48/rectangle-buy-text.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [frame]: frame and b are 7 apart on centerlines nearest (4, 16)<->(11, 16); (needs 8) | mic [frame]: frame and y-top are 3 apart on centerlines nearest (44, 16)<->(41, 16); (needs 8) | mic [b]: b and u are 5 apart on centerlines nearest (17, 20)<->(22, 20); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [frame]: parallel straight edges frame-2 and y-stem are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [u]: parallel straight edges u-right and u-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b]: parallel straight edges b-stem and frame-6 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  14. pictographic-primitives/other/rectangle employee resume 1_bbec6574-bfdd-4612-9ecb-0def3df626fd.svg
     icon_id: rectangle-employee-resume-1
     current drawing: published/failed/solo48/rectangle-employee-resume-1.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [frame]: frame and person-head are 6 apart on centerlines nearest (22, 4)<->(22, 10); (needs 8) | mic [frame]: frame and text1 are 6 apart on centerlines nearest (16, 44)<->(16, 38); (needs 8) | mic [person-shoulders]: person-shoulders and text0 are 6 apart on centerlines nearest (16, 26)<->(16, 32); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [text0]: parallel straight edges text0 and text1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [text1]: parallel straight edges text1 and frame-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  15. pictographic-primitives/other/rectangle employee resume_485264e5-d5d9-4af5-a33a-88ae3ae2126e.svg
     icon_id: rectangle-employee-resume
     current drawing: published/failed/solo48/rectangle-employee-resume.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [frame]: frame and person-head are 6 apart on centerlines nearest (21, 4)<->(21, 10); (needs 8) | mic [frame]: frame and person-shoulders are 7 apart on centerlines nearest (8, 26)<->(15, 26); (needs 8) | mic [frame]: frame and side0 are 5 apart on centerlines nearest (40, 23)<->(35, 23); (needs 8) (+7 more)
       - parallel straight edges under 8: mic [bottom0]: parallel straight edges bottom0 and bottom1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [bottom1]: parallel straight edges bottom1 and frame-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
```

### batch-17

```
Run $primitive-make-ray to repair failed icons, batch 17 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg
     icon_id: rectangle-like-text
     current drawing: published/failed/solo48/rectangle-like-text.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [frame]: frame and l are 6 apart on centerlines nearest (4, 18)<->(10, 18); (needs 8) | mic [frame]: frame and e are 4 apart on centerlines nearest (44, 18)<->(40, 18); (needs 8) | mic [l]: l and i are 5 apart on centerlines nearest (15, 30)<->(20, 30); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [k-stem]: parallel straight edges k-stem and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [l]: parallel straight edges l-1 and frame-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [e]: parallel straight edges e-1 and e-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  2. pictographic-primitives/other/rectangle single man focus_748d6e5f-8942-4061-a602-5b499075202e.svg
     icon_id: rectangle-single-man-focus
     current drawing: published/failed/solo48/rectangle-single-man-focus.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [panel]: panel and focus-tl are 6 apart on centerlines nearest (8, 18)<->(14, 18); (needs 8) | mic [panel]: panel and focus-tr are 6 apart on centerlines nearest (40, 12)<->(34, 12); (needs 8) | mic [panel]: panel and focus-bl are 6 apart on centerlines nearest (8, 30)<->(14, 30); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [panel]: parallel straight edges panel-2 and focus-br-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [panel]: parallel straight edges panel-2 and focus-tr-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [focus-bl]: parallel straight edges focus-bl-1 and panel-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
  3. pictographic-primitives/other/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg
     icon_id: rectangle-sub-text
     current drawing: published/failed/solo48/rectangle-sub-text.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [panel]: panel and s are 5.889 apart on centerlines nearest (4, 18.884)<->(9.889, 18.884); (needs 8) | mic [panel]: panel and b-upper are 4 apart on centerlines nearest (44, 20)<->(40, 20); (needs 8) | mic [s]: s and u are 4.903 apart on centerlines nearest (18.096, 27.901)<->(23, 27.901); (needs 8) (+1 more)
       - parallel straight edges under 8: mic [b-stem]: parallel straight edges b-stem-2, b-stem-1 and u-right are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [u]: parallel straight edges u-right and u-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  4. pictographic-primitives/other/rectangle two persons_d96343a5-e841-44ec-86db-6217d2856341.svg
     icon_id: rectangle-two-persons
     current drawing: published/failed/solo48/rectangle-two-persons.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [panel]: panel and left-head are 7 apart on centerlines nearest (15, 8)<->(15, 15); (needs 8) | mic [panel]: panel and left-shoulders are 4 apart on centerlines nearest (4, 33)<->(8, 33); (needs 8) | mic [panel]: panel and right-head are 7 apart on centerlines nearest (33, 8)<->(33, 15); (needs 8) (+2 more)
  5. pictographic-primitives/other/ribbon 2_0c3535ed-6772-4bdc-aea7-fb01cc99793c.svg
     icon_id: ribbon-2
     current drawing: published/failed/solo48/ribbon-2.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [medal / tail-1]: medal-4 and tail-1-3 have 0.886 units of ink clearance over 4.673 units; requires 4; review required | internal-spacing [medal / tail-0]: medal-5 and tail-0-3 have 0.886 units of ink clearance over 4.673 units; requires 4; review required
  6. pictographic-primitives/other/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg
     icon_id: self-payment-computer-dollar
     current drawing: published/failed/solo48/self-payment-computer-dollar.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  7. pictographic-primitives/other/self payment computer pound_1e1fac7c-54c5-4468-baea-d2c722f0520d.svg
     icon_id: self-payment-computer-pound
     current drawing: published/failed/solo48/self-payment-computer-pound.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [screen]: screen and pound-turn are 5 apart on centerlines nearest (12, 34)<->(12, 29); (needs 8)
       - parallel straight edges under 8: mic [pound-base]: parallel straight edges pound-base-1 and screen-4, screen-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
  8. pictographic-primitives/other/shield 3_500267df-8bce-44e8-a3f7-89f2ab1be4c0.svg
     icon_id: shield-3
     current drawing: published/failed/solo48/shield-3.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [crown / band]: crown-2 and band have 1.277 units of ink clearance over 5.714 units; requires 4; review required | internal-spacing [crown / band]: crown-5 and band have 1.277 units of ink clearance over 5.714 units; requires 4; review required
  9. pictographic-primitives/other/smart watch circle euro sign_73571a2b-4ed5-4ead-96e1-495841cb43da.svg
     icon_id: smart-watch-circle-euro-sign
     current drawing: published/failed/solo48/smart-watch-circle-euro-sign.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [case]: case and euro-bar are 6.999 apart on centerlines nearest (8.000, 23.945)<->(15, 24); (needs 8)
       - undersized holes: holes/pinches: 2 undersized holes; 0 pinches
  10. pictographic-primitives/other/smart watch circle pound sign_f2d45871-ff3d-44d5-84a8-774df3bd6ba3.svg
     icon_id: smartwatch-pound-symbol
     current drawing: published/failed/solo48/smartwatch-pound-symbol.svg
     violates 1 rule: undersized holes
       - undersized holes: holes/pinches: 3 undersized holes; 0 pinches
  11. pictographic-primitives/other/smart watch square dollar sign_22b0de95-e0f5-450b-9f1f-9e0284263be7.svg
     icon_id: smart-watch-square-dollar-sign
     current drawing: published/failed/solo48/smart-watch-square-dollar-sign.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [case]: case and dollar-stem are 6 apart on centerlines nearest (24, 8)<->(24, 14); (needs 8)
       - parallel straight edges under 8: mic [strap-top]: parallel straight edges strap-top-2 and case-0-0, case-0-1, case-0-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [case]: parallel straight edges case-4-2, case-4-1, case-4-0 and strap-bottom-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 4 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 4 undersized holes; 2 pinches
  12. pictographic-primitives/other/smart watch square pound sign_2c0ac7cd-8681-4e21-803e-6437b35eb4a2.svg
     icon_id: smart-watch-square-pound-sign
     current drawing: published/failed/solo48/smart-watch-square-pound-sign.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [case]: case and pound-hook are 6 apart on centerlines nearest (25, 8)<->(25, 14); (needs 8)
       - parallel straight edges under 8: mic [strap-top]: parallel straight edges strap-top-2 and case-0-0, case-0-1, case-0-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [case]: parallel straight edges case-4-2, case-4-1, case-4-0 and strap-bottom-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  13. pictographic-primitives/other/spoon and fork_dd96595d-042a-465f-9681-d8c23c641754.svg
     icon_id: spoon-and-fork
     current drawing: published/failed/solo48/spoon-and-fork.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [fork / center-tine]: bowl and center-tine have 2.968 units of ink clearance over 3.732 units; requires 4; review required
  14. pictographic-primitives/other/square bubble user_262dd529-82e6-4744-ac57-ec46c428f624.svg
     icon_id: square-bubble-user
     current drawing: published/failed/solo48/square-bubble-user.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [bubble]: bubble and head are 7 apart on centerlines nearest (24, 6)<->(24, 13); (needs 8) | mic [bubble]: bubble and shoulders are 3 apart on centerlines nearest (32, 36)<->(32, 33); (needs 8)
  15. pictographic-primitives/other/square megaphone_84596dd2-069a-450e-b70c-08a8dc22159b.svg
     icon_id: square-megaphone
     current drawing: published/failed/solo48/square-megaphone.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [frame]: frame and grip are 4.167 apart on centerlines nearest (26.747, 42)<->(26.747, 37.832); (needs 8)
```

### batch-18

```
Run $primitive-make-ray to repair failed icons, batch 18 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/other/suitcase pill_4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa.svg
     icon_id: suitcase-pill
     current drawing: published/failed/solo48/suitcase-pill.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [case]: case and pill are 5.680 apart on centerlines nearest (25.987, 14)<->(25.987, 19.681); (needs 8)
  2. pictographic-primitives/other/test file_f799a4bf-12e6-4111-a7f7-3023b0c48446.svg
     icon_id: test-file
     current drawing: published/failed/solo48/test-file.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [page]: page and b are 6 apart on centerlines nearest (16, 44)<->(16, 38); (needs 8) | mic [page]: page and answer-0 are 6 apart on centerlines nearest (40, 22)<->(34, 22); (needs 8) | mic [page]: page and answer-1 are 6 apart on centerlines nearest (40, 35)<->(34, 35); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [b]: parallel straight edges b-2 and b-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b]: parallel straight edges b-2 and b-lower-0 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b]: parallel straight edges b-4 and b-lower-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
       - pinches: holes/pinches: 3 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 1 pinches
  3. pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg
     icon_id: tv-circle-check
     current drawing: published/failed/solo48/tv-circle-check.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [screen]: screen and status-ring are 6 apart on centerlines nearest (24, 6)<->(24, 12); (needs 8) | mic [status-ring]: status-ring and check are 2.999 apart on centerlines nearest (30.387, 15.183)<->(28, 17); (needs 8)
  4. pictographic-primitives/other/tv password_2cc3609a-d235-46f7-828b-ef134a6021e2.svg
     icon_id: tv-password
     current drawing: published/failed/solo48/tv-password.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [screen]: screen and password-0-0 are 7 apart on centerlines nearest (6, 21)<->(13, 21); (needs 8) | mic [screen]: screen and password-2-1 are 7 apart on centerlines nearest (42, 25)<->(35, 25); (needs 8) | mic [password-0-1]: password-0-1 and password-1-3 are 5 apart on centerlines nearest (17, 25)<->(22, 25); (needs 8) (+1 more)
  5. pictographic-primitives/other/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg
     icon_id: ui-webpage-ad-text
     current drawing: published/failed/solo48/ui-webpage-ad-text.svg
     violates 3 rules: part spacing under 8, pinches, undersized holes
       - part spacing under 8: mic [browser]: browser and d-bowl are 6 apart on centerlines nearest (42, 28)<->(36, 28); (needs 8)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  6. pictographic-primitives/other/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg
     icon_id: ui-webpage-skull
     current drawing: published/failed/solo48/ui-webpage-skull.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [browser]: browser and skull are 5 apart on centerlines nearest (20, 42)<->(20, 37); (needs 8) | mic [browser]: browser and middle-tooth are 5 apart on centerlines nearest (24, 42)<->(24, 37); (needs 8) | mic [skull]: skull and eye-21 are 4.999 apart on centerlines nearest (16.001, 28.078)<->(21, 28); (needs 8) (+5 more)
       - parallel straight edges under 8: mic [skull]: parallel straight edges jaw-right and middle-tooth are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [middle-tooth]: parallel straight edges middle-tooth and jaw-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  7. pictographic-primitives/other/ui webpage t shirt_6fd53a7d-aab1-479b-9e12-e2f8acddcfb2.svg
     icon_id: ui-webpage-t-shirt
     current drawing: published/failed/solo48/ui-webpage-t-shirt.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [shirt]: shirt-left-2 and shirt-left-4 have -0.273 units of ink clearance over 2.705 units; requires 4; review required | internal-spacing [shirt]: shirt-left-3 and neckline have 3.708 units of ink clearance over 2.644 units; requires 4; review required | internal-spacing [shirt]: shirt-left-8 and shirt-left-10 have -0.273 units of ink clearance over 2.705 units; requires 4; review required (+1 more)
  8. pictographic-primitives/other/woman nude_f11ccece-81b6-415d-a20a-a1bdd3fceb3c.svg
     icon_id: woman-nude
     current drawing: published/failed/solo48/woman-nude.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [torso--1]: torso--1 and nipple-0 are 4.987 apart on centerlines nearest (15.636, 23.416)<->(20, 21); (needs 8) | mic [torso-1]: torso-1 and nipple-1 are 4.987 apart on centerlines nearest (32.363, 23.416)<->(28, 21); (needs 8) | mic [chest]: chest and navel are 5.559 apart on centerlines nearest (22.269, 25.716)<->(24, 31); (needs 8)
  9. pictographic-primitives/outdoors/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg
     icon_id: outdoors-pig-apple
     current drawing: published/failed/solo48/outdoors-pig-apple.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [panel]: panel and apple are 3.806 apart on centerlines nearest (22, 23.269)<->(25.806, 23.269); (needs 8)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  10. pictographic-primitives/payments/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg
     icon_id: credit-card-payment
     current drawing: published/failed/solo48/credit-card-payment.svg
     violates 3 rules: parallel straight edges under 8, pinches, undersized holes
       - parallel straight edges under 8: mic [card]: parallel straight edges card-2-0 and stripe are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [stripe]: parallel straight edges stripe and card-6-0 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [terminal]: parallel straight edges terminal-2-0, terminal-2-1 and receipt-5, receipt-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) (+1 more)
       - pinches: holes/pinches: 3 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 2 pinches
  11. pictographic-primitives/programing/amazon web service sagemaker_f2265828-4def-5cb0-be87-edeb3a4d341e.svg
     icon_id: atom-three-orbits-reference
     current drawing: published/failed/solo48/atom-three-orbits-reference.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 6 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 6 undersized holes; 2 pinches
  12. pictographic-primitives/programing/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg
     icon_id: data-lake-code
     current drawing: published/failed/solo48/data-lake-code.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [digit-0-0]: digit-0-0 and digit-0-1 are 4 apart on centerlines nearest (6, 10)<->(10, 10); (needs 8) | mic [digit-0-0]: digit-0-0 and digit-1-0 are 6.526 apart on centerlines nearest (6, 14)<->(8.199, 20.144); (needs 8) | mic [digit-0-1]: digit-0-1 and digit-0-2 are 4 apart on centerlines nearest (16, 10)<->(20, 10); (needs 8) (+18 more)
       - parallel straight edges under 8: mic [digit-1-2]: parallel straight edges digit-1-2 and digit-1-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  13. pictographic-primitives/rating/rating star three_cf0d9970-8b38-5723-b109-a3be9696acdb.svg
     icon_id: rating-star-three;three-star-rating-row;three-star-rating-row-v2;three-star-rating-row-v3
     current drawing: published/failed/solo48/rating-star-three.svg
     violates 4 rules: keyshape bounds, part spacing under 8, pinches, undersized holes
       - keyshape bounds: canvas/keyshape bounds: visible ink (2, 15, 46, 33) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.0, 7.0, 0.0, 7.0], tolerance 0.0)
       - part spacing under 8: mic [star-0]: star-0 and star-1 are 2 apart on centerlines nearest (16, 20)<->(18, 20); (needs 8) | mic [star-1]: star-1 and star-2 are 2 apart on centerlines nearest (30, 20)<->(32, 20); (needs 8) | mic [star-0]: star-0 and star-1 are 2 apart on centerlines nearest (16, 22)<->(18, 22); (needs 8) (+1 more)
       - pinches: holes/pinches: 3 undersized holes; 3 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 0 pinches | holes/pinches: 3 undersized holes; 3 pinches
  14. pictographic-primitives/romance/wedding celebration_c0ea9f23-ec77-44d1-920d-71fcc67e252e.svg
     icon_id: wedding-celebration
     current drawing: published/failed/solo48/wedding-celebration.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 3 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 3 undersized holes; 1 pinches
  15. pictographic-primitives/sports/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg
     icon_id: scoreboard
     current drawing: published/failed/solo48/scoreboard.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [hanger-0]: hanger-0 and two-top are 4.544 apart on centerlines nearest (13, 17)<->(14.583, 21.259); (needs 8) | mic [hanger-1]: hanger-1 and zero are 4 apart on centerlines nearest (35, 17)<->(35, 21); (needs 8) | mic [two-top]: two-top and colon-0 are 5.055 apart on centerlines nearest (19.975, 24.557)<->(25, 24); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [panel]: parallel straight edges panel-2 and zero-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [two-bottom]: parallel straight edges two-bottom-2 and panel-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
```

### batch-19

```
Run $primitive-make-ray to repair failed icons, batch 19 of 20. Redraw each of these 15 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/sports/scoreboard_26cfbb23-55d5-4b36-b8ee-026317013752.svg
     icon_id: scoreboard-26cfbb23
     current drawing: published/failed/solo48/scoreboard-26cfbb23.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [panel]: panel and two-top are 6 apart on centerlines nearest (6, 18)<->(12, 18); (needs 8) | mic [panel]: panel and colon-1 are 7 apart on centerlines nearest (25, 32)<->(25, 25); (needs 8) | mic [panel]: panel and zero are 3 apart on centerlines nearest (42, 18)<->(39, 18); (needs 8) (+4 more)
       - parallel straight edges under 8: mic [panel]: parallel straight edges panel-2 and zero-2 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [two-bottom]: parallel straight edges two-bottom-2 and panel-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  2. pictographic-primitives/sports/shooting rifle aim_4ed91cc5-870d-4844-a54d-8cf25bededb3.svg
     icon_id: shooting-rifle-aim
     current drawing: published/failed/solo48/shooting-rifle-aim.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [trigger]: trigger and sight-bottom are 3.830 apart on centerlines nearest (22.028, 29.715)<->(24, 33); (needs 8)
       - parallel straight edges under 8: mic [rifle]: parallel straight edges rifle-1 and stock-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 4 undersized holes; 0 pinches
  3. pictographic-primitives/sports/tournament bracket_6d731820-468b-5c38-b10b-859f24a8eab3.svg
     icon_id: tournament-bracket
     current drawing: published/failed/solo48/tournament-bracket.svg
     violates 1 rule: parallel straight edges under 8
       - parallel straight edges under 8: mic [bracket]: parallel straight edges bracket-2, bracket-3 and node-left-0, node-left-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [bracket]: parallel straight edges bracket-2, bracket-3 and node-right-0, node-right-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal)
  4. pictographic-primitives/technology/head lock content movement_f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6.svg
     icon_id: head-lock-content-movement
     current drawing: published/failed/solo48/head-lock-content-movement.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [content]: content and ray-left are 4.242 apart on centerlines nearest (14, 14)<->(11, 11); (needs 8) | mic [content]: content and ray-right are 4.242 apart on centerlines nearest (19, 21)<->(22, 24); (needs 8) | mic [content]: content and turn are 2.828 apart on centerlines nearest (28, 12)<->(30, 10); (needs 8) (+2 more)
  5. pictographic-primitives/technology/network 5g_9dc361bf-d268-4878-852c-ebdc9f66c69b.svg
     icon_id: network-5g
     current drawing: published/failed/solo48/network-5g.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [bottom--1]: bottom--1 and five-bowl are 7.464 apart on centerlines nearest (18, 38)<->(16.937, 30.611); (needs 8) | mic [tick--1-16]: tick--1-16 and five-top are 2.828 apart on centerlines nearest (10, 16)<->(12, 18); (needs 8) | mic [tick--1-32]: tick--1-32 and five-bowl are 2.828 apart on centerlines nearest (10, 32)<->(12, 30); (needs 8) (+4 more)
  6. pictographic-primitives/transportation/automatic drive gear_f89489d3-928e-4d8e-8a13-9ff760315c90.svg
     icon_id: automatic-drive-gear
     current drawing: published/failed/solo48/automatic-drive-gear.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [letter-a]: letter-a and letter-u are 5.475 apart on centerlines nearest (11.623, 35.361)<->(17.043, 34.586); (needs 8) | mic [letter-u]: letter-u and t-bar are 3 apart on centerlines nearest (25, 10)<->(28, 10); (needs 8) | mic [t-bar]: t-bar and letter-o are 2.830 apart on centerlines nearest (36, 10)<->(38.426, 11.457); (needs 8)
       - parallel straight edges under 8: mic [letter-o]: parallel straight edges letter-o-2 and letter-o-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [letter-o]: parallel straight edges letter-o-6 and t-stem are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [t-stem]: parallel straight edges t-stem and u-right are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  7. pictographic-primitives/transportation/four wheel drive_1dfab6f7-a053-5aee-8d2b-b99c63e6f3df.svg
     icon_id: four-wheel-drive
     current drawing: published/failed/solo48/four-wheel-drive.svg
     violates 2 rules: pinches, undersized holes
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  8. pictographic-primitives/transportation/kiss and ride_b90f680f-f022-4110-b907-97ad0bbc7f46.svg
     icon_id: kiss-and-ride
     current drawing: published/failed/solo48/kiss-and-ride.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [r-stem / r-leg]: r-stem-1 and r-leg have 0.277 units of ink clearance over 8.447 units; requires 4; review required
  9. pictographic-primitives/transportation/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg
     icon_id: parkig-aid-system
     current drawing: published/failed/solo48/parkig-aid-system.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [wave-outer]: wave-outer and obstacle are 2.493 apart on centerlines nearest (31.385, 25.652)<->(33.615, 26.768); (needs 8)
  10. pictographic-primitives/transportation/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg
     icon_id: road-sign-4m-high
     current drawing: published/failed/solo48/road-sign-4m-high.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [four-bar]: four-bar and m are 6 apart on centerlines nearest (22, 28)<->(28, 28); (needs 8) | mic [four]: four and up are 4.472 apart on centerlines nearest (18, 14)<->(20, 10); (needs 8) | mic [four]: four and down are 4.472 apart on centerlines nearest (18, 34)<->(20, 38); (needs 8) (+2 more)
  11. pictographic-primitives/travel/transit no entering stop_688256eb-e269-4b62-9dcc-ecccc8d9b352.svg
     icon_id: transit-no-entering-stop
     current drawing: published/failed/solo48/transit-no-entering-stop.svg
     violates 1 rule: part spacing under 8
       - part spacing under 8: mic [start]: start and dash-top are 7 apart on centerlines nearest (14, 10)<->(21, 10); (needs 8) | mic [right-turn]: right-turn and dash-top are 4 apart on centerlines nearest (28, 10)<->(24, 10); (needs 8) | mic [right-turn]: right-turn and stop-1 are 7.071 apart on centerlines nearest (34, 26)<->(27, 27); (needs 8) (+2 more)
  12. pictographic-primitives/users/user experience design_0bed2a31-9297-4a65-99ad-c1ed293776b1.svg
     icon_id: user-centered-shape-diagram;user-centered-shape-diagram-v2;user-centered-shape-diagram-v3
     current drawing: published/failed/solo48/user-centered-shape-diagram.svg
     violates 2 rules: part spacing under 8, undersized holes
       - part spacing under 8: mic [square]: square and head are 7 apart on centerlines nearest (24, 14)<->(24, 21); (needs 8) | mic [circle]: circle and shoulders are 4.318 apart on centerlines nearest (13.920, 36.791)<->(18.145, 37.685); (needs 8) | mic [circle]: circle and orbit-left are 7.704 apart on centerlines nearest (8.652, 32.233)<->(6, 25); (needs 8) (+11 more)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches | holes/pinches: 1 undersized holes; 0 pinches | holes/pinches: 1 undersized holes; 0 pinches
  13. pictographic-primitives/video-games/batch-04/game bundle package 2 game game bundle package_11e6c80b-9352-46d6-afbf-71492aac441e.svg
     icon_id: game-bundle-package-2-game-game-bundle-package
     current drawing: published/failed/solo48/game-bundle-package-2-game-game-bundle-package.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [controller]: controller-2 and controller-4 have 2.091 units of ink clearance over 3.710 units; requires 4; review required | internal-spacing [controller]: controller-6 and controller-8 have 2.091 units of ink clearance over 3.710 units; requires 4; review required
  14. pictographic-primitives/video-games/batch-12/war banner guild faction_c0fef2f7-6c93-5a77-973b-346d07d1e626.svg
     icon_id: war-banner-guild-faction
     current drawing: published/failed/solo48/war-banner-guild-faction.svg
     violates 1 rule: internal ink clearance under 4
       - internal ink clearance under 4: internal-spacing [finial / banner]: finial-1 and banner-1 have 2.195 units of ink clearance over 3.25 units; requires 4; review required
  15. pictographic-primitives/video/amazon web service interactive video service_676befa5-604d-5f0a-9344-ef3dfc7baea7.svg
     icon_id: triangular-video-emblem
     current drawing: published/failed/solo48/triangular-video-emblem.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [diagonal-a]: diagonal-a and triangle-1 are 4.437 apart on centerlines nearest (25.538, 21.692)<->(28, 18); (needs 8) | mic [triangle-3]: triangle-3 and triangle-5 are 5.487 apart on centerlines nearest (32, 26)<->(29.176, 30.705); (needs 8) | mic [diagonal-b]: diagonal-b and triangle-4 are 2.529 apart on centerlines nearest (20.8, 27.6)<->(20, 30); (needs 8)
       - parallel straight edges under 8: mic [triangle-2]: parallel straight edges triangle-2-2 and triangle-4-1 are 5.487 apart on centerlines (ink gap 1.487); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [triangle-3]: parallel straight edges triangle-3-2 and triangle-5-1 are 5.487 apart on centerlines (ink gap 1.487); requires at least 8 centerline / 4 ink (midpoint-normal)
```

### batch-20

```
Run $primitive-make-ray to repair failed icons, batch 20 of 20. Redraw each of these 4 reference files in order.
  Every file below was already drawn (a registered model and/or an earlier primitive-make-ray run), and that drawing FAILED the build. It shows as "Drawn, unpublished" on gallery/primitives.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Each file lists its icon id and EVERY build rule its current drawing violates, with the errors. Fix all of the listed rules for that file, not just the first; a file passes only when none remain.
  How to fix each rule that appears in this batch:
    - Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
    - Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
    - Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
    - Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  Files:
  1. pictographic-primitives/war/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg
     icon_id: death-rip
     current drawing: published/failed/solo48/death-rip.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [stone]: stone and r-stem are 6 apart on centerlines nearest (10, 29)<->(16, 29); (needs 8) | mic [stone]: stone and p-bowl are 3 apart on centerlines nearest (38, 22)<->(35, 22); (needs 8) | mic [plinth]: plinth and i are 7 apart on centerlines nearest (25, 36)<->(25, 29); (needs 8) (+2 more)
       - parallel straight edges under 8: mic [stone]: parallel straight edges stone-right and p-stem-2, p-stem-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [p-stem]: parallel straight edges p-stem-2, p-stem-1 and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [r-stem]: parallel straight edges r-stem-2, r-stem-1 and stone-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 2 undersized holes; 2 pinches
       - undersized holes: holes/pinches: 2 undersized holes; 2 pinches
  2. pictographic-primitives/war/tools tear gas_8f58894e-3584-4d7e-9183-ffe9e81333d8.svg
     icon_id: tools-tear-gas
     current drawing: published/failed/solo48/tools-tear-gas.svg
     violates 4 rules: part spacing under 8, parallel straight edges under 8, pinches, undersized holes
       - part spacing under 8: mic [eye-upper]: eye-upper and pupil are 3.938 apart on centerlines nearest (15.031, 6.129)<->(15.559, 10.032); (needs 8) | mic [eye-lower]: eye-lower and tear are 4.631 apart on centerlines nearest (18, 22)<->(13.887, 24.131); (needs 8) | mic [eye-lower]: eye-lower and gas are 1.342 apart on centerlines nearest (27.909, 14.220)<->(29.152, 14.728); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [nozzle]: parallel straight edges nozzle-2 and canister-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [nozzle]: parallel straight edges nozzle-1 and nozzle-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - pinches: holes/pinches: 1 undersized holes; 1 pinches
       - undersized holes: holes/pinches: 1 undersized holes; 1 pinches
  3. pictographic-primitives/weather/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg
     icon_id: east
     current drawing: published/failed/solo48/east.svg
     violates 3 rules: part spacing under 8, parallel straight edges under 8, undersized holes
       - part spacing under 8: mic [rim]: rim and needle are 5.514 apart on centerlines nearest (33.923, 8.124)<->(30, 12); (needs 8) | mic [rim]: rim and letter-e are 4 apart on centerlines nearest (24, 32)<->(24, 36); (needs 8)
       - parallel straight edges under 8: mic [letter-e]: parallel straight edges letter-e-1 and e-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [e-middle]: parallel straight edges e-middle and letter-e-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
       - undersized holes: holes/pinches: 1 undersized holes; 0 pinches
  4. pictographic-primitives/weather/visibility_c9a32a88-1037-4cb5-8b11-265935d5449f.svg
     icon_id: visibility
     current drawing: published/failed/solo48/visibility.svg
     violates 2 rules: part spacing under 8, parallel straight edges under 8
       - part spacing under 8: mic [triangle]: triangle and dash-0 are 6 apart on centerlines nearest (18, 16)<->(24, 16); (needs 8) | mic [triangle]: triangle and one are 4.472 apart on centerlines nearest (18, 30)<->(20, 34); (needs 8) | mic [dash-0]: dash-0 and dash-1 are 6 apart on centerlines nearest (28, 16)<->(34, 16); (needs 8) (+3 more)
       - parallel straight edges under 8: mic [zero-1]: parallel straight edges zero-1-1 and zero-1-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [zero-1]: parallel straight edges zero-1-4 and zero-0-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [zero-0]: parallel straight edges zero-0-1 and zero-0-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
```
