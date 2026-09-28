from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-graduate-avatar/20260926T175624Z-thuan-mac-1/reference/man graduate_7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False, ids=None):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = (ids or {}).get(i, f"{name}-{i + 1}")
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
    icon_id = 'man-graduate-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'graduate', 'portrait', 'bust')

    def build(self) -> None:
        # Graduate: a full-width mortarboard (3:8 rhombus) sits directly on the
        # head -- the face sides rise into its lower edges -- with a tassel cord
        # hanging from its left corner; circular r8 jaw touching a rounded bust
        # with a V collar.  Reference: human_ref/user.svg shoulders.
        _path(self, 'board', (8, 10), [(24, 4), (40, 10), (32, 13), (24, 16), (16, 13), (8, 10)], True)
        _path(self, 'face', (16, 13), [(16, 22), ((32, 22), 8, 8, False), (32, 13)])
        self.relate('connect', 'board', 'face')
        self.add_line('tassel', (8, 10), (8, 24))
        self.relate('connect', 'board', 'tassel')
        _path(self, 'body', (8, 44), [((18, 34), 10, 10, True), (24, 34), (30, 34), ((40, 44), 10, 10, True)],
              ids={1: 'body-top', 2: 'body-top-right'})
        self.relate('connect', 'face', 'body')
        _path(self, 'collar', (18, 34), [(24, 44), (30, 34)])
        self.relate('connect', 'collar', 'body')
