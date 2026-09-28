from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47a78895-0132-42e2-8459-c80e2e317111'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airplane/20260927T084830Z-thuan-mac-1/reference/airplane_47a78895-0132-42e2-8459-c80e2e317111.svg'
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
    icon_id = 'airplane'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-refine', 'solo-ai-first50', 'airplane')

    def build(self) -> None:
        # side-view airliner climbing to the right, one outline as in the reference: slim tail
        # wedge, notch, swept wing, long straight belly, round nose; the tail tip is the r20 point
        # (before drew a top-view 45-degree plane, not the reference's side view)
        _path(self, "plane", (4, 24), [
            (13, 25), (20, 21), (13, 12), (27, 16), (35, 12),
            ('c', (37.25, 11), (41, 13), (41, 16)),
            ('c', (41, 18.5), (39.86, 20.03), (38, 21)),
            (17, 32),
            ('c', (15, 33), (12, 33), (10, 31)),
            (4, 24)], True)
