from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8a539a1a-386f-4b22-a291-e532287b8a66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flash-bolt-arrow/20260927T032039Z-thuan-mac-1/reference/light mode flash_8a539a1a-386f-4b22-a291-e532287b8a66.svg'
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
    icon_id = 'flash-bolt-arrow'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('flash', 'lightning', 'bolt', 'camera flash', 'auto flash', 'electric', 'power', 'arrow')

    def build(self) -> None:
        # Outlined lightning bolt ending in a symmetric arrowhead, built on
        # 1:2 bands (2x+y = const): upper blade 50..68 (8.05 wide), lower
        # shaft 68..88 (8.9 wide). Right step A(28,12)-B(38,12), left step
        # I(15,20)-H(24,20). Arrowhead base on x-2y=-46 with barbs of 4*sqrt5
        # each side; tip (17,44) on the shaft axis 2x+y=78.
        _path(self, 'bolt', (23, 4), [(32, 4), (28, 12), (38, 12), (26, 36), (34, 40), (17, 44),
                                      (10, 28), (18, 32), (24, 20), (15, 20), (23, 4)], True)
