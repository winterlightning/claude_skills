# Batch 09 revisions

Ten independent solo variants. Author: `gpt-6`. Parents preserved. No review approvals were changed.

[Light preview](light.png) · [Dark preview](dark.png)

## cactus-in-rounded-pot-v2

Larger, taller cactus arms with rounded tips; SQUARE (2,2)-(46,46) gives the branches more width. Unequal arm heights preserve organic asymmetry. Pot retained.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/cactus_in_rounded_pot_v2_9ca14b29_db60_5c73_9981_f223340be7a7.py) · Parent: `cactus-in-rounded-pot`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## cactus-in-rimmed-pot-v2

Larger, taller cactus arms with rounded tips; SQUARE (2,2)-(46,46) gives the branches more width. Unequal arm heights preserve organic asymmetry. Rimmed pot retained.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/cactus_in_rimmed_pot_v2_5b8fbfc9_7597_5fd2_b24f_701fd84d868c.py) · Parent: `cactus-in-rimmed-pot`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## crab-v2

Crab claws formed by opposing elliptical curves, mirrored across x=24. SQUARE (2,2)-(46,46) preserves the leg span and claw height.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/crab_v2_41bb3775_67e6_5a7f_bc03_6922fe35a73f.py) · Parent: `crab`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## crawling-beetle-v2

Crawling beetle with the middle lower leg removed. HRECT_L (2,8)-(46,40) preserves the low side silhouette and antenna. Lucide bug informed sparse leg construction.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/crawling_beetle_v2_8bc281c9_b25f_4f1a_a127_ca91c9194046.py) · Parent: `crawling-beetle`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## crested-penguin-v2

Crested penguin with a rounded head, uninterrupted body and long flippers. VRECT_XL (5,2)-(43,46) supports an upright body. Mirrored across x=24; pointed flipper notches removed. Lucide bird informed broad head and belly arcs.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/crested_penguin_v2_b013a26e_4b3d_4d2f_a975_ca81de5ad6ce.py) · Parent: `crested-penguin`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## crocodile-in-water-v3

Crocodile with a raised eye and extended rectangular snout above one smooth wave. HRECT_L (2,8)-(46,40) gives room for the eye and water. Back ridge removed to emphasize the head. Deliberate right-facing asymmetry.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/crocodile_in_water_v3_ca6a591c_ff28_52f1_afee_3a6b95328acd.py) · Parent: `crocodile-in-water`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## duck-silhouette-v2

Duck with a broad bill and visible eye. HRECT_L (2,8)-(46,40) retains its swimming silhouette. Lucide bird informed the rounded head and clear eye; triangular bill replaced. Deliberate right-facing asymmetry.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/duck_silhouette_v2_4cda3eae_34c4_5ab8_a48f_adebd3cb4042.py) · Parent: `duck-silhouette`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## flying-bird-v2

Flying bird with a single raised wing, rounded breast and simple beak. SQUARE (2,2)-(46,46) retains flight height. Feather zigzags removed. Lucide bird informed broad contours. Deliberate right-facing asymmetry.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/flying_bird_v2_00732191_23f0_53ae_84da_b288489181c6.py) · Parent: `flying-bird`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## grizzly-head-profile-v2

Bear head with the neck joined to both endpoints of the head contour. HRECT_XL (2,5)-(46,43) preserves the profile. Roaring jaws and eye retained. Deliberate right-facing asymmetry.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/grizzly_head_profile_v2_3b805db1_6ba6_4ad5_8913_496730af8a1d.py) · Parent: `grizzly-head-profile`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## hammerhead-shark-v2

Hammerhead shark with an enlarged angular tail and straight fork edges. SQUARE (2,2)-(46,46) preserves hammer width and tail extent. Curved tail edge replaced; swept body remains deliberately asymmetric.

[Python module](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/hammerhead_shark_v2_bdd1577c_6f14_5bee_a41f_fac2b80017a7.py) · Parent: `hammerhead-shark`

Geometry validation: valid, zero warnings. Export hole/pinch QA: pass, zero warnings.

## Construction references

Reviewed local Lucide `bird` and `bug` original and atomic-debug drawings. Used broad coherent arcs for bird contours and sparse attached legs for the beetle. No useful direct Lucide match was found for the cactus, crab, crocodile, grizzly, or hammerhead; their parent drawings supplied subject geometry. Both themes were inspected at native 48 px and enlarged.

## Repository checks

Full suite: 276 tests, 111 failures, 17 errors, 1 skipped. Failures include unrelated invalid variants (`cobra-head-v2`, `paw-print-small-outer-toes-v2`), absent exports for newly added variants, stale generated skills, a missing smartwatch reference, gallery fixture JSON errors, and local-server socket restrictions. The complete solo build reported 9 failures in unrelated variants: anteater-v2, bird-in-flight-v2, buffalo-head-v2, cockatoo-v2, grand-canyon-with-river-v2, howling-wolf-v2, paw-print-small-outer-toes-v2, pelican-on-water-v2, and simple-gabled-shack-v2. After the solo failure was established, its optional cross-family QA and the redundant later build were interrupted. The family was not published to the main gallery; the batch SVGs are exported separately in `svg/`. Main-manifest inclusion and gallery Ready status remain blocked by the family build. No validation rules were changed. The ten parent Python modules and SVGs match their initial SHA-256 hashes.
