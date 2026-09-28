from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b2c77d3-0c2d-57e2-9129-cc5e7279aa93'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-dead-fish-with-crossed-eye/20260927T091421Z-thuan-mac-1/reference/pollution fish_6b2c77d3-0c2d-57e2-9129-cc5e7279aa93.svg'
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
    icon_id = 'diagonal-dead-fish-with-crossed-eye'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('fish', 'dead', 'eye', 'tail', 'fins', 'pollution', 'water', 'ecology')

    def build(self) -> None:
        # Fish on the 45-degree axis x + y = 48, mirror-symmetric about it: (x, y) -> (48 - y, 48 - x).
        # Pointed nose on the SQUARE corner (42,6) (nose control level with it, so the nose knot is the
        # exact top/right extreme). Each flank is two tangent-continuous cubics meeting at a flank knot.
        import math
        m = lambda p: (48 - p[1], 48 - p[0])
        nose, root, joint = (42, 6), (14, 13), (16, 32)
        dx, dy = -2 / math.sqrt(13), 3 / math.sqrt(13)
        c1, c2 = (24, 6), (root[0] - 8 * dx, root[1] - 8 * dy)
        c3, c4 = (root[0] + 6 * dx, root[1] + 6 * dy), (12, 26)
        _path(self, "body", nose, [('c', c1, c2, root), ('c', c3, c4, joint),
                                   ('c', m(c4), m(c3), m(root)), ('c', m(c2), m(c1), nose)], True)
        # Forked tail: closed triangle hung from the tail joint.
        _path(self, "tail", joint, [(6, 34), (14, 42), joint], True)
        self.relate("connect", "body", "tail")
        e = (27, 21)
        self.add_line("eye-a", (e[0] - 4, e[1] - 4), (e[0] + 4, e[1] + 4))
        self.add_line("eye-b", (e[0] - 4, e[1] + 4), (e[0] + 4, e[1] - 4))
        self.relate("connect", "eye-a", "eye-b")
