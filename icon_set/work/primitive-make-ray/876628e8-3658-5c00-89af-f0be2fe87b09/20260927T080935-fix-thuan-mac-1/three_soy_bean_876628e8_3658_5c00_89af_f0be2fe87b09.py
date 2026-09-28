from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '876628e8-3658-5c00-89af-f0be2fe87b09'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-soy-bean/20260927T080754Z-thuan-mac-1/reference/black bean_876628e8-3658-5c00-89af-f0be2fe87b09.svg'
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


class Drawing(Solo48):
    icon_id = 'three-soy-bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('three', 'soy', 'bean')

    def build(self) -> None:
        import math

        def ellipse(name, cx, cy, a, b, deg, shift=(0, 0)):
            """Tilted ellipse as four cubics between its axis-extreme points (knots rounded to the grid)."""
            th = math.radians(deg)
            P = lambda t: (cx + a * math.cos(th) * math.cos(t) - b * math.sin(th) * math.sin(t),
                           cy + a * math.sin(th) * math.cos(t) + b * math.cos(th) * math.sin(t))
            D = lambda t: (-a * math.cos(th) * math.sin(t) - b * math.sin(th) * math.cos(t),
                           -a * math.sin(th) * math.sin(t) + b * math.cos(th) * math.cos(t))
            tx = math.atan2(-b * math.sin(th), a * math.cos(th))      # x extreme
            ty = math.atan2(b * math.cos(th), a * math.sin(th))       # y extreme
            ts = sorted(t % (2 * math.pi) for t in (tx, tx + math.pi, ty, ty + math.pi))
            knots = [tuple(int(round(v)) for v in P(t)) for t in ts]
            segs = []
            for i in range(4):
                t1, t2 = ts[i], ts[(i + 1) % 4] + (2 * math.pi if i == 3 else 0)
                d = t2 - t1
                al = math.sin(d) * (math.sqrt(4 + 3 * math.tan(d / 2) ** 2) - 1) / 3
                k1, k2 = knots[i], knots[(i + 1) % 4]
                d1, d2 = D(t1), D(t2)
                # keep handles axis-aligned at the extreme knots
                c1 = (k1[0] + al * d1[0], k1[1] + al * d1[1])
                c2 = (k2[0] - al * d2[0], k2[1] - al * d2[1])
                segs.append(('c', c1, c2, k2))
            kn = [(k[0] + shift[0], k[1] + shift[1]) for k in knots]
            segs = [('c', (s[1][0] + shift[0], s[1][1] + shift[1]), (s[2][0] + shift[0], s[2][1] + shift[1]),
                     (s[3][0] + shift[0], s[3][1] + shift[1])) for s in segs]
            return _path(self, name, kn[0], segs, True)
        # three scattered, differently tilted beans as in the reference
        ellipse("bean-a", 31.38, 12.64, 11, 6, 18)
        ellipse("bean-b", 12.245, 31, 9, 5, -60)
        ellipse("bean-c", 33.86, 34.87, 9, 6, 35)
