from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '18f96efa-93ca-4c4e-9556-e131c14f8073'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plane-1/20260927T084830Z-thuan-mac-1/reference/plane 1_18f96efa-93ca-4c4e-9556-e131c14f8073.svg'
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
    icon_id = 'plane-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'travel'
    categories = ('travel', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'plane-1')

    def build(self) -> None:
        # side-view jet climbing right (reference): one outline with the tail fin bump, notch,
        # long swept wing with a flat tip, straight belly and a broad round nose (before tapered
        # the fuselage into a pinched, cusped nose)
        _path(self, "plane", (4, 33), [
            (9, 26), (17, 30), (23, 22), (9, 17), (16, 10), (29, 15), (36, 11),
            ('c', (38.6, 9.5), (39.5, 8), (41, 8)),
            ('c', (42.8, 8), (44, 9.8), (44, 12)),
            ('c', (44, 15), (43.5, 18.7), (42, 20)),
            (18, 40), (4, 33)], True)
