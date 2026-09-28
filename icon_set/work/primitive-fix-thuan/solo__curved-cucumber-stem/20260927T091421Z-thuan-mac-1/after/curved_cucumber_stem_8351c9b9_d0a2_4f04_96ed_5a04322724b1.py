from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8351c9b9-d0a2-4f04-96ed-5a04322724b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-cucumber-stem/20260927T091421Z-thuan-mac-1/reference/cucumber whole_8351c9b9-d0a2-4f04-96ed-5a04322724b1.svg'
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
    icon_id = 'curved-cucumber-stem'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'fresh', 'cucumber')

    def build(self) -> None:
        # Cucumber on the diagonal. Axis frame ab(a, b) = (24 + a + b, 24 - a + b): a runs along the
        # fruit (lower-left -> upper-right), b across it. The body is 10 wide in ab (14 on the canvas)
        # with semicircular cubic caps; the stem leaves the upper tip and ends on the CIRCLE radius 20
        # at (36,8). Everything else stays inside radius 20.
        def ab(a, b):
            return (24 + a + b, 24 - a + b)
        k = 0.5523 * 5
        lo, hi, w = -9, 5, 5
        _path(self, "body", ab(hi + w, 0), [
            ('c', ab(hi + w, k), ab(hi + k, w), ab(hi, w)),
            ab(lo, w),
            ('c', ab(lo - k, w), ab(lo - w, k), ab(lo - w, 0)),
            ('c', ab(lo - w, -k), ab(lo - k, -w), ab(lo, -w)),
            ab(hi, -w),
            ('c', ab(hi + k, -w), ab(hi + w, -k), ab(hi + w, 0)),
        ], True)
        self.add_line("stem", ab(hi + w, 0), (36, 8))
        self.relate("connect", "body", "stem")
