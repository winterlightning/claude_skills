from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a2e89861-f395-4a39-b6ce-109ebb0f1ac0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-with-stacked-roof-luggage/20260927T144116Z-thuan-mac-1/reference/car truck luggage_a2e89861-f395-4a39-b6ce-109ebb0f1ac0.svg'
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
    icon_id = 'car-with-stacked-roof-luggage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'with', 'stacked', 'roof', 'luggage')

    def build(self) -> None:
        # Car with stacked roof luggage (side view): a rounded body box, a
        # trapezoid cabin split into two windows, and on the roof a wide case
        # (its bottom edge is the roof) with a smaller case stacked on its
        # left half; small solid wheels hang under the sill.
        _path(self, 'body', (6, 30), [
            (10, 30), (38, 30), (42, 30), (42, 35), ((39, 38), 3, 3, True), (35, 38), (13, 38), (9, 38), ((6, 35), 3, 3, True), (6, 30),
        ], closed=True)
        _path(self, 'case-lower', (13, 22), [(15, 22), (24, 22), (33, 22), (35, 22), (35, 14), (25, 14), (13, 14), (13, 22)], closed=True)
        _path(self, 'case-upper', (13, 14), [(13, 6), (25, 6), (25, 14)])
        self.add_line('pillar-front', (10, 30), (15, 22))
        self.add_line('pillar-rear', (38, 30), (33, 22))
        self.add_line('pillar-mid', (24, 22), (24, 30))
        for p in ('pillar-front', 'pillar-rear', 'pillar-mid'):
            self.relate('connect', 'body', p)
            self.relate('connect', 'case-lower', p)
        self.relate('connect', 'case-lower', 'case-upper')
        _circle(self, 'wheel-front', 13, 40, 2)
        _circle(self, 'wheel-rear', 35, 40, 2)
        self.relate('connect', 'body', 'wheel-front')
        self.relate('connect', 'body', 'wheel-rear')
