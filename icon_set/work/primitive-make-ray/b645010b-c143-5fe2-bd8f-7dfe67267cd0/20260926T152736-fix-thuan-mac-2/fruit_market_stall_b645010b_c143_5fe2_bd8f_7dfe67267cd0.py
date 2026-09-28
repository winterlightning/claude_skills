from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b645010b-c143-5fe2-bd8f-7dfe67267cd0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fruit-market-stall/20260926T152555Z-thuan-mac-2/reference/farmers market kiosk_b645010b-c143-5fe2-bd8f-7dfe67267cd0.svg'
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
    icon_id = 'fruit-market-stall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'events'
    categories = ('primitives', 'events')
    aliases = ()
    keywords = ('market', 'stall', 'with', 'fruit')

    def build(self) -> None:
        # Plan: market stall on SQUARE, mirrored about x=24.
        # Awning: trapezoid (10,6)-(38,6) flaring to (6,14)/(42,14), its bottom edge
        # three scallops (r7 arcs on 12-wide chords); two stripe dividers run from the
        # top edge to the scallop cusps. Posts drop from the awning corners to the
        # ground; the counter shelf spans them at y=40. The fruit is one pile of three
        # round bumps standing on the shelf (dips 8 above the shelf, tops 9 below the
        # scallops) - three separate apples cannot keep 8 apart between the posts.
        _path(self, 'awning', (10, 6), [
            (38, 6), (42, 14),
            ((30, 14), 7, 7, True), ((18, 14), 7, 7, True), ((6, 14), 7, 7, True),
            (10, 6),
        ], closed=True)
        self.add_line('stripe-left', (19, 6), (18, 14))
        self.add_line('stripe-right', (29, 6), (30, 14))
        _path(self, 'post-left', (6, 14), [(6, 40), (6, 42)])
        _path(self, 'post-right', (42, 14), [(42, 40), (42, 42)])
        self.add_line('shelf-left', (6, 40), (15, 40))
        self.add_line('shelf-mid', (15, 40), (33, 40))
        self.add_line('shelf-right', (33, 40), (42, 40))
        _path(self, 'fruit', (15, 40), [
            ('c', (14, 33), (17, 27.5), (21, 32)),
            ('c', (21, 26), (27, 26), (27, 32)),
            ('c', (31, 27.5), (34, 33), (33, 40)),
        ])
        for part in ('stripe-left', 'stripe-right', 'post-left', 'post-right'):
            self.relate('connect', 'awning', part)
        self.relate('connect', 'shelf-left', 'post-left', 'shelf-mid')
        self.relate('connect', 'shelf-right', 'post-right', 'shelf-mid')
        self.relate('connect', 'shelf-mid', 'fruit')
