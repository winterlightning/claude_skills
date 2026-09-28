from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b191a60a-4e23-4725-b37a-a8e55c809774'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-users-pyramid/20260927T080754Z-thuan-mac-1/reference/multiple users_b191a60a-4e23-4725-b37a-a8e55c809774.svg'
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
    icon_id = 'three-users-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('users', 'group', 'three', 'team', 'people', 'network', 'hierarchy', 'community')

    def build(self) -> None:
        # apex user: head + shoulder arc whose ends tuck behind the two front users' heads below
        _circle(self, "head-top", 24, 12, 6)
        _path(self, "head-l", (11, 32), [((14, 33), 5, 5, True), ((16, 37), 5, 5, True), ((11, 42), 5, 5, True),
                                          ((6, 37), 5, 5, True), ((11, 32), 5, 5, True)], True)
        _path(self, "head-r", (37, 32), [((42, 37), 5, 5, True), ((37, 42), 5, 5, True), ((32, 37), 5, 5, True),
                                          ((34, 33), 5, 5, True), ((37, 32), 5, 5, True)], True)
        _path(self, "shoulders", (14, 33), [((24, 27), 10, 6, True), ((34, 33), 10, 6, True)])
        self.relate("connect", "shoulders-1", "head-l-1")
        self.relate("connect", "shoulders-1", "head-l-2")
        self.relate("connect", "shoulders-2", "head-r-4")
        self.relate("connect", "shoulders-2", "head-r-5")
