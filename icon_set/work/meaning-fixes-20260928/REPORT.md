# Meaning fixes — thuan-mac

20 claimed icons revised and returned to Ready through `primitive_fix.py finish`. All modules use `AUTHOR = "gpt-6"`. Two automatically pass with zero warnings; 18 use user-authorized, drawing-bound visual exceptions. Automatic findings remain in each validation report.

The original and rejected SVGs were rendered and visually compared before drawing. Final candidates were inspected at 48px and enlarged in both light and dark themes. All retained the SOLO48 canvas and uniform 4px strokes.

[Visual comparison gallery](index.html)

## 1. `solo/acro-yoga-stacked-bridge`

- **Before:** The heads were attached to the limbs; the upper pose became a tall arch with no supporting arm.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore two detached heads, a shallow upper bridge, an arm and two lower supports.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** human_ref/full_body_ref.png. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Outlined limbs reduced to coherent strokes.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e90b7491-c523-516a-bb5e-3f47ddbb4cab/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e90b7491-c523-516a-bb5e-3f47ddbb4cab/20260928T180739Z-meaning-fix/acro-yoga-stacked-bridge.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e90b7491-c523-516a-bb5e-3f47ddbb4cab/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass`; automatic model `valid`.

**Human construction:** Both head centres (10,13)/(10,31), radii 4; necks (22,13)/(22,31): 12 - 4 = 8 centreline / 4 ink. Upper pose preserves a deliberate sideways neck bend from the source. Shared reference: `icon_set/references/human_ref/`.

## 2. `solo/acro-yoga-supported-balance`

- **Before:** An extra head-like ring at the top and a single shared body obscured the two-person pose.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Keep exactly two right-facing detached heads and two horizontal torsos, with the upper curled leg and lower bent leg.
- **Keyshape:** `VRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** human_ref/full_body_ref.png. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Outlined limbs reduced to strokes; only the two actual heads are circular.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5240dbe0-19a2-54d5-b0f7-5cc3089e49e4/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5240dbe0-19a2-54d5-b0f7-5cc3089e49e4/20260928T180739Z-meaning-fix/acro-yoga-supported-balance.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5240dbe0-19a2-54d5-b0f7-5cc3089e49e4/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The two-person balance needs a tall asymmetric pose; retain its natural envelope and two exactly detached heads instead of distorting the pose to a rectangle. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

**Human construction:** Head centres (38,24)/(38,40), radii 4; necks (26,24)/(26,40): 12 - 4 = 8 centreline / 4 ink. Both torsos point left away from their heads. Shared reference: `icon_set/references/human_ref/`.

## 3. `solo/bearded-pirate-with-crossed-hat-mark`

