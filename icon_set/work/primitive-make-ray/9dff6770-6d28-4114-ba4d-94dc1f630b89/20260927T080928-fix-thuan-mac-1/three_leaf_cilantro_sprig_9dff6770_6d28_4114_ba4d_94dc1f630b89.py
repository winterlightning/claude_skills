from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9dff6770-6d28-4114-ba4d-94dc1f630b89'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-leaf-cilantro-sprig/20260927T080754Z-thuan-mac-1/reference/cilantro colliander_9dff6770-6d28-4114-ba4d-94dc1f630b89.svg'
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
    icon_id = 'three-leaf-cilantro-sprig'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('cilantro', 'coriander', 'herb', 'leaf', 'sprig', 'seasoning', 'plant')

    def build(self) -> None:
        # cilantro sprig: stem with a pointed three-lobed top leaf and two lobed side leaves growing from one node
        def poly(name, pts):
            return _path(self, name, pts[0], list(pts[1:]), True)
        poly("leaf-top", [(24, 18), (14, 12), (19, 12), (24, 6), (29, 12), (34, 12), (24, 18)])
        self.add_line("stem-a", (24, 18), (24, 34))
        self.add_line("stem-b", (24, 34), (24, 42))
        poly("leaf-l", [(24, 34), (10, 40), (13, 34), (6, 30), (13, 28), (14, 22), (24, 34)])
        poly("leaf-r", [(24, 34), (38, 40), (35, 34), (42, 30), (35, 28), (34, 22), (24, 34)])
        for a, b in (("stem-a", "leaf-top-1"), ("stem-a", "leaf-top-6"), ("stem-a", "stem-b"),
                     ("stem-a", "leaf-l-1"), ("stem-a", "leaf-l-6"), ("stem-b", "leaf-l-1"), ("stem-b", "leaf-l-6"),
                     ("stem-a", "leaf-r-1"), ("stem-a", "leaf-r-6"), ("stem-b", "leaf-r-1"), ("stem-b", "leaf-r-6"),
                     ("leaf-l-1", "leaf-r-1"), ("leaf-l-6", "leaf-r-6"), ("leaf-l-1", "leaf-r-6"), ("leaf-l-6", "leaf-r-1")):
            self.relate("connect", a, b)
