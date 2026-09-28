from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '39150a1e-77de-4299-ad47-aea402520e87'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plane/20260927T084830Z-thuan-mac-1/reference/plane_39150a1e-77de-4299-ad47-aea402520e87.svg'
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
    icon_id = 'plane'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'travel'
    categories = ('travel', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'plane')

    def build(self) -> None:
        # three-quarter airliner flying up-right (reference): slim fuselage from a raised tail to a
        # round nose, small far wing above, large swept near wing below with flat tips, lower tail
        # stabiliser. Before squashed the wings into stubs.
        _path(self, "plane", (4, 21), [
            (14, 22), (22, 18), (12, 13), (20, 8), (32, 14), (37, 12),
            ('c', (40, 11), (44, 11.5), (44, 14)),
            ('c', (44, 16.5), (42.5, 19.4), (41, 20)),
            (33, 23), (29, 37), (20, 40), (22, 28), (14, 32), (4, 21)], True)
