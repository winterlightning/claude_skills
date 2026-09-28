from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'baa1fd0f-249e-41b9-9925-8471559e72c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fish-and-hook/20260927T032145Z-thuan-mac-1/reference/fish with a line_baa1fd0f-249e-41b9-9925-8471559e72c2.svg'
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
    icon_id = 'fish-and-hook'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('fishing', 'fish', 'hook', 'angling', 'sea', 'catch', 'hobby', 'line')

    def build(self) -> None:
        # fishing line dropping into a U hook (r6 about (12,36)) whose point turns back up
        _path(self, "line", (6, 6), [(6, 36), ((12, 42), 6, 6, False), ((18, 36), 6, 6, False)])
        # fish facing the hook: lens body nose (16,20) to tail joint (34,20), triangular tail fin
        _path(self, "body", (16, 20), [
            ('c', (20, 8), (30, 8), (34, 20)),
            ('c', (30, 32), (20, 32), (16, 20)),
        ], closed=True)
        _path(self, "tail", (34, 20), [(42, 12), (42, 28), (34, 20)], closed=True)
        self.relate("connect", "body", "tail")
        self.add_dot("eye", (25, 20))
