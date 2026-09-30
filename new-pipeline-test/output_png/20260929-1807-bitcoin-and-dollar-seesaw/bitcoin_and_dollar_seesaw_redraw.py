"""bitcoin and dollar seesaw (redraw of the new-pipeline traced SVG): a Bitcoin
sign above the low left end of a tilted seesaw beam, a dollar sign above the
high right end, and a small fulcrum under the middle of the beam.

Plan: SQUARE envelope, centerline box (6,6)-(42,42).
- bitcoin: B with two equal D bowls (bars 8 long + r5 arcs, bowls 10 tall so
  each opening is 6 inscribed), stem on x=6, two ticks (x=6 and x=14, 8 apart)
  of length 2 above and below. Top y=6, bottom y=30.
- dollar: Lucide dollar-sign construction (terminal line, arc, short middle
  line, arc, terminal line) with r4 arcs and rows 8 apart (y=8,16,24); the bar
  is two stubs on x=36 attached to the top and bottom rows. Top y=6, right
  x=42.
- beam: one straight 1:6 run (6,40)-(42,34), split at its midpoint (24,37).
- fulcrum: open inverted V from the beam midpoint to feet on y=42, connected
  to the beam (a closed triangle would need a 6-inscribed hole, about 15 units
  tall, which the budget cannot hold).
The heavier (bitcoin) end is down, matching the source's "unequal" tilt; the
bitcoin is 4 units taller than the dollar, which the tilt pays for.
Lucide construction: dollar-sign (terminals + arcs + short middle run);
Lucide bitcoin's two-tick B, set upright.

Keyshape: SQUARE instead of the suggested HRECT_M. HRECT_M is 28 tall on
centerlines, but the bitcoin alone needs 24 (two 10-unit bowls for the 6-unit
holes + ticks), plus the 8 gap to the beam and the fulcrum under it.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted for it.
- stroke-count: 12 traced strokes -> 4 parts (bitcoin, dollar, beam, fulcrum)
  built from contours and connected stubs.
- keyshape-short-axis: SQUARE filled exactly: x=6 (stem, beam end), x=42
  (dollar terminal, beam end), y=6 (ticks, dollar bar), y=42 (fulcrum feet).
- clearance e0/e10, e2/e10 (dollar vs beam): dollar bottom 26 sits >= 8.8
  off the beam (beam y=35 under it).
- clearance e3/e6, e3/e8, e3/e9, e4/e5, e4/e7, e4/e8, e5/e7, e6/e9 (bitcoin
  internals): bars 10 apart, ticks 8 apart, ticks carried on bar vertices.
- clearance e4/e10, e6/e10, e7/e10, e8/e10 (bitcoin vs beam): lowest ticks
  at y=30 stay >= 8.5 off the beam.
- clearance e10/e11 (beam vs fulcrum): the fulcrum now meets the beam at a
  shared endpoint with relate("connect").
- loose-join e1/e0, e2/e0, e7/e8, e8/e9: stubs and ticks share exact
  endpoints with their rows and are related as connections.
- hole (0.4 in the B, 1.17 in the triangle): B bowls are 6 inscribed; the
  fulcrum is an open V, so it has no hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "45ba347e-d70c-49ad-bd22-e2ad93cdeafd"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1807-bitcoin-and-dollar-seesaw/bitcoin-and-dollar-seesaw_raw.svg"
AUTHOR = "claude-opus-5-5"

# bitcoin
BX = 6            # stem
B_BAR = 8         # straight bar length; second tick sits on its end
B_R = 5           # bowl radius (bowl height 10)
B_TOP = 8         # top bar row
TICK = 2

# dollar
DX = 36           # bar axis
D_R = 4           # arc radius (rows 8 apart)
D_TOP = 8         # top row
D_HALF = 6        # terminals reach DX +/- 6

# seesaw
BEAM_L = (6, 40)
BEAM_MID = (24, 37)
BEAM_R = (42, 34)
FOOT_Y = 42
FOOT_DX = 4


class BitcoinAndDollarSeesawRedraw(Solo48):
    icon_id = "bitcoin-and-dollar-seesaw-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ("bitcoin versus dollar", "crypto dollar balance")
    keywords = ("bitcoin", "dollar", "seesaw", "balance", "compare", "cryptocurrency", "exchange")

    def build(self) -> None:
        self._bitcoin()
        self._dollar()
        self.add_polyline("beam", BEAM_L, BEAM_MID, BEAM_R)
        mx, my = BEAM_MID
        self.add_polyline("fulcrum", (mx - FOOT_DX, FOOT_Y), BEAM_MID, (mx + FOOT_DX, FOOT_Y))
        self.relate("connect", "beam", "fulcrum")

    def _bitcoin(self) -> None:
        x0, x1 = BX, BX + B_BAR
        top, mid, bot = B_TOP, B_TOP + 2 * B_R, B_TOP + 4 * B_R
        self.add_line("btc-top", (x0, top), (x1, top))
        self.add_arc("btc-upper", (x1, top), (x1, mid), radius_x=B_R, sweep=True)
        self.add_arc("btc-lower", (x1, mid), (x1, bot), radius_x=B_R, sweep=True)
        self.add_line("btc-bottom", (x1, bot), (x0, bot))
        self.add_line("btc-stem-low", (x0, bot), (x0, mid))
        self.add_line("btc-stem-high", (x0, mid), (x0, top))
        self.add_contour("bitcoin", "btc-top", "btc-upper", "btc-lower", "btc-bottom",
                         "btc-stem-low", "btc-stem-high", closed=True)
        self.add_line("btc-mid", (x0, mid), (x1, mid))
        self.relate("connect", "bitcoin", "btc-mid")
        for i, x in enumerate((x0, x1), 1):
            self.add_line(f"btc-tick-top-{i}", (x, top - TICK), (x, top))
            self.add_line(f"btc-tick-bottom-{i}", (x, bot), (x, bot + TICK))
            self.relate("connect", "bitcoin", f"btc-tick-top-{i}")
            self.relate("connect", "bitcoin", f"btc-tick-bottom-{i}")

    def _dollar(self) -> None:
        r0, r1, r2 = D_TOP, D_TOP + 2 * D_R, D_TOP + 4 * D_R
        left, right = DX - D_R // 2, DX + D_R // 2   # arc ends: DX-2 / DX+2
        self.add_line("usd-top-a", (DX + D_HALF, r0), (DX, r0))
        self.add_line("usd-top-b", (DX, r0), (left, r0))
        self.add_arc("usd-upper", (left, r0), (left, r1), radius_x=D_R, sweep=False)
        self.add_line("usd-mid", (left, r1), (right, r1))
        self.add_arc("usd-lower", (right, r1), (right, r2), radius_x=D_R, sweep=True)
        self.add_line("usd-bottom-a", (right, r2), (DX, r2))
        self.add_line("usd-bottom-b", (DX, r2), (DX - D_HALF, r2))
        self.add_contour("dollar", "usd-top-a", "usd-top-b", "usd-upper", "usd-mid",
                         "usd-lower", "usd-bottom-a", "usd-bottom-b")
        self.add_line("usd-bar-top", (DX, r0 - TICK), (DX, r0))
        self.add_line("usd-bar-bottom", (DX, r2), (DX, r2 + TICK))
        self.relate("connect", "dollar", "usd-bar-top")
        self.relate("connect", "dollar", "usd-bar-bottom")
