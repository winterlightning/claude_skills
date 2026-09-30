"""currency-dollar (redraw of the new-pipeline traced SVG).

Plan: the dollar sign on VRECT_M (centerline box (10,4)-(38,44)), built about
the vertical axis x=24 and point-symmetric about the centre (24,24).
- s: one tangent-continuous run of cubics, as in the generated image: curled
  top terminal (36,12) -> top (24,8) -> left bowl apex (10,16) -> diagonal
  spine through the centre (24,24) -> right bowl apex (38,32) -> bottom (24,40)
  -> curled bottom terminal (12,36). The bowls are quarter-ellipses rx 14 /
  ry 8 (kappa controls); the spine leaves both apexes vertically and crosses
  the centre on a 2:1 slope (handles 4 out of the apex, (-6,-3) into the
  centre, chosen over longer handles that wobbled at the apex), so every
  knot is smooth. The lower half is the 180-degree rotation of the upper
  half.
- stem: one straight line x=24 from y=4 to y=44, split at the three places the
  S crosses it (24,8), (24,24), (24,40) so the crossings are shared nodes and
  declared with relate("connect"). It projects 4 above and below the S.
Extremes: stem ends y=4 and y=44, bowl apexes x=10 and x=38 land exactly on
the VRECT_M box. Lucide `dollar-sign` informed the construction (stem through
an S, shared crossing nodes); the curled terminals follow the generated image
instead of Lucide's flat bars.

Metric issues:
- clearance e0/e1 0.0 (need 8): fixed. The crossing is the identity of the
  glyph, so it cannot be opened; the stem now shares integer nodes with the S
  at all three crossings and the contact is declared (connect), which is the
  certified form of a junction rather than an accidental overlap.
- hole 4.6 at (20,17) and hole 5.0 at (29,31) (need 6 inscribed): fixed. The
  bowls are widened to 14 each side of the stem, and the S is 32 tall (was ~27),
  so each counter between the stem, the bowl and the spine is about 14 wide
  and 12 tall on centerlines; rasterised at stroke 4 both counters measure
  8.1 inscribed (need 6).
- keyshape-short-axis (x filled 67%, stretch 1.5): fixed, the bowl apexes sit
  exactly on x=10 and x=38; y is filled by the stem (4..44).
- stroke-width 2.67 (info): redrawn at stroke 4; the terminals are 12 from the
  stem and the counters are budgeted for stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3334fbb0-436e-4762-bc8a-40fa2559c98c"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1106-currency-dollar/currency-dollar_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, MID, BOTTOM = 8, 24, 40       # S crossings of the stem
HALF_W = 14                        # bowl half-width: apexes at x=10 and x=38
BOWL_RY = 8                        # bowl half-height (TOP..MID split in two)
STEM_TOP, STEM_BOTTOM = 4, 44
TERMINAL = (36, 12)                # top curl end; the bottom one is its rotation
K = 0.5523                         # quarter-ellipse cubic kappa
SPINE_OUT = 4                      # vertical handle leaving each bowl apex
SPINE_IN = 3                       # 2:1 handle into the centre: (-6, -3)
CURL = ((32.8, 9.1), (28.5, TOP))  # curl handles, terminal -> top


def _rot(p):
    """180-degree rotation about the centre (24,24)."""
    return (2 * AXIS - p[0], 2 * MID - p[1])


class CurrencyDollarRedraw(Solo48):
    icon_id = "currency-dollar-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money"
    aliases = ("dollar sign", "usd")
    keywords = ("currency", "dollar", "money", "usd", "price", "cash")

    def build(self) -> None:
        left, right = AXIS - HALF_W, AXIS + HALF_W
        upper = [
            # curl: terminal -> top, arriving horizontally
            (*CURL, (AXIS, TOP)),
            # upper bowl quarter-ellipse: top -> left apex
            ((AXIS - HALF_W * K, TOP), (left, TOP + BOWL_RY - BOWL_RY * K), (left, TOP + BOWL_RY)),
            # spine: left apex (vertical) -> centre on a 2:1 slope
            ((left, TOP + BOWL_RY + SPINE_OUT), (AXIS - 2 * SPINE_IN, MID - SPINE_IN), (AXIS, MID)),
        ]
        lower = [
            (_rot(c2), _rot(c1), _rot(start))
            for (c1, c2, _), start in zip(
                reversed(upper),
                reversed([TERMINAL] + [seg[2] for seg in upper[:-1]]),
            )
        ]
        self.add_bezier("s", TERMINAL, *upper, *lower)
        assert lower[-1][2] == _rot(TERMINAL) and lower[0][2] == (right, MID + BOWL_RY)

        self.add_polyline("stem", (AXIS, STEM_TOP), (AXIS, TOP), (AXIS, MID),
                          (AXIS, BOTTOM), (AXIS, STEM_BOTTOM))
        self.relate("connect", "stem", "s")
