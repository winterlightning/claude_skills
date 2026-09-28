from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dfccab11-823b-4fad-8702-015ab9e71741'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__industrial-factory-batch-025-09/20260926T164653Z-thuan-mac/reference/factory_dfccab11-823b-4fad-8702-015ab9e71741.svg'
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
    icon_id = 'industrial-factory-batch-025-09'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('industrial', 'factory')

    def build(self) -> None:
        # Plan: factory as in the reference, on HRECT_L (x 4..44, y 8..40): one
        # closed outline of a wide body (y 24..40) with shoulders at both ends,
        # two tall chimneys standing on it near the sides (outer side tapering
        # in from 9 wide at the base to 8 at the top, y 8..24), and a low gable
        # roof between the chimneys peaking at (24,19), 8 clear of both
        # chimneys. Mirrored about x=24. On SQUARE the 8-unit clearances force
        # full-width chimneys with no shoulders, the drawing that was rejected.
        _path(self, 'factory', (4, 40), [
            (4, 24), (7, 24), (8, 8), (16, 8), (16, 24), (24, 19), (32, 24), (32, 8), (40, 8), (41, 24),
            (44, 24), (44, 40), (4, 40),
        ], closed=True)
