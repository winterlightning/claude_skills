from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e7507033-a4fb-4857-8a9a-208685a6411c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-women-pyramid/20260927T080754Z-thuan-mac-1/reference/user multiple half female group_e7507033-a4fb-4857-8a9a-208685a6411c.svg'
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
    icon_id = 'three-women-pyramid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('women', 'group', 'three', 'team', 'female', 'users', 'people', 'community')

    def build(self) -> None:
        # apex woman: head with flared side locks + shoulder arc tucked behind two front women's heads (flared locks)
        _circle(self, "head-top", 24, 12, 6)
        self.add_line("lock-top-l", (18, 12), (16, 20))
        self.add_line("lock-top-r", (30, 12), (32, 20))
        self.relate("connect", "lock-top-l", "head-top-3"); self.relate("connect", "lock-top-l", "head-top-4")
        self.relate("connect", "lock-top-r", "head-top-1"); self.relate("connect", "lock-top-r", "head-top-2")
        _path(self, "head-l", (13, 32), [((16, 33), 5, 5, True), ((18, 37), 5, 5, True), ((13, 42), 5, 5, True),
                                          ((8, 37), 5, 5, True), ((13, 32), 5, 5, True)], True)
        _path(self, "head-r", (35, 32), [((40, 37), 5, 5, True), ((35, 42), 5, 5, True), ((30, 37), 5, 5, True),
                                          ((32, 33), 5, 5, True), ((35, 32), 5, 5, True)], True)
        _path(self, "shoulders", (16, 33), [((24, 27), 8, 6, True), ((32, 33), 8, 6, True)])
        self.relate("connect", "shoulders-1", "head-l-1")
        self.relate("connect", "shoulders-1", "head-l-2")
        self.relate("connect", "shoulders-2", "head-r-4")
        self.relate("connect", "shoulders-2", "head-r-5")
        locks = {"l-out": ((8, 37), (6, 42), "head-l-3", "head-l-4"), "l-in": ((18, 37), (20, 42), "head-l-2", "head-l-3"),
                 "r-out": ((40, 37), (42, 42), "head-r-1", "head-r-2"), "r-in": ((30, 37), (28, 42), "head-r-3", "head-r-4")}
        for n, (p, q, a, b) in locks.items():
            self.add_line(f"lock-{n}", p, q)
            self.relate("connect", f"lock-{n}", a); self.relate("connect", f"lock-{n}", b)
