from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'adb04192-9291-4a64-8bd6-a8f21d407e1b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bather-sitting-in-a-rounded-tub/20260927T141159Z-thuan-mac-1/reference/bathroom tub person_adb04192-9291-4a64-8bd6-a8f21d407e1b.svg'
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
    icon_id = 'bather-sitting-in-a-rounded-tub'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bather', 'bathtub', 'person', 'bath', 'arm', 'water', 'tub')

    def build(self) -> None:
        # Bather sitting in a rounded tub (reference: a round bowl tub with a straight rim, a person
        # sitting in it with head and shoulders above the rim).
        # Tub: rim line y30 across x6-42 and an rx18/ry12 half-ellipse bowl down to y42.
        # Bather (human_ref/user.svg bust): r4 ring head about (16,10); the shoulders an r8 dome about
        # (16,30) rising from the rim, its crown exactly 8 below the head.
        _circle(self, "head", 16, 10, 4)
        self.add_arc("shoulders", (8, 30), (24, 30), radius_x=8, radius_y=8, sweep=True)
        self.add_line("rim-1", (6, 30), (8, 30))
        self.add_line("rim-2", (8, 30), (24, 30))
        self.add_line("rim-3", (24, 30), (42, 30))
        self.add_arc("bowl", (42, 30), (6, 30), radius_x=18, radius_y=12, sweep=True)
        rims = ["rim-1", "rim-2", "rim-3"]
        for a, b in zip(rims, rims[1:]):
            self.relate("connect", a, b)
        for part, touching in (("shoulders", ("rim-1", "rim-2", "rim-3")), ("bowl", ("rim-1", "rim-3"))):
            for t in touching:
                self.relate("connect", part, t)
