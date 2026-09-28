from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2f08daf6-071b-5ac7-9717-2239ffbb2925'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__canoe/20260926T182452Z-thuan-mac-1/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg'
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
    icon_id = 'canoe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('canoe', 'outdoors', 'solo-ai-next100')

    def build(self) -> None:
        # Side-view canoe: sagging gunwale between two raised tips. Each end is
        # an r10 upper bow arc (3-4-5 tip) running tangent into a flat rx10/ry5
        # lower arc, so the hull stays low and flat-bottomed like the reference.
        _path(self, 'hull', (8, 16), [('c', (16, 22), (32, 22), (40, 16)),
                                      ((44, 24), 10, 10, True),
                                      ((34, 29), 10, 5, True),
                                      (14, 29),
                                      ((4, 24), 10, 5, True),
                                      ((8, 16), 10, 10, True)], True)
