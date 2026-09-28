from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3fa61ac-129f-4215-bc78-72af508b4c04'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-person/20260927T083044Z-thuan-mac-1/reference/walking fast_d3fa61ac-129f-4215-bc78-72af508b4c04.svg'
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
    icon_id = 'walking-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'walking', 'stride', 'pedestrian', 'movement', 'figure')

    def build(self) -> None:
        # Plan (human ref full_body_ref.png): person walking briskly to the right - r5 head 8 above
        # a short vertical neck stub, torso leaning slightly forward to the hip, front arm bent
        # forward, back arm swung behind, walking stride with the front knee bent.
        _circle(self, "head", 25, 9, 5)
        self.add_line("torso", (25, 22), (25, 24))
        self.add_line("torso-lean", (25, 24), (21, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm-front", (25, 24), (33, 29), (40, 26))
        self.add_polyline("arm-back", (25, 24), (16, 28), (8, 32))
        self.add_polyline("leg-front", (21, 32), (28, 38), (30, 44))
        self.add_polyline("leg-back", (21, 32), (17, 39), (12, 44))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-front"), ("torso", "arm-back"),
                     ("torso-lean", "arm-front"), ("torso-lean", "arm-back"), ("arm-front", "arm-back"),
                     ("torso-lean", "leg-front"), ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
