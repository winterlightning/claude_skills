from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f540eba4-5f02-4b15-ab87-852a4076e2c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-circle-leaves/20260927T032037Z-thuan-mac-1/reference/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'
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
    icon_id = 'hierarchy-circle-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'state')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: org chart mirrored about x=24. Root box (16,6)-(32,14); stem
        # (24,14)-(24,22) to a bus y22 (x12..36); drops to two r6 leaf circles
        # about (12,36)/(36,36) that set the left, right and bottom extremes.
        _path(self, 'root', (24, 14), [(16, 14), (16, 6), (32, 6), (32, 14), (24, 14)], True)
        self.add_line('stem', (24, 14), (24, 22))
        self.add_line('bus-l', (12, 22), (24, 22))
        self.add_line('bus-r', (24, 22), (36, 22))
        self.add_line('drop-l', (12, 22), (12, 30))
        self.add_line('drop-r', (36, 22), (36, 30))
        _circle(self, 'leaf-l', 12, 36, 6)
        _circle(self, 'leaf-r', 36, 36, 6)
        for a, b in [('root', 'stem'), ('stem', 'bus-l'), ('stem', 'bus-r'), ('bus-l', 'bus-r'),
                     ('bus-l', 'drop-l'), ('bus-r', 'drop-r'), ('drop-l', 'leaf-l'), ('drop-r', 'leaf-r')]:
            self.relate('connect', a, b)
