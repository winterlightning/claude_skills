from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a6e0c75c-ba38-5637-ab79-106bd4d8480d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-rocket-round-window/20260927T084830Z-thuan-mac-1/reference/exploration apollo saturn v_a6e0c75c-ba38-5637-ab79-106bd4d8480d.svg'
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
    icon_id = 'upright-rocket-round-window'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('rocket', 'space', 'window', 'fin', 'nozzle', 'launch')

    def build(self) -> None:
        # tall upright rocket (reference): pointed ogive nose over a band, straight narrow body with
        # a round window, swept side fins standing on the base line, small trapezoid nozzle.
        # Before drew a pentagon (house) outline with a ring; the narrow body is restored here, so
        # the window becomes a solid porthole dot to keep 8 from both walls.
        self.add_bezier("nose-left", (24, 4), ((20, 6), (16.6, 9.5), (16, 13)))
        self.add_bezier("nose-right", (24, 4), ((28, 6), (31.4, 9.5), (32, 13)))
        self.add_line("band", (16, 13), (32, 13))
        for s, tag in ((1, "left"), (-1, "right")):
            X = lambda x: 24 + s * (x - 24)
            self.add_line(f"wall-{tag}-top", (X(16), 13), (X(16), 25))
            self.add_line(f"wall-{tag}-low", (X(16), 25), (X(16), 36))
            self.add_polyline(f"fin-{tag}", (X(16), 25), (X(8), 33), (X(8), 36))
            self.relate("connect", f"nose-{tag}", "band")
            self.relate("connect", f"nose-{tag}", f"wall-{tag}-top")
            self.relate("connect", "band", f"wall-{tag}-top")
            self.relate("connect", f"wall-{tag}-top", f"wall-{tag}-low")
            self.relate("connect", f"wall-{tag}-top", f"fin-{tag}")
            self.relate("connect", f"wall-{tag}-low", f"fin-{tag}")
        self.relate("connect", "nose-left", "nose-right")
        xs = (8, 16, 20, 28, 32, 40)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"base-{n}", (a, 36), (b, 36))
            if n:
                self.relate("connect", f"base-{n - 1}", f"base-{n}")
        self.relate("connect", "fin-left", "base-0"); self.relate("connect", "fin-right", "base-4")
        self.relate("connect", "wall-left-low", "base-0"); self.relate("connect", "wall-left-low", "base-1")
        self.relate("connect", "wall-right-low", "base-3"); self.relate("connect", "wall-right-low", "base-4")
        self.add_polyline("nozzle", (20, 36), (19, 44), (29, 44), (28, 36))
        for n in (1, 2, 3):
            self.relate("connect", "nozzle", f"base-{n}")
        self.add_dot("window", (24, 22))
