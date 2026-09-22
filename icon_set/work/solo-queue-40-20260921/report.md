# Solo queue — offset 40

Frozen page: 10 references from http://localhost:8000. Processed in returned order; no replacement fetches.

Outcome: **5 generated, 4 unresolved, 1 skipped because its selected family is sub, 0 combinations.**

Each item had its current status and saved brief reread before work. Default status entries were absent (TODO); the minus reference retained its user-selected sub family. No reference artwork, saved editorial brief or classification was changed. No component-saving failures occurred.

## Generated icons

All five have `validate_icon(): valid` with zero warnings, full stroke QA pass with no errors/warnings, successful targeted exports, exact SVG/model equality, and verified solo manifest entries. Both the contact-sheet renders and actual exported SVGs were inspected at native 48 pixels and enlarged in light/dark themes.

| Source UUID | Subject | Result |
|---|---|---|
| `003d246d-a760-4a25-8856-bbee07fbec57` | Treasure Chest with Sword | generated |
| `2f1ae9d4-7c42-400d-8760-d69f1f5f0abd` | Blood Drop Target | unresolved |
| `770b8052-e66d-401b-ae0d-9284719da14f` | Rounded Horizontal Minus Sign | skipped-family |
| `3cd7f4ab-a736-49a3-96ab-94392c320c57` | Smartphone with Home Button | generated |
| `8c0da42a-e577-481a-a50e-84f0e8648aae` | Four Stud Toy Building Brick | unresolved |
| `bd3ed1c5-f392-45bf-ac8f-4f6eb786cbd1` | Dental Molar Tooth Symbol | generated |
| `6e501462-4458-4ee8-918b-3b9b1c8dded4` | Human Head with Brain | unresolved |
| `0231a044-ecb1-470e-bcc3-8a45ccdc5d4a` | Human Head with Brain | unresolved |
| `19858aa1-e5f6-48f8-b744-522528105d32` | User Profile Avatar | generated |
| `e2fc1c66-2c6a-4bed-b334-72d7a85619d3` | Happy Striped Cat Face | generated |

## Treasure Chest with Sword — 003d246d-a760-4a25-8856-bbee07fbec57

VRECT_L; diagonal sword with round pommel and crossguard above chest. Omitted doubled chest rim and blade outline; retains the physical sword/chest scene. Lucide sword informed the guard.

- Python: `icon_set/model/icons/solo/sword_standing_inside_open_treasure_chest_003d246d_a760_4a25_8856_bbee07fbec57.py`
- SVG: `published/solo48/sword-standing-inside-open-treasure-chest.svg`
- Manifest: `published/solo48/manifest.json` → `sword-standing-inside-open-treasure-chest`
- Vector validation: valid, zero warnings. Release QA: pass, zero errors/warnings.
- Visual result: readable silhouette, consistent stroke, clear openings and balanced geometry in both themes.

## Blood Drop Target — 2f1ae9d4-7c42-400d-8760-d69f1f5f0abd

Existing editorial hold retained. Drop plus detached lower-right ring remains ambiguous: evidence modifier versus physical scene. No classification or brief changes.

## Rounded Horizontal Minus Sign — 770b8052-e66d-401b-ae0d-9284719da14f

Saved family is sub, following the recorded user decision. Excluded from this solo run; reference and brief preserved for icon-sub.

## Smartphone with Home Button — 3cd7f4ab-a736-49a3-96ab-94392c320c57

VRECT_M; tall rounded phone with circular home-button opening. Removed bezel dividers for clearance; blank screen remains dominant. Lucide smartphone informed rounded case.

- Python: `icon_set/model/icons/solo/phone_circular_home_button_3cd7f4ab_a736_49a3_96ab_94392c320c57.py`
- SVG: `published/solo48/phone-circular-home-button.svg`
- Manifest: `published/solo48/manifest.json` → `phone-circular-home-button`
- Vector validation: valid, zero warnings. Release QA: pass, zero errors/warnings.
- Visual result: readable silhouette, consistent stroke, clear openings and balanced geometry in both themes.

## Four Stud Toy Building Brick — 8c0da42a-e577-481a-a50e-84f0e8648aae

Existing draft is numerically valid, but its four-stud top view reads as a die or button and loses the perspective block. Retained unpublished; no two-stud substitution. A second depth tier needs clearance absent from this footprint.

## Dental Molar Tooth Symbol — bd3ed1c5-f392-45bf-ac8f-4f6eb786cbd1

