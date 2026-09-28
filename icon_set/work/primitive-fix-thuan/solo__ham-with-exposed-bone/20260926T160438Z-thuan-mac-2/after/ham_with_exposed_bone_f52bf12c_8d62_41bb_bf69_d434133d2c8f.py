from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f52bf12c-8d62-41bb-bf69-d434133d2c8f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ham-with-exposed-bone/20260926T160438Z-thuan-mac-2/reference/flesh_f52bf12c-8d62-41bb-bf69-d434133d2c8f.svg'
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
    icon_id = 'ham-with-exposed-bone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('ham', 'with', 'exposed', 'bone')

    def build(self) -> None:
        # Plan: ham with exposed bone on SQUARE (naturally asymmetric 3/4 view).
        # Body: one closed outline - round top and left (top y=6, leftmost x=6),
        # bottom sweeping right to the bone knob, which protrudes at the bottom
        # right as three quarters of an r4 circle about (38,38) (its inner quarter
        # hidden in the meat; right x=42, bottom y=42), then the right side back up
        # to the top. The cut edge curves from the top T down to the bottom-left B,
        # splitting the cut face (left) from the skin (right). No mark on the cut
        # face: a dot there reads as an eye.
        T, B = (22, 6), (10, 38)
        _path(self, 'ham', T, [
            ('c', (13, 6), (6, 14), (6, 24)),
            ('c', (6, 31), (7, 35), B),
            ('c', (12, 40), (15, 40), (18, 40)),
            ('c', (24, 40), (30, 39), (34, 38)),
            ((38, 42), 4, 4, False), ((42, 38), 4, 4, False), ((38, 34), 4, 4, False),
            ('c', (38, 28), (38, 20), (36, 15)),
            ('c', (33, 9), (28, 6), T),
        ], closed=True)
        self.add_bezier('cut-edge', T, ((31, 13), (28, 28), B))
        self.relate('connect', 'ham', 'cut-edge')
