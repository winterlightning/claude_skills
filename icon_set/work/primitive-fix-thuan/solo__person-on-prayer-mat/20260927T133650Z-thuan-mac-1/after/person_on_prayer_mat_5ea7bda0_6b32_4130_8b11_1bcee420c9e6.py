from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5ea7bda0-6b32-4130-8b11-1bcee420c9e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-on-prayer-mat/20260927T133650Z-thuan-mac-1/reference/islamic muslim pray salah_5ea7bda0-6b32-4130-8b11-1bcee420c9e6.svg'
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
    icon_id = 'person-on-prayer-mat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('person', 'headscarf', 'prayer', 'mat', 'kneeling', 'worship')

    def build(self) -> None:
        # Woman in a hijab kneeling on a prayer mat, as in the reference: a tall round hood framing the
        # face opening (an arch open at the chin), the hood's sides sweeping in to the robed body, and
        # a prayer mat drawn in perspective as a trapezoid whose top edge passes behind the body.
        _path(self, "face", (20, 23), [(20, 19), ((28, 19), 4, 4, True), (28, 23)])
        _path(self, "figure", (18, 42), [(18, 32), ('c', (15, 30), (11, 27), (11, 24)), (11, 19), ((37, 19), 13, 13, True),
                                         (37, 24), ('c', (37, 27), (33, 30), (30, 32)), (30, 42)])
        self.add_line("mat-bottom-l", (6, 42), (18, 42))
        self.add_line("mat-bottom-m", (18, 42), (30, 42))
        self.add_line("mat-bottom-r", (30, 42), (42, 42))
        _path(self, "mat-l", (18, 32), [(10, 32), (6, 42)])
        _path(self, "mat-r", (30, 32), [(38, 32), (42, 42)])
        for a, b in (("figure", "mat-bottom-m"), ("mat-bottom-l", "mat-bottom-m"), ("mat-bottom-m", "mat-bottom-r"),
                     ("figure", "mat-l"), ("figure", "mat-r"), ("mat-l", "mat-bottom-l"), ("mat-r", "mat-bottom-r"),
                     ("figure", "mat-bottom-l"), ("figure", "mat-bottom-r")):
            self.relate("connect", a, b)
