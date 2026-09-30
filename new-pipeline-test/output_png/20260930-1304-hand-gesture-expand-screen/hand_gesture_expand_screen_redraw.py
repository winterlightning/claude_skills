"""hand-gesture-expand-screen (redraw of the new-pipeline traced SVG).

Subject: a hand with the index finger raised and the thumb out to the left,
with a diagonal arrow to the upper right and one to the lower left -- the
"spread to expand / zoom in" touch gesture.

Plan: SQUARE (centerline box (6,6)-(42,42)).
- hand: one open stroke, open at the wrist (x=24 and x=36, y=38..42).
  * index finger: walls x=18 / x=26 (width 8), r4 tip about (22,10), apex y=6.
  * folded fingers: two r4 knuckle bumps about (30,25) and (38,25) on the
    right of the finger; the second one ends on the right edge x=42.
  * palm right side: x=42 down to y=30, then a tangent S-bend into the wrist.
  * thumb: an r2 fillet out of the finger's left wall, a short top edge
    y=18, an r4 tip about (12,22) (left x=8), then the heel of the hand as
    one r12 quarter arc about (12,38) into the left wrist wall x=24.
- arrows: the same arrow twice, mirrored through the centre (24,24), head
  arms 5 and a shaft of 7 on each axis so the shaft reads past the head:
  NE tip (42,6) with head (37,6)-(42,6)-(42,11), shaft to (35,13);
  SW tip (6,42) with head (6,37)-(6,42)-(11,42), shaft to (13,35).
Extremes: left x=6 SW arrow, top y=6 finger apex + NE arrow, right x=42
knuckle / palm side + NE arrow, bottom y=42 wrist + SW arrow.

Keyshape: SQUARE, as suggested by the metrics (score 1.12, shape hint square).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- stroke-count (warn, 8 > 6): now 5 strokes -- the hand outline and a
  shaft + head for each arrow (the trace split each arrow in three).
- keyshape-short-axis (warn, x filled 87%): the subject now spans x 6..42,
  the SW arrow sits in the left corner and the knuckles reach x=42.
- clearance e0/e3 7.11 and e0/e4 3.76 (errors, NE arrow vs finger and
  knuckles): the arrow moved into the corner; shaft end (35,13) is 9.3 from
  the finger tip, 9 from the finger wall and 8.1 / 8.4 from the knuckles.
- clearance e4/e5 2.9, e4/e6 7.24, e4/e7 7.99 (errors, SW arrow vs thumb and
  heel): the arrow is in the corner and the heel is an r12 arc about (12,38),
  so the arrow shaft end (13,35) is 8.8 from the heel and 9 from the thumb.
- no-head (warn): not applicable -- the only human part is a hand; there is
  no figure and no head.
Lucide `pointer` informed the finger + knuckle-bump construction (knuckle
radius = stroke width) and Lucide `move-diagonal` the matching corner arrows.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "50312a29-a897-494e-b23f-8a7aa90fde0d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1304-hand-gesture-expand-screen/hand-gesture-expand-screen_raw.svg"
AUTHOR = "claude-opus-5-5"

# Hand
FL, FR = 18, 26                  # index finger walls
TIP, TIP_R = (22, 10), 4         # finger tip (apex y=6)
KNUCKLE_Y, KNUCKLE_R = 25, 4     # knuckle bumps about (30,25) and (38,25)
RIGHT = 42                       # palm right side
SIDE_BEND = 30                   # palm side leaves x=42 here
WRIST_L, WRIST_R, WRIST_TOP, BOTTOM = 24, 36, 38, 42
FILLET_C, FILLET_R = (16, 16), 2  # finger -> thumb crotch
THUMB, THUMB_R = (12, 22), 4     # thumb tip
HEEL_C, HEEL_R = (12, 38), 12    # heel arc (ends at (24,38))
# Arrows
ARM, SHAFT = 5, 7                # head arm length; shaft run on each axis
NE, SW = (42, 6), (6, 42)


def arc(c, r, a0, a1):
    """Cubic segments for a circular arc from angle a0 to a1 (radians, y down)."""
    n = max(1, math.ceil(abs(a1 - a0) / (math.pi / 2) - 1e-9))
    step = (a1 - a0) / n
    h = 4 / 3 * math.tan(step / 4) * r
    segs = []
    for i in range(n):
        s, e = a0 + i * step, a0 + (i + 1) * step
        p0 = (c[0] + r * math.cos(s), c[1] + r * math.sin(s))
        p3 = (c[0] + r * math.cos(e), c[1] + r * math.sin(e))
        c1 = (p0[0] - h * math.sin(s), p0[1] + h * math.cos(s))
        c2 = (p3[0] + h * math.sin(e), p3[1] - h * math.cos(e))
        segs.append((c1, c2, p3))
    return segs


def line(a, b):
    return ((a[0] + (b[0] - a[0]) / 3, a[1] + (b[1] - a[1]) / 3),
            (a[0] + 2 * (b[0] - a[0]) / 3, a[1] + 2 * (b[1] - a[1]) / 3), b)


class HandGestureExpandScreenRedraw(Solo48):
    icon_id = "hand-gesture-expand-screen-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "gestures/touch"
    aliases = ("expand gesture", "spread gesture", "zoom in gesture", "pinch out")
    keywords = ("hand", "finger", "thumb", "gesture", "touch", "expand", "zoom",
                "fullscreen", "arrows", "spread")

    def build(self) -> None:
        pi = math.pi
        k1 = (FR + KNUCKLE_R, KNUCKLE_Y)
        k2 = (RIGHT - KNUCKLE_R, KNUCKLE_Y)
        mid = (WRIST_TOP + SIDE_BEND) / 2
        # Hand, right wrist -> palm side -> knuckles -> finger -> thumb -> heel -> left wrist.
        self.add_bezier(
            "hand", (WRIST_R, BOTTOM),
            line((WRIST_R, BOTTOM), (WRIST_R, WRIST_TOP)),
            ((WRIST_R, mid), (RIGHT, mid), (RIGHT, SIDE_BEND)),
            line((RIGHT, SIDE_BEND), (RIGHT, KNUCKLE_Y)),
            *arc(k2, KNUCKLE_R, 0, -pi),
            *arc(k1, KNUCKLE_R, 0, -pi),
            line((FR, KNUCKLE_Y), (FR, TIP[1])),
            *arc(TIP, TIP_R, 0, -pi),
            line((FL, TIP[1]), (FL, FILLET_C[1])),
            *arc(FILLET_C, FILLET_R, 0, pi / 2),
            line((FILLET_C[0], FILLET_C[1] + FILLET_R), (THUMB[0], THUMB[1] - THUMB_R)),
            *arc(THUMB, THUMB_R, -pi / 2, -3 * pi / 2),
            *arc(HEEL_C, HEEL_R, -pi / 2, 0),
            line((WRIST_L, WRIST_TOP), (WRIST_L, BOTTOM)),
        )

        # Two identical arrows, mirrored through the centre.
        for name, tip, sx, sy in (("ne", NE, -1, 1), ("sw", SW, 1, -1)):
            self.add_polyline(f"arrow-{name}-head", (tip[0] + sx * ARM, tip[1]), tip,
                              (tip[0], tip[1] + sy * ARM))
            self.add_line(f"arrow-{name}-shaft", (tip[0] + sx * SHAFT, tip[1] + sy * SHAFT), tip)
            self.relate("connect", f"arrow-{name}-head", f"arrow-{name}-shaft")
