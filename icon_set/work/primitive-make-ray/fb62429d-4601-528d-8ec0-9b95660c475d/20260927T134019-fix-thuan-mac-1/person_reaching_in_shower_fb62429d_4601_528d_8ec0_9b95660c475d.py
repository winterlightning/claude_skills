from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fb62429d-4601-528d-8ec0-9b95660c475d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-in-shower/20260927T133650Z-thuan-mac-1/reference/bathroom shower person_fb62429d-4601-528d-8ec0-9b95660c475d.svg'
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
    icon_id = 'person-reaching-in-shower'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('person', 'reaching', 'in', 'shower')

    def build(self) -> None:
        # Person under a shower, as in the reference: a dome shower head hanging from its pipe at the
        # upper left spraying two streams, and a bust at the right (round head exactly 8 above round
        # shoulders) with one arm bent up at the elbow, reaching toward the top.
        self.add_line("stem", (10, 8), (10, 12))
        self.add_arc("rose-l", (4, 18), (10, 12), radius_x=6, radius_y=6, sweep=True)
        self.add_arc("rose-r", (10, 12), (16, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_contour("rose", "rose-l", "rose-r")
        self.relate("connect", "stem", "rose")
        self.add_line("spray-l", (5, 27), (4, 33))
        self.add_line("spray-r", (13, 27), (14, 33))
        _circle(self, "head", 30, 18, 5)
        _path(self, "shoulders", (22, 40), [(22, 35), ((26, 31), 4, 4, True), (34, 31)])
        self.add_line("side", (34, 31), (34, 40))
        self.add_line("upper-arm", (34, 31), (44, 27))
        self.add_line("forearm", (44, 27), (44, 8))
        for a, b in (("shoulders", "side"), ("shoulders", "upper-arm"), ("side", "upper-arm"), ("upper-arm", "forearm")):
            self.relate("connect", a, b)
