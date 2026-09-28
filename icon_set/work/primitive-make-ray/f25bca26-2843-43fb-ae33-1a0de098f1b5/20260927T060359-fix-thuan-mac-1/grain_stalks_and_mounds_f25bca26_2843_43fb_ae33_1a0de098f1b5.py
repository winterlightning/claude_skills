from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f25bca26-2843-43fb-ae33-1a0de098f1b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grain-stalks-and-mounds/20260927T055657Z-thuan-mac-1/reference/reishit katzir feast of firstfruits_f25bca26-2843-43fb-ae33-1a0de098f1b5.svg'
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
    icon_id = 'grain-stalks-and-mounds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('firstfruits', 'grain', 'barley', 'harvest', 'stalks', 'feast', 'agriculture', 'offering')

    def build(self) -> None:
        # upright grain stalk: stem rising past two V branch pairs (vertices 12 apart for 45-degree arms)
        self.add_line("stem", (36, 6), (36, 30))
        for n, vy in enumerate((14, 26)):
            self.add_polyline(f"ear-{n}", (30, vy - 6), (36, vy), (42, vy - 6))
            self.relate("connect", "stem", f"ear-{n}")
        # tilted stalk: stem at 45 degrees ending in a branch pair (one horizontal, one vertical arm)
        self.add_polyline("tilted", (24, 26), (17, 19), (9, 19))
        self.add_line("tilted-arm", (17, 19), (17, 11))
        self.relate("connect", "tilted", "tilted-arm")
        # two mounds on the ground line; the ground is split at the mound feet
        xs = (6, 22, 34, 42)
        for n, (a, b) in enumerate(zip(xs, xs[1:])):
            self.add_line(f"ground-{n}", (a, 42), (b, 42))
        self.relate("connect", "ground-0", "ground-1"); self.relate("connect", "ground-1", "ground-2")
        self.add_arc("mound-big", (6, 42), (22, 42), radius_x=8)
        self.add_arc("mound-small", (22, 42), (34, 42), radius_x=6)
        for g, m in (("ground-0", "mound-big"), ("ground-1", "mound-big"), ("ground-1", "mound-small"),
                     ("ground-2", "mound-small"), ("mound-big", "mound-small")):
            self.relate("connect", g, m)
