from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6175b21e-96a2-4503-a4cc-6b0bc36376c0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fresh-carrot-batch-011-12/20260926T152555Z-thuan-mac-2/reference/carrot_6175b21e-96a2-4503-a4cc-6b0bc36376c0.svg'
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
    icon_id = 'fresh-carrot-batch-011-12'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('food', 'state')
    aliases = ()
    keywords = ('carrot', 'vegetable', 'root', 'leaves', 'food', 'produce')

    def build(self) -> None:
        # Plan: carrot on VRECT_M (10..38 x 4..44), mirrored about x=24 (Lucide carrot:
        # lens leaves from one base point). Root: closed outline from the crown B down
        # rounded shoulders, 1:3 tapering sides and a rounded tip at (24,44). Two
        # lens leaves grow from B to the top corners (10,4) and (38,4). Two notch
        # marks leave the left side at integer points of the 1:3 side line.
        B = (24, 16)
        def mx(p):
            return (48 - p[0], p[1])
        for name, X in (('leaf-left', lambda x: x), ('leaf-right', lambda x: 48 - x)):
            _path(self, name, B, [
                ('c', (X(22), 9), (X(19), 4), (X(10), 4)),
                ('c', (X(10), 10), (X(15), 15), B),
            ], closed=True)
        _path(self, 'root', B, [
            ('c', (18, 17), (14, 19), (14, 23)),
            (15, 26), (18, 35), (20, 41),
            ('c', (20.8, 43), (22.3, 44), (24, 44)),
            ('c', (25.7, 44), (27.2, 43), mx((20, 41))),
            mx((14, 23)),
            ('c', (34, 19), (30, 17), B),
        ], closed=True)
        self.add_line('notch-upper', (15, 26), (21, 26))
        self.add_line('notch-lower', (18, 35), (21, 35))
        self.relate('connect', 'root', 'leaf-left')
        self.relate('connect', 'root', 'leaf-right')
        self.relate('connect', 'leaf-left', 'leaf-right')
        self.relate('connect', 'root', 'notch-upper')
        self.relate('connect', 'root', 'notch-lower')
