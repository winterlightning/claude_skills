from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '13d59ce5-d5e2-4166-a18d-364a3de6b8e4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iwiw-logo/20260927T070909Z-thuan-mac-1/reference/iwiw logo_13d59ce5-d5e2-4166-a18d-364a3de6b8e4.svg'
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
    icon_id = 'iwiw-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('iwiw', 'social', 'letter-c', 'logo', 'brand', 'network', 'hungarian')

    def build(self) -> None:
        # outlined hexagonal C (8-thick band, chamfered corners, round ends) and an outlined pill
        _path(self, "c", (22, 6), [
            (14, 6), (6, 14), (6, 34), (14, 42), (22, 42),
            ((22, 34), 4, 4, False),
            (18, 34), (14, 30), (14, 18), (18, 14), (22, 14),
            ((22, 6), 4, 4, False),
        ], closed=True)
        _path(self, "pill", (34, 14), [((42, 14), 4, 4, True), (42, 34), ((34, 34), 4, 4, True), (34, 14)], closed=True)
