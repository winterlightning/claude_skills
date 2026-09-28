from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a894d3a4-f35b-4f12-bdb2-21459fe032ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-inmate-avatar/20260926T175624Z-thuan-mac-1/reference/man inmate_a894d3a4-f35b-4f12-bdb2-21459fe032ab.svg'
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False, ids=None):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = (ids or {}).get(i, f"{name}-{i + 1}")
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
    icon_id = 'man-inmate-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('man', 'inmate', 'portrait', 'bust')

    def build(self) -> None:
        # Inmate: a rounded prison cap (r4 crown corners) crossed by two stripe
        # lines 8 apart, over a circular r10 jaw touching a closed shirt
        # (rounded shoulders, hem line across the bottom).
        # Reference: human_ref/user.svg bust; supplied inmate drawing.
        _path(self, 'head', (14, 13), [(14, 8), ((18, 4), 4, 4, True), (30, 4), ((34, 8), 4, 4, True),
                                      (34, 13), (34, 21), ((14, 21), 10, 10, True), (14, 13)], True)
        self.add_line('stripe-top', (14, 13), (34, 13))
        self.add_line('stripe-bottom', (14, 21), (34, 21))
        self.relate('connect', 'head', 'stripe-top')
        self.relate('connect', 'head', 'stripe-bottom')
        _path(self, 'body', (8, 44), [((18, 35), 10, 9, True), (24, 35), (30, 35), ((40, 44), 10, 9, True), (8, 44)], True,
              ids={1: 'body-top', 2: 'body-top-right'})
        self.relate('connect', 'head', 'body')
