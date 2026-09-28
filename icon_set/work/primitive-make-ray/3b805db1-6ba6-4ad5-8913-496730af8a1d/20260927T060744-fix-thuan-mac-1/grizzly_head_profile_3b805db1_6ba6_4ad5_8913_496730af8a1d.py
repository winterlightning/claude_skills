from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3b805db1-6ba6-4ad5-8913-496730af8a1d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grizzly-head-profile/20260927T055730Z-thuan-mac-1/reference/grizzly head side_3b805db1-6ba6-4ad5-8913-496730af8a1d.svg'
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
    icon_id = 'grizzly-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('bear', 'grizzly', 'head', 'profile', 'roar', 'snout', 'wildlife', 'animal')

    def build(self) -> None:
        # grizzly head in profile facing right, open at the neck
        _path(self, "head", (6, 26), [
            (10, 14),                                     # back of the neck up to the ear
            ((18, 8), 5, 5, True),                        # round ear, r5 about (14,11), top y=6
            (26, 10),                                     # forehead
            (39, 16),                                     # long sloping snout
            ((39, 22), 3, 3, True, True),                 # rounded nose (x=42)
            (32, 24),                                     # under the snout to the mouth corner
            ('c', (38, 26), (38, 34), (32, 34)),          # jaw
            ('c', (26, 36), (22, 40), (20, 42)),          # throat running off the bottom
        ])
        self.add_dot("eye", (25, 19))
