from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '438d4d45-f9a0-5f90-b790-f2a7071aea62'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-hair-buns-avatar/20260926T180600Z-thuan-mac-1/reference/user-hair-buns-avatar_438d4d45-f9a0-5f90-b790-f2a7071aea62.svg'
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
    icon_id = 'user-hair-buns-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'hair', 'buns', 'portrait', 'bust')

    def build(self) -> None:
        # Profile facing right (Font Awesome user-hair-buns concept): rounded
        # skull, a bun as a 3/4 lobe at the back of the crown, forehead-nose-chin
        # profile, neck and a shoulder line on each side.
        self.add_bezier('back', (8, 44), ((8, 36), (13, 31), (18, 30)))
        self.add_line('nape', (18, 30), (18, 24))
        self.add_bezier('skull-back', (18, 24), ((14, 22), (12, 18), (13, 15)))
        self.add_arc('bun', (13, 15), (18, 9), radius_x=5, large_arc=True, sweep=True)
        self.add_bezier('crown', (18, 9), ((20, 6), (22, 4), (26, 4)))
        self.add_bezier('forehead', (26, 4), ((30, 4), (33, 6), (34, 10)))
        self.add_line('brow', (34, 10), (34, 14))
        self.add_line('nose-top', (34, 14), (37, 19))
        self.add_line('nose-under', (37, 19), (34, 20))
        self.add_bezier('chin', (34, 20), ((35, 24), (33, 27), (29, 27)))
        self.add_line('neck', (29, 27), (29, 30))
        self.add_bezier('chest', (29, 30), ((35, 30), (40, 36), (40, 44)))
        self.add_contour('profile', 'back', 'nape', 'skull-back', 'bun', 'crown', 'forehead', 'brow',
                         'nose-top', 'nose-under', 'chin', 'neck', 'chest')
        # Hairline: from the brow back over the temple to the nape; hair covers the crown.
        self.add_bezier('hairline', (34, 10), ((28, 13), (22, 16), (18, 24)))
        self.relate('connect', 'hairline', 'profile')
