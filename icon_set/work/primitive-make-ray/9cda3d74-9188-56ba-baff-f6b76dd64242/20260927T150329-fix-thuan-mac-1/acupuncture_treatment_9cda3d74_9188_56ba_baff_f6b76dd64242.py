from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9cda3d74-9188-56ba-baff-f6b76dd64242'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acupuncture-treatment/20260927T150142Z-thuan-mac-1/reference/acupuncture_9cda3d74-9188-56ba-baff-f6b76dd64242.svg'
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
    icon_id = 'acupuncture-treatment'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('acupuncture', 'treatment')

    def build(self) -> None:
        # acupuncture: a patient lies face down on a treatment bed (r6 head resting on it; the body rises in a
        # rounded shoulder and tapers down toward the feet) with two needles standing out of the back, each with
        # a round knob handle
        self.add_line("bed-1", (4, 40), (10, 40))
        self.add_line("bed-2", (10, 40), (24, 40))
        self.add_line("bed-3", (24, 40), (44, 40))
        _circle(self, "head", 10, 34, 6)
        _path(self, "back", (24, 40), [('c', (24, 32), (24, 27), (28, 27)), (38, 27), ('c', (41, 27), (44, 33), (44, 40))])
        self.add_line("needle-1", (28, 27), (30, 12))
        self.add_line("needle-2", (38, 27), (42, 12))
        _circle(self, "knob-1", 30, 10, 2)
        _circle(self, "knob-2", 42, 10, 2)
        pairs = [("bed-1", "bed-2"), ("bed-2", "bed-3"), ("head", "bed-1"), ("head", "bed-2"), ("back", "bed-2"),
                 ("back", "bed-3"), ("needle-1", "back"), ("needle-2", "back"), ("needle-1", "knob-1"), ("needle-2", "knob-2")]
        for a, b in pairs:
            self.relate("connect", a, b)
