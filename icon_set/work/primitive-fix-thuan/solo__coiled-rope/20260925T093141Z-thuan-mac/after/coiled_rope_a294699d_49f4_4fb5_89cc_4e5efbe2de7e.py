"""A coiled rope hank: two rope loops lying on a diagonal, tied at the waist by a binding.

Symbol plan: the hank axis runs 45 degrees from lower-left to upper-right through (24,24).
The binding is a rectangle turned 45 degrees about (24,24), 17 along the axis and 14
across it, split by one wrap line into two equal wrapped bands (8.5 each). Each loop is a
round cubic loop leaving and rejoining the binding at its two end corners, mirrored about
the axis, with knots on its outer extremes (top/right, bottom/left) so the keyshape edges
land on knots. The lower loop is the upper one turned 180 degrees about the centre.
Lucide construction: no rope glyph; loops follow Lucide's full-circle arcs, the binding
its 45-degree straight runs (as in 'diamond').
Keyshape SQUARE: centerline x 6..42, y 6..42 (outer sides of the two loops).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a294699d-49f4-4fb5-89cc-4e5efbe2de7e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__coiled-rope/20260925T093141Z-thuan-mac/reference/outdoors rope 1_a294699d-49f4-4fb5-89cc-4e5efbe2de7e.svg"
AUTHOR = "claude-opus-5-5"


class CoiledRope(Solo48):
    icon_id = "coiled-rope"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors/equipment"
    aliases = ("outdoors-rope", "rope", "rope-hank")
    keywords = ("rope", "coil", "hank", "climbing", "outdoors", "camping", "cord", "lasso")

    def build(self) -> None:
        turn = lambda p: (48 - p[0], 48 - p[1])  # 180-degree turn about (24,24)
        # binding: rotated rectangle p in [-6, 6] along the axis, q in [-5, 5] across it
        a, b = (25, 13), (35, 23)            # upper-right end corners
        c, d = turn(a), turn(b)              # lower-left end corners (23,35), (13,25)
        self.add_polyline("binding", a, b, c, d, closed=True)
        self.add_line("binding-wrap", (19, 19), (29, 29))
        self.relate("connect", "binding", "binding-wrap")
        # upper loop: corner a -> top extreme -> right extreme -> corner b
        top, right = (31, 6), (42, 17)
        h1, h2, h3 = 3, 4, 6
        self.add_bezier("loop-upper", a,
                        ((a[0], a[1] - h1), (top[0] - h2, top[1]), top),
                        ((top[0] + h3, top[1]), (right[0], right[1] - h3), right),
                        ((right[0], right[1] + h2), (b[0] + h1, b[1]), b))
        tb, tr, tt = turn(b), turn(right), turn(top)
        self.add_bezier("loop-lower", c,
                        ((c[0], c[1] + h1), (tt[0] + h2, tt[1]), tt),
                        ((tt[0] - h3, tt[1]), (tr[0], tr[1] + h3), tr),
                        ((tr[0], tr[1] - h2), (d[0] - h1, d[1]), d))
        self.relate("connect", "binding", "loop-upper")
        self.relate("connect", "binding", "loop-lower")
