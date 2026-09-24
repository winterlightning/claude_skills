# Tasks — claude_skills

<!--
Synced with the TodoPusher app. Edit freely (agents: add tasks for this
project here):
- Add a task: a "- [ ]" line under a section holding the prompt sent to
  the agent; indented lines below it continue the prompt.
- Check "[x]" to mark done; move a line between sections to change status.
- Don't edit or invent (tp:xxxxxxxx) tags — the app assigns them.
-->

## Queued


## Backlog

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 5 of 11. Redraw each of these 15 reference files in order. (tp:d048e486)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_34/shoemaker_4a1b8b06-db68-40b2-adfe-7ecac75aaa72.svg
    failed: mic [shoulder-right]: shoulder-right and shoe are 1.14414 apart on centerlines nearest (34, 34)<->(34.0407, 35.1434) (needs 8) | mic [apron]: apron and shoe are 1 apart on centerlines nearest (22, 42)<->(23, 42) (needs 8)
    current drawing: published/failed/solo48/shoemaker.svg
  pictographic-primitives/_uncategorized_34/shopping basket rating_21ed6f6c-e1f2-48f6-9bc3-1792c8f73f0d.svg
    failed: mic [left]: left and center are 4.12311 apart on centerlines nearest (16, 15)<->(20, 16) (needs 8) | mic [left]: left and left-handle are 4.4376 apart on centerlines nearest (15, 21)<->(18.6923, 23.4615) (needs 8) (+6 more)
    also: undersized holes
    current drawing: published/failed/solo48/shopping-basket-rating.svg
  pictographic-primitives/_uncategorized_34/signal slash_945b25be-2ad9-4b54-9548-b41ff357244a.svg
    failed: mic [ring]: ring and wave-top are 5.63054 apart on centerlines nearest (41.4701, 19.6654)<->(36, 21) (needs 8) | mic [ring]: ring and dot are 4.99991 apart on centerlines nearest (23.9693, 41.9998)<->(24, 37) (needs 8) (+3 more)
    current drawing: published/failed/solo48/signal-slash.svg
  pictographic-primitives/_uncategorized_34/smart house open_cd72149b-476c-4b5b-a1fd-e19535644748.svg
    failed: mic [wifi-inner]: wifi-inner and roof are 5.99993 apart on centerlines nearest (23.9705, 14.0001)<->(24, 20) (needs 8) | mic [roof]: roof and walls are 2.75599 apart on centerlines nearest (8.53933, 29.6629)<->(10, 32) (needs 8) (+2 more)
    current drawing: published/failed/solo48/smart-house-open.svg
  pictographic-primitives/_uncategorized_34/smiley bright_d25557be-d198-406c-ac40-686ab3f61c2a.svg
    failed: mic [face]: face and eye-16 are 7.46969 apart on centerlines nearest (6.43405, 14.4385)<->(13, 18) (needs 8) | mic [face]: face and eye-32 are 7.46969 apart on centerlines nearest (41.566, 14.4385)<->(35, 18) (needs 8) (+1 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/sparkle-eyed-face-with-uneven-smile.svg
  pictographic-primitives/_uncategorized_34/smiley decode_2421c5d7-2ff1-480c-8526-9252cbdd43cf.svg
    failed: mic [dome]: dome and eye-left are 7.70406 apart on centerlines nearest (15.2439, 8.27363)<->(19, 15) (needs 8) | mic [dome]: dome and eye-right are 7.70406 apart on centerlines nearest (32.7561, 8.27363)<->(29, 15) (needs 8)
    current drawing: published/failed/solo48/angry-face-with-broad-mouth-cover.svg
  pictographic-primitives/_uncategorized_34/smiley shine big eyes_58fdbda2-95d4-42f4-b93e-df89f627bc82.svg
    failed: mic [face]: face and eye-16 are 7.46969 apart on centerlines nearest (6.43405, 14.4385)<->(13, 18) (needs 8) | mic [face]: face and eye-32 are 7.46969 apart on centerlines nearest (41.566, 14.4385)<->(35, 18) (needs 8) (+1 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/large-sparkle-eyed-smiling-face.svg
  pictographic-primitives/_uncategorized_35/south west_00066094-2048-4259-bd02-411ee5eca13f.svg
    failed: mic [dial]: dial and s are 3.19887 apart on centerlines nearest (19.1679, 35.2529)<->(18.1879, 38.2979) (needs 8) | mic [dial]: dial and w are 2.02806 apart on centerlines nearest (24.8881, 35.975)<->(25, 38) (needs 8) (+5 more)
    also: undersized holes
    current drawing: published/failed/solo48/south-west.svg
  pictographic-primitives/_uncategorized_35/square code_bace2392-58d6-42ff-85cc-dedbb5e924c6.svg
    failed: mic [chevron-0]: chevron-0 and slash are 2.84605 apart on centerlines nearest (19, 30)<->(21.7, 30.9) (needs 8) | mic [chevron-1]: chevron-1 and slash are 2.84605 apart on centerlines nearest (29, 18)<->(26.3, 17.1) (needs 8)
    current drawing: published/failed/solo48/square-code-solo.svg
  pictographic-primitives/_uncategorized_35/square dashed circle plus_b67f4e19-f005-4972-8fd5-b3a7a1f67e76.svg
    failed: mic [dash-0]: dash-0 and dash-1 are 3.60555 apart on centerlines nearest (27, 14)<->(30, 16) (needs 8) | mic [dash-0]: dash-0 and dash-7 are 3.60555 apart on centerlines nearest (21, 14)<->(18, 16) (needs 8) (+14 more)
    current drawing: published/failed/solo48/square-dashed-circle-plus.svg
  pictographic-primitives/_uncategorized_36/square user_55360bd5-b0c0-48c8-b255-4f7c05d395d6.svg
    failed: mic [frame]: frame and head are 8 apart on centerlines nearest (24, 6)<->(24, 14) (needs 8) | mic [frame]: frame and body are 8 apart on centerlines nearest (15, 42)<->(15, 34) (needs 8)
    current drawing: published/failed/solo48/square-user.svg
  pictographic-primitives/_uncategorized_36/start your machine learning journey_ef84068a-8813-43c3-b7d5-546375fbf309.svg
    failed: mic [map]: map and root are 3.05584 apart on centerlines nearest (22, 20)<->(22.3368, 23.0372) (needs 8) | mic [map]: map and upper-link are 7.07107 apart on centerlines nearest (22, 20)<->(27, 25) (needs 8) (+9 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/start-your-machine-learning-journey.svg
  pictographic-primitives/_uncategorized_36/step sister_073b7984-a3fe-4699-87e9-47bf76004f1c.svg
    failed: mic [head]: head and hair-left are 0.187976 apart on centerlines nearest (12.1082, 14.5327)<->(11.9224, 14.5041) (needs 8) | mic [head]: head and hair-right are 0.187976 apart on centerlines nearest (31.8918, 14.5327)<->(32.0776, 14.5041) (needs 8) (+7 more)
    also: undersized holes
    current drawing: published/failed/solo48/step-sister.svg
  pictographic-primitives/_uncategorized_36/stepdaughter_7bead6c0-72f2-44e3-81e8-617544d2ab4d.svg
    failed: mic [head]: head and hair-left are 0.187976 apart on centerlines nearest (12.1082, 14.5327)<->(11.9224, 14.5041) (needs 8) | mic [head]: head and hair-right are 0.187976 apart on centerlines nearest (31.8918, 14.5327)<->(32.0776, 14.5041) (needs 8) (+7 more)
    also: undersized holes
    current drawing: published/failed/solo48/stepdaughter.svg
  pictographic-primitives/_uncategorized_37/tea cup herbal_fd3519ca-61c2-4e48-a98b-ef47a0103f4c.svg
    failed: mic [cup]: cup and leaf-stem are 0.524435 apart on centerlines nearest (10.6041, 33.344)<->(11, 33) (needs 8)
    current drawing: published/failed/solo48/tea-cup-herbal.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 6 of 11. Redraw each of these 15 reference files in order. (tp:7a5a0757)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_37/technology ar searching finger touch_505403c5-6a6b-4a09-8ee4-eac7ce3a505f.svg
    failed: mic [cube-bottom]: cube-bottom and hand are 1.50722 apart on centerlines nearest (19.0582, 29.4709)<->(19.7323, 30.819) (needs 8)
    current drawing: published/failed/solo48/technology-ar-searching-finger-touch.svg
  pictographic-primitives/_uncategorized_37/text options_f3c9dbea-9e4f-4e89-b366-3b67f9116e34.svg
    failed: mic [dropdown]: dropdown and chevron are 3 apart on centerlines nearest (32, 34)<->(32, 37) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/text-options.svg
  pictographic-primitives/_uncategorized_38/tire pressure warning_992df6cb-53a3-42d8-b584-7ec4584f57b0.svg
    failed: mic [tire]: tire and warning are 4.02954 apart on centerlines nearest (28.024, 14.7881)<->(24, 15) (needs 8)
    current drawing: published/failed/solo48/tire-pressure-warning.svg
  pictographic-primitives/_uncategorized_38/tour_486721e9-ba81-4dfa-9797-b5882d2c9ef1.svg
    failed: mic [pin]: pin and pin-hole are 5.99955 apart on centerlines nearest (33.7083, 8.39584)<->(29.4142, 12.5858) (needs 8)
    current drawing: published/failed/solo48/tour.svg
  pictographic-primitives/_uncategorized_38/transporter 2_a94a77f8-560c-43b1-83e5-a5b781212a50.svg
    failed: mic [door]: door and up-head are 4 apart on centerlines nearest (30, 10)<->(34, 10) (needs 8) | mic [door]: door and down-head are 4 apart on centerlines nearest (30, 38)<->(34, 38) (needs 8)
    current drawing: published/failed/solo48/transporter-2.svg
  pictographic-primitives/_uncategorized_38/trash clock_b4bf811c-cc24-4d58-a27f-2cf37289678d.svg
    failed: mic [lid]: lid and clock are 4 apart on centerlines nearest (24, 20)<->(24, 24) (needs 8) | mic [lid]: lid and hands are 7 apart on centerlines nearest (24, 20)<->(24, 27) (needs 8) (+1 more)
    current drawing: published/failed/solo48/trash-clock.svg
  pictographic-primitives/_uncategorized_38/trash plus_38a24b73-5041-4ea2-83f6-2bbac1782a14.svg
    failed: mic [lid]: lid and plus-2 are 8 apart on centerlines nearest (24, 20)<->(24, 28) (needs 8)
    current drawing: published/failed/solo48/trash-plus.svg
  pictographic-primitives/_uncategorized_38/triangle exclamation_3ed0411c-4d4d-4b46-9ef9-41c8004000c9.svg
    failed: mic [triangle]: triangle and dot are 8 apart on centerlines nearest (24, 40)<->(24, 32) (needs 8)
    current drawing: published/failed/solo48/triangle-exclamation.svg
  pictographic-primitives/_uncategorized_38/trip road 1_ad200efe-c77b-4f38-9fed-8ab02c8a6235.svg
    failed: mic [road-right]: road-right and pin are 4.24751 apart on centerlines nearest (38, 30)<->(34.9647, 27.0287) (needs 8) | mic [center-far]: center-far and pin are 4.11209 apart on centerlines nearest (24, 22)<->(27.6308, 20.0696) (needs 8) (+1 more)
    current drawing: published/failed/solo48/trip-road-1.svg
  pictographic-primitives/_uncategorized_39/veterinarian_16ebf22c-f2dd-4834-bf5b-3033fd6dbd8a.svg
    failed: mic [shoulders]: shoulders and stethoscope-tube are 0.544138 apart on centerlines nearest (13.8883, 26.4674)<->(14, 27) (needs 8) | mic [collar]: collar and stethoscope-tube are 2.23607 apart on centerlines nearest (16, 26)<->(14, 27) (needs 8) (+5 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/veterinarian.svg
  pictographic-primitives/_uncategorized_39/video game 360 vr_c710459a-2d6e-4c8e-89da-f6b82e663367.svg
    failed: mic [band]: band and game-mouth are 0.00125759 apart on centerlines nearest (24.3783, 29.9988)<->(24.3783, 30.0001) (needs 8) | mic [three]: three and six are 2.7394 apart on centerlines nearest (19.2251, 15.6949)<->(21.8978, 15.094) (needs 8) (+2 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/video-game-360-vr.svg
  pictographic-primitives/_uncategorized_39/video slash_6fd86d6a-33c2-48c8-8e2b-48ffc1882ec2.svg
    failed: mic [body-upper]: body-upper and slash are 3.48791 apart on centerlines nearest (16, 12)<->(13.3931, 14.3172) (needs 8) | mic [body-lower]: body-lower and slash are 4.98273 apart on centerlines nearest (10, 18)<->(13.7241, 14.6897) (needs 8)
    current drawing: published/failed/solo48/video-slash.svg
  pictographic-primitives/_uncategorized_39/waiting room couple_18363920-a131-4703-9250-544ef6984fd4.svg
    failed: mic [clock]: clock and clock-hands are 2.99977 apart on centerlines nearest (17.9995, 12.0368)<->(15, 12) (needs 8) | mic [clock]: clock and head-0 are 3.64997 apart on centerlines nearest (17.6972, 13.8821)<->(21.1629, 15.027) (needs 8) (+3 more)
    also: undersized holes
    current drawing: published/failed/solo48/waiting-room-couple.svg
  pictographic-primitives/_uncategorized_40/weather app sun cloud location_f404c979-1c1a-47d8-a682-5c3d8c7994bf.svg
    failed: mic [sun]: sun and ray-north are 1 apart on centerlines nearest (16, 8)<->(16, 7) (needs 8) | mic [sun]: sun and ray-west are 1 apart on centerlines nearest (8, 16)<->(7, 16) (needs 8) (+9 more)
    also: undersized holes
    current drawing: published/failed/solo48/weather-app-sun-cloud-location.svg
  pictographic-primitives/_uncategorized_40/wheat awn circle exclamation_1e6635a8-8173-444b-b047-ddcc2a5f1d19.svg
    failed: mic [ring]: ring and grain-1--1-outline are 7.90987 apart on centerlines nearest (9.74977, 38.0327)<->(15.3771, 32.474) (needs 8) | holes/pinches: 4 undersized holes; 2 pinches
    also: pinches, undersized holes
    current drawing: published/failed/solo48/wheat-awn-circle-exclamation.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 7 of 11. Redraw each of these 15 reference files in order. (tp:e4a632fb)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_40/workflow agreement_3c6ab24c-f835-4933-927e-e286153e4e97.svg
    failed: mic [bubble]: bubble and check are 5 apart on centerlines nearest (28, 6)<->(28, 11) (needs 8) | mic [bubble]: bubble and head-0 are 4.61614 apart on centerlines nearest (18, 25)<->(13.7716, 26.8519) (needs 8) (+1 more)
    current drawing: published/failed/solo48/workflow-agreement.svg
  pictographic-primitives/_uncategorized_40/z wave logo_36316472-32cf-4e56-a2d2-8989a12c4e29.svg
    failed: mic [wave-0]: wave-0 and wave-1 are 5.99989 apart on centerlines nearest (10.1093, 12.5526)<->(14.7239, 16.3873) (needs 8) | mic [wave-1]: wave-1 and wave-2 are 5.99955 apart on centerlines nearest (17.7681, 13.7459)<->(20.9154, 18.8536) (needs 8) (+2 more)
    current drawing: published/failed/solo48/z-wave-logo.svg
  pictographic-primitives/audio/microphone podcast international 1_1b529eb2-ba2a-4b82-8816-bb0f813a06d5.svg
    failed: mic [equator]: equator and microphone are 4 apart on centerlines nearest (24, 20)<->(24, 24) (needs 8) | mic [globe]: globe and support are 2.82843 apart on centerlines nearest (38, 28)<->(36, 30) (needs 8) (+3 more)
    also: undersized holes
    current drawing: published/failed/solo48/microphone-podcast-international-1.svg
  pictographic-primitives/audio/microphone podcast international_9241b7de-9722-4a77-a035-d10d9bdf9d33.svg
    failed: mic [globe]: globe and support are 2.82843 apart on centerlines nearest (38, 28)<->(36, 30) (needs 8) | mic [microphone]: microphone and stand are 4 apart on centerlines nearest (24, 36)<->(24, 40) (needs 8) (+2 more)
    also: undersized holes
    current drawing: published/failed/solo48/microphone-podcast-international.svg
  pictographic-primitives/design/pen tools_e4b8631c-5185-5ace-a823-05b73325753b.svg
    failed: mic [control-square]: control-square and nib are 4 apart on centerlines nearest (24, 14)<->(24, 18) (needs 8)
    current drawing: published/failed/solo48/pen-tools.svg
  pictographic-primitives/design/photo crop rotate_05a94426-1cba-44df-a701-8939c33872de.svg
    failed: mic [crop-right]: crop-right and top-head are 3 apart on centerlines nearest (26, 15)<->(26, 12) (needs 8) | mic [crop-left]: crop-left and bottom-head are 3 apart on centerlines nearest (22, 33)<->(22, 36) (needs 8)
    current drawing: published/failed/solo48/photo-crop-rotate.svg
  pictographic-primitives/finance/saving money flower_776da6f9-d7d4-597a-a158-44ea69d4fbb8.svg
    failed: mic [coin]: coin and dollar are 4.85038 apart on centerlines nearest (30.7875, 21.3427)<->(27.4863, 17.7891) (needs 8) | mic [coin]: coin and dollar-stem are 2.99977 apart on centerlines nearest (24.0368, 4.00045)<->(24, 7) (needs 8) (+3 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/saving-money-flower.svg
  pictographic-primitives/finance/virtual coin crypto algorand_099a478f-4287-40bc-a508-fc3894c1428a.svg
    failed: mic [logo]: logo and inner-stroke are 4.41894 apart on centerlines nearest (16.0946, 28.9324)<->(20, 31) (needs 8)
    current drawing: published/failed/solo48/virtual-coin-crypto-algorand.svg
  pictographic-primitives/health/insurance cheap_58b70697-62ea-4501-873d-8e51b3416d7a.svg
    failed: mic [coin]: coin and dollar are 2.99952 apart on centerlines nearest (18.8162, 11.6129)<->(17, 14) (needs 8) | mic [coin]: coin and dollar-stem are 0.999925 apart on centerlines nearest (14.0123, 10.0002)<->(14, 11) (needs 8) (+3 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/insurance-cheap.svg
  pictographic-primitives/health/insurance expensive_bf8f6fdd-5ee3-4cb9-9a0f-3104f1eeaa48.svg
    failed: mic [coin]: coin and dollar are 2.99952 apart on centerlines nearest (18.8162, 7.61287)<->(17, 10) (needs 8) | mic [coin]: coin and dollar-stem are 0.999925 apart on centerlines nearest (13.9877, 21.9998)<->(14, 21) (needs 8) (+3 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/insurance-expensive.svg
  pictographic-primitives/health/laboratory sperm_fdaa2690-f7c0-4893-81b1-967aecf80f4b.svg
    failed: mic [field]: field and tail-left are 6.07142 apart on centerlines nearest (5.32211, 31.1503)<->(11, 29) (needs 8) | mic [field]: field and head-right are 7.30335 apart on centerlines nearest (41.9016, 15.0827)<->(35.3581, 18.3263) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/laboratory-sperm.svg
  pictographic-primitives/health/specialty hearing_4c966f3f-127d-48b1-9cb4-530f9109feb3.svg
    failed: mic [outer]: outer and fold are 5.09902 apart on centerlines nearest (18, 34)<->(23, 33) (needs 8) | mic [outer]: outer and sound are 4.47214 apart on centerlines nearest (18, 16)<->(16, 20) (needs 8) (+1 more)
    current drawing: published/failed/solo48/specialty-hearing.svg
  pictographic-primitives/hobbies/embroidery hoop_43991475-8f12-5467-b407-e55e5e59e1f3.svg
    failed: mic [outer-hoop]: outer-hoop and ear-28 are 0.492458 apart on centerlines nearest (27.8833, 12.4784)<->(28, 12) (needs 8)
    current drawing: published/failed/solo48/embroidery-hoop.svg
  pictographic-primitives/hobbies/embroidery hoop_d9cf0e21-172d-52e9-8723-29202feb39ba.svg
    failed: mic [hoop]: hoop and inner-ring are 7.42221 apart on centerlines nearest (16, 16)<->(20.111, 22.1797) (needs 8)
    current drawing: published/failed/solo48/embroidery-hoop-d9cf0e21.svg
  pictographic-primitives/holidays/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg
    failed: mic [heart-top]: heart-top and heart-left are 4.96594 apart on centerlines nearest (20.5448, 17.1403)<->(17.6726, 21.1913) (needs 8) | mic [heart-top]: heart-top and heart-right are 4.96594 apart on centerlines nearest (27.4552, 17.1403)<->(30.3274, 21.1913) (needs 8) (+2 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/kanda-matsuri.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 8 of 11. Redraw each of these 15 reference files in order. (tp:46031b5e)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/holidays/thaipusam 1_d6a78037-29f1-4227-a0c5-2e4158ef4f53.svg
    failed: mic [base-triangle]: base-triangle and emblem are 4 apart on centerlines nearest (24, 38)<->(24, 34) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/thaipusam-1.svg
  pictographic-primitives/hotels/reception pay_3d9430ac-9d10-4057-8ed4-2eea37cb58a1.svg
    failed: mic [clerk-shoulders]: clerk-shoulders and arms are 4.47214 apart on centerlines nearest (22, 26)<->(26, 28) (needs 8) | mic [counter]: counter and dollar are 5.25281 apart on centerlines nearest (20.6401, 26)<->(20.6401, 31.2528) (needs 8) (+4 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/reception-pay.svg
  pictographic-primitives/interface-essential/expand corner_ea16c393-c392-4d12-b19e-6f8605815090.svg
    failed: mic [open-box]: open-box and shaft are 5.65685 apart on centerlines nearest (26, 14)<->(30, 18) (needs 8)
    current drawing: published/failed/solo48/expand-corner.svg
  pictographic-primitives/interface-essential/resize expand spreadsheet_f210946c-cdf6-4570-9689-058b554c18ac.svg
    failed: mic [table]: table and right-head are 4 apart on centerlines nearest (26, 30)<->(26, 34) (needs 8) | mic [table]: table and up-head are 4 apart on centerlines nearest (30, 10)<->(34, 10) (needs 8)
    current drawing: published/failed/solo48/resize-expand-spreadsheet.svg
  pictographic-primitives/interface-essential/tags double 1_c5a47e41-429f-478a-ac27-be0495e5d5ae.svg
    failed: mic [front]: front and hole are 5.48528 apart on centerlines nearest (21, 17)<->(17.1213, 20.8787) (needs 8)
    current drawing: published/failed/solo48/tags-double-1.svg
  pictographic-primitives/interface-essential/tags double_b3607490-ea3a-409f-a7b1-8386a80c0b93.svg
    failed: mic [front]: front and hole are 6 apart on centerlines nearest (6, 23)<->(12, 23) (needs 8)
    current drawing: published/failed/solo48/tags-double.svg
  pictographic-primitives/interface-essential/tags double_bbbb8c01-8107-4272-9dce-88135b510ab3.svg
    failed: mic [front]: front and hole are 6 apart on centerlines nearest (6, 23)<->(12, 23) (needs 8)
    current drawing: published/failed/solo48/tags-double-bbbb8c01.svg
  pictographic-primitives/interface-essential/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg
    failed: mic [clock]: clock and hands are 5.75693 apart on centerlines nearest (31.1204, 31.0205)<->(27, 27) (needs 8)
    current drawing: published/failed/solo48/time-clock-file-1.svg
  pictographic-primitives/mobile/charging flash wave_c8b3d9a1-bb0f-4df5-b706-4b00986008d6.svg
    failed: mic [flash]: flash and left-inner are 4.93246 apart on centerlines nearest (18, 26)<->(13.0801, 26.3515) (needs 8) | mic [flash]: flash and right-inner are 4.93246 apart on centerlines nearest (30, 22)<->(34.9199, 21.6485) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/charging-flash-wave.svg
  pictographic-primitives/mobile/squeeze sides_bb90ccf0-9578-45c7-ad84-a7eb1350bdaf.svg
    failed: mic [phone]: phone and left-squeeze are 8 apart on centerlines nearest (10, 14)<->(18, 14) (needs 8) | mic [phone]: phone and right-squeeze are 8 apart on centerlines nearest (38, 14)<->(30, 14) (needs 8) (+2 more)
    current drawing: published/failed/solo48/squeeze-sides-bb90ccf0.svg
  pictographic-primitives/music/ipod play_95b0fd3b-05a5-49bd-b7c9-29486aaf4857.svg
    failed: mic [separator]: separator and play are 4 apart on centerlines nearest (18, 28)<->(18, 24) (needs 8) | mic [body]: body and button are 5 apart on centerlines nearest (24, 44)<->(24, 39) (needs 8)
    current drawing: published/failed/solo48/ipod-play.svg
  pictographic-primitives/navigation/compass east_e91a4b42-5376-4b1a-ab2d-8d86c029fcca.svg
    failed: mic [badge]: badge and letter-e are 3.05524 apart on centerlines nearest (10.6599, 13.2543)<->(12, 16) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/compass-east.svg
  pictographic-primitives/other/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg
    failed: mic [lower-tip]: lower-tip and letter-a are 2 apart on centerlines nearest (14, 32)<->(16, 32) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/a-with-sync-arrow.svg
  pictographic-primitives/other/app window wifi_d12b5c6d-5cff-4f23-9893-76defe7ca390.svg
    failed: mic [wifi-outer]: wifi-outer and wifi-inner are 7.9994 apart on centerlines nearest (10.0779, 11.2522)<->(16.6741, 15.7777) (needs 8) | mic [wifi-outer]: wifi-outer and window are 8 apart on centerlines nearest (8, 18)<->(8, 26) (needs 8) (+1 more)
    current drawing: published/failed/solo48/app-window-wifi.svg
  pictographic-primitives/other/book person_8ed961c5-a996-4c78-a7d6-d1d6baa41755.svg
    failed: mic [book]: book and arms are 8 apart on centerlines nearest (8, 24)<->(16, 24) (needs 8) | mic [head]: head and arms are 7.99992 apart on centerlines nearest (24, 19)<->(24.0368, 26.9998) (needs 8)
    current drawing: published/failed/solo48/book-person.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 9 of 11. Redraw each of these 15 reference files in order. (tp:7472b46e)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches | mic [frame]: frame and bluetooth are 3.18322 apart on centerlines nearest (4.34245, 8.24777)<->(7, 10); SUB32 requires at least 6 (ink clearance 2) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/bluetooth-wireless-connectivity-symbol-solo.svg
  pictographic-primitives/other/circle skull 1_0275d46c-9a52-48fb-9993-9a0c2a0a4b89.svg
    failed: mic [skull]: skull and eye--1 are 5.99955 apart on centerlines nearest (13.0009, 22.9264)<->(19, 23) (needs 8) | mic [skull]: skull and eye-1 are 5.99955 apart on centerlines nearest (34.9991, 22.9264)<->(29, 23) (needs 8)
    current drawing: published/failed/solo48/circle-skull-1.svg
  pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg
    failed: mic [outline]: outline and skull-shape are 6.99627 apart on centerlines nearest (33.0971, 6.18913)<->(29.9132, 12.4189) (needs 8) | mic [outline]: outline and bone-a are 3.02938 apart on centerlines nearest (9.8448, 9.87109)<->(12, 12) (needs 8) (+5 more)
    also: undersized holes
    current drawing: published/failed/solo48/skull-and-crossbones-danger-circle-solo.svg
  pictographic-primitives/other/circle skull_52cd86bc-bba7-4a12-8eae-e78fbf4ca2ec.svg
    failed: mic [skull]: skull and eye--1 are 6.99947 apart on centerlines nearest (13.0011, 22.9141)<->(20, 23) (needs 8) | mic [skull]: skull and eye-1 are 6.99947 apart on centerlines nearest (34.9989, 22.9141)<->(28, 23) (needs 8)
    current drawing: published/failed/solo48/circle-skull.svg
  pictographic-primitives/other/file person_96e78ff1-3119-4911-8baf-721686e578a7.svg
    failed: mic [page]: page and head are 7.72792 apart on centerlines nearest (32, 8)<->(26.5355, 13.4645) (needs 8)
    current drawing: published/failed/solo48/file-person.svg
  pictographic-primitives/other/file with shield plus_d1c4154e-8c68-4782-9c5a-e5c81055a594.svg
    failed: mic [page]: page and shield are 6.36396 apart on centerlines nearest (36.5, 12.5)<->(32, 17) (needs 8) | mic [shield]: shield and plus-vertical are 6.26099 apart on centerlines nearest (26.8, 14.4)<->(24, 20) (needs 8)
    current drawing: published/failed/solo48/file-with-shield-plus.svg
  pictographic-primitives/other/heart user_e7e97355-bccb-465c-ae55-5037fd70d291.svg
    failed: mic [heart]: heart and head are 2 apart on centerlines nearest (24, 15)<->(24, 17) (needs 8) | mic [heart]: heart and shoulders are 0.389896 apart on centerlines nearest (17.715, 35.266)<->(18, 35) (needs 8)
    current drawing: published/failed/solo48/heart-user.svg
  pictographic-primitives/other/home cog_8e974970-0198-4484-85aa-47bb0a455f4b.svg
    failed: mic [house]: house and cog are 6 apart on centerlines nearest (24, 42)<->(24, 36) (needs 8) | mic [cog]: cog and hub are 4.47214 apart on centerlines nearest (20, 30)<->(24, 28) (needs 8)
    current drawing: published/failed/solo48/home-cog.svg
  pictographic-primitives/other/house paw print_704fbfc7-8565-458d-83d3-502a2bedf683.svg
    failed: mic [left]: left and top are 6.0001 apart on centerlines nearest (17.6064, 23.8086)<->(22.3936, 20.1914) (needs 8) | mic [left]: left and pad are 5.77817 apart on centerlines nearest (17.4142, 26.4142)<->(21.5, 30.5) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/house-paw-print.svg
  pictographic-primitives/other/house with play button_7e3b79f2-dcc5-4988-ab08-8460306de315.svg
    failed: mic [house]: house and button are 7 apart on centerlines nearest (24, 42)<->(24, 35) (needs 8) | mic [button]: button and play are 3.52747 apart on centerlines nearest (20.4528, 19.83)<->(22, 23) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/house-with-play-button.svg
  pictographic-primitives/other/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg
    failed: mic [lens]: lens and pill are 5.45378 apart on centerlines nearest (10.3906, 31.6034)<->(14.25, 27.75) (needs 8)
    current drawing: published/failed/solo48/magnifying-glass-pill.svg
  pictographic-primitives/other/mail card bug_0b79dbcd-029c-4c05-baad-34d720b23be7.svg
    failed: mic [card]: card and leg-2 are 2 apart on centerlines nearest (34, 19)<->(32, 19) (needs 8) | holes/pinches: 8 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/mail-card-bug.svg
  pictographic-primitives/other/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg
    failed: mic [add-circle]: add-circle and plus-h are 3.9997 apart on centerlines nearest (31.9994, 19.9509)<->(28, 20) (needs 8)
    current drawing: published/failed/solo48/mobile-phone-circle-add.svg
  pictographic-primitives/other/mobile phone eye_68f5ee87-964a-4acb-b5b1-78cd1710295f.svg
    failed: mic [eye-outline]: eye-outline and pupil are 6.83961 apart on centerlines nearest (29.2998, 24.3234)<->(24, 20) (needs 8)
    current drawing: published/failed/solo48/mobile-phone-eye.svg
  pictographic-primitives/other/mobile phone fingerprint_0ef09a66-6578-497b-817b-f821ad82e177.svg
    failed: mic [separator]: separator and inner-ridge are 7 apart on centerlines nearest (32, 36)<->(32, 29) (needs 8) | mic [separator]: separator and left-tail are 6 apart on centerlines nearest (20, 36)<->(20, 30) (needs 8) (+6 more)
    also: undersized holes
    current drawing: published/failed/solo48/mobile-phone-fingerprint.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 10 of 11. Redraw each of these 15 reference files in order. (tp:9c11e689)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/mobile phone woman_c9fc1e73-299a-4164-b9c1-efd780db953d.svg
    failed: mic [head]: head and hair are 0.174753 apart on centerlines nearest (19.0135, 19.3678)<->(18.8392, 19.3799) (needs 8) | mic [hair]: hair and shoulders are 6.06686 apart on centerlines nearest (18, 25)<->(18.8125, 31.0122) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/mobile-phone-woman.svg
  pictographic-primitives/other/mobile phone wrench_05e2ce47-0cc9-49ed-8c9a-44eadff51505.svg
    failed: mic [separator]: separator and jaw-bottom are 6 apart on centerlines nearest (22, 36)<->(22, 30) (needs 8) | mic [jaw-bottom]: jaw-bottom and jaw-top are 4.88654 apart on centerlines nearest (22.6315, 23.5818)<->(25.89, 19.9402) (needs 8)
    current drawing: published/failed/solo48/mobile-phone-wrench.svg
  pictographic-primitives/other/monitor astronomy_05e504e4-9d44-430b-a3b8-b381d38174f9.svg
    failed: mic [screen]: screen and moon are 4.18209 apart on centerlines nearest (20.3428, 34)<->(20.3428, 29.8179) (needs 8) | mic [screen]: screen and star are 6 apart on centerlines nearest (32, 6)<->(32, 12) (needs 8) (+2 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/monitor-astronomy.svg
  pictographic-primitives/other/monitor bug 1_3648786c-989b-4daf-b5c8-46f46ae599ce.svg
    failed: mic [leg-0]: leg-0 and leg-1 are 6 apart on centerlines nearest (21, 16)<->(27, 16) (needs 8) | mic [leg-2]: leg-2 and leg-3 are 6 apart on centerlines nearest (21, 24)<->(27, 24) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/monitor-bug-1.svg
  pictographic-primitives/other/monitor globe_47d2e77c-7d13-4e49-a9d3-b0ee7dd5fe74.svg
    failed: mic [screen]: screen and globe are 4 apart on centerlines nearest (24, 6)<->(24, 10) (needs 8) | mic [screen]: screen and meridian are 4 apart on centerlines nearest (24, 6)<->(24, 10) (needs 8) (+1 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/monitor-globe.svg
  pictographic-primitives/other/monitor math_6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13.svg
    failed: mic [screen]: screen and plus-v are 5 apart on centerlines nearest (19, 34)<->(19, 29) (needs 8) | mic [screen]: screen and divide-bar are 7 apart on centerlines nearest (42, 16)<->(35, 16) (needs 8) (+3 more)
    current drawing: published/failed/solo48/monitor-math.svg
  pictographic-primitives/other/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg
    failed: mic [screen]: screen and palette are 5.1928 apart on centerlines nearest (20.4498, 34)<->(20.4498, 28.8072) (needs 8) | mic [screen]: screen and brush-head are 3 apart on centerlines nearest (42, 18)<->(39, 18) (needs 8) (+7 more)
    also: undersized holes
    current drawing: published/failed/solo48/monitor-painting.svg
  pictographic-primitives/other/passwords correct_602e570f-55c9-4a0a-85e7-806684d11f77.svg
    failed: mic [field]: field and x-0-0 are 5 apart on centerlines nearest (4, 21)<->(9, 21) (needs 8) | mic [field]: field and x-2-1 are 5 apart on centerlines nearest (44, 27)<->(39, 27) (needs 8) (+2 more)
    current drawing: published/failed/solo48/passwords-correct.svg
  pictographic-primitives/other/person magnifying glass_8d4aec38-b440-43a0-b4f2-b3a846ae4cb1.svg
    failed: mic [lens]: lens and person-head are 5.99972 apart on centerlines nearest (21.0046, 6.00028)<->(21, 12) (needs 8) | mic [lens]: lens and body-right are 1.07133 apart on centerlines nearest (26.3848, 34.9998)<->(26, 34) (needs 8)
    current drawing: published/failed/solo48/person-magnifying-glass-solo.svg
  pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg
    failed: mic [check]: check and divider are 6.34545 apart on centerlines nearest (22, 15)<->(27.4412, 18.2647) (needs 8) | mic [divider]: divider and cross-a are 5.83095 apart on centerlines nearest (24, 24)<->(29, 27) (needs 8) (+6 more)
    also: undersized holes
    current drawing: published/failed/solo48/check-and-cross-square-solo.svg
  pictographic-primitives/other/rectangle two persons_d96343a5-e841-44ec-86db-6217d2856341.svg
    failed: mic [panel]: panel and left-head are 7 apart on centerlines nearest (15, 8)<->(15, 15) (needs 8) | mic [panel]: panel and left-shoulders are 4 apart on centerlines nearest (4, 33)<->(8, 33) (needs 8) (+3 more)
    current drawing: published/failed/solo48/rectangle-two-persons.svg
  pictographic-primitives/other/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg
    failed: mic [screen]: screen and dollar-stem are 5 apart on centerlines nearest (18, 6)<->(18, 11) (needs 8) | holes/pinches: 2 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/self-payment-computer-dollar.svg
  pictographic-primitives/other/smart watch circle euro sign_73571a2b-4ed5-4ead-96e1-495841cb43da.svg
    failed: mic [case]: case and euro-bar are 6.99979 apart on centerlines nearest (8.00043, 23.9454)<->(15, 24) (needs 8) | holes/pinches: 2 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/smart-watch-circle-euro-sign.svg
  pictographic-primitives/other/square bubble user_262dd529-82e6-4744-ac57-ec46c428f624.svg
    failed: mic [bubble]: bubble and head are 7 apart on centerlines nearest (24, 6)<->(24, 13) (needs 8) | mic [bubble]: bubble and shoulders are 3 apart on centerlines nearest (32, 36)<->(32, 33) (needs 8)
    current drawing: published/failed/solo48/square-bubble-user.svg
  pictographic-primitives/other/square megaphone_84596dd2-069a-450e-b70c-08a8dc22159b.svg
    failed: mic [frame]: frame and grip are 4.16734 apart on centerlines nearest (26.7474, 42)<->(26.7474, 37.8327) (needs 8)
    current drawing: published/failed/solo48/square-megaphone.svg

- [ ] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 11 of 11. Redraw each of these 13 reference files in order. (tp:50fef212)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/suitcase pill_4c57be23-fe0b-4cb8-b06e-9aed4bc5f3aa.svg
    failed: mic [case]: case and pill are 5.68095 apart on centerlines nearest (25.9876, 14)<->(25.9876, 19.681) (needs 8)
    current drawing: published/failed/solo48/suitcase-pill.svg
  pictographic-primitives/other/tv circle check_91199cb3-6e0d-41e0-9c27-12e09942eed6.svg
    failed: mic [screen]: screen and status-ring are 6 apart on centerlines nearest (24, 6)<->(24, 12) (needs 8) | mic [status-ring]: status-ring and check are 2.99952 apart on centerlines nearest (30.3871, 15.1838)<->(28, 17) (needs 8)
    current drawing: published/failed/solo48/tv-circle-check.svg
  pictographic-primitives/other/tv password_2cc3609a-d235-46f7-828b-ef134a6021e2.svg
    failed: mic [screen]: screen and password-0-0 are 7 apart on centerlines nearest (6, 21)<->(13, 21) (needs 8) | mic [screen]: screen and password-2-1 are 7 apart on centerlines nearest (42, 25)<->(35, 25) (needs 8) (+2 more)
    current drawing: published/failed/solo48/tv-password.svg
  pictographic-primitives/other/ui webpage ad text_24fe2386-b951-48d1-8a50-9d4e65f27e91.svg
    failed: mic [browser]: browser and d-bowl are 6 apart on centerlines nearest (42, 28)<->(36, 28) (needs 8) | holes/pinches: 1 undersized holes; 1 pinches
    also: pinches, undersized holes
    current drawing: published/failed/solo48/ui-webpage-ad-text.svg
  pictographic-primitives/other/ui webpage social profile_6765de1f-1adc-4a6a-bbb4-c497deffd007.svg
    failed: mic [page]: page and shoulders are 1 apart on centerlines nearest (13, 42)<->(13, 41) (needs 8)
    current drawing: published/failed/solo48/ui-webpage-social-profile.svg
  pictographic-primitives/other/woman nude_f11ccece-81b6-415d-a20a-a1bdd3fceb3c.svg
    failed: mic [torso--1]: torso--1 and nipple-0 are 4.98797 apart on centerlines nearest (15.6365, 23.4165)<->(20, 21) (needs 8) | mic [torso-1]: torso-1 and nipple-1 are 4.98797 apart on centerlines nearest (32.3635, 23.4165)<->(28, 21) (needs 8) (+1 more)
    current drawing: published/failed/solo48/woman-nude.svg
  pictographic-primitives/outdoors/outdoors pig apple_1c6d508d-38fb-4b6a-bfe9-e20ebd9e9bf4.svg
    failed: mic [panel]: panel and apple are 3.80664 apart on centerlines nearest (22, 23.2695)<->(25.8066, 23.2695) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/outdoors-pig-apple.svg
  pictographic-primitives/technology/head lock content movement_f9cd92b5-81e6-4ebc-aa40-c2db3af7fac6.svg
    failed: mic [content]: content and ray-left are 4.24264 apart on centerlines nearest (14, 14)<->(11, 11) (needs 8) | mic [content]: content and ray-right are 4.24264 apart on centerlines nearest (19, 21)<->(22, 24) (needs 8) (+3 more)
    current drawing: published/failed/solo48/head-lock-content-movement.svg
  pictographic-primitives/technology/network 5g_9dc361bf-d268-4878-852c-ebdc9f66c69b.svg
    failed: mic [bottom--1]: bottom--1 and five-bowl are 7.46489 apart on centerlines nearest (18, 38)<->(16.9373, 30.6111) (needs 8) | mic [tick--1-16]: tick--1-16 and five-top are 2.82843 apart on centerlines nearest (10, 16)<->(12, 18) (needs 8) (+5 more)
    current drawing: published/failed/solo48/network-5g.svg
  pictographic-primitives/transportation/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg
    failed: mic [wave-outer]: wave-outer and obstacle are 2.49388 apart on centerlines nearest (31.3853, 25.6528)<->(33.6159, 26.7681) (needs 8)
    current drawing: published/failed/solo48/parkig-aid-system.svg
  pictographic-primitives/transportation/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg
    failed: mic [four-bar]: four-bar and m are 6 apart on centerlines nearest (22, 28)<->(28, 28) (needs 8) | mic [four]: four and up are 4.47214 apart on centerlines nearest (18, 14)<->(20, 10) (needs 8) (+3 more)
    current drawing: published/failed/solo48/road-sign-4m-high.svg
  pictographic-primitives/travel/transit no entering stop_688256eb-e269-4b62-9dcc-ecccc8d9b352.svg
    failed: mic [start]: start and dash-top are 7 apart on centerlines nearest (14, 10)<->(21, 10) (needs 8) | mic [right-turn]: right-turn and dash-top are 4 apart on centerlines nearest (28, 10)<->(24, 10) (needs 8) (+3 more)
    current drawing: published/failed/solo48/transit-no-entering-stop.svg
  pictographic-primitives/users/user experience design_0bed2a31-9297-4a65-99ad-c1ed293776b1.svg
    failed: mic [square]: square and head are 7 apart on centerlines nearest (24, 14)<->(24, 21) (needs 8) | mic [circle]: circle and shoulders are 4.31853 apart on centerlines nearest (13.9209, 36.791)<->(18.1458, 37.6854) (needs 8) (+12 more)
    also: undersized holes
    current drawing: published/failed/solo48/user-centered-shape-diagram.svg, published/failed/solo48/user-centered-shape-diagram-v2.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 1 of 9. Redraw each of these 15 reference files in order. (tp:75ca5219)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_02/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg
    failed: mic [upper-node]: parallel straight edges upper-node-3 and right-upper-node-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-no | mic [right-upper-node]: parallel straight edges right-upper-node-3 and right-lower-node-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink  (+6 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/amazon-emr.svg
  pictographic-primitives/_uncategorized_03/anaconda_22672d31-d164-4dfa-a6e8-c5a29193cea8.svg
    failed: mic [snake]: parallel straight edges snake-2 and snake-4 are 6.36396 apart on centerlines (ink gap 2.36396); requires at least 8 centerline / 4 ink (midpoint-normal) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/s-curved-snake.svg
  pictographic-primitives/_uncategorized_04/archive books_42cdb953-b64a-446a-9e2f-0a5e1116e601.svg
    failed: mic [binder-2]: parallel straight edges binder-2-2 and label-2-2 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [binder-2]: parallel straight edges binder-2-2 and label-2-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (overlap-fallback) (+30 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/archive-books.svg
  pictographic-primitives/_uncategorized_04/audio book headphones_b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a.svg
    failed: mic [right-ear]: parallel straight edges right-inner and book-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [book]: parallel straight edges book-6 and left-inner are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/audiobook-with-headphones.svg
  pictographic-primitives/_uncategorized_04/auto pilot car signal 1_148a6d3d-6e93-44b0-ad9c-3c3c30856f29.svg
    failed: mic [beacon-right]: parallel straight edges beacon-right and beacon-stem-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal | mic [window-divider]: parallel straight edges window-divider and center-base are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-norm (+22 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/autonomous-domed-car-with-signal.svg
  pictographic-primitives/_uncategorized_05/band saw_f8387852-af8b-4221-a8f7-998fc1b24294.svg
    failed: mic [inner]: parallel straight edges inner-1 and frame-left-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [inner]: parallel straight edges inner-2 and wheel-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/band-saw.svg
  pictographic-primitives/_uncategorized_12/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg
    failed: mic [gear-1]: parallel straight edges gear-1-2 and gear-1-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-1]: parallel straight edges gear-1-16 and gear-1-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+11 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/cog-double-1.svg
  pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg
    failed: mic [gear-1]: parallel straight edges gear-1-2 and gear-1-32 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [gear-1]: parallel straight edges gear-1-16 and gear-1-18 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+11 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/cog-double.svg
  pictographic-primitives/_uncategorized_14/daytum logo_13398523-c61f-487e-93bd-5e12bc1429a6.svg
    failed: mic [column-3]: parallel straight edges column-3-3 and column-3-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [column-3]: parallel straight edges column-3-1 and column-2-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/four-ascending-chart-columns.svg
  pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg
    failed: mic [tabletop]: parallel straight edges tabletop-5 and crouched-body-4 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [crouched-body]: parallel straight edges crouched-body-4 and crouched-body-12 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint (+9 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/earthquake-hiding-proof-table.svg
  pictographic-primitives/_uncategorized_17/face grin stars_3e7a0a74-079b-41a7-abfe-d06129db8361.svg
    failed: mic [face]: face and star-0 are 2.53539 apart on centerlines nearest (5.67586, 15.9868)<->(8, 17) (needs 8) | mic [face]: face and star-1 are 2.53539 apart on centerlines nearest (42.3241, 15.9868)<->(40, 17) (needs 8) (+12 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/smiling-face-with-star-eyes.svg, published/failed/solo48/smiling-face-with-star-eyes-v2.svg
  pictographic-primitives/_uncategorized_27/modern music monitor speaker_ddfc1e41-af2e-4f27-a89f-8cb60796155a.svg
    failed: mic [music-notes]: parallel straight edges right-note-stem and left-note-stem are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-nor | mic [monitor-bezel]: parallel straight edges monitor-bezel and monitor-bottom are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-nor (+6 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/music-monitor-and-speaker.svg
  pictographic-primitives/_uncategorized_29/office desk 1_57237fb8-d140-4fc2-97bb-fe24ab1c7285.svg
    failed: mic [cup]: parallel straight edges cup-3 and cup-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cup]: parallel straight edges cup-2 and desk-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/office-desk-1.svg
  pictographic-primitives/_uncategorized_29/parking p_7ade5dac-3851-477f-ac45-3ecabf8df504.svg
    failed: mic [p-stem]: parallel straight edges p-stem-3 and p-return are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [roof]: parallel straight edges roof-2 and car-0 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/parking-p.svg
  pictographic-primitives/_uncategorized_30/passport ticket_4813164b-bbb2-498a-aa24-70f1ec279cb1.svg
    failed: mic [ticket-text-0]: parallel straight edges ticket-text-0 and ticket-text-1 are 7.84465 apart on centerlines (ink gap 3.84465); requires at least 8 centerline / 4 ink (m | mic [passport]: passport and globe are 4 apart on centerlines nearest (6, 29)<->(10, 29) (needs 8) (+4 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/passport-ticket.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 2 of 9. Redraw each of these 15 reference files in order. (tp:5894fbbf)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_30/path logo_34127b46-eb99-4c72-abde-13c6d20da3f3.svg
    failed: mic [logo]: parallel straight edges stem-left and left-return are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (midpoint-normal) | holes/pinches: 0 undersized holes; 1 pinches
    also: pinches
    current drawing: published/failed/solo48/path-logo.svg
  pictographic-primitives/_uncategorized_30/people conflict 1_ede2fe9e-b299-44e2-90dd-71980708f31f.svg
    failed: mic [right-back]: parallel straight edges right-back and left-back are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [spark-0]: parallel straight edges spark-0-1 and spark-0-3 are 2.82843 apart on centerlines (ink gap -1.17157); requires at least 8 centerline / 4 ink (midpoint-norma (+4 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/people-conflict-1.svg
  pictographic-primitives/_uncategorized_30/performance increase mail_15cdcedc-403b-4401-be0b-ba02e4b22811.svg
    failed: mic [envelope]: parallel straight edges envelope-3 and bar-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [bar-0]: parallel straight edges bar-0 and envelope-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) (+5 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/performance-increase-mail.svg
  pictographic-primitives/_uncategorized_30/performance tablet increase_2db6cf72-5f8c-42a8-a787-67d6ad07a91f.svg
    failed: mic [thumb]: parallel straight edges thumb-2 and bar-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tablet]: parallel straight edges tablet-3 and arrow-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/performance-tablet-increase.svg
  pictographic-primitives/_uncategorized_30/pest busters_326bdd17-1f70-4f59-8cfb-654489aa053d.svg
    failed: mic [right-antenna]: parallel straight edges right-antenna-1 and slash are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (midpoin | mic [right0]: parallel straight edges right0-1 and right1-1 are 7.58947 apart on centerlines (ink gap 3.58947); requires at least 8 centerline / 4 ink (midpoint-normal) (+13 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/pest-busters.svg
  pictographic-primitives/_uncategorized_31/plane trip cocktail service_102607c1-25ef-426c-be86-bf3e263e4a81.svg
    failed: mic [aircraft]: parallel straight edges aircraft-12 and divider are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [divider]: parallel straight edges divider and rim are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/plane-trip-cocktail-service.svg
  pictographic-primitives/_uncategorized_31/plane trip food service_373ac967-90cc-46ee-9b78-f2b3cc4a75c9.svg
    failed: mic [fork]: parallel straight edges fork-right and fork-stem-1, fork-stem-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-norma | mic [fork-stem]: parallel straight edges fork-stem-1, fork-stem-2 and fork-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-n (+7 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/plane-trip-food-service.svg
  pictographic-primitives/_uncategorized_31/plane trip person_5ba1d1e1-9400-4baf-a55c-e0c11aabf158.svg
    failed: mic [torso]: parallel straight edges torso and bag-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
    current drawing: published/failed/solo48/plane-trip-person.svg
  pictographic-primitives/_uncategorized_31/polyester_7a069c80-678a-480c-a3ff-5da10f209d9c.svg
    failed: mic [sheet]: parallel straight edges sheet-8 and fold-2 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [fold]: fold and vertical-2 are 0.707107 apart on centerlines nearest (31.5, 15.5)<->(31, 16) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/polyester.svg
  pictographic-primitives/_uncategorized_31/pound_4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9.svg
    failed: mic [pound]: parallel straight edges bar-right-1 and foot-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
    current drawing: published/failed/solo48/pound.svg
  pictographic-primitives/_uncategorized_31/prescription drug px 2_5a9d43a5-7519-4e64-81a0-64a7c06298cc.svg
    failed: mic [writing-0]: parallel straight edges writing-0 and writing-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [writing-1]: parallel straight edges writing-1 and paper-bottom are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/prescription-drug-px-2.svg
  pictographic-primitives/_uncategorized_32/rating booklet_d9776d01-07f9-402d-ac77-fc73a405a509.svg
    failed: mic [text-0]: parallel straight edges text-0 and text-1 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [text-0]: parallel straight edges text-0 and cover-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rating-booklet.svg
  pictographic-primitives/_uncategorized_32/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg
    failed: mic [house]: parallel straight edges walls-right-3 and walls-right-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [house]: parallel straight edges walls-right-1 and walls-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/real-estate-favorite-house-rating.svg
  pictographic-primitives/_uncategorized_32/real estate market calculator house_110df7d0-d83c-4e1f-a771-57b0adb39e09.svg
    failed: mic [vertical-divider]: parallel straight edges vertical-divider-1, vertical-divider-2 and plus-bottom are 7 apart on centerlines (ink gap 3); requires at least 8 centerl | mic [vertical-divider]: parallel straight edges vertical-divider-1, vertical-divider-2 and plus-top are 7 apart on centerlines (ink gap 3); requires at least 8 centerline (+21 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/real-estate-market-calculator-house.svg
  pictographic-primitives/_uncategorized_32/real estate market house_1228a3cf-b0ac-41b8-a4db-2d272fbe1241.svg
    failed: mic [house]: parallel straight edges house-3 and door-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/real-estate-market-house.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 3 of 9. Redraw each of these 15 reference files in order. (tp:7aa9a4b1)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_32/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg
    failed: mic [house]: parallel straight edges house-4 and bubble-6 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [house]: parallel straight edges house-4 and bubble-3 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap-fallback) (+4 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/real-estate-message-couple-building.svg
  pictographic-primitives/_uncategorized_32/real estate search house 2_eb4e4433-41fd-4f9e-9779-df93d4b8c025.svg
    failed: mic [house]: parallel straight edges house-3 and door-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    current drawing: published/failed/solo48/real-estate-search-house-2.svg
  pictographic-primitives/_uncategorized_32/recruiting resume document_37ae4172-af70-4ae7-8de2-52970a6302ab.svg
    failed: mic [text1]: parallel straight edges text1 and document-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [document]: document and text1 are 4 apart on centerlines nearest (14, 42)<->(14, 38) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/recruiting-resume-document.svg
  pictographic-primitives/_uncategorized_32/rectangle code_0efa564f-5fe3-43ba-904f-a0826782e979.svg
    failed: mic [frame]: parallel straight edges frame-2 and tr-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [corner]: parallel straight edges corner-1 and bl-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+13 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-code.svg
  pictographic-primitives/_uncategorized_32/rectangle vertical history_69099a2e-0b2c-47a9-931c-af42c66da3a2.svg
    failed: mic [panel]: parallel straight edges panel-2 and arrow-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [arrow]: parallel straight edges arrow-1 and hands-2 are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-vertical-history.svg
  pictographic-primitives/_uncategorized_32/refugee immigration war 2_922ba268-0492-4ece-8f41-54253b52949a.svg
    failed: mic [house]: parallel straight edges house-3 and door-right are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-right and door-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/refugee-immigration-war-2.svg
  pictographic-primitives/_uncategorized_33/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg
    failed: mic [tail]: parallel straight edges tail-2 and legs-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [animal]: animal and trend are 2.43122 apart on centerlines nearest (27.8498, 20.142)<->(29, 18) (needs 8) (+1 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/saving-bull.svg
  pictographic-primitives/_uncategorized_33/seeker_eebf9355-e5dd-4833-b849-ec1865cc85fe.svg
    failed: mic [arm-edge]: parallel straight edges arm-edge and body-side-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [head]: head and lens are 5.26121 apart on centerlines nearest (19.9832, 16.4865)<->(23.4683, 20.4279) (needs 8) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/seeker.svg
  pictographic-primitives/_uncategorized_33/sense of stability_0257fd69-7a18-40fc-a7d2-903d1b421449.svg
    failed: mic [wall-right]: parallel straight edges wall-right-1, wall-right-2 and window-right-1, window-right-2 are 6 apart on centerlines (ink gap 2); requires at least 8 center | mic [window-left]: parallel straight edges window-left-1, window-left-2 and wall-left-1, wall-left-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerlin (+2 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/sense-of-stability.svg
  pictographic-primitives/_uncategorized_34/shipment approve smartphone_59f997a9-32d8-436a-ae34-06535681b16e.svg
    failed: mic [home]: parallel straight edges home and phone-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [box-edge]: box-edge and phone are 5 apart on centerlines nearest (30, 16)<->(30, 21) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/shipment-approve-smartphone.svg
  pictographic-primitives/_uncategorized_34/shipment fragile_6fb1e1e2-8daf-44eb-99ef-5f74d171ee0f.svg
    failed: mic [foot]: parallel straight edges foot and box-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tape]: tape and glass are 7 apart on centerlines nearest (18, 17)<->(18, 24) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/shipment-fragile.svg
  pictographic-primitives/_uncategorized_34/side road angle left 2_d0d6406a-6c7c-431f-a9b8-ee87990c2cf2.svg
    failed: mic [diamond]: parallel straight edges diamond-1 and head-1 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [diamond]: diamond and road are 4.24264 apart on centerlines nearest (15, 33)<->(18, 30) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/side-road-angle-left-2.svg
  pictographic-primitives/_uncategorized_34/side road angle right 2_d19fe7af-bf3f-4193-8210-2e69b664727e.svg
    failed: mic [diamond]: parallel straight edges diamond-4 and head-1 are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [diamond]: diamond and branch are 2.82843 apart on centerlines nearest (32, 34)<->(30, 32) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/side-road-angle-right-2.svg
  pictographic-primitives/_uncategorized_34/smart induction stove_cc0f870e-e6f6-426d-9d3f-73d669be714f.svg
    failed: mic [front]: parallel straight edges front-5, front-4, front-3 and base-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [top]: top and wifi-outer are 6 apart on centerlines nearest (24, 6)<->(24, 12) (needs 8) (+3 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/smart-induction-stove.svg
  pictographic-primitives/_uncategorized_34/smart refrigerator device_30cd9303-dbd1-4ff5-9b6d-c3de44b1a7e4.svg
    failed: mic [handle-0]: parallel straight edges handle-0 and fridge-left-upper, fridge-left-lower are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink ( | mic [handle-1]: parallel straight edges handle-1 and fridge-left-upper, fridge-left-lower are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink ( (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/smart-refrigerator-device.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 4 of 9. Redraw each of these 15 reference files in order. (tp:6e1cee35)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_34/smartphone pay dollar_76f441a8-5364-4c32-8def-992dfc5a44ec.svg
    failed: mic [banknote]: parallel straight edges banknote-4-0 and phone-footer are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [phone]: phone and dollar-stem are 3.16228 apart on centerlines nearest (26, 12)<->(29, 13) (needs 8) (+5 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/smartphone-pay-dollar.svg
  pictographic-primitives/_uncategorized_34/snorer_f8998b5a-15d8-45ce-9679-4cac7ab954c3.svg
    failed: mic [large]: parallel straight edges large-1 and large-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [small]: parallel straight edges small-1 and small-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/snorer.svg
  pictographic-primitives/_uncategorized_34/solar charging car 3_3f94101a-2b9f-45aa-9df1-583e0d6d7077.svg
    failed: mic [panel]: parallel straight edges panel-1 and row are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [row]: parallel straight edges row and panel-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/solar-charging-car-3.svg
  pictographic-primitives/_uncategorized_35/south east_4236f26b-6e26-4a4e-b565-3dda332eac7d.svg
    failed: mic [e]: parallel straight edges e-1 and e-bar are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [e]: parallel straight edges e-1 and e-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) (+8 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/south-east.svg
  pictographic-primitives/_uncategorized_35/square parking_7ad3706e-c1c2-4821-ba45-49920032c75f.svg
    failed: mic [counter-bottom]: parallel straight edges counter-bottom-2 and p-left-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-norma | mic [p-foot]: parallel straight edges p-foot-2 and p-left-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/square-parking.svg
  pictographic-primitives/_uncategorized_35/square person confined_405a762c-b2c7-43c2-8ccd-42ddd4967863.svg
    failed: mic [body-base]: parallel straight edges body-base-3 and right-arm are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [left-arm]: parallel straight edges left-arm and body-base-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/square-person-confined.svg
  pictographic-primitives/_uncategorized_36/stablization operation female_852044c0-c346-4658-9c9c-035df8dc7b7b.svg
    failed: mic [female-cross-2]: parallel straight edges female-cross-2 and female-shaft are 4.24264 apart on centerlines (ink gap 0.242641); requires at least 8 centerline / 4 ink  | mic [female-cross-3]: parallel straight edges female-cross-3 and female-shaft are 4.24264 apart on centerlines (ink gap 0.242641); requires at least 8 centerline / 4 ink  (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/stablization-operation-female.svg
  pictographic-primitives/_uncategorized_37/tag yuan_280da1a2-f9bb-4c4f-8a82-4da931ec7064.svg
    failed: mic [upper]: parallel straight edges upper-1, upper-2 and lower-1, lower-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal | mic [tag]: tag and hole are 6.89949 apart on centerlines nearest (25, 9)<->(29.8787, 13.8787) (needs 8) (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/tag-yuan.svg
  pictographic-primitives/_uncategorized_37/task list multiple_d590c41a-0991-45d2-955b-ea0aa00b5b4a.svg
    failed: mic [check-0]: parallel straight edges check-0-2 and check-1-2 are 6.36396 apart on centerlines (ink gap 2.36396); requires at least 8 centerline / 4 ink (overlap-fallbac | mic [front]: parallel straight edges front-0, front-1 and text-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/task-list-multiple.svg
  pictographic-primitives/_uncategorized_37/technology hand chip_40415ff8-ab5e-4613-9886-33d055540f90.svg
    failed: mic [pin-bottom-1]: parallel straight edges pin-bottom-1 and pin-bottom-0 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [pin-top-1]: parallel straight edges pin-top-1 and pin-top-0 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+11 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/technology-hand-chip.svg
  pictographic-primitives/_uncategorized_37/ticket basketball game_776076fa-8de2-42b1-9fac-cc7b5225e2bd.svg
    failed: mic [ticket-rule-0]: parallel straight edges ticket-rule-0 and ticket-rule-1 are 5.37587 apart on centerlines (ink gap 1.37587); requires at least 8 centerline / 4 ink (m | mic [ball]: ball and seam-one are 0.272066 apart on centerlines nearest (9.80586, 9.8094)<->(10, 10) (needs 8) (+11 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/ticket-basketball-game.svg
  pictographic-primitives/_uncategorized_38/toilet use right_2dff611f-5296-466d-ac68-3fd4303496ea.svg
    failed: mic [toilet]: parallel straight edges toilet-3 and toilet-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [leg]: parallel straight edges leg-1 and toilet-4 are 1 apart on centerlines (ink gap -3); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/toilet-use-right.svg
  pictographic-primitives/_uncategorized_38/toilet use wrong_53c92910-6cf3-4deb-8c80-dce8bbb9cc11.svg
    failed: mic [toilet]: parallel straight edges toilet-3 and toilet-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [leg]: parallel straight edges leg-1 and toilet-4 are 1 apart on centerlines (ink gap -3); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/toilet-use-wrong.svg
  pictographic-primitives/_uncategorized_38/trading news 1_55261672-8aa2-44d9-b648-0fed630f399c.svg
    failed: mic [page]: parallel straight edges page-2 and arrow-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [header]: parallel straight edges header-4 and text-long are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/trading-news-1.svg
  pictographic-primitives/_uncategorized_38/transportation ticket boat transfer_79b63fb3-53d2-42aa-af62-afdbc09d4964.svg
    failed: mic [sail]: parallel straight edges sail-2 and hull-0, hull-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | holes/pinches: 1 undersized holes; 1 pinches
    also: pinches, undersized holes
    current drawing: published/failed/solo48/transportation-ticket-boat-transfer.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 5 of 9. Redraw each of these 15 reference files in order. (tp:b42412af)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_38/trash can list_ec941977-3867-480d-8373-1d308ee56a47.svg
    failed: mic [lid]: parallel straight edges lid-7, lid-6, lid-5 and list-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [list-0]: parallel straight edges list-0 and list-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/trash-can-list.svg
  pictographic-primitives/_uncategorized_38/trash list_1d6b9ee2-a7d3-4044-8400-4b4bc924b7cc.svg
    failed: mic [lid]: parallel straight edges lid-7, lid-6, lid-5 and list-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [list-0]: parallel straight edges list-0 and list-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+11 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/trash-list.svg
  pictographic-primitives/_uncategorized_38/truck moving_1bdf40bf-9d96-43bd-a767-f5237c9e61eb.svg
    failed: mic [house-walls]: parallel straight edges house-walls-3 and door-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [door]: parallel straight edges door-3 and door-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8, pinches
    current drawing: published/failed/solo48/truck-moving.svg
  pictographic-primitives/_uncategorized_39/turn 1_9906051d-60e6-48a1-85dc-e14a0d83a72d.svg
    failed: mic [route]: parallel straight edges route-5 and route-7 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [route]: parallel straight edges route-11 and route-8 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/turn-1.svg
  pictographic-primitives/_uncategorized_39/tv retro_f213d74b-e15b-42ab-953a-a7a36392d15b.svg
    failed: mic [display]: parallel straight edges display-6 and cabinet-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cabinet]: parallel straight edges cabinet-0 and display-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/tv-retro.svg
  pictographic-primitives/_uncategorized_39/user cash scale_fca396e7-351b-4b96-8ac4-233b3625135c.svg
    failed: mic [person-body]: parallel straight edges person-bottom-left, person-bottom-right and beam-1, beam-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerl | mic [person-body]: person-body and beam are 2 apart on centerlines nearest (6, 30)<->(6, 32) (needs 8) (+3 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/user-cash-scale.svg
  pictographic-primitives/_uncategorized_39/user drop zone 1_d40b2438-c966-462c-8e4e-d118211694e3.svg
    failed: mic [upper-link]: parallel straight edges upper-link and p-stem-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [main]: main and p-bowl are 4.99981 apart on centerlines nearest (28.3858, 12.7896)<->(25.3828, 16.7872) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/user-drop-zone-1.svg
  pictographic-primitives/_uncategorized_39/user live_ec05ecd3-fd02-4b5d-ae99-33f8a6f16464.svg
    failed: mic [letter-e]: parallel straight edges letter-e-1 and e-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [e-middle]: parallel straight edges e-middle and letter-e-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/user-live.svg
  pictographic-primitives/_uncategorized_39/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg
    failed: mic [v-first]: parallel straight edges v-first-2 and a-sides-1 are 5.96585 apart on centerlines (ink gap 1.96585); requires at least 8 centerline / 4 ink (midpoint-normal | mic [v-first]: v-first and a-sides are 5.96585 apart on centerlines nearest (10, 10)<->(15.9319, 10.6356) (needs 8) (+7 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/valve-logo.svg
  pictographic-primitives/_uncategorized_39/video game bowl city_c4822a44-f834-4646-8377-fe8ba010de72.svg
    failed: mic [city]: parallel straight edges city-7 and city-5 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [city]: parallel straight edges city-2 and city-10 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/video-game-bowl-city.svg
  pictographic-primitives/_uncategorized_39/video game control directions_171ff3c8-7724-4935-ac18-b58d43e05931.svg
    failed: mic [b-top]: parallel straight edges b-top-0 and b-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b]: parallel straight edges b-4 and b-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/video-game-control-directions.svg
  pictographic-primitives/_uncategorized_39/video game logo companion cube_6e798969-b8c1-4108-aa25-07455cf19213.svg
    failed: mic [right-connector]: parallel straight edges right-connector-2 and right-connector-6 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (mid | mic [corner-1]: parallel straight edges corner-1-6 and top-connector-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+14 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/video-game-logo-companion-cube.svg
  pictographic-primitives/_uncategorized_39/vr video 1_66464e9f-35f0-4894-b4e2-7c801bd38b27.svg
    failed: mic [headset]: parallel straight edges headset-10 and cube-left-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [headset]: parallel straight edges headset-1 and headset-rim are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/vr-video-1.svg
  pictographic-primitives/_uncategorized_39/walking forbidden_d3d76995-132c-4fd1-ae17-729e5381f6a4.svg
    failed: mic [arms]: parallel straight edges arms-1 and hip are 6.1017 apart on centerlines (ink gap 2.1017); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [slash]: slash and head are 4.20004 apart on centerlines nearest (18.2303, 16.3071)<->(21.5904, 13.7871) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/walking-forbidden.svg
  pictographic-primitives/_uncategorized_40/workflow data table increasing arrow_bd44c072-c5cf-4191-b2b0-3681a58f3a3a.svg
    failed: mic [table]: parallel straight edges table-3, table-4 and row-27-1, row-27-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-norm | mic [row-27]: parallel straight edges row-27-1, row-27-2 and row-32-1, row-32-2, row-32-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink ( (+5 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/workflow-data-table-increasing-arrow.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 6 of 9. Redraw each of these 15 reference files in order. (tp:8e38bca3)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/design/design pen tool_cd921e04-704d-5a6b-a478-676cad6d9f2e.svg
    failed: mic [control]: parallel straight edges control-4 and control-2 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint-normal | mic [control]: parallel straight edges control-1 and control-3 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint-normal (+4 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/design-pen-tool.svg
  pictographic-primitives/entertainment/concert rock_3a11e17f-1153-59b2-b135-910a41a584c7.svg
    failed: mic [top-bolt]: parallel straight edges top-bolt-1 and top-bolt-3 are 4.24264 apart on centerlines (ink gap 0.242641); requires at least 8 centerline / 4 ink (midpoint-no | mic [hand]: hand and left-bolt are 2 apart on centerlines nearest (12, 14)<->(12, 12) (needs 8) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/concert-rock.svg
  pictographic-primitives/finance/virtual coin crypto 0x zrx_24bf1d97-6037-5919-9f14-530a400a7d7a.svg
    failed: mic [x-outline]: parallel straight edges x-outline-10 and x-outline-8 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint | mic [x-outline]: parallel straight edges x-outline-2 and x-outline-4 are 5.65685 apart on centerlines (ink gap 1.65685); requires at least 8 centerline / 4 ink (midpoint- (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/virtual-coin-crypto-0x-zrx.svg
  pictographic-primitives/health/monitor heart beat touch_effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1.svg
    failed: mic [hand]: parallel straight edges finger and thumb-6, thumb-5 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [sensor]: parallel straight edges sensor-bottom-right and hand-top are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: undersized holes
    current drawing: published/failed/solo48/monitor-heart-beat-touch.svg
  pictographic-primitives/health/monitoring heart beat hand_f238b6ea-82d0-5437-a344-0ec38b16a28d.svg
    failed: mic [hand-inner]: parallel straight edges finger-1, finger-2 and wrist-inner-3 are 4.94975 apart on centerlines (ink gap 0.949747); requires at least 8 centerline / 4 ink | mic [hand-inner]: parallel straight edges wrist-inner-3 and heart-lower-2 are 6.36396 apart on centerlines (ink gap 2.36396); requires at least 8 centerline / 4 ink (over (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/monitoring-heart-beat-hand.svg
  pictographic-primitives/health/oxygen tank timer_12af7a01-21fd-509d-9eae-c7bfcfdaedd2.svg
    failed: mic [valve]: parallel straight edges valve-3 and valve-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [valve-top]: parallel straight edges valve-top-1, valve-top-2 and hose are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (overlap-fallbac (+5 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/oxygen-tank-timer.svg
  pictographic-primitives/holidays/vaisakhi harvest_a0865ae5-c028-46f5-ade5-f26da83b22c2.svg
    failed: mic [grain-high]: parallel straight edges grain-high and grain-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (overlap-fallback) | mic [drum]: parallel straight edges drum-top and hoop-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/vaisakhi-harvest.svg
  pictographic-primitives/interface-essential/multiple tags 2_da3a18cb-9766-5ab1-b651-eb447e6f30a2.svg
    failed: mic [rear]: parallel straight edges rear-upper-2 and front-right-1, front-right-2 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink (overlap | mic [front]: front and hole are 6.48528 apart on centerlines nearest (24, 10)<->(28.5858, 14.5858) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/multiple-tags-2.svg
  pictographic-primitives/mobile/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg
    failed: mic [thumb]: parallel straight edges thumb-2 and phone-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [finger-0]: finger-0 and left-arrow are 3.21111 apart on centerlines nearest (7.77772, 18.6741)<->(6, 16) (needs 8) (+2 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/squeeze-sides.svg
  pictographic-primitives/office/co working space plug users_2bdfdcc8-48c5-486d-8a22-b5eab51fd4e4.svg
    failed: mic [plug]: parallel straight edges plug-6-1, plug-6-0 and cord-left-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [plug]: parallel straight edges plug-4-0 and cord-left-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/co-working-space-plug-users.svg
  pictographic-primitives/other/Mobile Phone Cube_23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be.svg
    failed: mic [cube]: parallel straight edges cube-2 and cube-front-seam are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [cube-front-seam]: parallel straight edges cube-front-seam and cube-5 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/mobile-phone-cube.svg
  pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg
    failed: internal-spacing [bolt]: bolt-1 and bolt-3 have 1.7651 units of ink clearance over 7.7225 units; requires 4; review required | mic [terminal]: parallel straight edges terminal and battery-2 are 4 apart on centerlines (ink gap 0); requires at least 6 centerline / 2 ink (midpoint-normal) (+2 more)
    also: part spacing under 8, internal ink clearance
    current drawing: published/failed/solo48/charging-battery-110-solo.svg
  pictographic-primitives/other/browser with 18+ text_fc5ffdff-80e9-4119-bf62-fb7c515c5aad.svg
    failed: mic [calendar-body]: parallel straight edges calendar-body-0 and plus-vertical-1, plus-vertical-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / | mic [calendar-body]: calendar-body and one are 6 apart on centerlines nearest (6, 26)<->(12, 26) (needs 8) (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/browser-with-18-plus-text.svg
  pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg
    failed: mic [m]: parallel straight edges m-4 and m-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [bubble]: bubble and p-stem are 4.96361 apart on centerlines nearest (10.4988, 31.5184)<->(14, 28) (needs 8) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/bubble-message-pm-text.svg
  pictographic-primitives/other/calendar math_14b5dacf-2ae7-4b43-b032-7129b3d49037.svg
    failed: mic [calendar-body]: parallel straight edges calendar-body-0 and one-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [calendar-body]: calendar-body and one are 5 apart on centerlines nearest (44, 20)<->(39, 20) (needs 8) (+2 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/calendar-math.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 7 of 9. Redraw each of these 15 reference files in order. (tp:e40611f7)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/gdpr text in rectangle_06655b8e-39ad-4051-aafc-316a27ffb14a.svg
    failed: mic [d-stem]: parallel straight edges d-stem and g-6 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [g]: parallel straight edges g-6 and g-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/gdpr-text-in-rectangle.svg
  pictographic-primitives/other/house phone_7c7ae497-e683-4449-9d47-32e2c0e677e7.svg
    failed: mic [phone]: parallel straight edges end-left-3 and end-left-1 are 4.94975 apart on centerlines (ink gap 0.949747); requires at least 8 centerline / 4 ink (midpoint-norma | mic [house]: house and phone are 6.6564 apart on centerlines nearest (14.3077, 12.4615)<->(18, 18) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/house-phone.svg
  pictographic-primitives/other/house thermometer_c6485cd4-824d-44f8-a250-201a66d4bd70.svg
    failed: mic [thermometer]: parallel straight edges tube-right and mercury are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [mercury]: parallel straight edges mercury and tube-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/house-thermometer.svg
  pictographic-primitives/other/laptop skull_44a8272b-04c4-4a7c-b200-ee122a35ef32.svg
    failed: mic [jaw-right]: parallel straight edges jaw-right and tooth are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tooth]: parallel straight edges tooth and jaw-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/laptop-skull.svg
  pictographic-primitives/other/laptop small squares_71714a04-dd1b-4fab-90a6-dbd391dacaf5.svg
    failed: mic [screen]: parallel straight edges screen-top and tile-0-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [tile-0]: parallel straight edges tile-0-3 and tile-1-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/laptop-small-squares.svg
  pictographic-primitives/other/mobile phone headphone_e65c555e-8915-44b9-98b2-344d81aac941.svg
    failed: mic [ear-right]: parallel straight edges ear-right-2 and ear-right-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [ear-right]: parallel straight edges ear-right-4 and ear-left-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/mobile-phone-headphone.svg
  pictographic-primitives/other/mobile phone skull_079086c7-cfbe-4c2b-a1d3-438ec4146466.svg
    failed: mic [skull]: parallel straight edges jaw-right and jaw-center are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [jaw-center]: parallel straight edges jaw-center and jaw-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/mobile-phone-skull.svg
  pictographic-primitives/other/mobile phone unlock_b0d42cd4-6acc-4018-ae89-490f3eb333a9.svg
    failed: mic [lock-body]: parallel straight edges lock-body-4 and separator are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [separator]: separator and lock-body are 5 apart on centerlines nearest (28, 36)<->(28, 31) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/mobile-phone-unlock.svg
  pictographic-primitives/other/module file_e715b082-2f7d-4370-a969-0707c7e743f2.svg
    failed: mic [document]: parallel straight edges document-3 and module-2-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [module-2]: parallel straight edges module-2-4 and module-1-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/module-file.svg
  pictographic-primitives/other/monitor graduation hat_25a4cb19-9e79-49d4-b5af-74c85495cf76.svg
    failed: mic [mortarboard]: parallel straight edges mortarboard-1 and mortarboard-3 are 7.42781 apart on centerlines (ink gap 3.42781); requires at least 8 centerline / 4 ink (ove | mic [mortarboard]: parallel straight edges mortarboard-2 and mortarboard-4 are 7.42781 apart on centerlines (ink gap 3.42781); requires at least 8 centerline / 4 ink (ove (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/monitor-graduation-hat.svg
  pictographic-primitives/other/monitor laboratory_6ac9826c-356d-4f89-843e-a1caf6908626.svg
    failed: mic [liquid]: parallel straight edges liquid and flask-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [flask]: parallel straight edges flask-4 and bottom-left, bottom-right are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal (+2 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/monitor-laboratory.svg
  pictographic-primitives/other/monitor letters_dd80ecbb-13f8-47dc-9883-44bd19aa7cc6.svg
    failed: mic [b-top]: parallel straight edges b-top and b-middle are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b-middle]: parallel straight edges b-middle and b-bottom are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/monitor-letters.svg
  pictographic-primitives/other/monitor small squares_1aef3c2a-6d0d-43a2-9616-698d70dc5298.svg
    failed: mic [screen]: parallel straight edges screen-0 and square-0-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [square-0]: parallel straight edges square-0-1 and square-0-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/monitor-small-squares.svg
  pictographic-primitives/other/monitor unlock_045a0447-9d31-4ac4-8345-6b457d6d7fdb.svg
    failed: mic [lock]: parallel straight edges lock-4 and screen-5, screen-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [screen]: screen and lock are 5 apart on centerlines nearest (24, 34)<->(24, 29) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/monitor-unlock.svg
  pictographic-primitives/other/rectangle buy text_7ecac39c-d98d-4ff3-af33-ae4cbc274cb3.svg
    failed: mic [frame]: parallel straight edges frame-2 and y-stem are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [u]: parallel straight edges u-right and u-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/rectangle-buy-text.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 8 of 9. Redraw each of these 15 reference files in order. (tp:84de81b7)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/rectangle employee resume 1_bbec6574-bfdd-4612-9ecb-0def3df626fd.svg
    failed: mic [text0]: parallel straight edges text0 and text1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [text1]: parallel straight edges text1 and frame-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-employee-resume-1.svg
  pictographic-primitives/other/rectangle employee resume_485264e5-d5d9-4af5-a33a-88ae3ae2126e.svg
    failed: mic [bottom0]: parallel straight edges bottom0 and bottom1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [bottom1]: parallel straight edges bottom1 and frame-3 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+10 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-employee-resume.svg
  pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg
    failed: mic [k-stem]: parallel straight edges k-stem and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [l]: parallel straight edges l-1 and frame-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-like-text.svg
  pictographic-primitives/other/rectangle single man focus_748d6e5f-8942-4061-a602-5b499075202e.svg
    failed: mic [panel]: parallel straight edges panel-2 and focus-br-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [panel]: parallel straight edges panel-2 and focus-tr-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+10 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/rectangle-single-man-focus.svg
  pictographic-primitives/other/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg
    failed: mic [b-stem]: parallel straight edges b-stem-2, b-stem-1 and u-right are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [u]: parallel straight edges u-right and u-left are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/rectangle-sub-text.svg
  pictographic-primitives/other/self payment computer pound_1e1fac7c-54c5-4468-baea-d2c722f0520d.svg
    failed: mic [pound-base]: parallel straight edges pound-base-1 and screen-4, screen-3 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-nor | mic [screen]: screen and pound-turn are 5 apart on centerlines nearest (12, 34)<->(12, 29) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/self-payment-computer-pound.svg
  pictographic-primitives/other/smart watch square dollar sign_22b0de95-e0f5-450b-9f1f-9e0284263be7.svg
    failed: mic [strap-top]: parallel straight edges strap-top-2 and case-0-0, case-0-1, case-0-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midp | mic [case]: parallel straight edges case-4-2, case-4-1, case-4-0 and strap-bottom-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoi (+2 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/smart-watch-square-dollar-sign.svg
  pictographic-primitives/other/smart watch square pound sign_2c0ac7cd-8681-4e21-803e-6437b35eb4a2.svg
    failed: mic [strap-top]: parallel straight edges strap-top-2 and case-0-0, case-0-1, case-0-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midp | mic [case]: parallel straight edges case-4-2, case-4-1, case-4-0 and strap-bottom-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoi (+2 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/smart-watch-square-pound-sign.svg
  pictographic-primitives/other/test file_f799a4bf-12e6-4111-a7f7-3023b0c48446.svg
    failed: mic [b]: parallel straight edges b-2 and b-4 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [b]: parallel straight edges b-2 and b-lower-0 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+10 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/test-file.svg
  pictographic-primitives/other/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg
    failed: mic [skull]: parallel straight edges jaw-right and middle-tooth are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [middle-tooth]: parallel straight edges middle-tooth and jaw-left are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/ui-webpage-skull.svg
  pictographic-primitives/payments/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg
    failed: mic [card]: parallel straight edges card-2-0 and stripe are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [stripe]: parallel straight edges stripe and card-6-0 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/credit-card-payment.svg
  pictographic-primitives/programing/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg
    failed: mic [digit-1-2]: parallel straight edges digit-1-2 and digit-1-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [digit-0-0]: digit-0-0 and digit-0-1 are 4 apart on centerlines nearest (6, 10)<->(10, 10) (needs 8) (+20 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/data-lake-code.svg
  pictographic-primitives/sports/scoreboard_0918c48a-7ee6-4895-9035-4645fdc17ae1.svg
    failed: mic [panel]: parallel straight edges panel-2 and zero-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [two-bottom]: parallel straight edges two-bottom-2 and panel-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/scoreboard.svg
  pictographic-primitives/sports/scoreboard_26cfbb23-55d5-4b36-b8ee-026317013752.svg
    failed: mic [panel]: parallel straight edges panel-2 and zero-2 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [two-bottom]: parallel straight edges two-bottom-2 and panel-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/scoreboard-26cfbb23.svg
  pictographic-primitives/sports/shooting rifle aim_4ed91cc5-870d-4844-a54d-8cf25bededb3.svg
    failed: mic [rifle]: parallel straight edges rifle-1 and stock-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [trigger]: trigger and sight-bottom are 3.83095 apart on centerlines nearest (22.0282, 29.7155)<->(24, 33) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/shooting-rifle-aim.svg

- [ ] Run $primitive-make-ray to repair failed icons: parallel edges too close, batch 9 of 9. Redraw each of these 7 reference files in order. (tp:d183f434)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Parallel straight edges: two parallel straight runs (slots, teeth, list lines, columns, inner frames) are under 8 apart on centerlines. Space parallel runs at least 8 apart, use fewer repeated lines, or widen the part holding them.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/sports/tournament bracket_6d731820-468b-5c38-b10b-859f24a8eab3.svg
    failed: mic [bracket]: parallel straight edges bracket-2, bracket-3 and node-left-0, node-left-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink ( | mic [bracket]: parallel straight edges bracket-2, bracket-3 and node-right-0, node-right-1 are 2 apart on centerlines (ink gap -2); requires at least 8 centerline / 4 ink
    current drawing: published/failed/solo48/tournament-bracket.svg
  pictographic-primitives/transportation/automatic drive gear_f89489d3-928e-4d8e-8a13-9ff760315c90.svg
    failed: mic [letter-o]: parallel straight edges letter-o-2 and letter-o-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [letter-o]: parallel straight edges letter-o-6 and t-stem are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/automatic-drive-gear.svg
  pictographic-primitives/video/amazon web service interactive video service_676befa5-604d-5f0a-9344-ef3dfc7baea7.svg
    failed: mic [triangle-2]: parallel straight edges triangle-2-2 and triangle-4-1 are 5.48795 apart on centerlines (ink gap 1.48795); requires at least 8 centerline / 4 ink (midpoi | mic [triangle-3]: parallel straight edges triangle-3-2 and triangle-5-1 are 5.48795 apart on centerlines (ink gap 1.48795); requires at least 8 centerline / 4 ink (midpoi (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/triangular-video-emblem.svg
  pictographic-primitives/war/death rip_c37f6508-e0df-51bf-9da4-8fafc43e3b54.svg
    failed: mic [stone]: parallel straight edges stone-right and p-stem-2, p-stem-1 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [p-stem]: parallel straight edges p-stem-2, p-stem-1 and i are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/death-rip.svg
  pictographic-primitives/war/tools tear gas_8f58894e-3584-4d7e-9183-ffe9e81333d8.svg
    failed: mic [nozzle]: parallel straight edges nozzle-2 and canister-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [nozzle]: parallel straight edges nozzle-1 and nozzle-3 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/tools-tear-gas.svg
  pictographic-primitives/weather/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg
    failed: mic [letter-e]: parallel straight edges letter-e-1 and e-middle are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [e-middle]: parallel straight edges e-middle and letter-e-4 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+3 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/east.svg
  pictographic-primitives/weather/visibility_c9a32a88-1037-4cb5-8b11-265935d5449f.svg
    failed: mic [zero-1]: parallel straight edges zero-1-1 and zero-1-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) | mic [zero-1]: parallel straight edges zero-1-4 and zero-0-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+8 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/visibility.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 1 of 8. Redraw each of these 15 reference files in order. (tp:a6ba9604)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_03/american football ball 1_a9f0b51b-1232-4e6f-922b-648cbe4c0f54.svg
    failed: internal-spacing [outline / end-band-high]: cap-upper and end-band-high have 1.8312 units of ink clearance over 10.4717 units; requires 4; review required | internal-spacing [outline / end-band-low]: cap-lower and end-band-low have 1.9531 units of ink clearance over 10.2224 units; requires 4; review required
    current drawing: published/failed/solo48/diagonal-american-football.svg
  pictographic-primitives/_uncategorized_03/amphibian frog body_b274b037-6061-4c72-b6f8-f750487d883c.svg
    failed: internal-spacing [frog / right-haunch]: frog-4 and right-haunch-0 have -0.8893 units of ink clearance over 3.0191 units; requires 4; review required | internal-spacing [frog / right-haunch]: frog-5 and right-haunch-0 have 3.4347 units of ink clearance over 2.9165 units; requires 4; review required (+4 more)
    current drawing: published/failed/solo48/front-facing-seated-frog.svg
  pictographic-primitives/_uncategorized_03/ankle tracker_09ba7447-8f77-4033-ba06-5bf4e4d39449.svg
    failed: internal-spacing [foot-outline]: foot-outline-3 and foot-outline-5 have 0.1636 units of ink clearance over 3.7268 units; requires 4; review required | internal-spacing [foot-outline]: foot-outline-6 and foot-outline-9 have 2.9768 units of ink clearance over 2.5 units; requires 4; review required
    current drawing: published/failed/solo48/electronic-ankle-tracking-device.svg
  pictographic-primitives/_uncategorized_04/arch linux logo_7f1ad0e2-4f9e-423b-9473-4df26eae6fed.svg
    failed: internal-spacing [left / base]: left-1 and base-1 have 3.1161 units of ink clearance over 10.9571 units; requires 4; review required | internal-spacing [left / base]: left-2 and base-1 have 3.3082 units of ink clearance over 4.2362 units; requires 4; review required
    current drawing: published/failed/solo48/pointed-arch-linux-emblem.svg
  pictographic-primitives/_uncategorized_04/archaeologist_434aebe0-5637-41b2-ba5b-e41942db8485.svg
    failed: internal-spacing [brim / jaw]: brim and jaw have 3.0287 units of ink clearance over 8.2114 units; requires 4; review required | internal-spacing [jaw / shoulders]: jaw and shoulders have 0.0379 units of ink clearance over 2.646 units; requires 4; review required
    current drawing: published/failed/solo48/archaeologist-beside-a-spade.svg
  pictographic-primitives/_uncategorized_05/avatar carpenter_0a473297-da88-4e1f-8691-703bcbdef5cb.svg
    failed: internal-spacing [saw]: saw-1 and saw-3 have 0.2778 units of ink clearance over 7.9505 units; requires 4; review required | internal-spacing [saw]: saw-1 and saw-4 have 0.2778 units of ink clearance over 7.9505 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/capped-carpenter-beside-a-hand-saw.svg
  pictographic-primitives/_uncategorized_06/bhudda hand finger citron 1_76411d38-aca5-4268-9511-bc3205689722.svg
    failed: internal-spacing [hand]: thumb and thumb have 1.9043 units of ink clearance over 4.3343 units; requires 4; review required
    current drawing: published/failed/solo48/upright-hand-with-curled-fingers.svg
  pictographic-primitives/_uncategorized_06/bilibili logo_967f7cba-3409-4e70-8a1c-ac8501b16e27.svg
    failed: internal-spacing [tv / aerial]: tv-0 and aerial-1 have -3.7462 units of ink clearance over 9.75 units; requires 4; review required | internal-spacing [tv / aerial]: tv-0 and aerial-2 have -3.7462 units of ink clearance over 9.75 units; requires 4; review required
    current drawing: published/failed/solo48/smiling-television-mascot.svg
  pictographic-primitives/_uncategorized_08/buggy_f32dfbb3-c9cb-4afa-ab8c-f60fb98b6072.svg
    failed: internal-spacing [roof / body]: roof-1 and body-3 have 3.6176 units of ink clearance over 2.2359 units; requires 4; review required | internal-spacing [roof / body]: roof-3 and body-3 have 3.6176 units of ink clearance over 2.2359 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/rounded-passenger-car-profile.svg
  pictographic-primitives/_uncategorized_11/chinchilla_df04551f-f9b1-422f-a44f-8a7dfd1d0dda.svg
    failed: internal-spacing [chinchilla]: chinchilla-1 and chinchilla-3 have 3.7033 units of ink clearance over 2.1529 units; requires 4; review required
    current drawing: published/failed/solo48/seated-chinchilla-with-curved-tail.svg
  pictographic-primitives/_uncategorized_11/clapboard_7812933e-4da0-4067-9131-d948a045fef8.svg
    failed: internal-spacing [slate / clapper]: slate-2 and clapper-6 have -2.8485 units of ink clearance over 5.2476 units; requires 4; review required | internal-spacing [slate / clapper]: slate-3 and clapper-5 have 1.15 units of ink clearance over 9.4007 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/movie-production-clapperboard.svg
  pictographic-primitives/_uncategorized_11/cloister_19554f1f-19e3-4b9e-87c9-d610d1b7dcb6.svg
    failed: internal-spacing [facade / door]: facade-4 and door-1 have 3.1275 units of ink clearance over 7.3031 units; requires 4; review required | internal-spacing [window-0 / floor]: window-0-1 and floor have 3.5224 units of ink clearance over 4.1881 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/arched-facade-with-upper-arcade.svg
  pictographic-primitives/_uncategorized_16/eel_f644d4c1-b881-4092-96b4-a643877d65a5.svg
    failed: internal-spacing [eel]: eel-2 and eel-5 have 3.2512 units of ink clearance over 10.3901 units; requires 4; review required | internal-spacing [eel]: eel-4 and eel-8 have 0.6491 units of ink clearance over 2.4051 units; requires 4; review required (+4 more)
    current drawing: published/failed/solo48/eel-with-narrow-raised-tail.svg
  pictographic-primitives/_uncategorized_20/gesture swipe vertical 3_db37e620-1eb0-4c99-bce3-2c53b5c5fa76.svg
    failed: internal-spacing [hand]: hand-6 and hand-9 have 2.9877 units of ink clearance over 2.5 units; requires 4; review required
    current drawing: published/failed/solo48/one-finger-vertical-swipe-gesture.svg
  pictographic-primitives/_uncategorized_20/gesture tap swipe right 1_3b0fa0d0-112f-4a7d-9586-70fd5b30cbaa.svg
    failed: internal-spacing [hand]: hand-3 and hand-11 have 2.3381 units of ink clearance over 6.2165 units; requires 4; review required | internal-spacing [hand]: hand-8 and hand-10 have 0.6248 units of ink clearance over 5 units; requires 4; review required
    current drawing: published/failed/solo48/hand-swipe-right-gesture.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 2 of 8. Redraw each of these 15 reference files in order. (tp:4601754a)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_20/gesture two finger flip right_3808dced-acba-4c34-8f9f-05ba44dfe152.svg
    failed: internal-spacing [hand]: hand-3 and hand-18 have 2.0882 units of ink clearance over 6.9879 units; requires 4; review required | internal-spacing [hand]: hand-4 and hand-8 have 3.0049 units of ink clearance over 7.2467 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/two-finger-swipe-right.svg
  pictographic-primitives/_uncategorized_21/graffiti_c6d7f6d7-a700-4894-830b-9788ba0a2a17.svg
    failed: internal-spacing [cloud / seam]: cloud and seam have 2.7551 units of ink clearance over 3.8535 units; requires 4; review required
    current drawing: published/failed/solo48/interlocking-graffiti-cloud.svg
  pictographic-primitives/_uncategorized_23/infancy care_a8c124ba-bd78-456b-87fd-6763a1095d57.svg
    failed: internal-spacing [hand]: hand-slope and hand-under have 0.2778 units of ink clearance over 5.7144 units; requires 4; review required | internal-spacing [hand]: hand-slope and hand-thumb have 2.4124 units of ink clearance over 5.4659 units; requires 4; review required
    current drawing: published/failed/solo48/hand-protecting-swaddled-baby.svg
  pictographic-primitives/_uncategorized_23/insurance hands_66883e78-cb13-4f81-a6f8-a7ec339ba917.svg
    failed: internal-spacing [hand-left]: hand-left-1 and hand-left-5 have 2.946 units of ink clearance over 4.75 units; requires 4; review required | internal-spacing [hand-left]: hand-left-1 and hand-left-6 have 3.287 units of ink clearance over 3.6893 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/hands-holding-medical-cross.svg
  pictographic-primitives/_uncategorized_24/labor worker_5e90a983-c6c8-4780-99a7-53d2101f43e0.svg
    failed: internal-spacing [head-and-hat / hat-brim]: hard-hat-dome and hat-brim have 3.0287 units of ink clearance over 8.2114 units; requires 4; review required | internal-spacing [head-and-hat / hard-hat-rib]: hard-hat-dome and hard-hat-rib have 2.9685 units of ink clearance over 3.7324 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/construction-worker-with-wrench.svg
  pictographic-primitives/_uncategorized_25/linguist_d3d86e97-b873-48ff-bd6b-fc4456184a6e.svg
    failed: internal-spacing [face / skull]: face-6 and skull have 2.017 units of ink clearance over 5.2485 units; requires 4; review required
    current drawing: published/failed/solo48/speaking-profile-with-empty-bubble.svg
  pictographic-primitives/_uncategorized_26/love heart ranking_23d9de33-2d15-4372-8f12-18cd47ea7ba3.svg
    failed: internal-spacing [heart]: heart-1 and heart-4 have 2.7548 units of ink clearance over 6.7261 units; requires 4; review required | internal-spacing [heart]: heart-5 and heart-8 have 2.7548 units of ink clearance over 6.7261 units; requires 4; review required
    current drawing: published/failed/solo48/heart-ranking-podium.svg
  pictographic-primitives/_uncategorized_26/mantel_cd0e91bf-8014-4487-8310-916da006a67a.svg
    failed: internal-spacing [flame]: flame-1 and flame-5 have 2.4523 units of ink clearance over 4 units; requires 4; review required | internal-spacing [flame]: flame-2 and flame-6 have 3.3786 units of ink clearance over 2.1853 units; requires 4; review required
    current drawing: published/failed/solo48/fireplace-with-burning-flame.svg
  pictographic-primitives/_uncategorized_26/map marks_4a6fa657-5f3d-4ab6-8949-77cda8ee6030.svg
    failed: internal-spacing [pin-1 / map]: pin-right-1 and map-5 have 2.6176 units of ink clearance over 2.25 units; requires 4; review required
    current drawing: published/failed/solo48/map-with-two-location-pins.svg
  pictographic-primitives/_uncategorized_26/mastodon logo 2_5728b0bd-4ca7-4880-8dd9-2620444de10e.svg
    failed: internal-spacing [outline]: underbody and tail-return have 2.4903 units of ink clearance over 5.5 units; requires 4; review required
    current drawing: published/failed/solo48/mastodon-social-network-logo.svg
  pictographic-primitives/_uncategorized_27/mastodon logo 3_0ab8e84d-e705-47dc-805d-8eeccbcc900b.svg
    failed: internal-spacing [outline]: underbody and tail-return have 2.4903 units of ink clearance over 5.5 units; requires 4; review required
    current drawing: published/failed/solo48/mastodon-social-network-icon.svg
  pictographic-primitives/_uncategorized_27/maya logo_adef874c-e298-460c-b8fd-7d6806bd6e51.svg
    failed: internal-spacing [letter-outline]: letter-outline-2 and letter-outline-10 have 2.4726 units of ink clearance over 8.6569 units; requires 4; review required | internal-spacing [letter-outline]: letter-outline-2 and letter-outline-11 have 2.7364 units of ink clearance over 3 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/outlined-capital-m.svg
  pictographic-primitives/_uncategorized_27/medical app smartphone listen_811410b0-f597-4cad-ad05-e3c48b6e64b7.svg
    failed: internal-spacing [stethoscope-u / lower-tube]: u-right-bend and lower-tube-2 have 1.0186 units of ink clearance over 10.75 units; requires 4; review required
    current drawing: published/failed/solo48/smartphone-with-stethoscope.svg
  pictographic-primitives/_uncategorized_27/microsoft internet explorer logo_ff53feac-62ae-4745-9bd7-4e08ad72f21a.svg
    failed: internal-spacing [e-main]: middle-bar and lower-bowl-right have 1.6022 units of ink clearance over 14.534 units; requires 4; review required | internal-spacing [e-main]: lower-bowl-left and outer-bottom-left have 3.9813 units of ink clearance over 10.2226 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/internet-explorer-e.svg
  pictographic-primitives/_uncategorized_28/music box_b9c25347-4f61-49ed-b94b-bdbb23fd2b5e.svg
    failed: internal-spacing [note-right / beam]: note-right-a and beam-1 have 2.1958 units of ink clearance over 3.25 units; requires 4; review required | internal-spacing [note-right / second-beam]: note-right-a and second-beam have -0.9974 units of ink clearance over 5.5 units; requires 4; review required
    current drawing: published/failed/solo48/music-box.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 3 of 8. Redraw each of these 15 reference files in order. (tp:9835b8d1)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_28/music making_8fed7998-a482-495d-a5a5-6b6237429d87.svg
    failed: internal-spacing [note-right / beam]: note-right-a and beam-2 have 3.2164 units of ink clearance over 7.2467 units; requires 4; review required
    current drawing: published/failed/solo48/music-making.svg
  pictographic-primitives/_uncategorized_28/muskrat_763a2d28-4b32-458f-8301-cf3ad514b5a1.svg
    failed: internal-spacing [muskrat / tail]: muskrat-4 and tail-1 have 1.0157 units of ink clearance over 18.7711 units; requires 4; review required | internal-spacing [muskrat / tail]: muskrat-5 and tail-1 have 1.5951 units of ink clearance over 3.75 units; requires 4; review required
    current drawing: published/failed/solo48/crouching-muskrat.svg
  pictographic-primitives/_uncategorized_28/natural disaster hurricane house_3f984823-804b-4a87-b5c2-3f6d4596f2d2.svg
    failed: internal-spacing [hurricane]: tail and inner-coil have 1.6019 units of ink clearance over 23.0852 units; requires 4; review required | internal-spacing [hurricane]: outer-coil and core have 1.6248 units of ink clearance over 29.6698 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/natural-disaster-hurricane-house.svg
  pictographic-primitives/_uncategorized_28/nightclub_4f2adf74-2b0c-4983-8567-ce3c6c50bff8.svg
    failed: internal-spacing [cornice / door]: cornice-2 and door-top have 2.0019 units of ink clearance over 11.25 units; requires 4; review required | internal-spacing [building / door]: building-3 and door-top have 3.5224 units of ink clearance over 4.1881 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/nightclub.svg
  pictographic-primitives/_uncategorized_29/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg
    failed: internal-spacing [dog]: dog-6 and dog-8 have 0.9411 units of ink clearance over 4 units; requires 4; review required
    current drawing: published/failed/solo48/outdoors-dog-house.svg
  pictographic-primitives/_uncategorized_29/paintwork_6c8a1385-af01-4783-b140-1d97d33064f1.svg
    failed: internal-spacing [handle-outline]: handle and handle have 1.7077 units of ink clearance over 20.4118 units; requires 4; review required | internal-spacing [handle-outline / ferrule]: handle-base and ferrule-2 have 2.8436 units of ink clearance over 6.25 units; requires 4; review required
    current drawing: published/failed/solo48/broad-tipped-artist-brush.svg
  pictographic-primitives/_uncategorized_29/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg
    failed: internal-spacing [bent-leg]: outer-thigh and toe-2 have 0.4358 units of ink clearance over 5.3103 units; requires 4; review required | internal-spacing [bent-leg]: outer-calf and toe-2 have 0.4105 units of ink clearance over 13.8979 units; requires 4; review required
    current drawing: published/failed/solo48/pantyhose.svg
  pictographic-primitives/_uncategorized_30/pencil edit desktop_242c5167-10ea-4717-a24b-bd22d2cf9483.svg
    failed: internal-spacing [screen / pencil]: screen-3 and pencil-b-2 have 0.1716 units of ink clearance over 11.25 units; requires 4; review required
    current drawing: published/failed/solo48/pencil-edit-desktop.svg
  pictographic-primitives/_uncategorized_30/pillbox_da7fc73f-7180-4170-9161-a6c525c99704.svg
    failed: internal-spacing [box / lid]: box-1 and lid have 3.2156 units of ink clearance over 2.728 units; requires 4; review required | internal-spacing [box / lid]: box-7 and lid have 3.2156 units of ink clearance over 2.728 units; requires 4; review required
    current drawing: published/failed/solo48/pillbox.svg
  pictographic-primitives/_uncategorized_31/pinworm_12ed033b-94af-439b-9775-23fdba88d590.svg
    failed: internal-spacing [worm]: worm-1 and worm-3 have 2.6827 units of ink clearance over 2.1644 units; requires 4; review required | internal-spacing [worm]: worm-5 and worm-7 have 3.2986 units of ink clearance over 9.7991 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/curving-pinworm.svg
  pictographic-primitives/_uncategorized_31/playroom_c6ecc684-688c-443b-ae9b-74c5652fb4fa.svg
    failed: internal-spacing [house / toy-knob]: house-2 and toy-knob-1 have 3.2619 units of ink clearance over 6.9402 units; requires 4; review required | internal-spacing [house / toy-knob]: house-3 and toy-knob-1 have 2.1958 units of ink clearance over 2.75 units; requires 4; review required (+6 more)
    current drawing: published/failed/solo48/playroom.svg
  pictographic-primitives/_uncategorized_31/plug circle xmark_2fa2e764-f653-4eb6-b13a-4c6d7b198877.svg
    failed: internal-spacing [plug-top / plug-bowl]: plug-top-2 and bowl-right have 2.2156 units of ink clearance over 2.728 units; requires 4; review required | internal-spacing [plug-top / plug-bowl]: plug-top-2 and bowl-left have 2.2156 units of ink clearance over 2.728 units; requires 4; review required
    current drawing: published/failed/solo48/plug-circle-xmark.svg
  pictographic-primitives/_uncategorized_31/programming hold code 2_f5badc78-84c0-4392-89e1-d9fa0712f0cb.svg
    failed: internal-spacing [cupped-left]: hand-left and palm-left have 3.1552 units of ink clearance over 4.9527 units; requires 4; review required | internal-spacing [cupped-left]: hand-left and finger-left have 0 units of ink clearance over 3.0674 units; requires 4; review required (+6 more)
    current drawing: published/failed/solo48/programming-hold-code-2.svg
  pictographic-primitives/_uncategorized_31/protocol open id logo_962c33a0-eaf5-4a99-9127-a5fd1da5870b.svg
    failed: internal-spacing [arrow-upper / arrow-lower]: arrow-upper-1 and arrow-lower-2 have 0.2778 units of ink clearance over 8.4474 units; requires 4; review required | internal-spacing [outer-loop / inner-loop]: outer-loop and inner-loop have 1.5745 units of ink clearance over 22.5312 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/protocol-open-id-logo.svg
  pictographic-primitives/_uncategorized_31/psycho analysis 5_fc8e8b95-766a-4f15-a80b-5e30979a5fc8.svg
    failed: internal-spacing [head-bowl / shoulders]: jaw and shoulders have 0.0186 units of ink clearance over 6.0109 units; requires 4; review required
    current drawing: published/failed/solo48/psycho-analysis-5.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 4 of 8. Redraw each of these 15 reference files in order. (tp:75ae0647)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_32/quote left_bbf400c0-4ed9-481e-8643-979aa728bc9d.svg
    failed: internal-spacing [quote-0]: quote-0-outer and quote-0-inner have 2.3416 units of ink clearance over 19.6173 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer and quote-1-inner have 2.3416 units of ink clearance over 19.6173 units; requires 4; review required
    current drawing: published/failed/solo48/quote-left.svg
  pictographic-primitives/_uncategorized_32/quote right_a669591d-8405-49c2-be0a-5d69af49a20c.svg
    failed: internal-spacing [quote-0]: quote-0-outer and quote-0-inner have 2.3416 units of ink clearance over 19.6173 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer and quote-1-inner have 2.3416 units of ink clearance over 19.6173 units; requires 4; review required
    current drawing: published/failed/solo48/quote-right.svg
  pictographic-primitives/_uncategorized_32/quotes_d8e178df-75a7-436c-99cf-7f7c90cf866a.svg
    failed: internal-spacing [quote-0]: quote-0-outer-tail and quote-0-inner-tail have 1.8304 units of ink clearance over 17.5376 units; requires 4; review required | internal-spacing [quote-1]: quote-1-outer-tail and quote-1-inner-tail have 1.8304 units of ink clearance over 17.5376 units; requires 4; review required
    current drawing: published/failed/solo48/quotes.svg
  pictographic-primitives/_uncategorized_32/real estate deal shake_490f19a8-c170-4914-bea1-18cbfb479033.svg
    failed: internal-spacing [handshake-outline]: left-hand-top-1 and thumb-1 have -0.8996 units of ink clearance over 2.1893 units; requires 4; review required | internal-spacing [handshake-outline]: left-hand-top-2 and thumb-return have 1.3525 units of ink clearance over 2.2207 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/real-estate-deal-shake.svg
  pictographic-primitives/_uncategorized_32/remains_7c0ac5c3-a514-484c-9bdf-404c88d05eb7.svg
    failed: internal-spacing [bone]: shaft-upper and shaft-lower have 1.9342 units of ink clearance over 4.7124 units; requires 4; review required
    current drawing: published/failed/solo48/remains.svg
  pictographic-primitives/_uncategorized_33/rogue_4eebbb0e-3d47-4014-a9b8-95819896ada8.svg
    failed: internal-spacing [face / shoulders]: face-1 and shoulders have 0.0264 units of ink clearance over 3.5066 units; requires 4; review required
    current drawing: published/failed/solo48/hooded-person-with-blank-face.svg
  pictographic-primitives/_uncategorized_33/route interstate_65d8507f-531a-4e81-bd3e-1e2516aebe33.svg
    failed: internal-spacing [shield / header]: left-top and header have 3.6868 units of ink clearance over 7 units; requires 4; review required | internal-spacing [shield / header]: right-top and header have 3.6868 units of ink clearance over 7 units; requires 4; review required
    current drawing: published/failed/solo48/route-interstate.svg
  pictographic-primitives/_uncategorized_33/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg
    failed: internal-spacing [bowl-leg / top]: bowl-top and top have -3.9831 units of ink clearance over 6.25 units; requires 4; review required
    current drawing: published/failed/solo48/rupee-sign.svg
  pictographic-primitives/_uncategorized_34/single woman hierachy_868652f3-4bc5-4fe0-96a0-1bc2494937b3.svg
    failed: internal-spacing [spine / node-0]: spine-1 and node-0-3 have 0.1358 units of ink clearance over 2.25 units; requires 4; review required | internal-spacing [spine / node-1]: spine-1 and node-1-0 have 0.1358 units of ink clearance over 2.75 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/single-woman-hierachy.svg
  pictographic-primitives/_uncategorized_34/snake_793e902f-88a8-4473-bf76-f80306c7a173.svg
    failed: internal-spacing [snake]: snake-0 and snake-13 have 1.2192 units of ink clearance over 6.2447 units; requires 4; review required | internal-spacing [snake]: snake-0 and snake-14 have 1.2598 units of ink clearance over 5.7935 units; requires 4; review required (+11 more)
    current drawing: published/failed/solo48/upright-snake-with-curled-lower-body.svg
  pictographic-primitives/_uncategorized_34/soccer kick ball_7637106f-a796-4b5a-8382-ddbd48faa5f0.svg
    failed: internal-spacing [boot]: boot-2 and boot-4 have 3.0682 units of ink clearance over 15.1472 units; requires 4; review required
    current drawing: published/failed/solo48/football-boot-kicking-panelled-ball.svg
  pictographic-primitives/_uncategorized_35/sonic 1_eb2aefc1-7636-41c6-9f3f-921141c93aab.svg
    failed: internal-spacing [head]: head-1 and head-3 have 2.3128 units of ink clearance over 2.4478 units; requires 4; review required | internal-spacing [head]: head-3 and head-5 have 1.5922 units of ink clearance over 4.445 units; requires 4; review required
    current drawing: published/failed/solo48/sonic-head-with-swept-spines.svg
  pictographic-primitives/_uncategorized_35/spasm_c67c9f34-aa4a-4561-aba3-e1d5e5f4f809.svg
    failed: internal-spacing [bolt]: bolt-5 and bolt-7 have 3.3741 units of ink clearance over 2.4678 units; requires 4; review required
    current drawing: published/failed/solo48/spasm.svg
  pictographic-primitives/_uncategorized_35/spork_af4b0bcf-b76c-4768-8a09-e4eb2d20860e.svg
    failed: internal-spacing [spork]: spork-0 and spork-11 have -0.3438 units of ink clearance over 3.2846 units; requires 4; review required | internal-spacing [spork]: spork-6 and spork-8 have -0.3438 units of ink clearance over 3.8864 units; requires 4; review required
    current drawing: published/failed/solo48/three-tined-spork-with-rounded-handle.svg
  pictographic-primitives/_uncategorized_35/spreadsheet data analysis_25858b73-169f-47b3-b602-412321f8cd10.svg
    failed: internal-spacing [axes / curve]: axes-2 and curve have 0.0365 units of ink clearance over 4.25 units; requires 4; review required
    current drawing: published/failed/solo48/spreadsheet-data-analysis.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 5 of 8. Redraw each of these 15 reference files in order. (tp:7b6572c5)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_35/square fragile_611bc604-f296-4d2b-bb5f-5565ddcd7e36.svg
    failed: internal-spacing [foot / bowl-bottom]: foot-1 and bowl-bottom have 0.0166 units of ink clearance over 4 units; requires 4; review required | internal-spacing [foot / bowl-bottom]: foot-2 and bowl-bottom have 0.0166 units of ink clearance over 4 units; requires 4; review required
    current drawing: published/failed/solo48/square-fragile.svg
  pictographic-primitives/_uncategorized_35/square phone hangup_48b58407-6e7b-4cf9-b629-9742f8a963af.svg
    failed: internal-spacing [handset]: handset and handset have -2.0659 units of ink clearance over 13.1472 units; requires 4; review required
    current drawing: published/failed/solo48/square-phone-hangup.svg
  pictographic-primitives/_uncategorized_35/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg
    failed: internal-spacing [handset]: handset and handset have -2.0659 units of ink clearance over 13.1472 units; requires 4; review required
    current drawing: published/failed/solo48/square-phone.svg
  pictographic-primitives/_uncategorized_36/step uncle_eb0291a2-d110-4e0e-9cb6-552c49ef98d5.svg
    failed: internal-spacing [badge / hem]: badge-lower and hem have -3.9663 units of ink clearance over 3 units; requires 4; review required
    current drawing: published/failed/solo48/step-uncle.svg
  pictographic-primitives/_uncategorized_36/street view_6498afd8-8355-4072-b42d-b96eef9111b1.svg
    failed: internal-spacing [arms / legs]: arms-1 and legs-2 have 0.7516 units of ink clearance over 4 units; requires 4; review required | internal-spacing [arms / legs]: arms-2 and legs-3 have 2.1832 units of ink clearance over 3.6893 units; requires 4; review required
    current drawing: published/failed/solo48/street-view.svg
  pictographic-primitives/_uncategorized_38/truck medical_c14f0462-1a4f-4fce-8591-b63fddf2fa6d.svg
    failed: internal-spacing [cargo / wheel-left]: cargo-2 and wheel-left-top have 0.0798 units of ink clearance over 3.5 units; requires 4; review required | internal-spacing [cab / wheel-right]: cab-3 and wheel-right-top have 0.0798 units of ink clearance over 3 units; requires 4; review required
    current drawing: published/failed/solo48/truck-medical.svg
  pictographic-primitives/_uncategorized_39/type cursor_54b02242-5568-41c3-a69f-a06ca068bbf9.svg
    failed: internal-spacing [field / hook]: field-bottom-2 and hook have 3.2156 units of ink clearance over 2.728 units; requires 4; review required
    current drawing: published/failed/solo48/type-cursor.svg
  pictographic-primitives/_uncategorized_40/wave square_23bded82-26fd-41b4-9b35-3c4566fa527a.svg
    failed: internal-spacing [wave]: wave-rise and wave-curl have -0.8965 units of ink clearance over 10.6099 units; requires 4; review required
    current drawing: published/failed/solo48/wave-square.svg
  pictographic-primitives/_uncategorized_40/zcool logo_14555301-7f11-43db-978e-a383d12a3b27.svg
    failed: internal-spacing [flame]: flame-upper and flame-upper have 1.3776 units of ink clearance over 2.1032 units; requires 4; review required
    current drawing: published/failed/solo48/zcool-logo.svg
  pictographic-primitives/files/common file text_5aeb0892-b41b-5c32-97fe-0a13b74d6d80.svg
    failed: internal-spacing [page / fold]: fold-diagonal and fold-corner have 2.3109 units of ink clearance over 4.3492 units; requires 4; review required
    current drawing: published/failed/solo48/common-file-text.svg
  pictographic-primitives/food/symbol fork cross knife_aba5bfb7-5990-4b45-9606-e4cfe58ad1ea.svg
    failed: internal-spacing [fork-head / knife-handle]: fork-left-curve and knife-handle-1 have 1.673 units of ink clearance over 8.7348 units; requires 4; review required | internal-spacing [fork-head / knife-handle]: fork-right-curve and knife-handle-2 have 1.673 units of ink clearance over 7.2374 units; requires 4; review required
    current drawing: published/failed/solo48/crossed-fork-and-chef-knife.svg
  pictographic-primitives/food/symbol spoon cross fork_53cd4f82-ae5a-4f7a-8ddd-de64747944f4.svg
    failed: internal-spacing [fork-head / spoon-handle]: fork-left-curve and spoon-handle-1 have 1.673 units of ink clearance over 8.7348 units; requires 4; review required | internal-spacing [fork-head / spoon-bowl]: fork-right-curve and spoon-upper have 1.2681 units of ink clearance over 4.0814 units; requires 4; review required (+1 more)
    current drawing: published/failed/solo48/crossed-fork-with-spoon.svg
  pictographic-primitives/health/blood bag_7d002be2-8db0-591d-9e62-868a56fdf240.svg
    failed: internal-spacing [bag / tube]: bag-4 and tube have 0.3491 units of ink clearance over 2.2087 units; requires 4; review required
    current drawing: published/failed/solo48/blood-bag-solo.svg
  pictographic-primitives/health/heart rate_8a7bb75e-fc55-5c1f-9e7a-6055f25d511f.svg
    failed: internal-spacing [heart / pulse]: point-2 and pulse-4 have 0.6632 units of ink clearance over 6.4274 units; requires 4; review required
    current drawing: published/failed/solo48/heart-rate.svg
  pictographic-primitives/health/heart rate_a954f676-1cce-4e19-81eb-ec067ec52edc.svg
    failed: internal-spacing [outline / pulse]: right-side and pulse-4 have 1.6448 units of ink clearance over 7.4397 units; requires 4; review required
    current drawing: published/failed/solo48/heart-with-pulse-wave-solo.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 6 of 8. Redraw each of these 15 reference files in order. (tp:2af5cf9c)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/health/prescription drug paper_e0b1e330-cc81-522c-9a29-44fd4f8881cf.svg
    failed: internal-spacing [r / x-cross]: r-bowl and x-cross-1 have 0.4862 units of ink clearance over 4.6731 units; requires 4; review required
    current drawing: published/failed/solo48/prescription-drug-paper.svg
  pictographic-primitives/holidays/snow globe_6c2435e0-bbe9-5122-8cf7-2b3eb32963f3.svg
    failed: internal-spacing [globe / base]: globe-b and base-1 have -3.999 units of ink clearance over 18.5 units; requires 4; review required
    current drawing: published/failed/solo48/snow-globe.svg
  pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg
    failed: internal-spacing [star]: star-1 and star-8 have 3.2675 units of ink clearance over 2.4845 units; requires 4; review required | internal-spacing [star]: star-3 and star-10 have 3.2675 units of ink clearance over 2.4845 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/star.svg
  pictographic-primitives/hotels/room service do not disturb_be992ed2-ade4-5f64-a515-8f186d7ca8e3.svg
    failed: internal-spacing [tag]: hook-return and mouth have 3.5236 units of ink clearance over 2.25 units; requires 4; review required
    current drawing: published/failed/solo48/room-service-do-not-disturb.svg
  pictographic-primitives/interface-essential/dial finger_ac8740e0-9a7e-4e67-901d-18b0353d7000.svg
    failed: internal-spacing [hand]: palm-left and thumb-return have 2.8774 units of ink clearance over 4.1812 units; requires 4; review required
    current drawing: published/failed/solo48/dial-finger.svg
  pictographic-primitives/mobile/force touch press_c167b0e7-d4ac-469d-8f57-09582e267096.svg
    failed: internal-spacing [finger]: finger and finger have 1.7293 units of ink clearance over 13.7031 units; requires 4; review required
    current drawing: published/failed/solo48/force-touch-press.svg
  pictographic-primitives/other/box pen_a89e6154-b80a-49dd-8449-f86a088a5c81.svg
    failed: internal-spacing [box-edge / rim]: box-edge-2 and rim-1 have 0.0283 units of ink clearance over 16.955 units; requires 4; review required | internal-spacing [box-edge / rim]: box-edge-3 and rim-2 have 3.0633 units of ink clearance over 4.9835 units; requires 4; review required
    current drawing: published/failed/solo48/box-pen.svg
  pictographic-primitives/other/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg
    failed: internal-spacing [dollar]: dollar and dollar have 0.6082 units of ink clearance over 3.0712 units; requires 4; review required
    current drawing: published/failed/solo48/briefcase-dollar.svg
  pictographic-primitives/other/browser dollar sign right_150d4701-3c3f-45a7-a26d-8c580a891da1.svg
    failed: internal-spacing [dollar]: dollar and dollar have 1.6267 units of ink clearance over 3.0712 units; requires 4; review required
    current drawing: published/failed/solo48/browser-dollar-sign-right.svg
  pictographic-primitives/other/calendar pie_8c9afa4f-6b92-41b3-8bcd-f538c69afde6.svg
    failed: internal-spacing [pie / spoke-diagonal]: pie-br and spoke-diagonal have 2.7379 units of ink clearance over 3.9976 units; requires 4; review required | internal-spacing [pie / spoke-diagonal]: pie-tl and spoke-diagonal have 2.7379 units of ink clearance over 3.9976 units; requires 4; review required
    current drawing: published/failed/solo48/calendar-pie.svg
  pictographic-primitives/other/car flash_3cb36a1f-8edb-4e21-9623-b8c8fac724c3.svg
    failed: internal-spacing [flash]: flash-1 and flash-3 have -0.1707 units of ink clearance over 5.8577 units; requires 4; review required
    current drawing: published/failed/solo48/car-flash.svg
  pictographic-primitives/other/house lock_a7f1734e-4fae-4c0a-9d33-80bf4a3da78f.svg
    failed: internal-spacing [lock-body / shackle]: lock-body-2 and shackle-top have 3.3897 units of ink clearance over 5.2354 units; requires 4; review required
    current drawing: published/failed/solo48/house-lock.svg
  pictographic-primitives/other/house music_3640f2f0-b0c0-4dbd-9d92-86762ff6cfbb.svg
    failed: internal-spacing [right-note / beam]: right-note-a and beam-1 have 2.1958 units of ink clearance over 3.25 units; requires 4; review required | internal-spacing [right-note / beam]: right-note-a and beam-2 have -0.9974 units of ink clearance over 5.5 units; requires 4; review required
    current drawing: published/failed/solo48/house-music.svg
  pictographic-primitives/other/house unlock_d9e732b9-6854-4fe7-b39f-365bfd54abee.svg
    failed: internal-spacing [lock-body / open-shackle]: lock-body-2 and shackle-top have 3.3491 units of ink clearance over 2.2087 units; requires 4; review required
    current drawing: published/failed/solo48/house-unlock.svg
  pictographic-primitives/other/house ventilator_adc26099-d55f-405e-935e-9a654dc938e4.svg
    failed: internal-spacing [hub / blade-0]: hub-a and blade-0 have 1.5047 units of ink clearance over 4.1175 units; requires 4; review required | internal-spacing [hub / blade-3]: hub-a and blade-3 have 2.0146 units of ink clearance over 2.1757 units; requires 4; review required (+6 more)
    current drawing: published/failed/solo48/house-ventilator.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 7 of 8. Redraw each of these 15 reference files in order. (tp:4351ed28)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg
    failed: internal-spacing [euro-curve / euro-bar]: euro-curve and euro-bar have 1.2741 units of ink clearance over 2.7159 units; requires 4; review required
    current drawing: published/failed/solo48/mobile-phone-euro-sign.svg
  pictographic-primitives/other/mobile phone lock_26319804-c7ff-498f-a76f-62441d482fc8.svg
    failed: internal-spacing [lock-body / shackle]: lock-body-0 and shackle-top have 2.5224 units of ink clearance over 4.1881 units; requires 4; review required
    current drawing: published/failed/solo48/mobile-phone-lock.svg
  pictographic-primitives/other/mobile phone music note_9541eb00-a034-4794-a052-1575ee33b845.svg
    failed: internal-spacing [note-head / flag]: note-head-a and flag have 3.1501 units of ink clearance over 7.3976 units; requires 4; review required
    current drawing: published/failed/solo48/mobile-phone-music-note.svg
  pictographic-primitives/other/mobile phone plane_0a850f90-2953-422f-b95d-65062508b5a1.svg
    failed: internal-spacing [fuselage / wing]: fuselage and wing have 2.4918 units of ink clearance over 2.7477 units; requires 4; review required
    current drawing: published/failed/solo48/mobile-phone-plane.svg
  pictographic-primitives/other/mobile phone pound sign_a70db137-a446-4f4c-b656-4fea14660981.svg
    failed: internal-spacing [pound / bar]: pound and bar have 3.4023 units of ink clearance over 2.824 units; requires 4; review required
    current drawing: published/failed/solo48/mobile-phone-pound-sign.svg
  pictographic-primitives/other/money bill pound_a2425a69-d3ed-4c10-8e19-41a99038d49e.svg
    failed: internal-spacing [note / corner-0]: note-1 and corner-0 have 2.9882 units of ink clearance over 3.6958 units; requires 4; review required | internal-spacing [note / corner-1]: note-1 and corner-1 have 2.9882 units of ink clearance over 3.6958 units; requires 4; review required (+6 more)
    current drawing: published/failed/solo48/money-bill-pound.svg
  pictographic-primitives/other/money bill_57a71ef9-0c30-4a25-a290-84a6666d4f6e.svg
    failed: internal-spacing [note / corner-0]: note-1 and corner-0 have 2.9882 units of ink clearance over 3.6958 units; requires 4; review required | internal-spacing [note / corner-1]: note-1 and corner-1 have 2.9882 units of ink clearance over 3.6958 units; requires 4; review required (+6 more)
    current drawing: published/failed/solo48/money-bill.svg
  pictographic-primitives/other/note dollar sign_d6e3d9b9-b561-4ac3-8008-110d0dfc61d6.svg
    failed: internal-spacing [dollar-s]: dollar-top-bar and dollar-lower have 1.0214 units of ink clearance over 3.75 units; requires 4; review required | internal-spacing [dollar-s]: dollar-upper and dollar-bottom-bar have 1.0214 units of ink clearance over 3.75 units; requires 4; review required
    current drawing: published/failed/solo48/note-dollar-sign.svg
  pictographic-primitives/other/preferences_fea7afa8-61b7-411c-860f-fcb3e2894cf6.svg
    failed: internal-spacing [gear / gear-hub]: gear-1 and gear-hub have 3.5827 units of ink clearance over 2.1828 units; requires 4; review required | internal-spacing [gear / gear-hub]: gear-11 and gear-hub have -0.2971 units of ink clearance over 2.6679 units; requires 4; review required
    current drawing: published/failed/solo48/preferences.svg
  pictographic-primitives/other/prescription px square_83ea3f1d-dfb5-4247-948a-2314faaff6ad.svg
    failed: internal-spacing [rx-up / r-bowl]: rx-up-2 and r-bowl have 0.1929 units of ink clearance over 4.6731 units; requires 4; review required
    current drawing: published/failed/solo48/prescription-px-square.svg
  pictographic-primitives/other/ribbon 2_0c3535ed-6772-4bdc-aea7-fb01cc99793c.svg
    failed: internal-spacing [medal / tail-1]: medal-4 and tail-1-3 have 0.8867 units of ink clearance over 4.6731 units; requires 4; review required | internal-spacing [medal / tail-0]: medal-5 and tail-0-3 have 0.8867 units of ink clearance over 4.6731 units; requires 4; review required
    current drawing: published/failed/solo48/ribbon-2.svg
  pictographic-primitives/other/shield 3_500267df-8bce-44e8-a3f7-89f2ab1be4c0.svg
    failed: internal-spacing [crown / band]: crown-2 and band have 1.2778 units of ink clearance over 5.7144 units; requires 4; review required | internal-spacing [crown / band]: crown-5 and band have 1.2778 units of ink clearance over 5.7144 units; requires 4; review required
    current drawing: published/failed/solo48/shield-3.svg
  pictographic-primitives/other/spoon and fork_dd96595d-042a-465f-9681-d8c23c641754.svg
    failed: internal-spacing [fork / center-tine]: bowl and center-tine have 2.9685 units of ink clearance over 3.7324 units; requires 4; review required
    current drawing: published/failed/solo48/spoon-and-fork.svg
  pictographic-primitives/other/ui webpage t shirt_6fd53a7d-aab1-479b-9e12-e2f8acddcfb2.svg
    failed: internal-spacing [shirt]: shirt-left-2 and shirt-left-4 have -0.2739 units of ink clearance over 2.7055 units; requires 4; review required | internal-spacing [shirt]: shirt-left-3 and neckline have 3.7082 units of ink clearance over 2.6441 units; requires 4; review required (+2 more)
    current drawing: published/failed/solo48/ui-webpage-t-shirt.svg
  pictographic-primitives/phones/phone book_b18b4462-5e10-44fd-99e3-3fb256fb4f34.svg
    failed: internal-spacing [book / shoulders]: book-4 and shoulder-left have 1.2156 units of ink clearance over 2.728 units; requires 4; review required | internal-spacing [book / shoulders]: book-4 and shoulder-right have 1.2156 units of ink clearance over 2.728 units; requires 4; review required
    current drawing: published/failed/solo48/phone-book.svg

- [ ] Run $primitive-make-ray to repair failed icons: internal ink clearance, batch 8 of 8. Redraw each of these 5 reference files in order. (tp:fa372eef)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Internal ink clearance: two edges run side by side over a sustained length with under 4 units of ink gap. The build reports this as 'review required', and that counts as a fail. Open the band to at least 8 on centerlines, or reroute one edge so the pair diverges quickly.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg
    failed: internal-spacing [cell / tail]: cell and tail have 3.3246 units of ink clearance over 2.1578 units; requires 4; review required
    current drawing: published/failed/solo48/slash-sperm.svg
  pictographic-primitives/transportation/kiss and ride_b90f680f-f022-4110-b907-97ad0bbc7f46.svg
    failed: internal-spacing [r-stem / r-leg]: r-stem-1 and r-leg have 0.2778 units of ink clearance over 8.4474 units; requires 4; review required
    current drawing: published/failed/solo48/kiss-and-ride.svg
  pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg
    failed: internal-spacing [body / wheel-36]: body-5 and wheel-36-r have -0.1 units of ink clearance over 6.6407 units; requires 4; review required
    also: reviewer marked Needs fix
    current drawing: published/failed/solo48/shipping-delivery-truck-batch-033.svg, published/solo48/shipping-delivery-truck-solo.svg
  pictographic-primitives/video-games/batch-04/game bundle package 2 game game bundle package_11e6c80b-9352-46d6-afbf-71492aac441e.svg
    failed: internal-spacing [controller]: controller-2 and controller-4 have 2.091 units of ink clearance over 3.7108 units; requires 4; review required | internal-spacing [controller]: controller-6 and controller-8 have 2.091 units of ink clearance over 3.7108 units; requires 4; review required
    current drawing: published/failed/solo48/game-bundle-package-2-game-game-bundle-package.svg
  pictographic-primitives/video-games/batch-12/war banner guild faction_c0fef2f7-6c93-5a77-973b-346d07d1e626.svg
    failed: internal-spacing [finial / banner]: finial-1 and banner-1 have 2.1958 units of ink clearance over 3.25 units; requires 4; review required
    current drawing: published/failed/solo48/war-banner-guild-faction.svg

- [ ] Run $primitive-make-ray to repair failed icons: pinches, batch 1 of 2. Redraw each of these 15 reference files in order. (tp:0ed82997)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_03/amber_3ccf997d-67a6-4970-9541-a4835906cdba.svg
    failed: holes/pinches: 5 undersized holes; 4 pinches
    also: undersized holes
    current drawing: published/failed/solo48/fossilized-bug-in-amber.svg
  pictographic-primitives/_uncategorized_03/amusement park ferris wheel 1_504a0510-ec03-4633-a8b4-a32a2b49ce54.svg
    failed: holes/pinches: 2 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/spoked-ferris-wheel-with-round-cabins.svg
  pictographic-primitives/_uncategorized_03/aquarium_4fb53005-bb60-46fd-bc0e-7ea549f599e9.svg
    failed: holes/pinches: 2 undersized holes; 4 pinches
    also: undersized holes
    current drawing: published/failed/solo48/fish-in-an-aquarium-tank.svg
  pictographic-primitives/_uncategorized_06/bicycle person_816c0a6d-a6b1-4041-9b3e-aa2bb963535f.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/cyclist-on-a-fully-framed-bicycle.svg
  pictographic-primitives/_uncategorized_11/chef gear tea cookies_8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/chef-gear-tea-cookies.svg
  pictographic-primitives/_uncategorized_12/concert microphone_a37d9a40-16b7-4abd-b2f5-962b0ceb5244.svg
    failed: holes/pinches: 3 undersized holes; 3 pinches
    also: undersized holes
    current drawing: published/failed/solo48/concert-stage-with-singer.svg
  pictographic-primitives/_uncategorized_13/crawdad_f4812ef0-fce6-4380-9124-384916ee103d.svg
    failed: holes/pinches: 1 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/crawdad.svg
  pictographic-primitives/_uncategorized_13/crayfish_813ecb4a-07a5-40d2-a4dc-2d3842c2a9f0.svg
    failed: holes/pinches: 4 undersized holes; 6 pinches
    also: undersized holes
    current drawing: published/failed/solo48/crayfish.svg
  pictographic-primitives/_uncategorized_26/male star_9d16496d-3f1e-497f-acc5-d87ece1bf0c8.svg
    failed: holes/pinches: 3 undersized holes; 3 pinches
    also: undersized holes
    current drawing: published/failed/solo48/person-with-three-stars.svg
  pictographic-primitives/_uncategorized_27/microsoft powerpoint logo_1a770dd1-2225-4204-b85f-81e18d91cca2.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/presentation-pie-chart-badge.svg
  pictographic-primitives/_uncategorized_28/nectar_74f05c03-957b-4b86-b062-d7cbbb568098.svg
    failed: holes/pinches: 7 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/nectar.svg
  pictographic-primitives/_uncategorized_29/olympic rings_3c672b26-42c9-4289-a407-8947e0d6a086.svg
    failed: holes/pinches: 7 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/five-interlocking-olympic-rings.svg
  pictographic-primitives/_uncategorized_34/shopping pay hide advertising_59b04c40-2006-4e31-a230-a6be869385d4.svg
    failed: holes/pinches: 4 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/shopping-pay-hide-advertising.svg
  pictographic-primitives/_uncategorized_37/tandem bike_bf66e761-47e7-4f37-adf7-8e87414c6db8.svg
    failed: holes/pinches: 3 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/single-rider-road-bicycle.svg
  pictographic-primitives/_uncategorized_37/task list pin 1_5de932db-9cc5-44c6-b9d7-4ae36e88165f.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/task-list-pin-1.svg

- [ ] Run $primitive-make-ray to repair failed icons: pinches, batch 2 of 2. Redraw each of these 14 reference files in order. (tp:a9f77a3b)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Pinches: the negative space between strokes narrows into a neck that nearly closes (near-tangent approaches, acute junctions, strokes grazing each other). Meet at wider angles, end strokes cleanly on a shared point, or open the neck. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_39/user cash scale 1_79fff0c7-26d4-4146-b968-24705c1e7d4a.svg
    failed: holes/pinches: 4 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/user-cash-scale-1.svg
  pictographic-primitives/_uncategorized_39/user signal_2000d10a-a193-4355-bf76-3a121de4ad3f.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/user-signal.svg
  pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg
    failed: holes/pinches: 4 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/smartwatch-dollar-sign.svg
  pictographic-primitives/ecology/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg
    failed: holes/pinches: 3 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/noise-pollution-car.svg
  pictographic-primitives/other/lock person_ca0b86cd-f823-4251-8d27-7775eddb1f7a.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/lock-person.svg
  pictographic-primitives/other/mobile phone phone_13ea825f-ae04-4150-a4b6-56b3bed9dc5d.svg
    failed: holes/pinches: 2 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/mobile-phone-phone.svg
  pictographic-primitives/other/monitor spoon and folk_84f3f807-398a-4f6c-9d2e-58805a5192a4.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/monitor-spoon-and-folk.svg
  pictographic-primitives/other/monitor with a_fe4e3f6c-b05b-4d47-b62a-141f6676b4fe.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/monitor-with-a.svg
  pictographic-primitives/other/rectangle ad text_e23fb9d7-ed54-45f6-9142-77054c14c7bc.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/rectangle-ad-text.svg
  pictographic-primitives/other/square woman_7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1.svg
    failed: holes/pinches: 1 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/square-woman.svg
  pictographic-primitives/programing/amazon web service sagemaker_f2265828-4def-5cb0-be87-edeb3a4d341e.svg
    failed: holes/pinches: 6 undersized holes; 2 pinches
    also: undersized holes
    current drawing: published/failed/solo48/atom-three-orbits-reference.svg
  pictographic-primitives/romance/wedding celebration_c0ea9f23-ec77-44d1-920d-71fcc67e252e.svg
    failed: holes/pinches: 3 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/wedding-celebration.svg
  pictographic-primitives/transportation/four wheel drive_1dfab6f7-a053-5aee-8d2b-b99c63e6f3df.svg
    failed: holes/pinches: 1 undersized holes; 1 pinches
    also: undersized holes
    current drawing: published/failed/solo48/four-wheel-drive.svg
  pictographic-primitives/travel/plane 1_44d3d80b-4240-42cf-9ac4-2237f7c5d0aa.svg
    failed: holes/pinches: 0 undersized holes; 3 pinches
    current drawing: published/failed/solo48/plane-1-solo.svg

- [ ] Run $primitive-make-ray to repair failed icons: undersized holes, batch 1 of 4. Redraw each of these 15 reference files in order. (tp:1741505b)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_01/adjustable lamp 1_afa0c105-3fb7-4c77-b44d-80888cf292ec.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/adjustable-brightness-light-bulb.svg
  pictographic-primitives/_uncategorized_01/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/aerial-yoga-bow-pose.svg
  pictographic-primitives/_uncategorized_02/amazon web service code commit_e3ffb6e8-3bc2-43d5-82fe-ae251b7b7f41.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/code-version-control-and-branching.svg
  pictographic-primitives/_uncategorized_05/baby care pacifier_fcf2e80c-06a5-42d9-a45c-b4984bad2541.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/diagonal-pacifier-with-a-round-handle.svg
  pictographic-primitives/_uncategorized_07/bower logo_ff183e37-2bed-4312-ad52-11655fc8a512.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/bower-logo.svg
  pictographic-primitives/_uncategorized_08/breeding gender symbols_d98a91a3-2cf0-4bb4-a37a-26d5ea8781e0.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/breeding-gender-symbols.svg
  pictographic-primitives/_uncategorized_15/disability hearing t_42121486-14f6-4035-afad-601034d0d354.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/hearing-assistance-symbol.svg
  pictographic-primitives/_uncategorized_16/elf_2a1d8754-4e2e-4a0a-b2fe-427b85f1964c.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/smiling-elf-with-drooping-bobble-hat.svg
  pictographic-primitives/_uncategorized_26/love boat_74aefd26-5ecb-469f-857a-7b635d067fa7.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/couple-in-bed-with-hearts.svg
  pictographic-primitives/_uncategorized_27/monetization tablet_e64a63c8-c12a-4dd2-90a5-e6fbd2b163fb.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/smartphone-with-dollar-sign.svg
  pictographic-primitives/_uncategorized_27/moving walkway_b13ef0ee-32e3-468d-876a-7e9b08b10fa2.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/person-on-rising-escalator.svg
  pictographic-primitives/_uncategorized_28/netsuke_caf0865b-e1c7-4007-9994-158b89caccc0.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/netsuke.svg
  pictographic-primitives/_uncategorized_28/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/right-profile-with-folded-brain.svg
  pictographic-primitives/_uncategorized_29/paintbrush_f6746ee9-8a45-44c8-81ef-7d3da12c0bca.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/pointed-artist-paintbrush.svg
  pictographic-primitives/_uncategorized_30/passport hand_b569bafc-f80a-44b7-a43f-233891818936.svg
    failed: holes/pinches: 4 undersized holes; 0 pinches
    current drawing: published/failed/solo48/passport-hand.svg

- [ ] Run $primitive-make-ray to repair failed icons: undersized holes, batch 2 of 4. Redraw each of these 15 reference files in order. (tp:e08bfc8d)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_30/phone translate_8e1da427-4019-4007-a9b7-0389885201df.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/phone-translate.svg
  pictographic-primitives/_uncategorized_30/pickup_dd459eaf-90a6-4872-a777-772bcbc71cdf.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/compact-pickup-side-view.svg
  pictographic-primitives/_uncategorized_31/print slash_d0766f1e-f6cf-4413-a966-2923a42de78b.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/print-slash.svg
  pictographic-primitives/_uncategorized_32/read email target_ea274b51-b095-451d-addb-e6a29ef9d9da.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/read-email-target.svg
  pictographic-primitives/_uncategorized_34/snarl_47ddf223-ee29-448c-9235-3145f69bc3fa.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/snarling-face-with-two-fangs.svg
  pictographic-primitives/_uncategorized_35/square bolt_abd4c13a-0851-416c-9370-fe3d89993b99.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/square-bolt.svg
  pictographic-primitives/_uncategorized_35/square dollar_48149687-aa67-49b2-9c81-78cd430cefd6.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/square-dollar-solo.svg
  pictographic-primitives/_uncategorized_35/square quote_34d34b9c-9b87-4c4c-a90e-43f2b8d72ff5.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/square-quote.svg
  pictographic-primitives/_uncategorized_36/station wagon_11bcc694-f1a4-49f8-94dc-9d171a957687.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/station-wagon-reference-11bcc694.svg
  pictographic-primitives/_uncategorized_36/step son_cd254b93-0bc0-4673-bae6-ab625d673425.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/step-son.svg
  pictographic-primitives/_uncategorized_37/tampon with blood_09835567-0ff1-4a11-8952-a45583265d59.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/tampon-with-blood.svg
  pictographic-primitives/_uncategorized_37/terrarium_8e34e917-cb83-4efb-83a2-0bcf26f62a1c.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/terrarium.svg
  pictographic-primitives/_uncategorized_38/tty answer_91565135-36f8-42bb-b2ed-6c12f04a7eb5.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/tty-answer.svg
  pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/smart-watch-yuan-symbol.svg
  pictographic-primitives/ecology/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/noise-pollution-traffic.svg

- [ ] Run $primitive-make-ray to repair failed icons: undersized holes, batch 3 of 4. Redraw each of these 15 reference files in order. (tp:44a16be1)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/holidays/maha shivaratri_53d72a10-e412-48cc-8f05-68600caa04a9.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/maha-shivaratri.svg
  pictographic-primitives/interface-essential/list numbers_b096a1c9-9eca-5c00-9ea3-878dc2c4ba9b.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/list-numbers.svg
  pictographic-primitives/interface-essential/rearrange column_4c602b7b-4759-408d-85ec-47eb4b50b541.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/rearrange-column.svg
  pictographic-primitives/other/Academic Graduation Cap_078c527e-7fad-4791-9242-4409c4f071d0.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/academic-graduation-cap-solo.svg
  pictographic-primitives/other/biology_37c9b2bf-2623-41e2-b321-1ce5634ee388.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/biology.svg
  pictographic-primitives/other/house dollar sign_ac9f1218-ef15-4d4e-a1dd-51bf700d94db.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/house-dollar-sign.svg
  pictographic-primitives/other/men nude_cb6d4791-374d-48bd-942d-4c57ef0d8eb0.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/men-nude.svg
  pictographic-primitives/other/mobile phone a text_1651603f-bfb9-458c-8d4f-d01b057f84fa.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/mobile-phone-a-text.svg
  pictographic-primitives/other/mobile phone moon_f95043ca-40ab-49c2-a1e1-3374c581f165.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/mobile-phone-moon.svg
  pictographic-primitives/other/monitor language_1d9a58b4-68ec-4f8d-9e8a-122fc721d471.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/monitor-language.svg
  pictographic-primitives/other/monitor leaf_991e767c-0d53-46c0-b400-e2914ae3c7ef.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/monitor-leaf.svg
  pictographic-primitives/other/monitor shuttlecock_675d2e83-bae0-46ca-b68a-04732a2c88a9.svg
    failed: holes/pinches: 4 undersized holes; 0 pinches
    current drawing: published/failed/solo48/monitor-shuttlecock.svg
  pictographic-primitives/other/play button_bc216d11-8cf2-4ba4-93cc-9f69078fdc84.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/play-button.svg
  pictographic-primitives/other/ribbon_b54db383-db23-4859-92c2-e71b7abb5e7a.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/ribbon.svg
  pictographic-primitives/other/smart watch circle pound sign_f2d45871-ff3d-44d5-84a8-774df3bd6ba3.svg
    failed: holes/pinches: 3 undersized holes; 0 pinches
    current drawing: published/failed/solo48/smartwatch-pound-symbol.svg

- [ ] Run $primitive-make-ray to repair failed icons: undersized holes, batch 4 of 4. Redraw each of these 13 reference files in order. (tp:f17dc9e2)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Undersized holes: an enclosed pocket of negative space is too small (tiny gaps between strokes, small triangles at junctions, slivers where strokes cross). Enlarge the pocket, close it by merging the strokes, or remove the part. Only complete circles with a centerline diameter of exactly 4 or 6 are exempt. Check gate/holes.png.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/smartwatch circle_db3fcec3-cc75-47da-9ae3-062e38521adb.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/smartwatch-circle.svg
  pictographic-primitives/other/square folk_b2e51317-7251-4abe-a7c5-6e845a33f1c5.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/square-spoon-and-knife-solo.svg
  pictographic-primitives/other/tv control next_99b37bd2-37e1-42f8-b918-e34adc73280d.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/tv-control-next.svg
  pictographic-primitives/other/tv control previous_16b19145-212f-42bd-b9b5-ab0936754a35.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/tv-control-previous.svg
  pictographic-primitives/other/ui webpage bug_0a0feef2-02cf-4796-98f1-93d8a372ce93.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/ui-webpage-bug.svg
  pictographic-primitives/rewards/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg
    failed: holes/pinches: 2 undersized holes; 0 pinches
    current drawing: published/failed/solo48/gift-heart.svg
  pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/ranking-ribbon.svg
  pictographic-primitives/romance/lesbian lgbt festival fair exhibition_6ea8474c-4454-55bb-9882-399cf49d120a.svg
    failed: holes/pinches: 3 undersized holes; 0 pinches
    current drawing: published/failed/solo48/lesbian-lgbt-festival-fair-exhibition.svg
  pictographic-primitives/romance/love heart keyhole_d91aa870-d162-59ac-ae8f-ebb2fbe18fc5.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/love-heart-keyhole.svg
  pictographic-primitives/transportation/luggage compartment release_5f2c92bb-8547-4bda-9a89-b7724021c337.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/luggage-compartment-release.svg
  pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg
    failed: holes/pinches: 4 undersized holes; 0 pinches
    current drawing: published/failed/solo48/passport.svg
  pictographic-primitives/video/video edit split_2dcda804-d52b-4984-9a4e-b6abdfa0030f.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/video-edit-split.svg
  pictographic-primitives/video/video player movie_585c392a-9c3f-4878-ad5b-8aae0e8bf5b5.svg
    failed: holes/pinches: 1 undersized holes; 0 pinches
    current drawing: published/failed/solo48/video-player-movie.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 1 of 12. Redraw each of these 15 reference files in order. (tp:64ce00c0)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_01/airship_94ee19fa-6c64-4340-9c2b-4d23bc7e3842.svg
    reviewer: meaning: "Does not convey the intended meaning"
    current drawing: published/solo48/flying-blimp-airship-batch-033.svg
  pictographic-primitives/_uncategorized_03/apple whole_00524635-8904-4470-bdab-b1b3bd2a41f0.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/apple-with-leaf-solo-00524635.svg
  pictographic-primitives/_uncategorized_11/cloud rain_1b0e7b77-0101-4ff8-b82d-4b17ff5d13e2.svg
    reviewer: manual fix requested
    current drawing: published/solo48/cloud-with-rain-drops.svg
  pictographic-primitives/_uncategorized_15/doorbell_98f12741-22af-40d9-ac63-b267d9991649.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/modern-doorbell-button.svg
  pictographic-primitives/_uncategorized_27/money bill_b1e5658b-c303-4f04-bd4a-6e87cd1ca809.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/rectangular-currency-banknote.svg
  pictographic-primitives/_uncategorized_30/people_492c5a6b-bbb1-4d5d-8fb7-a4836fc2ec91.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/three-person-user-group.svg
  pictographic-primitives/_uncategorized_37/tape measure_7bda009e-9307-44d2-81d1-0e1d95fcd9f0.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/retractable-measuring-tape-tool.svg
  pictographic-primitives/animals/tiger_8d5b656b-3421-5a09-b55b-b470ebf0175b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/bear-muzzle-face.svg
  pictographic-primitives/apps/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg
    reviewer: manual fix requested; manual fix requested; marked Needs fix, no note
    current drawing: published/solo48/android-mascot-robot-icon-batch-001-r2.svg, published/solo48/android-mascot-robot-icon-batch-001-r3.svg
  pictographic-primitives/apps/android_bd2aa3e8-f7cc-5a5e-a765-53cb2b41aabb.svg
    reviewer: other: "make the spacing between two hands and body is 4 units"
    current drawing: published/solo48/android-mascot-with-arms.svg
  pictographic-primitives/artificial-intelligence/brain_2543e428-8532-5444-9cdb-344b1eca155c.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/brain-with-central-fissure.svg
  pictographic-primitives/artificial-intelligence/deepfake face_5e37ff04-4c02-4607-a4b2-b81aa6048524.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/digital-face-with-input-nodes.svg
  pictographic-primitives/audio/headphones human_87b4dae7-6d5a-504e-b877-c237378af3a1.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/person-wearing-headphones-in-profile.svg
  pictographic-primitives/avatars/detective woman_e9337ccf-6e62-4109-8b9f-fb9a7582cfcb.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/detective-woman-1-avatar.svg
  pictographic-primitives/avatars/girl full body_45881775-2179-41cc-98a1-78a598c550c1.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/girl-with-centre-parted-hair.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 2 of 12. Redraw each of these 15 reference files in order. (tp:e9f15166)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/avatars/man doctor_1e909a20-b59c-51ff-929f-4d51607994a7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/doctor-with-stethoscope.svg
  pictographic-primitives/avatars/man doctor_7c323144-b65a-558b-a01d-ac1899c73509.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/man-doctor-avatar.svg
  pictographic-primitives/avatars/man graduate_7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/man-graduate-avatar.svg
  pictographic-primitives/avatars/man_991b8ae3-461f-513b-aacf-3e86a2bc7b73.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/man-wearing-bow-tie.svg
  pictographic-primitives/avatars/woman nurse_e365094b-61bd-5f0a-a1d1-1a7c9525470b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/woman-nurse-avatar.svg
  pictographic-primitives/avatars/woman_420efd38-3335-538c-8fe6-abc9051f9f1b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-with-flared-bob.svg
  pictographic-primitives/avatars/woman_95b40f44-d1d6-5bf0-b419-318e3341e675.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-with-wavy-hair.svg
  pictographic-primitives/avatars/woman_e4415d5a-c5ee-540c-87ea-8ae00f1bef5f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-with-bob-and-v-neck-shirt.svg
  pictographic-primitives/avatars/woman_ff4a6b33-a236-5f2d-89ee-7f8719bc7553.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-with-hair-swept-behind-ears.svg
  pictographic-primitives/beauty/make up lipstick_422fa961-4cef-5bf4-8415-0550aee83639.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/upright-lipstick-with-angled-tip.svg
  pictographic-primitives/beauty/oxygen tank_f86557da-1cc7-4eae-8fd9-4d5f68f015ce.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/oxygen-cylinder-with-t-valve.svg
  pictographic-primitives/beauty/tube_deaee2ee-fbdb-5b36-895c-ad3e9fb08cbb.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/cosmetic-tube-with-oval-label.svg
  pictographic-primitives/building/door left hand closed_f3bcb648-33a4-4112-a9ca-00bcdf092bab.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/door-left-hand-closed.svg
  pictographic-primitives/business/begging hand ask_a322931e-aa9b-59e9-8a03-20657747f732.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/open-palm-hand-gesture-solo-b002-11.svg
  pictographic-primitives/business/scale_098c5b62-8287-467b-95c6-c1b202763219.svg
    reviewer: other: "Make two hanging pans more bigger"
    current drawing: published/solo48/balanced-scale-with-hanging-pans.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 3 of 12. Redraw each of these 15 reference files in order. (tp:da492ff2)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/business/target center_b8bc77c7-b4fc-5617-9e10-555fef8d3e87.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/bullseye-target-with-arrow.svg
  pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/seven-lobed-cannabis-leaf.svg
  pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg
    reviewer: other: "Make the screen wider and more vertical"; other: "Make the screen wider and more vertical"
    current drawing: published/solo48/batch-01-monitor.svg, published/solo48/batch-01-monitor-computers.svg
  pictographic-primitives/computers/batch-04/keyboard_669aedc6-7742-41bf-85bd-47da4843ea6b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/computer-keyboard.svg
  pictographic-primitives/computers/batch-04/mouse_af38802b-7208-5060-b370-9b6f0871299d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/corded-computer-mouse.svg
  pictographic-primitives/computers/batch-06/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/simple-computer-keyboard.svg
  pictographic-primitives/construction/safety helmet mine_cefdcc61-2ed2-5460-9530-e110178b2c81.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/hard-hat-with-wide-curved-brim.svg
  pictographic-primitives/content/book close_49781b64-ccc2-5e53-93f8-360efdda93fc.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/book-close-49781b64.svg
  pictographic-primitives/content/book open_b5768591-30d0-458a-8f42-f8fa19890c4e.svg
    reviewer: other: "Make the book taller vertically, remove all inner lines, and leave the inside empty"
    current drawing: published/solo48/book-open-b5768591.svg
  pictographic-primitives/content/book open_e1dee87f-e9eb-5067-afed-727092c03d65.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/book-open-e1dee87f.svg
  pictographic-primitives/design/color palette sample_0a6ea07b-96af-593d-a5c6-dbc342111877.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/kidney-palette-with-three-round-wells.svg
  pictographic-primitives/design/color palette sample_a50f4b37-52bf-57b9-a897-fe227c4018c5.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/palette-with-two-angular-paint-marks.svg
  pictographic-primitives/design/color picker_8ba14a04-c8da-5278-9772-abe74358faf2.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/broad-diagonal-eyedropper-with-crossbar.svg
  pictographic-primitives/design/fill adjustment layer_3bfeb607-fee8-43a8-8a4a-88f605a7b761.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/fill-adjustment-layer.svg
  pictographic-primitives/devices/device google glass_f3f157a4-4ba4-56cb-af69-39f5c5fe3376.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/augmented-reality-glasses-with-corner-display.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 4 of 12. Redraw each of these 15 reference files in order. (tp:500041a6)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/devices/device wearable vr goggles_b855886b-3199-52ae-a327-5e124680a94d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/rounded-vr-goggles-with-short-side-straps.svg
  pictographic-primitives/drinks/wine barrel_d5b47441-37c4-578a-93be-e68b3ac3e6a3.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/wooden-barrel-with-two-hoops-and-curved-staves.svg
  pictographic-primitives/ecology/air purifier 1_a83ae7ee-8a41-4fef-9868-438ff298dd07.svg
    reviewer: other: "Replace the two solid shapes above the purifier with two thin, vertical S-shaped airflow lines"
    current drawing: published/solo48/air-purifier-with-midline-and-upright-indicator.svg
  pictographic-primitives/ecology/air purifier_e686f130-6226-4d7d-b4c5-09b77a01b089.svg
    reviewer: other: "make clear two curve airflow at the top"
    current drawing: published/solo48/air-purifier-with-two-feet-and-airflow-strokes.svg
  pictographic-primitives/electronics/usb type c_c0a14e2a-4419-5c4d-bceb-f564e7b8279f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/usb-type-c.svg
  pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/landscape-picture-media-file-solo.svg
  pictographic-primitives/food/chocolate bar_b591714c-777b-49a0-ad5a-afc8f96f98b0.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/chocolate-bar.svg
  pictographic-primitives/food/corn_dfc9df01-8144-40e0-b66d-be471956d900.svg
    reviewer: manual fix requested
    current drawing: published/solo48/corn.svg
  pictographic-primitives/food/protein gluten wheat_8c67d503-423f-4f89-820c-06ea16117fe2.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/single-wheat-ear.svg
  pictographic-primitives/furnitures/chair_a6d7267b-b3b5-5e0b-9e6e-aa9a3007719e.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/lounge-chair-side-profile.svg
  pictographic-primitives/health/chemical hexagon_e1fa397a-aca0-4f59-875f-b0f6abeb1a51.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/chemical-molecule-linked-atoms.svg
  pictographic-primitives/health/condom_b5722f6d-66b4-536a-8978-4788bc7df3e7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/condom-reference.svg
  pictographic-primitives/health/hearing aid ear_6a3e9b51-1d2b-5969-ac5c-503d8629e1bb.svg
    reviewer: manual fix requested
    current drawing: published/solo48/ear-with-hearing-aid-reference.svg
  pictographic-primitives/health/medical file_9fea270f-2e24-4304-9328-79e02032c303.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/medical-record-document.svg
  pictographic-primitives/health/pill_02e59f2b-ee20-5358-9891-c4a83553f91b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/capsule-pill-02e59f2b.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 5 of 12. Redraw each of these 15 reference files in order. (tp:67d660d0)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/health/specialty eye_3c23a43b-4a6b-55be-b95b-bc7bc22223cd.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/eye-with-iris-and-pupil.svg
  pictographic-primitives/health/tooth_6120fd88-df4b-5d97-b808-229a95697404.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/molar-tooth-6120fd88.svg
  pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b.svg, published/solo48/raised-open-palm.svg
  pictographic-primitives/holidays/hand_ce1ed58e-e672-4d3c-afbe-79946ffec09f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/open-palm-hand-ce1ed58e-e672-4d3c-afbe-79946ffec09f.svg
  pictographic-primitives/hotels/hotel bed_65881da4-e2b5-4025-8419-8ee364d9b2ba.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-sleeping-in-bed.svg
  pictographic-primitives/hotels/hotel single bed_ec421b89-c7d9-573b-bec3-256a6da2bdb4.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/single-bed-with-pillow.svg
  pictographic-primitives/images/woman_b7558322-6681-447e-8b8a-0f4a588a3f0e.svg
    reviewer: meaning: "Does not convey the intended meaning"
    current drawing: published/solo48/female-user-profile.svg
  pictographic-primitives/interface-essential/cog_3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/cog-interface-essential.svg
  pictographic-primitives/interface-essential/cog_66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg
    reviewer: bad stroke drawn; marked Needs fix, no note
    current drawing: published/solo48/six-lobed-cog-66a27160-f0ef-48c6-8ce3-c2ea9255ad5b.svg, published/solo48/six-lobed-cog-87f6e9f3-5032-4352-afb7-e324d3585e75.svg
  pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg
    reviewer: bad stroke drawn; bad stroke drawn
    current drawing: published/solo48/angular-gear.svg, published/solo48/cog-54edfc1d.svg
  pictographic-primitives/interface-essential/cog_cbadf384-f227-495e-8017-d7e7ebdf0faa.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/cog-cbadf384.svg
  pictographic-primitives/interface-essential/hammer_314dcf43-c8b9-4ecf-b0ac-34ec596e757f.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/hammer.svg, published/solo48/hammer-interface-essential.svg
  pictographic-primitives/interface-essential/pin_f442e678-6fbd-570e-923f-8eae8fd127e0.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/location-pin-above-baseline.svg
  pictographic-primitives/interface-essential/volume_ce974c56-ba13-40f8-bcc7-d0c05f09f26f.svg
    reviewer: marked Needs fix, no note; marked rejected, no note
    current drawing: published/solo48/volume.svg, published/solo48/volume-interface-essential.svg
  pictographic-primitives/mobile/lte_1e4774df-ef53-5eda-941a-67a7eac299a4.svg
    reviewer: marked rejected, no note
    current drawing: published/solo48/lte-text.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 6 of 12. Redraw each of these 15 reference files in order. (tp:55db34d7)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/a half of earth_f0f6fad5-2f20-4017-8eb0-09f030a3cd29.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/half-globe-batch-024-01.svg
  pictographic-primitives/other/adjustable_9d3425c4-0090-4fdf-b40b-9f93695f8ca8.svg
    reviewer: bad stroke drawn; bad stroke drawn
    current drawing: published/solo48/curved-gauge-indicator-batch-018-15.svg, published/solo48/curved-gauge-indicator-solo-b017.svg
  pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg
    reviewer: marked Needs fix, no note; other: "The airplane tilts upward to the right, with an elongated body, a broad rounded nose, and a straight lower edge that curves smoothly into the rear. A large angular wing projects toward the upper left, and a smaller tail fin extends to the left, separated by a deep V-shaped notch"
    current drawing: published/solo48/airplane.svg, published/solo48/airplane-other.svg
  pictographic-primitives/other/artist_537c9790-95ad-4207-bed6-e5d11691c98f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/long-haired-woman-bust.svg
  pictographic-primitives/other/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/diagonal-paperclip-batch-021-13.svg
  pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/bicycle-reference-25-solo.svg, published/solo48/bicycle-with-straight-seat-post.svg
  pictographic-primitives/other/browser dollar sign_07cafd66-efd4-43ca-978e-239ccb6dfed3.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/online-payment-browser-window.svg
  pictographic-primitives/other/calendar number seven_d7201890-607e-4568-916a-e843756d3ef0.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/calendar-number-seven.svg
  pictographic-primitives/other/cart 1_09afbc31-5487-4884-b5bb-9534c9f636f2.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-rounded-open-wheels.svg
  pictographic-primitives/other/cart 1_2007d848-4f3e-4571-a43a-9e9ad6abf259.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/shopping-cart-rounded.svg
  pictographic-primitives/other/cart 1_3352f8c5-b764-483d-b1b4-cbbf08da871f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-angular-open-wheels.svg
  pictographic-primitives/other/circle colon_6a0ef6b0-613d-4883-ad08-e75fd510a4f6.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/circle-colon.svg
  pictographic-primitives/other/cog dollar_fa84ff77-a565-4df3-9360-0b7e9c3de772.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/cog-dollar.svg
  pictographic-primitives/other/device wearable vr goggles_1bc0a357-ae8c-5287-a849-d7b91c2e7aff.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-wearing-vr-headset.svg
  pictographic-primitives/other/doctor_709ecaa2-14b1-430d-9254-115ba73f6c42.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/doctor-wearing-medical-cap-batch-021-15.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 7 of 12. Redraw each of these 15 reference files in order. (tp:bb772b9b)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/double images_206fa313-37ee-4826-b03f-bda05b9a6f9d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/stacked-landscape-photo-gallery.svg
  pictographic-primitives/other/electric waves_e84a88d0-3ca7-4537-a4d9-b98932585c2f.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/wireless-signal-waves-batch-033.svg
  pictographic-primitives/other/file clock_0ef08051-f8cf-452c-9504-27f2eb99eb1b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/document-with-clock-symbol.svg
  pictographic-primitives/other/file code left_a7885b17-70fa-431a-8397-cf8f653fa82c.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/source-code-file.svg
  pictographic-primitives/other/file data bars_d48f86f5-12a6-47ce-a5d0-968db65faf5e.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/document-with-bar-chart.svg
  pictographic-primitives/other/file shield_4b6ec7ff-fa5a-4489-9bab-e1e940ac236f.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/file-shield.svg
  pictographic-primitives/other/folder file_d7b60535-d86c-4822-a2a7-f6c1499603fc.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/folder-file-solo.svg
  pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/female-person-pictogram-batch-023-02.svg, published/solo48/female-user-profile-icon-solo.svg
  pictographic-primitives/other/give hand 1_21f148ad-8725-429c-aa23-cad9257d7f13.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/open-helping-hand.svg
  pictographic-primitives/other/half globe_5ab3ac50-c850-4e2d-9757-c6093f013562.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/hemisphere-globe-batch-024-12.svg
  pictographic-primitives/other/hand holding_c1ff8321-3ac1-48fc-bdd4-880798eeea3c.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/two-open-cupped-hands.svg
  pictographic-primitives/other/hanger_b8261937-d8d8-4ee2-83fd-5404997b0511.svg
    reviewer: manual fix requested
    current drawing: published/solo48/clothes-hanger.svg
  pictographic-primitives/other/head_66eefdff-ac9b-4760-951f-816ff21b1e05.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/human-head-side-profile-solo.svg
  pictographic-primitives/other/head_a6a05294-58e7-4c68-ad44-2ec3bff40327.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/head-in-profile-batch-025-07.svg
  pictographic-primitives/other/headphone_71ce4923-14d6-48ce-9ae4-686eac75200e.svg
    reviewer: marked Needs fix, no note; bad stroke drawn
    current drawing: published/solo48/headphones-with-rounded-earcups.svg, published/solo48/simple-music-headphones-solo.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 8 of 12. Redraw each of these 15 reference files in order. (tp:fad61968)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/hospital 1_d9212b2f-353c-4ae0-96bd-8e2bf060245f.svg
    reviewer: manual fix requested
    current drawing: published/solo48/hospital-building-batch-025-02.svg
  pictographic-primitives/other/house door open_3f4973e2-f775-4a1e-8ffa-b700409c92a7.svg
    reviewer: marked rejected, no note
    current drawing: published/solo48/house-with-open-door-batch-025-05.svg
  pictographic-primitives/other/house power_95e78717-28bd-4a88-951a-54d6ae9c18e6.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/house-power.svg
  pictographic-primitives/other/laptop dollar sign_e6666fd5-a646-4ccf-89c4-7931517ccd22.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/laptop-dollar-symbol.svg
  pictographic-primitives/other/message bubble person_f27e9ceb-3471-4f88-9ba7-afea584d2ef1.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/message-bubble-person.svg
  pictographic-primitives/other/mobile phone dollar sign_31035467-a6b8-4c8d-8d52-52dc236bc2c7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/mobile-phone-dollar-sign.svg
  pictographic-primitives/other/mobile phone qr code_de84ba40-054e-4737-9aee-c6a39715be64.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/mobile-phone-qr-code-scanner.svg
  pictographic-primitives/other/mobile phone small squares_de85edfc-1420-4097-b674-118748dbeac1.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/smartphone-with-app-icons.svg
  pictographic-primitives/other/needle_132f47bc-4c0e-4882-9b9d-93439d0723ca.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/threaded-sewing-needle.svg
  pictographic-primitives/other/note_4db84a45-4c16-4769-b6b7-4205d0a42357.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/note-solo.svg
  pictographic-primitives/other/pail_25f19f1b-73c5-4a9f-938c-3d8a86938aaf.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/utility-bucket-with-handle.svg
  pictographic-primitives/other/paw print_959794ae-1023-4273-a3cf-8add9155265b.svg
    reviewer: manual fix requested
    current drawing: published/solo48/four-toed-paw-print.svg
  pictographic-primitives/other/phone vertical_c77144a9-35d2-4377-bddd-6845d3a0bbad.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/vertical-telephone-handset-batch-032.svg, published/solo48/vertical-telephone-receiver.svg
  pictographic-primitives/other/poverty person_2739b613-55fd-4f47-af97-f5cf90cb523d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/seated-curled-person-solo-2739b613.svg
  pictographic-primitives/other/robot hand_449c7cfd-5f9c-48e0-b0b3-0622be2b53fa.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/open-robotic-hand.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 9 of 12. Redraw each of these 15 reference files in order. (tp:c210d174)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/other/samosa_fb2a2e58-efc6-41ca-9022-2f437cd1717f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/samosas-on-a-plate.svg
  pictographic-primitives/other/smart watch square euro sign_ac5e07e4-9e24-406e-8500-ef19796d1933.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/square-wristwatch-solo-ac5e07e4.svg
  pictographic-primitives/other/sync arrow_75f115c6-e249-48a1-aac9-f840b6e89c3e.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/circular-sync-arrows.svg
  pictographic-primitives/other/tape measure_89fb6fa1-89d3-4277-a364-d6e026cea6f2.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/retractable-tape-measure.svg
  pictographic-primitives/other/technology device smart band_240918de-1160-4292-9b40-49d0208b6170.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/fitness-band-on-wrist.svg
  pictographic-primitives/other/two users woman_f2eb39da-ca20-4f47-8b9c-8c8796ff574d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/woman-and-person-profile-icons-batch-033.svg
  pictographic-primitives/other/ui webpage bank_dd2e4d0c-a37f-4f00-aaeb-0f1973cb4cc5.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/browser-header-window-solo-dd2e4d0c.svg
  pictographic-primitives/other/vr headset 1_019edb66-6728-4e28-ae42-b3dcaedeee84.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/vr-headset-profile-solo-019edb66.svg
  pictographic-primitives/other/women_223acbcd-fc0d-46aa-a05a-cd4a9693b0b8.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/woman-head-avatar-batch-033.svg
  pictographic-primitives/other/women_d56550d9-6b05-4800-a322-0335dc878173.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/woman-with-bob-hair-batch-022-15.svg
  pictographic-primitives/outdoors/binoculars_c302c027-d345-469d-98e7-0e924b296946.svg
    reviewer: bad stroke drawn; marked Needs fix, no note
    current drawing: published/solo48/binoculars.svg, published/solo48/binoculars-with-large-front-lenses.svg
  pictographic-primitives/pets/dog head_eab5a9ed-7706-42c2-851d-b7c76c820840.svg
    reviewer: manual fix requested
    current drawing: published/solo48/dog-profile-circle-solo.svg
  pictographic-primitives/pets/dog_b76bd92a-2013-4017-bb60-03561982e9e9.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/sitting-dog-with-ground-line.svg
  pictographic-primitives/pets/dog_b82a8e4c-4496-539d-b448-cb99ae868dd5.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/bulldog-face.svg
  pictographic-primitives/pets/dog_bf29416e-316c-548b-9cc0-8b851d979c09.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/dog-catching-disc.svg, published/solo48/dog-catching-disc-raised-head.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 10 of 12. Redraw each of these 15 reference files in order. (tp:63031199)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/pets/dog_cd0aa2ec-ca07-513d-88f0-0566b2c9e3a4.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/sitting-dog-tucked-paw.svg
  pictographic-primitives/pets/dog_ebece14d-0743-5ed8-b6fd-65b38f33eb1c.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/standing-dog-side.svg
  pictographic-primitives/photography/battery_e3172eb9-da83-4f83-a7f8-416647bd23e6.svg
    reviewer: manual fix requested
    current drawing: published/solo48/battery-photography.svg
  pictographic-primitives/protection/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/helmet-protection.svg
  pictographic-primitives/protection/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.svg
    reviewer: manual fix requested
    current drawing: published/solo48/helmet-6b6d3305.svg
  pictographic-primitives/protection/helmet_83968c0b-0769-4e90-a1c4-33974d290536.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/helmet-83968c0b.svg
  pictographic-primitives/protection/shield_ba7b0c51-fe87-48cd-a5c0-eea81086a3a9.svg
    reviewer: bad stroke drawn; bad stroke drawn
    current drawing: published/solo48/shield-9d1518e9.svg, published/solo48/shield-ba7b0c51.svg
  pictographic-primitives/rewards/flag_8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/wheelchair-user-holding-a-flag.svg
  pictographic-primitives/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/server-choose.svg
  pictographic-primitives/shipping/box_25bec113-9501-56df-8f1c-88dce76cb03d.svg
    reviewer: manual fix requested
    current drawing: published/solo48/box-25bec113.svg
  pictographic-primitives/shopping/cart_0941fae4-611d-41dd-8f02-a68399a41448.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-open-wheels.svg
  pictographic-primitives/shopping/cart_4f97114c-a7e4-4f5d-935d-2b5d4711fb3f.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-rounded-basket.svg
  pictographic-primitives/shopping/shopping cart empty_265d771c-37ea-4a56-8f73-ffaf2094e77b.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-empty.svg
  pictographic-primitives/shopping/shopping cart_22ba9936-54d3-4de1-815f-e80d16f43ff1.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-right-grip-lower-rail.svg
  pictographic-primitives/shopping/shopping cart_76482251-1a3c-4ca3-b8db-13d73354b42d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/shopping-cart-large-open-wheels.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 11 of 12. Redraw each of these 15 reference files in order. (tp:eaa6dbb9)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/spas/sauna heat stone_e2e71463-3949-5bb1-825f-2b5f7009fede.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/sauna-heat-stone.svg
  pictographic-primitives/sports/yoga tree pose_cd308a08-5d16-5ba7-ba3b-4c7cff751329.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/tree-pose.svg
  pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/heart-message-77-solo.svg
  pictographic-primitives/symbol/se (text)_65ff17d5-d6f4-45f8-9685-b215f34e7ba1.svg
    reviewer: marked rejected, no note
    current drawing: published/solo48/se-text.svg
  pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg
    reviewer: marked Needs fix, no note; marked Needs fix, no note
    current drawing: published/solo48/thermometer-mercury.svg, published/solo48/vertical-temperature-measurement-gauge-batch-032.svg
  pictographic-primitives/technology/hyperloop_e2358ded-b54e-4d0e-8caf-4e7de6c2d7dc.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/hyperloop-pod.svg
  pictographic-primitives/transportation/bicycle_6ce17d6f-0a53-4eaa-b433-061d444307dc.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/minimal-bicycle.svg
  pictographic-primitives/transportation/bicycle_71cc0503-f8f3-434e-9c8e-e1524bb2498d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/bicycle-angled-handlebar.svg
  pictographic-primitives/transportation/bicycle_b43a6544-1e7b-481a-aad7-01ad2bdb307d.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/road-bicycle.svg
  pictographic-primitives/transportation/bike cargo back_697554f1-3afd-5c1d-87a3-50b358ece127.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/cargo-bicycle-rear-box.svg
  pictographic-primitives/transportation/car_1fdb13eb-bc4d-44a6-bca4-d87dd2adb768.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/sedan-silhouette.svg
  pictographic-primitives/transportation/car_38792ded-1850-5f89-8b9a-dc4c3354c564.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/car-transportation.svg
  pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg
    reviewer: bad stroke drawn; bad stroke drawn
    current drawing: published/solo48/car.svg, published/solo48/car-796e3289.svg
  pictographic-primitives/transportation/car_9d24ac7b-c494-5a05-b347-45c5044a4d57.svg
    reviewer: other: "Replace the straight top bar with the vehicle’s curved body outline."
    current drawing: published/solo48/atv-side-view.svg
  pictographic-primitives/transportation/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/car-e1ae9ac1.svg

- [ ] Run $primitive-make-ray to repair failed icons: reviewer marked Needs fix, batch 12 of 12. Redraw each of these 13 reference files in order. (tp:316326f8)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Do not reuse an earlier run: the reviewer rejected the drawing itself.
  Failure type for this batch: Reviewer Needs fix: the current drawing passes validation, but a reviewer rejected it. It is usually off-reference in shape, has bad strokes, or has wrong proportions. Render the reference and the current drawing side by side, apply the reviewer note when there is one, and redraw so it reads like the reference. It must still pass every check below.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/transportation/e scooter_5a173d3f-0f7b-4dcd-a49d-423f38bee3a7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/electric-kick-scooter.svg
  pictographic-primitives/transportation/truck_0ec7e42f-2776-5a70-a652-9140ef5c56c7.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/parcel-delivery-truck.svg
  pictographic-primitives/travel/crafts model plane_f7df912f-c801-53cc-a0b8-6bfbd3f5fdf8.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/slender-airliner-diagonal.svg
  pictographic-primitives/travel/plane 1_8fe19626-3dae-5f95-be02-4dbe10f65534.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/climbing-airplane-rounded-nose.svg
  pictographic-primitives/travel/plane_1a77b164-d1b5-40f6-89b4-9b211524fbb0.svg
    reviewer: other: "scale vertical the airplane's head"
    current drawing: published/solo48/airplane-top-view-swept-wings.svg
  pictographic-primitives/typeface/a_615e9ffb-b53e-40a6-9ba6-86b05b552fd0.svg
    reviewer: marked rejected, no note
    current drawing: published/solo48/a.svg
  pictographic-primitives/users/man podium_df91a888-ce29-4b72-a6a9-d9fd7c079490.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/man-at-podium.svg
  pictographic-primitives/users/neutral podium_1461f130-1461-5759-8ff2-8de25b9591b9.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/person-at-podium.svg
  pictographic-primitives/users/woman half_163a9d8d-9ccd-53b0-b145-c50822422f8c.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/woman-bust-long-hair.svg
  pictographic-primitives/users/woman podium_764d4993-c502-42d1-9520-e7dd676c9d28.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/woman-at-podium.svg
  pictographic-primitives/video-games/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.svg
    reviewer: bad stroke drawn
    current drawing: published/solo48/vr-headset.svg
  pictographic-primitives/video/video player adjust_e50dd243-25aa-43e1-a7df-40fa0e7aacf2.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/video-player-timeline-solo-e50dd243.svg
  pictographic-primitives/wayfinding/liquid detergent_9c232443-1304-41d8-b531-e6b54e649616.svg
    reviewer: marked Needs fix, no note
    current drawing: published/solo48/liquid-detergent-bottle.svg


## Done

- [x] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 4 of 11. Redraw each of these 15 reference files in order. (tp:49de58f8)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_32/recycling label_aec06f81-4835-4b96-93f1-57f1ca360f5e.svg
    failed: mic [tag-outline]: tag-outline and eyelet are 4.77817 apart on centerlines nearest (35.5, 19.5)<->(32.1213, 16.1213) (needs 8) | mic [tag-outline]: tag-outline and leaf are 4.93649 apart on centerlines nearest (27.3463, 27.6537)<->(30.8369, 31.1443) (needs 8)
    current drawing: published/failed/solo48/recycling-label.svg
  pictographic-primitives/_uncategorized_32/religion cao dai_77937bbd-92c4-4b29-ac40-52719ed0b6cd.svg
    failed: mic [triangle]: triangle and eye are 1.78885 apart on centerlines nearest (11.4, 31.2)<->(13, 32) (needs 8) | mic [triangle]: triangle and iris are 7 apart on centerlines nearest (24, 42)<->(24, 35) (needs 8) (+1 more)
    current drawing: published/failed/solo48/religion-cao-dai.svg
  pictographic-primitives/_uncategorized_32/remote access_c9953fdc-3825-4f26-8597-533126256825.svg
    failed: mic [inner]: inner and center are 5 apart on centerlines nearest (24, 16)<->(24, 21) (needs 8)
    current drawing: published/failed/solo48/remote-access.svg
  pictographic-primitives/_uncategorized_32/retouch landscape_9bf20118-a278-4080-979f-4ea937240a2a.svg
    failed: mic [small-mountain]: small-mountain and sun are 5.24621 apart on centerlines nearest (18, 29)<->(16.7289, 23.9101) (needs 8) | mic [frame]: frame and wand are 2 apart on centerlines nearest (42, 26)<->(42, 24) (needs 8) (+7 more)
    also: undersized holes
    current drawing: published/failed/solo48/retouch-landscape.svg
  pictographic-primitives/_uncategorized_33/road lock_ea945a43-10ca-4ee5-a157-515c7b4149fa.svg
    failed: mic [body]: body and road-dash are 4 apart on centerlines nearest (24, 44)<->(24, 40) (needs 8)
    current drawing: published/failed/solo48/road-lock.svg
  pictographic-primitives/_uncategorized_33/robot wifi 5g_30dfa027-64b7-4bea-957e-c1a147e61020.svg
    failed: mic [wifi-outer]: wifi-outer and wifi-inner are 7.82223 apart on centerlines nearest (6, 10)<->(11.0362, 15.9853) (needs 8) | mic [wifi-inner]: wifi-inner and arm-top are 5.17647 apart on centerlines nearest (18, 18)<->(20.436, 22.5675) (needs 8)
    current drawing: published/failed/solo48/robot-wifi-5g.svg
  pictographic-primitives/_uncategorized_33/romance heterosextual symbol_1bf5b8f8-1714-40eb-bf12-43026ede4d1e.svg
    failed: mic [ring]: ring and heart are 7.29086 apart on centerlines nearest (32.9694, 14.3015)<->(27.2493, 18.8222) (needs 8) | mic [ring]: ring and male-shaft are 0.142136 apart on centerlines nearest (31.8995, 13.1005)<->(32, 13) (needs 8) (+2 more)
    also: undersized holes
    current drawing: published/failed/solo48/romance-heterosextual-symbol.svg
  pictographic-primitives/_uncategorized_33/romance pride gay lgbt heart_c0e31e5f-9872-4414-9334-38d9e1e42539.svg
    failed: mic [rainbow-2]: rainbow-2 and heart are 4.2368 apart on centerlines nearest (32, 28)<->(29.6825, 31.5468) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/romance-pride-gay-lgbt-heart.svg
  pictographic-primitives/_uncategorized_33/rss_bb8fc343-a336-4027-84fb-5394db05a944.svg
    failed: mic [badge]: badge and dot are 6 apart on centerlines nearest (14, 42)<->(14, 36) (needs 8)
    current drawing: published/failed/solo48/rss.svg
  pictographic-primitives/_uncategorized_33/sass circle logo_b60b81a4-9d88-4566-84d3-7931d6c1da67.svg
    failed: mic [badge]: badge and script are 5.81022 apart on centerlines nearest (14.292, 41.4855)<->(17.1248, 36.4126) (needs 8)
    current drawing: published/failed/solo48/sass-circle-logo.svg
  pictographic-primitives/_uncategorized_33/saving bear increase_b70b7993-149f-4dd9-95d6-fe029f2c8b42.svg
    failed: mic [trend]: trend and bear are 4.47022 apart on centerlines nearest (12.3955, 16.6045)<->(15.5564, 19.7654) (needs 8) | mic [bear]: bear and muzzle are 0.499997 apart on centerlines nearest (26.9982, 42)<->(27, 41.5) (needs 8) (+2 more)
    also: undersized holes
    current drawing: published/failed/solo48/saving-bear-increase.svg
  pictographic-primitives/_uncategorized_33/scooter parking shade roof_090386bc-ec29-43fe-9dba-5fd9ed1f0f5e.svg
    failed: mic [roof]: roof and seat are 5.81378 apart on centerlines nearest (6.4, 16.8)<->(9, 22) (needs 8) | mic [rear-wheel]: rear-wheel and seat are 7.4018 apart on centerlines nearest (11.9331, 32.1449)<->(10, 25) (needs 8) (+3 more)
    also: undersized holes
    current drawing: published/failed/solo48/scooter-parking-shade-roof.svg
  pictographic-primitives/_uncategorized_33/self driving car_7a8b5b6b-d72f-42df-9379-3389fd1e33fd.svg
    failed: mic [body]: body and headlight-0 are 5 apart on centerlines nearest (14, 26)<->(14, 31) (needs 8) | mic [body]: body and headlight-1 are 5 apart on centerlines nearest (34, 26)<->(34, 31) (needs 8) (+2 more)
    current drawing: published/failed/solo48/self-driving-car.svg
  pictographic-primitives/_uncategorized_33/seo search eye_4bd2f046-d00e-4c3d-99dd-153eae347474.svg
    failed: mic [lens]: lens and eye are 3.99985 apart on centerlines nearest (6.0003, 21.0346)<->(10, 21) (needs 8) | mic [eye]: eye and iris are 2.74989 apart on centerlines nearest (20.9758, 27.7498)<->(21, 25) (needs 8)
    current drawing: published/failed/solo48/seo-search-eye.svg
  pictographic-primitives/_uncategorized_34/share holder notification 2_57218de4-325d-49db-9661-2dd851d08161.svg
    failed: mic [bell-outline]: bell-outline and left-head are 5.54453 apart on centerlines nearest (14, 18)<->(12.0107, 23.1754) (needs 8) | mic [bell-outline]: bell-outline and center-head are 5 apart on centerlines nearest (24, 18)<->(24, 23) (needs 8) (+7 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/share-holder-notification-2.svg

- [x] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 3 of 11. Redraw each of these 15 reference files in order. (tp:60df3ae5)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_28/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg
    failed: mic [wifi-0]: wifi-0 and wifi-1 are 6.64772 apart on centerlines nearest (38, 12)<->(32.9322, 16.3023) (needs 8) | mic [wifi-1]: wifi-1 and wifi-2 are 5.66191 apart on centerlines nearest (34, 19)<->(29.1464, 21.9154) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/multiple-users-wifi.svg
  pictographic-primitives/_uncategorized_28/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg
    failed: mic [bubble]: bubble and pin are 2 apart on centerlines nearest (29, 30)<->(29, 28) (needs 8)
    current drawing: published/failed/solo48/navigation-smartphone-message.svg
  pictographic-primitives/_uncategorized_29/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg
    failed: mic [rim]: rim and petal-2 are 1.39855 apart on centerlines nearest (40.1284, 35.8262)<->(39, 35) (needs 8)
    current drawing: published/failed/solo48/onam-1.svg
  pictographic-primitives/_uncategorized_29/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg
    failed: mic [body]: body and medical-t are 1.50899 apart on centerlines nearest (35.3009, 30.5213)<->(35, 32) (needs 8) | mic [laptop]: laptop and medical-l are 4.66399 apart on centerlines nearest (27.0449, 38.4719)<->(31, 36) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/online-doctor-laptop-facetime.svg
  pictographic-primitives/_uncategorized_29/palate_d3ea8f6b-49cc-4787-9672-77eeeeac6b7b.svg
    failed: mic [palette]: palette and well-left are 7.995 apart on centerlines nearest (8.74459, 34.6343)<->(15.3371, 30.1111) (needs 8)
    current drawing: published/failed/solo48/kidney-shaped-paint-palette.svg
  pictographic-primitives/_uncategorized_30/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg
    failed: mic [fold]: fold and writing are 5.09902 apart on centerlines nearest (30, 14)<->(25, 15) (needs 8) | mic [seal]: seal and ribbon are 0.485281 apart on centerlines nearest (37.6569, 37.6569)<->(38, 38) (needs 8) (+1 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/patentee.svg
  pictographic-primitives/_uncategorized_30/pegboard_5ae49a1e-1226-441e-91e1-428676a4faba.svg
    failed: mic [board]: board and hole-15-15 are 6 apart on centerlines nearest (6, 15)<->(12, 15) (needs 8) | mic [board]: board and hole-24-15 are 6 apart on centerlines nearest (24, 6)<->(24, 12) (needs 8) (+26 more)
    current drawing: published/failed/solo48/nine-hole-square-pegboard.svg
  pictographic-primitives/_uncategorized_30/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg
    failed: mic [person-0-shoulders]: person-0-shoulders and arrow-left are 3.99946 apart on centerlines nearest (19.9989, 31.9346)<->(16, 32) (needs 8) | mic [person-1-shoulders]: person-1-shoulders and arrow-right are 3.99946 apart on centerlines nearest (28.0011, 31.9346)<->(32, 32) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/people-arrows.svg
  pictographic-primitives/_uncategorized_30/people conflict 3_e990e7ac-7a33-40af-9103-6dc2c867b7fd.svg
    failed: mic [left-skull]: left-skull and burst are 6 apart on centerlines nearest (14, 20)<->(14, 14) (needs 8)
    current drawing: published/failed/solo48/people-conflict-3.svg
  pictographic-primitives/_uncategorized_30/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg
    failed: mic [frame]: frame and fork-1 are 6 apart on centerlines nearest (42, 22)<->(36, 22) (needs 8) | holes/pinches: 2 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/permafrost.svg
  pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg
    failed: mic [plate]: plate and tile are 4 apart on centerlines nearest (22, 38)<->(26, 38) (needs 8) | holes/pinches: 1 undersized holes; 1 pinches
    also: pinches, undersized holes
    current drawing: published/failed/solo48/pesach-passover-2.svg
  pictographic-primitives/_uncategorized_30/picture sun_d8495254-20a2-4d70-a2c6-140b4f7cd24a.svg
    failed: mic [frame]: frame and ray-top are 4 apart on centerlines nearest (24, 6)<->(24, 10) (needs 8) | mic [frame]: frame and ray-left are 7 apart on centerlines nearest (6, 20)<->(13, 20) (needs 8) (+16 more)
    current drawing: published/failed/solo48/picture-sun.svg
  pictographic-primitives/_uncategorized_30/pin add_edc387fb-8345-489a-a276-38ea07c6e827.svg
    failed: mic [pin]: pin and plus-a are 6.87281 apart on centerlines nearest (24.3302, 28.1155)<->(30, 32) (needs 8) | holes/pinches: 1 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/pin-add.svg
  pictographic-primitives/_uncategorized_32/read world_707a74f4-f696-4ab1-aaf2-6be7de8a3c1a.svg
    failed: mic [book]: book and text-0 are 5.83722 apart on centerlines nearest (16.7833, 40.709)<->(18, 35) (needs 8) | mic [book]: book and text-1 are 5.2446 apart on centerlines nearest (34.49, 40.2217)<->(34, 35) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/read-world.svg
  pictographic-primitives/_uncategorized_32/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg
    failed: mic [document]: document and clock are 7 apart on centerlines nearest (8, 22)<->(15, 22) (needs 8) | mic [clock]: clock and hands are 4.99962 apart on centerlines nearest (24.0614, 13.0008)<->(24, 18) (needs 8) (+1 more)
    current drawing: published/failed/solo48/rectangle-history.svg

- [x] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 2 of 11. Redraw each of these 15 reference files in order. (tp:8b84e397)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_16/emoji gift lover hug 1_4de1746e-1e17-4608-9148-82107fed5099.svg
    failed: mic [face]: face and eye-19 are 6.71761 apart on centerlines nearest (15.2353, 8.27845)<->(18.5104, 14.1436) (needs 8) | mic [face]: face and eye-29 are 6.71761 apart on centerlines nearest (32.7647, 8.27845)<->(29.4896, 14.1436) (needs 8) (+4 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/smiling-face-hugging-ribboned-gift.svg
  pictographic-primitives/_uncategorized_16/engineer project superviser 1_9ec9ed06-396b-4bca-8680-e36e1ed302bf.svg
    failed: mic [head]: head and shoulders are 6 apart on centerlines nearest (24, 25)<->(24, 31) (needs 8) | mic [head]: head and plan-line are 5 apart on centerlines nearest (33, 16)<->(38, 16) (needs 8) (+1 more)
    current drawing: published/failed/solo48/engineering-project-supervisor.svg
  pictographic-primitives/_uncategorized_17/escalator descend person_ef26ac2a-67ca-4e82-9052-f1f383659603.svg
    failed: mic [torso]: torso and rail are 2.01948 apart on centerlines nearest (13, 34)<->(14.4682, 35.3866) (needs 8)
    current drawing: published/failed/solo48/person-on-descending-escalator.svg
  pictographic-primitives/_uncategorized_17/face awesome_236451ca-3512-494c-8c17-87481ad251f8.svg
    failed: mic [head]: head and star-0 are 7.46969 apart on centerlines nearest (6.43405, 14.4385)<->(13, 18) (needs 8) | mic [head]: head and star-1 are 7.46969 apart on centerlines nearest (41.566, 14.4385)<->(35, 18) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/smiling-star-eyed-face.svg
  pictographic-primitives/_uncategorized_17/face dizzy_aa0c1f8e-f7ca-4bf9-adf6-7f6f74e5b90a.svg
    failed: mic [head]: head and spiral-0 are 1.74497 apart on centerlines nearest (4.58247, 19.2097)<->(6.27771, 19.6233) (needs 8) | mic [head]: head and spiral-1 are 1.74497 apart on centerlines nearest (43.4175, 19.2097)<->(41.7223, 19.6233) (needs 8) (+4 more)
    current drawing: published/failed/solo48/dizzy-face-with-spiral-eyes.svg
  pictographic-primitives/_uncategorized_18/face smile hearts_9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg
    failed: mic [heart]: heart and eye-0 are 5.73334 apart on centerlines nearest (23.2397, 12.2432)<->(19.2076, 16.3192) (needs 8) | mic [heart]: heart and eye-1 are 5.73334 apart on centerlines nearest (24.7603, 12.2432)<->(28.7924, 16.3192) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/heart-shaped-face-with-heart-eyes.svg
  pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg
    failed: mic [head]: head and spiral-0 are 1.74497 apart on centerlines nearest (4.58247, 19.2097)<->(6.27771, 19.6233) (needs 8) | mic [head]: head and spiral-1 are 1.74497 apart on centerlines nearest (43.4175, 19.2097)<->(41.7223, 19.6233) (needs 8) (+2 more)
    current drawing: published/failed/solo48/dizzy-hypnotized-face.svg
  pictographic-primitives/_uncategorized_20/genie_f9d2a78b-2eb0-40a5-bcec-c567992dd9f2.svg
    failed: mic [mustache-left]: mustache-left and torso are 8 apart on centerlines nearest (24, 20)<->(24, 28) (needs 8)
    current drawing: published/failed/solo48/genie-with-turban-and-curling-body-batch-051.svg
  pictographic-primitives/_uncategorized_21/grandpa_2e10b85b-424e-4558-b38e-c8c3b76d9e52.svg
    failed: mic [head]: head and glasses-left are 0.917201 apart on centerlines nearest (9.4565, 13.3303)<->(10.288, 13.7173) (needs 8) | mic [jaw]: jaw and frown are 7.05548 apart on centerlines nearest (16.8665, 34.3215)<->(20, 28) (needs 8) (+1 more)
    current drawing: published/failed/solo48/bespectacled-bust-with-downturned-facial-arc.svg
  pictographic-primitives/_uncategorized_27/mastoid_5fe7f155-57d9-4703-a38c-886ec75e5bc6.svg
    failed: mic [outer]: outer and fold are 7.86126 apart on centerlines nearest (10, 18)<->(17.7252, 19.4564) (needs 8)
    current drawing: published/failed/solo48/ear-with-deep-inner-fold-and-rounded-lobe.svg
  pictographic-primitives/_uncategorized_27/messages bubble text_b43ae04a-1ea7-48c8-9d78-6d2f1fe1a195.svg
    failed: mic [speech-bubble]: speech-bubble and text-top are 7.50629 apart on centerlines nearest (30.0612, 14.4566)<->(25, 20) (needs 8) | mic [speech-bubble]: speech-bubble and text-bottom are 7.27324 apart on centerlines nearest (16.1, 30.3)<->(23, 28) (needs 8)
    current drawing: published/failed/solo48/circular-message-badge.svg
  pictographic-primitives/_uncategorized_27/module four_8c0da42a-e577-481a-a50e-84f0e8648aae.svg
    failed: mic [front-edge]: front-edge and stud-3 are 2.41404 apart on centerlines nearest (21.2179, 28.8871)<->(22.1144, 26.6458) (needs 8) | mic [stud-0]: stud-0 and stud-1 are 5.68724 apart on centerlines nearest (20.6741, 12.6667)<->(16.378, 16.3933) (needs 8) (+5 more)
    also: pinches, undersized holes
    current drawing: published/failed/solo48/module-four.svg
  pictographic-primitives/_uncategorized_27/money bags_facf19d7-e5b7-4559-806e-6d1d682ef4d0.svg
    failed: mic [small-bag-crown]: small-bag-crown and dollar are 7.21382 apart on centerlines nearest (19, 21)<->(23.4727, 26.6599) (needs 8) | mic [front-bag-tie]: front-bag-tie and dollar are 6 apart on centerlines nearest (27, 18)<->(27, 24) (needs 8) (+1 more)
    also: undersized holes
    current drawing: published/failed/solo48/two-dollar-money-bags.svg
  pictographic-primitives/_uncategorized_27/monitoring activity tracking 2_3932acf9-d8a9-4dab-a9e2-4e0a52270bc7.svg
    failed: mic [lens]: lens and foot-left-sole are 4.062 apart on centerlines nearest (13.1394, 7.67255)<->(15.059, 11.2524) (needs 8) | mic [lens]: lens and foot-right-sole are 2.96996 apart on centerlines nearest (30, 30)<->(27.7274, 28.0879) (needs 8) (+7 more)
    also: undersized holes
    current drawing: published/failed/solo48/magnifying-glass-footprints.svg
  pictographic-primitives/_uncategorized_27/monster_154635b8-1d1c-444f-931c-c6c0d2a48acc.svg
    failed: mic [body]: body and brow-left are 7 apart on centerlines nearest (14, 23)<->(21, 23) (needs 8) | mic [body]: body and brow-right are 7 apart on centerlines nearest (34, 23)<->(27, 23) (needs 8) (+6 more)
    current drawing: published/failed/solo48/angry-horned-monster-with-raised-arms.svg

- [x] Run $primitive-make-ray to repair failed icons: part spacing under 8, batch 1 of 11. Redraw each of these 15 reference files in order. (tp:a2f635c4)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Part spacing: two distinct parts are closer than 8 units between centerlines (ink clearance 4). Give every gap at least 8, or truly join the parts (shared endpoint plus relate('connect')), or merge or drop the minor part. A mark between two walls needs a 16-unit band, or 17 if a wall is curved. Never squeeze.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_02/amazon mq_14a3a91e-9beb-47ca-9999-bd7a4d5e5429.svg
    failed: mic [ring-0]: ring-0 and ring-1 are 8 apart on centerlines nearest (40, 20)<->(40, 28) (needs 8)
    current drawing: published/failed/solo48/square-centered-ring-network.svg
  pictographic-primitives/_uncategorized_02/amazon web service codepipeline 1_12be411f-98cd-4c43-b650-b16b090dc516.svg
    failed: mic [left-rail]: left-rail and left-chevron are 5 apart on centerlines nearest (6, 24)<->(11, 24) (needs 8) | mic [right-rail]: right-rail and right-chevron are 5 apart on centerlines nearest (42, 24)<->(37, 24) (needs 8) (+2 more)
    current drawing: published/failed/solo48/amazon-web-service-codepipeline-1.svg
  pictographic-primitives/_uncategorized_04/astronomy eclipse_6d179933-acab-43ec-bf9b-e0d73eebedfc.svg
    failed: mic [front]: front and rear are 1.88874 apart on centerlines nearest (27.1612, 38.3078)<->(28, 40) (needs 8)
    current drawing: published/failed/solo48/overlapping-eclipse-disks.svg
  pictographic-primitives/_uncategorized_04/astronomy planet saturn 1_d3179da3-e2e2-4329-8932-7b3c8044a535.svg
    failed: mic [planet]: planet and edge-on-ring are 0 apart on centerlines nearest (11.2721, 36.7279)<->(11.2721, 36.7279) (needs 8)
    current drawing: published/failed/solo48/planet-with-diagonal-ring-solo.svg
  pictographic-primitives/_uncategorized_04/athletics running 1_bbab0c61-cd66-44e3-8954-bcb31ddc3d23.svg
    failed: mic [outer]: outer and arrowhead are 8 apart on centerlines nearest (34, 40)<->(34, 32) (needs 8) | mic [inner]: inner and arrowhead are 8 apart on centerlines nearest (34, 17)<->(34, 25) (needs 8)
    current drawing: published/failed/solo48/running-track-curve-arrow.svg
  pictographic-primitives/_uncategorized_04/auto pilot car radius_8a6f5388-93e2-4e87-bb21-8db3666f5c20.svg
    failed: mic [sensor-0-0-inner]: sensor-0-0-inner and body are 4.47214 apart on centerlines nearest (18, 14)<->(20, 18) (needs 8) | mic [sensor-0-1-outer]: sensor-0-1-outer and body are 7.07107 apart on centerlines nearest (6, 30)<->(13, 29) (needs 8) (+4 more)
    current drawing: published/failed/solo48/autonomous-car-sensor-signal.svg
  pictographic-primitives/_uncategorized_05/avatar piracy laptop_aa4f64c4-a374-44b3-9890-7cd9bfe00eab.svg
    failed: mic [hat]: hat and beard are 7.58835 apart on centerlines nearest (30.7222, 20)<->(30.7222, 27.5883) (needs 8) | holes/pinches: 2 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/bearded-pirate-behind-a-laptop.svg
  pictographic-primitives/_uncategorized_05/babe_4601d69f-9445-41fa-8190-2bd52b395af7.svg
    failed: mic [face]: face and smile are 6.15664 apart on centerlines nearest (20.3207, 16.0768)<->(22, 22) (needs 8)
    current drawing: published/failed/solo48/smiling-woman-with-shoulder-length-hair.svg
  pictographic-primitives/_uncategorized_05/baggage weight_ee2a071e-6904-4d7d-a879-a7315aec3bd6.svg
    failed: mic [dial]: dial and needle are 5.17118 apart on centerlines nearest (29.6114, 6.29882)<->(26, 10) (needs 8)
    current drawing: published/failed/solo48/baggage-weight.svg
  pictographic-primitives/_uncategorized_06/bike parking 2_7eea5c25-9b41-4dec-ba5e-91b557120a37.svg
    failed: mic [wheel-36]: wheel-36 and frame are 3.80382 apart on centerlines nearest (28.7681, 28.5796)<->(25.3144, 26.9855) (needs 8) | holes/pinches: 3 undersized holes; 1 pinches
    also: pinches, undersized holes
    current drawing: published/failed/solo48/angled-handlebar-road-bicycle.svg
  pictographic-primitives/_uncategorized_10/caviar_e625a592-a7be-4a88-9cc8-1a1640f52612.svg
    failed: mic [egg-0]: egg-0 and egg-1 are 2.42224 apart on centerlines nearest (20.6666, 16.9888)<->(19.3334, 19.0112) (needs 8) | mic [egg-0]: egg-0 and egg-2 are 2.42224 apart on centerlines nearest (27.3334, 16.9888)<->(28.6666, 19.0112) (needs 8) (+4 more)
    also: undersized holes
    current drawing: published/failed/solo48/pyramid-of-round-caviar-eggs.svg
  pictographic-primitives/_uncategorized_12/conversation smile type 1_32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c.svg
    failed: mic [back]: back and smile are 6.71692 apart on centerlines nearest (21.3629, 32.8838)<->(20.5615, 26.2148) (needs 8) | mic [front]: front and eye-24 are 6.81192 apart on centerlines nearest (27.8537, 21.617)<->(24, 16) (needs 8) (+1 more)
    current drawing: published/failed/solo48/round-smiling-speech-bubble-pair.svg
  pictographic-primitives/_uncategorized_13/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg
    failed: mic [lower-band]: lower-band and small-band are 1.31961 apart on centerlines nearest (24, 40)<->(24.4965, 38.7774) (needs 8) | holes/pinches: 2 undersized holes; 0 pinches
    also: undersized holes
    current drawing: published/failed/solo48/crowdin-logo.svg
  pictographic-primitives/_uncategorized_16/elemental mediaconnect 1_6b152715-10e9-4683-860f-3b5e258f19e4.svg
    failed: mic [link-left]: link-left and left-node are 4.47214 apart on centerlines nearest (10, 18)<->(8, 22) (needs 8) | mic [link-right]: link-right and right-node are 4.47214 apart on centerlines nearest (38, 18)<->(40, 22) (needs 8) (+3 more)
    current drawing: published/failed/solo48/connected-hexagon-network-arrow.svg
  pictographic-primitives/_uncategorized_16/emoji gaming lover hug 1_b0db5c05-63ca-4bad-830f-6a24ddb21cb3.svg
    failed: mic [face]: face and eye-19 are 7.32341 apart on centerlines nearest (14.4245, 8.75859)<->(18.3045, 14.9697) (needs 8) | mic [face]: face and eye-29 are 7.32341 apart on centerlines nearest (33.5755, 8.75859)<->(29.6955, 14.9697) (needs 8) (+1 more)
    current drawing: published/failed/solo48/smiling-face-behind-game-controller.svg

- [x] Run $primitive-make-ray to repair failed icons: near-miss symmetry, batch 1 of 1. Redraw each of these 4 reference files in order. (tp:04b18317)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Near-miss symmetry: the ink is about 98% mirrored but the centerlines are off by under 1 unit. Either make the subject exactly symmetric (shared axis, mirrored coordinates, equal radii) or make any asymmetry deliberate and clearly larger.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_16/duplicate column_90da22c6-273c-4d21-a1a8-a6cfb89b48b6.svg
    failed: symmetry [arrow-head-1]: ink is 98.02% mirrored about vertical axis 24, but centerline differs by 1.41421 units near [25.0, 21.0] | symmetry [arrow-head-2]: ink is 98.02% mirrored about vertical axis 24, but centerline differs by 1.41421 units near [25.0, 27.0]
    current drawing: published/failed/solo48/duplicate-table-column.svg
  pictographic-primitives/_uncategorized_35/square sliders_38f5f3f1-85e8-450a-a8ab-23c97cd150d2.svg
    failed: mic [knob-0]: knob-0 and left-1 are 6 apart on centerlines nearest (21, 18)<->(21, 24) (needs 8) | mic [knob-1]: knob-1 and right-2 are 6 apart on centerlines nearest (27, 26)<->(27, 32) (needs 8) (+6 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/square-sliders.svg
  pictographic-primitives/animals/lion_9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad.svg
    failed: symmetry [face]: ink is 98.19% mirrored about vertical axis 24, but centerline differs by 0.931868 units near [20.0, 28.0]
    current drawing: published/failed/solo48/lion.svg
  pictographic-primitives/outdoors/outdoors fire camp_5a6bc318-1415-407d-8cee-66dc95d8d15f.svg
    failed: symmetry [fire-left]: ink is 98.95% mirrored about vertical axis 24, but centerline differs by 0.442642 units near [26.13897727382034, 9.86102272617966] | symmetry [fire-tip]: ink is 98.95% mirrored about vertical axis 24, but centerline differs by 0.442642 units near [21.548027441044795, 9.548027441044798]
    current drawing: published/failed/solo48/outdoors-fire-camp.svg

- [x] Run $primitive-make-ray to repair failed icons: keyshape bounds, batch 3 of 3. Redraw each of these 8 reference files in order. (tp:89c7b1c6)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/health/autism disorder symptoms_4a264e06-6d44-57cc-8176-d57369c6c0ee.svg
    failed: canvas/keyshape bounds: visible ink (4, 3.98075, 44, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0193, 0.0, 0.0], tolerance 0.0) | mic [profile]: parallel straight edges forehead-top and piece-right-1 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+2 more)
    also: parallel edges too close, part spacing under 8
    current drawing: published/failed/solo48/autism-disorder-symptoms.svg
  pictographic-primitives/interface-essential/web form progress_93ee9247-04b8-4aa1-b24d-f007fa02d450.svg
    failed: canvas/keyshape bounds: visible ink (2, 16, 46, 32) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.0, 8.0, 0.0, 8.0], tolerance 0.0)
    current drawing: published/failed/solo48/web-form-progress.svg
  pictographic-primitives/messages/sign language thank you_98f6fd32-ffa9-4713-85d4-721b3399c95c.svg
    failed: canvas/keyshape bounds: visible ink (3.78127, 4, 48, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.2187, 0.0, 4.0, 0.0], tolerance 0.0) | mic [index-side]: index-side and middle-left are 0.196116 apart on centerlines nearest (19.8077, 15.9615)<->(20, 16) (needs 8) (+9 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/sign-language-thank-you.svg
  pictographic-primitives/rating/rating star three_cf0d9970-8b38-5723-b109-a3be9696acdb.svg
    failed: mic [star-0]: star-0 and star-1 are 2 apart on centerlines nearest (16, 20)<->(18, 20) (needs 8) | mic [star-1]: star-1 and star-2 are 2 apart on centerlines nearest (30, 20)<->(32, 20) (needs 8) (+4 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/three-star-rating-row.svg, published/failed/solo48/three-star-rating-row-v2.svg
  pictographic-primitives/sports/sport curling_8032e556-8b26-54fa-ba05-e7108d122eaf.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 44.1803) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.1803], tolerance 0.0) | mic [stone-side]: stone-side and broom-head are 3.19211 apart on centerlines nearest (10, 36)<->(13.1291, 36.631) (needs 8) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/sport-curling.svg
  pictographic-primitives/video-games/batch-04/gaming award_17c7d2fd-712c-4723-bb68-d76fbbb8bbd0.svg
    failed: canvas/keyshape bounds: visible ink (3.94972, 4, 44.0503, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0503, 0.0, 0.0503, 0.0], tolerance 0.0) | mic [left-stem]: left-stem and left-leaf1 are 3.90155 apart on centerlines nearest (12.7034, 21.0209)<->(8.90216, 21.8999) (needs 8) (+6 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/gaming-award.svg
  pictographic-primitives/video-games/batch-09/roleplay game poisonous dagger knife_3e8bfa80-059e-487c-bda0-70b3d4ddf001.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44.4025, 45) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.4025, 1.0], tolerance 0.0) | mic [dagger]: dagger and drop are 4.92262 apart on centerlines nearest (31, 22)<->(35.772, 23.2084) (needs 8) (+9 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/roleplay-game-poisonous-dagger-knife.svg
  pictographic-primitives/video-games/batch-11/team vs team mode_5bac2074-ad7e-4c93-acd8-d73142b163b6.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 43.8114) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.1886], tolerance 0.0) | mic [controller]: parallel straight edges controller-0 and controller-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/team-vs-team-mode.svg

- [x] Run $primitive-make-ray to repair failed icons: keyshape bounds, batch 2 of 3. Redraw each of these 15 reference files in order. (tp:b37c2912)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_18/face woozy_fe974dc7-4d81-41d1-9dba-73ed68ac785f.svg
    failed: canvas/keyshape bounds: visible ink reaches radius 25.4307 about (24, 24), outside the CIRCLE radius 22.0 | mic [eye-left]: eye-left and star are 1.41421 apart on centerlines nearest (14, 22)<->(13, 21) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/woozy-face-floating-star.svg
  pictographic-primitives/_uncategorized_18/factory building eco friendly 3_f782aaea-ece3-4563-802f-f0a5558305f6.svg
    failed: canvas/keyshape bounds: visible ink (2, 3, 46, 42) does not match the HRECT_L envelope (2, 6, 46, 42) (deltas [0.0, 3.0, 0.0, 0.0], tolerance 0.0) | mic [stem]: stem and leaf-right are 0.784485 apart on centerlines nearest (29.2986, 11.9098)<->(30.0752, 12.0207) (needs 8) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/eco-friendly-building-plant.svg
  pictographic-primitives/_uncategorized_18/family hold_1123c19a-08d6-416a-bfa1-beb497d65c19.svg
    failed: canvas/keyshape bounds: visible ink (2, 6, 45, 43) does not match the HRECT_L envelope (2, 6, 46, 42) (deltas [0.0, 0.0, 1.0, 1.0], tolerance 0.0) | mic [adult-left]: adult-left and body-left are 7.30601 apart on centerlines nearest (12.5869, 15.9567)<->(13.6987, 23.1776) (needs 8) (+5 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/hand-supporting-family.svg
  pictographic-primitives/_uncategorized_28/nun_2e67f3b7-0bac-4846-8d2b-bc6d88672024.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 45) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 1.0], tolerance 0.0) | mic [shoulders]: parallel straight edges shoulder-top and cross-l are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: parallel edges too close
    current drawing: published/failed/solo48/nun.svg
  pictographic-primitives/_uncategorized_28/ocd disorder symptoms 2_9bf327e4-22cd-4f46-a740-34545d603a6f.svg
    failed: canvas/keyshape bounds: visible ink (6, 2, 42, 46) does not match the VRECT_L envelope (6, 2, 42, 46) (deltas [0.0, 0.0, 0.0, 0.0], tolerance 0.0) | mic [profile-top]: parallel straight edges neck-back and empty-box-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: parallel edges too close, part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/ocd-disorder-symptoms-2.svg
  pictographic-primitives/_uncategorized_30/passport globe_df632f40-c8e3-4ae9-9986-caca559c4210.svg
    failed: canvas/keyshape bounds: visible ink (4.41527, 4.25955, 44, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.4153, 0.2595, 0.0, 0.0], tolerance 0.0) | mic [passport]: parallel straight edges passport-6 and continent-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal) (+4 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/passport-globe.svg
  pictographic-primitives/_uncategorized_30/pepper hot_1b9c1a21-5633-4aac-a5fa-db87094b0bc1.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44.2076, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.2076, 0.0], tolerance 0.0) | mic [flame]: parallel straight edges flame-2 and flame-4 are 7.07107 apart on centerlines (ink gap 3.07107); requires at least 8 centerline / 4 ink (overlap-fallback) (+1 more)
    also: parallel edges too close, part spacing under 8
    current drawing: published/failed/solo48/pepper-hot.svg
  pictographic-primitives/_uncategorized_33/safety fire right_10fe00ef-bdce-47d7-95cd-4727e2fc9f1a.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 44.0494) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.0494], tolerance 0.0) | mic [arrow]: parallel straight edges arrow-7 and arrow-5 are 2.82843 apart on centerlines (ink gap -1.17157); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/safety-fire-right.svg
  pictographic-primitives/_uncategorized_35/spellbook_4a5d4a34-afe6-4020-b1fa-c429eb47cc78.svg
    failed: canvas/keyshape bounds: visible ink (4, 4.5, 44, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.5, 0.0, 0.0], tolerance 0.0) | mic [outer]: outer and star are 2 apart on centerlines nearest (6, 22)<->(8, 22) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/spellbook.svg
  pictographic-primitives/_uncategorized_38/trading learning 3_0e825ec7-4e16-4b31-8f5e-172f49f26a63.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44.0335, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0335, 0.0], tolerance 0.0)
    current drawing: published/failed/solo48/trading-learning-3.svg
  pictographic-primitives/_uncategorized_39/video game controller monitor_861e17b0-a761-4ce1-aadb-ee4995755d3f.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 44.1803) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.1803], tolerance 0.0) | mic [monitor]: parallel straight edges monitor-6, monitor-5 and stand-foot-1, stand-foot-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink  (+4 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/video-game-controller-monitor.svg
  pictographic-primitives/_uncategorized_39/video game controller team_fb5ed3c8-9522-4523-9735-214910411c7e.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 43.1384) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.8616], tolerance 0.0) | mic [controller]: parallel straight edges controller-0 and d-pad-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+6 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/video-game-controller-team.svg
  pictographic-primitives/_uncategorized_39/video game controller wifi_36ec33e6-3587-4196-b433-a5ed4e77ad2d.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 43.1384) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.8616], tolerance 0.0) | mic [controller]: parallel straight edges controller-0 and d-pad-1 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: parallel edges too close, part spacing under 8, undersized holes
    current drawing: published/failed/solo48/video-game-controller-wifi.svg
  pictographic-primitives/crime/robbing_4d29ffb6-bda5-416a-be77-62a701e144e4.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44.4682, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.4682, 0.0], tolerance 0.0) | mic [money-stem]: parallel straight edges money-stem and victim-torso are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+7 more)
    also: parallel edges too close, part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/robbing.svg
  pictographic-primitives/food/food allegic vegan meal 1_588d68f8-b31a-4c4c-97e2-20473cedb4a3.svg
    failed: canvas/keyshape bounds: visible ink (3.03425, 3.03425, 45.0955, 45.0955) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.9657, 0.9657, 1.0955, 1.0955], toler | mic [slash]: slash and upper-leaves are 5.65685 apart on centerlines nearest (14, 14)<->(18, 10) (needs 8) (+5 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/food-allergen-free.svg

- [x] Run $primitive-make-ray to repair failed icons: keyshape bounds, batch 1 of 3. Redraw each of these 15 reference files in order. (tp:afae8ce3)
  Every file below was already drawn at least once (a registered model and/or an earlier primitive-make-ray or side-main-make-thuan run), and that drawing FAILED the check. It shows as "Drawn, unpublished" on gallery/primitives.html or "Needs fix" on gallery/side-mains.html. Do not skip a file because a result.json exists. Author a fresh run in a new RESULT_DIR for every file. Only skip a file when its newest existing run passes the build gate below with zero errors and zero warnings; report that file as done.
  Failure type for this batch: Keyshape bounds: the visible ink does not exactly match the chosen keyshape envelope (rectangles fit with tolerance 0; CIRCLE is radial). Choose the keyshape first, get its extremes from Keyshape.<TOKEN>.bounds_for(Profile.SOLO48), and design backwards so the outermost strokes sit exactly on the centerline box. Put arc centres on integer points with the apex at the endpoint so nothing overshoots or falls short.
  validate_icon() alone is NOT enough. It misses the build's hole/pinch, internal-spacing and symmetry gates, which is why earlier runs reported "valid" and still failed. Once validate_icon() is valid with zero warnings, also run `python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py --debug RESULT_DIR/gate` and require BUILD GATE PASS.
  Retry automatically. If either check fails, read the named element and coordinates (and the overlays in RESULT_DIR/gate), repair the Python model, and re-run both checks. Keep going for at least 5 repair rounds, following the repair ladder: enlarge the opening, rebalance, change the keyshape, simplify or drop a minor part. Stop only when both pass. Never weaken a rule, declare a false connect, add a FREE record, or hand-edit the SVG. Save the last gate output as RESULT_DIR/build-gate.txt and set "build_gate": "pass" or "fail" in result.json. If a file still fails after the retries, record the failing check and element as a blocker and continue with the next file. At the end, list each file as pass or blocked.
  Files (the earlier failure and current drawing are under each one):
  pictographic-primitives/_uncategorized_02/amazon eventbridge_34f87da9-e584-47f7-8fe0-ca66e9aa7da9.svg
    failed: canvas/keyshape bounds: visible ink (4, 0, 44, 48) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 4.0, 0.0, 4.0], tolerance 0.0) | mic [perimeter]: perimeter and event-bus are 7.31049 apart on centerlines nearest (40.6804, 21.0309)<->(34, 24) (needs 8) (+3 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/amazon-eventbridge.svg
  pictographic-primitives/_uncategorized_02/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg
    failed: canvas/keyshape bounds: visible ink (4, 3, 44, 46) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 1.0, 0.0, 2.0], tolerance 0.0) | mic [top]: parallel straight edges top-6 and top-3 are 7.15542 apart on centerlines (ink gap 3.15542); requires at least 8 centerline / 4 ink (midpoint-normal) (+10 more)
    also: parallel edges too close, part spacing under 8
    current drawing: published/failed/solo48/amazon-elemental-medialive.svg
  pictographic-primitives/_uncategorized_02/amazon web service marketplaces cart_b98df773-88b9-4b59-bf8f-31bdee2160b2.svg
    failed: canvas/keyshape bounds: visible ink (4, 3, 46, 45) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 1.0, 2.0, 1.0], tolerance 0.0) | mic [right]: parallel straight edges right-5 and left-2 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal) (+9 more)
    also: parallel edges too close, part spacing under 8
    current drawing: published/failed/solo48/amazon-web-service-marketplaces-cart.svg
  pictographic-primitives/_uncategorized_04/arduino plus minus_ed08c4ae-cd2f-485c-a2ad-1642f69c286c.svg
    failed: canvas/keyshape bounds: visible ink (2.25, 8, 45.75, 40) does not match the HRECT_M envelope (2, 8, 46, 40) (deltas [0.25, 0.0, 0.25, 0.0], tolerance 0.0) | mic [infinity]: infinity and minus are 5.74993 apart on centerlines nearest (4.25015, 23.9711)<->(10, 24) (needs 8) (+1 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/infinity-loop-with-plus-and-minus.svg
  pictographic-primitives/_uncategorized_04/astronomy telescope stars_4a8d494e-32cc-4073-96a3-0c1ca2d67952.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 46, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 2.0, 0.0], tolerance 0.0) | mic [eyepiece]: eyepiece and star-0 are 7.51356 apart on centerlines nearest (13.0515, 20.866)<->(10, 14) (needs 8) (+2 more)
    also: part spacing under 8, pinches, undersized holes
    current drawing: published/failed/solo48/telescope-between-two-stars.svg
  pictographic-primitives/_uncategorized_07/brain circuit_994c360d-a3ef-411d-83b6-1227713cc09e.svg
    failed: canvas/keyshape bounds: visible ink (4, 3.91837, 44, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0816, 0.0, 0.0], tolerance 0.0) | mic [brain]: brain and terminal-left are 7 apart on centerlines nearest (9, 20)<->(16, 20) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/circuit-brain-outline.svg
  pictographic-primitives/_uncategorized_15/do not throw trash toilet_7c784cb7-5aec-47a9-96ef-4c2afb98e94a.svg
    failed: canvas/keyshape bounds: visible ink (6, 4, 33, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [2.0, 0.0, 11.0, 0.0], tolerance 0.0) | mic [arm]: parallel straight edges arm-2 and toilet-3 are 3 apart on centerlines (ink gap -1); requires at least 8 centerline / 4 ink (midpoint-normal) (+5 more)
    also: parallel edges too close, part spacing under 8
    current drawing: published/failed/solo48/person-dropping-trash-into-toilet.svg
  pictographic-primitives/_uncategorized_15/donation care hands heart 1_c4776ceb-e74e-4923-a8f4-ac3c1635d4e5.svg
    failed: canvas/keyshape bounds: visible ink (3.73389, 4, 44.2661, 43) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.2661, 0.0, 0.2661, 1.0], tolerance 0.0) | mic [heart]: heart and right-arch are 2.8415 apart on centerlines nearest (29.0842, 9.54426)<->(29.9823, 6.84843) (needs 8) (+1 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/hands-holding-heart.svg
  pictographic-primitives/_uncategorized_16/ear listen_4317946e-a563-47b7-9c3d-e830b878ecc6.svg
    failed: canvas/keyshape bounds: visible ink (5.99951, 3.87445, 56, 44) leaves the 48x48 canvas | canvas/keyshape bounds: visible ink (5.99951, 3.87445, 56, 44) does not match the VRECT_L envelope (6, 2, 42, 46) (deltas [0.0005, 1.8744, 14.0, 2.0], tolerance 0.0) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/ear-with-sound-waves-solo.svg
  pictographic-primitives/_uncategorized_16/emoji care hug heart face_4376565b-9b1c-4d38-bc0d-e4819924e5d3.svg
    failed: canvas/keyshape bounds: visible ink (3.82868, 4, 44.1713, 44) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.1713, 0.0, 0.1713, 0.0], tolerance 0.0) | mic [face]: face and heart are 6.46847 apart on centerlines nearest (42, 24)<->(35.5368, 24.2602) (needs 8) (+6 more)
    also: part spacing under 8, pinches
    current drawing: published/failed/solo48/closed-eye-face-holding-heart.svg
  pictographic-primitives/_uncategorized_16/emoji smiling face open hands_4d157948-bac0-4b3b-b00b-4b00b21719a6.svg
    failed: canvas/keyshape bounds: visible ink (4, 4, 44, 44.4081) does not match the SQUARE envelope (4, 4, 44, 44) (deltas [0.0, 0.0, 0.0, 0.4081], tolerance 0.0) | mic [head]: head and left-hand are 3 apart on centerlines nearest (10, 22)<->(10, 25) (needs 8) (+5 more)
    also: part spacing under 8, undersized holes
    current drawing: published/failed/solo48/smiling-face-with-two-open-hands.svg
  pictographic-primitives/_uncategorized_17/face kiss beam_b020e38b-16c9-41eb-9970-ec2702be1b3c.svg
    failed: canvas/keyshape bounds: visible ink reaches radius 22.1478 about (24, 24), outside the CIRCLE radius 22.0 | mic [face]: face and eye-left are 7.63051 apart on centerlines nearest (4.58693, 19.1914)<->(12, 21) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/kissing-face-heart-beam.svg
  pictographic-primitives/_uncategorized_17/face kiss wink heart_465fa6c6-5f8b-4335-a186-c938fe764751.svg
    failed: canvas/keyshape bounds: visible ink reaches radius 22.1478 about (24, 24), outside the CIRCLE radius 22.0 | mic [face]: face and wink are 6.65796 apart on centerlines nearest (4.51289, 19.5014)<->(11, 21) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/kissing-face-wink-heart.svg
  pictographic-primitives/_uncategorized_17/face kiss_08de5c3e-418d-4732-b0b0-0789943abce3.svg
    failed: canvas/keyshape bounds: visible ink reaches radius 22.1478 about (24, 24), outside the CIRCLE radius 22.0 | mic [face]: face and eye-left are 7.35059 apart on centerlines nearest (5.03469, 17.6515)<->(12, 20) (needs 8) (+3 more)
    also: part spacing under 8
    current drawing: published/failed/solo48/kissing-face-heart.svg
  pictographic-primitives/_uncategorized_17/face party_db4dd436-0c1b-4e44-a5c2-fb12637a6682.svg
    failed: canvas/keyshape bounds: visible ink reaches radius 23.2603 about (24, 24), outside the CIRCLE radius 22.0 | mic [face]: face and horn are 3.23661 apart on centerlines nearest (43.0914, 29.9585)<->(40, 29) (needs 8)
    also: part spacing under 8
    current drawing: published/failed/solo48/celebration-face-party-horn.svg

- [x] Run $primitive-make-ray on side mains (not generated) batch 3 of 3: draw each of these 17 reference files in order. (tp:e7757dd5)
  Some of these already have a primitive-make-ray or side-main-make-thuan run. Do not skip a file because a result.json exists: author a fresh run in a new RESULT_DIR for every file, unless its newest existing run is already valid, in which case report it as done and move on.
  pictographic-primitives/computers/batch-06/monitor upload_0005e7b2-b6eb-47bb-9376-770c2522288d.svg
  pictographic-primitives/state/slash sperm_ff7e8050-8817-4660-b5a8-3ebce79568b0.svg
  pictographic-primitives/interface-essential/list numbers_b096a1c9-9eca-5c00-9ea3-878dc2c4ba9b.svg
  pictographic-primitives/other/self payment computer dollar_2c2ce02e-d93f-4086-969c-7135c5b08d1b.svg
  pictographic-primitives/office/business card_60032c95-543e-5926-8602-a22b2840c109.svg
  pictographic-primitives/messages/messages bubble square question_dd81b6db-6dd5-4927-8f6a-80c73d19c8cd.svg
  pictographic-primitives/video/video player_360a1d59-d44c-4d9c-9791-f0399e67d10a.svg
  pictographic-primitives/protection/protection shield_703647aa-6053-5e38-b352-06e55bc0fb70.svg
  pictographic-primitives/video/video player movie_585c392a-9c3f-4878-ad5b-8aae0e8bf5b5.svg
  pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg
  pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg
  pictographic-primitives/other/tv control next_99b37bd2-37e1-42f8-b918-e34adc73280d.svg
  pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg
  pictographic-primitives/typeface/A_79c9f630-25fd-42e0-b4e7-486218ea118b.svg
  pictographic-primitives/other/rectangle uv low_25e8dad2-374e-4a65-b6de-697a33714628.svg
  pictographic-primitives/video/video player movie_ea039057-d0a3-4e3b-a6b8-c3a23d0ade26.svg
  pictographic-primitives/other/ui webpage social profile_6765de1f-1adc-4a6a-bbb4-c497deffd007.svg

- [x] Run $primitive-make-ray on side mains (not generated) batch 2 of 3: draw each of these 15 reference files in order. (tp:85ea58d5)
  Some of these already have a primitive-make-ray or side-main-make-thuan run. Do not skip a file because a result.json exists: author a fresh run in a new RESULT_DIR for every file, unless its newest existing run is already valid, in which case report it as done and move on.
  pictographic-primitives/other/mobile phone bug_600bc5a2-131a-4e43-b134-f5e672684c21.svg
  pictographic-primitives/other/square woman_7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1.svg
  pictographic-primitives/travel/plane boarding pass_3911cfa6-22d7-4747-95a0-fced35ce7946.svg
  pictographic-primitives/travel/plane boarding pass_9cbe2481-852f-43a0-a967-6cc8e7df1295.svg
  pictographic-primitives/travel/plane 1_44d3d80b-4240-42cf-9ac4-2237f7c5d0aa.svg
  pictographic-primitives/money/crypto currency bitcoin_91a08a40-6b1a-44f8-90e3-1e362a296712.svg
  pictographic-primitives/phones/phone book_b18b4462-5e10-44fd-99e3-3fb256fb4f34.svg
  pictographic-primitives/work/task list plain_cbffa972-bda1-56ed-9c77-cf75b93eefd1.svg
  pictographic-primitives/interface-essential/time clock file 1_e7ce785e-158f-41d6-9e8b-dcba4879acac.svg
  pictographic-primitives/files/common file text_5aeb0892-b41b-5c32-97fe-0a13b74d6d80.svg
  pictographic-primitives/_uncategorized_12/coin_a07f9b96-a4e7-42f6-9db1-6cfe9d540507.svg
  pictographic-primitives/typeface/a_615e9ffb-b53e-40a6-9ba6-86b05b552fd0.svg
  pictographic-primitives/health/blood bag_7d002be2-8db0-591d-9e62-868a56fdf240.svg
  pictographic-primitives/health/prescription drug paper_e0b1e330-cc81-522c-9a29-44fd4f8881cf.svg
  pictographic-primitives/computers/batch-05/monitor download_7adf19ee-e35e-403f-8547-7156c16131ae.svg

- [x] Run $primitive-make-ray on side mains (not generated) batch 1 of 3: draw each of these 15 reference files in order. (tp:4febbdf1)
  Some of these already have a primitive-make-ray or side-main-make-thuan run. Do not skip a file because a result.json exists: author a fresh run in a new RESULT_DIR for every file, unless its newest existing run is already valid, in which case report it as done and move on.
  pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg
  pictographic-primitives/other/mobile phone wifi_a2e42ae3-1e50-4ab6-8845-45739f1e04ef.svg
  pictographic-primitives/other/smart watch circle pound sign_f2d45871-ff3d-44d5-84a8-774df3bd6ba3.svg
  pictographic-primitives/combination/smart watch circle dollar sign_6b9fab53-d945-4f18-86b9-fcc5bd5840ce.svg
  pictographic-primitives/combination/smart watch square yuan sign_130ae17c-e9b2-44fc-bcbf-03cd5a3dc1d9.svg
  pictographic-primitives/interface-essential/calendar check_7539933b-41e7-42c6-8893-c05af64c76c8.svg
  pictographic-primitives/interface-essential/calendar check_d38332cc-ed3e-4e29-835b-f24fbd23eb07.svg
  pictographic-primitives/programing/app window code_8f19f3cf-e4de-4237-b690-a9fa123f3e52.svg
  pictographic-primitives/other/mobile phone clock_49a79098-c0be-4d5e-8dd8-ff360a2a7d0d.svg
  pictographic-primitives/work/task list to do_d9177fba-2a20-515e-81aa-43f5ec22aeda.svg
  pictographic-primitives/mobile/3g_f5658962-8a89-5980-a105-1b899cfd5a20.svg
  pictographic-primitives/mobile/4g_760eff2b-e2a4-5207-9921-b55280c076a0.svg
  pictographic-primitives/other/5g (text)_0440d8eb-b611-409c-b5fd-71315e26622e.svg
  pictographic-primitives/money/crypto currency bitcoin_8fbdf83e-7f75-5f64-b826-fc7b55c55a27.svg
  pictographic-primitives/other/mobile phone key_45efdc96-5aab-49eb-ac68-b0e1ceb428c9.svg

