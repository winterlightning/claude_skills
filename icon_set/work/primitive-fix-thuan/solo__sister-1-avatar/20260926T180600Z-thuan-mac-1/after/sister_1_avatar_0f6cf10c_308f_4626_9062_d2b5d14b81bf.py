from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0f6cf10c-308f-4626-9062-d2b5d14b81bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sister-1-avatar/20260926T180600Z-thuan-mac-1/reference/sister_0f6cf10c-308f-4626-9062-d2b5d14b81bf.svg'
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
    icon_id = 'sister-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('sister', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Nun (reference): tall veil arch framing the face and running down to the
        # bottom edge, r7 round face crossed by the wimple band, shoulders
        # spanning the veil and touching the chin.
        _path(self, 'veil', (8, 44), [(8, 40), (8, 18), ((24, 4), 16, 14, True), ((40, 18), 16, 14, True), (40, 40), (40, 44)])
        _circle(self, 'face', 24, 20, 7)
        self.add_line('band', (17, 20), (31, 20))
        self.relate('connect', 'face', 'band')
        _path(self, 'shoulders', (8, 40), [((24, 31), 16, 9, True), ((40, 40), 16, 9, True)])
        self.relate('connect', 'shoulders', 'veil')
        self.relate('connect', 'face', 'shoulders')
