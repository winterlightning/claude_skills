# Bad-stroke revisions — thuan-mac

Requested: 20 at offset 0. Production returned 5 claimable icons; all 5 finished as done and returned to Ready.

Reviewer feedback for every icon: **Bad stroke drawn**. Every module records **AUTHOR = "gpt-6"**. All drawings use SOLO48 with 4px strokes.

[Reference / rejected / revised light / revised dark comparison](comparison.png)

One strict pass and four exact-SVG visual exceptions authorized by the user. Automatic failures and warnings are preserved in each validation report; exception acceptance is not an automatic strict pass.

## solo/low-crescent-with-two-sparkles

The current crescent is blunt and hooked, and two crosses replace the original four-point sparkles.

**Feedback:** Bad stroke drawn
**Revision:** Restored a clean diagonal crescent and two pointed diamond sparkles, with straight sparkle sides to keep their openings clear at 48px.
**Author:** `gpt-6`.
**Keyshape:** SQUARE. One smooth crescent and two diamond sparkle instances, each symmetric about its own axes. Ink extremes (4,4)-(44,44).
**Construction:** Lucide moon and sparkles: coherent crescent contour and four-point sparkle construction. Intentional upper-right sparkle arrangement follows the original.
**Reduction:** Concave sparkle edges replaced with diamond sides to keep open centers.
**Validation:** pass · exception; automatic fail. Production finish accepted; status Ready.

**Exception reason:** User authorized visual exceptions for UI quality. The two diamond sparkles retain visible open centers and distinct silhouettes at 48px. Their 3.07px internal opening and approximately 2–3px local gaps preserve the two-star crescent composition. All strokes remain 4px; inspected in both themes. Diamond sides intentionally replace deeply concave sides that closed the small sparkle hole.

**RESULT_DIR:** [20260928-thuan-mac-fix-03](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9/20260928-thuan-mac-fix-03)
**SVG:** [low-crescent-with-two-sparkles.svg](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9/20260928-thuan-mac-fix-03/low-crescent-with-two-sparkles.svg)
**Python module:** [low_crescent_with_two_sparkles_2e3cad1b_f9fc_43b2_b7f0_4c06b892a8b9.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9/20260928-thuan-mac-fix-03/low_crescent_with_two_sparkles_2e3cad1b_f9fc_43b2_b7f0_4c06b892a8b9.py)
**Validation:** [validation.txt](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9/20260928-thuan-mac-fix-03/validation.txt)
**Production receipt:** [result.json](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__low-crescent-with-two-sparkles/20260928T175139Z-thuan-mac/result.json)

## solo/reflective-safety-vest

The current vest has abrupt stepped armholes and heavy corners instead of the original curved sleeveless outline.

**Feedback:** Bad stroke drawn
**Revision:** Rebuilt mirrored curved armholes, rounded shoulders and hem, a centered V neck and seam, and two evenly spaced reflective-band edges.
**Author:** `gpt-6`.
**Keyshape:** VRECT_L. A symmetric vest outline owns shoulder radius, curved armholes, central seam and two band edges; x symmetry axis 24. Ink extremes (6,2)-(42,46).
**Construction:** Lucide shirt: rounded garment contours and intrinsic neckline. The original establishes the sleeveless armholes and reflective strip.
**Reduction:** Minor contour irregularities simplified; defining subject and arrangement preserved.
**Validation:** strict pass, zero warnings. Production finish accepted; status Ready.

**RESULT_DIR:** [20260928-thuan-mac-fix-01](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b470e44a-3a3c-592d-bab6-492f02f8e8fb/20260928-thuan-mac-fix-01)
**SVG:** [reflective-safety-vest.svg](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b470e44a-3a3c-592d-bab6-492f02f8e8fb/20260928-thuan-mac-fix-01/reflective-safety-vest.svg)
**Python module:** [reflective_safety_vest_b470e44a_3a3c_592d_bab6_492f02f8e8fb.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b470e44a-3a3c-592d-bab6-492f02f8e8fb/20260928-thuan-mac-fix-01/reflective_safety_vest_b470e44a_3a3c_592d_bab6_492f02f8e8fb.py)
**Validation:** [validation.txt](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b470e44a-3a3c-592d-bab6-492f02f8e8fb/20260928-thuan-mac-fix-01/validation.txt)
**Production receipt:** [result.json](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__reflective-safety-vest/20260928T175139Z-thuan-mac/result.json)

## solo/refresh-token-loop

The current inner loop is joined to the coin and the outer loop ends in an uneven short bend; the reference has two clean concentric open loops and a separate token.

**Feedback:** Bad stroke drawn
**Revision:** Rebuilt concentric three-quarter circles and detached the circular token, restoring the open lower-right sector.
**Author:** `gpt-6`.
**Keyshape:** SQUARE. Two concentric circles centered at (21,21) with radii 15 and 8, open in the lower-right quadrant; token centered (35,35), radius 7. Ink extremes (4,4)-(44,44).
**Construction:** Lucide rotate-cw: continuous circular sweep; source keeps two loops without an arrow. Deliberate open lower-right sector accommodates the separate coin.
**Reduction:** Minor contour irregularities simplified; defining subject and arrangement preserved.
**Validation:** pass · exception; automatic fail. Production finish accepted; status Ready.

