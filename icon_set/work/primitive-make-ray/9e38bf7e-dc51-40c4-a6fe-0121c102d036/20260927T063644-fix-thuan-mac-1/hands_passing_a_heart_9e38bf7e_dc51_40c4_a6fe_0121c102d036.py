from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9e38bf7e-dc51-40c4-a6fe-0121c102d036'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-passing-a-heart/20260927T061820Z-thuan-mac-1/reference/donation charity hand give heart_9e38bf7e-dc51-40c4-a6fe-0121c102d036.svg'
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
    icon_id = 'hands-passing-a-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('heart', 'hands', 'giving', 'care', 'love', 'donation', 'support', 'compassion')

    def build(self) -> None:
        # Lucide hand-heart construction: the giving hand (palm up, lower left) holds the heart on
        # its thumb; the receiving hand reaches in from the upper right, open fingers toward it.
        def heart(n, cx, y, r, tip):
            self.add_arc(n + '-l', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
            self.add_arc(n + '-shl', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
            self.add_line(n + '-sl', (cx - 2 * r + 2, y + 4), (cx, tip))
            self.add_line(n + '-sr', (cx, tip), (cx + 2 * r - 2, y + 4))
            self.add_arc(n + '-shr', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
            self.add_arc(n + '-r', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
            self.add_contour(n, n + '-l', n + '-shl', n + '-sl', n + '-sr', n + '-shr', n + '-r', closed=True)
        heart('heart', 16, 12, 4, 22)
        # giving hand
        self.add_arc('palm-upper', (4, 28), (12, 24), radius_x=8, radius_y=4, sweep=True)
        self.add_line('thumb-top-l', (12, 24), (16, 24))
        self.add_line('thumb-top-r', (16, 24), (20, 24))
        self.add_arc('thumb-tip-upper', (20, 24), (24, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (24, 28), (20, 32), radius_x=4)
        self.add_line('thumb-bottom', (20, 32), (12, 32))
        self.add_contour('thumb', 'palm-upper', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.add_line('heart-stem', (16, 22), (16, 24))
        self.relate('connect', 'heart', 'heart-stem'); self.relate('connect', 'heart-stem', 'thumb')
        self.add_line('fingers-upper', (24, 28), (30, 28))
        self.add_arc('fingertips', (30, 28), (36, 32), radius_x=6)
        self.add_line('fingers-lower', (36, 32), (28, 40))
        self.add_line('palm-base', (28, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
        # receiving hand from the upper right: fingers reach down-left at 45 degrees (r5 3-4-5 cap about (38,15))
        _path(self, 'receiver', (44, 8), [(38, 8), (34, 12), ((41, 19), 5, 5, False, True), (44, 16)])