- **Before:** The broad pirate hat became a domed helmet, the cross collapsed, and the beard was narrow and angular.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the flared tricorn silhouette, readable crossed mark, rounded face sides and pointed full beard.
- **Keyshape:** `HRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** skull. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/871b202b-58cd-4c8b-af66-2a006eddce86/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/871b202b-58cd-4c8b-af66-2a006eddce86/20260928T180416Z-meaning-fix/bearded-pirate-with-crossed-hat-mark.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/871b202b-58cd-4c8b-af66-2a006eddce86/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Retain the full tricorn hat, crossed emblem, face and pointed beard. Their compact portrait spacing is needed for pirate recognition at 48px. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 4. `solo/beer-mug-with-bread`

- **Before:** The mug left wall disappeared behind a large bread shape and the handle became a tiny loop.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore a visible mug body, rounded foam, a generous side handle and a separate rounded loaf with one scoring cut.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** beer. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Two bread scores reduced to one.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda/20260928T180739Z-meaning-fix/beer-mug-with-bread.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f7b3cdc5-a4f3-4160-a8d1-71f476dc0fda/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Retain the beer mug, foam, side handle and overlapping bread loaf. Their intentional overlap and natural bounds preserve the tavern subject. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 5. `solo/brain-with-undivided-centre`

- **Before:** The flattened scalloped outline read as a cloud or flower, with no anatomical folds.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Use a taller paired-lobe outline and two short inward folds while retaining an undivided centre.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** brain. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Small edge wrinkles reduced to broad lobes; centre stays undivided.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/505cc1d4-dec0-4492-aadd-1c3ba0a9d545/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/505cc1d4-dec0-4492-aadd-1c3ba0a9d545/20260928T180416Z-meaning-fix/brain-with-undivided-centre.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/505cc1d4-dec0-4492-aadd-1c3ba0a9d545/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Use the natural rounded brain perimeter instead of flattening its lobes to the keyshape. Two inward folds clarify the brain without dividing the centre. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 6. `solo/browser-yuan-sign-solo`

- **Before:** The browser toolbar had no controls and the oversized single-bar currency mark dominated the frame.
- **Reviewer feedback:** Does not convey the intended meaning /  / Browser
- **Changed:** Add a clear browser toolbar with two controls and restore a finer-positioned yuan mark in the lower-right content area.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** panel-top. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted; single currency bar follows the supplied reference.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f3a40f08-7124-46f5-9ed2-b85ee4e25e73/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f3a40f08-7124-46f5-9ed2-b85ee4e25e73/20260928T180416Z-meaning-fix/browser-yuan-sign-solo.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f3a40f08-7124-46f5-9ed2-b85ee4e25e73/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The two browser controls must remain visible inside a compact toolbar. Preserve the toolbar and yuan sign with their reviewed compact spacing. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 7. `solo/bunch-of-bananas-batch-010-10`

- **Before:** Straight triangular wedges replaced the rounded banana fruits.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore three nested sweeping banana contours, blunt curved tips, and their shared upright stalk.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** banana. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted; three fruits retained.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/01dfab52-1214-532b-8f84-ea5dce7a2998/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/01dfab52-1214-532b-8f84-ea5dce7a2998/20260928T180416Z-meaning-fix/bunch-of-bananas-batch-010-10.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/01dfab52-1214-532b-8f84-ea5dce7a2998/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Three curved bananas must converge at their shared stalk. Preserve the smooth fan and tapered fruit contours rather than triangular wedges. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 8. `solo/bunny-holding-easter-egg`

- **Before:** The rabbit was squared off like a letter H, with only one eye and no recognizable face or holding paw.
- **Reviewer feedback:** Does not convey the intended meaning /  / Bunny
- **Changed:** Restore a rounded rabbit face, two outward ears, paired eyes, a small nose and a paw holding an egg.
- **Keyshape:** `VRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** rabbit. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Fine whiskers omitted to keep the paired eyes, nose and holding gesture clear.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/606ec34e-20d1-525e-a765-4f3fca8d3c47/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/606ec34e-20d1-525e-a765-4f3fca8d3c47/20260928T180739Z-meaning-fix/bunny-holding-easter-egg.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/606ec34e-20d1-525e-a765-4f3fca8d3c47/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The complete rabbit face, outward ears, holding paw and egg need compact facial and attached-part spacing. The paired eyes, nose and egg opening remain visible at 48px. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 9. `solo/burning-crashed-aircraft`

- **Before:** The aircraft became a jagged lightning shape and the fire merged into it.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore a rounded nose, diagonal fuselage, wing and tail, with a separate flame and two smoke wisps.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** plane. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Smoke reduced to two short curved wisps.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/81f5c526-61a1-4426-afae-2fec80a31cb2/20260928T181020Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/81f5c526-61a1-4426-afae-2fec80a31cb2/20260928T181020Z-meaning-fix/burning-crashed-aircraft.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/81f5c526-61a1-4426-afae-2fec80a31cb2/20260928T181020Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Preserve the diagonal aircraft with its fin and wing plus a separate flame and smoke. The tapered silhouette and compact composition communicate the crash. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 10. `solo/camel-pose`

