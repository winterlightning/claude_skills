"""Afternoon sun: a rayed sun high on the left above the horizon, with the day's
path arcing down from beside it to the horizon on the right.

Symbol plan: the sun is a ring (radius 3, the approved 6-diameter circle) with
eight dot rays: cardinal at distance 12 and diagonal at (9,9), each 9+ from the ring
and 10+ from each other. The horizon is one straight line along the bottom edge.
The day path is a quarter ellipse (rx 8, ry 14 about (36,40)) that leaves the
horizon at the right edge vertically and levels off at (36,26), pointing back at
the sun, 9+ from its nearest rays.
Revision (reviewer: "Make the circle become the sun"): the bare circle now has
rays; the composition of the rejected drawing is kept.
Lucide construction: 'sun' - centre disc with eight rays; 'sunset' horizon line.
Keyshape HRECT_L: centerline x 4 (horizon, left ray + cap) .. 44, y 8 (top ray)
.. 40 (horizon).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3b91179d-54d6-411e-a6dd-c91c93c5edd3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__afternoon-sun/20260926T061914Z-thuan-mac/reference/day afternoon_3b91179d-54d6-411e-a6dd-c91c93c5edd3.svg"
AUTHOR = "claude-opus-5-5"


class AfternoonSun(Solo48):
    icon_id = "afternoon-sun"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("day-afternoon",)
    keywords = ("afternoon", "sun", "day", "time", "horizon", "weather", "sunny")

    def build(self) -> None:
        cx, cy, r = 17, 20, 3
        self.add_arc("sun-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("sun-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour("sun", "sun-top", "sun-bottom", closed=True)
        rays = {"e": (12, 0), "s": (0, 12), "w": (-12, 0), "n": (0, -12),
                "se": (9, 9), "sw": (-9, 9), "nw": (-9, -9), "ne": (9, -9)}
        for name, (dx, dy) in rays.items():
            self.add_dot(f"ray-{name}", (cx + dx, cy + dy))
        self.add_line("horizon", (4, 40), (44, 40))
        self.add_arc("day-path", (44, 40), (36, 26), radius_x=8, radius_y=14, sweep=False)
        self.relate("connect", "horizon", "day-path")
