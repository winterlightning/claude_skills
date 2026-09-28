from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1f4d1069-f84c-4b28-abe2-500ccee986de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-with-two-seated-occupants/20260927T144116Z-thuan-mac-1/reference/carpool_1f4d1069-f84c-4b28-abe2-500ccee986de.svg'
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
    icon_id = 'car-with-two-seated-occupants'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'with', 'two', 'seated', 'occupants')

    def build(self) -> None:
        # Carpool: car in side view (bonnet to the right). A tall glass cabin
        # with a slanted rear window and windscreen shows two occupants' heads
        # side by side; a straight-sided body below with two r4 wheels hung
        # from the sill.
        _path(self, 'body', (4, 24), [(8, 24), (40, 24), (44, 24), (44, 32), (36, 32), (12, 32), (4, 32), (4, 24)], closed=True)
        _path(self, 'cabin', (8, 24), [(12, 8), (32, 8), (40, 24)])
        self.relate('connect', 'body', 'cabin')
        self.add_dot('head-rear', (19, 16))
        self.add_dot('head-front', (27, 16))
        _circle(self, 'wheel-rear', 12, 36, 4)
        _circle(self, 'wheel-front', 36, 36, 4)
        self.relate('connect', 'body', 'wheel-rear')
        self.relate('connect', 'body', 'wheel-front')
