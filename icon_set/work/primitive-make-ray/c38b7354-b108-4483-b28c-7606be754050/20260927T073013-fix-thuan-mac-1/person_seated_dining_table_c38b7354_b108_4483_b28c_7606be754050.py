from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c38b7354-b108-4483-b28c-7606be754050'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-seated-dining-table/20260927T072841Z-thuan-mac-1/reference/restaurant seat_c38b7354-b108-4483-b28c-7606be754050.svg'
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
    icon_id = 'person-seated-dining-table'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('person', 'seated', 'dining', 'table')

    def build(self) -> None:
        # diner (human ref full_body_ref.png): r4 head 8 above the upright torso, forearm on the table,
        # thigh on the seat, shin down; pedestal table with a glass on it
        _circle(self, "head", 10, 10, 4)
        self.add_line("torso", (10, 22), (10, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (10, 24), (22, 24))
        self.add_polyline("leg", (10, 32), (20, 32), (20, 42))
        xs = (22, 26, 34, 38, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"table-{n}", (a, 24), (b, 24))
        for n in range(3):
            self.relate("connect", f"table-{n}", f"table-{n + 1}")
        self.add_line("pedestal", (38, 24), (38, 42))
        self.add_line("foot", (32, 42), (42, 42))
        self.add_polyline("glass", (26, 24), (25, 14), (35, 14), (34, 24))
        for a, b in (("torso", "arm"), ("torso", "leg"), ("arm", "table-0"), ("pedestal", "table-2"), ("pedestal", "table-3"),
                     ("pedestal", "foot"), ("glass", "table-0"), ("glass", "table-1"), ("glass", "table-2")):
            self.relate("connect", a, b)
