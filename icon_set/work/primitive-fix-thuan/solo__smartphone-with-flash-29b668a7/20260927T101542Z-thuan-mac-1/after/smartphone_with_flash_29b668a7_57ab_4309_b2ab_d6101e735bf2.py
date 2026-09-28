from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '29b668a7-57ab-4309-b2ab-d6101e735bf2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smartphone-with-flash-29b668a7/20260927T101542Z-thuan-mac-1/reference/phone selfie_29b668a7-57ab-4309-b2ab-d6101e735bf2.svg'
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
    icon_id = 'smartphone-with-flash-29b668a7'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('smartphone', 'with', 'flash')

    def build(self) -> None:
        # Tall phone (x 14..34, y 16..44) with r4 corners; the middle of its top edge is replaced
        # by a flash burst: a vertical ray and two diagonal rays spreading to the keyshape sides.
        # Screen lines mark the top and bottom bezels.
        _path(self, "body", (18, 16), [((14, 20), 4, 4, False), (14, 25), (14, 36), (14, 40), ((18, 44), 4, 4, False),
                                        (30, 44), ((34, 40), 4, 4, False), (34, 36), (34, 25), (34, 20), ((30, 16), 4, 4, False)])
        self.add_line("screen-top", (14, 25), (34, 25))
        self.add_line("screen-bottom", (14, 36), (34, 36))
        self.relate("connect", "body", "screen-bottom")
        self.relate("connect", "body", "screen-top")
        self.add_line("ray-centre", (24, 4), (24, 8))
        self.add_line("ray-left", (16, 8), (10, 4))
        self.add_line("ray-right", (32, 8), (38, 4))
