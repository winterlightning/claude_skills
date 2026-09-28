from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e1e6b172-0589-49ee-9311-e9b8ae8c07ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-running-through-doorway/20260927T072841Z-thuan-mac-1/reference/safety exit door_e1e6b172-0589-49ee-9311-e9b8ae8c07ff.svg'
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
    icon_id = 'person-running-through-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('exit', 'doorway', 'running', 'person', 'escape', 'safety')

    def build(self) -> None:
        # doorway: lintel and two jambs
        self.add_polyline("doorway", (6, 42), (6, 6), (42, 6), (42, 42))
        # runner inside it (human ref full_body_ref.png): r3 head 8 above a vertical neck segment, torso
        # leaning back to the hip, arms swinging, legs striding
        _circle(self, "head", 24, 18, 3)
        self.add_line("torso", (24, 29), (24, 31))
        self.add_line("torso-lean", (24, 31), (20, 36))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm-front", (24, 31), (33, 28))
        self.add_line("arm-back", (24, 31), (15, 28))
        self.add_polyline("leg-front", (20, 36), (28, 39), (29, 42))
        self.add_line("leg-back", (20, 36), (14, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm-front"), ("torso", "arm-back"), ("torso-lean", "arm-front"),
                     ("torso-lean", "arm-back"), ("arm-front", "arm-back"), ("torso-lean", "leg-front"),
                     ("torso-lean", "leg-back"), ("leg-front", "leg-back")):
            self.relate("connect", a, b)
