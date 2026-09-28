from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ece8ab4e-b49d-4584-a897-5c82841a003c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__photographer-man-avatar/20260926T180600Z-thuan-mac-1/reference/photographer man_ece8ab4e-b49d-4584-a897-5c82841a003c.svg'
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
    icon_id = 'photographer-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('photographer', 'man', 'portrait', 'bust')

    def build(self) -> None:
        # Photographer: r10 head with side-swept fringe, camera hung on a strap.
        TOP = 28
        _path(self, 'head', (24, 24), [((14, 14), 10, 10, True), ((24, 4), 10, 10, True),
                                       ((30, 6), 10, 10, True), ((34, 14), 10, 10, True),
                                       ((24, 24), 10, 10, True)], True)
        self.add_bezier('fringe', (14, 14), ((20, 14), (27, 11), (30, 6)))
        self.relate('connect', 'head', 'fringe')
        self.relate('connect', 'head', 'body-top')
        self.relate('connect', 'head', 'body-top-right')
        # Flat-topped shoulders (human_ref user.svg) with a strap V down to a camera.
        _path(self, 'body-left', (8, 44), [(8, TOP + 8), ((16, TOP), 8, 8, True)])
        self.add_line('body-top', (16, TOP), (24, TOP))
        self.add_line('body-top-right', (24, TOP), (32, TOP))
        _path(self, 'body-right', (32, TOP), [((40, TOP + 8), 8, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top'), ('body-top', 'body-top-right'), ('body-top-right', 'body-right')]:
            self.relate('connect', a, b)
        self.add_line('strap-left', (16, TOP), (18, 36))
        self.add_line('strap-right', (32, TOP), (30, 36))
        _path(self, 'camera', (18, 36), [(24, 36), (30, 36), (30, 44), (18, 44), (18, 36)], True)
        for s in ('strap-left', 'strap-right'):
            self.relate('connect', s, 'camera')
        for s in ('body-left', 'body-top'):
            self.relate('connect', 'strap-left', s)
        for s in ('body-right', 'body-top-right'):
            self.relate('connect', 'strap-right', s)
