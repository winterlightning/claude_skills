from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '288502c6-5133-5149-95a3-52e3acc6c690'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rock-horns-hand-with-crossing-thumb/20260927T101542Z-thuan-mac-1/reference/concert rock_288502c6-5133-5149-95a3-52e3acc6c690.svg'
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
    icon_id = 'rock-horns-hand-with-crossing-thumb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('rock', 'on', 'hand', 'gesture')

    def build(self) -> None:
        # Plan: sign-of-the-horns hand from the back. Index (x 8-16, tip at 4) and a
        # shorter pinky (x 32-40, tip at 8) stand up as 8-wide fingers with r4 tips;
        # middle and ring fold down as two r4 knuckle bumps between them; an 8-wide
        # thumb with a round tip crosses the palm below the knuckles; the palm closes
        # in a flat half-ellipse to the wrist.
        _path(self, "hand", (8, 8), [(8, 27), (8, 35), ((40, 35), 16, 9, False), (40, 12),
                                     ((32, 12), 4, 4, False), (32, 18), ((24, 18), 4, 4, False),
                                     ((16, 18), 4, 4, False), (16, 8), ((8, 8), 4, 4, False)], True)
        _path(self, "thumb", (8, 27), [(27, 27), ((27, 35), 4, 4, True), (8, 35)], False)
        self.relate("connect", "thumb", "hand")
