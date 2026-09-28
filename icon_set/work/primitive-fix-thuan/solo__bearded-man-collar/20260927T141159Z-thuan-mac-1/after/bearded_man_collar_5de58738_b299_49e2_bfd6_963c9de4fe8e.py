from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5de58738-b299-49e2-bfd6-963c9de4fe8e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bearded-man-collar/20260927T141159Z-thuan-mac-1/reference/man beard 1_5de58738-b299-49e2-bfd6-963c9de4fe8e.svg'
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
    icon_id = 'bearded-man-collar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'primitive', 'primitives')
    aliases = ()
    keywords = ('bearded', 'man', 'collar')

    def build(self) -> None:
        # Bearded man with a shirt collar (reference: a bust: hair dome on top, ears at the sides,
        # the face band down to a curly moustache, a full beard rounding to the chin, broad shoulders
        # with an open shirt collar). Avatar construction (human_ref/user.svg, touching jaw/body):
        # hair dome rx12/ry8 about (24,14) over the hairline y14; r4 ears bulging to x8/x40;
        # moustache: two scallops from the ear bottoms (12,22)/(36,22) meeting at (24,22); the beard
        # is the jaw, ONE r13 arc about (24,17) down to the chin y30, exactly 4 above the flat
        # body-top y34. Shoulders: r8 arcs down to (6,42)/(42,42). Collar: a V from the body-top at
        # (16,34)/(32,34), leaving steeply and rounding down to (24,42).
        self.add_arc("hair", (12, 14), (36, 14), radius_x=12, radius_y=8, sweep=True)
        self.add_line("hairline", (12, 14), (36, 14))
        self.add_arc("ear-right", (36, 14), (36, 22), radius_x=4, radius_y=4, sweep=True)
        _path(self, "moustache", (36, 22), [('c', (33, 25), (27, 25), (24, 22)), ('c', (21, 25), (15, 25), (12, 22))])
        self.add_arc("ear-left", (12, 22), (12, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_arc("jaw", (12, 22), (36, 22), radius_x=13, radius_y=13, sweep=False)
        for a, b in (("hair", "hairline"), ("hair", "ear-right"), ("hair", "ear-left"), ("hairline", "ear-right"),
                     ("hairline", "ear-left"), ("ear-right", "moustache"), ("ear-left", "moustache"),
                     ("jaw", "moustache"), ("jaw", "ear-left"), ("jaw", "ear-right")):
            self.relate("connect", a, b)
        self.add_arc("shoulder-left", (6, 42), (14, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line("body-top-l", (14, 34), (16, 34))
        self.add_line("body-top", (16, 34), (32, 34))
        self.add_line("body-top-r", (32, 34), (34, 34))
        self.add_arc("shoulder-right", (34, 34), (42, 42), radius_x=8, radius_y=8, sweep=True)
        _path(self, "collar", (16, 34), [("c", (17, 39), (20, 42), (24, 42)), ("c", (28, 42), (31, 39), (32, 34))])
        for a, b in (("shoulder-left", "body-top-l"), ("body-top-l", "body-top"), ("body-top", "body-top-r"),
                     ("body-top-r", "shoulder-right"), ("collar", "body-top"), ("collar", "body-top-l"),
                     ("collar", "body-top-r"), ("jaw", "body-top")):
            self.relate("connect", a, b)
