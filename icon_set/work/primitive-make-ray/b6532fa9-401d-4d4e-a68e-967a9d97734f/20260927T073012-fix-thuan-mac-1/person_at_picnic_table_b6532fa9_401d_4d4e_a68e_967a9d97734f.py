from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b6532fa9-401d-4d4e-a68e-967a9d97734f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-at-picnic-table/20260927T072841Z-thuan-mac-1/reference/outdoors bench sit_b6532fa9-401d-4d4e-a68e-967a9d97734f.svg'
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
    icon_id = 'person-at-picnic-table'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('picnic', 'bench', 'table', 'sitting', 'person', 'park', 'rest', 'outdoors', 'outdoors-batch-02')

    def build(self) -> None:
        # seated person leaning toward a picnic table (human ref full_body_ref.png): r4 head exactly 8
        # above a short vertical neck segment, torso slanting back to the hip, arm reaching the table top,
        # thigh forward and shin down
        _circle(self, "head", 14, 10, 4)
        self.add_line("torso", (14, 22), (14, 24))
        self.add_line("torso-lean", (14, 24), (6, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (14, 24), (24, 22))
        self.add_polyline("leg", (6, 32), (18, 32), (18, 42))
        xs = (24, 30, 40, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"table-top-{n}", (a, 22), (b, 22))
        self.add_line("table-leg-left", (30, 22), (28, 42))
        self.add_line("table-leg-right", (40, 22), (42, 42))
        for a, b in (("torso", "torso-lean"), ("torso", "arm"), ("torso-lean", "arm"), ("torso-lean", "leg"),
                     ("arm", "table-top-0"), ("table-top-0", "table-top-1"), ("table-top-1", "table-top-2"),
                     ("table-leg-left", "table-top-0"), ("table-leg-left", "table-top-1"),
                     ("table-leg-right", "table-top-1"), ("table-leg-right", "table-top-2")):
            self.relate("connect", a, b)
