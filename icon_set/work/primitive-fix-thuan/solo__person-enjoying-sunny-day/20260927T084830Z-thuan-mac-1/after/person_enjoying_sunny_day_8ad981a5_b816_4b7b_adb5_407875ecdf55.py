from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8ad981a5-b816-4b7b-adb5-407875ecdf55'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-enjoying-sunny-day/20260927T084830Z-thuan-mac-1/reference/virtual environment day_8ad981a5-b816-4b7b-adb5-407875ecdf55.svg'
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
    icon_id = 'person-enjoying-sunny-day'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('person', 'sun', 'cloud', 'day', 'weather', 'outdoors', 'environment', 'relax')

    def build(self) -> None:
        # person out on a sunny day (reference): a head-and-shoulders bust on the left, the sun on
        # the right shining over the horizon line with detached rays. Before drew a stick figure
        # under a crosshair-like sun.
        _circle(self, "head", 12, 20, 4)
        self.add_arc("shoulders", (4, 38), (20, 38), radius_x=8, radius_y=5, sweep=True)
        self.add_arc("sun-left", (29, 30), (35, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_arc("sun-right", (35, 24), (41, 30), radius_x=6, radius_y=6, sweep=True)
        self.add_contour("sun", "sun-left", "sun-right")
        xs = (26, 29, 41, 44)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"horizon-{n}", (a, 30), (b, 30))
            if n:
                self.relate("connect", f"horizon-{n - 1}", f"horizon-{n}")
        for n in range(3):
            self.relate("connect", "sun", f"horizon-{n}")
        self.add_line("ray-left", (26, 18), (23, 14))
        self.add_line("ray-up", (35, 15), (35, 10))
        self.add_line("ray-right", (43, 17), (44, 15))
