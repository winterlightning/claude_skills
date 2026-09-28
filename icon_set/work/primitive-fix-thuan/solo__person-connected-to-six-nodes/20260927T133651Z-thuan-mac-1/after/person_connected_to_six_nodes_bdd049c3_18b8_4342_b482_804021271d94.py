from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bdd049c3-18b8-4342-b482-804021271d94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-connected-to-six-nodes/20260927T133651Z-thuan-mac-1/reference/user network_bdd049c3-18b8-4342-b482-804021271d94.svg'
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
    icon_id = 'person-connected-to-six-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('person', 'connected', 'to', 'six', 'nodes')

    def build(self) -> None:
        # User network: a user bust (r5 head exactly 8 above an r7 shoulder dome) in the centre, with six
        # solid node discs (r2 rings) on the left and right edges, each with a short link pointing in
        # toward the person (links stop at least 8 short of the bust, as in the reference).
        _circle(self, "head", 24, 18, 5)
        self.add_arc("shoulder-left", (17, 38), (24, 31), radius_x=7, radius_y=7, sweep=True)
        self.add_arc("shoulder-right", (24, 31), (31, 38), radius_x=7, radius_y=7, sweep=True)
        self.add_line("body-side-right", (31, 38), (31, 40))
        self.add_line("body-base", (31, 40), (17, 40))
        self.add_line("body-side-left", (17, 40), (17, 38))
        self.add_contour("body", "shoulder-left", "shoulder-right", "body-side-right", "body-base", "body-side-left", closed=True)
        self.mark_human_figure("person", head="head", torso="shoulder-right", torso_junction="start")
        for side, sx in (("left", 1), ("right", -1)):
            X = 24 - 18 * sx  # node column: x=6 on the left, x=42 on the right
            specs = (("top", 10, (X + 2 * sx, 10), (X + 6 * sx, 12), (1, 2) if sx > 0 else (3, 4)),
                     ("middle", 22, (X + 2 * sx, 22), (X + 5 * sx, 22), (1, 2) if sx > 0 else (3, 4)),
                     ("bottom", 38, (X, 36), (X + 3 * sx, 33), (4, 1)))
            for level, cy, start, end, (m1, m2) in specs:
                node = f"node-{side}-{level}"
                _circle(self, node, X, cy, 2)
                self.add_line(f"link-{side}-{level}", start, end)
                self.relate("connect", f"link-{side}-{level}", f"{node}-{m1}", f"{node}-{m2}")
