from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ba2928f2-1522-47a1-b82a-642cd2a72da4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__parent-child-raised-arms/20260927T084830Z-thuan-mac-1/reference/parent with kids babies_ba2928f2-1522-47a1-b82a-642cd2a72da4.svg'
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
    icon_id = 'parent-child-raised-arms'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'family'
    categories = ('primitives', 'family')
    aliases = ()
    keywords = ('parent', 'and', 'child')

    def build(self) -> None:
        # parent with a child above, both with arms raised (reference): each figure is a head
        # cradled by a rounded V of raised arms; the child's small hands tip over outward, the
        # parent's long arms reach up past its head. Before drew straight-sided U cups that read
        # as bowls.
        _circle(self, "child-head", 24, 7, 3)
        a = 14 / 3
        _path(self, "child-arms", (9, 12), [
            (11, 8), (13, 12), ('c', (13 + a, 12 + 2 * a), (35 - a, 12 + 2 * a), (35, 12)), (37, 8), (39, 12)])
        _circle(self, "parent-head", 24, 31, 3)
        b = 16 / 3
        _path(self, "parent-arms", (8, 26), [
            (13, 36), ('c', (13 + b, 36 + 2 * b), (35 - b, 36 + 2 * b), (35, 36)), (40, 26)])
