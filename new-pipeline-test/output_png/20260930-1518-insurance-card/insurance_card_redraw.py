"""insurance-card (redraw of the new-pipeline traced SVG).

Plan: a wide rounded card holding a shield on the left and two stacked
info lines on the right, on HRECT_L (centerline box (4,8)-(44,40)).
- card: rounded rectangle on the full centerline box, corner radius 4
  (Lucide credit-card rx 2 at 24 -> 4 at 48).
- interior band: every inner mark stays 9 off the card walls (an exact 8
  against the card contour comes back `review`), so inner detail lives
  in x 13..35, y 17..31.
- shield: mirrored about x=18, 10 wide (x 13..23), 14 tall (y 17..31):
  concave shoulders (y=19) rising to a top peak, straight flanks down to
  y=23, then tangent cubics closing on a pointed tip.
- info lines: two equal lines x 31..35 at y=20 and y=28 (8 apart,
  centred on the card's y=24), 8 clear of the shield flank, 9 of the wall.
Keyshape: the metrics suggested HRECT_M, but its centerline box leaves an
inner band only 12 tall (y 18..30) or less once the 8 wall clearance is taken,
too short for a readable shield with a 6 hole; HRECT_L (score 0.83,
second) gives a 14-16 band and was used instead.
Lucide constructions used: credit-card (rounded card, corner radius) and
shield (peaked top, straight flanks, curved lower sides to a point).

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: the card now sits exactly on all four HRECT_L
  extremes (x 4/44, y 8/40).
- clearance e0/e1 (card/shield 3.13): shield is 9 off the left, top and
  bottom card walls.
- clearance e0/e2, e0/e3 (card/lines ~5.2): lines end 9 before the right wall.
- clearance e1/e2, e1/e3 (shield/lines ~5): lines start 8 right of the shield.
- clearance e2/e3 (lines 4.14): lines are 8 apart.
- holes (3.4 / 4.1 between the tight parts): gone with the 8 clearances;
  the shield interior keeps a 6 inscribed hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bf6cf58a-c4bd-55e5-b5c2-806c4c390311"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1518-insurance-card/insurance-card_raw.svg"
)
AUTHOR = "claude-opus-5-5"

L, T, R, B = 4, 8, 44, 40   # card centerline box (HRECT_L)
CR = 4                      # card corner radius

AXIS = 18                   # shield mirror axis
SH_HALF = 5                 # shield flanks at AXIS -/+ 5
SH_PEAK = 17
SH_SHOULDER = 19
SH_FLANK_END = 23
SH_TIP = 31

LINE_X0, LINE_X1 = 31, 35
LINE_YS = (20, 28)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class InsuranceCardRedraw(Solo48):
    icon_id = "insurance-card-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("health-insurance-card", "insurance-id-card")
    keywords = ("insurance", "card", "shield", "coverage", "policy", "id", "health", "protection")

    def build(self) -> None:
        # Card: rounded rectangle, clockwise from the top-left corner.
        self.add_line("card-top", (L + CR, T), (R - CR, T))
        self.add_arc("card-tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("card-right", (R, T + CR), (R, B - CR))
        self.add_arc("card-br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("card-bottom", (R - CR, B), (L + CR, B))
        self.add_arc("card-bl", (L + CR, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("card-left", (L, B - CR), (L, T + CR))
        self.add_arc("card-tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        self.add_contour(
            "card", "card-top", "card-tr", "card-right", "card-br",
            "card-bottom", "card-bl", "card-left", "card-tl", closed=True,
        )

        # Shield: right half authored, left half mirrored about AXIS.
        peak = (AXIS, SH_PEAK)
        shoulder = (AXIS + SH_HALF, SH_SHOULDER)
        flank_end = (AXIS + SH_HALF, SH_FLANK_END)
        tip = (AXIS, SH_TIP)
        top_c = ((AXIS + 1.5, 18.3), (AXIS + 3, SH_SHOULDER))
        low_c = ((AXIS + SH_HALF, 27), (AXIS + 2.5, 29.5))

        self.add_bezier("shield-top-r", peak, (top_c[0], top_c[1], shoulder))
        self.add_line("shield-flank-r", shoulder, flank_end)
        self.add_bezier("shield-low-r", flank_end, (low_c[0], low_c[1], tip))
        self.add_bezier(
            "shield-low-l", tip, (mirror(low_c[1]), mirror(low_c[0]), mirror(flank_end))
        )
        self.add_line("shield-flank-l", mirror(flank_end), mirror(shoulder))
        self.add_bezier(
            "shield-top-l", mirror(shoulder), (mirror(top_c[1]), mirror(top_c[0]), peak)
        )
        self.add_contour(
            "shield", "shield-top-r", "shield-flank-r", "shield-low-r",
            "shield-low-l", "shield-flank-l", "shield-top-l", closed=True,
        )

        # Info lines.
        for i, y in enumerate(LINE_YS, 1):
            self.add_line(f"info-{i}", (LINE_X0, y), (LINE_X1, y))
