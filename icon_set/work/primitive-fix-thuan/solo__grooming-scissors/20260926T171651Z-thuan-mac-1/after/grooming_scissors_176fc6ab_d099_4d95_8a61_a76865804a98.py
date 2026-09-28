from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '176fc6ab-d099-4d95-8a61-a76865804a98'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__grooming-scissors/20260926T171651Z-thuan-mac-1/reference/grooming scissor_176fc6ab-d099-4d95-8a61-a76865804a98.svg'
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
    icon_id = 'grooming-scissors'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('scissors', 'grooming', 'cut', 'trim', 'shears', 'pet', 'salon')

    def build(self) -> None:
        # Plan: the reference's open grooming scissors on SQUARE (6..42),
        # mirrored about the 45-degree axis through the pivot P (a point
        # offset (dx, dy) maps to (-dy, -dx)): two r5 finger rings (left and
        # bottom, four cardinal quarter arcs each) whose shanks meet at P,
        # and two broad leaf blades opening up and to the right. Each blade
        # is a closed lens: a straight cutting edge from P to its tip and a
        # curved back (one cubic) returning to P, bulging outward.
        P = (26, 22)
        _circle(self, 'ring-left', 11, 23, 5)
        _circle(self, 'ring-bottom', 25, 37, 5)
        self.add_line('shank-left', (16, 23), P)
        self.add_line('shank-bottom', (25, 32), P)
        _path(self, 'blade-up', P, [(32, 6), ('c', (22, 6), (18, 13), P)], True)
        _path(self, 'blade-right', P, [(42, 16), ('c', (42, 26), (35, 30), P)], True)
        for a, b in (('ring-left', 'shank-left'), ('ring-bottom', 'shank-bottom'), ('shank-left', 'shank-bottom'),
                     ('shank-left', 'blade-up'), ('shank-left', 'blade-right'), ('shank-bottom', 'blade-up'),
                     ('shank-bottom', 'blade-right'), ('blade-up', 'blade-right')):
            self.relate('connect', a, b)
