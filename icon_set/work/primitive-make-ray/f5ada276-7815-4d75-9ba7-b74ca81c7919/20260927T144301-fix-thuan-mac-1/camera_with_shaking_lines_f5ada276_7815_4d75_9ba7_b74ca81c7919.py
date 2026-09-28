from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f5ada276-7815-4d75-9ba7-b74ca81c7919'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__camera-with-shaking-lines/20260927T144116Z-thuan-mac-1/reference/camera settings frame 1_f5ada276-7815-4d75-9ba7-b74ca81c7919.svg'
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
    icon_id = 'camera-with-shaking-lines'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('camera', 'with', 'shaking', 'lines')

    def build(self) -> None:
        # Camera shake: a landscape camera body with a low viewfinder hump on
        # top and a centred r3 lens ring, flanked by two vertical shake lines.
        # The body edges are standalone lines joined by r3 corner arcs so the
        # exact 8-unit gaps (lens to walls, shake lines to sides) certify.
        self.add_line('side-left', (12, 19), (12, 35))
        self.add_line('side-right', (36, 19), (36, 35))
        self.add_line('base', (15, 38), (33, 38))
        self.add_line('top-left', (15, 16), (18, 16))
        self.add_line('top-right', (30, 16), (33, 16))
        _path(self, 'hump', (18, 16), [(20, 10), (28, 10), (30, 16)])
        _path(self, 'corner-tl', (12, 19), [((15, 16), 3, 3, True)])
        _path(self, 'corner-tr', (33, 16), [((36, 19), 3, 3, True)])
        _path(self, 'corner-br', (36, 35), [((33, 38), 3, 3, True)])
        _path(self, 'corner-bl', (15, 38), [((12, 35), 3, 3, True)])
        ring = ['side-left', 'corner-tl', 'top-left', 'hump', 'top-right', 'corner-tr',
                'side-right', 'corner-br', 'base', 'corner-bl']
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate('connect', a, b)
        _circle(self, 'lens', 24, 27, 3)
        self.add_line('shake-left', (4, 19), (4, 35))
        self.add_line('shake-right', (44, 19), (44, 35))
