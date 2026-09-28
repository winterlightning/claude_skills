from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b327017b-1e45-5ef4-ba3a-ac5794b2643e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dump-truck-facing-right/20260927T061820Z-thuan-mac-1/reference/mortar truck_b327017b-1e45-5ef4-ba3a-ac5794b2643e.svg'
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
    icon_id = 'dump-truck-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('dump truck', 'tipper', 'truck', 'construction', 'vehicle', 'load', 'haulage', 'transport')

    def build(self) -> None:
        # side view facing right: tipper bed with its headboard lip reaching forward over the cab,
        # rear underside slanting up; cab with a raked windshield; chassis rail; two r5 wheels
        _path(self, "bed", (4, 14), [(24, 14), (28, 8), (28, 16), (28, 22), (10, 22), (4, 14)], closed=True)
        self.add_line("lip", (28, 8), (40, 8))
        _path(self, "cab", (28, 16), [(36, 16), (44, 24), (44, 30), (36, 30), (28, 30), (12, 30), (4, 30)])
        self.add_line("cab-rear", (28, 22), (28, 30))
        _circle(self, "wheel-rear", 12, 35, 5)
        _circle(self, "wheel-front", 36, 35, 5)
        for a, b in (("lip", "bed"), ("cab", "bed"), ("cab-rear", "bed"), ("cab-rear", "cab"), ("wheel-rear", "cab"), ("wheel-front", "cab")):
            self.relate("connect", a, b)
