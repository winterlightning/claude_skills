from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd2809250-1b46-4c46-822c-17af67873899'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__festive-bunting-confetti/20260927T072058Z-thuan-mac-1/reference/party decoration_d2809250-1b46-4c46-822c-17af67873899.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'festive-bunting-confetti'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'events'
    categories = ('primitives', 'events')
    aliases = ()
    keywords = ('festive', 'party', 'bunting', 'flags')

    def build(self) -> None:
        # Plan (mirrored about x=24): a sagging bunting string across the
        # top with three closed pennants hanging from it (top edges are rope
        # segments, inradius > 3.2), and confetti below - a plus in the
        # middle and a slanted streamer dash in each lower corner.
        rope = [(4, 8), (14, 11), (19, 13), (29, 13), (34, 11), (44, 8)]
        _path(self, 'rope', rope[0], rope[1:])
        for i, (a, b, tip) in enumerate([((4, 8), (14, 11), (9, 26)), ((19, 13), (29, 13), (24, 26)),
                                         ((34, 11), (44, 8), (39, 26))]):
            _path(self, f'pennant-{i}', b, [tip, a])
            self.relate('connect', f'pennant-{i}', 'rope')
        self.add_line('plus-h', (21, 37), (27, 37))
        self.add_line('plus-v', (24, 34), (24, 40))
        self.relate('connect', 'plus-h', 'plus-v')
        self.add_line('streamer-left', (4, 40), (8, 34))
        self.add_line('streamer-right', (40, 34), (44, 40))
