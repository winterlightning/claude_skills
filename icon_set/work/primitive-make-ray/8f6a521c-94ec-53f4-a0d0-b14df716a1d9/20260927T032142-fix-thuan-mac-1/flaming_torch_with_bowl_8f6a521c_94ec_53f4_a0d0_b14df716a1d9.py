from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8f6a521c-94ec-53f4-a0d0-b14df716a1d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flaming-torch-with-bowl/20260927T032039Z-thuan-mac-1/reference/trends torch_8f6a521c-94ec-53f4-a0d0-b14df716a1d9.svg'
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
    icon_id = 'flaming-torch-with-bowl'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('torch', 'flame', 'fire', 'handle', 'bowl', 'burning')

    def build(self) -> None:
        # Bowl: wide rim (10..38) tapering to a rounded base at y=30; the rim
        # is split where the flame rises from it.
        _path(self, 'bowl', (14, 22), [(34, 22), (38, 22), (35, 28), ((31, 30), 3, 3, True, False),
                                       (17, 30), ((13, 28), 3, 3, True), (10, 22), (14, 22)], True)
        # Flame: three tongues, the tall middle one leaning right, rising from the rim.
        _path(self, 'flame', (14, 22), [('c', (12, 18), (12, 13), (14, 9)), ('c', (16, 12), (19, 14), (22, 14)),
                                        ('c', (21, 9), (24, 6), (29, 4)), ('c', (27, 8), (28, 12), (31, 14)),
                                        ('c', (32, 13), (33, 12), (34, 10)), ('c', (36, 14), (36, 18), (34, 22))])
        self.relate('connect', 'flame-1', 'bowl-1')
        self.relate('connect', 'flame-1', 'bowl-8')
        self.relate('connect', 'flame-6', 'bowl-1')
        self.relate('connect', 'flame-6', 'bowl-2')
        # Handle: cone narrowing to a point under the bowl.
        _path(self, 'handle', (19, 30), [(24, 44), (29, 30)])
        self.relate('connect', 'handle-1', 'bowl-5')
        self.relate('connect', 'handle-2', 'bowl-5')
