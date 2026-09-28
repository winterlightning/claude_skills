from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ae8162b-1fa3-4f3e-a7f2-5375c421b45f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wireless-earbuds-charging-case-solo-b001-15/20260927T104205Z-thuan-mac-1/reference/earpods charge_9ae8162b-1fa3-4f3e-a7f2-5375c421b45f.svg'
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
    icon_id = 'wireless-earbuds-charging-case-solo-b001-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('wireless', 'earbuds', 'charging', 'case')

    def build(self) -> None:
        # Plan: an open charging case with two earbuds standing in it, mirrored
        # about x=24. Each earbud = r6 round head about (14,10)/(34,10) whose inner
        # side runs straight down as the stem (x=20/28, tangent at the head's
        # cardinal point) into the case top - the classic AirPod silhouette.
        # Case = rounded rectangle (8,25)-(40,44) with r6 corners and a charging
        # LED dot in the middle of the front.
        _path(self, "case", (20, 25), [(28, 25), (34, 25), ((40, 31), 6, 6, True), (40, 38),
                                       ((34, 44), 6, 6, True), (14, 44), ((8, 38), 6, 6, True),
                                       (8, 31), ((14, 25), 6, 6, True), (20, 25)], True)
        self.add_dot("charge-led", (24, 35))
        for side, s in (("left", 1), ("right", -1)):
            X = lambda x: 24 + s * (x - 24)
            _circle(self, f"bud-{side}-head", X(14), 10, 6)
            self.add_line(f"bud-{side}-stem", (X(20), 10), (X(20), 25))
            self.relate("connect", f"bud-{side}-stem", f"bud-{side}-head")
            self.relate("connect", f"bud-{side}-stem", "case")
