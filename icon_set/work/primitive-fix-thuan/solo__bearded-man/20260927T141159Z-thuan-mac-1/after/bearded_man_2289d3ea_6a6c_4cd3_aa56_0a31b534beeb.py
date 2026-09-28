from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2289d3ea-6a6c-4cd3-aa56-0a31b534beeb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bearded-man/20260927T141159Z-thuan-mac-1/reference/man beard 2_2289d3ea-6a6c-4cd3-aa56-0a31b534beeb.svg'
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
    icon_id = 'bearded-man'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'primitive', 'primitives')
    aliases = ()
    keywords = ('bearded', 'man')

    def build(self) -> None:
        # Bearded man (reference: a head with a full crop of hair on top, ears at the sides, the face
        # band between the hairline and a curly moustache, and a full beard rounding down to the
        # chin). Head only, so the beard gets the room it needs.
        # Hair: an rx14/ry12 dome about (24,18) over a gently sagging hairline (10,18)-(38,18).
        # Ears: r4 half-circles bulging out to x6/x42 between y18 and y26. Moustache: from the ear
        # bottoms (10,26)/(38,26) dipping in two scallops to y31 and peaking at (24,28) under the nose,
        # 8+ below the hairline. Beard: rounds down from the ear bottoms to the chin (24,42).
        k = 0.5523
        self.add_arc("hair", (10, 18), (38, 18), radius_x=14, radius_y=12, sweep=True)
        self.add_bezier("hairline", (10, 18), ((16, 21), (32, 21), (38, 18)))
        self.add_arc("ear-right", (38, 18), (38, 26), radius_x=4, radius_y=4, sweep=True)
        self.add_arc("ear-left", (10, 26), (10, 18), radius_x=4, radius_y=4, sweep=True)
        _path(self, "moustache", (10, 26), [('c', (12, 30), (15, 31), (17, 31)), ('c', (20, 31), (22, 28), (24, 28)),
                                            ('c', (26, 28), (28, 31), (31, 31)), ('c', (33, 31), (36, 30), (38, 26))])
        _path(self, "beard", (10, 26), [('c', (10, 36), (16, 42), (24, 42)), ('c', (32, 42), (38, 36), (38, 26))])
        parts = ("hair", "hairline", "ear-right", "ear-left", "moustache", "beard")
        for a, b in (("hair", "hairline"), ("hair", "ear-right"), ("hair", "ear-left"), ("hairline", "ear-right"),
                     ("hairline", "ear-left"), ("ear-right", "moustache"), ("ear-left", "moustache"),
                     ("beard", "moustache"), ("beard", "ear-left"), ("beard", "ear-right")):
            self.relate("connect", a, b)
