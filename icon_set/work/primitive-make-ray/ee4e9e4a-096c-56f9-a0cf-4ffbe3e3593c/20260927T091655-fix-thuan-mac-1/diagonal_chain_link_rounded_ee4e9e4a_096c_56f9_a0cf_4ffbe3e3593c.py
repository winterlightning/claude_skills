from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ee4e9e4a-096c-56f9-a0cf-4ffbe3e3593c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-chain-link-rounded/20260927T091421Z-thuan-mac-1/reference/hyperlink_ee4e9e4a-096c-56f9-a0cf-4ffbe3e3593c.svg'
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
    icon_id = 'diagonal-chain-link-rounded'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('diagonal', 'chain', 'link')

    def build(self) -> None:
        # Diagonal link-2: two U links with round r10 caps about (32,16)/(16,32) on the axis x - y = 0
        # (caps reach the SQUARE extremes), sides on x + y = 34 / 62 ending 8.5 apart, bridged by a bar.
        _path(self, "link-a", (20, 14), [(26, 8), ((32, 6), 10, 10, True), ((42, 16), 10, 10, True),
                                          ((40, 22), 10, 10, True), (34, 28)])
        _path(self, "link-b", (28, 34), [(22, 40), ((16, 42), 10, 10, True), ((6, 32), 10, 10, True),
                                          ((8, 26), 10, 10, True), (14, 20)])
        self.add_line("bar", (17, 31), (31, 17))
