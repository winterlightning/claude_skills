from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '955af99e-4ca7-4122-9d20-02138f6d605b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headache-profile-955af99e/20260926T162509Z-thuan-mac/reference/head pain_955af99e-4ca7-4122-9d20-02138f6d605b.svg'
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
    icon_id = 'headache-profile-955af99e'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('headache', 'profile')

    def build(self) -> None:
        # Plan: head in profile facing left with pain rising above it, on
        # VRECT_L (x 8..40, y 4..44). One open outline runs from the back of the
        # neck (34,44) up a cubic into the back of the skull, over two
        # quarter-ellipse crown arcs (back rx16 ry11, front rx12 ry8) meeting at
        # the crown top (24,18), down a straight bridge to the low pointed nose
        # (8,32) of this reference, back along the nose base, down the lip line,
        # round an r4 jaw and down the front of the neck (x=20). Two S-shaped
        # pain squiggles (x 20 and 30, y 4..10) rise 8+ above the crown, 10
        # apart. The crown is closed (the reference leaves it open) because an
        # opening wide enough for 8-unit clearance cut the skull down to two
        # brackets.
        _path(self, 'head', (34, 44), [
            (34, 38), ('c', (34, 34), (40, 33), (40, 29)), ((24, 18), 16, 11, False), ((12, 26), 12, 8, False),
            (8, 32), (13, 32), (13, 35), ((17, 39), 4, 4, False), (20, 39), (20, 44),
        ])
        self.add_bezier('pain-left', (20, 4), ((17, 6), (23, 8), (20, 10)))
        self.add_bezier('pain-right', (30, 4), ((27, 6), (33, 8), (30, 10)))
