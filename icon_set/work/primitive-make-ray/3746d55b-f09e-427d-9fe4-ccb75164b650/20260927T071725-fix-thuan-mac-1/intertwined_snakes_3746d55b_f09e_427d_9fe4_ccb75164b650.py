from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__intertwined-snakes/20260927T070909Z-thuan-mac-1/reference/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'
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
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('snake', 'serpent', 'intertwined', 'caduceus', 'mythology', 'coil', 'reptile', 'symbol')

    def build(self) -> None:
        # two snakes winding round each other: mirrored S bodies crossing twice at >30 degrees,
        # r3 heads at the top (they set the x edges), tails at the bottom
        for side, s in (("left", -1), ("right", 1)):
            x = lambda d: 24 + s * d
            _circle(self, f"head-{side}", x(-11), 7, 3)
            _path(self, f"snake-{side}", (x(-11), 10), [
                ('c', (x(-11), 18), (x(11), 16), (x(11), 26)),
                ('c', (x(11), 36), (x(-8), 34), (x(-8), 44)),
            ])
            self.relate("connect", f"head-{side}", f"snake-{side}")
        self.relate("connect", "snake-left", "snake-right")
