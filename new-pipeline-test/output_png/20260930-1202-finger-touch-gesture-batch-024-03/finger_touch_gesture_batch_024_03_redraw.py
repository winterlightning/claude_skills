"""finger-touch-gesture (redraw of the new-pipeline traced SVG).

Plan: a pointing hand tapping, on VRECT_L (centerline box (8,4)-(40,44)).
Two parts:
- hand: one closed contour, clockwise from the thumb notch J=(24,30).
  Index finger is a tube of width 8 (walls x=24 and x=32) with a radius-4
  tip about F=(28,17). The right wall drops to the knuckle (32,26), where a
  radius-8 shoulder turns out to the palm side x=40, flowing tangent into a
  radius-10 bottom-right corner that lands on the base y=44. The base runs
  left to a radius-10 heel that rises to x=8 and rolls tangent into the
  radius-4 thumb tip about (12,34); the thumb top runs flat back to J, so
  the thumb is the upper-left lobe of a rounded fist.
- touch: a radius-13 arc concentric with the fingertip about F, from
  (16,12) over the apex (28,4) to (40,12) -- a 5-12-13 triple, so the ends
  are on the grid and the gap to the fingertip is 9 all round.
Extremes: thumb tip x=8, touch arc end and palm side x=40, touch apex y=4,
palm base y=44.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8+.
- keyshape-short-axis (warn, x filled 86% of VRECT_M): fixed by moving to
  VRECT_L and filling it exactly. At stroke 4 the thumb tip needs 8 clear
  of the finger wall and the touch arc needs 12+ either side of the finger
  axis; together that is 32 wide, which VRECT_M's 28 cannot hold.
- clearance e0/e1 (error, touch arc 3.5 from the fingertip): fixed. The
  arc is concentric with the fingertip at radius 13 vs 4 (gap 9), and its
  ends clear the finger walls by 9.4.
- hole at [22.4, 6.7] (error, 1.6 wide): fixed. It was the sliver between
  the touch arc and the fingertip; that band is now 9 on centerlines.
Also repaired from the image: the thumb tip sat about 6 from the finger
wall; the thumb now sits level with the notch, its tip 8.6 clear of it.
Lucide construction: `pointer` informed the tube finger with a round tip,
the knuckle step and the rounded heel under the thumb; Lucide has no tap
ring, so the arc is a plain concentric cap. Deliberately asymmetric (a hand).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f6e6d80b-db8f-4ede-9278-c10ce856fdd2"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1202-finger-touch-gesture-batch-024-03/"
    "finger-touch-gesture-batch-024-03_raw.svg"
)
AUTHOR = "claude-opus-5-5"

FX, FY = 28, 17            # fingertip centre (shared by the touch arc)
TIP_R = 4                  # finger and thumb half-width
LEFT, RIGHT = FX - TIP_R, FX + TIP_R   # finger walls x=24, x=32
KNUCKLE_Y = 26
PALM_X, BASE_Y = 40, 44
SHOULDER_R, CORNER_R = 8, 10
NOTCH_Y = 30               # thumb top edge / notch J
THUMB_X = 12               # thumb tip centre x (tip reaches x=8)
HEEL_R = 10                # lower-left palm curve
TOUCH_R = 13               # 5-12-13: ends at (FX +/- 12, FY - 5)


class FingerTouchGestureRedraw(Solo48):
    icon_id = "finger-touch-gesture-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures"
    aliases = ("tap", "touch", "finger tap", "pointer hand")
    keywords = ("finger", "touch", "tap", "gesture", "hand", "pointer",
                "press", "click", "touchscreen")

    def build(self) -> None:
        corner_x = PALM_X - CORNER_R
        heel_x = THUMB_X - TIP_R + HEEL_R      # heel arc centre x
        heel_y = BASE_Y - HEEL_R              # heel arc centre y (= thumb tip y)
        self.add_line("finger-left", (LEFT, NOTCH_Y), (LEFT, FY))
        self.add_arc("fingertip", (LEFT, FY), (RIGHT, FY), radius_x=TIP_R)
        self.add_line("finger-right", (RIGHT, FY), (RIGHT, KNUCKLE_Y))
        self.add_arc("shoulder", (RIGHT, KNUCKLE_Y),
                     (PALM_X, KNUCKLE_Y + SHOULDER_R), radius_x=SHOULDER_R)
        self.add_arc("palm-corner", (PALM_X, KNUCKLE_Y + SHOULDER_R),
                     (corner_x, BASE_Y), radius_x=CORNER_R)
        self.add_line("base", (corner_x, BASE_Y), (heel_x, BASE_Y))
        self.add_arc("heel", (heel_x, BASE_Y), (THUMB_X - TIP_R, heel_y),
                     radius_x=HEEL_R)
        self.add_arc("thumb-tip", (THUMB_X - TIP_R, heel_y),
                     (THUMB_X, NOTCH_Y), radius_x=TIP_R)
        self.add_line("thumb-top", (THUMB_X, NOTCH_Y), (LEFT, NOTCH_Y))
        self.add_contour("hand", "finger-left", "fingertip", "finger-right",
                         "shoulder", "palm-corner", "base", "heel",
                         "thumb-tip", "thumb-top", closed=True)

        self.add_arc("touch", (FX - 12, FY - 5), (FX + 12, FY - 5),
                     radius_x=TOUCH_R)
