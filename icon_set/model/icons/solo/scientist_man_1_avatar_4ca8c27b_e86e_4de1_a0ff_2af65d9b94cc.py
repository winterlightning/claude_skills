from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ca8c27b-e86e-4de1-a0ff-2af65d9b94cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__scientist-man-1-avatar/20260926T180600Z-thuan-mac-1/reference/scientist man_4ca8c27b-e86e-4de1-a0ff-2af65d9b94cc.svg'
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
    icon_id = 'scientist-man-1-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('scientist', 'man', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Scientist (reference): r10 head with a swept fringe (the reference's
        # centre notch reads as a moustache at 48), round shoulders touching the
        # chin and the lab-coat lapel running from the neck to the lower right.
        _path(self, 'head', (24, 24), [((14, 14), 10, 10, True), ((24, 4), 10, 10, True),
                                       ((30, 6), 10, 10, True), ((34, 14), 10, 10, True),
                                       ((24, 24), 10, 10, True)], True)
        self.add_bezier('fringe', (14, 14), ((20, 14), (27, 11), (30, 6)))
        self.relate('connect', 'head', 'fringe')
        _path(self, 'shoulders', (8, 44), [((24, 28), 16, 16, True), ((40, 44), 16, 16, True)])
        self.relate('connect', 'head', 'shoulders')
        self.add_line('lapel', (24, 28), (31, 44))
        self.relate('connect', 'lapel', 'shoulders')
