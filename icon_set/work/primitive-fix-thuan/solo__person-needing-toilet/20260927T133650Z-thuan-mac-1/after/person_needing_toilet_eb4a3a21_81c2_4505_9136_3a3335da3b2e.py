from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eb4a3a21-81c2-4505-9136-3a3335da3b2e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-needing-toilet/20260927T133650Z-thuan-mac-1/reference/toilet need_eb4a3a21-81c2-4505-9136-3a3335da3b2e.svg'
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
    icon_id = 'person-needing-toilet'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'toilet', 'urgency', 'restroom', 'crossed', 'legs')

    def build(self) -> None:
        # Person urgently needing the toilet, as in the reference: a round head exactly 8 above a
        # round-shouldered body whose forearms fold in so both hands meet at the crotch, and
        # knock-kneed legs whose knees press in toward each other before the feet splay out.
        _circle(self, "head", 24, 9, 5)
        _path(self, "body", (10, 30), [((18, 22), 8, 8, True), (30, 22), ((38, 30), 8, 8, True)])
        self.add_line("arm-l1", (10, 30), (17, 32))
        self.add_line("arm-l2", (17, 32), (24, 34))
        self.add_line("arm-r1", (38, 30), (31, 32))
        self.add_line("arm-r2", (31, 32), (24, 34))
        _path(self, "leg-l", (17, 32), [(19, 41), (16, 44)])
        _path(self, "leg-r", (31, 32), [(29, 41), (32, 44)])
        for a, b in (("body", "arm-l1"), ("body", "arm-r1"), ("arm-l1", "arm-l2"), ("arm-r1", "arm-r2"), ("arm-l2", "arm-r2"),
                     ("arm-l1", "leg-l"), ("arm-l2", "leg-l"), ("arm-r1", "leg-r"), ("arm-r2", "leg-r")):
            self.relate("connect", a, b)
