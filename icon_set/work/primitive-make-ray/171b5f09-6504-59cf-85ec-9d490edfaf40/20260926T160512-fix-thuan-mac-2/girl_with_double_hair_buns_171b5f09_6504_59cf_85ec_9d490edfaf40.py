from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '171b5f09-6504-59cf-85ec-9d490edfaf40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__girl-with-double-hair-buns/20260926T160438Z-thuan-mac-2/reference/chinese kid girl_171b5f09-6504-59cf-85ec-9d490edfaf40.svg'
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
    icon_id = 'girl-with-double-hair-buns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('girl', 'with', 'double', 'hair', 'buns')

    def build(self) -> None:
        # Plan: girl's head with two hair buns on SQUARE, mirrored about x=24 (a
        # head silhouette, no detached-head flags apply). Each bun is three quarters
        # of an r6 circle in a top corner (touching x=6/42 and y=6); its inner
        # quarter is hidden behind the head, as in the reference. The head's domed
        # top (r8 arc) runs between the buns' inner points (18,12)/(30,12); the head
        # sides leave the buns' bottom points (12,18)/(36,18) and curve down to the
        # chin (24,42). The hairline (bangs) runs from the sides at (9,29) up to a
        # centre parting at (24,22).
        def mx(p):
            return (48 - p[0], p[1])
        _path(self, 'head', (18, 12), [
            ((30, 12), 8, 8, True),
            ((36, 6), 6, 6, True), ((42, 12), 6, 6, True), ((36, 18), 6, 6, True),
            ('c', mx((10, 21)), mx((9, 25)), mx((9, 29))),
            ('c', mx((9, 37)), mx((15, 42)), (24, 42)),
            ('c', (15, 42), (9, 37), (9, 29)),
            ('c', (9, 25), (10, 21), (12, 18)),
            ((6, 12), 6, 6, True), ((12, 6), 6, 6, True), ((18, 12), 6, 6, True),
        ], closed=True)
        _path(self, 'hairline', (9, 29), [
            ('c', (13, 25), (18, 23), (24, 22)),
            ('c', mx((18, 23)), mx((13, 25)), mx((9, 29))),
        ])
        self.relate('connect', 'head', 'hairline')
