from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5d4383cc-7fa3-4af5-b119-dc3b67d08db0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__burger-beside-drink-cup/20260927T142733Z-thuan-mac-1/reference/fast food burger drink_5d4383cc-7fa3-4af5-b119-dc3b67d08db0.svg'
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
    icon_id = 'burger-beside-drink-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('burger', 'beside', 'drink', 'cup')

    def build(self) -> None:
        # Tall tapered cup at the back left with a slanted straw crossing its rim,
        # and a burger in front at the right: domed top bun (9 tall), patty wider
        # than the buns (r4 caps, 8 tall) and a bottom bun (9 tall). The cup's
        # right wall disappears behind the bun dome and its base runs into the
        # burger's base line.
        _path(self, 'bun-top', (22, 27), [(22, 23), ((27, 18), 5, 5, True), (31, 18), ((36, 23), 5, 5, True), (36, 27)])
        _path(self, 'patty', (22, 27), [(36, 27), ((36, 35), 4, 4, True), (22, 35), ((22, 27), 4, 4, True)], closed=True)
        _path(self, 'bun-bottom', (22, 35), [(22, 39), ((27, 44), 5, 5, False), (31, 44), ((36, 39), 5, 5, False), (36, 35)])
        _path(self, 'cup', (27, 18), [(27, 10), (19, 10), (8, 10), (10, 44), (27, 44)])
        _path(self, 'straw', (18, 13), [(19, 10), (21, 4)])
        for a, b in (('bun-top', 'patty'), ('patty', 'bun-bottom'), ('cup', 'bun-top'), ('cup', 'bun-bottom'), ('straw', 'cup')):
            self.relate('connect', a, b)
