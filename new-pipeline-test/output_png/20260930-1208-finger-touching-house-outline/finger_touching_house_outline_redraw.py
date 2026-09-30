"""finger-touching-house-outline (redraw of the new-pipeline traced SVG).

Plan: a pointing hand whose index finger rises into the open lower-right
corner of a peaked house outline, on SQUARE (centerline box (6,6)-(42,42)).
Two parts:
- house: one open contour in the Lucide `house` manner (no eaves): floor
  end (18,25) -> left wall x=6 -> 45-degree roof over the peak (14,6) ->
  right wall top (22,14) -> short right wall stub ending at (22,16). The
  floor stops at x=18 and the right wall stops high, so the lower-right
  corner is left open for the finger, as in the generated image.
- hand: one closed outline. The index finger is an 8-wide tube on x=32
  (walls x=28 and x=36, r4 round tip about (32,23)). The right wall steps
  out as a short level knuckle at y=30, rounds (r4) into the palm side
  x=42 and down (r6) to the flat base y=42. On the left the thumb leaves
  the finger at (28,37) along a 45-degree edge, ends in a round tip about
  (22,37) (radius 3*sqrt(2), two quarter cubics so the knots stay integer)
  and returns through a heel curve into the base.
Extremes: left wall x=6, roof peak y=6, palm side x=42, hand base y=42.
Spacing (centerlines, need 8): stub end 12.2 from the fingertip centre
(8.2 to the tip), floor end 10 from the finger wall and 12.2 from the tip
centre, stub end 9.2 from the floor end, thumb tip 8.4 from the floor end.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8+.
- keyshape-short-axis (warn, x filled 86%): fixed. The house left wall
  sits on x=6 and the palm on x=42, so SQUARE is exact on both axes
  without stretching the subject.
- clearance e0/e5 (error, roof 6.58 from the finger): fixed. The eaves are
  dropped (Lucide house) and the finger moves right to x=32; the roof's
  right end (22,14) is 13.5 from the fingertip centre.
- clearance e1/e5 (error, floor end 2.89 from the finger): fixed. The
  floor stops at x=18, 10 from the finger wall.
- clearance e2/e5 (error, right wall stub 2.42 from the finger): fixed.
  The stub sits at x=22 and stops at y=16, 12.2 from the fingertip centre.
Trade-off: at 8-unit clearance the fingertip cannot rise as high into the
house corner as in the image; the right wall stub is kept short (2) and
the finger stands 11 above the knuckle so both parts stay readable.
Lucide construction: `house` informed the 45-degree peaked roof meeting
the walls without eaves; `pointer` informed the upright index finger with
a round tip, the knuckle step and the rounded palm. The traced knuckle
scallops are dropped (they do not survive stroke 4 at 48). The
composition is deliberately asymmetric: house upper left, hand lower right.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f58e0b9-2d9d-4e01-88b6-5e110128d93c"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1208-finger-touching-house-outline/"
    "finger-touching-house-outline_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# house
PEAK = (14, 6)
WALL_L, WALL_R = 6, 22         # wall x positions
WALL_TOP = PEAK[1] + (PEAK[0] - WALL_L)   # 14, roof height at the walls
FLOOR_Y = 25
FLOOR_END = 18                 # the floor stops short of the finger
STUB_END = 16                  # right wall stub bottom

# hand
FX = 32                        # finger axis
FW = 4                         # half finger width (walls FX +- FW)
TIP_Y = 23                     # finger tip arc centre y
KNUCKLE_Y = 30
PALM_X = 42
BASE_Y = 42
CROTCH = (FX - FW, 37)         # thumb leaves the finger here
TC = (22, 37)                  # thumb tip centre
TR = 3                         # thumb tip offset: radius TR*sqrt(2)
K = 4 / 3 * math.tan(math.pi / 8)   # quarter-circle cubic constant


def _quarter(centre, start, end):
    """Cubic control points for a 90-degree arc about ``centre``."""
    cx, cy = centre
    sx, sy = start[0] - cx, start[1] - cy
    ex, ey = end[0] - cx, end[1] - cy
    c1 = (start[0] + K * ex, start[1] + K * ey)
    c2 = (end[0] + K * sx, end[1] + K * sy)
    return c1, c2, end


class FingerTouchingHouseOutlineRedraw(Solo48):
    icon_id = "finger-touching-house-outline-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("tap home", "touch home", "home button", "smart home touch")
    keywords = ("finger", "touch", "tap", "house", "home", "pointer",
                "hand", "smart home", "real estate", "select")

    def build(self) -> None:
        # house: floor end, left wall, roof, right wall stub
        self.add_polyline(
            "house", (FLOOR_END, FLOOR_Y), (WALL_L, FLOOR_Y),
            (WALL_L, WALL_TOP), PEAK, (WALL_R, WALL_TOP), (WALL_R, STUB_END))

        # hand: finger up, tip, knuckle, palm side, base, heel, thumb
        lx, rx = FX - FW, FX + FW
        self.add_line("finger-left", CROTCH, (lx, TIP_Y))
        self.add_arc("finger-tip", (lx, TIP_Y), (rx, TIP_Y), radius_x=FW)
        self.add_line("finger-right", (rx, TIP_Y), (rx, KNUCKLE_Y))
        self.add_line("knuckle", (rx, KNUCKLE_Y), (PALM_X - 4, KNUCKLE_Y))
        self.add_arc("knuckle-corner", (PALM_X - 4, KNUCKLE_Y),
                     (PALM_X, KNUCKLE_Y + 4), radius_x=4)
        self.add_line("palm-side", (PALM_X, KNUCKLE_Y + 4), (PALM_X, BASE_Y - 6))
        self.add_arc("palm-corner", (PALM_X, BASE_Y - 6), (PALM_X - 6, BASE_Y),
                     radius_x=6)
        heel_end = (TC[0] + 3, BASE_Y)
        self.add_line("palm-base", (PALM_X - 6, BASE_Y), heel_end)
        tip_low = (TC[0] - TR, TC[1] + TR)     # (19,40)
        tip_apex = (TC[0] - TR, TC[1] - TR)    # (19,34)
        tip_high = (TC[0] + TR, TC[1] - TR)    # (25,34)
        # heel: leaves the base level, arrives along the thumb's 45-degree side
        self.add_bezier("heel", heel_end,
                        ((heel_end[0] - 2, BASE_Y),
                         (tip_low[0] + 2, tip_low[1] + 2), tip_low))
        self.add_bezier("thumb-tip", tip_low,
                        _quarter(TC, tip_low, tip_apex),
                        _quarter(TC, tip_apex, tip_high))
        self.add_line("thumb-top", tip_high, CROTCH)
        self.add_contour(
            "hand", "finger-left", "finger-tip", "finger-right", "knuckle",
            "knuckle-corner", "palm-side", "palm-corner", "palm-base", "heel",
            "thumb-tip", "thumb-top", closed=True)
