from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c41ef721-60c2-4320-a7d5-7a5f29e74c2b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-pushing-wheelchair-user/20260927T072841Z-thuan-mac-1/reference/wheelchair helper_c41ef721-60c2-4320-a7d5-7a5f29e74c2b.svg'
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
    icon_id = 'person-pushing-wheelchair-user'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('wheelchair', 'helper', 'person', 'assistance', 'mobility', 'accessibility')

    def build(self) -> None:
        # (human ref full_body_ref.png) both heads r4, exactly 8 above a vertical neck segment
        # helper: leaning into the push, arm straight to the chair back, striding legs
        _circle(self, "helper-head", 12, 12, 4)
        self.add_line("helper-torso", (12, 24), (12, 26))
        self.add_line("helper-lean", (12, 26), (8, 32))
        self.mark_human_figure("helper", head="helper-head", torso="helper-torso", torso_junction="start")
        self.add_line("helper-arm", (12, 26), (32, 26))
        self.add_polyline("helper-legs", (4, 40), (8, 32), (14, 40))
        # rider: upright on the seat, legs forward and down; the wheel arcs from the chair back to under the seat
        _circle(self, "rider-head", 32, 12, 4)
        self.add_line("rider-torso", (32, 24), (32, 26))
        self.add_polyline("rider-body", (32, 26), (32, 32), (40, 32), (44, 40))
        self.mark_human_figure("rider", head="rider-head", torso="rider-torso", torso_junction="start")
        self.add_arc("wheel", (32, 26), (32, 40), radius_x=8, radius_y=7, sweep=False)
        for a, b in (("helper-torso", "helper-lean"), ("helper-torso", "helper-arm"), ("helper-lean", "helper-arm"),
                     ("helper-lean", "helper-legs"), ("rider-torso", "rider-body"), ("wheel", "rider-body"),
                     ("wheel", "rider-torso"), ("helper-arm", "rider-torso"), ("helper-arm", "rider-body"),
                     ("helper-arm", "wheel")):
            self.relate("connect", a, b)
