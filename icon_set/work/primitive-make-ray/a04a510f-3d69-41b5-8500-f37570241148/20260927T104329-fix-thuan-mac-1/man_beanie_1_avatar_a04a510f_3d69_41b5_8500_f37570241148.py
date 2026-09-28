from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a04a510f-3d69-41b5-8500-f37570241148'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-beanie-1-avatar/20260927T104205Z-thuan-mac-1/reference/man beanie 1_a04a510f-3d69-41b5-8500-f37570241148.svg'
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
    icon_id = 'man-beanie-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'primitive', 'primitives')
    aliases = ()
    keywords = ('man', 'beanie', '1', 'portrait', 'bust')

    def build(self) -> None:
        # Plan (reference): a man's bust wearing a beanie, mirrored about x=24.
        # Beanie = low dome crown (half-ellipse rx12 ry9, top on y=4) standing on
        # a rolled cuff drawn as an 8-tall pill (r4 caps, x=8..40) across the
        # forehead. Face = r12 jaw arc about (24,21) hanging from the cuff's
        # lower edge, as wide as the crown (bottom on y=33). Shoulders = one
        # half-ellipse arch (rx16, ry7 about (24,44)) whose top touches the jaw
        # exactly 4 below it (avatar contact) and whose feet reach the bottom
        # corners.
        self.add_arc("crown", (12, 13), (36, 13), radius_x=12, radius_y=9, sweep=True)
        _path(self, "cuff", (12, 13), [(36, 13), ((36, 21), 4, 4, True), (12, 21),
                                       ((12, 13), 4, 4, True)], True)
        self.add_arc("face", (36, 21), (12, 21), radius_x=12, radius_y=12, sweep=True)
        self.add_arc("shoulders", (8, 44), (40, 44), radius_x=16, radius_y=7, sweep=True)
        self.relate("connect", "crown", "cuff")
        self.relate("connect", "face", "cuff")
        self.relate("connect", "face", "shoulders")
