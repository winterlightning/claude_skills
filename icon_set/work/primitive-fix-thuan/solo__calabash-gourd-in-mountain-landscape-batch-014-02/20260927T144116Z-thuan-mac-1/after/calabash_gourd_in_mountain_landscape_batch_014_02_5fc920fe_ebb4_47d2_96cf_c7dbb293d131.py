from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5fc920fe-ebb4-47d2-96cf-c7dbb293d131'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__calabash-gourd-in-mountain-landscape-batch-014-02/20260927T144116Z-thuan-mac-1/reference/double ninth festival calabash_5fc920fe-ebb4-47d2-96cf-c7dbb293d131.svg'
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
    icon_id = 'calabash-gourd-in-mountain-landscape-batch-014-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('gourd', 'calabash', 'mountain', 'cloud', 'landscape', 'festival')

    def build(self) -> None:
        # Calabash in a mountain landscape: a calabash standing on the ground
        # line in front, on the left (r10 lower bulb and r5 upper bulb joined
        # by 45-degree neck lines at the 6-8-10 / 3-4-5 lattice points), and a
        # tall rounded mountain behind it rising from the ground on the
        # right, whose left flank disappears behind the gourd's upper bulb.
        _path(self, 'gourd', (10, 24), [
            ((16, 42), 10, 10, False), ((22, 24), 10, 10, False), (19, 21), ((20, 14), 5, 5, False),
            ((12, 14), 5, 5, False), ((13, 21), 5, 5, False), (10, 24),
        ], closed=True)
        self.add_line('ground', (16, 42), (42, 42))
        _path(self, 'mountain', (20, 14), [
            ('c', (21, 10), (25, 6), (30, 6)),
            ('c', (36, 6), (42, 16), (42, 42)),
        ])
        self.relate('connect', 'gourd', 'mountain')
        self.relate('connect', 'gourd', 'ground')
        self.relate('connect', 'ground', 'mountain')
