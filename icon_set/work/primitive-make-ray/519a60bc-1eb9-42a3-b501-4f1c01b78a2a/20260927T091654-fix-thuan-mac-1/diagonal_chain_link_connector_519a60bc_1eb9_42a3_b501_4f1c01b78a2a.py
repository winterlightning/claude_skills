from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '519a60bc-1eb9-42a3-b501-4f1c01b78a2a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-chain-link-connector/20260927T091421Z-thuan-mac-1/reference/hyperlink_519a60bc-1eb9-42a3-b501-4f1c01b78a2a.svg'
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
    icon_id = 'diagonal-chain-link-connector'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    aliases = ()
    keywords = ('diagonal', 'chain', 'link')

    def build(self) -> None:
        # Diagonal chain: two rounded-rectangle links on the axis x - y = 0, point-symmetric about
        # (24,24), open toward each other and bridged by a centre bar. Corner cubics (cut 6, controls
        # 4 along each side) put their extremes exactly on the SQUARE edges (6 / 42).
        _path(self, "link-a", (20, 14), [(25, 9), ('c', (29, 5), (33, 5), (37, 9)), (39, 11),
                                          ('c', (43, 15), (43, 19), (39, 23)), (34, 28)])
        _path(self, "link-b", (28, 34), [(23, 39), ('c', (19, 43), (15, 43), (11, 39)), (9, 37),
                                          ('c', (5, 33), (5, 29), (9, 25)), (14, 20)])
        self.add_line("bar", (17, 31), (31, 17))
