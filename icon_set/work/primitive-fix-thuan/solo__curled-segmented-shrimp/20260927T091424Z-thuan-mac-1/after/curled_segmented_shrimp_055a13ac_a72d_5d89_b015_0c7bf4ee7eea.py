from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '055a13ac-a72d-5d89-b015-0c7bf4ee7eea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curled-segmented-shrimp/20260927T091424Z-thuan-mac-1/reference/shrimp_055a13ac-a72d-5d89-b015-0c7bf4ee7eea.svg'
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
    icon_id = 'curled-segmented-shrimp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('shrimp', 'prawn', 'seafood', 'shellfish', 'tail', 'segment', 'food')

    def build(self) -> None:
        # Plan (Lucide shrimp, mirrored to the reference pose): rostrum pill (cap r4
        # about (10,13)) with an antenna hook up to (23,6); head bar y=17; curled
        # back = two quarter ellipses about (28,29) to the tail point (28,42); tail
        # loop r4 inside the curl; inner edge = quarter ellipse back to the cap;
        # one segment arc; eye 8 below the bar; lower tail flick.
        _path(self, 'rostrum', (23, 6), [
            ((20, 9), 3, 3, True), (10, 9), ((6, 13), 4, 4, False), ((10, 17), 4, 4, False),
        ])
        self.add_line('bar', (10, 17), (28, 17))
        _path(self, 'body', (28, 17), [
            ((42, 29), 14, 12, True), ((28, 42), 14, 13, True),
            ((32, 38), 4, 4, False), ((28, 34), 4, 4, False),
            ((10, 17), 18, 17, True),
        ])
        self.add_bezier('segment', (28, 17), ((34, 21), (34, 30), (28, 34)))
        self.add_line('flick', (28, 42), (23, 42))
        self.add_dot('eye', (24, 25))
        for a, b in (('rostrum', 'bar'), ('rostrum', 'body'), ('bar', 'body'), ('segment', 'body'),
                     ('segment', 'bar'), ('flick', 'body')):
            self.relate('connect', a, b)
