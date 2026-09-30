"""Crossed fingers with extended thumb (redraw of the new-pipeline traced SVG).

Subject: a raised hand with the index and middle fingers crossed; the front
finger leans up-right over the rear one, whose rounded tip peeks out on the
left. The thumb sticks out to the left, the two lower fingers are curled
into one rounded knuckle block, and a short wrist closes the hand.

Plan: VRECT_L (centerline box (8,4)-(40,44)). The metrics suggested VRECT_M
(score 1.21 vs 1.16), but its 28-wide box cannot hold an 8-wide thumb, an
8.94-wide front finger and a 6-inscribed curled-finger opening side by side
at 8 spacing; the extra 4 units of VRECT_L are what make room for the thumb.
- front finger: straight tube along (1,-2), edges 8.94 apart, left edge
  A(28,6)-J2(26,10)-J1(21,20)-K(17,28), right edge B(36,10)-P(32,18)-F(25,32);
  the tip is two cubics over a horizontal-tangent apex (32,4).
- rear finger: r5 cap about (19,9) (apex (19,4)), both edges tangent along
  (3,4), 10 apart; they end on the front finger's left edge at J2 and J1
  (declared connect), so the finger reads as passing behind.
- thumb: top edge K-T(14,24) parallel to the rear finger's left edge at
  exactly 8; a cubic tip turns over to the left extreme (8,30); the
  underside curves down to the wrist.
- curled fingers: r8 knuckle arc about (32,26) from P to the right side
  x 40, closed by the fold line y 32 that starts on the front finger's
  right edge (the front finger passes in front of them).
- heel: r8 arc (40,32)-(32,40); wrist lines x 18 and x 32, y 40-44.
Extremes: x 8 thumb tip, x 40 knuckle side, y 4 both fingertips, y 44 wrist.
Lucide `hand` informed the rounded-tube fingers and the open wrist; Lucide
has no crossed-fingers icon. There is no head or torso, so no human figure
is marked.

Metric issues (crossed-fingers-with-extended-thumb-batch-021-08_metrics.json):
- stroke-width (info, trace 2.55): redrawn at stroke 4, all gaps sized for 4.
- keyshape-short-axis (warn, VRECT_M y fill 96%): fixed on VRECT_L without
  stretching; every extreme sits exactly on the box.
- clearance e0/e1 4.17 (error): fixed; the trace's rear-finger piece that
  reappears right of the front finger is dropped, and the front finger runs
  over the curled fingers, which are enclosed by the knuckle arc and fold.
- clearance e1/e2 5.72 (error): fixed; the two fingertips are rebuilt as
  separate 10 / 8.94 wide tubes joined only at J2 and J1.
- hole 0.89 at the rear fingertip (error): fixed; now 6.0 inscribed
  (r5 tube, 10 on centerlines).
- hole 2.0 in the curled fingers (error): fixed; now 7.4 inscribed.
Re-running svg_metrics.py on the redraw reports no issues; validate_icon()
is valid and library QA passes with no warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ffa5f097-3a06-4fd0-9be9-200d8a58103b"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1111-crossed-fingers-with-extended-thumb-batch-021-08/crossed-fingers-with-extended-thumb-batch-021-08_raw.svg"
AUTHOR = "claude-opus-5-5"

# Front finger: straight tube along (1,-2); left edge x = 28 - (y - 6) / 2,
# right edge x = 36 - (y - 10) / 2 (8.94 apart).
A, B = (28, 6), (36, 10)            # cap ends; B - A = (8, 4) is the perpendicular chord
FRONT_APEX = (32, 4)                # cap top, horizontal tangent
J2, J1, K = (26, 10), (21, 20), (17, 28)   # rear-finger joins and thumb crotch on the left edge
P, F = (32, 18), (25, 32)           # knuckle join and fold join on the right edge
# Rear finger: r5 cap about (19,9); both edges tangent along (3,4), 10 apart.
REAR_C, REAR_R = (19, 9), 5
L, R = (15, 12), (23, 6)            # REAR_C -/+ (4,-3)
# Thumb: top edge K-T runs along (3,4), 8 from the rear finger's left edge;
# the rounded tip turns over to the left extreme (8,30).
THUMB_T, THUMB_LEFT = (14, 24), (8, 30)
# Curled fingers: r8 knuckle about (32,26), right side x 40, fold at y 32.
KNUCKLE_C, KNUCKLE_R, FOLD_Y, RIGHT_X = (32, 26), 8, 32, 40
WRIST_L, WRIST_R, WRIST_TOP, BOTTOM = 18, 32, 40, 44


class CrossedFingersWithExtendedThumbRedraw(Solo48):
    icon_id = "crossed-fingers-with-extended-thumb-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("fingers crossed", "good luck hand", "hope gesture")
    keywords = ("hand", "fingers", "crossed", "luck", "hope", "wish", "gesture", "thumb")

    def build(self) -> None:
        kx, ky = KNUCKLE_C
        knuckle_side = (RIGHT_X, ky)
        fold_end = (RIGHT_X, FOLD_Y)
        wrist_l, wrist_r = (WRIST_L, WRIST_TOP), (WRIST_R, WRIST_TOP)

        # Hand outline: wrist, thumb, front finger, knuckles, heel, wrist.
        self.add_line("wrist-left", (WRIST_L, BOTTOM), wrist_l)
        self.add_bezier("thumb-under", wrist_l, ((13, 38.5), (8, 35), THUMB_LEFT))
        self.add_bezier("thumb-tip", THUMB_LEFT, ((8, 25.9), (11.55, 20.74), THUMB_T))
        self.add_line("thumb-top", THUMB_T, K)
        self.add_line("front-left-low", K, J1)
        self.add_line("front-left-mid", J1, J2)
        self.add_line("front-left-top", J2, A)
        self.add_bezier("front-tip", A,
                        ((28.76, 4.49), (30.31, 4), FRONT_APEX),
                        ((35.33, 4), (37.49, 7.02), B))
        self.add_line("front-right", B, P)
        self.add_arc("knuckle", P, knuckle_side, radius_x=KNUCKLE_R, sweep=True)
        self.add_line("palm-right", knuckle_side, fold_end)
        self.add_arc("palm-heel", fold_end, wrist_r,
                     radius_x=RIGHT_X - WRIST_R, radius_y=WRIST_TOP - FOLD_Y, sweep=True)
        self.add_line("wrist-right", wrist_r, (WRIST_R, BOTTOM))
        self.add_contour("hand", "wrist-left", "thumb-under", "thumb-tip", "thumb-top",
                         "front-left-low", "front-left-mid", "front-left-top", "front-tip",
                         "front-right", "knuckle", "palm-right", "palm-heel", "wrist-right")

        # Front finger passes over the curled fingers; the fold closes them off.
        self.add_line("front-right-low", P, F)
        self.add_line("fold", F, fold_end)
        self.add_contour("curl", "front-right-low", "fold")
        self.relate("connect", "curl", "hand")

        # Rear finger: only its tip shows, left of the front finger.
        self.add_line("rear-left", J1, L)
        self.add_arc("rear-tip", L, R, radius_x=REAR_R, sweep=True)
        self.add_line("rear-right", R, J2)
        self.add_contour("rear", "rear-left", "rear-tip", "rear-right")
        self.relate("connect", "rear", "hand")