VRECT_L; mirrored broad crown, shallow central dip and two rounded roots. One closed contour; no essential details omitted. No useful local Lucide tooth match.

- Python: `icon_set/model/icons/solo/broad_molar_with_two_rounded_roots_bd3ed1c5_f392_45bf_ac8f_4f6eb786cbd1.py`
- SVG: `published/solo48/broad-molar-with-two-rounded-roots.svg`
- Manifest: `published/solo48/manifest.json` → `broad-molar-with-two-rounded-roots`
- Vector validation: valid, zero warnings. Release QA: pass, zero errors/warnings.
- Visual result: readable silhouette, consistent stroke, clear openings and balanced geometry in both themes.

## Human Head with Brain — 6e501462-4458-4ee8-918b-3b9b1c8dded4

Existing left-facing anatomical head draft is numerically valid, but its brain reads as a small irregular ring, losing lobes and descending stem. Native light/dark review failed recognition. Brain is intrinsic anatomy, not a container combination.

## Human Head with Brain — 0231a044-ecb1-470e-bcc3-8a45ccdc5d4a

Existing right-facing anatomical head draft is numerically valid, but lacks the folded brain and descending stem. Native light/dark review failed recognition. Brain is intrinsic anatomy, not a container combination.

## User Profile Avatar — 19858aa1-e5f6-48f8-b744-522528105d32

VRECT_L; avatar specialization uses circular head, broad curved shoulders, open bottom, zero visible head/body gap. Replaced long oval neck silhouette to follow current avatar rules. Human user.svg and Lucide user-round informed construction.

- Python: `icon_set/model/icons/solo/long_necked_profile_bust_19858aa1_e5f6_48f8_b744_522528105d32.py`
- SVG: `published/solo48/long-necked-profile-bust.svg`
- Manifest: `published/solo48/manifest.json` → `long-necked-profile-bust`
- Vector validation: valid, zero warnings. Release QA: pass, zero errors/warnings.
- Visual result: readable silhouette, consistent stroke, clear openings and balanced geometry in both themes.

## Happy Striped Cat Face — e2fc1c66-2c6a-4bed-b334-72d7a85619d3

SQUARE; symmetric cat with ears, two forehead stripes, closed curved eyes and smile. Removed separate triangular nose, muzzle lobes and open mouth for clearance. Repaired existing draft in place then promoted it for registry discovery; Lucide cat informed contour.

- Python: `icon_set/model/icons/solo/smiling_striped_cat_head_e2fc1c66_2c6a_4bed_b334_72d7a85619d3.py`
- SVG: `published/solo48/smiling-striped-cat-head.svg`
- Manifest: `published/solo48/manifest.json` → `smiling-striped-cat-head`
- Vector validation: valid, zero warnings. Release QA: pass, zero errors/warnings.
- Visual result: readable silhouette, consistent stroke, clear openings and balanced geometry in both themes.

## Checks and limits

- Targeted build succeeded: 5 icons checked; 11,228 existing icons reused. Shared output contention was retried without modifying the lock or interrupting other work.
- 16 profile/keyshape tests passed. The new avatar passed the focused existing construction test, including centered circular face and zero ink gap. Its full stroke holes/pinches check passed.
- The broad avatar/profile test run reported 37 failures and 5 errors. It included a naming mismatch in the new avatar used by that test; the new avatar was corrected and passed the focused rerun. The other reported avatar failures concern existing library artwork and were left untouched. The broad suite is not claimed green.
- Four unresolved sources remain unpublished. The brick and two brain drafts pass geometry but fail reference recognition; their existing drafts were retained. Blood/ring interpretation remains on the existing editorial hold.
- Minus source is not counted as a generated solo. Its authoritative sub-family assignment was preserved for the sub workflow.
- No commits or full-library publication were requested. No validator/profile changes or metadata seeding were made. Authorship of new/revised originals is `gpt-6`, already used in this repository.

## Evidence

- `batch.json`: fixed UUIDs, source paths and saved editorial briefs.
- `item-N-status.json` / `item-N-briefs.json`: immediate per-item checks.
- `validation.json`, `*-qa.json`, `build.log`, `export-verification.json`: validation and export evidence.
- `references.png`, `contact-light.png`, `contact-dark.png`, `exports-light.png`, `exports-dark.png`: reference and final visual review.
- `unresolved-light.png`, `unresolved-dark.png`: visual failures retained for later work.
