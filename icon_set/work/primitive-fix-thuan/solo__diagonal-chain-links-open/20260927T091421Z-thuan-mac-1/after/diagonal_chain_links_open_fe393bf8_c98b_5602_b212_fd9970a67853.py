from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fe393bf8-c98b-5602-b212-fd9970a67853'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-chain-links-open/20260927T091421Z-thuan-mac-1/reference/hyperlink_fe393bf8-c98b-5602-b212-fd9970a67853.svg'
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
    icon_id = 'diagonal-chain-links-open'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('diagonal', 'chain', 'links')

    def build(self) -> None:
        # Two open links on the 45-degree axis, point-symmetric about (24,24): outer caps r10 about
        # (32,16)/(16,32) reach the SQUARE extremes; each inner cap r10 about (27,21)/(21,27) stops at
        # its tip, leaving the links open toward each other.
        _path(self, "link-a", (26, 8), [((32, 6), 10, 10, True), ((42, 16), 10, 10, True), ((40, 22), 10, 10, True),
                                         (33, 29), ((27, 31), 10, 10, True)])
        _path(self, "link-b", (22, 40), [((16, 42), 10, 10, True), ((6, 32), 10, 10, True), ((8, 26), 10, 10, True),
                                          (15, 19), ((21, 17), 10, 10, True)])
