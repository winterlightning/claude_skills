from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7a744411-5fc5-4b46-a2ca-fabc0d60942f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-bumper-emitting-three-sensor-arcs/20260927T144116Z-thuan-mac-1/reference/auto pilot car sound warning_7a744411-5fc5-4b46-a2ca-fabc0d60942f.svg'
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
    icon_id = 'car-bumper-emitting-three-sensor-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('car', 'bumper', 'emitting', 'three', 'sensor', 'arcs')

    def build(self) -> None:
        # Parking sensor: the cropped rear of a car (bumper, boot lid, rear
        # window and wheel) on the right, emitting three concentric sensor
        # arcs to the left, 9 apart, centred on C=(25,24). Arcs are cubic
        # circle segments between integer knots.
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

        wave('wave-1', 25, 24, (24, 21), (22, 24), (24, 27))
        wave('wave-2', 25, 24, (17, 15), (13, 24), (17, 33))
        wave('wave-3', 25, 24, (11, 8), (4, 24), (11, 40))
        _circle(self, 'wheel', 40, 36, 4)
        _path(self, 'body', (36, 36), [
            (35, 36), ((32, 33), 3, 3, True), (32, 27), ((35, 24), 3, 3, True), (36, 24),
            (41, 10), (44, 10),
        ])
        self.relate('connect', 'body', 'wheel')
