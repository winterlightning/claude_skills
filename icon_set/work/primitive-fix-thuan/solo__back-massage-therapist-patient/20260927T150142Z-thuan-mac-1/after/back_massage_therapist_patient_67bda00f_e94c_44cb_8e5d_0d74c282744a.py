from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '67bda00f-e94c-44cb-8e5d-0d74c282744a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__back-massage-therapist-patient/20260927T150142Z-thuan-mac-1/reference/massage back_67bda00f-e94c-44cb-8e5d-0d74c282744a.svg'
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
    icon_id = 'back-massage-therapist-patient'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    human_construction = "bust"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('back', 'massage', 'therapy')

    def build(self) -> None:
        # back massage, after the reference: the patient lies face down (capsule body with the legs running off to
        # the left, r4 head at the right end); the therapist is a bust over the patient's upper back (r4 head
        # resting on a rounded r8 shoulder dome, shared axis x=18) whose sides drop onto the patient's back
        _path(self, "patient", (8, 32), [(10, 32), (24, 32), ((24, 40), 4, 4, True), (8, 40), ((8, 32), 4, 4, True)], True)
        _circle(self, "patient-head", 40, 36, 4)
        _circle(self, "therapist-head", 18, 12, 4)
        _path(self, "therapist-body", (10, 32), [(10, 28), ((18, 20), 8, 8, True), ((26, 28), 8, 8, True), (24, 32)])
        self.relate("connect", "therapist-head", "therapist-body")
        self.relate("connect", "therapist-body", "patient")
