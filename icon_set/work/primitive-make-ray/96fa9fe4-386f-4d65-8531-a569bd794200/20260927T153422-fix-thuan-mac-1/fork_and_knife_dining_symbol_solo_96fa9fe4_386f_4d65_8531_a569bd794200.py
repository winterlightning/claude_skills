from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fork-and-knife-dining-symbol-solo/20260927T153247Z-thuan-mac-1/reference/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
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
    icon_id = 'fork-and-knife-dining-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sub icon', 'fork and knife dining symbol')

    def build(self) -> None:
        # Dining symbol, as in the reference: a round plate rim with a fork and a knife standing
        # side by side inside it. Fork = two tines joined by a round U into a straight handle;
        # knife = straight spine with a rounded blade bulging to the right at the top.
        _circle(self, "plate", 24, 24, 20)
        _path(self, "fork", (13, 20), [(13, 23), ((21, 23), 4, 4, False), (21, 20)])
        self.add_line("fork-handle", (17, 27), (17, 33))
        _path(self, "knife", (29, 34), [(29, 26), (29, 14), ('c', (32, 15), (35, 18), (35, 22)),
                                        ('c', (35, 24.5), (32.5, 26), (29, 26))])
        self.relate("connect", "fork", "fork-handle")
