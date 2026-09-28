from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3077a15f-909e-5ae1-9555-d52644d8badb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rocket-with-porthole/20260927T101542Z-thuan-mac-1/reference/rocket attack_3077a15f-909e-5ae1-9555-d52644d8badb.svg'
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
    icon_id = 'rocket-with-porthole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('rocket', 'porthole', 'space', 'fin', 'exhaust', 'flight')

    def build(self) -> None:
        # Axis x+y=48, mirrored with (x,y)->(48-y,48-x). Nose tip (42,6) hits top and right.
        _path(self, "body", (10, 22), [(14, 26), (22, 34), (26, 38), (36, 28),
                                       ('c', (40, 24), (42, 14), (42, 6)),
                                       ('c', (34, 6), (24, 8), (20, 12)), (10, 22)], True)
        _circle(self, "porthole", 28, 20, 3)
        _path(self, "fin-left", (20, 12), [(6, 12), (10, 22)])
        _path(self, "fin-right", (36, 28), [(36, 42), (26, 38)])
        _path(self, "flame", (14, 26), [('c', (8, 28), (6, 36), (6, 42)),
                                        ('c', (12, 42), (20, 40), (22, 34))])
        self.relate("connect", "body", "fin-left")
        self.relate("connect", "body", "fin-right")
        self.relate("connect", "body", "flame")
