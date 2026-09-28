from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '246da30c-4eca-45d5-9192-54c56c7c7ec3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ice-skate/20260926T164653Z-thuan-mac/reference/skating shoes_246da30c-4eca-45d5-9192-54c56c7c7ec3.svg'
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
    icon_id = 'ice-skate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: ice skate as in the reference, on SQUARE (6..42). Boot: straight
        # back (x=8) with a rounded heel, a collar sloping up to the front
        # (8,10)->(22,6), a straight shaft front down to an r5 instep curve, a
        # flat vamp (y=21) and a round r5/r4 toe onto the sole (y=34). Two posts
        # (x 14/33) carry the flat blade, one full-width stroke on y=42 whose
        # round caps give the reference's thin rounded bar.
        _path(self, 'boot', (12, 34), [
            ((8, 30), 4, 4, True), (8, 10), (22, 6), (22, 16), ((27, 21), 5, 5, False), (34, 21),
            ((39, 26), 5, 5, True), (39, 30), ((35, 34), 4, 4, True), (33, 34), (14, 34), (12, 34),
        ], closed=True)
        _path(self, 'blade', (6, 42), [(14, 42), (33, 42), (42, 42)])
        self.add_line('rear-post', (14, 34), (14, 42))
        self.add_line('front-post', (33, 34), (33, 42))
        for post in ('rear-post', 'front-post'):
            self.relate('connect', 'boot', post)
            self.relate('connect', 'blade', post)
