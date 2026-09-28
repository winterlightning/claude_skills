from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thumbs-up-symbol/20260927T080808Z-thuan-mac-1/reference/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'
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
    icon_id = 'thumbs-up-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('thumbs', 'up', 'symbol')

    def build(self) -> None:
        # Thumbs up (reference, Lucide thumbs-up at ~1.8x): cuff box on the
        # left split by a cuff line at x=14; the thumb edge rises from the
        # cuff top (14,20) tangent into an r5 tip about (27,11) (3-4-5
        # point (23,8)), comes down to the finger top on y=20, and the
        # fist's front slants down to a rounded base.
        _path(self, 'hand', (14, 20), [(23, 8), ((27, 6), 5, 5, True), ((32, 11), 5, 5, True),
                                       ('c', (32, 15), (31, 18), (30, 20)), (38, 20), ((42, 24), 4, 4, True),
                                       (38, 38), ('c', (37, 41.5), (36, 42), (33, 42)), (14, 42), (10, 42),
                                       ((6, 38), 4, 4, True), (6, 24), ((10, 20), 4, 4, True), (14, 20)], True)
        self.add_line('cuff', (14, 20), (14, 42))
        self.relate('connect', 'cuff', 'hand')
