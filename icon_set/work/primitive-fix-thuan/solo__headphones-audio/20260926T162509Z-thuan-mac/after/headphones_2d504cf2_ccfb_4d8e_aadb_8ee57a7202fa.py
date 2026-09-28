from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphones-audio/20260926T162509Z-thuan-mac/reference/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.svg'
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
    icon_id = 'headphones-audio'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'audio'
    categories = ('audio', 'state')
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self) -> None:
        # Plan: over-ear headphones as in the reference (Lucide "headphones"
        # construction), on SQUARE (6..42), mirrored about x=24. The headband
        # is an r18 semicircle (apex (24,6)) on short straight ends down to the
        # ear cups' top outer corners (6,28) / (42,28). Each ear cup is a
        # rounded rectangle 10 wide (y 28..42) whose outer side continues the
        # band line, with r3 corners on the inner side and the bottom outer.
        _path(self, 'band', (6, 28), [
            (6, 24), ((24, 6), 18, 18, True), ((42, 24), 18, 18, True), (42, 28),
        ])
        _path(self, 'cup-left', (6, 28), [
            (13, 28), ((16, 31), 3, 3, True), (16, 39), ((13, 42), 3, 3, True), (9, 42), ((6, 39), 3, 3, True), (6, 28),
        ], closed=True)
        _path(self, 'cup-right', (42, 28), [
            (35, 28), ((32, 31), 3, 3, False), (32, 39), ((35, 42), 3, 3, False), (39, 42), ((42, 39), 3, 3, False), (42, 28),
        ], closed=True)
        self.relate('connect', 'band', 'cup-left')
        self.relate('connect', 'band', 'cup-right')
