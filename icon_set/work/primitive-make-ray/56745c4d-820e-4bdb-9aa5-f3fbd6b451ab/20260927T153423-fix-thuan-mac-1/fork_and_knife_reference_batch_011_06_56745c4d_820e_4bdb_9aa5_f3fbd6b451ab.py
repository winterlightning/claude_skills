from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '56745c4d-820e-4bdb-9aa5-f3fbd6b451ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fork-and-knife-reference-batch-011-06/20260927T153247Z-thuan-mac-1/reference/fork and spoon_56745c4d-820e-4bdb-9aa5-f3fbd6b451ab.svg'
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


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'fork-and-knife-reference-batch-011-06'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('food', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('fork', 'knife', 'cutlery', 'utensils', 'meal', 'dining')

    def build(self) -> None:
        # Fork and knife standing side by side, as in the reference: a tall fork whose two outer
        # tines curve into a round U around the middle tine, which runs straight down as the
        # handle, and a knife whose blade leaves the top of the straight spine, sweeps out to the
        # right and curls back into the spine above the handle.
        _path(self, "fork-u", (8, 4), [(8, 14), ((16, 22), 8, 8, False), ((24, 14), 8, 8, False), (24, 4)])
        self.add_line("fork-tine", (16, 4), (16, 22))
        self.add_line("fork-handle", (16, 22), (16, 44))
        _path(self, "knife", (32, 44), [(32, 26), (32, 4), ('c', (36, 9), (40, 16), (40, 21)),
                                        ('c', (40, 24.5), (36, 26), (32, 26))])
        for a, b in (("fork-u", "fork-tine"), ("fork-u", "fork-handle"), ("fork-tine", "fork-handle")):
            self.relate("connect", a, b)
