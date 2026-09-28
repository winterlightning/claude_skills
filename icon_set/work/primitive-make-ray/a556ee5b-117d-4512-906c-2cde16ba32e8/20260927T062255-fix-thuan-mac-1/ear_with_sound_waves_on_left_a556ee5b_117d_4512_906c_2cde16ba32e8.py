from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a556ee5b-117d-4512-906c-2cde16ba32e8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ear-with-sound-waves-on-left/20260927T061820Z-thuan-mac-1/reference/music ear_a556ee5b-117d-4512-906c-2cde16ba32e8.svg'
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
    icon_id = 'ear-with-sound-waves-on-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'listening', 'audio', 'wave', 'acoustic', 'anatomy')

    def build(self) -> None:
        # Lucide `ear` construction: open helix = semicircle over the top, cubic down the back into
        # an r4 lobe; antihelix = the inner hook (quarter arc + drop). Two sound arcs on the left.
        _path(self, "helix", (22, 19), [((44, 19), 11, 11, True), ('c', (44, 29), (38, 29), (38, 36)),
                                         ((30, 36), 4, 4, True)])
        _path(self, "antihelix", (34, 17), [((31, 20), 3, 3, False), (31, 27)])
        self.add_arc("wave-outer", (9, 9), (9, 39), radius_x=25, radius_y=25, sweep=False)
        self.add_arc("wave-inner", (14, 20), (14, 30), radius_x=13, radius_y=13, sweep=False)
