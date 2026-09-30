"""bitcoin-and-dollar-balance-scale (redraw of the new-pipeline traced SVG).

Plan: a Bitcoin sign and a dollar sign floating over the two ends of a
level balance beam, with a pan hanging under each end and a central pillar,
on SQUARE (centerline box (6,6)-(42,42), ink (4,4)-(44,44)).
- glyphs: one shared bar pitch of 8 (bars at y=8, 16, 24) and tick/stem
  tips at y=6 and y=26, so both signs are exactly the same height.
  - bitcoin: closed B contour (spine x=6, bars to x=14, upper bowl r4,
    lower bowl 5x4 so the lower lobe is slightly fuller), middle bar, and
    four 2-unit ticks at x=6 and x=14 (8 apart).
  - dollar: Lucide dollar-sign construction (bar, r4 arc, bar, r4 arc,
    bar) about stem x=36, with 2-unit stem stubs landing on split bar nodes.
- scale: beam y=35 from x=6 to 42, 9 below the glyph tips (an exact 8
  comes back review). Pans are 5x7 half-ellipses hanging from the beam
  ends (x 6..16 and 32..42) down to y=42. The pillar rises from y=42 through
  the beam to a tip at y=29 between the glyphs, the balance pivot.
Traced shape: bitcoin-and-dollar-balance-scale_raw.svg and the generated
PNG (read for the subject only; nothing copied from their coordinates).
Lucide: dollar-sign (bar/arc/bar/arc/bar) for the $; scale (beam, centre
post, pans) for the balance, reduced to fit the 48 grid.

Metric issues:
- clearance errors (60, all glyph-internal crowding, pivot ring, V hangers,
  pan rims vs bowls and the foot): fixed by rebuilding every part at
  stroke 4 with >= 8 between distinct centerlines; the validator is clean.
- stroke-count (24 strokes, budget 6): fixed by merging into contours:
  bitcoin, dollar, beam, pillar and two pans, plus small tick/stem stubs.
- loose-join (9 info, near-miss trace joins): fixed; every contact is a
  shared integer node with a declared connect (ticks, stems, pans, pillar).
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
- keyshape-short-axis (HRECT_M, x fills 96%): not kept. HRECT_M gives 28
  of centerline height; the glyphs alone need 20 (three bars at pitch 8
  plus tips), the beam needs 9 more and hanging pans 7, so 36 is the
  minimum. SQUARE fits exactly: x 6..42 and y 6..42 are all touched.
Not repairable at 48 (reductions, stated): the pivot ring, the V pan
hangers, the flat pan rims and the foot bar are dropped; each needs 8 of
clearance the 36-unit budget does not have. The pans therefore hang
directly from the beam ends, and the pillar has no foot (a foot at y=42
would sit < 8 from the pan bowls).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "40a6f5d9-1d48-449a-9169-f46dd5fad662"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1805-bitcoin-and-dollar-balance-scale/bitcoin-and-dollar-balance-scale_raw.svg"
AUTHOR = "claude-opus-5-5"

TOP = 6            # tick / stem tips (keyshape top)
BAR = 8            # glyph bar pitch: top bar y=8, middle 16, bottom 24
BEAM_Y = 35        # beam: 9 below the glyph tips at y=26 (exact 8 comes back review)
BOTTOM = 42        # pan bottoms and post foot (keyshape bottom)
LEFT, RIGHT, AX = 6, 42, 24
PAN_RX = 5         # pans hang from the beam ends, 10 wide, 7 deep
FINIAL_Y = 29      # post tip above the beam, >= 8.6 from both glyphs

B_X = 6            # bitcoin spine
B_W = 8            # bitcoin bar length = tick pitch
USD_X = 36         # dollar stem


class BitcoinAndDollarBalanceScaleRedraw(Solo48):
    icon_id = "bitcoin-and-dollar-balance-scale-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/crypto"
    aliases = ("crypto-vs-fiat", "bitcoin-dollar-scale")
    keywords = ("bitcoin", "dollar", "balance", "scale", "compare",
                "exchange rate", "crypto", "fiat", "currency", "weigh")

    def _bitcoin(self) -> None:
        x0, x1 = B_X, B_X + B_W
        y0, y1, y2 = TOP + 2, TOP + 2 + BAR, TOP + 2 + 2 * BAR
        self.add_line("btc-top", (x0, y0), (x1, y0))
        self.add_arc("btc-upper", (x1, y0), (x1, y1), radius_x=4, radius_y=4)
        self.add_arc("btc-lower", (x1, y1), (x1, y2), radius_x=5, radius_y=4)
        self.add_line("btc-bottom", (x1, y2), (x0, y2))
        self.add_line("btc-spine", (x0, y2), (x0, y0))
        self.add_contour("bitcoin", "btc-top", "btc-upper", "btc-lower",
                         "btc-bottom", "btc-spine", closed=True)
        self.add_line("btc-middle", (x0, y1), (x1, y1))
        self.relate("connect", "bitcoin", "btc-middle")
        for i, x in enumerate((x0, x1)):
            self.add_line(f"btc-tick-top-{i}", (x, TOP), (x, y0))
            self.add_line(f"btc-tick-bottom-{i}", (x, y2), (x, y2 + 2))
            self.relate("connect", "bitcoin", f"btc-tick-top-{i}")
            self.relate("connect", "bitcoin", f"btc-tick-bottom-{i}")

    def _dollar(self) -> None:
        c = USD_X
        y0, y1, y2 = TOP + 2, TOP + 2 + BAR, TOP + 2 + 2 * BAR
        self.add_line("usd-top-right", (c + 5, y0), (c, y0))
        self.add_line("usd-top-left", (c, y0), (c - 2, y0))
        self.add_arc("usd-upper", (c - 2, y0), (c - 2, y1), radius_x=4, sweep=False)
        self.add_line("usd-middle", (c - 2, y1), (c + 2, y1))
        self.add_arc("usd-lower", (c + 2, y1), (c + 2, y2), radius_x=4, sweep=True)
        self.add_line("usd-bottom-right", (c + 2, y2), (c, y2))
        self.add_line("usd-bottom-left", (c, y2), (c - 5, y2))
        self.add_contour("dollar", "usd-top-right", "usd-top-left", "usd-upper", "usd-middle",
                         "usd-lower", "usd-bottom-right", "usd-bottom-left")
        # both bars are split at the stem so both stubs land on contour nodes
        self.add_line("usd-stem-top", (c, TOP), (c, y0))
        self.add_line("usd-stem-bottom", (c, y2), (c, y2 + 2))
        self.relate("connect", "dollar", "usd-stem-top")
        self.relate("connect", "dollar", "usd-stem-bottom")

    def build(self) -> None:
        self._bitcoin()
        self._dollar()
        l_in, r_in = LEFT + 2 * PAN_RX, RIGHT - 2 * PAN_RX
        self.add_polyline("beam", (LEFT, BEAM_Y), (l_in, BEAM_Y), (AX, BEAM_Y),
                          (r_in, BEAM_Y), (RIGHT, BEAM_Y))
        self.add_arc("pan-left", (l_in, BEAM_Y), (LEFT, BEAM_Y),
                     radius_x=PAN_RX, radius_y=BOTTOM - BEAM_Y)
        self.add_arc("pan-right", (RIGHT, BEAM_Y), (r_in, BEAM_Y),
                     radius_x=PAN_RX, radius_y=BOTTOM - BEAM_Y)
        self.add_line("post", (AX, FINIAL_Y), (AX, BEAM_Y))
        self.add_line("stand", (AX, BEAM_Y), (AX, BOTTOM))
        self.add_contour("pillar", "post", "stand")
        for part in ("pan-left", "pan-right", "pillar"):
            self.relate("connect", "beam", part)
