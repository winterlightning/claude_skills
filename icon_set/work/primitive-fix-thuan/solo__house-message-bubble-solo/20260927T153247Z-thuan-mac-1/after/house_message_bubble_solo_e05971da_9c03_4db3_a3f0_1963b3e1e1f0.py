from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e05971da-9c03-4db3-a3f0-1963b3e1e1f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-message-bubble-solo/20260927T153247Z-thuan-mac-1/reference/massage bubble with house_e05971da-9c03-4db3-a3f0-1963b3e1e1f0.svg'
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
    icon_id = 'house-message-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('sub icon', 'house message bubble')

    def build(self) -> None:
        def bubble(name):
            """Rounded oval speech bubble (rx18, ry16 about (24,22)) with a tail to the lower left."""
            kx, ky = 18 * 0.66, 16 * 0.66
            _path(self, name, (24, 6), [('c', (24 + kx, 6), (42, 22 - ky), (42, 22)),
                                        ('c', (42, 22 + ky), (24 + kx, 38), (24, 38)),
                                        ('c', (21, 38), (18.5, 37.5), (16, 37)), (8, 42), (9, 32),
                                        ('c', (7, 29), (6, 25.5), (6, 22)),
                                        ('c', (6, 22 - ky), (24 - kx, 6), (24, 6))], True)
        # House message, as in the reference: a rounded oval speech bubble with a pointed tail at
        # its lower left, holding a house: 45-degree gable roof whose eaves overhang the walls, and
        # a plain box body.
        bubble("bubble")
        _path(self, "house", (19, 20), [(24, 15), (29, 20), (29, 29), (19, 29), (19, 20)], True)
        self.add_line("eave-left", (19, 20), (17, 22))
        self.add_line("eave-right", (29, 20), (31, 22))
        self.relate("connect", "house", "eave-left")
        self.relate("connect", "house", "eave-right")
