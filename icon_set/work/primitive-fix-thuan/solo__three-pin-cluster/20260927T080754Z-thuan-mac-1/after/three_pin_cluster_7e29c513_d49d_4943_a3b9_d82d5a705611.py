from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7e29c513-d49d-4943-a3b9-d82d5a705611'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-pin-cluster/20260927T080754Z-thuan-mac-1/reference/trip pin multiple_7e29c513-d49d-4943-a3b9-d82d5a705611.svg'
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
    icon_id = 'three-pin-cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'maps'
    categories = ('maps', 'primitives')
    aliases = ()
    keywords = ('pins', 'locations', 'multiple', 'trip', 'map', 'places', 'markers', 'route')

    def build(self) -> None:
        # front map pin (r8 head about (24,26), tail to (24,42)); two back pins behind it, heads in the top corners, pointed tips out at the sides
        _path(self, "front", (24, 42), [('c', (21, 39), (16, 32), (16, 26)), ((24, 18), 8, 8, True),
                                         ((32, 26), 8, 8, True), ('c', (32, 32), (27, 39), (24, 42))], True)
        k = 0.5523 * 8
        for s, f in (("l", lambda x: x), ("r", lambda x: 48 - x)):
            P = lambda x, y: (f(x), y)
            _path(self, f"back-{s}", P(16, 26), [P(8, 33), ("c", P(7, 27), P(6, 20), P(6, 14)),
                                                   ('c', P(6, 14 - k), P(14 - k, 6), P(14, 6)),
                                                   ('c', P(14 + k, 6), P(22, 10), P(24, 18))])
            a, b = ("front-1", "front-2") if s == "l" else ("front-3", "front-4")
            self.relate("connect", f"back-{s}-1", a); self.relate("connect", f"back-{s}-1", b)
            self.relate("connect", f"back-{s}-4", "front-2"); self.relate("connect", f"back-{s}-4", "front-3")
        self.relate("connect", "back-l-4", "back-r-4")
