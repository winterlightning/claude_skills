# Batch 3: part-spacing repairs

All 15: `validate_icon()` valid and `BUILD GATE PASS`, zero errors and zero warnings. Native 48px and enlarged light/dark previews reviewed. Author: `gpt-6`. Standalone outputs only.

[Light/dark review sheet](batch3-review-sheet.png)

## 1. multiple users wifi — pass

Input: `pictographic-primitives/_uncategorized_28/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg`

[Run folder](a119cf45-d021-460f-b469-9d1f28774714/20260924-spacing-batch3/) · [SVG](a119cf45-d021-460f-b469-9d1f28774714/20260924-spacing-batch3/multiple-users-wifi.svg) · [Build gate](a119cf45-d021-460f-b469-9d1f28774714/20260924-spacing-batch3/build-gate.txt)

Three users under two Wi-Fi arcs.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: human_ref/user.svg; Lucide wifi nested arcs. Original and atomic-debug inspected.

Omissions: Drop one Wi-Fi arc; reduce heads to radius2.

Visual review: Shared bust shoulders join at actual endpoints. Head bottoms29, shoulder crests37: exact8 centerline /4 ink gap; symmetric x=24. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 2. navigation smartphone message — pass

Input: `pictographic-primitives/_uncategorized_28/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg`

[Run folder](9d04d41b-14a1-476d-b164-23e91f0672af/20260924-spacing-batch3/) · [SVG](9d04d41b-14a1-476d-b164-23e91f0672af/20260924-spacing-batch3/navigation-smartphone-message.svg) · [Build gate](9d04d41b-14a1-476d-b164-23e91f0672af/20260924-spacing-batch3/build-gate.txt)

A smartphone with a location message bubble.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide smartphone coherent enclosure; map-pin dome. Original and atomic-debug inspected.

Omissions: Drop home button and divider; enlarge bubble relative to phone.

Visual review: Pin is clear inside bubble; actual shared phone/bubble endpoints. Deliberate offset overlap. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 3. onam 1 — pass

Input: `pictographic-primitives/_uncategorized_29/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg`

[Run folder](7d27b436-d05f-41d3-b72f-2e31759f48e2/20260924-spacing-batch3/) · [SVG](7d27b436-d05f-41d3-b72f-2e31759f48e2/20260924-spacing-batch3/onam-1.svg) · [Build gate](7d27b436-d05f-41d3-b72f-2e31759f48e2/20260924-spacing-batch3/build-gate.txt)

A six-lobed Onam flower inside a circular rim.

Keyshape: CIRCLE. Circular rim, radius20 about (24,24).

Construction: Lucide flower coherent petal boundary. Original and atomic-debug inspected.

Omissions: Drop center hexagon and internal petal seams.

Visual review: Six smooth lobes mirror about both axes; rim and flower remain separated. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 4. online doctor laptop facetime — pass

Input: `pictographic-primitives/_uncategorized_29/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg`

[Run folder](bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265/20260924-spacing-batch3/) · [SVG](bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265/20260924-spacing-batch3/online-doctor-laptop-facetime.svg) · [Build gate](bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265/20260924-spacing-batch3/build-gate.txt)

A doctor beside a laptop.

Keyshape: HRECT_L. Wide composition, exact centerline box (4,8)-(44,40).

Construction: human_ref/user.svg; Lucide laptop tapered base. Original and atomic-debug inspected.

Omissions: Simplify laptop keyboard and reduce medical cross.

Visual review: Head bottom18 and shoulder crest26 give exact8 centerline /4 ink gap; head aligns with shoulder center33. Laptop arrangement intentionally asymmetric. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 5. palate — pass

Input: `pictographic-primitives/_uncategorized_29/palate_d3ea8f6b-49cc-4787-9672-77eeeeac6b7b.svg`

[Run folder](d3ea8f6b-49cc-4787-9672-77eeeeac6b7b/20260924-spacing-batch3/) · [SVG](d3ea8f6b-49cc-4787-9672-77eeeeac6b7b/20260924-spacing-batch3/kidney-shaped-paint-palette.svg) · [Build gate](d3ea8f6b-49cc-4787-9672-77eeeeac6b7b/20260924-spacing-batch3/build-gate.txt)

A kidney-shaped paint palette with circular wells.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide palette: separated wells and organic outline. Original and atomic-debug inspected.

Omissions: Reduce four paint wells to two.

