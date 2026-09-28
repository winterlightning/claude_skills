from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '90ffd8be-8c2b-43c1-9cda-658b2b74c820'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphones-90ffd8be/20260926T162509Z-thuan-mac/reference/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.svg'
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
    icon_id = 'headphones-90ffd8be'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('solo-ai-full-set', 'headphones-90ffd8be')

    def build(self) -> None:
        # Plan: headphones as in the reference, on HRECT_L (x 4..44, y 8..40),
        # mirrored about x=24. The headband is an r12 semicircle (apex (24,8))
        # on straight legs x=12 and x=36 that run down to y=40. Each ear cup is
        # a half-ellipse (rx8, ry6) bulging outward from the lower leg
        # (y 28..40), reaching the keyshape sides at (4,34) and (44,34).
        _path(self, 'band', (12, 40), [
            (12, 28), (12, 20), ((24, 8), 12, 12, True), ((36, 20), 12, 12, True), (36, 28), (36, 40),
        ])
        _path(self, 'cup-left', (12, 28), [((4, 34), 8, 6, False), ((12, 40), 8, 6, False)])
        _path(self, 'cup-right', (36, 28), [((44, 34), 8, 6, True), ((36, 40), 8, 6, True)])
        self.relate('connect', 'band', 'cup-left')
        self.relate('connect', 'band', 'cup-right')
