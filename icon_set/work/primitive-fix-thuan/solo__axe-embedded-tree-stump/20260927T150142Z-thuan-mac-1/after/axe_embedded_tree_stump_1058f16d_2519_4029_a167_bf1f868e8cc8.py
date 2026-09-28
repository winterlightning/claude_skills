from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1058f16d-2519-4029-a167-bf1f868e8cc8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__axe-embedded-tree-stump/20260927T150142Z-thuan-mac-1/reference/trees chop_1058f16d-2519-4029-a167-bf1f868e8cc8.svg'
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
    icon_id = 'axe-embedded-tree-stump'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('axe', 'in', 'tree', 'stump')

    def build(self) -> None:
        # tree stump with flared roots; an axe head (curved back, pointed beard) sits with its blade buried in the
        # stump top, handle rising to the upper right
        _path(self, "stump", (10, 28), [(14, 28), (28, 28), (36, 28), (36, 37), ('c', (36, 40), (38, 42), (42, 42)),
                                        (6, 42), ('c', (8, 42), (10, 40), (10, 37)), (10, 28)], True)
        _path(self, "head", (14, 28), [('c', (11, 21), (12, 12), (14, 6)), (22, 6), (22, 14), (32, 22), (28, 28)])
        self.add_line("handle", (22, 14), (42, 6))
        self.relate("connect", "head", "stump")
        self.relate("connect", "handle", "head")
