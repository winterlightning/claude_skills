from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fd7ba626-c30a-4140-8bc3-a2f36f3e9b70'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ham-leg-with-exposed-bone/20260926T160438Z-thuan-mac-2/reference/ham_fd7ba626-c30a-4140-8bc3-a2f36f3e9b70.svg'
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
    icon_id = 'ham-leg-with-exposed-bone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('ham', 'leg', 'with', 'exposed', 'bone')

    def build(self) -> None:
        # Plan: ham leg with exposed bone on SQUARE (a drumstick on the diagonal).
        # Meat: a smooth teardrop, round end at the bottom left (leftmost x=6, bottom
        # y=42), closed across the bone base N1-N2 at the upper right. The bone is
        # an outlined shaft at 45 degrees (sides N1-K1 and N2-K2, 9.9 apart) ending
        # in a round knob: an r5 circle about (37,11) whose far side runs from K1
        # over the top (37,6) and right (42,11) points to K2. The cut face is an r3
        # ring in the round end, 9+ from the outline.
        N1, N2 = (27, 14), (34, 21)
        K1, K2 = (33, 8), (40, 15)
        _path(self, 'meat', N1, [
            ('c', (19, 11), (6, 17), (6, 28)),
            ('c', (6, 37), (12, 42), (20, 42)),
            ('c', (29, 42), (35, 35), (35, 28)),
            ('c', (35, 25), (35, 23), N2),
            N1,
        ], closed=True)
        _path(self, 'bone', N1, [
            K1, ((37, 6), 5, 5, True), ((42, 11), 5, 5, True), (K2, 5, 5, True), N2,
        ])
        _circle(self, 'cut', 19, 29, 3)
        self.relate('connect', 'meat', 'bone')
