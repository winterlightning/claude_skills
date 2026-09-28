from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f2bc5957-ed09-45db-a629-7cd80741e351'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-seated-in-prayer/20260927T072841Z-thuan-mac-1/reference/islamic before bowing_f2bc5957-ed09-45db-a629-7cd80741e351.svg'
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
    icon_id = 'person-seated-in-prayer'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'religion'
    categories = ('primitives', 'religion')
    aliases = ()
    keywords = ('person', 'prayer', 'kneeling', 'seated', 'worship', 'posture')

    def build(self) -> None:
        # kneeling in prayer, sitting back on the heels (human ref full_body_ref.png): r4 head 8 above the
        # upright torso, thigh down to the knee, shin along the floor, hands raised together before the face
        _circle(self, "head", 24, 8, 4)
        self.add_line("torso", (24, 20), (24, 34))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("leg", (24, 34), (10, 44), (38, 44))
        self.add_polyline("arms", (24, 22), (16, 29), (11, 23))
        self.relate("connect", "torso", "leg"); self.relate("connect", "torso", "arms")
