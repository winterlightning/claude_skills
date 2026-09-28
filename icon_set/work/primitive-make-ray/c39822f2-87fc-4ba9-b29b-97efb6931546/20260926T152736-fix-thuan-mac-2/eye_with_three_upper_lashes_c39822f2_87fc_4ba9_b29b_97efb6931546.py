from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c39822f2-87fc-4ba9-b29b-97efb6931546'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eye-with-three-upper-lashes/20260926T152555Z-thuan-mac-2/reference/eyelash_c39822f2-87fc-4ba9-b29b-97efb6931546.svg'
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
    icon_id = 'eye-with-three-upper-lashes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('eye', 'with', 'three', 'upper', 'lashes')

    def build(self) -> None:
        # Plan: almond eye on axis x=24; top lid = 4 smooth cubics with knots at the
        # lash roots (13,18), apex (24,14), (35,18); bottom lid = one cubic reaching y=40.
        # Iris: r4 ring centred between the lids (9 clear each side). Three lashes.
        _path(self, 'eye', (4, 28), [
            ('c', (6, 25), (10, 19.5), (13, 18)),
            ('c', (17, 16), (20, 14), (24, 14)),
            ('c', (28, 14), (31, 16), (35, 18)),
            ('c', (38, 19.5), (42, 25), (44, 28)),
            ('c', (34, 44), (14, 44), (4, 28)),
        ], closed=True)
        _circle(self, 'iris', 24, 27, 4)
        self.add_line('lash-middle', (24, 14), (24, 8))
        self.add_line('lash-left', (13, 18), (9, 10))
        self.add_line('lash-right', (35, 18), (39, 10))
        self.relate('connect', 'eye-2', 'eye-3', 'lash-middle')
        self.relate('connect', 'eye-1', 'eye-2', 'lash-left')
        self.relate('connect', 'eye-3', 'eye-4', 'lash-right')
