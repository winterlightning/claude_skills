from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '11de53db-91e8-4ba6-95b4-7e2d64d91005'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thunderstorm-cloud/20260927T080808Z-thuan-mac-1/reference/weather cloud rain thunder_11de53db-91e8-4ba6-95b4-7e2d64d91005.svg'
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
    icon_id = 'thunderstorm-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('cloud', 'thunder', 'lightning', 'rain', 'storm', 'weather')

    def build(self) -> None:
        # Plan: closed three-lobe cloud (r5 side lobes, rx13/ry8 dome, flat base y24),
        # a Lucide-style zigzag bolt hanging from a node on the base, one slanted rain dash left.
        _path(self, "cloud", (24, 24), [(37, 24), ((37, 14), 5, 5, False), ((11, 14), 13, 8, False),
                                        ((11, 24), 5, 5, False), (24, 24)], closed=True)
        _path(self, "bolt", (24, 24), [(19, 33), (29, 33), (24, 42)])
        self.relate("connect", "cloud-1", "bolt-1")
        self.relate("connect", "cloud-5", "bolt-1")
        self.add_line("rain", (10, 32), (7, 38))
