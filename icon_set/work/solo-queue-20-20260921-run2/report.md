# Solo queue offset 20

Fixed page: 10 items, requested offset 20; initial queue total 151. Gallery: http://localhost:8000. No replacement page was fetched.

All 10 current reference states were read immediately before intake and were TODO, with saved solo briefs and no existing original for these source IDs. Actual references were rendered and inspected. All 10 are standalone subjects; no combinations were prepared, no classification or brief saves were needed, and no items were skipped.

## Validation and export

Completed: 10 generated icons; 0 prepared combinations; 0 status-change skips; 0 unresolved items or saving failures. All originals pass validate_icon and full library QA with zero errors and zero warnings. The targeted build checked these 10 originals and reused all others. Each exported SVG matches its manifest hash, its entry records valid/pass with zero warnings, and source UUID/path attribution is preserved in its Python original. Actual light and dark exported renders were visually reviewed at 48 pixels.

The initial dancer export exposed arm/leg crowding, which was repaired; subsequent full QA and export passed. Shared-output lock contention was resolved by retrying, without altering the lock or other work. Both rider arm/leg gaps were also widened after full QA. No failures remain.

Visual findings: the dancer retains its raised arm and bent-knee pose; the dart retains two tail flights and a diagonal point; both scooter scenes retain circular heads, cargo and two wheels, with a projecting visor distinguishing the capped rider; the tooth and hooked pick remain separate readable objects; all five arrows preserve their direction, open/outlined construction, and required bar or dash details. Paired geometry remains balanced and native-size negative spaces remain open. Simplifications are recorded per item.

[Actual light exports](exports-light.png) · [Actual dark exports](exports-dark.png) · [Light contact sheet](contact-sheet-light.png) · [Dark contact sheet](contact-sheet-dark.png)

## Items

### 1. dancer-with-raised-arm-and-bent-knee

- UUID: `771cdf79-e59d-4541-bdff-a58073f629be`
- Reference: `pictographic-primitives/_uncategorized_14/dancer_771cdf79-e59d-4541-bdff-a58073f629be.svg`
- Original: [dancer_with_raised_arm_and_bent_knee_771cdf79_e59d_4541_bdff_a58073f629be.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/dancer_with_raised_arm_and_bent_knee_771cdf79_e59d_4541_bdff_a58073f629be.py)
- Target output: [dancer-with-raised-arm-and-bent-knee.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/dancer-with-raised-arm-and-bent-knee.svg)
- Full QA: pass; zero errors and warnings.

A dancer balances with one raised arm and a lifted bent knee. Square extremes 6..42. Head radius 5, vertical upper torso, exact 8 centerline neck gap. Natural asymmetric pose. Human full_body_ref supplies circular head and round limbs; Lucide person-standing supplies branched shared joints. Source supplies raised right arm and lifted right knee. Omit outlined body bulk.

### 2. dart-with-two-visible-tail-flights

- UUID: `f95af12b-a19b-4e5a-a6ec-10d5dae17560`
- Reference: `pictographic-primitives/_uncategorized_14/dart_f95af12b-a19b-4e5a-a6ec-10d5dae17560.svg`
- Original: [dart_with_two_visible_tail_flights_f95af12b_a19b_4e5a_a6ec_10d5dae17560.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/dart_with_two_visible_tail_flights_f95af12b_a19b_4e5a_a6ec_10d5dae17560.py)
- Target output: [dart-with-two-visible-tail-flights.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/dart-with-two-visible-tail-flights.svg)
- Full QA: pass; zero errors and warnings.

A diagonal sports dart points lower left with two tail flights upper right. Square 6..42 fits the diagonal equipment. Flights mirror about x+y=48; shared diagonal seam and shaft own real attachment nodes. Source supplies orientation and two fins. No useful Lucide dart match. Omit barrel grip texture and outline thickness to retain clean shaft and two flights.

### 3. bareheaded-delivery-rider-on-scooter

