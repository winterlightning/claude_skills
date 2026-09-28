from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4defab66-f891-589d-9113-250444b98543'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__segmented-hand-grenade/20260927T072849Z-thuan-mac-1/reference/bomb grenade_4defab66-f891-589d-9113-250444b98543.svg'
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
    icon_id = 'segmented-hand-grenade'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('grenade', 'explosive', 'lever', 'cap', 'weapon', 'segment')

    def build(self) -> None:
        # Grenade body: r13 circle about (29,29) with a vertical seam and a
        # lower band on its 5-12-13 points (17,34)/(41,34).
        _path(self, 'body', (21, 19), [((29, 16), 13, 13, True), ((37, 19), 13, 13, True), ((42, 29), 13, 13, True),
                                       ((41, 34), 13, 13, True), ((29, 42), 13, 13, True), ((17, 34), 13, 13, True),
                                       ((16, 29), 13, 13, True), ((21, 19), 13, 13, True)], True)
        self.add_line('seam', (29, 16), (29, 34))
        self.add_line('seam-low', (29, 34), (29, 42))
        self.add_line('band', (17, 34), (29, 34))
        self.add_line('band-r', (29, 34), (41, 34))
        for n in ('seam', 'seam-low', 'band', 'band-r'):
            self.relate('connect', n, 'body')
        for a, b in [('seam', 'seam-low'), ('seam', 'band'), ('seam', 'band-r'), ('seam-low', 'band'),
                     ('seam-low', 'band-r'), ('band', 'band-r')]:
            self.relate('connect', a, b)
        # Fuse cap on top (walls 8 either side of the seam) and the safety
        # lever curving down the left side.
        _path(self, 'cap', (21, 19), [(21, 10), (21, 6), (37, 6), (37, 19)])
        _path(self, 'lever', (21, 10), [('c', (12, 10), (6, 18), (6, 28))])
        self.relate('connect', 'cap', 'body')
        self.relate('connect', 'lever', 'cap')
