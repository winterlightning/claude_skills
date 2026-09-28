from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b8b0eea-6001-47a8-b251-8639eacba336'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gas-pollution-mask/20260926T152555Z-thuan-mac-2/reference/gas pollution mask_0b8b0eea-6001-47a8-b251-8639eacba336.svg'
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
    icon_id = 'gas-pollution-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('gas', 'pollution', 'mask', 'protection')

    def build(self) -> None:
        # Plan: pollution mask on SQUARE. Outer shape as in the reference: a
        # half-ellipse top (rx18 ry16, top y=6), straight sides x=6/42 from y=22 to
        # y=32, and a half-ellipse bottom (rx18 ry10, bottom y=42). Across it run the
        # mask's upper edge - rising steeply from the left side to a pointed peak
        # (nose bridge) at (18,16), then sloping gently to the right side - and the
        # lower edge, a shallow arch between the side ends. Deliberately asymmetric
        # like the reference; every band stays 9+ clear.
        _path(self, 'outline', (6, 22), [
            ((42, 22), 18, 16, True),
            (42, 32),
            ((6, 32), 18, 10, True),
            (6, 22),
        ], closed=True)
        _path(self, 'mask-top', (6, 22), [
            ('c', (11, 22), (15, 19), (18, 16)),
            ('c', (24, 20), (34, 21), (42, 22)),
        ])
        self.add_bezier('mask-bottom', (6, 32), ((14, 28), (34, 27), (42, 32)))
        self.relate('connect', 'outline', 'mask-top')
        self.relate('connect', 'outline', 'mask-bottom')
