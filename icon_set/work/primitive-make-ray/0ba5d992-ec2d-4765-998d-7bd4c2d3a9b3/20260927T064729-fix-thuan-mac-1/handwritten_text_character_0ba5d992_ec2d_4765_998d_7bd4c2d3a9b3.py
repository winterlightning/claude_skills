from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handwritten-text-character/20260927T061820Z-thuan-mac-1/reference/handwritten text character_0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3.svg'
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
    icon_id = 'handwritten-text-character'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'handwritten-text-character')

    def build(self) -> None:
        # handwritten "M" in one stroke: the left leg sweeps up from the bottom-left corner to a
        # rounded peak, a smooth bowl dips to the valley at mid height, the second rounded peak sits
        # at the top right and the right leg drops straight down the right edge (as in the reference)
        _path(self, "m", (6, 42), [('c', (8, 24), (9, 6), (14, 6)),
                                   ('c', (19, 6), (19, 30), (24, 30)),
                                   ('c', (29, 30), (31, 6), (36, 6)),
                                   ('c', (40, 6), (42, 10), (42, 16)),
                                   (42, 42)])
