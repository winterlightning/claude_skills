from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'de769bf2-a3ba-4ba6-9576-1ee1987a08e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-boy-in-round-cap/20260927T101542Z-thuan-mac-1/reference/chinese kid boy_de769bf2-a3ba-4ba6-9576-1ee1987a08e0.svg'
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
    icon_id = 'smiling-boy-in-round-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('smiling', 'boy', 'in', 'round', 'cap')

    def build(self) -> None:
        # Plan: front head, mirrored about x=24. Round cap = dome rx14 ry9 over a
        # straight brim at y=15 with a centre seam; ears are r4 half-rounds just below
        # the brim; the face is the lower half-ellipse rx14 ry19 down to the chin.
        # Face: dot eyes 8 below the brim, a shallow smile.
        _path(self, "head", (10, 15), [((38, 15), 14, 9, True), ((38, 23), 4, 4, True),
                                       ((24, 42), 14, 19, True), ((10, 23), 14, 19, True),
                                       ((10, 15), 4, 4, True)], True)
        self.add_line("brim", (10, 15), (38, 15))
        self.add_line("seam", (24, 6), (24, 15))
        self.relate("connect", "brim", "head")
        self.relate("connect", "seam", "head")
        self.relate("connect", "seam", "brim")
        self.add_dot("eye-left", (20, 23))
        self.add_dot("eye-right", (28, 23))
        self.add_bezier("smile", (21, 31), ((22.5, 101 / 3), (25.5, 101 / 3), (27, 31)))
