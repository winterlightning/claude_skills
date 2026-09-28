from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '71d9d6f3-339b-435c-af6c-93206931b681'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bottle-and-package-floating-between-water-waves/20260927T072058Z-thuan-mac-1/reference/garbage pollution water_71d9d6f3-339b-435c-af6c-93206931b681.svg'
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
    icon_id = 'bottle-and-package-floating-between-water-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('plastic', 'waste', 'bottle', 'water', 'waves', 'pollution', 'litter', 'ecology')

    def build(self) -> None:
        # Plan: surface wave A carries a tilted box (left) and an upright bottle
        # (right) whose lower parts sink below it; wave B is A moved down 10.
        wave = [(4, 26), (14, 30), (28, 26), (44, 30)]
        _path(self, 'wave-top', wave[0], _smooth(wave))
        low = [(x, y + 10) for x, y in wave]
        _path(self, 'wave-low', low[0], _smooth(low))
        # Tilted package: side vectors (10,4) and (4,-10), bottom edge on the wave.
        _path(self, 'box', (4, 26), [(8, 16), (18, 20), (14, 30)])
        self.relate('connect', 'box', 'wave-top')
        # Bottle: 16-wide body, 45-degree shoulders, 8-wide neck.
        _path(self, 'bottle', (28, 26), [(28, 18), (32, 14), (32, 8), (40, 8), (40, 14), (44, 18), (44, 30)])
        self.relate('connect', 'bottle', 'wave-top')
