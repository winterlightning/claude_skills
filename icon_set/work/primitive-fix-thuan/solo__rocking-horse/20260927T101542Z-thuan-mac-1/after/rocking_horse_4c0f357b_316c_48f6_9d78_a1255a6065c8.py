from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4c0f357b-316c-48f6-9d78-a1255a6065c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rocking-horse/20260927T101542Z-thuan-mac-1/reference/toys rocking horse_4c0f357b-316c-48f6-9d78-a1255a6065c8.svg'
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
    icon_id = 'rocking-horse'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('rocking', 'horse', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Plan: side-view rocking horse on one long curved runner (three tangent
        # cubics; the middle one bottoms out exactly at y=40); legs splay from the
        # belly to knots on the runner.
        # Horse facing left: pointed ear, long face sloping 45 degrees down to an r3
        # nose, jaw and throat, chest, belly, r4 rounded rump, back and withers; the
        # tail hangs off the rump.
        _path(self, "horse", (15, 8), [(19, 12), (24, 18), (33, 18), ((37, 22), 4, 4, True),
                                       ((33, 26), 4, 4, True), (31, 26), (19, 26), (16, 26),
                                       (15, 21), (7, 22), ((7, 16), 3, 3, True), (15, 8)], True)
        self.add_bezier("tail", (37, 22), ((40, 22), (42, 23), (43, 27)))
        self.relate("connect", "tail", "horse")
        k = 38 + 8 / 3
        self.add_bezier("runner-left", (4, 32), ((5, 34), (9, 36.5), (14, 38)))
        self.add_bezier("runner-mid", (14, 38), ((20, k), (28, k), (34, 38)))
        self.add_bezier("runner-right", (34, 38), ((39, 36.5), (43, 34), (44, 32)))
        self.add_contour("runner", "runner-left", "runner-mid", "runner-right")
        self.add_line("leg-front", (19, 26), (14, 38))
        self.add_line("leg-back", (31, 26), (34, 38))
        for leg in ("leg-front", "leg-back"):
            self.relate("connect", leg, "horse")
            self.relate("connect", leg, "runner")
