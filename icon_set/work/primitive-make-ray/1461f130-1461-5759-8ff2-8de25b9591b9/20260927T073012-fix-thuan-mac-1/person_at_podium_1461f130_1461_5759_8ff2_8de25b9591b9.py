from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1461f130-1461-5759-8ff2-8de25b9591b9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-at-podium/20260927T072841Z-thuan-mac-1/reference/neutral podium_1461f130-1461-5759-8ff2-8de25b9591b9.svg'
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
    icon_id = 'person-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('person', 'podium', 'lectern', 'speaker', 'presentation', 'speech', 'talk', 'conference')

    def build(self) -> None:
        # speaker behind a podium (human ref user.svg): r4 head, shoulder arch 8 below it rising from the
        # podium top; podium narrowing to its base
        _circle(self, "head", 24, 10, 4)
        self.add_arc("shoulders", (16, 29), (32, 29), radius_x=8, radius_y=7)
        self.mark_human_figure("person", head="head", torso="shoulders", torso_junction="start")
        xs = (6, 10, 16, 32, 38, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"top-{n}", (a, 29), (b, 29))
        self.add_polyline("podium", (10, 29), (14, 42), (34, 42), (38, 29))
        for n in range(4):
            self.relate("connect", f"top-{n}", f"top-{n + 1}")
        for t in ("top-1", "top-2", "top-3"):
            self.relate("connect", "shoulders", t)
        for t in ("top-0", "top-1", "top-3", "top-4"):
            self.relate("connect", "podium", t)
