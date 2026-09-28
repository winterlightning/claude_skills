from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c1ec3ebc-af3e-4938-9bbc-35d4bd66a87a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jeet-logo/20260927T070909Z-thuan-mac-1/reference/jeet logo_c1ec3ebc-af3e-4938-9bbc-35d4bd66a87a.svg'
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
    icon_id = 'jeet-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('jeet', 'grid', 'css', 'quatrefoil', 'logo', 'brand', 'framework')

    def build(self) -> None:
        # quatrefoil: four r10 semicircular lobes about (24,14), (34,24), (24,34), (14,24), meeting in
        # notches at the lattice points (34,14), (34,34), (14,34), (14,14); ring r6 at the centre
        _path(self, "quatrefoil", (14, 14), [
            ((34, 14), 10, 10, True), ((34, 34), 10, 10, True),
            ((14, 34), 10, 10, True), ((14, 14), 10, 10, True),
        ], closed=True)
        _circle(self, "ring", 24, 24, 6)
