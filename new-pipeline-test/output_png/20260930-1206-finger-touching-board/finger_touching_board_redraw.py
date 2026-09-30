"""finger-touching-board (redraw of the new-pipeline traced SVG).

Plan: a pointing hand tapping a wide board, on SQUARE (centerline box
(6,6)-(42,42)). Two parts:
- board: a Lucide-style rounded rectangle (corner r2) spanning the full
  width, x 6..42, y 6..21. Its bottom edge is open around the finger and
  leaves two short stubs ending at (11,21) and (37,21).
- hand: one closed outline. The index finger is an 8-wide tube on the
  vertical axis x=24 (walls x=20 and x=28, r4 round tip about (24,19)) that
  reaches 6 into the board. The right wall steps out as a level knuckle at
  y=30, rounds (r4) into the palm side x=40 and down (r6) to the flat base
  y=42. On the left the thumb leaves the finger at (20,33) along a 45-degree
  edge, ends in a round tip about (14,33) (radius 3*sqrt(2), two quarter
  cubics so the knots stay integer) and returns through a smooth heel curve
  into the base.
Extremes: board top 6, board sides 6 and 42, hand base 42.
Spacing: finger walls 9 from both stubs, knuckle 9 below the board edge,
thumb tip 8.1 from the left stub end, thumb crotch 9 above the base, thumb
8.5 wide; the palm leaves a hole well above the 6-unit minimum.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8+.
- clearance e0/e1 (error, board stub 3.11 from the finger): fixed. The
  board's bottom edge now stops 9 from each finger wall, so the finger
  passes through a clean opening instead of grazing the stub end.
- no-head (warn): not applicable. The subject is a hand, not a stick
  figure; there is no head to trace, so no human figure is marked.
Lucide construction: `pointer` informed the upright index finger with a
round tip, the knuckle step and the rounded palm; its extra finger scallops
are dropped (they do not survive stroke 4 at 48). The board follows
Lucide's r2 rounded rectangles.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8485b3a4-fcce-4366-a674-06665c2bb463"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1206-finger-touching-board/"
    "finger-touching-board_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# board
L, R, T, B = 6, 42, 6, 21     # board centerline rectangle
RC = 2                         # corner radius
STUB_L, STUB_R = 11, 37        # where the open bottom edge stops

# hand
FX = 24                        # finger axis
FW = 4                         # half finger width (walls FX +- FW)
TIP_Y = 19                     # finger tip arc centre y
KNUCKLE_Y = 30
PALM_X = 40
BASE_Y = 42
CROTCH = (FX - FW, 33)         # thumb leaves the finger here
TC = (14, 33)                  # thumb tip centre
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


class FingerTouchingBoardRedraw(Solo48):
    icon_id = "finger-touching-board-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("touch board", "tap screen", "touchscreen", "pointing hand")
    keywords = ("finger", "touch", "tap", "board", "screen", "whiteboard",
                "pointer", "hand", "interactive", "presentation")

    def build(self) -> None:
        # board: open bottom edge, r2 corners
        self.add_line("board-bottom-left", (STUB_L, B), (L + RC, B))
        self.add_arc("board-corner-bl", (L + RC, B), (L, B - RC), radius_x=RC)
        self.add_line("board-left", (L, B - RC), (L, T + RC))
        self.add_arc("board-corner-tl", (L, T + RC), (L + RC, T), radius_x=RC)
        self.add_line("board-top", (L + RC, T), (R - RC, T))
        self.add_arc("board-corner-tr", (R - RC, T), (R, T + RC), radius_x=RC)
        self.add_line("board-right", (R, T + RC), (R, B - RC))
        self.add_arc("board-corner-br", (R, B - RC), (R - RC, B), radius_x=RC)
        self.add_line("board-bottom-right", (R - RC, B), (STUB_R, B))
        self.add_contour(
            "board", "board-bottom-left", "board-corner-bl", "board-left",
            "board-corner-tl", "board-top", "board-corner-tr", "board-right",
            "board-corner-br", "board-bottom-right")

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
        tip_low = (TC[0] - TR, TC[1] + TR)     # (11,36)
        tip_apex = (TC[0] - TR, TC[1] - TR)    # (11,30)
        tip_high = (TC[0] + TR, TC[1] - TR)    # (17,30)
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
