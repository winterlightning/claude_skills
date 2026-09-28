from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cf3ffa48-69ee-55a9-b0f2-b59ed9778e0e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__farmer-working-long-handled-hoe/20260927T072058Z-thuan-mac-1/reference/harvest farmer_cf3ffa48-69ee-55a9-b0f2-b59ed9778e0e.svg'
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
    icon_id = 'farmer-working-long-handled-hoe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('farmer', 'raking', 'the', 'soil')

    def build(self) -> None:
        # Plan: side-view farmer bent over a hoe, facing left. Hat: 12x8 crown
        # standing on the ends of an r6 face hung from a 16-wide brim, at the
        # top left. The shoulder sits down-right of the chin (9 clear); the
        # hunched back arches up and over to the hip, the legs stride down;
        # the arm reaches down-left to the long hoe handle (slope 1:2) whose
        # blade turns up at the end.
        _path(self, 'hat-crown', (10, 16), [(10, 8), (22, 8), (22, 16)])
        _path(self, 'hat-brim', (8, 16), [(10, 16), (22, 16), (24, 16)])
        self.add_arc('face', (10, 16), (22, 16), radius_x=6, radius_y=6, sweep=False)
        self.relate('connect', 'hat-crown', 'hat-brim')
        self.relate('connect', 'face', 'hat-brim')
        _path(self, 'back', (27, 26), [('c', (30, 21), (34, 19), (38, 19)), ('c', (41, 20), (42, 24), (42, 28))])
        _path(self, 'leg-front', (42, 28), [(34, 40)])
        _path(self, 'leg-back', (42, 28), [(44, 40)])
        self.add_line('arm', (27, 26), (18, 32))
        _path(self, 'hoe', (22, 30), [(18, 32), (6, 38), (4, 34)])
        for a, b in [('back', 'leg-front'), ('back', 'leg-back'), ('leg-front', 'leg-back'), ('back', 'arm'), ('arm', 'hoe')]:
            self.relate('connect', a, b)
