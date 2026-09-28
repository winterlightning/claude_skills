from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '13cb93f6-c485-4531-8105-41c9f2431b89'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shining-easter-eggs/20260927T101542Z-thuan-mac-1/reference/easter egg_13cb93f6-c485-4531-8105-41c9f2431b89.svg'
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


class Drawing(Solo48):
    icon_id = 'shining-easter-eggs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('shining', 'easter', 'eggs')

    def build(self) -> None:
        import math

        # Hermite cubics through integer knots with given tangent directions (axis-aligned
        # at the extremes, so the keyshape fit is exact); handle = chord * k.
        def herm(name, knots, closed, k=0.38):
            n = len(knots); members = []
            for i in range(n if closed else n - 1):
                (p1, t1), (p2, t2) = knots[i], knots[(i + 1) % n]
                L = math.dist(p1, p2) * k
                u1 = (t1[0] / math.hypot(*t1), t1[1] / math.hypot(*t1))
                u2 = (t2[0] / math.hypot(*t2), t2[1] / math.hypot(*t2))
                c1 = (p1[0] + u1[0] * L, p1[1] + u1[1] * L)
                c2 = (p2[0] - u2[0] * L, p2[1] - u2[1] * L)
                m = f"{name}-{i + 1}"; self.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
            self.add_contour(name, *members, closed=closed)

        J1, J2 = (23, 27), (24, 40)
        # Front egg lying on the right, about (31,33): x 20..42, y 24..42.
        herm("egg-front", [((20, 33), (0, -1)), (J1, (1, -1)), ((31, 24), (1, 0)), ((42, 33), (0, 1)),
                           ((31, 42), (-1, 0)), (J2, (-1, -1))], True)
        # Tall back egg on the left (tapered top), its lower right hidden behind the front egg.
        herm("egg-back", [(J1, (-0.2, -1)), ((20, 20), (-0.7, -1)), ((15, 16), (-1, 0)), ((10, 20), (-0.7, 1)),
                          ((7, 26), (-0.3, 1)), ((6, 31), (0, 1)), ((15, 42), (1, 0)), (J2, (1, -0.6))], False)
        # Decorative band across the back egg, running behind the front egg.
        herm("band", [((7, 26), (1, 0.35)), (J1, (1, -0.35))], False, k=0.35)
        self.relate("occlude", "egg-front", "egg-back")
        self.relate("connect", "egg-back", "band")
        self.relate("connect", "egg-front", "band")
        # Shine rays above.
        self.add_line("ray-top", (15, 6), (15, 8))
        self.add_line("ray-left", (6, 10), (7, 11))
        self.add_line("ray-right", (24, 10), (26, 8))
        self.add_line("ray-far-right", (35, 14), (38, 12))
