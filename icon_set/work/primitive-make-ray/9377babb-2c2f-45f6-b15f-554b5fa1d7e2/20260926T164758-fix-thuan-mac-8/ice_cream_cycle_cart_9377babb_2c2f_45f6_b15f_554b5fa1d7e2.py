from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9377babb-2c2f-45f6-b15f-554b5fa1d7e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ice-cream-cycle-cart/20260926T164653Z-thuan-mac/reference/ice cream truck_9377babb-2c2f-45f6-b15f-554b5fa1d7e2.svg'
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
    icon_id = 'ice-cream-cycle-cart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('ice', 'cream', 'cycle', 'cart')

    def build(self) -> None:
        # Plan: ice-cream tricycle cart as in the reference, on SQUARE (6..42):
        # a big umbrella canopy (half-ellipse rx13 ry8 over a straight rim,
        # x 16..42, top y=6) with a centre rib, on a pole that continues down to
        # the cart box (x 20..42, y 22..30); the box floor continues forward as
        # the frame to the front wheel; two r6 ring wheels hang from the frame at
        # their top points (12,30)/(34,30); a front stem rises from the front
        # wheel and bends back into a short handle (y=20).
        _path(self, 'canopy', (16, 14), [((29, 6), 13, 8, True), ((42, 14), 13, 8, True)])
        _path(self, 'canopy-rim', (42, 14), [(29, 14), (16, 14)])
        self.add_line('rib', (29, 6), (29, 14))
        self.add_line('pole', (29, 14), (29, 22))
        for a, b in (('canopy', 'canopy-rim'), ('canopy', 'rib'), ('canopy-rim', 'rib'), ('canopy-rim', 'pole'),
                     ('rib', 'pole')):
            self.relate('connect', a, b)
        _path(self, 'box', (20, 30), [(20, 22), (29, 22), (42, 22), (42, 30), (34, 30), (20, 30), (12, 30)])
        self.relate('connect', 'pole', 'box')
        _circle(self, 'front-wheel', 12, 36, 6)
        _circle(self, 'rear-wheel', 34, 36, 6)
        self.relate('connect', 'box', 'front-wheel')
        self.relate('connect', 'box', 'rear-wheel')
        _path(self, 'handle', (12, 30), [(10, 20), (6, 20)])
        self.relate('connect', 'box', 'handle')
        self.relate('connect', 'front-wheel', 'handle')
