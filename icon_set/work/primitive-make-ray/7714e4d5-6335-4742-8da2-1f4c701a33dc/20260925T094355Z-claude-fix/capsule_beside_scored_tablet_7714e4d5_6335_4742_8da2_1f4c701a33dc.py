"""A two-part capsule lying at 45 degrees beside a round scored tablet.

Symbol plan: two round forms share one circular construction. Every curve is a run of
circular cubic arcs about an integer centre, with knots on the integer grid: axis knots
set the keyshape extremes, 45-degree knots carry the joins to straight edges and to the
score line. Capsule: cap centres
A=(12,20) and B=(20,12) on a 45-degree axis, axis knots r6, sides offset +-(4,4), divider
across the middle perpendicular to the axis. Tablet: centre (33,33), axis knots r9, score
line through its (6,6) diagonal knots, parallel to the capsule axis as in the source; each
half keeps a depth of 9 so the halves stay open.
Lucide construction: pill (45-degree capsule with a mid divider) and tablets (round tablet
with a diagonal score).
Keyshape SQUARE: centerline 6..42 -- capsule reaches left and top, tablet right and bottom.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7714e4d5-6335-4742-8da2-1f4c701a33dc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__capsule-beside-scored-tablet/20260925T093141Z-thuan-mac/reference/pills_7714e4d5-6335-4742-8da2-1f4c701a33dc.svg"
AUTHOR = "claude-opus-5-5"


class CapsuleBesideScoredTablet(Solo48):
    icon_id = "capsule-beside-scored-tablet"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical"
    aliases = ("pills", "capsule-and-tablet", "medication")
    keywords = ("pill", "pills", "capsule", "tablet", "medicine", "medication", "drug", "pharmacy")

    def arc(self, name, centre, d0, d1):
        """Circular cubic about centre between the integer knots centre+d0 and centre+d1."""
        cx, cy = centre
        a0, a1 = math.atan2(d0[1], d0[0]), math.atan2(d1[1], d1[0])
        sweep = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        a1 = a0 + sweep
        r0, r1 = math.hypot(*d0), math.hypot(*d1)
        k = 4 / 3 * math.tan(sweep / 4)
        p0, p3 = (cx + d0[0], cy + d0[1]), (cx + d1[0], cy + d1[1])
        c1 = (p0[0] - k * r0 * math.sin(a0), p0[1] + k * r0 * math.cos(a0))
        c2 = (p3[0] + k * r1 * math.sin(a1), p3[1] - k * r1 * math.cos(a1))
        rnd = lambda p: (round(p[0], 3), round(p[1], 3))
        self.add_bezier(name, p0, (rnd(c1), rnd(c2), p3))
        return name

    def build(self) -> None:
        a, b, mid = (12, 20), (20, 12), (16, 16)
        add = lambda p, d: (p[0] + d[0], p[1] + d[1])

        # capsule: cap knots on the axes at r6, side joins at (4,4); clockwise from cap A
        self.add_line("capsule-low-a", add(a, (4, 4)), add(mid, (4, 4)))
        self.add_line("capsule-low-b", add(mid, (4, 4)), add(b, (4, 4)))
        caps_b = [self.arc("cap-b-1", b, (4, 4), (6, 0)), self.arc("cap-b-2", b, (6, 0), (0, -6)),
                  self.arc("cap-b-3", b, (0, -6), (-4, -4))]
        self.add_line("capsule-top-b", add(b, (-4, -4)), add(mid, (-4, -4)))
        self.add_line("capsule-top-a", add(mid, (-4, -4)), add(a, (-4, -4)))
        caps_a = [self.arc("cap-a-1", a, (-4, -4), (-6, 0)), self.arc("cap-a-2", a, (-6, 0), (0, 6)),
                  self.arc("cap-a-3", a, (0, 6), (4, 4))]
        self.add_contour("capsule", "capsule-low-a", "capsule-low-b", *caps_b,
                         "capsule-top-b", "capsule-top-a", *caps_a, closed=True)
        self.add_line("capsule-divider", add(mid, (-4, -4)), add(mid, (4, 4)))
        self.relate("connect", "capsule", "capsule-divider")

        # tablet: axis knots r9, score knots (6,-7)/(-6,7) at r9.2, score roughly parallel to the capsule
        c = (33, 33)
        ring_knots = [(9, 0), (0, 9), (-6, 7), (-9, 0), (0, -9), (6, -7), (9, 0)]
        ring = [self.arc(f"tablet-{i}", c, ring_knots[i], ring_knots[i + 1]) for i in range(6)]
        self.add_contour("tablet", *ring, closed=True)
        self.add_line("tablet-score", add(c, (-6, 7)), add(c, (6, -7)))
        self.relate("connect", "tablet", "tablet-score")
