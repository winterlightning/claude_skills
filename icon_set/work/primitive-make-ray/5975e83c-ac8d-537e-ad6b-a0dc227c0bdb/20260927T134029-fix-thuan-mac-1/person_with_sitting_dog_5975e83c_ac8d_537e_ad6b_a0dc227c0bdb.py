from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5975e83c-ac8d-537e-ad6b-a0dc227c0bdb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-sitting-dog/20260927T133650Z-thuan-mac-1/reference/dog playing_5975e83c-ac8d-537e-ad6b-a0dc227c0bdb.svg'
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
    icon_id = 'person-with-sitting-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'person', 'owner', 'training', 'play', 'pet', 'companion')

    def build(self) -> None:
        # Person playing with a dog, as in the reference: a user-style bust at the left (round head
        # exactly 8 above the shoulder) raising one arm up and out, and a dog's head in profile at the
        # lower right looking up at the hand - a squared snout, domed skull and a floppy ear hanging
        # at the back, with the neck running down.
        _circle(self, "head", 11, 11, 5)
        _path(self, "body", (6, 42), [(6, 28), ((10, 24), 4, 4, True), (14, 24)])
        self.add_line("side", (14, 24), (14, 42))
        self.add_line("arm", (14, 24), (30, 17))
        self.relate("connect", "body", "side")
        self.relate("connect", "body", "arm")
        self.relate("connect", "side", "arm")
        _path(self, "dog", (26, 42), [(26, 38), (22, 38), (22, 30), (28, 30), ('c', (30, 27), (32, 25), (35, 25)),
                                      ('c', (39, 25), (42, 26), (42, 30)), (42, 36), ((34, 36), 4, 4, True), (34, 33)])
