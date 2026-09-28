from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6f954029-c6f4-4eea-8610-b9a1827cde85'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-riding-handcycle/20260927T072841Z-thuan-mac-1/reference/handcycle_6f954029-c6f4-4eea-8610-b9a1827cde85.svg'
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
    icon_id = 'person-riding-handcycle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('handcycle', 'rider', 'cycle', 'accessibility', 'mobility', 'sport')

    def build(self) -> None:
        # handcycle: r6 wheels; seat on the rear wheel's top, the rider's legs stretch to the front wheel; crank post
        _circle(self, "rear-wheel", 12, 36, 6)
        _circle(self, "front-wheel", 36, 36, 6)
        self.add_line("frame-0", (12, 30), (18, 30))
        self.add_line("legs", (18, 30), (30, 36))
        self.add_line("crank", (36, 30), (32, 17))
        # rider (human ref full_body_ref.png): r4 head exactly 8 above the upright torso seated on the frame,
        # arm reaching forward and bending up to the crank handle
        _circle(self, "head", 18, 10, 4)
        self.add_line("torso", (18, 22), (18, 24))
        self.add_line("body", (18, 24), (18, 30))
        self.mark_human_figure("rider", head="head", torso="torso", torso_junction="start")
        self.add_polyline("arm", (18, 24), (26, 22), (32, 17))
        for a, b in (("frame-0", "legs"), ("rear-wheel", "frame-0"), ("front-wheel", "legs"), ("front-wheel", "crank"), ("torso", "body"), ("torso", "arm"), ("body", "arm"), ("body", "frame-0"), ("body", "legs"), ("arm", "crank")):
            self.relate("connect", a, b)
