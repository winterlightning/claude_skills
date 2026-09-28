from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c255cd70-d42e-428e-90f6-fea19ecba7bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__information-desk-man/20260927T070909Z-thuan-mac-1/reference/information desk man_c255cd70-d42e-428e-90f6-fea19ecba7bb.svg'
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
    icon_id = 'information-desk-man'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('information', 'desk', 'man', 'wayfinding')

    def build(self) -> None:
        # person behind a counter (human ref user.svg): detached r4 head, shoulder arch rising 8 above the
        # counter top with its top exactly 8 below the head (4-unit ink gap), counter and legs
        _circle(self, "head", 24, 10, 4)
        self.add_arc("shoulders", (14, 30), (34, 30), radius_x=10, radius_y=8)
        self.mark_human_figure("person", head="head", torso="shoulders", torso_junction="start")
        xs = (6, 14, 34, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"counter-top-{n}", (a, 30), (b, 30))
        self.add_polyline("counter", (42, 30), (42, 38), (6, 38), (6, 30))
        self.add_line("leg-left", (10, 38), (10, 42))
        self.add_line("leg-right", (38, 38), (38, 42))
        for a, b in (("counter-top-0", "counter-top-1"), ("counter-top-1", "counter-top-2"), ("counter", "counter-top-0"),
                     ("counter", "counter-top-2"), ("shoulders", "counter-top-1"), ("shoulders", "counter-top-0"),
                     ("shoulders", "counter-top-2"), ("leg-left", "counter"), ("leg-right", "counter")):
            self.relate("connect", a, b)
