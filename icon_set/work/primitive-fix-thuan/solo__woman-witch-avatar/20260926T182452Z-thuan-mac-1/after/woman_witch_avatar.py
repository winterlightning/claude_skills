from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a402ebbf-cb75-5b5e-a59b-2930e0822a8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-witch-avatar/20260926T182452Z-thuan-mac-1/reference/woman-witch-avatar_a402ebbf-cb75-5b5e-a59b-2930e0822a8b.svg'
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
    icon_id = 'woman-witch-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('woman', 'witch', 'portrait', 'bust')

    def build(self) -> None:
        # Witch avatar: a tall pointed hat whose tip flops over to the right and
        # a wide brim sitting on the face. The face is the lower half of an r10
        # head hung from the brim; its jaw touches flat user.svg shoulders.
        self.add_line('brim-left', (8, 18), (14, 18))
        self.add_line('brim-mid', (14, 18), (16, 18))
        self.add_line('brim-mid2', (16, 18), (32, 18))
        self.add_line('brim-mid3', (32, 18), (34, 18))
        self.add_line('brim-right', (34, 18), (40, 18))
        self.add_line('hat-left', (16, 18), (23, 4))
        self.add_line('hat-right', (23, 4), (32, 18))
        self.add_bezier('hat-tip', (23, 4), ((29, 4), (34, 4), (36, 8)))
        _path(self, 'face', (14, 18), [((24, 28), 10, 10, False), ((34, 18), 10, 10, False)])
        _path(self, 'body-left', (8, 44), [(8, 40), ((16, 32), 8, 8, True)])
        self.add_line('body-top', (16, 32), (24, 32))
        self.add_line('body-top-right', (24, 32), (32, 32))
        _path(self, 'body-right', (32, 32), [((40, 40), 8, 8, True), (40, 44)])
        self.add_contour('brim', 'brim-left', 'brim-mid', 'brim-mid2', 'brim-mid3', 'brim-right')
        for a, b in [('brim', 'hat-left'), ('brim', 'hat-right'),
                     ('hat-left', 'hat-right'), ('hat-left', 'hat-tip'), ('hat-right', 'hat-tip'),
                     ('face', 'brim'), ('body-left', 'body-top'), ('body-top', 'body-top-right'),
                     ('body-top-right', 'body-right'), ('face', 'body-top'), ('face', 'body-top-right')]:
            self.relate('connect', a, b)
