# Solo queue — offset 60

Frozen page: 10 references from http://localhost:8000. No replacement items fetched. All ten were still TODO at their individual intake checks; none was skipped due to a changed status.

## Results

| UUID | Reference | Result |
|---|---|---|
| f422872b-42cf-4b74-aa1f-bf870f557d7a | Human legs wearing pantyhose | Unresolved draft: keyshape and clearance failures |
| c2caf72a-e028-4b0f-9d4f-ea1a841b97bb | Document with Right Aligned Image | Verified container split; both component briefs saved |
| 602f9a81-4306-4859-94c6-dc6f92e2061c | Long Swimming Pike Fish | Drawing passes vector and release QA; see export verification |
| 407c218e-c29c-4f30-b87f-c44424fce8df | I Love You Hand Sign | Drawing passes vector and release QA; see export verification |
| 46622ecc-42b6-4d7f-b812-d85bb3ec076e | Diagonal Striped Pattern | Drawing passes vector and release QA; see export verification |
| 1a8ec40b-c5b8-4694-afaf-5baadb4972ad | Curved Elbow Pipe Fitting | Drawing passes vector and release QA; see export verification |
| 1d983437-28d4-4d9e-8147-91158ea165bf | Curved Plumbing Elbow Pipe | Drawing passes vector and release QA; see export verification |
| f1449e0a-c5a1-4ede-806c-ca36de940e2c | Rounded Plus Addition Symbol | Drawing passes vector and release QA; see export verification |
| ed60c884-6e26-4a90-9170-23473b0ad667 | Uniformed Police Officer Avatar | Drawing passes vector and release QA; see export verification |
| 79dff51d-7a09-497d-8df1-de4b77d03e31 | Decorative Ceramic Vase | Drawing passes vector and release QA; see export verification |

## Generated drawing details

All eight drawings have `valid` vector reports and `pass` release QA, with zero errors and warnings. Native 48px and enlarged renders were inspected in light and dark themes using the contact-sheet renderer. See `validation.json`, `contact-light.png`, `contact-dark.png`, and `exports.json` for evidence.

### slender-swimming-pike

icon_set.model.icons.solo.slender_swimming_pike_602f9a81_4306_4859_94c6_dc6f92e2061c

Left-facing slender pike with forked tail and upper/lower fins. Lucide fish informs fin/body construction; preserve source direction and long body.
Plan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_M uses exact SOLO48 contract bounds. Lucide fish original and atoms informed the continuous body contour; omit the crowded gill stroke.

- Original: `icon_set/model/icons/solo/slender_swimming_pike_602f9a81_4306_4859_94c6_dc6f92e2061c.py`
- Export: `published/solo48/slender-swimming-pike.svg`

### extended-thumb-two-fingers

icon_set.model.icons.solo.extended_thumb_two_fingers_407c218e_c29c_4f30_b87f_c44424fce8df

I-love-you gesture: thumb, index and little finger extended with folded middle fingers. Meaning-specific hand anatomy retained for visual checking.
Plan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. Lucide hand original and atoms inform semicircular finger ends. The two folded fingers share one simplified valley; palm crease omitted for clearance.

- Original: `icon_set/model/icons/solo/extended_thumb_two_fingers_407c218e_c29c_4f30_b87f_c44424fce8df.py`
- Export: `published/solo48/extended-thumb-two-fingers.svg`

### diagonal-striped-swatch

icon_set.model.icons.solo.diagonal_striped_swatch_46622ecc_42b6_4d7f_b812_d85bb3ec076e

A tall textile swatch with evenly spaced diagonal stripes. VRECT_L preserves the tall panel; one rounded border owns two stripes with constant x+y increments of 18. Source supplies all-over pattern; no reusable centered modifier. Lucide rectangle-vertical informs continuous quarter-circle corners; reduce source stripe count to two for clearance.

- Original: `icon_set/model/icons/solo/diagonal_striped_swatch_46622ecc_42b6_4d7f_b812_d85bb3ec076e.py`
- Export: `published/solo48/diagonal-striped-swatch.svg`

### flanged-elbow-pipe

icon_set.model.icons.solo.flanged_elbow_pipe_1a8ec40b_c5b8_4694_afaf_5baadb4972ad

A right-angle pipe with broad end flanges, opening left and upward. SQUARE fits the two equal arms. One outline owns collars and concentric radii 8 and 16 about (22,22). Source supplies orientation and flange steps; internal flange seams omitted to keep openings clear. Lucide rectangle-vertical informs continuous outline joins.

- Original: `icon_set/model/icons/solo/flanged_elbow_pipe_1a8ec40b_c5b8_4694_afaf_5baadb4972ad.py`
- Export: `published/solo48/flanged-elbow-pipe.svg`

### plain-rounded-elbow-pipe

icon_set.model.icons.solo.plain_rounded_elbow_pipe_1d983437_28d4_4d9e_8147_91158ea165bf

