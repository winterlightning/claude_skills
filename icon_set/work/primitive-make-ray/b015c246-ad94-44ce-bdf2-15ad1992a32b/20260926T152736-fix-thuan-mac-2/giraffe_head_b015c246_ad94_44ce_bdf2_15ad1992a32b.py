from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b015c246-ad94-44ce-bdf2-15ad1992a32b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__giraffe-head/20260926T152555Z-thuan-mac-2/reference/giraffe_b015c246-ad94-44ce-bdf2-15ad1992a32b.svg'
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
    icon_id = 'giraffe-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('giraffe', 'head', 'neck', 'ossicone', 'ear', 'profile', 'animal', 'safari')

    def build(self) -> None:
        # Plan: giraffe head and neck in profile facing right on SQUARE (naturally
        # asymmetric). One outline: the back of the neck rises at slope 1:2 from the
        # bottom-left corner to the ear base (18,18), the head top runs to the
        # forehead corner (28,14), the forehead slopes at 45 degrees to a rounded
        # muzzle (rightmost x=42), the jaw returns to the throat (28,30), and the
        # throat drops to the bottom edge. The head keeps 9+ between forehead and jaw.
        # A lens ear points up-left from the ear base; the ossicone rises from the
        # forehead corner to the top edge (its round cap is the knob).
        _path(self, 'head', (6, 42), [
            (18, 18), (28, 14), (37, 23),
            ('c', (40, 26), (42, 28), (42, 31)),
            ('c', (42, 34), (40, 36), (37, 36)),
            (28, 30), (22, 42),
        ])
        _path(self, 'ear', (18, 18), [
            ('c', (22, 11), (15, 6), (9, 7)),
            ('c', (6, 12), (11, 18), (18, 18)),
        ], closed=True)
        self.add_line('ossicone', (28, 14), (29, 6))
        self.relate('connect', 'head', 'ear')
        self.relate('connect', 'head', 'ossicone')
