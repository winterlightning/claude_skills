from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '26fbb103-f21c-436b-8013-3eb3bcd065b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-connected-panel/20260927T072841Z-thuan-mac-1/reference/immersive reality_26fbb103-f21c-436b-8013-3eb3bcd065b1.svg'
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
    icon_id = 'person-reaching-connected-panel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('immersive', 'person', 'panel', 'interaction', 'spatial', 'connection', 'virtual-reality')

    def build(self) -> None:
        # connected panel: a screen in perspective with a connector to a node and a stem to a second node
        self.add_polyline("panel", (6, 6), (20, 8), (20, 20), (14, 21), (6, 22), closed=True)
        self.add_polyline("connector", (20, 13), (28, 13), (28, 9), (31, 9))
        _circle(self, "node-top", 34, 9, 3)
        self.add_line("stem", (14, 21), (14, 30))
        _circle(self, "node-low", 14, 33, 3)
        for a, b in (("panel", "connector"), ("connector", "node-top"), ("panel", "stem"), ("stem", "node-low")):
            self.relate("connect", a, b)
        # person reaching toward it (human ref user.svg): r4 head 8+ above the shoulder, the shoulder
        # curve flowing up into the raised arm
        _circle(self, "head", 36, 24, 4)
        _path(self, "body", (25, 30), [(31, 36), ('c', (34, 36), (40, 36), (42, 42))])
        self.mark_human_figure("person", head="head", torso="body-2", torso_junction="start")
