from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8d49ce4-e7f0-58f5-b0a4-b166e1534148'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-raising-bottle-in-outstretched-hand/20260927T072841Z-thuan-mac-1/reference/party dance_e8d49ce4-e7f0-58f5-b0a4-b166e1534148.svg'
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
    icon_id = 'person-raising-bottle-in-outstretched-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('person', 'celebrating', 'with', 'bottle')

    def build(self) -> None:
        # walking person raising a bottle (human ref full_body_ref.png): r4 head 8 above the upright
        # torso; raised arm holds the bottle's base, other arm swings back, legs striding
        _circle(self, "head", 16, 10, 4)
        self.add_line("torso", (16, 22), (16, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm-raised", (16, 24), (31, 21))
        self.add_line("arm-back", (16, 24), (8, 25))
        self.add_line("leg-front", (16, 32), (24, 42))
        self.add_line("leg-back", (16, 32), (6, 42))
        # bottle tilted 45 degrees: body 11.3 x 8.5, neck from the middle of its top end
        self.add_polyline("bottle", (28, 18), (36, 10), (42, 16), (34, 24), closed=True)
        self.add_line("bottle-neck", (39, 13), (42, 10))
        for p in ("arm-raised", "arm-back", "leg-front", "leg-back"):
            self.relate("connect", "torso", p)
        for a, b in (("arm-raised", "arm-back"), ("leg-front", "leg-back"), ("arm-raised", "bottle"), ("bottle", "bottle-neck")):
            self.relate("connect", a, b)
