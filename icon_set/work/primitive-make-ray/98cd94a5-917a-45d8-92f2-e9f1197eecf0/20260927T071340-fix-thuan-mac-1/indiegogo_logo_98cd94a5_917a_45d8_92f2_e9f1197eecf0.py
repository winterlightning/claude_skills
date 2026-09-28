from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '98cd94a5-917a-45d8-92f2-e9f1197eecf0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__indiegogo-logo/20260927T070909Z-thuan-mac-1/reference/indiegogo logo_98cd94a5-917a-45d8-92f2-e9f1197eecf0.svg'
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
    icon_id = 'indiegogo-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('indiegogo', 'crowdfunding', 'go', 'wordmark', 'logo', 'brand', 'campaign')

    def build(self) -> None:
        # "GO" in the reference's rounded-rectangle letterforms (corner radius 6)
        _path(self, "g", (20, 14), [
            ((14, 8), 6, 6, False), (10, 8), ((4, 14), 6, 6, False),
            (4, 34), ((10, 40), 6, 6, False), (14, 40), ((20, 34), 6, 6, False),
            (20, 26), (12, 26),
        ])
        _path(self, "o", (34, 8), [
            (38, 8), ((44, 14), 6, 6, True), (44, 34), ((38, 40), 6, 6, True),
            (34, 40), ((28, 34), 6, 6, True), (28, 14), ((34, 8), 6, 6, True),
        ], closed=True)
