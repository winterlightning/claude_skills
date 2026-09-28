from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cab49e44-2820-52d2-8488-be5ad9fc1d3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-christian-1-avatar/20260926T175624Z-thuan-mac-1/reference/man-christian-1-avatar_cab49e44-2820-52d2-8488-be5ad9fc1d3a.svg'
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
    icon_id = 'man-christian-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('man', 'christian', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Christian man: r8 head with a side-swept fringe touching a rounded
        # bust (human_ref/user.svg shoulders) that carries a Latin cross on the
        # chest; the flat shoulder top is a standalone straight contour so the
        # cross top certifies at exactly 8.
        _path(self, 'head', (16, 12), [((24, 4), 8, 8, True), ((32, 12), 8, 8, True),
                                      ((24, 20), 8, 8, True), ((16, 12), 8, 8, True)], True)
        _path(self, 'hair', (16, 12), [('c', (19, 8), (26, 11), (32, 12))])
        self.relate('connect', 'head', 'hair')
        _path(self, 'shoulders', (16, 24), [(24, 24), (32, 24)], ids={0: 'body-top', 1: 'body-top-right'})
        _path(self, 'body-left', (8, 44), [((16, 24), 8, 20, True)])
        _path(self, 'body-right', (32, 24), [((40, 44), 8, 20, True)])
        self.relate('connect', 'shoulders', 'body-left')
        self.relate('connect', 'shoulders', 'body-right')
        self.relate('connect', 'head', 'shoulders')
        self.add_line('cross-stem', (24, 32), (24, 44))
        self.add_line('cross-arm', (20, 36), (28, 36))
        self.relate('connect', 'cross-stem', 'cross-arm')
