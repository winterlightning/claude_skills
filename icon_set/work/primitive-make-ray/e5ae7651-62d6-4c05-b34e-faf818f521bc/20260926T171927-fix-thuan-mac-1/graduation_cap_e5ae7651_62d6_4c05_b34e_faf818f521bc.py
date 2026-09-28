from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__graduation-cap-symbol/20260926T171659Z-thuan-mac-1/reference/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'
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
    icon_id = 'graduation-cap-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('graduation', 'cap', 'symbol')

    def build(self) -> None:
        # Mortarboard on HRECT_L, mirrored about x=24: a 1:2 diamond board
        # (4,18)-(24,8)-(44,18)-(24,28); the cap band hangs from the board's
        # lower edges at x=12/36 and closes with a shallow r20 arc (4 deep) at y=40.
        _path(self, 'board', (24, 8), [(44, 18), (36, 22), (24, 28), (12, 22), (4, 18), (24, 8)], closed=True)
        _path(self, 'band', (12, 22), [(12, 36), ((36, 36), 20, 20, False), (36, 22)])
        self.relate('connect', 'board', 'band')
