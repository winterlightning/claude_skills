from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6972ec9c-e5a0-53f5-9c8e-a492e4824ace'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pajamas-woman-avatar/20260926T180600Z-thuan-mac-1/reference/avatar pajamas woman_6972ec9c-e5a0-53f5-9c8e-a492e4824ace.svg'
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
    icon_id = 'pajamas-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'pajamas', 'woman', 'bust', 'body', 'portrait')

    def build(self) -> None:
        # Bob with centre-parted fringe, r7 face, shoulders (r17) touching the chin
        # and a pajama V collar with a button placket.
        _path(self, 'hair', (8, 24), [(8, 12), ((24, 4), 16, 8, True), ((40, 12), 16, 8, True), (40, 24)])
        self.add_bezier('fringe-left', (17, 16), ((20, 16), (23, 15), (24, 13)))
        self.add_bezier('fringe-right', (24, 13), ((25, 15), (28, 16), (31, 16)))
        self.add_contour('face-top', 'fringe-left', 'fringe-right')
        _path(self, 'jaw', (31, 16), [((24, 23), 7, 7, True), ((17, 16), 7, 7, True)])
        self.relate('connect', 'face-top', 'jaw')
        _path(self, 'shoulder-left', (9, 44), [(9, 36), ((16, 29), 17, 17, True), ((24, 27), 17, 17, True)])
        _path(self, 'shoulder-right', (24, 27), [((32, 29), 17, 17, True), ((39, 36), 17, 17, True), (39, 44)])
        self.relate('connect', 'shoulder-left', 'shoulder-right')
        self.relate('connect', 'jaw', 'shoulder-left')
        self.relate('connect', 'jaw', 'shoulder-right')
        self.add_line('collar-left', (16, 29), (24, 39))
        self.add_line('collar-right', (24, 39), (32, 29))
        self.add_contour('collar', 'collar-left', 'collar-right')
        self.relate('connect', 'collar', 'shoulder-left')
        self.relate('connect', 'collar', 'shoulder-right')
        self.add_line('placket', (24, 39), (24, 44))
        self.relate('connect', 'placket', 'collar')
