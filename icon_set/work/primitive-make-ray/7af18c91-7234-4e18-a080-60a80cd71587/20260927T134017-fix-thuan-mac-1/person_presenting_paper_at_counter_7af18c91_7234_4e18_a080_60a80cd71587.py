from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7af18c91-7234-4e18-a080-60a80cd71587'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-presenting-paper-at-counter/20260927T133650Z-thuan-mac-1/reference/information desk paper_7af18c91-7234-4e18-a080-60a80cd71587.svg'
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
    icon_id = 'person-presenting-paper-at-counter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('counter', 'paper', 'person', 'service', 'desk', 'document')

    def build(self) -> None:
        # Person presenting a paper at a counter, after the reference: a user-style bust at the left
        # (round head exactly 8 above round shoulders) raising one arm to hold up a sheet of paper,
        # beside the service counter at the lower right.
        _circle(self, "head", 11, 11, 5)
        _path(self, "body", (6, 42), [(6, 30), ((12, 24), 6, 6, True), ((18, 30), 6, 6, True), (18, 42)])
        self.add_line("arm", (18, 30), (24, 16))
        _path(self, "paper", (24, 16), [(24, 6), (32, 6), (32, 16), (24, 16)], True)
        self.add_line("counter-top", (28, 30), (42, 30))
        self.add_line("counter-l", (28, 30), (28, 42))
        self.add_line("counter-r", (42, 30), (42, 42))
        self.add_line("counter-b", (28, 42), (42, 42))
        for a, b in (("body", "arm"), ("arm", "paper"), ("counter-top", "counter-l"), ("counter-top", "counter-r"),
                     ("counter-l", "counter-b"), ("counter-r", "counter-b")):
            self.relate("connect", a, b)
