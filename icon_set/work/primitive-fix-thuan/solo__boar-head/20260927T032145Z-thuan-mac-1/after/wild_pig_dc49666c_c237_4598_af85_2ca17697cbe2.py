from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dc49666c-c237-4598-af85-2ca17697cbe2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boar-head/20260927T032145Z-thuan-mac-1/reference/wild pig_dc49666c-c237-4598-af85-2ca17697cbe2.svg'
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
    icon_id = 'boar-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('boar', 'pig', 'head', 'ears', 'silhouette', 'face', 'wild', 'animal')

    def build(self) -> None:
        # wild-pig head silhouette: tall peaked crest between two curled ears, round jowls
        _path(self, "head", (24, 6), [
            (31, 12),
            ('c', (35, 7), (42, 7), (42, 12)),
            ('c', (42, 15), (40, 17), (37, 19)),
            ('c', (39, 22), (40, 25), (40, 29)),
            ('c', (40, 37), (33, 42), (24, 42)),
            ('c', (15, 42), (8, 37), (8, 29)),
            ('c', (8, 25), (9, 22), (11, 19)),
            ('c', (8, 17), (6, 15), (6, 12)),
            ('c', (6, 7), (13, 7), (17, 12)),
            (24, 6),
        ], closed=True)
        self.add_dot("left-eye", (18, 24))
        self.add_dot("right-eye", (30, 24))
        self.add_dot("left-nostril", (20, 33))
        self.add_dot("right-nostril", (28, 33))
