# Batch 11 revisions

Ten independent SOLO48 variants. Original modules and SVGs are preserved. Author: `gpt-6`.

| Variant | Keyshape | Revision |
|---|---|---|
| [leaping-rabbit-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/leaping_rabbit_v2.py) | SQUARE | A leaping rabbit with a detached dot tail. SQUARE extremes (2,2)-(46,46) preserve the leaping pose; the open tail loop is removed. Lucide rabbit informs rounded ears and haunch. Right-facing asymmetry is intentional. |
| [leaping-marlin-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/leaping_marlin_v2.py) | SQUARE | A leaping marlin with a rounder left flank and curved dorsal edge. SQUARE extremes (2,2)-(46,46) preserve the bill and tall fin. No useful local Lucide marlin match; coherent elliptical arcs replace the pointed flank junction. Directional pose is intentional. |
| [leaping-dolphin-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/leaping_dolphin_v2.py) | SQUARE | A leaping dolphin with an enlarged tail fluke. SQUARE extremes (2,2)-(46,46) retain the original pose. Tail area expands into the lower negative space; no identity detail removed. No useful local Lucide dolphin match; directional asymmetry is intentional. |
| [peacock-feather-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/peacock_feather_v2.py) | VRECT_L | A peacock feather with a dot eye. VRECT_L extremes (8,2)-(40,46) retain the tall diagonal vane and quill. The circular eye loop is replaced by one dot. Lucide feather informs the sparse vane and diagonal shaft; the diagonal pose is intentional. |
| [pelican-on-water-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/pelican_on_water_v2.py) | SQUARE | A pelican floating on water with the short underline beneath its folded wing removed. SQUARE extremes (2,2)-(46,46) preserve the bill, neck and water. Lucide bird informs the sparse curved profile. Left-facing asymmetry is intentional. |
| [penguin-looking-down-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/penguin_looking_down_v2.py) | VRECT_L | A left-facing penguin looking down, with a rounded belly, compact downward bill and single curved flipper. VRECT_L extremes (8,2)-(40,46) retain upright proportions. The narrow parent neck-like body is replaced by a full torso. Lucide bird informs the coherent contour and dot eye. Side-view asymmetry is intentional. |
| [round-hand-fan-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/round_hand_fan_v2.py) | SQUARE | A round hand fan with a smooth circular blade and diagonal handle. SQUARE extremes (2,2)-(46,46) preserve the diagonal pose. Unequal blade lobes are replaced by consistent circular radii, split at the handle junction. No useful local Lucide hand-fan match. The handle direction is intentional. |
| [crocodile-in-water-v4](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/crocodile_in_water_v4.py) | HRECT_M | A crocodile in water with a single horizontal snout line. HRECT_M extremes (2,11)-(46,37) preserve the low aquatic profile. The rectangular mouth return is removed; brow, eye and waves remain. No useful local Lucide crocodile match. Right-facing asymmetry is intentional. |
| [scorpion-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/scorpion_v2.py) | SQUARE | A scorpion with four shorter legs and curved pincer jaws. SQUARE extremes (2,2)-(46,46) preserve the claws and curled tail. Lucide bug informs mirrored appendages and consistent paired curves. Leg extensions are shortened; the tail remains deliberately left-curled. |
| [singing-bird-v2](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/singing_bird_v2.py) | HRECT_XL | A singing bird with its triangular crest removed. HRECT_XL extremes (2,5)-(46,43) fit the remaining head and open bill without the crest. Lucide bird informs a smooth domed head and sparse dot eye. The open-beak side profile is intentionally asymmetric. |

Reviewed enlarged and at 48 pixels in both themes. Lucide original renders and atomic geometry inspected: bird, rabbit, feather, and bug. All supplied references are standalone subjects.

[Light preview](light.png) · [Dark preview](dark.png) · [Per-icon validation](validation.json)

The source metadata and variant parent links are preserved. No review approval or parent status changes were made. New catalog entries default to Ready.

Verification: all ten final variants pass `validate_icon()` with no warnings and full `inspect_icon()` QA including holes and pinches. Original Python and SVG hashes match the pre-edit snapshot.

The complete suite ran 276 tests: 110 failures, 2 errors, 1 skipped. Failures include shared pending exports, generated skill documents out of date, a missing smartwatch trace source, and an unrelated `pregnant-belly-with-heart-v2` arm/heart MIC violation. See [test log](tests.log).

Final family build succeeded: 680 SOLO48 icons validated and exported. All ten new variants are in the manifest, exported SVGs exactly match their final models, and the ten parent modules and SVGs remain byte-identical. The final build used `--no-report` to avoid regenerating the unrelated library-wide QA report while concurrent batches were building.

Post-build corpus check: 18 tests ran; 17 passed and one failed because the concurrently edited `pregnant-belly-with-heart-v2` export differs from its current model. Batch 11 export comparisons all pass. See [post-build corpus log](corpus-tests.log).
