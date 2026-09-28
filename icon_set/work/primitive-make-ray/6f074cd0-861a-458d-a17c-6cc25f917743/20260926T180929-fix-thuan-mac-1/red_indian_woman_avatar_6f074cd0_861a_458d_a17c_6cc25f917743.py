from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6f074cd0-861a-458d-a17c-6cc25f917743'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__red-indian-woman-avatar/20260926T180600Z-thuan-mac-1/reference/red indian woman_6f074cd0-861a-458d-a17c-6cc25f917743.svg'
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
    icon_id = 'red-indian-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('red', 'indian', 'woman', 'portrait', 'bust')

    def build(self) -> None:
        # Woman with a feather in her headband (reference): r8 head, the headband
        # runs along its diameter (hair above, face below), a lens feather rises
        # up-left from the crown, bob ends flick out from the band, shoulders touch the chin.
        _path(self, 'hair', (16, 20), [((24, 12), 8, 8, True), ((32, 20), 8, 8, True)])
        _path(self, 'face', (32, 20), [((24, 28), 8, 8, True), ((16, 20), 8, 8, True)])
        self.add_line('band', (16, 20), (32, 20))
        self.relate('connect', 'hair', 'face')
        self.relate('connect', 'hair', 'band')
        self.relate('connect', 'face', 'band')
        self.add_bezier('feather-a', (24, 12), ((26, 5), (20, 4), (14, 4)))
        self.add_bezier('feather-b', (14, 4), ((12, 10), (18, 12), (24, 12)))
        self.add_contour('feather', 'feather-a', 'feather-b', closed=True)
        self.relate('connect', 'feather', 'hair')
        self.add_bezier('bob-left', (16, 20), ((15, 24), (13, 26), (8, 26)))
        self.add_bezier('bob-right', (32, 20), ((33, 24), (35, 26), (40, 26)))
        for b in ('bob-left', 'bob-right'):
            for part in ('hair', 'face', 'band'):
                self.relate('connect', b, part)
        _path(self, 'shoulders', (8, 44), [((24, 32), 16, 12, True), ((40, 44), 16, 12, True)])
        self.relate('connect', 'face', 'shoulders')
