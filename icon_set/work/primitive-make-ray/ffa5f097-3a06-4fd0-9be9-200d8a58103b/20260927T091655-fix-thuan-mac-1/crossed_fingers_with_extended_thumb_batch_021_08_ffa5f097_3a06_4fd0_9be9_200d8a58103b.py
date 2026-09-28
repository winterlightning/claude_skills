from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ffa5f097-3a06-4fd0-9be9-200d8a58103b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-fingers-with-extended-thumb-batch-021-08/20260927T091424Z-thuan-mac-1/reference/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
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
    icon_id = 'crossed-fingers-with-extended-thumb-batch-021-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'extended', 'thumb')

    def build(self) -> None:
        # Plan: crossed index (front, lines 2x+y=59/79) and middle (back, lines
        # 2x-y=17/37) fingers on 1:2 bands (width 8.9, r5 tips about (29,11) and
        # (19,11)); the back finger hides behind the front one (joins (24,11),
        # (19,21)) and ends behind the curled fingers, whose knuckle line leaves
        # the front finger at (29,21) and rounds into the palm side (r7 about
        # (35,28)). The front finger's right edge runs on into the palm as a crease.
        # Extended thumb on a 2:1 band (width 8.9) from the web (17,25), r5 tip
        # about (11,27) reaching x=6; palm = cubic + quarter ellipse to y=42.
        _path(self, 'hand', (26, 7), [
            ((34, 11), 5, 5, True), (29, 21), (35, 21), ((42, 28), 7, 7, True), (42, 33),
            ((27, 42), 15, 9, True), ('c', (20, 42), (14, 38), (13, 33)), (7, 30),
            ((11, 22), 5, 5, True), (17, 25), (19, 21), (24, 11), (26, 7),
        ], True)
        _path(self, 'back-tip', (19, 21), [(14, 11), ((22, 7), 5, 5, True), (24, 11)])
        self.add_line('crease', (29, 21), (25, 29))
        self.relate('connect', 'back-tip', 'hand')
        self.relate('connect', 'crease', 'hand')
