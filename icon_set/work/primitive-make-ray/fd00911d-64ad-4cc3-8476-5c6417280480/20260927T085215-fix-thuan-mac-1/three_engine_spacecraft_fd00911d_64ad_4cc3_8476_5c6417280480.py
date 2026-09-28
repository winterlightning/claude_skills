from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fd00911d-64ad-4cc3-8476-5c6417280480'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-engine-spacecraft/20260927T084830Z-thuan-mac-1/reference/fiction ship_fd00911d-64ad-4cc3-8476-5c6417280480.svg'
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
    icon_id = 'three-engine-spacecraft'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('spacecraft', 'engine', 'cabin', 'rocket', 'nozzle', 'space')

    def build(self) -> None:
        # spacecraft (reference): domed central body with a porthole, a rounded side pod on each
        # side, three engine nozzles under the base (side ones under the pods). Before had no side
        # pods and read as a UFO with feet.
        _path(self, "hull", (12, 32), [(12, 24), (12, 20), ((24, 8), 12, 12, True), ((36, 20), 12, 12, True),
                                       (36, 24), (36, 32)])
        for s, tag in ((1, "left"), (-1, "right")):
            X = lambda x: 24 + s * (x - 24)
            _path(self, f"pod-{tag}", (X(12), 24), [(X(8), 24), ((X(4), 28), 4, 4, s < 0), (X(4), 32)])
            self.relate("connect", f"pod-{tag}", "hull")
        xs = (4, 12, 20, 28, 36, 44)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"base-{n}", (a, 32), (b, 32))
            if n:
                self.relate("connect", f"base-{n - 1}", f"base-{n}")
        self.relate("connect", "pod-left", "base-0"); self.relate("connect", "pod-right", "base-4")
        for t in ("base-0", "base-1", "base-3", "base-4"):
            self.relate("connect", "hull", t)
        for n, x in enumerate((4, 20, 36)):
            self.add_polyline(f"engine-{n}", (x, 32), (x, 40), (x + 8, 40), (x + 8, 32))
            self.relate("connect", f"engine-{n}", f"base-{2 * n}")
            if n == 1:
                self.relate("connect", f"engine-{n}", "base-1"); self.relate("connect", f"engine-{n}", "base-3")
        self.relate("connect", "engine-0", "pod-left"); self.relate("connect", "engine-2", "pod-right")
        self.relate("connect", "engine-0", "base-1"); self.relate("connect", "engine-2", "base-3")
        self.relate("connect", "engine-0", "hull"); self.relate("connect", "engine-2", "hull")
        _circle(self, "porthole", 24, 20, 3)
