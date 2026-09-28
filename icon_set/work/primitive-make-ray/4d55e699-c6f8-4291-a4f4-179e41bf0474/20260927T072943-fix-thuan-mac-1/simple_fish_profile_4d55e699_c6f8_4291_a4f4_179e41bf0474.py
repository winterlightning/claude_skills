from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4d55e699-c6f8-4291-a4f4-179e41bf0474'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__simple-fish-profile/20260927T072849Z-thuan-mac-1/reference/salmon_4d55e699-c6f8-4291-a4f4-179e41bf0474.svg'
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
    icon_id = 'simple-fish-profile'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('simple', 'fish', 'profile')

    def build(self) -> None:
        # Salmon in profile: round r12 head about (16,24), body tapering to
        # the tail joint (34,24), forked tail with a concave back edge.
        _path(self, 'body', (16, 12), [('c', (24, 12), (30, 18), (34, 24)), ('c', (37, 18), (40, 13), (44, 10)),
                                       ('c', (40, 17), (40, 31), (44, 38)), ('c', (40, 35), (37, 30), (34, 24)),
                                       ('c', (30, 30), (24, 36), (16, 36)), ((4, 24), 12, 12, True),
                                       ((16, 12), 12, 12, True)], True)
        # Gill line bulging back from the head, and a dot eye.
        self.add_arc('gill', (16, 12), (16, 36), radius_x=15, sweep=True)
        self.relate('connect', 'gill', 'body')
        self.add_dot('eye', (13, 22))
