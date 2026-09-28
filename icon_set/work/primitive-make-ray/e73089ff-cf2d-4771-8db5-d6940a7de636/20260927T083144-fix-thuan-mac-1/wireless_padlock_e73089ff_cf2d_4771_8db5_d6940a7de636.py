from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e73089ff-cf2d-4771-8db5-d6940a7de636'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-padlock/20260927T083044Z-thuan-mac-1/reference/smart lock lock wireless_e73089ff-cf2d-4771-8db5-d6940a7de636.svg'
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
    icon_id = 'wireless-padlock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('padlock', 'lock', 'wireless', 'smart-lock', 'security', 'signal', 'connected')

    def build(self) -> None:
        # Plan: smart padlock as in the reference - r8 semicircle shackle on straight legs (x16/x32)
        # into a wide body (x10..38, y26..42, square centreline corners so the keyhole dot's exact
        # 8 is straight-to-straight), keyhole dot, and one wireless arc on each side of the shackle
        # (r13 arcs about (19,13)/(29,13) on 5-12-13 lattice points, reaching x6 and x42).
        _path(self, "body", (10, 26), [(16, 26), (32, 26), (38, 26), (38, 42), (10, 42), (10, 26)], closed=True)
        _path(self, "shackle", (16, 26), [(16, 14), ((32, 14), 8, 8, True), (32, 26)])
        self.relate("connect", "shackle", "body")
        self.add_dot("keyhole", (24, 34))
        self.add_arc("signal-left", (7, 18), (7, 8), radius_x=13, radius_y=13, sweep=True)
        self.add_arc("signal-right", (41, 8), (41, 18), radius_x=13, radius_y=13, sweep=True)
