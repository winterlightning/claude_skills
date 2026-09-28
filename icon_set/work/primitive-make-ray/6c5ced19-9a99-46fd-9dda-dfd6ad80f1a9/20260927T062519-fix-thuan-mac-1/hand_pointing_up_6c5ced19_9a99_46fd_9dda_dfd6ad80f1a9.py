from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-up/20260927T055730Z-thuan-mac-1/reference/finger point 1_6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9.svg'
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
    icon_id = 'hand-pointing-up'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'pointing', 'up', 'index', 'finger', 'gesture')

    def build(self) -> None:
        # hand pointing up: index finger (8 wide, r4 tip), two folded knuckles, thumb out to the upper
        # left (8.5 wide, r6 tip whose leftmost point is its lower end), open wrist
        _path(self, "hand", (14, 42), [
            (14, 36), (6, 28),                          # wrist, thumb lower edge
            ((12, 22), 6, 6, True),                     # thumb tip
            (16, 26),                                   # thumb upper edge into the crotch
            (16, 10), ((24, 10), 4, 4, True),           # index finger (top y=6)
            (24, 18), ((32, 18), 4, 4, True),           # first folded knuckle
            (32, 21), ((42, 21), 5, 5, True),           # second knuckle (x=42)
            (42, 32),
            ('c', (42, 38), (38, 40), (36, 42)),        # heel of the hand into the wrist
        ])
