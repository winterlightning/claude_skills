from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-person-squad/20260927T080754Z-thuan-mac-1/reference/symbol squad_47b5d0d4-7421-51e3-82ac-4ebeeb7bce0a.svg'
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
    icon_id = 'three-person-squad'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('squad', 'group', 'people', 'team', 'military', 'person')

    def build(self) -> None:
        # squad: front person (head + rounded torso) with two people behind at the sides, their torsos hidden by the front one
        _circle(self, "head-c", 24, 11, 5)
        _path(self, "body-c", (14, 42), [(14, 32), ((18, 28), 4, 4, True), (30, 28), ((34, 32), 4, 4, True), (34, 42)])
        _circle(self, "head-l", 9, 19, 3)
        _circle(self, "head-r", 39, 19, 3)
        _path(self, "body-l", (6, 42), [(6, 36), ((10, 32), 4, 4, True), (14, 32)])
        _path(self, "body-r", (42, 42), [(42, 36), ((38, 32), 4, 4, False), (34, 32)])
        self.relate("connect", "body-l-3", "body-c-1"); self.relate("connect", "body-l-3", "body-c-2")
        self.relate("connect", "body-r-3", "body-c-4"); self.relate("connect", "body-r-3", "body-c-5")
