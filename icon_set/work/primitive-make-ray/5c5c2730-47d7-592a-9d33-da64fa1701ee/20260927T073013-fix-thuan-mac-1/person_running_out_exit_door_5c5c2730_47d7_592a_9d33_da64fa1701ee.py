from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5c5c2730-47d7-592a-9d33-da64fa1701ee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-running-out-exit-door/20260927T072841Z-thuan-mac-1/reference/evacuation center_5c5c2730-47d7-592a-9d33-da64fa1701ee.svg'
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
    icon_id = 'person-running-out-exit-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('exit', 'evacuation', 'emergency', 'running', 'person', 'door', 'escape', 'safety')

    def build(self) -> None:
        # runner heading out (human ref full_body_ref.png): head 8 above a vertical neck segment, torso
        # leaning back to the hip, bent arms, striding legs
        _circle(self, "head", 20, 10, 4)
        self.add_line("torso", (20, 22), (20, 24))
        self.add_line("torso-lean", (20, 24), (14, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm-front", (20, 24), (26, 29), (30, 25))
        self.add_polyline("arm-back", (20, 24), (12, 21), (8, 25))
        self.add_polyline("leg-front", (14, 32), (22, 35), (20, 42))
        self.add_polyline("leg-back", (14, 32), (8, 36), (6, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-front"), ("torso", "arm-back"), ("torso-lean", "arm-front"),
                     ("torso-lean", "arm-back"), ("arm-front", "arm-back"), ("torso-lean", "leg-front"),
                     ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
        # exit door frame on the right: lintel, jamb and threshold stub
        self.add_polyline("door", (32, 6), (42, 6), (42, 42), (34, 42))
