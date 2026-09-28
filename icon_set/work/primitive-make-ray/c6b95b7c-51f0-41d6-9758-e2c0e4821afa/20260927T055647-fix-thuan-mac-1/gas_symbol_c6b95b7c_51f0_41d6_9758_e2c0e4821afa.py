from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6b95b7c-51f0-41d6-9758-e2c0e4821afa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gas-symbol/20260927T055612Z-thuan-mac-1/reference/gas_c6b95b7c-51f0-41d6-9758-e2c0e4821afa.svg'
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
    icon_id = 'gas-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('gas', 'symbol')

    def build(self) -> None:
        # Plan: mirrored about x=24. Lid line y6 (x12..36) capping a neck
        # (x16/x32, y6..14); flat shoulders at y14 into a wide body
        # (x6..42, y14..42) with r6 corners.
        self.add_line('lid-l', (12, 6), (16, 6))
        self.add_line('lid-m', (16, 6), (32, 6))
        self.add_line('lid-r', (32, 6), (36, 6))
        _path(self, 'jar', (16, 6), [(16, 14), (12, 14), ((6, 20), 6, 6, False), (6, 36), ((12, 42), 6, 6, False),
                                     (36, 42), ((42, 36), 6, 6, False), (42, 20), ((36, 14), 6, 6, False),
                                     (32, 14), (32, 6)])
        for a, b in [('lid-l', 'lid-m'), ('lid-m', 'lid-r'), ('jar', 'lid-l'), ('jar', 'lid-m'), ('jar', 'lid-r')]:
            self.relate('connect', a, b)