Visual review: Move lower-left well inward one grid unit; preserve organic asymmetric notch and smooth outer silhouette. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 6. patentee — pass

Input: `pictographic-primitives/_uncategorized_30/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg`

[Run folder](64b0a542-67a6-4d92-8168-4adc3edbd214/20260924-spacing-batch3/) · [SVG](64b0a542-67a6-4d92-8168-4adc3edbd214/20260924-spacing-batch3/patentee.svg) · [Build gate](64b0a542-67a6-4d92-8168-4adc3edbd214/20260924-spacing-batch3/build-gate.txt)

A patent certificate with an award seal and ribbons.

Keyshape: VRECT_L. Upright composition, exact centerline box (8,4)-(40,44).

Construction: Lucide award open ribbon construction; file-clock interrupted page. Original and atomic-debug inspected.

Omissions: Drop writing, folded corner and ribbon notch.

Visual review: Seal has exact6-8-10 attachment nodes; both open ribbon tails genuinely join the seal. Intentional lower-right award placement. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 7. pegboard — pass

Input: `pictographic-primitives/_uncategorized_30/pegboard_5ae49a1e-1226-441e-91e1-428676a4faba.svg`

[Run folder](5ae49a1e-1226-441e-91e1-428676a4faba/20260924-spacing-batch3/) · [SVG](5ae49a1e-1226-441e-91e1-428676a4faba/20260924-spacing-batch3/nine-hole-square-pegboard.svg) · [Build gate](5ae49a1e-1226-441e-91e1-428676a4faba/20260924-spacing-batch3/build-gate.txt)

A square pegboard with nine perforation marks.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: No exact Lucide match; shared rounded-frame construction from image. Original and atomic-debug inspected.

Omissions: Replace tiny outlined holes with solid circular marks.

Visual review: Three-by-three pattern keeps equal pitch9 and centered alignment; rounded board. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 8. people arrows — pass

Input: `pictographic-primitives/_uncategorized_30/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg`

[Run folder](cd870bf9-9544-4c9b-a2dd-608effb82774/20260924-spacing-batch3/) · [SVG](cd870bf9-9544-4c9b-a2dd-608effb82774/20260924-spacing-batch3/people-arrows.svg) · [Build gate](cd870bf9-9544-4c9b-a2dd-608effb82774/20260924-spacing-batch3/build-gate.txt)

Two people with a bidirectional arrow beneath.

Keyshape: HRECT_L. Wide composition, exact centerline box (4,8)-(44,40).

Construction: human_ref/user.svg; Lucide users paired bust construction. Original and atomic-debug inspected.

Omissions: Smaller heads and shallower shoulders provide room for arrow.

Visual review: Head bottoms14 and shoulder crests22 give exact8 centerline /4 ink gap. Matched busts and arrow mirror about x=24. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 9. people conflict 3 — pass

Input: `pictographic-primitives/_uncategorized_30/people conflict 3_e990e7ac-7a33-40af-9103-6dc2c867b7fd.svg`

[Run folder](e990e7ac-7a33-40af-9103-6dc2c867b7fd/20260924-spacing-batch3/) · [SVG](e990e7ac-7a33-40af-9103-6dc2c867b7fd/20260924-spacing-batch3/people-conflict-3.svg) · [Build gate](e990e7ac-7a33-40af-9103-6dc2c867b7fd/20260924-spacing-batch3/build-gate.txt)

Two inward-facing human profiles beneath a conflict burst.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: human_ref/user.svg round cranium; source opposing profiles, no useful exact Lucide match. Original and atomic-debug inspected.

Omissions: Remove small mouth/jaw stair steps.

Visual review: Mirrored connected head/neck profiles; no detached-head gap applies. Broadened neck opening clears internal-spacing check. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 10. permafrost — pass

Input: `pictographic-primitives/_uncategorized_30/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg`

[Run folder](3f77b04c-ad63-443d-a816-599e467435a6/20260924-spacing-batch3/) · [SVG](3f77b04c-ad63-443d-a816-599e467435a6/20260924-spacing-batch3/permafrost.svg) · [Build gate](3f77b04c-ad63-443d-a816-599e467435a6/20260924-spacing-batch3/build-gate.txt)

A snowflake inside a rounded square.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide snowflake radial repeat definition. Original and atomic-debug inspected.

Omissions: Drop small branch forks; retain six radial arms.

Visual review: Six arms genuinely join at center24,24; balanced radial arrangement inside frame. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 11. pesach passover 2 — pass

