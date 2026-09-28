from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6fd863d5-f1e3-43e8-a4c6-11996800a801'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bone-in-ham-with-oval-cut-face/20260927T142727Z-thuan-mac-1/reference/sparerib_6fd863d5-f1e3-43e8-a4c6-11996800a801.svg'
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
    icon_id = 'bone-in-ham-with-oval-cut-face'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('ham', 'meat', 'bone', 'food', 'joint', 'cut')

    def build(self) -> None:
        # Bone-in ham lying on its side, as in the reference: a tall oval cut face on the left, the
        # ham body flaring from the oval's top and bottom and narrowing in concave curves to a
        # short shank, and a two-lobed bone knob at the right end. Mirrored about y=24.
        _path(self, "cut-face", (12, 10), [((20, 24), 8, 14, True), ((12, 38), 8, 14, True),
                                           ((4, 24), 8, 14, True), ((12, 10), 8, 14, True)], True)
        _path(self, "body", (12, 10), [('c', (25, 10), (24, 20), (30, 20)), (34, 20),
                                       ((44, 20), 5, 5, True), ((42, 24), 5, 5, True),
                                       ((44, 28), 5, 5, True), ((34, 28), 5, 5, True), (30, 28),
                                       ('c', (24, 28), (25, 38), (12, 38))])
        self.relate("connect", "cut-face", "body")
