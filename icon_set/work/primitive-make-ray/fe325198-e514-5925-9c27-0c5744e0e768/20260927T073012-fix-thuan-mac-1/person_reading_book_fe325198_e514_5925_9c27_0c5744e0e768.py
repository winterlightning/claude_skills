from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fe325198-e514-5925-9c27-0c5744e0e768'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reading-book/20260927T072841Z-thuan-mac-1/reference/read human_fe325198-e514-5925-9c27-0c5744e0e768.svg'
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
    icon_id = 'person-reading-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'school-learning'
    categories = ('school-learning', 'primitives')
    aliases = ()
    keywords = ('person', 'reading', 'book', 'study', 'reader', 'learning')

    def build(self) -> None:
        # person reading (human ref user.svg): r4 head, shoulder arch 8 below it rising behind an open book
        _circle(self, "head", 24, 10, 4)
        self.add_arc("shoulders", (15, 30), (33, 30), radius_x=9, radius_y=8)
        self.mark_human_figure("person", head="head", torso="shoulders", torso_junction="start")
        # open book: top edges dip to the spine, pages 10 tall
        self.add_polyline("top-left", (6, 28), (15, 30), (24, 32))
        self.add_polyline("top-right", (24, 32), (33, 30), (42, 28))
        self.add_polyline("book", (6, 28), (6, 38), (24, 42), (42, 38), (42, 28))
        self.add_line("spine", (24, 32), (24, 42))
        for a, b in (("top-left", "top-right"), ("book", "top-left"), ("book", "top-right"), ("spine", "top-left"),
                     ("spine", "top-right"), ("spine", "book"), ("shoulders", "top-left"), ("shoulders", "top-right")):
            self.relate("connect", a, b)
