from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bean/20260927T032145Z-thuan-mac-1/reference/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'
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
    icon_id = 'bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('bean', 'peanut', 'legume', 'seed', 'food', 'vegan', 'nut', 'coffee')

    def build(self) -> None:
        # kidney bean on the diagonal: convex back (lower-right), shallow notch (upper-left)
        _path(self, "bean", (32, 6), [
            ('c', (38, 6), (42, 12), (42, 18)),
            ('c', (42, 30), (30, 42), (18, 42)),
            ('c', (10, 42), (6, 38), (6, 32)),
            ('c', (6, 25), (12, 20), (18, 16)),
            ('c', (24, 12), (26, 6), (32, 6)),
        ], closed=True)
        # highlight stroke parallel to the notch, bowing toward the back
        self.add_bezier("highlight", (16, 30), ((23, 28), (28, 23), (30, 16)))
