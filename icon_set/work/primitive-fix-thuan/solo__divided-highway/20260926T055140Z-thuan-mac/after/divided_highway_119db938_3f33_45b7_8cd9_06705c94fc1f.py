"""A divided highway sign: two carriageway edges that bend inward and end in down arrows, with a
U-shaped median between them at the top.

Symbol plan: mirror-symmetric about x = 24 (m(x) = 48 - x). Each lane edge runs down
x = 8 from the top, then makes a tangent-continuous S-bend - an r5 arc (3-4-5 end
points), a straight run along the arc tangent (4, 3), and a second r5 arc returning to
vertical - into x = 16, and continues to the bottom tip (16, 44). An open chevron
arrowhead (12, 40)-(16, 44)-(20, 40) shares that tip; the two inner chevron ends are
exactly 8 apart. The median is a U: verticals x 20 and 28 from y 4 to 14 and an r4
semicircle bottom reaching y 18.
Lucide construction: 'arrow-down' chevron heads on Lucide-style smooth bends ('split').
Keyshape VRECT_L: centerline x 8..40 (upper lane edges), y 4..44 (tops, arrow tips).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "119db938-3f33-45b7-8cd9-06705c94fc1f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__divided-highway/20260926T055140Z-thuan-mac/reference/divided highway_119db938-3f33-45b7-8cd9-06705c94fc1f.svg"
AUTHOR = "claude-opus-5-5"


class DividedHighway(Solo48):
    icon_id = "divided-highway"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/traffic"
    aliases = ("divided highway", "dual carriageway", "median ahead")
    keywords = ("highway", "road", "sign", "traffic", "median", "divided", "lanes", "carriageway", "split")

    def lane(self, side, m):
        p = [m((8, 4)), m((8, 22)), m((10, 26)), m((14, 29)), m((16, 33)), m((16, 44))]
        sweep = side == "left"
        self.add_line(f"{side}-upper", p[0], p[1])
        self.add_arc(f"{side}-bend-1", p[1], p[2], radius_x=5, sweep=not sweep)
        self.add_line(f"{side}-bend-run", p[2], p[3])
        self.add_arc(f"{side}-bend-2", p[3], p[4], radius_x=5, sweep=sweep)
        self.add_line(f"{side}-lower", p[4], p[5])
        self.add_contour(f"{side}-lane", f"{side}-upper", f"{side}-bend-1", f"{side}-bend-run",
                         f"{side}-bend-2", f"{side}-lower")
        self.add_polyline(f"{side}-arrow", m((12, 40)), p[5], m((20, 40)))
        self.relate("connect", f"{side}-lane", f"{side}-arrow")

    def build(self) -> None:
        self.lane("left", lambda q: q)
        self.lane("right", lambda q: (48 - q[0], q[1]))
        self.add_line("median-left", (20, 4), (20, 14))
        self.add_arc("median-bottom", (20, 14), (28, 14), radius_x=4, sweep=False)
        self.add_line("median-right", (28, 14), (28, 4))
        self.add_contour("median", "median-left", "median-bottom", "median-right")
