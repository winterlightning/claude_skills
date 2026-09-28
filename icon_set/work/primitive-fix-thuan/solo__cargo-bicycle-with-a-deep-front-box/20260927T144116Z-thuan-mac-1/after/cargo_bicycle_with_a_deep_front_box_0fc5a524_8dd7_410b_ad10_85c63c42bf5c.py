from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0fc5a524-8dd7-410b-ad10-85c63c42bf5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cargo-bicycle-with-a-deep-front-box/20260927T144116Z-thuan-mac-1/reference/bike cargo_0fc5a524-8dd7-410b-ad10-85c63c42bf5c.svg'
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
    icon_id = 'cargo-bicycle-with-a-deep-front-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cargo', 'bicycle', 'with', 'a', 'deep', 'front', 'box')

    def build(self) -> None:
        # Cargo bike laid out as in the reference: big r7 rear wheel on the
        # left; a deep trapezoid cargo box at the front, riding low, with the
        # small r5 front wheel tucked under its floor; chainstay from the rear
        # wheel to the box floor; seat frame from the rear wheel top to a
        # raked seat post, top tube into the box's 1:3 back wall; handlebar
        # stem rising from the box's back corner.
        _circle(self, 'wheel-rear', 11, 33, 7)
        # Front wheel: r5 about (39,35); its short top arc between the 3-4-5
        # points (36,31)/(42,31) is part of the box floor, the rest hangs below.
        _path(self, 'wheel-front', (42, 31), [((36, 31), 5, 5, True, True)])
        _path(self, 'box', (24, 19), [(44, 19), (42, 31), ((36, 31), 5, 5, False), (28, 31), (27, 28), (25, 22), (24, 19)], closed=True)
        self.add_line('chainstay', (18, 33), (28, 31))
        _path(self, 'frame', (11, 26), [(16, 17), (25, 22)])
        self.add_line('seat-post', (16, 17), (14, 12))
        self.add_line('saddle', (9, 12), (14, 12))
        self.add_line('saddle-nose', (14, 12), (15, 12))
        _path(self, 'handlebar', (24, 19), [(22, 8), (28, 8)])
        for a, b in (('box', 'wheel-front'), ('chainstay', 'wheel-rear'), ('chainstay', 'box'),
                     ('frame', 'wheel-rear'), ('frame', 'box'), ('seat-post', 'frame'),
                     ('seat-post', 'saddle'), ('seat-post', 'saddle-nose'), ('saddle', 'saddle-nose'),
                     ('handlebar', 'box')):
            self.relate('connect', a, b)
