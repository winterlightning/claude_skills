from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cdf1b0dc-76f6-4d8f-8160-4d7a37024792'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-with-gift-box-body/20260927T080808Z-thuan-mac-1/reference/truck gift_cdf1b0dc-76f6-4d8f-8160-4d7a37024792.svg'
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
    icon_id = 'truck-with-gift-box-body'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'delivery'
    categories = ('delivery', 'primitives')
    aliases = ()
    keywords = ('truck', 'gift', 'box', 'ribbon', 'bow', 'delivery', 'vehicle', 'present')

    def build(self) -> None:
        # Truck with a gift-box body (reference): the cargo is a gift box
        # (lid band y12-20, box y20-34, ribbon x=30) with a Lucide-style bow
        # (r3 end loops + r9 arcs into the ribbon top); a low cab with an r6
        # rounded front sits against the box; r4 ring wheels hang from
        # floor nodes.
        # outer box: lid + body as one rectangle, split at every junction
        _path(self, 'box', (30, 12), [(42, 12), (42, 20), (42, 34), (36, 34), (30, 34), (18, 34),
                                      (18, 24), (18, 20), (18, 12), (30, 12)], True)
        self.add_line('lid-left', (18, 20), (30, 20))
        self.add_line('lid-right', (30, 20), (42, 20))
        self.add_line('ribbon-top', (30, 12), (30, 20))
        self.add_line('ribbon-body', (30, 20), (30, 34))
        _path(self, 'bow-left', (30, 12), [((22, 6), 9, 9, False), ((22, 12), 3, 3, False)])
        _path(self, 'bow-right', (30, 12), [((38, 6), 9, 9, True), ((38, 12), 3, 3, True)])
        _path(self, 'cab', (18, 24), [(12, 24), ((6, 30), 6, 6, False), (6, 34), (13, 34), (18, 34)])
        _circle(self, 'wheel-front', 13, 38, 4)
        _circle(self, 'wheel-back', 36, 38, 4)
        for part in ('lid-left', 'lid-right', 'ribbon-top', 'ribbon-body', 'bow-left', 'bow-right', 'cab'):
            self.relate('connect', part, 'box')
        self.relate('connect', 'ribbon-top', 'lid-left')
        self.relate('connect', 'ribbon-body', 'lid-right')
        self.relate('connect', 'wheel-front', 'cab')
        self.relate('connect', 'wheel-back', 'box')
