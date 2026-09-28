from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f809e2c8-e760-45e6-9aa4-6ffddd73a58f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jackhammer-with-side-handles/20260927T070909Z-thuan-mac-1/reference/construction drill_f809e2c8-e760-45e6-9aa4-6ffddd73a58f.svg'
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


class Drawing(Solo48):
    icon_id = 'jackhammer-with-side-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('jackhammer', 'with', 'side', 'handles')

    def build(self) -> None:
        # jackhammer: rounded body with a switch, side handles, a narrower neck and the chisel bit
        _path(self, "body", (18, 26), [
            (14, 26), (14, 10), ((18, 6), 4, 4, True), (30, 6), ((34, 10), 4, 4, True),
            (34, 26), (30, 26),
        ])
        self.add_line("body-base", (18, 26), (30, 26))
        self.add_dot("switch", (24, 16))
        self.add_line("handle-left", (6, 13), (14, 13))
        self.add_line("handle-right", (34, 13), (42, 13))
        _path(self, "neck", (18, 26), [(18, 30), ((30, 30), 6, 6, False), (30, 26)])
        self.add_line("bit", (24, 36), (24, 42))
        for a, b in (("body", "body-base"), ("handle-left", "body"), ("handle-right", "body"),
                     ("neck", "body-base"), ("neck", "body"), ("bit", "neck")):
            self.relate("connect", a, b)
