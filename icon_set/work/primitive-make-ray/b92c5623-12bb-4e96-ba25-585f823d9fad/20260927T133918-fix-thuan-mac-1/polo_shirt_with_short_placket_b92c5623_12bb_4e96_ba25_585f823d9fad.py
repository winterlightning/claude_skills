from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b92c5623-12bb-4e96-ba25-585f823d9fad'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__polo-shirt-with-short-placket/20260927T133651Z-thuan-mac-1/reference/shirt male_b92c5623-12bb-4e96-ba25-585f823d9fad.svg'
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
    icon_id = 'polo-shirt-with-short-placket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('polo', 'shirt', 'with', 'short', 'placket')

    def build(self) -> None:
        # Polo shirt (Lucide shirt construction at 2x): sloped shoulders, short sleeves with level cuffs,
        # straight body; the collar opening dips to a V and a short placket runs down from it.
        _path(self, "shirt", (18, 6), [(6, 12), (6, 24), (12, 24), (12, 42), (36, 42), (36, 24), (42, 24), (42, 12),
                                       (30, 6), (24, 14), (18, 6)], True)
        self.add_line("placket", (24, 14), (24, 24))
        self.relate("connect", "shirt-10", "shirt-11", "placket")
