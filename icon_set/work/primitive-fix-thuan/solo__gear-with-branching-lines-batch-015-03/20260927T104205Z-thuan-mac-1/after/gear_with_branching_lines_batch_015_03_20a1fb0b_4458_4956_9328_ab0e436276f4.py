from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '20a1fb0b-4458-4956-9328-ab0e436276f4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gear-with-branching-lines-batch-015-03/20260927T104205Z-thuan-mac-1/reference/set factor standard_20a1fb0b-4458-4956-9328-ab0e436276f4.svg'
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
    icon_id = 'gear-with-branching-lines-batch-015-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('gear', 'branch', 'settings', 'diagram', 'options', 'workflow')

    def build(self) -> None:
        # Plan: left, a six-tooth gear about (16,24): tapered teeth with tips at
        # r12 (+-10 deg) meeting in V valleys at r9, generated from angles, rounded
        # to the grid and mirror-symmetric; hub dot in the middle. The right tooth
        # tip (28,24) runs out as a line to a vertical bus at x=36 spanning the
        # full height; three branches run from the bus to the right edge at the
        # top, middle and bottom (the reference's tiny end dots are dropped).
        pts = [(28, 24), (28, 22), (24, 20), (24, 15), (20, 13), (16, 15), (12, 13), (8, 15),
               (8, 20), (4, 22), (4, 26), (8, 28), (8, 33), (12, 35), (16, 33), (20, 35),
               (24, 33), (24, 28), (28, 26)]
        _path(self, "gear", pts[0], pts[1:] + [pts[0]], True)
        self.add_dot("hub", (16, 24))
        self.add_line("link", (28, 24), (36, 24))
        self.add_line("bus-top", (36, 8), (36, 24))
        self.add_line("bus-bottom", (36, 24), (36, 40))
        for name, y in (("top", 8), ("middle", 24), ("bottom", 40)):
            self.add_line(f"branch-{name}", (36, y), (44, y))
        self.relate("connect", "link", "gear")
        for a in ("bus-top", "bus-bottom", "branch-middle"):
            self.relate("connect", "link", a)
        self.relate("connect", "bus-top", "bus-bottom")
        self.relate("connect", "bus-top", "branch-top")
        self.relate("connect", "bus-top", "branch-middle")
        self.relate("connect", "bus-bottom", "branch-middle")
        self.relate("connect", "bus-bottom", "branch-bottom")
