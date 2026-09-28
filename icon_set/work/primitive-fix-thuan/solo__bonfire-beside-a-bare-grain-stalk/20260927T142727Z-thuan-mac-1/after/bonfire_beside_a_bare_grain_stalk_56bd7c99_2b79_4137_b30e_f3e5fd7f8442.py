from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '56bd7c99-2b79-4137-b30e-f3e5fd7f8442'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bonfire-beside-a-bare-grain-stalk/20260927T142727Z-thuan-mac-1/reference/bhogi fire_56bd7c99-2b79-4137-b30e-f3e5fd7f8442.svg'
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
    icon_id = 'bonfire-beside-a-bare-grain-stalk'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bonfire', 'flame', 'sticks', 'grain', 'stalk', 'harvest', 'festival')

    def build(self) -> None:
        # Bhogi bonfire beside a bare grain stalk, as in the reference: a Lucide-style flame (round
        # body, tall tongue, lower side tongue behind a notch) sitting on two crossed logs, and to
        # its right a straight stalk with two V pairs of bare branches.
        _path(self, "flame", (14, 37), [((4, 27), 10, 10, True), ('c', (4, 25.4), (4.6, 23.7), (6, 23)),
                                        ((9, 26), 3, 3, False), ((12, 23), 3, 3, False),
                                        ('c', (12, 19), (9, 14), (14, 9)),
                                        ('c', (14.7, 13.4), (16.9, 16.9), (20, 19)),
                                        ('c', (22.6, 21.4), (24, 24.1), (24, 27)), ((14, 37), 10, 10, True)], True)
        _path(self, "log-a", (4, 34), [(14, 37), (24, 40)])
        _path(self, "log-b", (4, 40), [(14, 37), (24, 34)])
        self.relate("connect", "flame", "log-a")
        self.relate("connect", "flame", "log-b")
        self.relate("connect", "log-a", "log-b")
        self.add_line("stalk", (38, 8), (38, 18))
        self.add_line("stalk-mid", (38, 18), (38, 32))
        self.add_line("stalk-low", (38, 32), (38, 40))
        for name, a, b in (("branch-ul", (38, 18), (32, 10)), ("branch-ur", (38, 18), (44, 10)),
                           ("branch-ll", (38, 32), (32, 24)), ("branch-lr", (38, 32), (44, 24))):
            self.add_line(name, a, b)
        for a, b in (("stalk", "stalk-mid"), ("stalk-mid", "stalk-low"), ("branch-ul", "stalk"), ("branch-ur", "stalk"),
                     ("branch-ul", "stalk-mid"), ("branch-ur", "stalk-mid"), ("branch-ll", "stalk-mid"),
                     ("branch-lr", "stalk-mid"), ("branch-ll", "stalk-low"), ("branch-lr", "stalk-low")):
            self.relate("connect", a, b)
