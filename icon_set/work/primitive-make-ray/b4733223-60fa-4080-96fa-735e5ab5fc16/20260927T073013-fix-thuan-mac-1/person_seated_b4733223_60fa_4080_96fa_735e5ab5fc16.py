from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b4733223-60fa-4080-96fa-735e5ab5fc16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-seated/20260927T072841Z-thuan-mac-1/reference/sit_b4733223-60fa-4080-96fa-735e5ab5fc16.svg'
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
    icon_id = 'person-seated'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('sitting', 'person', 'seat', 'waiting', 'rest', 'chair', 'passenger', 'lounge')

    def build(self) -> None:
        # seated person in profile facing left (human ref full_body_ref.png): r4 head exactly 8 above the
        # upright back, thigh forward to the knee, shin angling down to the floor
        _circle(self, "head", 34, 8, 4)
        self.add_line("torso", (34, 20), (34, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("leg", (34, 32), (18, 32), (10, 44))
        self.relate("connect", "torso", "leg")
