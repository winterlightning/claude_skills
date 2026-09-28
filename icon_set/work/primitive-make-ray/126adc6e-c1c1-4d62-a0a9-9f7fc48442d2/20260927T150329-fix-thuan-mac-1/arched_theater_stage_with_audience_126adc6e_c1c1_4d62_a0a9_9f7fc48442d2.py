from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '126adc6e-c1c1-4d62-a0a9-9f7fc48442d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-theater-stage-with-audience/20260927T150142Z-thuan-mac-1/reference/ramlila_126adc6e-c1c1-4d62-a0a9-9f7fc48442d2.svg'
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
    icon_id = 'arched-theater-stage-with-audience'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('arched', 'theater', 'stage', 'with', 'audience')

    def build(self) -> None:
        # arched stage opening (r10 arch on short legs) above a row of three audience busts; each bust is an r2
        # head resting on an elliptical shoulder arch (shared axis, jaw 4 above the arch top); shoulders meet
        self.add_line("leg-l", (14, 22), (14, 16))
        self.add_arc("arch", (14, 16), (34, 16), radius_x=10, radius_y=10, sweep=True)
        self.add_line("leg-r", (34, 16), (34, 22))
        self.relate("connect", "leg-l", "arch")
        self.relate("connect", "arch", "leg-r")
        for i, cx in enumerate((12, 24, 36)):
            _circle(self, f"head-{i}", cx, 32, 2)
            self.add_arc(f"shoulders-{i}", (cx - 6, 42), (cx + 6, 42), radius_x=6, radius_y=4, sweep=True)
            self.relate("connect", f"head-{i}", f"shoulders-{i}")
        self.relate("connect", "shoulders-0", "shoulders-1")
        self.relate("connect", "shoulders-1", "shoulders-2")
