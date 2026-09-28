from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c7e5eabf-e0c2-47d6-9a2b-23487329395b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__javascript-logo/20260927T070911Z-thuan-mac-1/reference/java script logo_c7e5eabf-e0c2-47d6-9a2b-23487329395b.svg'
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
    icon_id = 'javascript-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('javascript', 'js', 'programming', 'language', 'logo', 'brand', 'web')

    def build(self) -> None:
        # "JS" at full height (y 6..42), as in the set's typescript-logo.
        # J: stem x=18 into an r6 hook whose tip (6,36) sets the left edge.
        _path(self, 'J', (18, 6), [(18, 36), ((12, 42), 6, 6, True), ((6, 36), 6, 6, True)])
        # S: two rx8/ry9 bowls about (34,15) and (34,33), spine through
        # (34,24); leftmost x=26 keeps 8 from the J stem, rightmost x=42.
        _path(self, 'S', (41, 10), [('c', (39, 7), (37, 6), (34, 6)), ((26, 15), 8, 9, False),
                                    ((34, 24), 8, 9, False), ((42, 33), 8, 9, True),
                                    ((34, 42), 8, 9, True), ('c', (31, 42), (28, 41), (27, 38))])