- UUID: `9046ec78-1a6b-4029-a2e9-be0d10843436`
- Reference: `pictographic-primitives/_uncategorized_14/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436.svg`
- Original: [bareheaded_delivery_rider_on_scooter_9046ec78_1a6b_4029_a2e9_be0d10843436.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/bareheaded_delivery_rider_on_scooter_9046ec78_1a6b_4029_a2e9_be0d10843436.py)
- Target output: [bareheaded-delivery-rider-on-scooter.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/bareheaded-delivery-rider-on-scooter.svg)
- Full QA: pass; zero errors and warnings.

A bareheaded courier rides a scooter with a rear parcel. Square extremes 6..42. Shared radius 3 circles for head and wheels; neck exactly 8 below head outline. Source supplies seated rider, rear box and scooter. Human full_body_ref supplies circular head and bent limbs; Lucide bike supplies simplified two-wheel scene. Omit headlamp and body panels. Parcel stays physical cargo, not a badge.

### 4. capped-delivery-rider-on-scooter

- UUID: `54079a5b-25ea-4346-8fc4-d2b5f8239da0`
- Reference: `pictographic-primitives/_uncategorized_14/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg`
- Original: [capped_delivery_rider_on_scooter_54079a5b_25ea_4346_8fc4_d2b5f8239da0.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/capped_delivery_rider_on_scooter_54079a5b_25ea_4346_8fc4_d2b5f8239da0.py)
- Target output: [capped-delivery-rider-on-scooter.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/capped-delivery-rider-on-scooter.svg)
- Full QA: pass; zero errors and warnings.

A capped courier rides a scooter carrying a rear box. Square 6..42 preserves equipment proportions. Head and wheels share radius 3; exact head gap 8. Cap visor attaches at head rightmost endpoint. Human full_body_ref and Lucide bike teach circular head and minimal bent limbs. Source supplies right-facing scooter, cap and rear parcel. Omit body panels and internal cap seam; retain projecting visor.

### 5. tooth-beside-bent-dental-stick

- UUID: `5fba6994-83b3-4c8e-872d-6f2fc2d663b7`
- Reference: `pictographic-primitives/_uncategorized_14/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7.svg`
- Original: [tooth_beside_bent_dental_stick_5fba6994_83b3_4c8e_872d_6f2fc2d663b7.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/tooth_beside_bent_dental_stick_5fba6994_83b3_4c8e_872d_6f2fc2d663b7.py)
- Target output: [tooth-beside-bent-dental-stick.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/tooth-beside-bent-dental-stick.svg)
- Full QA: pass; zero errors and warnings.

A two-rooted molar stands beside a hooked dental pick. Square 6..42 accommodates tool diagonal and upright tooth. Tooth owns a continuous broad crown and two roots; pick is separate physical equipment. Source supplies overlapping dental scene; no useful Lucide tooth match. Separate rather than overlap the pick and tooth; omit tool handle outline to retain spacing.

### 6. arrow-broad-rounded-bend-down

- UUID: `9c2120ce-007e-416d-a659-5f5577147e92`
- Reference: `pictographic-primitives/_uncategorized_14/diagram arrow bend down_9c2120ce-007e-416d-a659-5f5577147e92.svg`
- Original: [arrow_broad_rounded_bend_down_9c2120ce_007e_416d_a659_5f5577147e92.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/arrow_broad_rounded_bend_down_9c2120ce_007e_416d_a659_5f5577147e92.py)
- Target output: [arrow-broad-rounded-bend-down.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/arrow-broad-rounded-bend-down.svg)
- Full QA: pass; zero errors and warnings.

A broad outlined arrow bends right and then down. Square 6..42 fits bend and broad triangular tip. One open contour, concentric-style elbow with roomy inner turn. Source supplies open left tail, outlined bend and point; Lucide arrow-big-down supplies shoulder-to-tip contour principle. Omit no identity features.

### 7. arrow-down-right-with-open-head

- UUID: `7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b`
- Reference: `pictographic-primitives/_uncategorized_14/diagram arrow dash corner right down_7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b.svg`
- Original: [arrow_down_right_with_open_head_7d6d51d0_8bd7_4f12_a38b_3cc89d83a68b.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/arrow_down_right_with_open_head_7d6d51d0_8bd7_4f12_a38b_3cc89d83a68b.py)
- Target output: [arrow-down-right-with-open-head.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/arrow-down-right-with-open-head.svg)
- Full QA: pass; zero errors and warnings.

