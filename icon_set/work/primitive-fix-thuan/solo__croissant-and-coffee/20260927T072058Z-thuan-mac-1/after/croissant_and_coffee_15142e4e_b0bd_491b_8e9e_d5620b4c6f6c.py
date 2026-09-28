from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '15142e4e-b0bd-491b-8e9e-d5620b4c6f6c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__croissant-and-coffee/20260927T072058Z-thuan-mac-1/reference/croissant_15142e4e-b0bd-491b-8e9e-d5620b4c6f6c.svg'
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
    icon_id = 'croissant-and-coffee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('croissant', 'coffee', 'breakfast', 'bakery', 'cafe', 'pastry', 'food', 'morning')

    def build(self) -> None:
        # Plan: coffee mug on top (body 14x12, D handle rx7), croissant below
        # as a thick crescent with rounded rolled tips and two radial seams
        # (mirrored about x=24).
        _path(self, 'mug', (16, 6), [(30, 6), (30, 8), (30, 16), ('c', (30, 17.2), (29.2, 18), (28, 18)), (18, 18),
                                     ('c', (16.8, 18), (16, 17.2), (16, 16)), (16, 6)], True)
        self.add_arc('handle', (30, 8), (30, 16), radius_x=7, radius_y=4, sweep=True)
        self.relate('connect', 'handle', 'mug')
        _path(self, 'croissant', (6, 30), [
            ('c', (6, 26), (8, 24), (11, 24)),
            ('c', (14, 24), (15, 29), (18, 29)),
            ('c', (22, 31), (26, 31), (30, 29)),
            ('c', (33, 29), (34, 24), (37, 24)),
            ('c', (40, 24), (42, 26), (42, 30)),
            ('c', (42, 34), (39, 38), (34, 40)),
            ('c', (30, 41.6), (27, 42), (24, 42)),
            ('c', (21, 42), (18, 41.6), (14, 40)),
            ('c', (9, 38), (6, 34), (6, 30)),
        ], True)
        self.add_line('seam-left', (18, 29), (14, 40))
        self.add_line('seam-right', (30, 29), (34, 40))
        self.relate('connect', 'seam-left', 'croissant')
        self.relate('connect', 'seam-right', 'croissant')