A broad plain elbow pipe bending from below toward the right. SQUARE preserves equal arm extent. One contour with concentric elbow radii 18 and 6 around (24,24); matching terminal corners radius 4. Source supplies the broad smooth bend and rounded ends; no omitted identity features. Lucide rectangle-vertical informs tangent line/quarter-circle transitions.

- Original: `icon_set/model/icons/solo/plain_rounded_elbow_pipe_1d983437_28d4_4d9e_8147_91158ea165bf.py`
- Export: `published/solo48/plain-rounded-elbow-pipe.svg`

### rounded-equal-armed-plus

icon_set.model.icons.solo.rounded_equal_armed_plus_f1449e0a_c5a1_4ede_806c_ca36de940e2c

An outlined equal-armed plus with rounded terminal caps. SQUARE fits its four equal extents; rotate one arm definition around (24,24). Arms retain 8-unit internal centerline width. Source supplies outline and balanced silhouette; Lucide rectangle-vertical supplies rounded-terminal construction. No details omitted.

- Original: `icon_set/model/icons/solo/rounded_equal_armed_plus_f1449e0a_c5a1_4ede_806c_ca36de940e2c.py`
- Export: `published/solo48/rounded-equal-armed-plus.svg`

### police-officer-in-peaked-cap

icon_set.model.icons.solo.police_officer_in_peaked_cap_ed60c884_6e26_4a90_9170_23473b0ad667

Police officer bust with peaked cap and uniform badge. VRECT_L budgets cap, circular face and curved broad shoulders. Human reference user.svg owns shoulder construction; circular jaw radius 8 centered (24,18), shoulders apex y30 gives exact 4 centerline / zero ink gap. Shared vertical axis; mirrored cap and shoulders. Omit cap insignia, lapels and seam to preserve clearance; keep one chest badge. No useful Lucide police-specific match; human reference supplies anatomy.

- Original: `icon_set/model/icons/solo/police_officer_in_peaked_cap_ed60c884_6e26_4a90_9170_23473b0ad667.py`
- Export: `published/solo48/police-officer-in-peaked-cap.svg`

### flared-neck-ceramic-vase

icon_set.model.icons.solo.flared_neck_ceramic_vase_79dff51d_7a09_497d_8df1_de4b77d03e31

A symmetrical ceramic vase with flared rim, narrow neck and rounded belly. VRECT_L fits the upright vessel. One contour, with the left side derived by reversing and mirroring the right side about x24. Exact extremes x8/x40 and y4/y44. Source supplies the blank ceramic silhouette; no decorative details added. Lucide amphora informs continuous vessel side contours; handles are absent from this reference.

- Original: `icon_set/model/icons/solo/flared_neck_ceramic_vase_79dff51d_7a09_497d_8df1_de4b77d03e31.py`
- Export: `published/solo48/flared-neck-ceramic-vase.svg`

## Visual findings

The pipe variants remain distinct: stepped end flanges versus a plain rounded elbow. The vase has mirrored flowing sides and a clear neck. The plus has equal arms and an open interior. The swatch uses two diagonal stripes to avoid small corner pockets. The hand keeps three extended digits, simplifying folded fingers into one valley. The fish is strongly stylized with a pointed head and forked tail; its dorsal and lower fins are balanced. The police bust retains a peaked cap, circular lower face and one chest badge; the circular jaw and shoulder apex have 4 centerline units of separation, giving zero ink gap.

## Verified deferred combination

UUID `c2caf72a-e028-4b0f-9d4f-ea1a841b97bb`: container combination. Main: **Rounded article card frame** (`container`). Sub: **Article layout with right picture** (`sub`). Both component briefs were POSTed with the skip/container classification; the saved reference family and brief were amended. Both endpoints were read back and matched. No component generation was started. Original artwork unchanged. Payload and readback: `01-payloads.json`, `01-verified.json`. No saving failures.

## Unresolved crossed stockinged legs

UUID `f422872b-42cf-4b74-aa1f-bf870f557d7a` remains TODO. The pre-existing draft was inspected and validated; it was not overwritten or exported. Its crossed contours look tangled rather than like clean stockinged legs. No useful Lucide leg match was found.

The attempted VRECT_M draft layout fails exact bounds by 1.5 units on the left and 1.3726 on the right. `standing` / `rear` separation is 3.82933 centerline units and `rear` / `cross` is 3.85064, against the required 8. No invalid contacts, relaxed rules or false success claims were introduced. See `00-unresolved-validation.txt` and `00-draft-light.png`.

## Checks and limitations

- Targeted builds only; no full-library build or metadata seeding.
- All 16 profile/keyshape tests passed.
- The focused existing avatar test passed for the new police drawing after body primitive names were aligned with the test convention.
- The broad avatar run was not green (36 failure subtests, 6 errors in the initial run, including a naming issue in the new police drawing that was subsequently fixed). Other avatar failures remain outside this batch; no claim of a clean whole-library suite.
- No commit, publish, or production-state import was performed. Unrelated workspace changes were preserved.
- Authorship uses the existing `gpt-6` value; no new author label was introduced.
