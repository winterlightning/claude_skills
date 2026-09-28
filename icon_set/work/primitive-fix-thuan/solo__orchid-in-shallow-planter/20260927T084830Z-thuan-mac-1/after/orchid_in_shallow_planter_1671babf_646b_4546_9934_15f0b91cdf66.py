from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1671babf-646b-4546-9934-15f0b91cdf66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__orchid-in-shallow-planter/20260927T084830Z-thuan-mac-1/reference/orchid_1671babf-646b-4546-9934-15f0b91cdf66.svg'
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
    icon_id = 'orchid-in-shallow-planter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('orchid', 'flowers', 'blossoms', 'planter', 'leaves', 'stems', 'plant')

    def build(self) -> None:
        # flowering plant in a shallow planter (reference): a five-petal blossom on a straight stem,
        # two arching leaves and a wide trapezoid planter. Before drew lollipop circles on stems.
        # five round petals: arcs between lattice notches, top petal an exact r3 semicircle
        notches = [(21, 9), (27, 9), (29, 15), (24, 18), (19, 15)]
        radii = [3, 4, 4, 4, 4]
        steps = []
        for n in range(5):
            b = notches[(n + 1) % 5]
            steps.append((b, radii[n], radii[n], True, n > 0))
        _path(self, "blossom", notches[0], steps, True)
        self.add_line("stem", (24, 18), (24, 34))
        self.relate("connect", "stem", "blossom")
        xs = (6, 16, 24, 32, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"rim-{n}", (a, 34), (b, 34))
            if n:
                self.relate("connect", f"rim-{n - 1}", f"rim-{n}")
        self.add_polyline("planter", (6, 34), (10, 42), (38, 42), (42, 34))
        self.relate("connect", "planter", "rim-0"); self.relate("connect", "planter", "rim-3")
        self.relate("connect", "stem", "rim-1"); self.relate("connect", "stem", "rim-2")
        self.add_bezier("leaf-left", (16, 34), ((14, 30), (11, 27.5), (6, 27)))
        self.add_bezier("leaf-right", (32, 34), ((34, 30), (37, 27.5), (42, 27)))
        self.relate("connect", "leaf-left", "rim-0"); self.relate("connect", "leaf-left", "rim-1")
        self.relate("connect", "leaf-right", "rim-2"); self.relate("connect", "leaf-right", "rim-3")
