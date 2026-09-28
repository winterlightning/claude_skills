from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c9ec94c5-4ddc-4911-8248-43fbc7fa3b42'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__field-corner-kick/20260927T032037Z-thuan-mac-1/reference/field corner kick_c9ec94c5-4ddc-4911-8248-43fbc7fa3b42.svg'
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
    icon_id = 'field-corner-kick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('field', 'corner', 'kick', 'sports')

    def build(self) -> None:
        # Plan: corner flag. Pole x=20 (6..32) with a waving flag hung between
        # pole nodes (20,8)/(20,20) out to x=42. Two 1:2 touch lines leave the
        # pole foot (20,32) to (6,39) and (40,42); the corner arc is one cubic
        # between line nodes (10,37)/(30,37), kept >8 below the foot.
        self.add_line('pole-top', (20, 6), (20, 8))
        self.add_line('pole-mid', (20, 8), (20, 20))
        self.add_line('pole-low', (20, 20), (20, 32))
        _path(self, 'flag', (20, 8), [('c', (26, 4), (34, 12), (42, 8)), (42, 20),
                                      ('c', (34, 24), (26, 16), (20, 20))])
        self.add_line('line-l-in', (20, 32), (10, 37))
        self.add_line('line-l-out', (10, 37), (6, 39))
        self.add_line('line-r-in', (20, 32), (30, 37))
        self.add_line('line-r-out', (30, 37), (40, 42))
        _path(self, 'arc', (10, 37), [('c', (14, 41.5), (26, 41.5), (30, 37))])
        for a, b in [('pole-top', 'pole-mid'), ('pole-mid', 'pole-low'), ('flag', 'pole-top'), ('flag', 'pole-mid'),
                     ('flag', 'pole-low'), ('pole-low', 'line-l-in'), ('pole-low', 'line-r-in'),
                     ('line-l-in', 'line-r-in'), ('line-l-in', 'line-l-out'), ('line-r-in', 'line-r-out'),
                     ('arc', 'line-l-in'), ('arc', 'line-l-out'), ('arc', 'line-r-in'), ('arc', 'line-r-out')]:
            self.relate('connect', a, b)
