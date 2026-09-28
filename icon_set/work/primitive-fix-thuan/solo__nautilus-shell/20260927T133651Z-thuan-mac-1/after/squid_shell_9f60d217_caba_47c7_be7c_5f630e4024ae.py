from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9f60d217-caba-47c7-be7c-5f630e4024ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__nautilus-shell/20260927T133651Z-thuan-mac-1/reference/squid shell_9f60d217-caba-47c7-be7c-5f630e4024ae.svg'
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
    icon_id = 'nautilus-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('nautilus', 'shell', 'spiral', 'sea', 'marine', 'cephalopod', 'coil', 'ocean')

    def build(self) -> None:
        # Nautilus (reference: big coiled shell with a straight opening line into an inner coil, and two
        # trailing tentacles). The outer whorl (r14) runs from the opening over the top and round to its
        # base, then trails on as the right tentacle; the left tentacle drops from the opening and hooks
        # left. Inner coil r5, 9 inside the whorl.
        _path(self, "whorl", (14, 20), [((28, 6), 14, 14, True), ((42, 20), 14, 14, True), ((28, 34), 14, 14, True),
                                        ('c', (24, 34), (22, 42), (28, 42)), (36, 42)])
        self.add_line("opening", (14, 20), (23, 20))
        _path(self, "coil", (23, 20), [((28, 15), 5, 5, True), ((33, 20), 5, 5, True), ((28, 25), 5, 5, True)])
        _path(self, "tentacle-left", (14, 20), [(14, 38), ((6, 38), 4, 4, True)])
        self.relate("connect", "whorl-1", "opening", "tentacle-left-1")
        self.relate("connect", "opening", "coil-1")
