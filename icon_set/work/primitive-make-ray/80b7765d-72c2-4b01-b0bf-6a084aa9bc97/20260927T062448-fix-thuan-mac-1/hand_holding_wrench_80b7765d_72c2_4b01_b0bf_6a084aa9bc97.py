from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '80b7765d-72c2-4b01-b0bf-6a084aa9bc97'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260927T055730Z-thuan-mac-1/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg'
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
    icon_id = 'hand-holding-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('wrench', 'hand', 'holding', 'grip', 'repair', 'mechanic', 'fix', 'tool')

    def build(self) -> None:
        # 45-degree axis frame along the handle: ab(a, b) = (18 + a + b, 30 - a + b)
        ab = lambda a, b: (18 + a + b, 30 - a + b)
        # fist: two r6 knuckles on the upper-left side, flat top and bottom, arm leaving down-right
        _path(self, "hand", ab(-6, 6), [
            ab(-6, 4), ab(-6, -6),
            (ab(0, -6), 6, 6, True), (ab(6, -6), 6, 6, True),
            ab(6, 4), ab(6, 18),
        ])
        # handle shows below the fist and runs from its top to the wrench head
        self.add_line("handle-low", ab(-6, 0), ab(-10, 0))
        self.add_line("handle-high", ab(6, 0), (31, 15))
        self.relate("connect", "hand", "handle-low"); self.relate("connect", "hand", "handle-high")
        # open-end head: three quarters of an r5 ring about (34,11), jaw open to the upper right
        self.add_arc("jaw-lower", (39, 11), (31, 15), radius_x=5, sweep=True)
        self.add_arc("jaw-upper", (31, 15), (34, 6), radius_x=5, sweep=True)
        self.add_contour("head", "jaw-lower", "jaw-upper")
        self.relate("connect", "head", "handle-high")
