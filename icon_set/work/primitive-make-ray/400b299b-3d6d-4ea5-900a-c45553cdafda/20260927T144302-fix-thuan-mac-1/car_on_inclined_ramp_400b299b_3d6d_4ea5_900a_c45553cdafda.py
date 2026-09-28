from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '400b299b-3d6d-4ea5-900a-c45553cdafda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-on-inclined-ramp/20260927T144116Z-thuan-mac-1/reference/car descending control_400b299b-3d6d-4ea5-900a-c45553cdafda.svg'
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
    icon_id = 'car-on-inclined-ramp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'on', 'inclined', 'ramp')

    def build(self) -> None:
        # Car on an incline (hill-descent control). Everything is built in a
        # 3-4-5 frame along the slope: P(a, b) = O + a*(4,-3) + b*(-3,-4),
        # so every node is on the integer grid. The r5 wheels rest on the
        # slope at their tangent points and carry the body at their tops;
        # the car has a body box (b 2..4) and a cabin (b 4..6).
        ox, oy = 24, 39

        def P(a, b):
            return (ox + 4 * a - 3 * b, oy - 3 * a - 4 * b)

        _path(self, 'slope', (20, 42), [P(0, 0), P(4, 0)])
        for i, a in enumerate((0, 4)):
            _path(self, f'wheel-{i + 1}', P(a, 0), [(P(a, 2), 5, 5, True), (P(a, 0), 5, 5, True)], closed=True)
            self.relate('connect', 'slope', f'wheel-{i + 1}')
            self.relate('connect', 'body', f'wheel-{i + 1}')
        _path(self, 'body', P(-1, 2), [
            P(0, 2), P(4, 2), P(5, 2), P(5, 4), P(4, 4), P(3, 6), P(0, 6), P(-1, 4), P(-1, 2),
        ], closed=True)
