from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '904d0466-8146-5c60-a35f-f40e27fd454e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fan-network-circle/20260927T032037Z-thuan-mac-1/reference/internet of thing analytics_904d0466-8146-5c60-a35f-f40e27fd454e.svg'
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


class Drawing(Solo48):
    icon_id = 'fan-network-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: IoT analytics fan. Big r15 arc about (21,27) (left 6, bottom 42)
        # runs from node A to node C; three r5 nodes A(15,11) B(37,11) C(36,32)
        # meet it and each other at 3-4-5 ring points; three spokes fan from the
        # rim hub P(9,36) to the nodes.
        import math
        def ring(name, c, r, pts):
            cx, cy = c
            pts = sorted(set(pts) | {(cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)},
                         key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
            steps = [(p, r, r, True) for p in pts[1:]] + [(pts[0], r, r, True)]
            _path(self, name, pts[0], steps, True)
        ring('node-a', (15, 11), 5, [(12, 15), (18, 15), (20, 11)])
        ring('node-b', (37, 11), 5, [(34, 15), (37, 16), (32, 11)])
        ring('node-c', (36, 32), 5, [(33, 36), (32, 29), (36, 27)])
        _path(self, 'rim', (12, 15), [((9, 36), 15, 15, False), ((33, 36), 15, 15, False)])
        self.add_line('link-ab', (20, 11), (32, 11))
        self.add_line('link-bc', (37, 16), (36, 27))
        self.add_line('spoke-a', (9, 36), (18, 15))
        self.add_line('spoke-b', (9, 36), (34, 15))
        self.add_line('spoke-c', (9, 36), (32, 29))
        for a, b in [('rim', 'node-a'), ('rim', 'node-c'), ('link-ab', 'node-a'), ('link-ab', 'node-b'),
                     ('link-bc', 'node-b'), ('link-bc', 'node-c'), ('spoke-a', 'node-a'), ('spoke-b', 'node-b'),
                     ('spoke-c', 'node-c'), ('spoke-a', 'rim'), ('spoke-b', 'rim'), ('spoke-c', 'rim'),
                     ('spoke-a', 'spoke-b'), ('spoke-b', 'spoke-c'), ('spoke-a', 'spoke-c')]:
            self.relate('connect', a, b)
