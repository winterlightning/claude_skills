"""ios-logo (redraw of the new-pipeline traced SVG).

Plan: the "iOS" wordmark on HRECT_M (centerline box (4,10)-(44,38)), three
letters on one baseline (y=38), 8 apart on centerlines. The letter geometry
is reused from the typeface, not invented:
- O and S: v2 glyphs at size 28 (icon_set/typeface/glyphs-v2-sizes.json,
  centerline 12 x 24), placed at integer offsets: O (+4,+12) -> x 12..24,
  S (+24,+12) -> x 32..44, both y 14..38.
  - O: the glyph's rounded rectangle with 6-wide corners, hinted to a
    stadium: two r6 semicircles (centres (18,20) and (18,32)) and straight
    sides x=12 / x=24. The counter is 8 wide (hole >= 6).
  - S: the glyph's run (flat top bar, upper bowl, diagonal spine, lower
    bowl, flat bottom bar). Knots are snapped to integers ((38,14), (33,19),
    (35,23), (41,28), (44,33), (38,38)). Handles are re-aimed along the
    spine (6,5) so the curve-to-line joins stay tangent.
- i: the v1 letter-i construction (straight stem + stroke-wide dot). There is
  no v2 lowercase. The stem is x=4, y 18..38 (its top sits 4 below the cap
  line, as in the logo). The dot is at (4,10), 8 above the stem, and sets the
  top extreme of the box.
Extremes: x 4 (i) / 44 (S bars and lower bowl), y 10 (dot) / 38 (baseline).
No Lucide wordmark match; the construction follows Lucide type (monoline,
stadium O, flat-terminal S).

Metric issues fixed:
- clearance e0/e3 (dot 5.69 from the O) and e0/e4 (dot 3.48 from the stem):
  the dot is 8 above the stem and 11 clear of the O's top arc.
- clearance e3/e4 (stem 5.67 from the O): the stem is at x=4 and the O's left side at x=12.
- clearance e1/e3 and e2/e3 (S 3.98 / 4.17 from the O): O's right side
  x=24, the S bowl's leftmost point x=33 (9 apart), and the S bottom
  terminal (32,38) is 9.2 from the O's lower arc.
- keyshape-short-axis (y filled 85%): the dot at y=10 and the baseline at y=38
  sit on the HRECT_M box; x 4/44 fill the long axis.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- The S was traced as two paths (e1/e2) joined at the spine; it is now one
  open contour.
Not reproduced: the logo's ring-shaped i dot. A ring needs a 6-unit hole, so
r >= 5 (14 ink wide). That breaks the 40-unit width budget and the 8-unit gap
to the O, so the typeface's solid dot is used instead.
No human head/body, so the head-gap rule does not apply.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "864d41bd-ddf2-4080-a8e1-009b30743624"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1515-ios-logo/ios-logo_raw.svg"
AUTHOR = "claude-opus-5-5"

CAP, BASE = 14, 38       # v2 size-28 glyph band after the +12 y offset
# i
I_X, DOT_Y, STEM_TOP = 4, 10, 18
# O (stadium)
O_L, O_R = 12, 24
O_CX, O_R6 = 18, 6
# S (v2 glyph, +24 x offset)
S_L, S_R = 32, 44


class IosLogoRedraw(Solo48):
    icon_id = "ios-logo-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("ios", "apple ios", "iphone os")
    keywords = ("ios", "apple", "iphone", "operating system", "logo", "wordmark", "brand")

    def build(self) -> None:
        # i: v1 letter-i construction, stem + dot on one axis.
        self.add_dot("i-dot", (I_X, DOT_Y))
        self.add_line("i-stem", (I_X, STEM_TOP), (I_X, BASE))

        # O: stadium, clockwise from the top of the left side.
        top_c, bot_c = CAP + O_R6, BASE - O_R6
        self.add_arc("o-top", (O_L, top_c), (O_R, top_c), radius_x=O_R6, sweep=True)
        self.add_line("o-right", (O_R, top_c), (O_R, bot_c))
        self.add_arc("o-bottom", (O_R, bot_c), (O_L, bot_c), radius_x=O_R6, sweep=True)
        self.add_line("o-left", (O_L, bot_c), (O_L, top_c))
        self.add_contour("o", "o-top", "o-right", "o-bottom", "o-left", closed=True)

        # S: v2 glyph run from the top terminal to the bottom terminal.
        self.add_line("s-top", (S_R, CAP), (38, CAP))
        self.add_bezier("s-bowl-top", (38, CAP),
                        ((34.8, 14), (33, 16.5), (33, 19)))
        self.add_bezier("s-bowl-in", (33, 19),
                        ((33, 20.5), (33.5, 21.75), (35, 23)))
        self.add_line("s-spine", (35, 23), (41, 28))
        self.add_bezier("s-bowl-out", (41, 28),
                        ((42.8, 29.5), (44, 31.2), (44, 33)))
        self.add_bezier("s-bowl-bottom", (44, 33),
                        ((44, 35.8), (41.8, BASE), (38, BASE)))
        self.add_line("s-bottom", (38, BASE), (S_L, BASE))
        self.add_contour(
            "s", "s-top", "s-bowl-top", "s-bowl-in", "s-spine",
            "s-bowl-out", "s-bowl-bottom", "s-bottom",
        )