- **Before:** The kneeling legs collapsed into a triangular blob and the hand/body pose was ambiguous.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Draw a clear backbend, vertical reaching arm, bent knees and a horizontal shin, preserving the head position.
- **Keyshape:** `HRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** human_ref/full_body_ref.png. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Solid body silhouette reduced to torso, reaching arm, thigh and shin strokes.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/89df2d47-dd44-58e7-a2f9-f8f36667b21c/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/89df2d47-dd44-58e7-a2f9-f8f36667b21c/20260928T180416Z-meaning-fix/camel-pose.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/89df2d47-dd44-58e7-a2f9-f8f36667b21c/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Preserve the natural backbend proportions and exact diagonal head-to-neck gap rather than distort this human pose to a standard rectangular envelope. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

**Human construction:** Head (38,8), radius 5; neck (33,20): sqrt(5^2+12^2) - 5 = 8 centreline / 4 ink. The backbend intentionally extends the neck upward/right. Shared reference: `icon_set/references/human_ref/`.

## 11. `solo/camper-behind-flagged-tent`

- **Before:** The flag and doorway collapsed into thick marks; the camper was crowded against the tent.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore a triangular tent opening, a small flag, and a distinct camper head and shoulder behind the tent.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** tent + human_ref/user.svg. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Small shirt cuff omitted; head, shoulder, tent, door and flag retained.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5655244e-9c88-42c3-a2be-d90a6fab78b2/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5655244e-9c88-42c3-a2be-d90a6fab78b2/20260928T180739Z-meaning-fix/camper-behind-flagged-tent.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/5655244e-9c88-42c3-a2be-d90a6fab78b2/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Keep the camper behind a tent with a triangular doorway and small flag; the tiny flag opening and compact occluded composition are deliberate. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

**Human construction:** Head (37,12), radius 5; shoulder crest (37,25): 13 - 5 = 8 centreline / 4 ink. All shoulder controls stay at or below y=25. Shared reference: `icon_set/references/human_ref/`.

## 12. `solo/canoe-paddler`

- **Before:** The hull read as a bowl and the paddler had no clear bent arm or seated lean; water was omitted.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the leaning seated figure, bent arm, diagonal paddle, pointed canoe bow and two wave troughs.
- **Keyshape:** `HRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** sailboat + human_ref/full_body_ref.png. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Fine leg detail omitted behind the canoe gunwale.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/fc6689dd-a028-5cb2-b326-1fe893e5518c/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/fc6689dd-a028-5cb2-b326-1fe893e5518c/20260928T180739Z-meaning-fix/canoe-paddler.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/fc6689dd-a028-5cb2-b326-1fe893e5518c/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Keep the seated paddler, diagonal paddle, upturned canoe bow and detached water. The hand-to-paddle and torso-to-boat contacts and compact water spacing preserve the scene. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

**Human construction:** Head (23,9), radius 5; neck (18,21): sqrt(5^2+12^2) - 5 = 8 centreline / 4 ink. The diagonal torso follows the seated lean. Shared reference: `icon_set/references/human_ref/`.

## 13. `solo/cao-dai`

- **Before:** The defining almond-shaped Divine Eye was replaced by a small circle.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the eye contour and centred pupil inside the triangular symbol.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** eye. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/1a804c88-15f7-4476-b406-236f03484b85/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/1a804c88-15f7-4476-b406-236f03484b85/20260928T180416Z-meaning-fix/cao-dai.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/1a804c88-15f7-4476-b406-236f03484b85/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The almond-shaped Divine Eye deliberately approaches the triangle sides as in the source. Its contour and pupil are essential to the Cao Dai symbol. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 14. `solo/capped-delivery-rider-on-scooter`

- **Before:** The rider became a disconnected head over an angular frame; the seated posture and scooter body were lost.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the capped head, bent riding arm and leg, rounded scooter shell, parcel box and two open wheels.
- **Keyshape:** `HRECT_L`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** car + human_ref/full_body_ref.png. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Fine scooter trim omitted; parcel, rider, cap, wheels and steering retained.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/54079a5b-25ea-4346-8fc4-d2b5f8239da0/20260928T180739Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/54079a5b-25ea-4346-8fc4-d2b5f8239da0/20260928T180739Z-meaning-fix/capped-delivery-rider-on-scooter.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/54079a5b-25ea-4346-8fc4-d2b5f8239da0/20260928T180739Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** Retain the rider, cap, package, scooter shell and two wheels in one UI icon. Intentional mounted-part contacts and compact spacing preserve the delivery scene. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

**Human construction:** Head (26,8), radius 4; neck (26,20): 12 - 4 = 8 centreline / 4 ink. The cap is part of the head; the torso and arm recede below the junction. Shared reference: `icon_set/references/human_ref/`.

## 15. `solo/car-broken-beneath-impact-burst`

- **Before:** The impact became a closed badge and the car halves looked like two separate small cars.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore an open sharp impact burst above one car split by a central zigzag break, with two circular wheels.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** car. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** Small body trim omitted; split body, burst and two wheels retained.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/757187c1-fd16-4577-8bb6-b25ad4df2330/20260928T181020Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/757187c1-fd16-4577-8bb6-b25ad4df2330/20260928T181020Z-meaning-fix/car-broken-beneath-impact-burst.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/757187c1-fd16-4577-8bb6-b25ad4df2330/20260928T181020Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The car must remain one split vehicle under an impact burst; retain its jagged break, two wheels and compact scene proportions. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 16. `solo/loading-bar-interface-essential`

