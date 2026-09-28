from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '270a1a6b-80b7-445e-85e4-d5adfa15b5c5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__podcast-microphone-beside-laptop/20260927T104205Z-thuan-mac-1/reference/microphone podcast laptop_270a1a6b-80b7-445e-85e4-d5adfa15b5c5.svg'
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
    icon_id = 'podcast-microphone-beside-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('podcast', 'microphone', 'beside', 'laptop')

    def build(self) -> None:
        # Plan: left, an open laptop (Lucide laptop at 2x: screen rectangle
        # (6,10)-(22,24) over a wider keyboard base line 8 below). Right, a
        # podcast microphone on a desk stand: a 12-wide capsule (r6 caps about
        # (38,14)/(38,22)) with two grille bands across it at the cap joins, a
        # stem down from the capsule bottom and a flat foot on y=40.
        _path(self, "screen", (6, 10), [(22, 10), (22, 24), (6, 24), (6, 10)], True)
        self.add_line("base", (4, 32), (24, 32))
        _path(self, "capsule", (32, 14), [((44, 14), 6, 6, True), (44, 22), ((32, 22), 6, 6, True), (32, 14)], True)
        self.add_line("grille-top", (32, 14), (44, 14))
        self.add_line("grille-bottom", (32, 22), (44, 22))
        self.add_line("stem", (38, 28), (38, 40))
        self.add_line("foot", (32, 40), (44, 40))
        for part in ("grille-top", "grille-bottom", "stem"):
            self.relate("connect", part, "capsule")
        self.relate("connect", "stem", "foot")
