from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fbebeb22-f783-4b7a-80ca-ee1c22adc9bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__equipment-cement-cart/20260926T162509Z-thuan-mac/reference/equipment cement cart_fbebeb22-f783-4b7a-80ca-ee1c22adc9bc.svg'
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
    icon_id = 'equipment-cement-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('solo-ai-full-set', 'equipment-cement-cart')

    def build(self) -> None:
        # Plan: wheelbarrow of cement facing left on HRECT_L (x 4..44, y 8..40),
        # traced from the reference: a straight tray rim at y=22, a left wall
        # slanting down to the r5 wheel (meets it at the 3-4-5 point (11,31)), a
        # short floor from the wheel's east point, a 45-degree right wall up to the
        # rim corner (38,22), a 45-degree leg down to (38,40) with a vertical post
        # back to the corner, a 45-degree handle, and a cement heap mirrored about
        # x=21: r5 side bumps on short uprights and a taller r10 centre dome.
        _path(self, 'wheel', (14, 30), [
            ((19, 35), 5, 5, True), ((14, 40), 5, 5, True), ((9, 35), 5, 5, True),
            ((11, 31), 5, 5, True), ((14, 30), 5, 5, True),
        ], closed=True)
        _path(self, 'tray', (11, 31), [(4, 22), (38, 22), (29, 31), (25, 35), (19, 35)])
        _path(self, 'leg', (29, 31), [(38, 40), (38, 22)])
        self.add_line('handle', (38, 22), (44, 16))
        _path(self, 'heap', (4, 22), [
            (4, 15), ((13, 12), 5, 5, True), ((29, 12), 10, 10, True), ((38, 15), 5, 5, True), (38, 22),
        ])
        for a, b in (('tray', 'wheel'), ('tray', 'leg'), ('tray', 'handle'), ('leg', 'handle'),
                     ('tray', 'heap'), ('heap', 'leg'), ('heap', 'handle')):
            self.relate('connect', a, b)
