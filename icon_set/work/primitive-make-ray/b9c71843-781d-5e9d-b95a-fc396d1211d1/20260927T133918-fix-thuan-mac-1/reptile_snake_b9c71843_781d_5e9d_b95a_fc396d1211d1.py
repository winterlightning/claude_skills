from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b9c71843-781d-5e9d-b95a-fc396d1211d1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__slithering-snake/20260927T133651Z-thuan-mac-1/reference/reptile snake_b9c71843-781d-5e9d-b95a-fc396d1211d1.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'slithering-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('snake', 'slither', 'serpent', 'reptile', 'zigzag', 'coil', 'python', 'wild')

    def build(self) -> None:
        # Snake in profile (reference: a thick outlined body band that winds back on itself, tail up at the
        # top right, head below). Body band 8 thick: the tail run tapers to a point at the top right, turns
        # round the left (outer r12 / inner r4), and runs right into a rounded oval head with one eye.
        # Members are standalone and connected in order so the exact-8 band walls certify.
        steps = [("tail-top", 'c', (42, 10), ((38, 6), (35, 6), (32, 6))), ("back-top", 'l', (32, 6), (18, 6)),
                 ("turn-outer-1", 'a', (18, 6), (6, 18), 12, 12, False), ("turn-outer-2", 'a', (6, 18), (18, 30), 12, 12, False),
                 ("belly", 'l', (18, 30), (22, 30)), ("jaw", 'l', (22, 30), (22, 42)), ("chin", 'l', (22, 42), (30, 42)),
                 ("snout-low", 'a', (30, 42), (42, 32), 12, 10, False), ("snout-high", 'a', (42, 32), (30, 22), 12, 10, False),
                 ("crown", 'l', (30, 22), (18, 22)),
                 ("turn-inner-1", 'a', (18, 22), (14, 18), 4, 4, True), ("turn-inner-2", 'a', (14, 18), (18, 14), 4, 4, True),
                 ("back-under", 'l', (18, 14), (32, 14)), ("tail-under", 'c', (32, 14), ((35, 14), (38, 14), (42, 10)))]
        names = []
        for step in steps:
            name, kind = step[0], step[1]
            if kind == 'l':
                self.add_line(name, step[2], step[3])
            elif kind == 'a':
                self.add_arc(name, step[2], step[3], radius_x=step[4], radius_y=step[5], sweep=step[6])
            else:
                self.add_bezier(name, step[2], step[3])
            names.append(name)
        for a, b in zip(names, names[1:] + names[:1]):
            self.relate("connect", a, b)
        self.add_dot("eye", (32, 31))
