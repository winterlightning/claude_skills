from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0cf30456-605b-444e-b6dd-fe7af25447e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__coiled-hose-straight-nozzle/20260927T072058Z-thuan-mac-1/reference/watering pipe_0cf30456-605b-444e-b6dd-fe7af25447e4.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'coiled-hose-straight-nozzle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('coiled', 'garden', 'water', 'hose')

    def build(self) -> None:
        # Plan: straight nozzle on top (8-tall pill: rounded coupling + square
        # spout, split by a seam); the hose leaves the coupling's left cap,
        # loops round the bottom and curls back inward.
        _path(self, 'nozzle', (18, 10), [((22, 6), 4, 4, True), (30, 6), (42, 6), (42, 14), (30, 14), (22, 14),
                                          ((18, 10), 4, 4, True)], True)
        self.add_line('seam', (30, 6), (30, 14))
        self.relate('connect', 'seam', 'nozzle')
        _path(self, 'hose', (18, 10), [
            ('c', (12, 10), (6, 15), (6, 24)),
            ('c', (6, 34), (12, 42), (22, 42)),
            ('c', (32, 42), (38, 38), (38, 32)),
            ('c', (38, 26), (33, 24), (28, 24)),
            ('c', (23, 24), (20, 27), (20, 31)),
        ])
        self.relate('connect', 'nozzle', 'hose')
