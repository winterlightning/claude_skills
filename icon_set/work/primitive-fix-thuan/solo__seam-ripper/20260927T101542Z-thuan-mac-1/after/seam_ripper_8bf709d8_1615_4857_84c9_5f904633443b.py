from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8bf709d8-1615-4857-84c9-5f904633443b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seam-ripper/20260927T101542Z-thuan-mac-1/reference/sew tool_8bf709d8-1615-4857-84c9-5f904633443b.svg'
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
    icon_id = 'seam-ripper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hobbies'
    categories = ('primitives', 'hobbies')
    aliases = ()
    keywords = ('seam', 'ripper')

    def build(self) -> None:
        # 45-degree handle: r5 cap about (37,11) (3-4-5 ends, touches top 6 and right 42),
        # sides x+y=41 / x+y=55, flat foot (20,21)-(27,28); thin shaft on x+y=47 to (6,41);
        # a wavy thread below, 9+ from the shaft.
        _path(self, "handle", (20, 21), [(34, 7), ((41, 14), 5, 5, True), (27, 28), (23, 24), (20, 21)], True)
        self.add_line("shaft", (23, 24), (6, 41))
        self.relate("connect", "handle", "shaft")
        _path(self, "thread", (18, 42), [('c', (21, 42), (23, 37), (26, 37)),
                                         ('c', (29, 37), (31, 42), (34, 42)),
                                         ('c', (37, 42), (39, 37), (42, 37))])
