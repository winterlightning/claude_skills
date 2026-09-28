from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '89e4f18d-ea56-4da8-8bbf-763032c8091a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-pages/20260927T084830Z-thuan-mac-1/reference/book pages_89e4f18d-ea56-4da8-8bbf-763032c8091a.svg'
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
    icon_id = 'book-pages'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('book', 'pages', 'state', 'solo-ai-next50')

    def build(self) -> None:
        # open book, reference: tall pages whose top edges sag into the spine and whose bottom
        # edges slope down to a V at the spine (before drew flat Lucide pages without the V)
        _path(self, "cover", (24, 11), [
            ('c', (20, 7), (14, 6), (9, 6)), ((6, 9), 3, 3, False), (6, 34),
            ('c', (6, 36), (7, 37), (9, 37)), ('c', (15, 37), (20, 38), (24, 42)),
            ('c', (28, 38), (33, 37), (39, 37)), ('c', (41, 37), (42, 36), (42, 34)),
            (42, 9), ((39, 6), 3, 3, False), ('c', (34, 6), (28, 7), (24, 11))], True)
        self.add_line("spine", (24, 11), (24, 42))
        self.relate("connect", "cover", "spine")
