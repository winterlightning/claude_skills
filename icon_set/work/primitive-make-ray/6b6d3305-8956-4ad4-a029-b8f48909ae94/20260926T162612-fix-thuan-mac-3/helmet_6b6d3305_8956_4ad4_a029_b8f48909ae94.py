from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6b6d3305-8956-4ad4-a029-b8f48909ae94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__helmet-6b6d3305/20260926T162509Z-thuan-mac/reference/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.svg'
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
    icon_id = 'helmet-6b6d3305'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self) -> None:
        # Plan: hard hat as in the reference, on HRECT_L (x 4..44, y 8..40),
        # mirrored about x=24. Brim: a rounded rectangle x 4..44, y 28..40 (r3
        # corners). Dome: two cubic quarters that follow an r16 circle about
        # (24,28) from the brim at x 8/40 up to the ridge sides at (19,13) /
        # (29,13) (tangent there at the circle's slope). Ridge: a raised band
        # x 19..29 standing on the brim and rising above the dome to y=8, with
        # r3 top corners.
        _path(self, 'brim', (7, 28), [
            (8, 28), (19, 28), (29, 28), (40, 28), (41, 28), ((44, 31), 3, 3, True), (44, 37), ((41, 40), 3, 3, True),
            (7, 40), ((4, 37), 3, 3, True), (4, 31), ((7, 28), 3, 3, True),
        ], closed=True)
        _path(self, 'dome-left', (8, 28), [('c', (8, 20), (13, 15), (19, 13))])
        _path(self, 'dome-right', (40, 28), [('c', (40, 20), (35, 15), (29, 13))])
        _path(self, 'ridge', (19, 28), [
            (19, 13), (19, 11), ((22, 8), 3, 3, True), (26, 8), ((29, 11), 3, 3, True), (29, 13), (29, 28),
        ])
        for a, b in (('brim', 'dome-left'), ('brim', 'dome-right'), ('brim', 'ridge'),
                     ('ridge', 'dome-left'), ('ridge', 'dome-right')):
            self.relate('connect', a, b)
