from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '11057d2e-0abd-44e2-8f11-78749e9e05aa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-ads-logo/20260927T055612Z-thuan-mac-1/reference/google ads logo_11057d2e-0abd-44e2-8f11-78749e9e05aa.svg'
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
    icon_id = 'google-ads-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-ads', 'google', 'advertising', 'letter-a', 'logo', 'brand', 'marketing')

    def build(self) -> None:
        # Plan: Ads "A". Front pill on direction (3,4), width 10, r5 caps about
        # (19,11) (top 6) and (37,35) (right 42), sides tangent at the 3-4-5
        # points. Back pill runs from the front pill's top-left (15,14) and its
        # side node J(21,22) down-left onto a full r5 circle about (11,37)
        # (left 6, bottom 42) at its left/right points.
        _path(self, 'front', (15, 14), [((19, 6), 5, 5, True), ((23, 8), 5, 5, True), (41, 32),
                                        ((42, 35), 5, 5, True), ((37, 40), 5, 5, True), ((33, 38), 5, 5, True),
                                        (21, 22), (15, 14)], True)
        _circle(self, 'dot', 11, 37, 5)
        self.add_line('back-left', (15, 14), (6, 37))
        self.add_line('back-right', (21, 22), (16, 37))
        for a in ('back-left', 'back-right'):
            self.relate('connect', a, 'front')
            self.relate('connect', a, 'dot')
