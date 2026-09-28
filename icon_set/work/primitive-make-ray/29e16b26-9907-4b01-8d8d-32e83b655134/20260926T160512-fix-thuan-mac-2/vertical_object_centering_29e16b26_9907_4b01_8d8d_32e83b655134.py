from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '29e16b26-9907-4b01-8d8d-32e83b655134'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vertical-object-centering/20260926T160438Z-thuan-mac-2/reference/align middle move vertical_29e16b26-9907-4b01-8d8d-32e83b655134.svg'
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
    icon_id = 'vertical-object-centering'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('vertical', 'object', 'centering')

    def build(self) -> None:
        # Plan: align-middle (vertical centering) on SQUARE. The object is an upright
        # box 8 wide (26..34) centred on the horizontal guide y=22 (spans 16..28);
        # the guide runs from both edges to the box sides. A down arrow at the upper
        # left points at the guide (tip 8 above it); an up arrow under the box
        # points at it (tip 8 below). Arrows are open chevrons on shafts, as in the
        # reference.
        self.add_polyline('box', (26, 16), (34, 16), (34, 22), (34, 28), (26, 28), (26, 22), closed=True)
        self.add_line('guide-left', (6, 22), (26, 22))
        self.add_line('guide-right', (34, 22), (42, 22))
        self.add_line('arrow-down-shaft', (12, 6), (12, 14))
        self.add_polyline('arrow-down-head', (8, 10), (12, 14), (16, 10))
        self.add_line('arrow-up-shaft', (30, 36), (30, 42))
        self.add_polyline('arrow-up-head', (26, 40), (30, 36), (34, 40))
        self.relate('connect', 'box', 'guide-left')
        self.relate('connect', 'box', 'guide-right')
        self.relate('connect', 'arrow-down-shaft', 'arrow-down-head')
        self.relate('connect', 'arrow-up-shaft', 'arrow-up-head')
