from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-property-value-solo/20260926T164653Z-thuan-mac/reference/house dollar_ec996bcb-4c1a-4d3c-84fb-8218d5fa19b8.svg'
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
    icon_id = 'house-property-value-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: house with a dollar sign as in the reference, on VRECT_L
        # (x 8..40, y 4..44): 11:16 gable roof from the apex (24,4) to the eaves
        # (8,15)/(40,15), straight walls with r4 rounded bottom corners, and a
        # standalone floor line so the $ can sit exactly 8 above it.
        # The $ is a Lucide-style S of two r4 arcs on three levels 8 apart
        # (y 17/25/33, point-symmetric about (24,25)) with short bar ticks above
        # and below; a bar through the S cannot keep 8 from its own curves, and
        # the ticks stop 8 short of the roof and floor.
        _path(self, 'house', (12, 44), [
            ((8, 40), 4, 4, True), (8, 15), (24, 4), (40, 15), (40, 40), ((36, 44), 4, 4, True),
        ])
        self.add_line('floor', (36, 44), (12, 44))
        self.relate('connect', 'house', 'floor')
        _path(self, 'dollar-s', (28, 17), [
            (24, 17), (21, 17), ((21, 25), 4, 4, False), (27, 25), ((27, 33), 4, 4, True), (24, 33), (20, 33),
        ])
        self.add_line('tick-top', (24, 14), (24, 17))
        self.add_line('tick-bottom', (24, 33), (24, 36))
        self.relate('connect', 'dollar-s', 'tick-top')
        self.relate('connect', 'dollar-s', 'tick-bottom')
