"""combine-harvester-front-header (redraw of the new-pipeline traced SVG).

Plan: a combine harvester seen from the front, mirrored about x=24 on
HRECT_L (centerline box (4,8)-(44,40)).
- reel: one closed stadium contour, y 20..30, r5 end arcs centred (9,25) and
  (39,25) that reach x=4 and x=44. Its top and bottom walls are split at
  x=17 and x=31 so every attachment shares an endpoint.
- cab: an upright trapezoid, top (15,8)-(33,8), feet on the reel top at
  (17,20) and (31,20); the reel's top wall closes it.
- bars: two verticals x=17 and x=31 across the reel, continuing the cab
  sides, so the reel reads as three bays (13 / 14 / 13 wide).
- wheels: each is the part of a r5.8 circle (two cubics, knot at the
  bottom; arcs need integer radii) hanging below the reel's bottom wall, its chord from the reel corner (9,30) to the bar foot (17,30) and its
  bottom on y=40; the reel hides the top of the wheel, as in the image.
  Depth 10 below the wall gives the wheel opening its 6-unit hole.
One axis ties cab feet, bars and wheel ends together, so there is no
near-miss between them. Traced shape: combine-harvester-front-header_raw.svg,
read for proportion only. No useful Lucide match (Lucide has tractor but no
combine / header).

Keyshape: HRECT_L instead of the suggested HRECT_M. Stacking cab (12),
reel (10) and wheel (10) with every hole at least 6 needs 32 of height;
HRECT_M has 28. HRECT_L fills both axes exactly.

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (warn): fixed; the cab top sits on y=8 and the wheel
  bottoms on y=40, so HRECT_L is filled on both axes.
- clearance e0/e2, e0/e5, e1/e3, e1/e5 (wheel dots 3 apart from bars and
  reel, 4 errors): fixed; wheels are now arcs that share endpoints with the
  reel and bar feet.
- clearance e2/e4, e3/e4 (bars 4.9 from cab feet, 2 errors): fixed; bars and
  cab feet share the points (17,20) and (31,20).
- holes 2.2 wide in the reel bays (3 errors): fixed; the reel is 10 tall and
  its bays 13-14 wide, so each opening is 6 x 9 or more.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "44ee4e62-4052-5cd9-b8ce-7733bb2ccec0"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1040-combine-harvester-front-header/"
    "combine-harvester-front-header_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
REEL_TOP, REEL_BOTTOM, REEL_R = 20, 30, 5
REEL_END = 9           # where the end arcs meet the straight walls
BAR_X = 17             # bars, cab feet and wheel inner ends
CAB_TOP, CAB_TOP_X = 8, 15
WHEEL_BOTTOM = 40
# Wheel circle through (9,30), (17,30) and (13,40): half chord 4, depth 10.
_HALF, _DEPTH = (BAR_X - REEL_END) / 2, WHEEL_BOTTOM - REEL_BOTTOM
WHEEL_R = (_HALF ** 2 + _DEPTH ** 2) / (2 * _DEPTH)  # 5.8, not on grid 1


def wheel(x0, x1):
    """Two cubics from (x0,30) down round (cx,40) to (x1,30) on the r5.8 circle."""
    cx, cy = (x0 + x1) / 2, WHEEL_BOTTOM - WHEEL_R
    a0 = math.atan2(REEL_BOTTOM - cy, x0 - cx)          # upper-left start
    a0 = a0 if a0 > 0 else a0 + 2 * math.pi
    turn = (math.pi / 2 - a0)                           # to the bottom point
    k = 4 / 3 * math.tan(turn / 4)

    def pt(a):
        return cx + WHEEL_R * math.cos(a), cy + WHEEL_R * math.sin(a)

    def ctrl(a, sign):
        x, y = pt(a)
        return (round(x - sign * k * WHEEL_R * math.sin(a), 3),
                round(y + sign * k * WHEEL_R * math.cos(a), 3))

    a1, a2 = math.pi / 2, math.pi - a0                  # bottom, upper-right end
    return (
        (ctrl(a0, 1), ctrl(a1, -1), (cx, WHEEL_BOTTOM)),
        (ctrl(a1, 1), ctrl(a2, -1), (x1, REEL_BOTTOM)),
    )


def mx(x):
    return 2 * AXIS - x


class CombineHarvesterFrontHeaderRedraw(Solo48):
    icon_id = "combine-harvester-front-header-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/vehicles"
    aliases = ("combine harvester", "harvester header", "combine")
    keywords = ("combine", "harvester", "header", "reel", "farm", "agriculture", "harvest", "vehicle")

    def build(self) -> None:
        top, bot = REEL_TOP, REEL_BOTTOM
        # Reel stadium, walked clockwise from the top-left corner.
        self.add_line("reel-top-l", (REEL_END, top), (BAR_X, top))
        self.add_line("reel-top-m", (BAR_X, top), (mx(BAR_X), top))
        self.add_line("reel-top-r", (mx(BAR_X), top), (mx(REEL_END), top))
        self.add_arc("reel-end-r", (mx(REEL_END), top), (mx(REEL_END), bot), radius_x=REEL_R)
        self.add_line("reel-bot-r", (mx(REEL_END), bot), (mx(BAR_X), bot))
        self.add_line("reel-bot-m", (mx(BAR_X), bot), (BAR_X, bot))
        self.add_line("reel-bot-l", (BAR_X, bot), (REEL_END, bot))
        self.add_arc("reel-end-l", (REEL_END, bot), (REEL_END, top), radius_x=REEL_R)
        self.add_contour(
            "reel", "reel-top-l", "reel-top-m", "reel-top-r", "reel-end-r",
            "reel-bot-r", "reel-bot-m", "reel-bot-l", "reel-end-l", closed=True,
        )

        self.add_polyline(
            "cab", (BAR_X, top), (CAB_TOP_X, CAB_TOP), (mx(CAB_TOP_X), CAB_TOP), (mx(BAR_X), top),
        )

        self.add_line("bar-l", (BAR_X, top), (BAR_X, bot))
        self.add_line("bar-r", (mx(BAR_X), top), (mx(BAR_X), bot))

        # Wheels: major arcs below the reel wall, drawn outer end to bar foot.
        self.add_bezier("wheel-l", (REEL_END, bot), *wheel(REEL_END, BAR_X))
        self.add_bezier("wheel-r", (mx(BAR_X), bot), *wheel(mx(BAR_X), mx(REEL_END)))

        for part in ("cab", "bar-l", "bar-r", "wheel-l", "wheel-r"):
            self.relate("connect", part, "reel")
        for side in ("l", "r"):
            self.relate("connect", "cab", f"bar-{side}")
            self.relate("connect", f"wheel-{side}", f"bar-{side}")
