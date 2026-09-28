from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efbd83cc-eeb0-52c2-b1f7-2cb051c31e29'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-philosopher-avatar/20260926T175624Z-thuan-mac-1/reference/man philosopher_efbd83cc-eeb0-52c2-b1f7-2cb051c31e29.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'man-philosopher-2-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'philosopher', 'portrait', 'bust')

    def build(self) -> None:
        # Philosopher: bald r10 dome with r3 ears, a moustache-topped beard line
        # across the circular r10 jaw, touching a rounded bust with a V collar.
        # Reference: human_ref/user.svg bust; supplied philosopher drawing.
        _path(self, 'head', (14, 14), [((24, 4), 10, 10, True), ((34, 14), 10, 10, True), ((34, 20), 3, 3, True),
                                      ((24, 30), 10, 10, True), ((14, 20), 10, 10, True), ((14, 14), 3, 3, True)], True)
        _path(self, 'beard', (14, 20), [('c', (18, 22), (21, 18), (24, 18)), ('c', (27, 18), (30, 22), (34, 20))])
        self.relate('connect', 'head', 'beard')
        _path(self, 'body', (8, 44), [((18, 34), 10, 10, True), (24, 34), (30, 34), ((40, 44), 10, 10, True)],
              ids={1: 'body-top', 2: 'body-top-right'})
        self.relate('connect', 'head', 'body')
        _path(self, 'collar', (18, 34), [(24, 44), (30, 34)])
        self.relate('connect', 'collar', 'body')
