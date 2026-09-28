from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '552e41fd-8718-54f0-8dc4-2a014acdca94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-doctor-hair-long-avatar/20260926T180600Z-thuan-mac-1/reference/user-doctor-hair-long-avatar_552e41fd-8718-54f0-8dc4-2a014acdca94.svg'
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
    icon_id = 'user-doctor-hair-long-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'doctor', 'hair', 'long', 'portrait', 'bust')

    def build(self) -> None:
        # Long-haired doctor: dome hair falling straight to the shoulders at the
        # keyshape sides, centre-parted fringe on an r8 face, stethoscope on the collar.
        _path(self, 'hair', (8, 36), [(8, 12), ((24, 4), 16, 8, True), ((40, 12), 16, 8, True), (40, 36)])
        self.add_bezier('fringe-left', (16, 16), ((20, 16), (23, 15), (24, 13)))
        self.add_bezier('fringe-right', (24, 13), ((25, 15), (28, 16), (32, 16)))
        _path(self, 'jaw', (32, 16), [((24, 24), 8, 8, True), ((16, 16), 8, 8, True)])
        self.add_contour('face-top', 'fringe-left', 'fringe-right')
        self.relate('connect', 'face-top', 'jaw')
        self.relate('connect', 'hair', 'body-left')
        self.relate('connect', 'hair', 'body-right')
        self.relate('connect', 'jaw', 'body-top')
        self.relate('connect', 'jaw', 'body-top-right')
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
