from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '423dcab8-75b5-46fd-acba-3c2dc79a82f1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__physical-therapy-session-423dcab8/20260927T133650Z-thuan-mac-1/reference/specialty rehabilitation_423dcab8-75b5-46fd-acba-3c2dc79a82f1.svg'
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
    icon_id = 'physical-therapy-session-423dcab8'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('physical', 'therapy', 'session')

    def build(self) -> None:
        # Physical therapy session, as in the reference: a patient lying face down along the bottom (a
        # straight body with the head resting just past the level neck) and the therapist
        # above, a user-style bust (round head exactly 8 above round shoulders) whose arm reaches down
        # to press on the patient's back.
        _circle(self, "patient-head", 38, 38, 4)
        self.add_line("patient-legs", (6, 38), (16, 38))
        self.add_line("patient-torso", (16, 38), (25, 38))
        self.relate("connect", "patient-legs", "patient-torso")
        self.mark_human_figure("patient", head="patient-head", torso="patient-torso", torso_junction="end")
        _circle(self, "head", 29, 10, 4)
        _path(self, "shoulders", (22, 26), [((26, 22), 4, 4, True), (33, 22), ((37, 26), 4, 4, True)])
        self.add_line("arm", (22, 26), (16, 38))
        for a, b in (("shoulders", "arm"), ("arm", "patient-legs"), ("arm", "patient-torso")):
            self.relate("connect", a, b)
