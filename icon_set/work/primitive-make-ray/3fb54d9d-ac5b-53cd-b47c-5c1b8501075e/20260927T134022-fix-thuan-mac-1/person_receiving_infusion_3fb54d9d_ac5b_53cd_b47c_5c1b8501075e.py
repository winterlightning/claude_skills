from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3fb54d9d-ac5b-53cd-b47c-5c1b8501075e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-receiving-infusion-3fb54d9d/20260927T133650Z-thuan-mac-1/reference/transfusion human_3fb54d9d-ac5b-53cd-b47c-5c1b8501075e.svg'
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
    icon_id = 'person-receiving-infusion-3fb54d9d'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('person', 'receiving', 'infusion')

    def build(self) -> None:
        # Patient receiving an infusion, as in the reference: a user-style bust at the lower left
        # (round head exactly 8 above broad round shoulders), a tall IV pole at the right on a foot,
        # its arm carrying a hanging drip bag, and the drip line curving from the bag down to the
        # patient's shoulder.
        _circle(self, "head", 13, 17, 5)
        _path(self, "body", (6, 42), [(6, 36), ((12, 30), 6, 6, True), (16, 30), ((22, 36), 6, 6, True), (22, 42)])
        self.add_line("pole", (42, 6), (42, 42))
        self.add_line("foot", (34, 42), (42, 42))
        self.add_line("arm", (42, 6), (30, 6))
        self.add_line("hanger", (30, 6), (30, 14))
        _path(self, "bag", (30, 14), [(34, 14), (34, 24), (26, 24), (26, 14), (30, 14)], True)
        self.add_bezier("drip", (30, 24), ((30, 32), (26, 34), (22, 36)))
        for a, b in (("pole", "foot"), ("pole", "arm"), ("arm", "hanger"), ("hanger", "bag"), ("bag", "drip"), ("drip", "body")):
            self.relate("connect", a, b)
