"""bitcoin-cryptocurrency-symbol-solo (redraw of the new-pipeline traced SVG).

Plan: the upright Bitcoin sign on VRECT_M (centerline box (10,4)-(38,44)).
- B: straight spine at x=14, flat top edge (y=11), waist (y=23) and bottom
  edge (y=37). Upper bowl is an r6 half circle, lower bowl an r7 half circle,
  both centred on x=31 so they meet the waist in one cusp; the lower bowl is
  the wider one (right extreme x=38), the upper stops at x=37.
- serifs: the top and bottom edges run on past the spine to x=10, the left
  box edge, as in the generated image.
- bars: two short vertical currency bars at x=18 and x=26 (8 apart), from the
  top edge up to y=4 and from the bottom edge down to y=44.
Extremes: x 10 (serifs) / 38 (lower bowl), y 4 / 44 (bars).

Metric issues fixed:
- stroke-width: redrawn at stroke 4; every gap re-budgeted for it.
- keyshape-short-axis: the x axis now spans the full 28 (10..38) by
  construction instead of the trace's 85%.
- clearance e0/e2, e0/e4, e1/e2, e3/e4 (bars 3.6-6 from the spine and from
  each other): bars now sit 8 apart and 4 right of the spine, attached to the
  edges rather than floating beside the spine.
- loose-join e5/e6/e7: the waist and both bowls share the exact point
  (31,23) inside the B contours, and every attachment is related.
Not fixed:
- stroke-count (8, budget 6): the model still paints 8 parts (two B contours,
  two serifs, four bar stubs). Each bar stub and serif is a real feature of the
  sign and none can merge into a contour without a T-junction; all share exact
  endpoints with the B, so the drawing reads as one connected mark.
Lucide: bitcoin (slanted glyph with bars through the stem) informed the
two-bar construction; the upright, serifed form follows the generated image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "056563c8-a6c4-4201-b355-6ff5f08795ea"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1819-bitcoin-cryptocurrency-symbol-solo/bitcoin-cryptocurrency-symbol-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT = 10                     # serif ends, left box edge
SPINE = 14                    # B spine x
TOP, MID, BOT = 11, 23, 37    # top edge, waist, bottom edge
BOWL_X = 31                   # both bowl centres
R_UP, R_LOW = (MID - TOP) // 2, (BOT - MID) // 2   # 6 and 7
BAR_X = (18, 26)              # currency bars, 8 apart
BAR_TOP, BAR_BOT = 4, 44


class BitcoinCryptocurrencySymbolSoloRedraw(Solo48):
    icon_id = "bitcoin-cryptocurrency-symbol-solo-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "money"
    aliases = ("bitcoin", "btc")
    keywords = ("bitcoin", "cryptocurrency", "crypto", "currency", "money", "btc")

    def build(self) -> None:
        # upper counter: closed loop spine -> top edge -> upper bowl -> waist
        self.add_line("spine-top", (SPINE, MID), (SPINE, TOP))
        self.add_line("top-edge", (SPINE, TOP), (BOWL_X, TOP))
        self.add_arc("bowl-up", (BOWL_X, TOP), (BOWL_X, MID),
                     radius_x=R_UP, radius_y=R_UP, sweep=True)
        self.add_line("waist", (BOWL_X, MID), (SPINE, MID))
        self.add_contour("b-upper", "spine-top", "top-edge", "bowl-up", "waist", closed=True)
        # lower counter: open run from the waist cusp back to the spine node
        self.add_arc("bowl-low", (BOWL_X, MID), (BOWL_X, BOT),
                     radius_x=R_LOW, radius_y=R_LOW, sweep=True)
        self.add_line("bottom-edge", (BOWL_X, BOT), (SPINE, BOT))
        self.add_line("spine-bot", (SPINE, BOT), (SPINE, MID))
        self.add_contour("b-lower", "bowl-low", "bottom-edge", "spine-bot")
        self.relate("connect", "b-upper", "b-lower")

        self.add_line("serif-top", (LEFT, TOP), (SPINE, TOP))
        self.add_line("serif-bot", (LEFT, BOT), (SPINE, BOT))
        self.relate("connect", "serif-top", "b-upper")
        self.relate("connect", "serif-bot", "b-lower")

        for x in BAR_X:
            self.add_line(f"bar-up-{x}", (x, BAR_TOP), (x, TOP))
            self.add_line(f"bar-down-{x}", (x, BOT), (x, BAR_BOT))
            self.relate("connect", f"bar-up-{x}", "b-upper")
            self.relate("connect", f"bar-down-{x}", "b-lower")
