from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '83429111-05e6-413f-a4b9-97c0747e3712'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-slipping/20260927T072841Z-thuan-mac-1/reference/safety slippery_83429111-05e6-413f-a4b9-97c0747e3712.svg'
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
    icon_id = 'person-slipping'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('slipping', 'falling', 'person', 'floor', 'hazard', 'safety')

    def build(self) -> None:
        # person slipping backwards (human ref full_body_ref.png): r4 head 8 above a vertical neck segment,
        # torso tipping back to the hip, both arms flung up, legs kicked out, the floor below
        _circle(self, "head", 28, 10, 4)
        self.add_line("torso", (28, 22), (28, 24))
        self.add_line("torso-lean", (28, 24), (22, 30))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm-left", (28, 24), (18, 20), (14, 10))
        self.add_polyline("arm-right", (28, 24), (38, 22), (42, 14))
        self.add_polyline("leg-front", (22, 30), (12, 30), (6, 26))
        self.add_line("leg-back", (22, 30), (12, 36))
        self.add_line("floor", (18, 42), (38, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-left"), ("torso", "arm-right"), ("torso-lean", "arm-left"),
                     ("torso-lean", "arm-right"), ("arm-left", "arm-right"), ("torso-lean", "leg-front"),
                     ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
