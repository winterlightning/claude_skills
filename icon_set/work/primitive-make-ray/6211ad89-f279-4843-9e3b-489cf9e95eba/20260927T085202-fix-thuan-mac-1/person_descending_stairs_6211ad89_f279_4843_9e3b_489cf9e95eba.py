from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6211ad89-f279-4843-9e3b-489cf9e95eba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-descending-stairs/20260927T084830Z-thuan-mac-1/reference/stairs person decend_6211ad89-f279-4843-9e3b-489cf9e95eba.svg'
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
    icon_id = 'person-descending-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'stairs', 'descending', 'steps', 'walking', 'wayfinding')

    def build(self) -> None:
        # person stepping down a staircase (reference): upright figure, arm out for balance, back
        # foot on a step and front leg reaching down past the riser; steps rise to the right.
        # Before laid the figure almost flat so it read as a runner.
        _circle(self, "head", 16, 10, 4)
        self.add_line("torso", (16, 22), (16, 24))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("torso-low", (16, 24), (16, 30))
        self.add_line("arm", (16, 24), (6, 27))
        self.add_line("leg-front", (16, 30), (12, 42)); self.add_polyline("leg-back", (16, 30), (24, 32), (29, 38))
        for a, b in (("torso", "torso-low"), ("torso", "arm"), ("torso-low", "arm"), ("torso-low", "leg-front"),
                     ("torso-low", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
        _path(self, "stairs", (22, 42), [(22, 38), (29, 38), (32, 38), (32, 30), (42, 30)])
        self.relate("connect", "stairs", "leg-back")
