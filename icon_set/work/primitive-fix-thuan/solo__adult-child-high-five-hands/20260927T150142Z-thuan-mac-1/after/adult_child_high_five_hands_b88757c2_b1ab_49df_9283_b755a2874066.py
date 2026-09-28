from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b88757c2-b1ab-49df-9283-b755a2874066'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260927T150142Z-thuan-mac-1/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'adult-child-high-five-hands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'family'
    categories = ('primitives', 'family')
    aliases = ()
    keywords = ('adult', 'and', 'child', 'high', 'five')

    def build(self) -> None:
        # high five: a large raised adult hand (three 8-wide fingers sharing their walls, r4 fingertips, open palm)
        # meets a small child's hand reaching up at 45 degrees from the lower left, its r5 fingertip pressed on the
        # adult palm; the child hand passes in front and hides the lower-left of the adult palm
        # child hand: 45-degree tube (sides x+y=47 / x+y=61) with an r5 tip about (22,32) (3-4-5 ends)
        _path(self, "child", (8, 39), [(16, 31), (19, 28), ((26, 35), 5, 5, True, True), (17, 44)])
        # adult hand
        self.add_line("wall-l", (16, 31), (16, 10))
        self.add_arc("tip-1", (16, 10), (24, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-1a", (24, 10), (24, 8))
        self.add_arc("tip-2", (24, 8), (32, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-2a", (32, 8), (32, 10))
        self.add_arc("tip-3", (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_line("wall-r", (40, 10), (40, 44))
        self.add_line("wall-1b", (24, 10), (24, 19))
        self.add_line("wall-2b", (32, 10), (32, 19))
        ring = ["wall-l", "tip-1", "wall-1a", "tip-2", "wall-2a", "tip-3", "wall-r"]
        for a, b in zip(ring, ring[1:]):
            self.relate("connect", a, b)
        for w, n in (("wall-1b", ("tip-1", "wall-1a")), ("wall-2b", ("wall-2a", "tip-3"))):
            for m in n:
                self.relate("connect", w, m)
        self.relate("connect", "wall-l", "child")
