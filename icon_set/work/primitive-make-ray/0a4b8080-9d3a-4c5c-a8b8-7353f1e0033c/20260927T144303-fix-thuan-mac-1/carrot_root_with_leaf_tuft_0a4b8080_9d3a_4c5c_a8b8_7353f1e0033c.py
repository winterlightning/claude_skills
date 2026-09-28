from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0a4b8080-9d3a-4c5c-a8b8-7353f1e0033c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__carrot-root-with-leaf-tuft/20260927T144116Z-thuan-mac-1/reference/horseradish_0a4b8080-9d3a-4c5c-a8b8-7353f1e0033c.svg'
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
    icon_id = 'carrot-root-with-leaf-tuft'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('carrot', 'root', 'with', 'leaf', 'tuft')

    def build(self) -> None:
        # Horseradish root on VRECT_M (10..38 x 4..44), mirrored about x=24
        # (Lucide carrot: lens leaves from one crown point B). Root: closed
        # outline from B down rounded shoulders, 1:3 tapering sides and a
        # rounded tip at (24,44). Two lens leaves grow from B to the top
        # corners. Two root-ring notches leave the left flank (one per side
        # read as eyes with the leaves as ears, so both stay on the left).
        B = (24, 16)

        def mx(p):
            return (48 - p[0], p[1])

        for name, X in (('leaf-left', lambda x: x), ('leaf-right', lambda x: 48 - x)):
            _path(self, name, B, [
                ('c', (X(22), 9), (X(19), 4), (X(10), 4)),
                ('c', (X(10), 10), (X(15), 15), B),
            ], closed=True)
        _path(self, 'root', B, [
            ('c', (18, 17), (14, 19), (14, 23)),
            (15, 26), (18, 35), (20, 41),
            ('c', (20.8, 43), (22.3, 44), (24, 44)),
            ('c', (25.7, 44), (27.2, 43), mx((20, 41))),
            mx((14, 23)),
            ('c', (34, 19), (30, 17), B),
        ], closed=True)
        self.add_line('notch-left', (15, 26), (21, 26))
        self.add_line('notch-lower', (18, 35), (21, 35))
        for part in ('leaf-left', 'leaf-right', 'notch-left', 'notch-lower'):
            self.relate('connect', 'root', part)
        self.relate('connect', 'leaf-left', 'leaf-right')
