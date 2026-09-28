from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2edb1386-cc42-5319-ac47-13902a62e1ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__spiral-shell/20260927T133656Z-thuan-mac-1/reference/shell_2edb1386-cc42-5319-ac47-13902a62e1ed.svg'
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
    icon_id = 'spiral-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('shell', 'spiral', 'snail', 'nautilus', 'sea', 'beach', 'coil', 'marine')

    def build(self) -> None:
        # Shell as in the reference: a closed outer whorl that flares into a lip at the lower right and meets
        # the inner coil at junction J; the coil winds one turn inside, 9 units from the whorl.
        def herm(name, knots, closed=False):
            pts = knots + ([knots[0]] if closed else [])
            members = []
            for i in range(len(pts) - 1):
                (p0, t0, k0), (p1, t1, k1) = pts[i], pts[i + 1]
                c1 = (p0[0] + t0[0] * k0, p0[1] + t0[1] * k0)
                c2 = (p1[0] - t1[0] * k1, p1[1] - t1[1] * k1)
                m = f"{name}-{i + 1}"
                self.add_bezier(m, p0, (c1, c2, p1)); members.append(m)
            self.add_contour(name, *members, closed=closed)
        J = (36, 30)
        herm("whorl", [
            (J, (0.45, -0.9), 5),
            ((38, 18), (0, -1), 4),
            ((22, 6), (-1, 0), 9),
            ((6, 22), (0, 1), 9),
            ((24, 42), (1, 0), 9),
            ((42, 38), (0, -1), 4),
            (J, (-0.7, -0.7), 4),
        ])
        herm("coil", [
            (J, (-1, 0.25), 5),
            ((24, 33), (-1, 0), 5),
            ((15, 23), (0, -1), 5),
            ((22, 15), (1, 0), 4),
            ((29, 22), (0, 1), 3),
        ])
        self.relate("connect", "whorl", "coil")
