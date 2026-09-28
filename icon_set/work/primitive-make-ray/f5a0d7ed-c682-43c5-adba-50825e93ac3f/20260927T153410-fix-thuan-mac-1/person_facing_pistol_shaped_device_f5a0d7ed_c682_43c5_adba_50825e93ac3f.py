from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f5a0d7ed-c682-43c5-adba-50825e93ac3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-facing-pistol-shaped-device/20260927T153339Z-thuan-mac-1/reference/headshot_f5a0d7ed-c682-43c5-adba-50825e93ac3f.svg'
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
    icon_id = 'person-facing-pistol-shaped-device'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('person', 'facing', 'pistol', 'shaped', 'device')

    def build(self) -> None:
        # Person facing a pistol-shaped device, as in the reference: a head-and-shoulders bust on
        # the left (round head held 8 above a rounded shoulder line that runs off the bottom) and,
        # on the right, a pistol-shaped scanner aimed at the head: a long boxy barrel with a short
        # grip below its back end, raked backward like a pistol grip.
        _circle(self, "head", 11, 14, 4)
        _path(self, "shoulders", (6, 28), [('c', (7.5, 26.7), (9, 26), (11, 26)), ('c', (17, 26), (21, 31), (21, 42))])
        _path(self, "device", (23, 6), [(39, 6), ((42, 9), 3, 3, True), (42, 14), (42, 24), (34, 25), (33, 14), (23, 14),
                                        (23, 6)], True)
