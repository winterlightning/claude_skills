from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5655244e-9c88-42c3-a2be-d90a6fab78b2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__camper-behind-flagged-tent/20260927T144116Z-thuan-mac-1/reference/camping tent person_5655244e-9c88-42c3-a2be-d90a6fab78b2.svg'
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
    icon_id = 'camper-behind-flagged-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('camper', 'tent', 'flag', 'camping', 'person', 'outdoors', 'entrance')

    def build(self) -> None:
        # Camper behind a flagged tent: an A-frame tent (3:7 sides from the
        # apex (18,14) to the ground line) with a door slit, a pole rising to
        # a small solid pennant, and a camper standing behind the tent on the
        # right: r4 ring head resting on a shoulder arch (shared axis x=36)
        # that rises from the tent's right side and drops to the ground.
        _path(self, 'tent', (6, 42), [(18, 42), (30, 42), (42, 42)])
        _path(self, 'tent-sides', (6, 42), [(18, 14), (21, 21), (24, 28), (30, 42)])
        self.relate('connect', 'tent', 'tent-sides')
        self.add_line('door', (18, 42), (18, 35))
        self.relate('connect', 'tent', 'door')
        _path(self, 'flag', (18, 14), [(18, 10), (22, 8), (18, 6), (18, 7)])
        self.relate('connect', 'tent-sides', 'flag')
        _path(self, 'body', (24, 28), [
            ((36, 20), 12, 8, True), ('c', (39, 20), (42, 22), (42, 26)), (42, 42),
        ])
        self.relate('connect', 'tent-sides', 'body')
        self.relate('connect', 'tent', 'body')
        _circle(self, 'head', 36, 12, 4)
        self.relate('connect', 'head', 'body')
