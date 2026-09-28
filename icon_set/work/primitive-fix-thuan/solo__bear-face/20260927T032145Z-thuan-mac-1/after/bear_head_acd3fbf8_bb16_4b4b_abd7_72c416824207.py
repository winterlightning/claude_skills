from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'acd3fbf8-bb16-4b4b-abd7-72c416824207'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bear-face/20260927T032145Z-thuan-mac-1/reference/bear head_acd3fbf8-bb16-4b4b-abd7-72c416824207.svg'
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
    icon_id = 'bear-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('bear', 'face', 'head', 'cute', 'animal', 'teddy', 'wildlife', 'round')

    def build(self) -> None:
        # head r17 about (24,27); ears r5 about (12,15)/(36,15) meet it at (9,19),(16,12) and mirror
        _path(self, "head", (16, 12), [
            ((32, 12), 17, 17, True),
            ((39, 19), 5, 5, True, True),
            ((9, 19), 17, 17, True, True),
            ((16, 12), 5, 5, True, True),
        ], closed=True)
        self.add_dot("left-eye", (18, 27))
        self.add_dot("right-eye", (30, 27))
