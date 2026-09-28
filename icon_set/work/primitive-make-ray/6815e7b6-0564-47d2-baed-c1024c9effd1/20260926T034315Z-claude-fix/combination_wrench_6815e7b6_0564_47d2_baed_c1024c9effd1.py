"""A combination wrench: a diagonal spanner with a ring end at the top right and an open jaw at the bottom left.

Symbol plan: the shaft is one straight 45-degree stroke. The ring end is a circle (r5)
split at the shaft's attachment point (a 3-4-5 point on the circle). The open end is a
U jaw facing down-left: a half circle on the 45-degree axis (two cubic quarters through
integer knots at the back and the two tips, radius 4*sqrt2) with a straight prong from
each tip; the back knot is the shaft's lower end. The prongs differ by one unit so the
jaw reaches both the left and bottom envelope edges.
The reference's outlined shaft and small inner hole in the ring head are simplified: an
outlined 45-degree shaft only meets a circle at integer points for a 26-wide ring.
Lucide construction: 'wrench' - diagonal spanner with an open jaw.
Keyshape SQUARE: centerline x 6..42 (upper prong, ring), y 6..42 (ring, lower prong).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6815e7b6-0564-47d2-baed-c1024c9effd1"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__combination-wrench/20260926T034135Z-thuan-mac/reference/tools crescent double_6815e7b6-0564-47d2-baed-c1024c9effd1.svg"
AUTHOR = "claude-opus-5-5"


class CombinationWrench(Solo48):
    icon_id = "combination-wrench"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("wrench", "spanner", "crescent double")
    keywords = ("wrench", "spanner", "tool", "repair", "fix", "settings", "maintenance", "mechanic")

    def build(self) -> None:
        cx, cy, r = 37, 11, 5
        attach = (cx - 4, cy + 3)
        t = 16  # shaft run along (-1, 1)
        back = (attach[0] - t, attach[1] + t)
        jx, jy = back[0] - 4, back[1] + 4
        tip_lo, tip_hi = (jx + 4, jy + 4), (jx - 4, jy - 4)
        k = 0.5523 * 4  # cubic quarter-circle handle, per axis, for radius 4*sqrt2
        # ring
        ring_pts = [attach, (cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ["ring-a", "ring-b", "ring-c", "ring-d", "ring-e"]
        for i, name in enumerate(names):
            self.add_arc(name, ring_pts[i], ring_pts[(i + 1) % len(ring_pts)], radius_x=r)
        self.add_contour("ring", *names, closed=True)
        # shaft
        self.add_line("shaft", attach, back)
        self.relate("connect", "ring", "shaft")
        # jaw: half circle about (jx, jy) from the upper tip, round the back, to the lower tip
        lo_end = (tip_lo[0] - (42 - tip_lo[1]), 42)
        hi_end = (6, tip_hi[1] + (tip_hi[0] - 6))
        self.add_line("prong-hi", hi_end, tip_hi)
        self.add_bezier("jaw-hi", tip_hi, ((tip_hi[0] + k, tip_hi[1] - k), (back[0] - k, back[1] - k), back))
        self.add_bezier("jaw-lo", back, ((back[0] + k, back[1] + k), (tip_lo[0] + k, tip_lo[1] - k), tip_lo))
        self.add_line("prong-lo", tip_lo, lo_end)
        self.add_contour("jaw", "prong-hi", "jaw-hi", "jaw-lo", "prong-lo")
        self.relate("connect", "jaw", "shaft")
