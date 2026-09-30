"""apple-with-upright-leaf (redraw of the new-pipeline traced SVG).

Plan: an apple body with two upper lobes, a shallow top notch and a softly
dimpled base, plus one hollow almond leaf standing upright above the notch,
detached from the fruit. Everything is mirrored about x=24 on VRECT_M
(centerline box (10,4)-(38,44), ink (8,2)-(40,46)).
- leaf: one closed contour of four cubics, tips at (24,4) and (24,17),
  widest (19..29) at y=10 with a vertical tangent, so the opening is 6
  across (5.92 on the raster, accepted by svg_metrics). The tips are the only deliberate corners.
- body: one closed contour of eight cubics, tangent-continuous everywhere.
  Right half: notch (24,26) -> lobe top (32,23) -> widest (38,32) ->
  bottom lobe (30,44) -> base dimple (24,43); the left half mirrors it.
  The notch and base dimple are kept shallow so they do not pinch at 48 px.
  Extremes: x=10/38 at the widest, y=44 at the bottom lobes, leaf tip y=4.
Keyshape: the metrics suggested SQUARE, but its x axis filled only 73%
(stretch 1.36 would flatten the apple). VRECT_M (score 0.96, x 100%,
y stretch 1.05) keeps the traced 0.73 aspect, so it is the better fit.
Traced shape: apple-with-upright-leaf_raw.svg (read for the subject only;
nothing copied from its coordinates).
Lucide: `apple` informed the lobed body with a top notch; its stem/leaf is
replaced by the requested detached upright leaf.

Metric issues:
- clearance (leaf tip 3.04 from the body, need 8): fixed, the leaf ends at
  y=17 and the notch sits at y=26; re-measured minimum is 8.49 on
  centerlines (tip to the notch shoulder), ink gap 4.49.
- hole (leaf opening 1.4 wide, need 6): fixed, the leaf is 10 wide on
  centerlines, so the opening is 6 across at stroke 4.
- keyshape-short-axis (SQUARE x fills 73%): fixed by moving to VRECT_M; the
  body spans x=10..38 and the icon y=4..44.
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8dab56ea-1c91-48e4-9197-a2a2de0bb76d"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1808-apple-with-upright-leaf/apple-with-upright-leaf_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # mirror axis
LEAF_TOP, LEAF_BOTTOM, LEAF_MID = 4, 17, 10
LEAF_HW = 5             # leaf half-width on centerlines
NOTCH_Y = 26            # top notch of the body
LOBE = (32, 23)         # upper lobe top (horizontal tangent)
WIDE = (38, 32)         # widest point (vertical tangent)
FOOT = (30, 44)         # bottom lobe (horizontal tangent)
BASE_Y = 43             # base dimple


def m(p):
    return (2 * AX - p[0], p[1])


class AppleWithUprightLeafRedraw(Solo48):
    icon_id = "apple-with-upright-leaf-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("apple", "apple-leaf")
    keywords = ("apple", "fruit", "leaf", "food", "healthy", "produce")

    def build(self) -> None:
        # Leaf: top tip -> right widest -> bottom tip -> left widest.
        top, bot = (AX, LEAF_TOP), (AX, LEAF_BOTTOM)
        r, l = (AX + LEAF_HW, LEAF_MID), (AX - LEAF_HW, LEAF_MID)
        self.add_bezier("leaf-tr", top, ((AX + 3, 5), (r[0], 7), r))
        self.add_bezier("leaf-br", r, ((r[0], 13), (AX + 3, 15), bot))
        self.add_bezier("leaf-bl", bot, ((AX - 3, 15), (l[0], 13), l))
        self.add_bezier("leaf-tl", l, ((l[0], 7), (AX - 3, 5), top))
        self.add_contour("leaf", "leaf-tr", "leaf-br", "leaf-bl", "leaf-tl", closed=True)

        # Body, right half then mirrored left half, clockwise from the notch.
        notch, base = (AX, NOTCH_Y), (AX, BASE_Y)
        right = [
            ("body-notch-r", notch, ((27, NOTCH_Y), (29, LOBE[1]), LOBE)),
            ("body-lobe-r", LOBE, ((36, LOBE[1]), (WIDE[0], 27), WIDE)),
            ("body-side-r", WIDE, ((WIDE[0], 38), (34, FOOT[1]), FOOT)),
            ("body-foot-r", FOOT, ((27, FOOT[1]), (27, BASE_Y), base)),
        ]
        for name, start, (c1, c2, end) in right:
            self.add_bezier(name, start, (c1, c2, end))
        left = []
        for name, start, (c1, c2, end) in reversed(right):
            left_name = name[:-1] + "l"
            self.add_bezier(left_name, m(end), (m(c2), m(c1), m(start)))
            left.append(left_name)
        self.add_contour("body", *[n for n, *_ in right], *left, closed=True)