- **Before:** The progress bar was nearly square, so it read as a prohibition or capsule symbol.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the long horizontal capsule proportions and a diagonal progress boundary.
- **Keyshape:** `HRECT_M`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** No useful exact Lucide match; rounded enclosure construction from panel-top.. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/af64a969-821b-4b51-b04b-4e271c5910d7/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/af64a969-821b-4b51-b04b-4e271c5910d7/20260928T180416Z-meaning-fix/loading-bar-interface-essential.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/af64a969-821b-4b51-b04b-4e271c5910d7/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** A loading bar needs a slim horizontal capsule. Its reviewed 44x20 ink envelope preserves the source meaning; the standard HRECT_M height made the rejected drawing too squat. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 17. `solo/mobile-phone-pound-sign`

- **Before:** The device lacked its lower phone panel and the pound glyph had a straight bar-like foot.
- **Reviewer feedback:** Does not convey the intended meaning /  / pound
- **Changed:** Restore a rounded handset with bottom separator and a recognizable curved pound stem and baseline.
- **Keyshape:** `VRECT_M`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** smartphone. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a70db137-a446-4f4c-b656-4fea14660981/20260928T181147Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a70db137-a446-4f4c-b656-4fea14660981/20260928T181147Z-meaning-fix/mobile-phone-pound-sign.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a70db137-a446-4f4c-b656-4fea14660981/20260928T181147Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `review`.

**Exception:** Exact geometric minimum: the pound upper semicircle reaches y=12 and the phone top is y=4, giving 8 centreline units / 4 ink units. Retain the readable pound rather than distort it for the conservative curved-pair warning. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 18. `solo/type-a-outlet-with-flattened-circular-recess`

- **Before:** The square wall plate and flattened recess were removed, leaving a generic circle with two lines.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore a rounded square plate, flattened circular recess and matching vertical slots.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** plug. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db/20260928T180416Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db/20260928T180416Z-meaning-fix/type-a-outlet-with-flattened-circular-recess.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db/20260928T180416Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The square wall plate, flattened round recess and two vertical slots all identify Type A. Keep the nested structure with reviewed narrower-than-profile gaps. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 19. `solo/type-f-outlet-with-two-holes-and-earth-tabs`

- **Before:** The wall plate disappeared and the pin holes were rendered as filled dots.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore the square wall plate and two circular pin openings inside the grounded round recess.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** plug. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a953c01a-331f-443c-b5ed-5756e2821bc2/20260928T181020Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a953c01a-331f-443c-b5ed-5756e2821bc2/20260928T181020Z-meaning-fix/type-f-outlet-with-two-holes-and-earth-tabs.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/a953c01a-331f-443c-b5ed-5756e2821bc2/20260928T181020Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass-exception`; automatic model `invalid`.

**Exception:** The square plate, circular recess, open pin holes and upper/lower earth tabs identify Type F. Preserve these layers and small round apertures with compact but visible gaps. The approval identifies the user-delegated judgment and exact SHA-256; it does not erase automatic errors or warnings.

## 20. `solo/vectors-add-anchor`

- **Before:** The anchor nodes were tall ovals and the diagonal connectors merged into one heavy arrow-like shape.
- **Reviewer feedback:** Does not convey the intended meaning
- **Changed:** Restore four equal circular vector nodes and three distinct spokes with deliberate node-edge attachments.
- **Keyshape:** `SQUARE`; follows the dominant subject envelope, with the natural proportions retained where excepted.
- **Construction reference:** spline. The original reference determines the subject; local Lucide original/atomic geometry informs round enclosures, coherent curves or repeated circles as applicable.
- **Omissions:** No defining feature omitted; four equal circular nodes retained.
- **Artifacts:** [RESULT_DIR](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/eb962df2-7d7e-4704-b588-8cea12d18d62/20260928T181020Z-meaning-fix) · [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/eb962df2-7d7e-4704-b588-8cea12d18d62/20260928T181020Z-meaning-fix/vectors-add-anchor.svg) · [validation](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/eb962df2-7d7e-4704-b588-8cea12d18d62/20260928T181020Z-meaning-fix/validation.txt)
- **AUTHOR:** `gpt-6`.
- **Status:** production `done` → Ready; full QA `pass`; automatic model `valid`.
