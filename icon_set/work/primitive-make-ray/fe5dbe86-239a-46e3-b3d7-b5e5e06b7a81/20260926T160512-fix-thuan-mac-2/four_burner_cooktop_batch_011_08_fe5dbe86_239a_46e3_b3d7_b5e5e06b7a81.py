from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__four-burner-cooktop-batch-011-08/20260926T160438Z-thuan-mac-2/reference/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg'
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
    icon_id = 'four-burner-cooktop-batch-011-08'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('cooktop', 'stove', 'burners', 'kitchen', 'cooking', 'appliance')

    def build(self) -> None:
        # Plan: four-burner cooktop on SQUARE, mirrored about both axes. The frame
        # is four standalone edges joined at the corners (round caps paint round
        # corners), so each burner can sit exactly 8 from it. Four outlined burner
        # rings (r3) on a 14 grid, 8 apart and 8 from the frame.
        for name, a, b in (('edge-top', (6, 6), (42, 6)), ('edge-right', (42, 6), (42, 42)),
                           ('edge-bottom', (42, 42), (6, 42)), ('edge-left', (6, 42), (6, 6))):
            self.add_line(name, a, b)
        self.relate('connect', 'edge-top', 'edge-right')
        self.relate('connect', 'edge-right', 'edge-bottom')
        self.relate('connect', 'edge-bottom', 'edge-left')
        self.relate('connect', 'edge-left', 'edge-top')
        for name, cx, cy in (('burner-tl', 17, 17), ('burner-tr', 31, 17), ('burner-bl', 17, 31), ('burner-br', 31, 31)):
            _circle(self, name, cx, cy, 3)
