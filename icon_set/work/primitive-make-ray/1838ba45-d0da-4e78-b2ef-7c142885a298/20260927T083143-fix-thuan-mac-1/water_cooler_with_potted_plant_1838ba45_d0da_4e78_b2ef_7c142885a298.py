from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1838ba45-d0da-4e78-b2ef-7c142885a298'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-cooler-with-potted-plant/20260927T083044Z-thuan-mac-1/reference/outdoors_1838ba45-d0da-4e78-b2ef-7c142885a298.svg'
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
    icon_id = 'water-cooler-with-potted-plant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: office water cooler and a potted tree on one ground line, as in the reference.
        # Cooler: water jug (rounded top) tapering into its neck, seated on a wider stand top
        # with two legs and a tap hanging under the neck. Tree: r8 round crown on a trunk in a
        # tapered pot whose base is the ground line (y40), which spans the scene.
        _path(self, "jug", (9, 8), [(15, 8), ((18, 11), 3, 3, True), (18, 18), (14, 24), (10, 24), (6, 18),
                                     (6, 11), ((9, 8), 3, 3, True)], closed=True)
        _path(self, "stand-top", (4, 24), [(10, 24), (12, 24), (14, 24), (20, 24)])
        self.relate("connect", "stand-top", "jug")
        self.add_line("tap", (12, 24), (12, 28))
        self.relate("connect", "tap", "stand-top-2", "stand-top-3")
        self.add_line("leg-left", (4, 24), (4, 40))
        self.add_line("leg-right", (20, 24), (20, 40))
        self.relate("connect", "leg-left", "stand-top-1")
        self.relate("connect", "leg-right", "stand-top-4")
        _path(self, "ground", (4, 40), [(20, 40), (32, 40), (40, 40), (44, 40)])
        self.relate("connect", "ground", "leg-left", "leg-right")
        _circle(self, "crown", 36, 16, 8)
        self.add_line("trunk", (36, 24), (36, 32))
        _path(self, "pot", (32, 40), [(31, 32), (41, 32), (40, 40)])
        self.relate("connect", "trunk", "crown", "pot")
        self.relate("connect", "pot", "ground")
