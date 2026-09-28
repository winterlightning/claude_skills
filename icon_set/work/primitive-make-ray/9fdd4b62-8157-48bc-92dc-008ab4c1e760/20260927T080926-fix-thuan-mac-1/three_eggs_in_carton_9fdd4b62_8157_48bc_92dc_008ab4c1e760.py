from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9fdd4b62-8157-48bc-92dc-008ab4c1e760'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-eggs-in-carton/20260927T080754Z-thuan-mac-1/reference/eggs_9fdd4b62-8157-48bc-92dc-008ab4c1e760.svg'
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
    icon_id = 'three-eggs-in-carton'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('egg', 'carton', 'packaging', 'breakfast', 'poultry', 'food', 'groceries')

    def build(self) -> None:
        # three egg domes above a carton rim line; one carton body whose bottom bulges into three cups
        xs = (6, 18, 30, 42)
        _path(self, "rim", (4, 24), [(6, 24), (18, 24), (30, 24), (42, 24), (44, 24)])
        _path(self, "carton", (6, 24), [(6, 34), ((18, 34), 6, 6, False), ((30, 34), 6, 6, False), ((42, 34), 6, 6, False), (42, 24)])
        for i in range(3):
            l, r = xs[i], xs[i + 1]; m = (l + r) // 2
            _path(self, f"egg-{i + 1}", (l, 24), [('c', (l, 14), (m - 4, 8), (m, 8)), ('c', (m + 4, 8), (r, 14), (r, 24))])
        for a, b in (("rim-1", "carton-1"), ("rim-2", "carton-1"), ("rim-4", "carton-5"), ("rim-5", "carton-5"),
                     ("egg-1-1", "rim-1"), ("egg-1-1", "rim-2"), ("egg-1-2", "rim-2"), ("egg-1-2", "rim-3"),
                     ("egg-2-1", "rim-2"), ("egg-2-1", "rim-3"), ("egg-2-2", "rim-3"), ("egg-2-2", "rim-4"),
                     ("egg-3-1", "rim-3"), ("egg-3-1", "rim-4"), ("egg-3-2", "rim-4"), ("egg-3-2", "rim-5"),
                     ("egg-1-2", "egg-2-1"), ("egg-2-2", "egg-3-1"), ("egg-1-1", "carton-1"), ("egg-3-2", "carton-5")):
            self.relate("connect", a, b)
