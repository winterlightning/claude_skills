from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3b975376-341b-48a1-92cf-f4ed4b0af1eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__elevator-direction-doors/20260927T153247Z-thuan-mac-1/reference/elevator_3b975376-341b-48a1-92cf-f4ed4b0af1eb.svg'
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
    icon_id = 'elevator-direction-doors'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('elevator doors with directional arrows',)

    def build(self) -> None:
        # Elevator doors, as in the reference: a tall door frame with rounded top corners, split
        # down the middle into two doors; the left door carries an up chevron and the right door a
        # lower down chevron, each spanning its door from wall to wall (a floating chevron cannot
        # keep 8 from both walls of a 16-wide door).
        _path(self, "frame", (8, 44), [(8, 20), (8, 10), ((14, 4), 6, 6, True), (24, 4), (34, 4), ((40, 10), 6, 6, True),
                                       (40, 28), (40, 44), (24, 44), (8, 44)], True)
        self.add_line("split-top", (24, 4), (24, 20))
        self.add_line("split-mid", (24, 20), (24, 28))
        self.add_line("split-low", (24, 28), (24, 44))
        _path(self, "chevron-up", (8, 20), [(16, 12), (24, 20)])
        _path(self, "chevron-down", (24, 28), [(32, 36), (40, 28)])
        for a, b in (("frame", "split-top"), ("split-top", "split-mid"), ("split-mid", "split-low"), ("frame", "split-low"),
                     ("chevron-up", "frame"), ("chevron-up", "split-top"), ("chevron-up", "split-mid"),
                     ("chevron-down", "frame"), ("chevron-down", "split-mid"), ("chevron-down", "split-low")):
            self.relate("connect", a, b)
