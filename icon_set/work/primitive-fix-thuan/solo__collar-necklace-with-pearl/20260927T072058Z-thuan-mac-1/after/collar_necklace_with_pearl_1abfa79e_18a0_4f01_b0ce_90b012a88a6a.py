from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1abfa79e-18a0-4f01-b0ce-90b012a88a6a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__collar-necklace-with-pearl/20260927T072058Z-thuan-mac-1/reference/necklace with pearl_1abfa79e-18a0-4f01-b0ce-90b012a88a6a.svg'
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
    icon_id = 'collar-necklace-with-pearl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('collar', 'necklace', 'with', 'pearl')

    def build(self) -> None:
        # Plan (mirrored about x=24): the collar laid flat is a teardrop - round
        # back (r16 about (24,20)) narrowing to a point where the pearl hangs;
        # an inner arch (rx16, ry8) spans the back's ends and leaves the band.
        _path(self, 'collar', (8, 20), [
            ((40, 20), 16, 16, True),
            ('c', (40, 26), (30, 30), (24, 34)),
            ('c', (18, 30), (8, 26), (8, 20)),
        ], True)
        self.add_arc('neckline', (8, 20), (40, 20), radius_x=16, radius_y=8, sweep=True)
        self.relate('connect', 'neckline', 'collar')
        _circle(self, 'pearl', 24, 39, 5)
        self.relate('connect', 'pearl', 'collar')
