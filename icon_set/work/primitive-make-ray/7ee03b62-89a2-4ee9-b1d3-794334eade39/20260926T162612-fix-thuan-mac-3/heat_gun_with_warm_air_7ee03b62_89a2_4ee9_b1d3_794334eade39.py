from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7ee03b62-89a2-4ee9-b1d3-794334eade39'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heat-gun-with-warm-air/20260926T162509Z-thuan-mac/reference/heat gun_7ee03b62-89a2-4ee9-b1d3-794334eade39.svg'
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
    icon_id = 'heat-gun-with-warm-air'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('heat', 'gun', 'with', 'warm', 'air')

    def build(self) -> None:
        # Plan: heat gun pointing left and blowing warm air, as in the reference,
        # on HRECT_L (x 4..44, y 8..40). Body: a box x 26..44, y 8..20 with r4
        # top-rear and r2 bottom-rear corners. Nozzle: a square-ended tube
        # x 18..26, y 10..18 on the body's front wall. Grip: slants down and
        # back from the body floor (front edge (33,20)->(35,40), rear edge
        # (42,20)->(44,40)) to a flat base at y=40. Warm air: two tilde waves
        # (x 4..10, y 9 and 19) in front of the nozzle mouth, 8 clear of it.
        # The reference's small trigger loop is left out: at this size its
        # 8x8 pocket crowded the grip into a solid block.
        _path(self, 'body', (26, 8), [
            (40, 8), ((44, 12), 4, 4, True), (44, 18), ((42, 20), 2, 2, True), (33, 20), (26, 20),
            (26, 18), (26, 10), (26, 8),
        ], closed=True)
        _path(self, 'nozzle', (26, 10), [(18, 10), (18, 18), (26, 18)])
        _path(self, 'grip', (33, 20), [(35, 40), (44, 40), (42, 20)])
        self.relate('connect', 'body', 'nozzle')
        self.relate('connect', 'body', 'grip')
        self.add_bezier('air-top', (4, 9), ((6, 6), (8, 12), (10, 9)))
        self.add_bezier('air-bottom', (4, 19), ((6, 16), (8, 22), (10, 19)))
