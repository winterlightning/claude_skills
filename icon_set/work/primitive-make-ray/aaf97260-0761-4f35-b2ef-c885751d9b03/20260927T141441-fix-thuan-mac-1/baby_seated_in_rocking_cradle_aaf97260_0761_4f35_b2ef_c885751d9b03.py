from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'aaf97260-0761-4f35-b2ef-c885751d9b03'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-seated-in-rocking-cradle/20260927T141159Z-thuan-mac-1/reference/cradle_aaf97260-0761-4f35-b2ef-c885751d9b03.svg'
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
    icon_id = 'baby-seated-in-rocking-cradle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('baby', 'in', 'rocking', 'cradle')

    def build(self) -> None:
        # Baby in a rocking cradle (reference: a cradle basket between two tall corner posts, standing
        # on a long curved rocker with upturned ends, the baby's round head peeking above the rail).
        # Posts x11/x37 from y10 down to the rocker; basket rails y22 and y30 between them; rocker
        # knots (6,36)-(11,40)-(37,40)-(42,36), the long middle cubic sagging exactly to y42
        # (equal controls 8/3 below). Head r4 about (24,10), 8 above the top rail.
        _circle(self, "head", 24, 10, 4)
        self.add_line("post-left-top", (11, 10), (11, 22))
        self.add_line("post-left-mid", (11, 22), (11, 30))
        self.add_line("post-left-low", (11, 30), (11, 40))
        self.add_line("post-right-top", (37, 10), (37, 22))
        self.add_line("post-right-mid", (37, 22), (37, 30))
        self.add_line("post-right-low", (37, 30), (37, 40))
        self.add_line("rail-top", (11, 22), (37, 22))
        self.add_line("rail-bottom", (11, 30), (37, 30))
        k = 8 / 3
        _path(self, "rocker", (6, 36), [('c', (7, 38), (9, 40), (11, 40)),
                                        ('c', (20, 40 + k), (28, 40 + k), (37, 40)),
                                        ('c', (39, 40), (41, 38), (42, 36))])
        for side in ("left", "right"):
            t, m, l = f"post-{side}-top", f"post-{side}-mid", f"post-{side}-low"
            for a, b in ((t, m), (m, l), (t, "rail-top"), (m, "rail-top"), (m, "rail-bottom"),
                         (l, "rail-bottom"), (l, "rocker")):
                self.relate("connect", a, b)
