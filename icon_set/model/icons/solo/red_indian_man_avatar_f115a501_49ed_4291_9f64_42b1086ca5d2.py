from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f115a501-49ed-4291-9f64-42b1086ca5d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__red-indian-man-avatar/20260926T180600Z-thuan-mac-1/reference/red indian man_f115a501-49ed-4291-9f64-42b1086ca5d2.svg'
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
    icon_id = 'red-indian-man-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('red', 'indian', 'man', 'portrait', 'bust')

    def build(self) -> None:
        # Man with curly hair, headband and a feather (reference): r8 head whose
        # upper half is three curly bumps, the headband along the diameter, a
        # lens feather rising up-right from the notch between the bumps, shoulders
        # touching the chin. (The reference's second feather reads as a sprout at 48.)
        _path(self, 'hair', (16, 21), [((18, 14), 4, 4, True), ((30, 14), 7, 7, True), ((32, 21), 4, 4, True)])
        _path(self, 'face', (32, 21), [((24, 29), 8, 8, True), ((16, 21), 8, 8, True)])
        self.add_line('band', (16, 21), (32, 21))
        self.relate('connect', 'hair', 'face')
        self.relate('connect', 'hair', 'band')
        self.relate('connect', 'face', 'band')
        self.add_bezier('feather-a', (30, 14), ((30, 8), (34, 4), (40, 4)))
        self.add_bezier('feather-b', (40, 4), ((40, 10), (36, 14), (30, 14)))
        self.add_contour('feather', 'feather-a', 'feather-b', closed=True)
        self.relate('connect', 'feather', 'hair')
        _path(self, 'shoulders', (8, 44), [((24, 33), 16, 11, True), ((40, 44), 16, 11, True)])
        self.relate('connect', 'face', 'shoulders')
