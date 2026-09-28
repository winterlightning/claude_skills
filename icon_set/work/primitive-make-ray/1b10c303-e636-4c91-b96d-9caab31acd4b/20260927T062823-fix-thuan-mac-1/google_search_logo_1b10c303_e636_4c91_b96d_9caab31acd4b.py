from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1b10c303-e636-4c91-b96d-9caab31acd4b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-search-logo/20260927T061820Z-thuan-mac-1/reference/google search logo_1b10c303-e636-4c91-b96d-9caab31acd4b.svg'
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
    icon_id = 'google-search-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-search', 'google', 'search', 'letter-g', 'logo', 'brand', 'web')

    def build(self) -> None:
        # outlined Google "G": r20 outer and r10 inner rings about (24,24), radial cut on the
        # 3-4-5 ray (outer (36,8), inner (30,16)); the bar is the flat ledge at y=24 from the
        # outer right cardinal to the inner right cardinal
        _path(self, "g", (36, 8), [((44, 24), 20, 20, False, True), (34, 24),
                                   ((30, 16), 10, 10, True, True), (36, 8)], closed=True)
