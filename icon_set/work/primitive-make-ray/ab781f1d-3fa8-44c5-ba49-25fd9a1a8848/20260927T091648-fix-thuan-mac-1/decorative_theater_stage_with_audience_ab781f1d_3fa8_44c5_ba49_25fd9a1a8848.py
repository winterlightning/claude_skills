from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ab781f1d-3fa8-44c5-ba49-25fd9a1a8848'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__decorative-theater-stage-with-audience/20260927T091421Z-thuan-mac-1/reference/ramlila 1_ab781f1d-3fa8-44c5-ba49-25fd9a1a8848.svg'
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
    icon_id = 'decorative-theater-stage-with-audience'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('decorative', 'theater', 'stage', 'with', 'audience')

    def build(self) -> None:
        # Theater stage with audience, mirrored about x = 24. The stage is a framed box (x 6..42,
        # y 6..28); two curtains hang from the top bar and sweep out to the sides, leaving the opening
        # between them. The audience is a row of three head-backs (r6 semicircles) along the bottom,
        # 8 below the stage floor.
        _path(self, "stage", (6, 28), [(6, 6), (20, 6), (28, 6), (42, 6), (42, 28), (34, 28), (14, 28), (6, 28)], True)
        _path(self, "curtain-left", (20, 6), [('c', (20, 12), (14, 13), (14, 19)), (14, 28)])
        _path(self, "curtain-right", (28, 6), [('c', (28, 12), (34, 13), (34, 19)), (34, 28)])
        self.relate("connect", "stage", "curtain-left")
        self.relate("connect", "stage", "curtain-right")
        _path(self, "audience", (6, 42), [((12, 36), 6, 6, True), ((18, 42), 6, 6, True), ((24, 36), 6, 6, True),
                                          ((30, 42), 6, 6, True), ((36, 36), 6, 6, True), ((42, 42), 6, 6, True)])
