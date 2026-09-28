from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '942fd0e9-ec41-5bc3-903c-17e181a32512'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-doctor-hair-mullet-avatar/20260926T180600Z-thuan-mac-1/reference/user-doctor-hair-mullet-avatar_942fd0e9-ec41-5bc3-903c-17e181a32512.svg'
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
    icon_id = 'user-doctor-hair-mullet-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'doctor', 'hair', 'mullet', 'portrait', 'bust')

    def build(self) -> None:
        # Mullet doctor: r10 head with side-swept fringe, the mullet flicks out
        # below the temples, stethoscope on the flat collar line.
        _path(self, 'head', (24, 24), [((14, 14), 10, 10, True), ((24, 4), 10, 10, True),
                                       ((30, 6), 10, 10, True), ((34, 14), 10, 10, True),
                                       ((24, 24), 10, 10, True)], True)
        self.add_bezier('fringe', (14, 14), ((20, 14), (27, 11), (30, 6)))
        self.relate('connect', 'head', 'fringe')
        self.add_bezier('mullet-left', (14, 14), ((13, 17), (12, 19), (9, 21)))
        self.add_bezier('mullet-right', (34, 14), ((35, 17), (36, 19), (39, 21)))
        self.relate('connect', 'head', 'mullet-left')
        self.relate('connect', 'head', 'mullet-right')
        self.relate('connect', 'head', 'body-top')
        self.relate('connect', 'head', 'body-top-right')
        _path(self, 'body-left', (8, 44), [(8, 36), ((16, 28), 8, 8, True)])
        self.add_line('body-top-l', (16, 28), (18, 28))
        self.add_line('body-top', (18, 28), (24, 28))
        self.add_line('body-top-right', (24, 28), (30, 28))
        self.add_line('body-top-r', (30, 28), (32, 28))
        _path(self, 'body-right', (32, 28), [((40, 36), 8, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top-l'), ('body-top-l', 'body-top'), ('body-top', 'body-top-right'),
                     ('body-top-right', 'body-top-r'), ('body-top-r', 'body-right')]:
            self.relate('connect', a, b)
        # Stethoscope: tubes hang from the collar line into an r6 U, stem and r2 chest piece.
        _path(self, 'stethoscope', (18, 28), [(18, 32), ((24, 38), 6, 6, False), ((30, 32), 6, 6, False), (30, 28)])
        for part in ('body-top-l', 'body-top', 'body-top-right', 'body-top-r'):
            self.relate('connect', 'stethoscope', part)
        self.add_line("stem", (24, 38), (24, 39))
        _circle(self, 'chest-piece', 24, 41, 2)
        self.relate('connect', 'stethoscope', 'stem')
        self.relate('connect', 'stem', 'chest-piece')
