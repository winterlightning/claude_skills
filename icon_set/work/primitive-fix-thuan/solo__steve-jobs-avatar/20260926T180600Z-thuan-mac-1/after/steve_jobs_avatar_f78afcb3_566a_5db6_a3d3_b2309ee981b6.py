from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f78afcb3-566a-5db6-a3d3-b2309ee981b6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__steve-jobs-avatar/20260926T180600Z-thuan-mac-1/reference/steve jobs_f78afcb3-566a-5db6-a3d3-b2309ee981b6.svg'
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
    icon_id = 'steve-jobs-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('steve', 'jobs', 'portrait', 'bust')

    def build(self) -> None:
        # Steve Jobs (reference): bald head (r12 crown, straight temples, r12 jaw),
        # round r5 glasses whose rims meet the temples and a short bridge,
        # shoulders touching the chin.
        _path(self, 'head', (24, 32), [((12, 20), 12, 12, True), (12, 18), (12, 16), ((24, 4), 12, 12, True),
                                       ((36, 16), 12, 12, True), (36, 18), (36, 20), ((24, 32), 12, 12, True)], True)
        _circle(self, 'lens-left', 17, 18, 5)
        _circle(self, 'lens-right', 31, 18, 5)
        self.add_line('bridge', (22, 18), (26, 18))
        for lens in ('lens-left', 'lens-right'):
            self.relate('connect', lens, 'head')
            self.relate('connect', lens, 'bridge')
        _path(self, 'shoulders', (8, 44), [((24, 36), 16, 8, True), ((40, 44), 16, 8, True)])
        self.relate('connect', 'head', 'shoulders')
