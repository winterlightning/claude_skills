"""A three-blade boat propeller: swept blades around a round hub.

Symbol plan: one blade is authored pointing up about the centre (24,24): its root sits on
the hub at (+-3,-7), its leading edge bulges out to the left, the rounded tip reaches
radius 20 at the top and the trailing edge returns nearly straight. The other two blades
are the same blade turned by 120 and 240 degrees (knots rounded to the grid, control
offsets turned exactly), so the sweep keeps its direction like a real propeller. The hub
is a circle (six r8 arcs) through the six blade roots.
Lucide construction: 'fan' - three swept blade lobes around a central hub circle.
Keyshape CIRCLE: blade tips reach centerline radius 19.7-20 about (24,24).
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4b9f4301-4746-5105-a80a-44e05e91227c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__boat-propeller/20260926T030905Z-thuan-mac/reference/boat engine blade_4b9f4301-4746-5105-a80a-44e05e91227c.svg"
AUTHOR = "claude-opus-5-5"

# blade pointing up, relative to the centre: (knot, (offset-in, offset-out)) per node
ROOT_L, ROOT_R = (-3, -7), (3, -7)
BLADE = [
    # knot, control offset arriving, control offset leaving
    (ROOT_L, None, (-1.5, -2.5)),
    ((-10, -14), (0, 3.5), (0, -3.5)),
    ((0, -20), (-5, 0), (3.5, 0)),
    ((7, -15), (0, -3), (0, 4)),
    (ROOT_R, (1.5, -2.5), None),
]


def _turn(p, deg):
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    return (p[0] * c - p[1] * s, p[0] * s + p[1] * c)


class BoatPropeller(Solo48):
    icon_id = "boat-propeller"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/boat"
    aliases = ("boat-engine-blade", "propeller", "screw-propeller")
    keywords = ("propeller", "boat", "ship", "marine", "engine", "blade", "screw", "prop", "fan")

    def build(self) -> None:
        C = 24
        roots = []
        for n, deg in enumerate((0, 120, 240)):
            knots = [tuple(round(v) + C for v in _turn(k, deg)) for k, _, _ in BLADE]
            segs = []
            for i in range(1, len(BLADE)):
                out = _turn(BLADE[i - 1][2], deg)
                inn = _turn(BLADE[i][1], deg)
                a, b = knots[i - 1], knots[i]
                segs.append(((round(a[0] + out[0], 2), round(a[1] + out[1], 2)),
                             (round(b[0] + inn[0], 2), round(b[1] + inn[1], 2)), b))
            self.add_bezier(f"blade-{n + 1}", knots[0], *segs)
            self.relate("connect", "hub", f"blade-{n + 1}")
            roots += [knots[0], knots[-1]]
        roots.sort(key=lambda p: math.atan2(p[1] - C, p[0] - C))
        names = []
        for i, p in enumerate(roots):
            q = roots[(i + 1) % len(roots)]
            self.add_arc(f"hub-{i + 1}", p, q, radius_x=8, sweep=True)
            names.append(f"hub-{i + 1}")
        self.add_contour("hub", *names, closed=True)