A straight arrow points diagonally down right. Square 6..42 follows the directional diagonal. Open head shares one endpoint with shaft; balanced horizontal and vertical arms derive from a common length. Source supplies long shaft and short head; Lucide arrow-down-right supplies the shared endpoint construction. No omitted details.

### 8. arrow-straight-down-with-open-head

- UUID: `e978c911-6376-4c9f-a6c5-4de2b2acc0b1`
- Reference: `pictographic-primitives/_uncategorized_14/diagram arrow dash down 1_e978c911-6376-4c9f-a6c5-4de2b2acc0b1.svg`
- Original: [arrow_straight_down_with_open_head_e978c911_6376_4c9f_a6c5_4de2b2acc0b1.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/arrow_straight_down_with_open_head_e978c911_6376_4c9f_a6c5_4de2b2acc0b1.py)
- Target output: [arrow-straight-down-with-open-head.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/arrow-straight-down-with-open-head.svg)
- Full QA: pass; zero errors and warnings.

A vertical arrow points straight down with an open head. VRECT_M 10..38 x 4..44 emphasizes long shaft. Mirror head arms around x=24 and share the tip with the shaft. Source supplies long vertical stem; Lucide arrow-down supplies the common endpoint and mirrored diagonals. No omitted details.

### 9. arrow-down-beneath-separate-top-bar

- UUID: `97505a77-9794-4383-8806-61bbb128d83e`
- Reference: `pictographic-primitives/_uncategorized_14/diagram arrow dash down_97505a77-9794-4383-8806-61bbb128d83e.svg`
- Original: [arrow_down_beneath_separate_top_bar_97505a77_9794_4383_8806_61bbb128d83e.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/arrow_down_beneath_separate_top_bar_97505a77_9794_4383_8806_61bbb128d83e.py)
- Target output: [arrow-down-beneath-separate-top-bar.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/arrow-down-beneath-separate-top-bar.svg)
- Full QA: pass; zero errors and warnings.

A broad down arrow begins beneath a separate horizontal bar. Square extremes 6..42 retain broad bar and centered point. Mirror the two shaft sides and shoulders about x=24; separate bar is intrinsic arrow notation. Source supplies open-top shaft with flanges and separate bar; Lucide arrow-big-down supplies continuous shoulder/point contour. No omitted identity features.

### 10. arrow-up-with-dashed-outline-tail

- UUID: `8f674c71-e41d-4766-9a9e-25a0eb335c94`
- Reference: `pictographic-primitives/_uncategorized_14/diagram arrow dash up 1_8f674c71-e41d-4766-9a9e-25a0eb335c94.svg`
- Original: [arrow_up_with_dashed_outline_tail_8f674c71_e41d_4766_9a9e_25a0eb335c94.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/arrow_up_with_dashed_outline_tail_8f674c71_e41d_4766_9a9e_25a0eb335c94.py)
- Target output: [arrow-up-with-dashed-outline-tail.svg](/Applications/Workspaces/pictographic/claude_skills/published/solo48/arrow-up-with-dashed-outline-tail.svg)
- Full QA: pass; zero errors and warnings.

A broad upward outline arrow has a broken two-sided tail. VRECT_L x8..40 y4..44 gives room for the dashed progression. All paired marks derive from axis24 and shaft halfwidth6; tails have a short dash and terminal dot, separated by 8 centerline units. Source supplies outlined head and dashed/dotted tail. Lucide arrow-big-down supplies shoulder construction, reflected vertically for up. Reduce many tiny tail marks to one dash and one dot per side.

## Evidence

The numbered intake JSON files preserve source UUID/path, current status, saved reference brief, and gallery row. The reference SVGs and PNGs preserve the inspected source artwork. Per-item full QA files and contact sheets record the final geometry. `results.json` records the manifest verification outcome.

Authorship: `gpt-6-astra`. No commit, full-library build, metadata seeding, browser-artwork overwrite, or component job was requested or performed. Existing unrelated changes were preserved.
