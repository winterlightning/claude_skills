from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '731770b0-068a-4e6d-8736-2a503b462801'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__falcon-head-facing-left/20260926T152555Z-thuan-mac-2/reference/falcon_731770b0-068a-4e6d-8736-2a503b462801.svg'
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
    icon_id = 'falcon-head-facing-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('falcon', 'head', 'facing', 'left')

    def build(self) -> None:
        # Plan: raptor head in profile facing left on SQUARE (6..42).
        # Head outline: forehead F -> crown (27,6) -> back of neck down to (42,38),
        # then the shoulder curls back left to the bottom edge. Hooked beak: upper
        # mandible F -> hook tip (6,26) (leftmost), underside back along the gape
        # line y=22 to the gape corner G; the face line G -> F separates beak from
        # head. The throat drops from G in an S-curve to the bottom edge.
        F, G, TIP = (16, 12), (22, 22), (6, 26)
        _path(self, 'head', (42, 38), [
            ('c', (40, 36), (37, 35), (34, 35)),
            ('c', (28, 35), (23, 38), (21, 42)),
        ])
        _path(self, 'crown', F, [
            ('c', (18, 7.5), (22, 6), (27, 6)),
            ('c', (32, 6), (36, 9), (37, 13)),
            (42, 38),
        ])
        _path(self, 'beak', F, [
            ('c', (10, 13), (6, 19), TIP),
            ('c', (7, 23), (9, 22), (12, 22)),
            G,
            F,
        ], closed=True)
        self.add_bezier('throat', G, ((23, 30), (14, 33), (12, 42)))
        self.add_dot('eye', (29, 16))
        self.relate('connect', 'crown', 'head')
        self.relate('connect', 'crown', 'beak')
        self.relate('connect', 'beak', 'throat')
