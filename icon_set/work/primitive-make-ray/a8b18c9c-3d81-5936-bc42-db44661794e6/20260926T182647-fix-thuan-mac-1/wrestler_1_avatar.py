from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a8b18c9c-3d81-5936-bc42-db44661794e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wrestler-1-avatar/20260926T182452Z-thuan-mac-1/reference/wrestler_a8b18c9c-3d81-5936-bc42-db44661794e6.svg'
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
    icon_id = 'wrestler-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('wrestler', 'luchador', 'mask', 'singlet', 'sport', 'portrait')

    def build(self) -> None:
        # Wrestler (reference): masked r10 head on flat user.svg shoulders with
        # the arms folded across the chest as an X. The mask is the head's lower
        # rim with the mask's angry V brow meeting the rim at 6-8-10 points.
        _path(self, 'head', (16, 8), [((24, 4), 10, 10, True), ((32, 8), 10, 10, True),
                                      ((24, 24), 10, 10, True), ((16, 8), 10, 10, True)], True)
        self.add_line('mask-brow-left', (16, 8), (24, 14))
        self.add_line('mask-brow-right', (24, 14), (32, 8))
        for m in ('mask-brow-left', 'mask-brow-right'):
            self.relate('connect', 'head', m)
        self.relate('connect', 'mask-brow-left', 'mask-brow-right')
        _path(self, 'body-left', (8, 44), [(8, 36), ((16, 28), 8, 8, True)])
        self.add_line('body-top', (16, 28), (24, 28))
        self.add_line('body-top-right', (24, 28), (32, 28))
        _path(self, 'body-right', (32, 28), [((40, 36), 8, 8, True), (40, 44)])
        for a, b in [('body-left', 'body-top'), ('body-top', 'body-top-right'), ('body-top-right', 'body-right'),
                     ('head', 'body-top'), ('head', 'body-top-right')]:
            self.relate('connect', a, b)
        # Folded forearms: two strokes crossing at (24,40), split at the crossing.
        self.add_line('arm-a1', (18, 36), (24, 40)); self.add_line('arm-a2', (24, 40), (30, 44))
        self.add_line('arm-b1', (30, 36), (24, 40)); self.add_line('arm-b2', (24, 40), (18, 44))
        for a, b in [('arm-a1', 'arm-a2'), ('arm-a1', 'arm-b1'), ('arm-a1', 'arm-b2'),
                     ('arm-a2', 'arm-b1'), ('arm-a2', 'arm-b2'), ('arm-b1', 'arm-b2')]:
            self.relate('connect', a, b)
