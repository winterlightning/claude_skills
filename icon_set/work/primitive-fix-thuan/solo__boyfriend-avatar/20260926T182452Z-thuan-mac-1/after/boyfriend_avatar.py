from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6402d24c-4cdc-4ef1-8c10-4f0360f4ff23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boyfriend-avatar/20260926T182452Z-thuan-mac-1/reference/boyfriend_6402d24c-4cdc-4ef1-8c10-4f0360f4ff23.svg'
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
    icon_id = 'boyfriend-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('boyfriend', 'portrait', 'bust')

    def build(self) -> None:
        # Boyfriend (reference): young man's bust - r10 head with a side-swept
        # fringe and ear bumps built into the head outline, jaw touching flat
        # user.svg shoulders.
        _path(self, 'head', (24, 24), [((16, 20), 10, 10, True), ((14, 14), 4, 4, True),
                                       ((24, 4), 10, 10, True), ((34, 14), 10, 10, True),
                                       ((32, 20), 4, 4, True), ((24, 24), 10, 10, True)], True)
        self.add_bezier('fringe', (14, 14), ((20, 14), (27, 11), (30, 6)))
        self.relate('connect', 'head', 'fringe')
        _path(self, 'body-left', (8, 44), [(8, 36), ((16, 28), 8, 8, True)])
        self.add_line('body-top', (16, 28), (24, 28))
        self.add_line('body-top-right', (24, 28), (32, 28))
        _path(self, 'body-right', (32, 28), [((40, 36), 8, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top'), ('body-top', 'body-top-right'), ('body-top-right', 'body-right'),
                     ('head', 'body-top'), ('head', 'body-top-right')]:
            self.relate('connect', a, b)
