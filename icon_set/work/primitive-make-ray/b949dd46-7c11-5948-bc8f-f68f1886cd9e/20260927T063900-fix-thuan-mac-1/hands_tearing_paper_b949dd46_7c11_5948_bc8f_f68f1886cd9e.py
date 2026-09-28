from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b949dd46-7c11-5948-bc8f-f68f1886cd9e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-tearing-paper/20260927T061820Z-thuan-mac-1/reference/contract break_b949dd46-7c11-5948-bc8f-f68f1886cd9e.svg'
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
    icon_id = 'hands-tearing-paper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('hands', 'tearing', 'paper')

    def build(self) -> None:
        # a sheet torn in two, mirrored about x=24: each half tilts outward (top corner by the tear)
        # with a jagged tear edge facing the other half. A hand grips each half's lower outer
        # corner: r4 thumb arc in front of the paper, forearm (8 wide) running down to the edge.
        for side, mirror in (("left", False), ("right", True)):
            m = (lambda p: (48 - p[0], p[1])) if mirror else (lambda p: p)
            _path(self, f"half-{side}", m((4, 26)), [m((4, 14)), m((16, 8)), m((19, 15)), m((18, 19)), m((19, 22)),
                                                     m((12, 26)), (m((8, 22)), 4, 4, mirror),
                                                     (m((4, 26)), 4, 4, mirror)], closed=True)
            self.add_line(f"arm-out-{side}", m((4, 26)), m((4, 40)))
            self.add_line(f"arm-in-{side}", m((12, 26)), m((12, 40)))
            self.relate("connect", f"arm-out-{side}", f"half-{side}")
            self.relate("connect", f"arm-in-{side}", f"half-{side}")
