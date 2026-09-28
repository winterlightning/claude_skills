from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '41ddc2c0-0c9e-50b6-b43d-69ed1f18ea84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-police-hair-long-2-avatar/20260926T182452Z-thuan-mac-1/reference/user-police-hair-long-2-avatar_41ddc2c0-0c9e-50b6-b43d-69ed1f18ea84.svg'
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
    icon_id = 'user-police-hair-long-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'police', 'hair', 'long', '2', 'portrait', 'bust')

    def build(self) -> None:
        # Policewoman with long hair (redraw of the rejected drawing): peaked cap
        # (triangular crown over a full-width band, tapering to the brow), the
        # face as the lower half of an r10 head hung from the cap, long hair
        # flowing from the temples down and out toward the shoulders, jaw
        # touching flat shoulders. The four "apron" stubs that made the bust read
        # as legs are gone. Mirrored about x=24.
        cx = 24
        _path(self, 'cap', (8, 12), [(cx, 4), (40, 12), (34, 20), (14, 20), (8, 12)], True)
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'cap', 'band')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'cap', 'face')
        for side, s in (('left', -1), ('right', 1)):
            self.add_bezier(f'hair-{side}', (cx + s * 10, 20),
                            ((cx + s * 10, 24), (cx + s * 13, 26), (cx + s * 16, 28)))
            self.relate('connect', f'hair-{side}', 'cap')
            self.relate('connect', f'hair-{side}', 'face')
        top = 34
        _path(self, 'body-left', (8, 44), [(8, 42), ((18, top), 10, 8, True)])
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        _path(self, 'body-right', (30, top), [((40, 42), 10, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top'), ('body-top', 'body-top-right'), ('body-top-right', 'body-right'),
                     ('face', 'body-top'), ('face', 'body-top-right')]:
            self.relate('connect', a, b)
