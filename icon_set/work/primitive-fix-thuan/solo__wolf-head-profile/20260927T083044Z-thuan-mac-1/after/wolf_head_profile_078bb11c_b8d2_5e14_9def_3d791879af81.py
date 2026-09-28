from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '078bb11c-b8d2-5e14-9def-3d791879af81'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wolf-head-profile/20260927T083044Z-thuan-mac-1/reference/wolf_078bb11c-b8d2-5e14-9def-3d791879af81.svg'
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
    icon_id = 'wolf-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'ears', 'snout', 'canine', 'dog', 'wild')

    def build(self) -> None:
        # Plan: wolf head in right-facing profile as in the reference - one open outline: curved
        # back of the neck rising to a broad pointed ear (tip y6), forehead dropping through a
        # stop into a long snout ending at the nose (x42), rounded muzzle underside, jaw and
        # throat curving down to the front of the neck (y42); an eye dot behind the stop.
        _path(self, "head", (6, 38), [('c', (7, 29), (10, 22), (15, 17)), (19, 6), (26, 16),
                                      ('c', (28, 19), (30, 23), (33, 24)), (42, 30),
                                      ('c', (41, 33), (38, 34), (34, 34)), (30, 34),
                                      ('c', (27, 35), (26, 38), (26, 42))])
        self.add_dot("eye", (22, 25))