**Exception reason:** User authorized visual exceptions for UI quality. Concentric loops retain a uniform 3px ink gap, and the detached token has approximately 3px clearance. This preserves the original two open loops and a separate round token without a misleading contact. Readable in both themes at 48px; all strokes 4px.

**RESULT_DIR:** [20260928-thuan-mac-fix-01](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/aa5d89f8-061f-42c6-ad89-5ffec35319d3/20260928-thuan-mac-fix-01)
**SVG:** [refresh-token-loop.svg](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/aa5d89f8-061f-42c6-ad89-5ffec35319d3/20260928-thuan-mac-fix-01/refresh-token-loop.svg)
**Python module:** [refresh_token_loop_aa5d89f8_061f_42c6_ad89_5ffec35319d3.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/aa5d89f8-061f-42c6-ad89-5ffec35319d3/20260928-thuan-mac-fix-01/refresh_token_loop_aa5d89f8_061f_42c6_ad89_5ffec35319d3.py)
**Validation:** [validation.txt](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/aa5d89f8-061f-42c6-ad89-5ffec35319d3/20260928-thuan-mac-fix-01/validation.txt)
**Production receipt:** [result.json](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__refresh-token-loop/20260928T175139Z-thuan-mac/result.json)

## solo/running-track-curve-arrow

The current direction arrow collapses into a thick triangular wedge; the track and arrow lack the clean open strokes of the original.

**Feedback:** Bad stroke drawn
**Revision:** Used two concentric semicircular track lanes with tangent straights and a balanced open arrowhead with a visible shaft.
**Author:** `gpt-6`.
**Keyshape:** SQUARE. Two lane contours share center (24,24) and radii 18 and 10; separate right-facing arrow centered at y28. Ink extremes (4,4)-(44,44).
**Construction:** Lucide undo-2: a semicircular turn with tangent straight sections and an open chevron arrowhead. The source sets the rightward direction.
**Reduction:** Minor contour irregularities simplified; defining subject and arrangement preserved.
**Validation:** pass · exception; automatic fail. Production finish accepted; status Ready.

**Exception reason:** User authorized visual exceptions for UI quality. Two concentric lanes retain an analytical 4px ink gap (sampled curve warning); the open arrowhead retains 3px clearance from the horizontal lanes. Native light/dark review confirms a clear arrow, visible shaft and smooth track. All strokes 4px.

**RESULT_DIR:** [20260928-thuan-mac-fix-01](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/bbab0c61-cd66-44e3-8954-bcb31ddc3d23/20260928-thuan-mac-fix-01)
**SVG:** [running-track-curve-arrow.svg](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/bbab0c61-cd66-44e3-8954-bcb31ddc3d23/20260928-thuan-mac-fix-01/running-track-curve-arrow.svg)
**Python module:** [running_track_curve_arrow_bbab0c61_cd66_44e3_8954_bcb31ddc3d23.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/bbab0c61-cd66-44e3-8954-bcb31ddc3d23/20260928-thuan-mac-fix-01/running_track_curve_arrow_bbab0c61_cd66_44e3_8954_bcb31ddc3d23.py)
**Validation:** [validation.txt](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/bbab0c61-cd66-44e3-8954-bcb31ddc3d23/20260928-thuan-mac-fix-01/validation.txt)
**Production receipt:** [result.json](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__running-track-curve-arrow/20260928T175139Z-thuan-mac/result.json)

## solo/saving-bull

The current animal faces the wrong way and has a flat angular body and stick legs; it loses the reference bull's lowered head, arched back and broad planted legs.

**Feedback:** Bad stroke drawn
**Revision:** Restored a left-facing lowered head with a curved horn, arched back, outlined planted legs and a rising financial arrow.
**Author:** `gpt-6`.
**Keyshape:** HRECT_L. One coherent body contour with integrated foreleg and hindleg; separate curved horn and rising trend arrow. Ink extremes (2,6)-(46,42).
**Construction:** Lucide piggy-bank: continuous animal outline with integrated legs. No exact local bull match; the original owns the horn, lowered head and arched back. Intentional natural asymmetry.
**Reduction:** Minor contour irregularities simplified; defining subject and arrangement preserved.
**Validation:** pass · exception; automatic fail. Production finish accepted; status Ready.

**Exception reason:** User authorized visual exceptions for UI quality. Integrated outlined legs and lowered head retain their natural narrow channels, approximately 1.1–3px, preserving the left-facing bull silhouette and planted legs. Openings remain visible at 48px in both themes. The trend arrow shares a real body endpoint; all strokes 4px and no false connections.

**RESULT_DIR:** [20260928-thuan-mac-fix-02](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/936d0079-3089-4c8c-bc22-422921c13e69/20260928-thuan-mac-fix-02)
**SVG:** [saving-bull.svg](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/936d0079-3089-4c8c-bc22-422921c13e69/20260928-thuan-mac-fix-02/saving-bull.svg)
**Python module:** [saving_bull_936d0079_3089_4c8c_bc22_422921c13e69.py](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/936d0079-3089-4c8c-bc22-422921c13e69/20260928-thuan-mac-fix-02/saving_bull_936d0079_3089_4c8c_bc22_422921c13e69.py)
**Validation:** [validation.txt](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/936d0079-3089-4c8c-bc22-422921c13e69/20260928-thuan-mac-fix-02/validation.txt)
**Production receipt:** [result.json](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__saving-bull/20260928T175139Z-thuan-mac/result.json)

