from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3d9c4d13-b05d-5385-b082-74a41d0139d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-post-avatar/20260926T175624Z-thuan-mac-1/reference/man post_3d9c4d13-b05d-5385-b082-74a41d0139d5.svg'
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
    icon_id = 'man-post-avatar'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'post', 'portrait', 'bust')

    def build(self) -> None:
        # Mail carrier: a flared post cap (trapezoid wider at the top) over a
        # circular r6 jaw, touching a bust whose lower torso is a letter
        # envelope (full-width top edge, flap V meeting the hem at the centre).
        # A separate envelope on the chest cannot keep 8 from the shoulders
        # and still hold a flap, so the torso front is the envelope.
        # Reference: human_ref/user.svg shoulders; supplied post drawing.
        _path(self, 'head', (18, 12), [(14, 4), (34, 4), (30, 12), (30, 16), ((18, 16), 6, 6, True), (18, 12)], True)
        self.add_line('brim', (18, 12), (30, 12))
        self.relate('connect', 'head', 'brim')
        _path(self, 'body', (24, 26), [(30, 26), ((38, 34), 8, 8, True), (38, 44), (24, 44), (10, 44), (10, 34),
                                       ((18, 26), 8, 8, True), (24, 26)], True, ids={0: 'body-top-right', 7: 'body-top'})
        self.relate('connect', 'head', 'body')
        _path(self, 'envelope', (10, 34), [(38, 34)])
        _path(self, 'flap', (10, 34), [(24, 44), (38, 34)])
        self.relate('connect', 'envelope', 'body')
        self.relate('connect', 'flap', 'body')
        self.relate('connect', 'flap', 'envelope')
