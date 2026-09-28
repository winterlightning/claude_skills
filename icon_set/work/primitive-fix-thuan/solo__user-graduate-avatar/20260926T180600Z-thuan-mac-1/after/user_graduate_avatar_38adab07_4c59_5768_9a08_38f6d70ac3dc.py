from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '38adab07-4c59-5768-9a08-38f6d70ac3dc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__user-graduate-avatar/20260926T180600Z-thuan-mac-1/reference/user-graduate-avatar_38adab07-4c59-5768-9a08-38f6d70ac3dc.svg'
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
    icon_id = 'user-graduate-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'graduate', 'portrait', 'bust')

    def build(self) -> None:
        # Graduate: mortarboard rhombus resting on the head's crown point, tassel
        # hanging from the right corner, r7 head, shoulders touching the chin.
        _path(self, 'board', (8, 10), [(24, 4), (40, 10), (24, 16), (8, 10)], True)
        self.add_line('tassel', (40, 10), (40, 20))
        self.relate('connect', 'board', 'tassel')
        _circle(self, 'head', 24, 23, 7)
        self.relate('connect', 'board', 'head')
        _path(self, 'shoulders', (8, 44), [((24, 34), 16, 10, True), ((40, 44), 16, 10, True)])
        self.relate('connect', 'head', 'shoulders')