Input: `pictographic-primitives/_uncategorized_30/pesach passover 2_8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef.svg`

[Run folder](8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef/20260924-spacing-batch3/) · [SVG](8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef/20260924-spacing-batch3/pesach-passover-2.svg) · [Build gate](8eb34e8a-c1a0-4770-a3b1-2f00e05fdaef/20260924-spacing-batch3/build-gate.txt)

A star plate beside a segmented Passover matzo.

Keyshape: HRECT_L. Wide composition, exact centerline box (4,8)-(44,40).

Construction: Source star plate and matzo. Original and atomic-debug inspected.

Omissions: Open plate to left semicircle; reduce matzo to two segments; blunt star tips and widen center.

Visual review: Five-point star now has a broad open center. Tile dividing row meets split walls at real shared nodes. Asymmetric plate/tile composition follows source. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 12. picture sun — pass

Input: `pictographic-primitives/_uncategorized_30/picture sun_d8495254-20a2-4d70-a2c6-140b4f7cd24a.svg`

[Run folder](d8495254-20a2-4d70-a2c6-140b4f7cd24a/20260924-spacing-batch3/) · [SVG](d8495254-20a2-4d70-a2c6-140b4f7cd24a/20260924-spacing-batch3/picture-sun.svg) · [Build gate](d8495254-20a2-4d70-a2c6-140b4f7cd24a/20260924-spacing-batch3/build-gate.txt)

A framed sun above two rounded hills.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide image rounded frame, sun and joined landscape. Original and atomic-debug inspected.

Omissions: Drop detached sun rays.

Visual review: Paired hills join the frame at explicit endpoints; smooth curves, centered sun and balanced openings. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 13. pin add — pass

Input: `pictographic-primitives/_uncategorized_30/pin add_edc387fb-8345-489a-a276-38ea07c6e827.svg`

[Run folder](edc387fb-8345-489a-a276-38ea07c6e827/20260924-spacing-batch3/) · [SVG](edc387fb-8345-489a-a276-38ea07c6e827/20260924-spacing-batch3/pin-add.svg) · [Build gate](edc387fb-8345-489a-a276-38ea07c6e827/20260924-spacing-batch3/build-gate.txt)

A location pin with a lower-right plus.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide map-pin domed pin and taper. Original and atomic-debug inspected.

Omissions: Drop circular add-badge boundary.

Visual review: Pin retains smooth dome and coherent taper; separate plus has four truly joined arms. Deliberate offset composition. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 14. read world — pass

Input: `pictographic-primitives/_uncategorized_32/read world_707a74f4-f696-4ab1-aaf2-6be7de8a3c1a.svg`

[Run folder](707a74f4-f696-4ab1-aaf2-6be7de8a3c1a/20260924-spacing-batch3/) · [SVG](707a74f4-f696-4ab1-aaf2-6be7de8a3c1a/20260924-spacing-batch3/read-world.svg) · [Build gate](707a74f4-f696-4ab1-aaf2-6be7de8a3c1a/20260924-spacing-batch3/build-gate.txt)

An open book below a globe.

Keyshape: VRECT_L. Upright composition, exact centerline box (8,4)-(40,44).

Construction: Lucide book-open paired curved pages and shared spine. Original and atomic-debug inspected.

Omissions: Drop page text; use one equator and one meridian; separate complete globe above book.

Visual review: Paired page curves and globe quadrants mirror about x=24. Globe reads as a globe, rather than the earlier umbrella-like dome. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.


## 15. rectangle history — pass

Input: `pictographic-primitives/_uncategorized_32/rectangle history_5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93.svg`

[Run folder](5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93/20260924-spacing-batch3/) · [SVG](5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93/20260924-spacing-batch3/rectangle-history.svg) · [Build gate](5bf1aba4-f7d5-46d8-ad17-5b349ba3bb93/20260924-spacing-batch3/build-gate.txt)

A clipped-corner history document with a clock.

Keyshape: SQUARE. Balanced square composition, exact centerline box (6,6)-(42,42).

Construction: Lucide file-clock: clock overlapping an interrupted document. Original and atomic-debug inspected.

Omissions: Drop bottom text rule; move clock to lower-left overlap.

Visual review: Large clock provides legal spacing around both hands. Deliberate asymmetric overlap follows Lucide file-clock construction. Reviewed at native48 and enlarged240 in light/dark themes.

Validation: valid, zero warnings. Build gate: PASS, zero errors and warnings.

