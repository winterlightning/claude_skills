from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-running-right/20260927T072841Z-thuan-mac-1/reference/safety exit right_faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb.svg'
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
    icon_id = 'person-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'running', 'right', 'escape', 'motion', 'wayfinding')

    def build(self) -> None:
        # runner heading right (human ref full_body_ref.png): r4 head exactly 8 above a short vertical neck
        # segment, torso leaning back to the hip, bent arms swinging, legs in a long stride
        _circle(self, "head", 32, 10, 4)
        self.add_line("torso", (32, 22), (32, 24))
        self.add_line("torso-lean", (32, 24), (24, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm-front", (32, 24), (38, 30), (42, 26))
        self.add_polyline("arm-back", (32, 24), (24, 20), (18, 24))
        self.add_polyline("leg-front", (24, 32), (32, 36), (30, 42))
        self.add_polyline("leg-back", (24, 32), (16, 36), (6, 36))
        for p in ("arm-front", "arm-back", "torso-lean"):
            self.relate("connect", "torso", p)
        for a, b in (("torso-lean", "arm-front"), ("torso-lean", "arm-back"), ("arm-front", "arm-back"),
                     ("torso-lean", "leg-front"), ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
