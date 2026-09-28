from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9791b83d-e217-4313-8247-0c609a1b5e16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__blank-face-bob-hair-bust-batch-057/20260927T142727Z-thuan-mac-1/reference/grandmother_9791b83d-e217-4313-8247-0c609a1b5e16.svg'
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
    icon_id = 'blank-face-bob-hair-bust-batch-057'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'bust', 'portrait', 'bob', 'hair', 'avatar')

    def build(self) -> None:
        # Woman with a jaw-length bob (human ref: icon_set/references/human_ref/user.svg): a round
        # head resting on broad shoulders (circular jaw centred on x=24, its bottom exactly 4 above
        # the straight body-top line), a fringe hairline sweeping from the right temple up to the
        # left of the crown as in the reference, and the bob ending in short flicks below the
        # temples. No face features.
        cx, cy, r = 24, 16, 10
        top = cy + r + 4
        _path(self, "head", (cx - r, cy), [((18, 8), r, r, True), ((cx + r, cy), r, r, True),
                                          ((cx - r, cy), r, r, True)], True)
        _path(self, "fringe", (cx + r, cy), [('c', (31, 14), (24, 14.5), (18, 8))])
        self.add_line("bob-left", (cx - r, cy), (12, 22))
        self.add_line("bob-right", (cx + r, cy), (36, 22))
        for part in ("fringe", "bob-left", "bob-right"):
            self.relate("connect", "head", part)
        self.add_line("body-top", (16, top), (cx, top))
        self.add_line("body-top-right", (cx, top), (32, top))
        self.add_arc("shoulder-left", (16, top), (6, 42), radius_x=10, radius_y=42 - top, sweep=False)
        self.add_arc("shoulder-right", (32, top), (42, 42), radius_x=10, radius_y=42 - top, sweep=True)
        for a, b in (("body-top", "body-top-right"), ("body-top", "shoulder-left"), ("body-top-right", "shoulder-right"),
                     ("head", "body-top"), ("head", "body-top-right")):
            self.relate("connect", a, b)
