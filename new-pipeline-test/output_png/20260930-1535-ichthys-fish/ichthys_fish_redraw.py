"""ichthys fish (redraw of the new-pipeline traced SVG).

Plan: the Christian fish symbol on HRECT_M (centerline box (4,10)-(44,38)),
mirrored about y=24.
- body: a closed lens of two r=17 arcs from the nose (4,24) to the crossing
  X=(34,24); chord 30, sagitta 9, so the circle centres (19,32)/(19,16) are on
  integer points and the apexes sit at y=15 / y=33.
- tail: the two strokes carry on past X. Each tail is one cubic leaving X on
  the body arc's own tangent (8,+-15), so the crossing reads as two smooth
  continuous strokes, then flaring out to the (44,38) / (44,10) corners,
  which are the x=44 and y=10/38 extremes of the keyshape.
- the two tails form one contour sharing X; body and tail share X exactly
  and are related with connect.

Metric issues:
- keyshape-short-axis (y filled 48%): fixed. The body is fattened (half
  height 9 instead of ~5) and the tail tips are pushed to the y=10/38
  corners, so all four HRECT_M extremes are on the box.
- stroke-width (trace 2.67 vs 4): fixed by re-authoring at stroke 4; the
  lens opening is 18 units on centerlines (14 of ink), far above 6.
- loose-join x4 (e0-e4 fragments missing each other by 0.76-1.11 around the
  crossing): fixed. The trace's five fragments are replaced by one body
  contour and one tail contour meeting at the exact integer node X.
No useful Lucide match (Lucide `fish` is a naturalistic fish); construction
follows Lucide practice of integer-centred circular arcs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4b380f58-586b-45bc-8749-b86c9b2f3e5c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1535-ichthys-fish/ichthys-fish_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_Y = 24
NOSE = (4, AXIS_Y)
CROSS = (34, AXIS_Y)
BODY_R = 17                      # chord 30, sagitta 9: centres (19, 24 +- 8)
TAIL_TIP = (44, 38)              # lower tail tip; the upper one is mirrored
# Leave X along the body-arc tangent (8, 15), then flare out to the tip.
TAIL_LO = ((36, 27.75), (40, 33), TAIL_TIP)


def my(p):
    return (p[0], 2 * AXIS_Y - p[1])


class IchthysFishRedraw(Solo48):
    icon_id = "ichthys-fish-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/religion"
    aliases = ("ichthys", "jesus fish", "christian fish")
    keywords = ("ichthys", "fish", "christian", "christianity", "religion", "faith", "symbol")

    def build(self) -> None:
        self.add_arc("body-top", NOSE, CROSS, radius_x=BODY_R, sweep=True)
        self.add_arc("body-bottom", CROSS, NOSE, radius_x=BODY_R, sweep=True)
        self.add_contour("body", "body-top", "body-bottom", closed=True)

        # Upper tail drawn tip -> X, lower tail X -> tip, as one contour.
        up = [my(p) for p in TAIL_LO]
        self.add_bezier("tail-up", up[2], (up[1], up[0], CROSS))
        self.add_bezier("tail-low", CROSS, TAIL_LO)
        self.add_contour("tail", "tail-up", "tail-low")
        self.relate("connect", "tail", "body")
