from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c9e24a22-9295-4cdf-847c-570f09ece027'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__beckoning-lucky-cat-with-medallion/20260927T032145Z-thuan-mac-1/reference/lucky cat_c9e24a22-9295-4cdf-847c-570f09ece027.svg'
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
    icon_id = 'beckoning-lucky-cat-with-medallion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('beckoning', 'lucky', 'cat', 'with', 'medallion')

    def build(self) -> None:
        # head: two pointed ears on a flat brow, straight cheeks, chin arc (rx12, ry7) doubling as the collar
        self.add_polyline("head-top", (16, 20), (16, 6), (20, 10), (36, 10), (40, 6), (40, 20))
        self.add_arc("chin", (40, 20), (16, 20), radius_x=12, radius_y=7)
        self.add_dot("eye-left", (24, 18))
        self.add_dot("eye-right", (32, 18))
        # round body hanging from the cheeks
        _path(self, "body", (16, 20), [
            ('c', (16, 24), (6, 26), (6, 32)),
            ((16, 42), 10, 10, False),
            (32, 42), ((42, 32), 10, 10, False),
            ('c', (42, 26), (40, 24), (40, 20)),
        ])
        # raised beckoning paw rising from the left shoulder
        self.add_line("paw", (6, 32), (6, 14))
        for a, b in (("head-top", "chin"), ("head-top", "body"), ("chin", "body"), ("paw", "body")):
            self.relate("connect", a, b)
        # bell medallion hanging from the collar: r3 ring touching the chin's lowest point
        _circle(self, "medallion", 28, 30, 3)
        self.relate("connect", "medallion", "chin")
