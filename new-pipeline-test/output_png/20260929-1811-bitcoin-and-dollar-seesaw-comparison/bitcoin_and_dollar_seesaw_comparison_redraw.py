"""Bitcoin and dollar seesaw comparison (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)) instead of the suggested HRECT_M.
At stroke 4 the Bitcoin sign needs 20 units of height (two 8-high counters
plus 2-unit ticks), then 8 of clearance to the beam, then the beam and a
6-high fulcrum: 36 units. HRECT_M gives 28 and HRECT_L 32, and on either
the beam would have to rise to the left to clear the B, reversing the
comparison. As in the image: B high on the left, $ lower on the right, one
straight beam sloping down to the right, fulcrum centred under it.
- bitcoin: one closed contour, spine x=6 (the x=6 extreme), top/bottom
  edges y=8/y=24 to x=18, two radius-4 bowls out to x=22; a mid bar y=16
  from the spine to the bowl node. Two ticks (x=10, x=18) 2 above and below
  make it a Bitcoin sign rather than a baht; the top ticks set the y=6
  extreme. Counters are 12x8 on centerlines (8 inscribed, over the 6 floor).
- dollar: an S of two half-ellipses (rx 6, ry 4) between a top terminal to
  x=42 (the x=42 extreme) and a bottom terminal to x=30, centred on x=36,
  y=19, with 2-unit stem ends above and below (Lucide dollar-sign's bar-arc
  -arc-bar S; its full stem is shortened because a stem through a 12-wide S
  sits 6 from each bowl).
- beam: (6,34)->(24,36)->(42,38), split at the pivot node; slope 1/9 is the
  steepest that keeps the B's bottom ticks 8 clear of the beam.
- fulcrum: an open wedge (18,42)-(24,36)-(30,42) sharing the beam's pivot
  node; its feet set the y=42 extreme.
Metric issues:
- stroke-width (trace 2.55): redrawn at stroke 4 on the integer grid.
- stroke-count (11 vs 6): kept at 11 marks; the ₿ needs its bar and four
  ticks and the $ its two stem ends to stay readable currency signs.
- keyshape-short-axis (HRECT_M x fill 96%): moot; SQUARE is used (see plan)
  and all four extremes sit exactly on its box.
- clearance e0/e1 vs e2..e6 (B ticks, spine, serif stubs 2.6-5.1 apart):
  fixed; the traced spine, serif stubs and doubled strokes are rebuilt as one
  B contour whose ticks are 8 apart and attach to its edges.
- clearance/hole errors inside the $ and B (holes 1.0-1.2 inscribed): fixed;
  B counters are 8 inscribed on centerlines and the S is open.
- hole (23.7,35.4) (fulcrum triangle 1.0): fixed by opening the fulcrum into
  a wedge; a closed triangle with a 6 opening needs 9 of height that the
  square does not have below the beam.
- clearance between symbols and beam: fixed; B ticks clear the beam by
  8.4, the $ stem by 8.3.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ebaeb4ff-d25c-4ebd-91eb-0f8877362e5b"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1811-bitcoin-and-dollar-seesaw-comparison/bitcoin-and-dollar-seesaw-comparison_raw.svg"
AUTHOR = "claude-opus-5-5"

TICK = 2

B_SPINE = 6
B_TOP, B_MID, B_BOTTOM = 8, 16, 24
B_BOWL_X = 18
B_BOWL_R = (B_MID - B_TOP) // 2
B_TICKS = (10, 18)

S_X, S_Y = 36, 19
S_RX, S_RY = 6, 4

BEAM = ((6, 34), (24, 36), (42, 38))
FOOT_Y = 42
FOOT_HALF = 6


class BitcoinAndDollarSeesawComparisonRedraw(Solo48):
    icon_id = "bitcoin-and-dollar-seesaw-comparison-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ("bitcoin vs dollar", "crypto versus fiat", "currency seesaw")
    keywords = ("bitcoin", "dollar", "seesaw", "balance", "comparison", "crypto",
                "currency", "exchange", "value")

    def build(self) -> None:
        self._bitcoin()
        self._dollar()
        self._seesaw()

    def _bitcoin(self) -> None:
        s, t, m, b, x = B_SPINE, B_TOP, B_MID, B_BOTTOM, B_BOWL_X
        self.add_line("b-top", (s, t), (x, t))
        self.add_arc("b-bowl-upper", (x, t), (x, m), radius_x=B_BOWL_R, sweep=True)
        self.add_arc("b-bowl-lower", (x, m), (x, b), radius_x=B_BOWL_R, sweep=True)
        self.add_line("b-bottom", (x, b), (s, b))
        self.add_line("b-spine-low", (s, b), (s, m))
        self.add_line("b-spine-up", (s, m), (s, t))
        self.add_contour("bitcoin", "b-top", "b-bowl-upper", "b-bowl-lower", "b-bottom",
                         "b-spine-low", "b-spine-up", closed=True)
        self.add_line("b-bar", (s, m), (x, m))
        self.relate("connect", "b-bar", "bitcoin")
        for i, tx in enumerate(B_TICKS):
            self.add_line(f"b-tick-top-{i}", (tx, t), (tx, t - TICK))
            self.add_line(f"b-tick-bottom-{i}", (tx, b), (tx, b + TICK))
            self.relate("connect", f"b-tick-top-{i}", "bitcoin")
            self.relate("connect", f"b-tick-bottom-{i}", "bitcoin")

    def _dollar(self) -> None:
        x, y = S_X, S_Y
        top, bottom = y - 2 * S_RY, y + 2 * S_RY
        self.add_line("s-top", (x + S_RX, top), (x, top))
        self.add_arc("s-upper", (x, top), (x, y), radius_x=S_RX, radius_y=S_RY, sweep=False)
        self.add_arc("s-lower", (x, y), (x, bottom), radius_x=S_RX, radius_y=S_RY, sweep=True)
        self.add_line("s-foot", (x, bottom), (x - S_RX, bottom))
        self.add_contour("dollar", "s-top", "s-upper", "s-lower", "s-foot")
        self.add_line("s-stem-top", (x, top - TICK), (x, top))
        self.add_line("s-stem-bottom", (x, bottom), (x, bottom + TICK))
        self.relate("connect", "s-stem-top", "dollar")
        self.relate("connect", "s-stem-bottom", "dollar")

    def _seesaw(self) -> None:
        left, pivot, right = BEAM
        px, py = pivot
        self.add_line("beam-left", left, pivot)
        self.add_line("beam-right", pivot, right)
        self.add_contour("beam", "beam-left", "beam-right")
        self.add_line("fulcrum-left", (px - FOOT_HALF, FOOT_Y), pivot)
        self.add_line("fulcrum-right", pivot, (px + FOOT_HALF, FOOT_Y))
        self.add_contour("fulcrum", "fulcrum-left", "fulcrum-right")
        self.relate("connect", "beam", "fulcrum")
