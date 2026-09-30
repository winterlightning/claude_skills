"""hands-gripping-wrists (redraw of the new-pipeline traced SVG).

Plan: HRECT_M, centerline box (4,10)-(44,38); two forearms locked in a
reciprocal wrist grip, drawn as the brief asks ("two opposing forearms, each
ending in a simple open hooked grip around the other wrist"), with 180 degree
rotational symmetry about (24,24).
- arm-a: the lower-left forearm, a straight line on y=38 from the left edge
  (x=4) to the grip axis x=24.
- hook-a: its hand, an arc r10 about (24,28) that turns up out of the arm
  tangentially, bulges right to x=34 and curls in to the fingertip (30,20)
  (a 6-8-10 point), inside the mouth of the other hand.
- arm-b / hook-b: the upper-right forearm and hand, the same pair rotated 180
  degrees (y=10 from x=44 to 24; arc about (24,20) bulging left to x=14,
  fingertip at (18,28)).
Each fingertip sits inside the other hook's mouth, so the two open grips
interlock without touching: fingertip to the other arm 10, fingertip to
fingertip 14.4. Full semicircles (fingertips on x=24) put a fingertip exactly
8 from the other hook's curve, which the engine returns as review; the
6-8-10 fingertips stop short of that.
Extremes: left 4 (arm-a), right 44 (arm-b), top 10 (arm-b), bottom 38 (arm-a).
Metric issues fixed:
- clearance e0/e5, e0/e7, e0/e8, e1/e5, e1/e7, e1/e8, e2/e6, e3/e4 (6.0-6.5
  on centerlines): the traced knuckles, cuff and doubled arm edges are
  replaced by two lines and two hooks; every distinct pair is >= 8 apart.
- hole x2 (3.61 and 2.95 inscribed): the grips are open hooks, so the drawing
  encloses no hole at all.
- stroke-count (9 traced, budget 6): 4 primitives in 2 contours.
- stroke-width (2.47 traced): authored at stroke 4 with every gap budgeted at
  8 on centerlines.
- keyshape-short-axis (x filled 81% on HRECT_L): the arms now run to x=4 and
  x=44, so every extreme lies on the box. HRECT_M is used instead of the
  suggested HRECT_L: the two hooks set the arm spacing (28, arms on the
  HRECT_M short axis 10/38). HRECT_L needs 32, i.e. r12 hooks 24 across
  on 20-long arms, so the hands would outweigh the forearms.
Not applicable: no-head (the subject is two forearms, no figure or head).
Lucide: no hand-grip original matches; construction follows Lucide `link`/
`paperclip` (straight runs flowing tangentially into semicircular turns).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6f5654b6-d336-40f6-84c1-e153d3ad1fc3"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1514-hands-gripping-wrists/"
    "hands-gripping-wrists_raw.svg"
)
AUTHOR = "claude-opus-5-5"

CX = 24          # grip axis and centre of symmetry (24,24)
ARM = 14         # arm offset from the centre: arms at y=10 and y=38
R = 10           # hook radius
TIP = (6, 8)     # fingertip offset from the hook centre (6-8-10 triangle)
LEFT, RIGHT = 4, 44


class HandsGrippingWristsRedraw(Solo48):
    icon_id = "hands-gripping-wrists-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("wrist grip", "helping hand", "rescue grip")
    keywords = ("hands", "grip", "wrist", "hold", "help", "rescue", "trust", "support", "teamwork")

    def build(self) -> None:
        low, high = 24 + ARM, 24 - ARM
        # -- lower-left forearm and its hooked hand ----------------------------
        self.add_line("arm-a", (LEFT, low), (CX, low))
        ca = (CX, low - R)
        self.add_arc("hook-a", (CX, low), (ca[0] + TIP[0], ca[1] - TIP[1]), radius_x=R, sweep=False)
        self.add_contour("hand-a", "arm-a", "hook-a")
        # -- upper-right forearm and its hooked hand (180 degree copy) ---------
        self.add_line("arm-b", (RIGHT, high), (CX, high))
        cb = (CX, high + R)
        self.add_arc("hook-b", (CX, high), (cb[0] - TIP[0], cb[1] + TIP[1]), radius_x=R, sweep=False)
        self.add_contour("hand-b", "arm-b", "hook-b")
