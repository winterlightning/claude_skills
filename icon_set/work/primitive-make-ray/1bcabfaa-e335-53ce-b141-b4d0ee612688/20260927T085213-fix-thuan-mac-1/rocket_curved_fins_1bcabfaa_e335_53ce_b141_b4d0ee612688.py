from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1bcabfaa-e335-53ce-b141-b4d0ee612688'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rocket-curved-fins/20260927T084830Z-thuan-mac-1/reference/spaceship_1bcabfaa-e335-53ce-b141-b4d0ee612688.svg'
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
    icon_id = 'rocket-curved-fins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('rocket', 'fin', 'window', 'nozzle', 'space', 'spacecraft')

    def build(self) -> None:
        # upright rocket (reference): ogive body with a nose-cone band, round porthole, curved
        # sickle fins reaching the bottom corners, trapezoid nozzle. Before had no nose band and
        # only small side bumps for fins.
        def side(s):
            X = lambda x: 24 + s * (x - 24)
            return [('c', (X(20), 6), (X(17.6), 9), (X(16), 12)), ('c', (X(13.5), 15.5), (X(12), 20), (X(12), 24)),
                    (X(12), 26), ("c", (X(12), 31), (X(14), 34), (X(16), 36))]
        _path(self, "body-left", (24, 4), side(1))
        _path(self, "body-right", (24, 4), side(-1))
        self.add_line("band", (16, 12), (32, 12))
        xs = (16, 20, 28, 32)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"base-{n}", (a, 36), (b, 36))
        self.add_polyline("nozzle", (20, 36), (19, 44), (29, 44), (28, 36))
        for s, tag in ((1, "left"), (-1, "right")):
            X = lambda x: 24 + s * (x - 24)
            self.add_bezier(f"fin-{tag}-out", (X(12), 26), ((X(8), 29), (X(8), 37), (X(8), 44)))
            self.add_bezier(f"fin-{tag}-in", (X(8), 44), ((X(10), 40), (X(13), 37), (X(16), 36)))
            self.relate("connect", f"fin-{tag}-out", f"body-{tag}")
            self.relate("connect", f"fin-{tag}-out", f"fin-{tag}-in")
            self.relate("connect", f"fin-{tag}-in", f"body-{tag}")
        _circle(self, "porthole", 24, 24, 3)
        for part in ("body-left", "body-right"):
            self.relate("connect", "band", part)
        self.relate("connect", "body-left", "body-right")
        self.relate("connect", "body-left", "base-0"); self.relate("connect", "body-right", "base-2")
        self.relate("connect", "fin-left-in", "base-0"); self.relate("connect", "fin-right-in", "base-2")
        for n in range(2):
            self.relate("connect", f"base-{n}", f"base-{n + 1}")
        self.relate("connect", "nozzle", "base-0"); self.relate("connect", "nozzle", "base-1"); self.relate("connect", "nozzle", "base-2")
