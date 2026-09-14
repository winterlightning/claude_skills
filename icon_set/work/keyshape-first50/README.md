# First 50 keyshape repairs

[Before/after comparison](review.html). Selection: first 50 matches in the failure gallery’s default fewest-issues order, frozen in `selection.json`. Original models are in `before-models/`; the final diff is `model-changes.patch`. Only these 50 models were edited by this task.

All 50 final models pass validation with zero warnings and full release QA, including holes/pinches. The focused build exited 0. All 50 are in `dist/solo48/manifest.json`. No profile, tolerance, or emitted SVG was manually patched.

## Shape decisions

Horizontal subjects retain HRECT_L; upright subjects retain VRECT_L; compact subjects retain SQUARE. Older aliases were normalized. The arched window, potty, bear face, and eagle head use SQUARE to suit their natural compact proportions. Repairs adjust shared boundary nodes or owning arc radii without whole-icon scaling.

Bottle handles use circular 6-8-10 attachment vectors; load-balance nodes use true circles. The airplane’s far wing joins the silhouette without a redundant crossing seam and has been widened for legal spacing. All five vine leaves remain, with an enlarged upper-right opening. Other identifying features were retained.

Human reference: `icon_set/references/human_ref/user.svg` for the profile card, and `full_body_ref.png` for camel pose. Profile head: center (14,14), radius 6, bottom y=20; shoulder top y=28. Pose head: center (34,10), radius 6, bottom y=16; body top y=24. Both have exactly 4 units of visible head/body clearance. The fetus retains its anatomical neck.

## References and visual review

Inspected local Lucide originals and atomic-debug geometry for user-round, sun, cloud, baby, bird, bug, and briefcase-business. Circle construction, paired wings, and rounded case corners informed repairs; coordinates were authored for SOLO48. No exact Lucide match was used for specialized subjects such as bat, fetus, and flexed biceps; their existing silhouettes were retained. Directional aircraft, birds, biceps and the kneeling pose keep deliberate asymmetry. Paired faces and wings retain their balance.

Reviewed every icon at 48 px and enlarged size in light and dark themes. The comparison offers keyshape envelope guides.

## Verification limitations

The broad unittest run completed 339 tests in 175.951 seconds: 505 failures, 26 errors, 1 skip. Findings include failing icons outside this sample and server tests blocked from binding sockets in the sandbox. That run occurred during refinements and is not a clean final repository-wide pass. The final sample was subsequently verified by the full focused build: 50 checked, 50 passed, exit 0 (`build.log`).

`results.json` records model validation. `release-results.json` records source hashes and release verdicts. `check.py` regenerates contact sheets; after a focused build, `publish_review.py` regenerates the comparison. The remaining 211 original group entries await the user’s decision.
