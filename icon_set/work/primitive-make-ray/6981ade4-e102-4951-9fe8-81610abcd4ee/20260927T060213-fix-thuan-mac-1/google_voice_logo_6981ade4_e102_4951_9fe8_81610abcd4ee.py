from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6981ade4-e102-4951-9fe8-81610abcd4ee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-voice-logo/20260927T055657Z-thuan-mac-1/reference/google voice logo_6981ade4-e102-4951-9fe8-81610abcd4ee.svg'
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
    icon_id = 'google-voice-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'google-voice-logo')

    def build(self) -> None:
        # handset: round ear cap r5 about (12,11), round mouth cap r5 about (37,37) (3-4-5 joins),
        # a smooth back and an inner edge with two rounded knees
        _path(self, "handset", (7, 11), [
            ((16, 8), 5, 5, True),                  # ear cap over the top (y=6)
            (19, 12),                                     # ear inner edge, leaving the cap tangentially
            ('c', (21, 15), (19, 18), (16, 19)),          # upper knee
            ('c', (15, 24), (23, 30), (27, 29)),          # hollow of the grip
            ('c', (30, 29), (32, 28), (35, 29)),          # lower knee
            (40, 33),                                     # mouth inner edge
            ((37, 42), 5, 5, True),                       # mouth cap (x=42, ends at its bottom y=42)
            ('c', (24, 42), (6, 34), (6, 22)),            # back
            ('c', (6, 17), (7, 14), (7, 11)),
        ], closed=True)
        # the voice quarter: square corner at lower left, quarter-circle r14 edge at upper right
        _path(self, "voice", (28, 6), [((42, 20), 14, 14, True), (28, 20), (28, 6)], closed=True)
