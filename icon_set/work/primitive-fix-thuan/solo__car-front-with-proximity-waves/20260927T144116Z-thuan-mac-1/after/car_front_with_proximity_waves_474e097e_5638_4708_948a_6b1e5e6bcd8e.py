from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '474e097e-5638-4708-948a-6b1e5e6bcd8e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-front-with-proximity-waves/20260927T144116Z-thuan-mac-1/reference/auto pilot car rear warning_474e097e-5638-4708-948a-6b1e5e6bcd8e.svg'
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
    icon_id = 'car-front-with-proximity-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'front', 'with', 'proximity', 'waves')

    def build(self) -> None:
        # Front proximity warning: the cropped nose of a car (bumper, bonnet
        # and belt line, windscreen up to the roof, front wheel) on the
        # right, with two proximity waves centred on C=(26,24) to its left
        # (radii about 13 and 22, 9 apart), drawn as cubic circle segments
        # between integer knots.
        import math

        def wave(name, cx, cy, top, mid, bottom):
            members = []
            for i, (p, q) in enumerate(((top, mid), (mid, bottom))):
                a0 = math.atan2(p[1] - cy, p[0] - cx)
                a1 = math.atan2(q[1] - cy, q[0] - cx)
                r0 = math.hypot(p[0] - cx, p[1] - cy)
                r1 = math.hypot(q[0] - cx, q[1] - cy)
                d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
                k = 4 / 3 * math.tan(d / 4)
                c1 = (p[0] - k * r0 * math.sin(a0), p[1] + k * r0 * math.cos(a0))
                c2 = (q[0] + k * r1 * math.sin(a1), q[1] - k * r1 * math.cos(a1))
                m = f'{name}-{i + 1}'
                self.add_bezier(m, p, (c1, c2, q))
                members.append(m)
            self.add_contour(name, *members)

        wave('wave-inner', 26, 24, (16, 16), (13, 24), (16, 32))
        wave('wave-outer', 26, 24, (12, 8), (4, 24), (12, 40))
        _circle(self, 'wheel', 37, 36, 4)
        _path(self, 'body', (33, 36), [
            (29, 36), ((26, 33), 3, 3, True), (26, 26), ((29, 23), 3, 3, True), (31, 23),
            (37, 8), (44, 8),
        ])
        self.add_line('belt', (31, 23), (44, 23))
        self.add_line('sill', (41, 36), (44, 36))
        self.relate('connect', 'body', 'wheel')
        self.relate('connect', 'body', 'belt')
        self.relate('connect', 'sill', 'wheel')
