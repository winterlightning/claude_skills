from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0792de2c-10a7-4244-a020-3cd7e338617d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__drink-can-with-bent-straw/20260926T162509Z-thuan-mac/reference/softdrink_0792de2c-10a7-4244-a020-3cd7e338617d.svg'
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
    icon_id = 'drink-can-with-bent-straw'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('can', 'drink', 'straw', 'soda', 'beverage', 'container')

    def build(self) -> None:
        # Plan: soda can on VRECT_M (x 10..38, y 4..44) as in the reference: a
        # tall body with rounded base, a tapered lid (shoulders 1:4) closed by a
        # rim line 8 below the lid top, and a straw rising from the lid at x=28,
        # bent once toward the upper right corner.
        _path(self, 'can', (12, 14), [
            (28, 14), (32, 14), (34, 22), (34, 40), ((30, 44), 4, 4, True),
            (14, 44), ((10, 40), 4, 4, True), (10, 22), (12, 14),
        ], closed=True)
        self.add_line('rim', (10, 22), (34, 22))
        self.relate('connect', 'can', 'rim')
        _path(self, 'straw', (28, 14), [(30, 8), (38, 4)])
        self.relate('connect', 'can', 'straw')
