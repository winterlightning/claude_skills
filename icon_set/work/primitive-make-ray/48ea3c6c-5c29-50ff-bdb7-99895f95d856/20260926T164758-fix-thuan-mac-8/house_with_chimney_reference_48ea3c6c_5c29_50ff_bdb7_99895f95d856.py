from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '48ea3c6c-5c29-50ff-bdb7-99895f95d856'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__house-with-chimney-reference/20260926T164653Z-thuan-mac/reference/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
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
    icon_id = 'house-with-chimney-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('house', 'home', 'chimney', 'roof', 'door', 'building')

    def build(self) -> None:
        # Plan: house with a chimney as in the reference, on SQUARE (6..42): a
        # 45-degree gable roof from (6,24) up to the apex (24,6) and down to
        # (42,24) that overhangs the walls (x 10/38). The body is one open path:
        # walls from the roof down to r4 rounded bottom corners, a floor on
        # y=42, and an arched door (sides x 18/30, r6 top about (24,34)) that
        # breaks the floor. The chimney is a detached corner bracket at the top
        # right, kept 8 clear of the roof. Everything but the chimney mirrors
        # about x=24.
        _path(self, 'roof', (6, 24), [(10, 20), (24, 6), (38, 20), (42, 24)])
        _path(self, 'body-left', (10, 20), [(10, 38), ((14, 42), 4, 4, False), (18, 42), (18, 34),
                                            ((24, 28), 6, 6, True), ((30, 34), 6, 6, True), (30, 42),
                                            (34, 42), ((38, 38), 4, 4, False), (38, 20)])
        self.relate('connect', 'roof', 'body-left')
        _path(self, 'chimney', (36, 6), [(42, 6), (42, 12)])
