from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8dd89814-5165-5a73-b29f-bad43339ce91'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-chef-hair-long-avatar/20260926T180600Z-thuan-mac-1/reference/user-chef-hair-long-avatar_8dd89814-5165-5a73-b29f-bad43339ce91.svg'
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
    icon_id = 'user-chef-hair-long-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'chef', 'hair', 'long', 'portrait', 'bust')

    def build(self) -> None:
        # Chef with long hair: three-lobed toque (r5, r6, r5 half circles) on a
        # full-width band, hair falling straight from under the band, r8 face whose
        # forehead is the band, broad shoulders touching the chin.
        _path(self, 'toque', (8, 16), [(8, 10), ((18, 10), 5, 5, True), ((30, 10), 6, 6, True),
                                       ((40, 10), 5, 5, True), (40, 16)])
        self.add_line('band-left', (8, 16), (16, 16))
        self.add_line('band', (16, 16), (32, 16))
        self.add_line('band-right', (32, 16), (40, 16))
        self.add_line('hair-left', (8, 16), (8, 26))
        self.add_line('hair-right', (40, 16), (40, 26))
        for a, b in [('toque', 'band-left'), ('band-left', 'band'), ('band', 'band-right'), ('band-right', 'toque'),
                     ('hair-left', 'toque'), ('hair-left', 'band-left'), ('hair-right', 'toque'), ('hair-right', 'band-right')]:
            self.relate('connect', a, b)
        _path(self, 'face', (16, 16), [(16, 20), ((24, 28), 8, 8, False), ((32, 20), 8, 8, False), (32, 16)])
        for part in ('band-left', 'band', 'band-right'):
            self.relate('connect', 'face', part)
        _path(self, 'shoulders', (8, 44), [((24, 32), 16, 12, True), ((40, 44), 16, 12, True)])
        self.relate('connect', 'face', 'shoulders')
