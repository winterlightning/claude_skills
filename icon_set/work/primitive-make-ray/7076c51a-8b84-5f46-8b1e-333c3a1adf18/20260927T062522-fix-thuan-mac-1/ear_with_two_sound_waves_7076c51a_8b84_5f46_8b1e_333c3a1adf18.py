from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7076c51a-8b84-5f46-8b1e-333c3a1adf18'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ear-with-two-sound-waves/20260927T061820Z-thuan-mac-1/reference/earpod listen_7076c51a-8b84-5f46-8b1e-333c3a1adf18.svg'
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
    icon_id = 'ear-with-two-sound-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'listening', 'audio', 'wave', 'acoustic', 'anatomy')

    def build(self) -> None:
        # Lucide `ear` construction on the left: open helix = semicircle over the top, cubic down the
        # back into an r4 lobe; antihelix = inner hook. Two sound arcs radiate to the right.
        _path(self, "helix", (4, 19), [((26, 19), 11, 11, True), ('c', (26, 29), (20, 29), (20, 36)),
                                        ((12, 36), 4, 4, True)])
        _path(self, "antihelix", (16, 17), [((13, 20), 3, 3, False), (13, 27)])
        self.add_arc("wave-inner", (34, 20), (34, 30), radius_x=13, radius_y=13, sweep=True)
        self.add_arc("wave-outer", (39, 9), (39, 39), radius_x=25, radius_y=25, sweep=True)
