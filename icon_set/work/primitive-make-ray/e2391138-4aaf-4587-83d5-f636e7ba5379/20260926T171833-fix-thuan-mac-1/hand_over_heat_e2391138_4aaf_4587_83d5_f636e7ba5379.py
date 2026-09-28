from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260926T171707Z-thuan-mac-1/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
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
    icon_id = 'hand-over-heat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('hand', 'heat', 'warm', 'hot', 'temperature', 'steam', 'burn', 'sensation')

    def build(self) -> None:
        # Flat hand, palm down, index finger pointing down-left along (-4,3): an r5 cap about
        # (11,16) with 3-4-5 side points (8,12)/(14,20); the back runs level at y=6, the thumb
        # is tucked under the finger, the palm base sits at y=25 and a 3-4-5 wrist rises right.
        # The palm base is a standalone line so its exact 8 gap to the heat certifies.
        _path(self, 'hand', (34, 6), [(16, 6), (8, 12), ((14, 20), 5, 5, False), (18, 17), (18, 21),
                                       ((22, 25), 4, 4, False)])
        self.add_line('palm', (22, 25), (30, 25))
        self.add_line('wrist', (30, 25), (42, 9))
        self.relate('connect', 'hand', 'palm')
        self.relate('connect', 'palm', 'wrist')
        # Gap between the index finger and the thumb.
        self.add_line('thumb-top', (18, 17), (25, 17))
        self.relate('connect', 'hand', 'thumb-top')
        # Rising heat: three in-phase S waves, 12 apart, 8 below the palm.
        for i, x in enumerate((12, 24, 36)):
            self.add_bezier(f'heat-{i}', (x, 33), ((x - 3, 36), (x + 3, 39), (x, 42)))
