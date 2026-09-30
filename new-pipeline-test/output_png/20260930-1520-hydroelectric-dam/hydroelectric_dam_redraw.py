"""hydroelectric-dam (redraw of the new-pipeline traced SVG).

Plan: a trapezoidal dam wall with two spillway lines on its face and one
water wave below, on HRECT_M (centerline box (4,10)-(44,38)), mirrored about
x=24.
- wall: closed trapezoid, crest y=10 from x=10..38, base y=25 from x=4..44
  (sides slope 2:5). Crest and base are split where the spillways attach.
- spillways: (19,10)->(17,25) and the mirror (29,10)->(31,25), splaying
  outward like the trace; they share endpoints with the crest and base and
  are declared as connections. The middle bay is wider than the side bays
  (as in the image) and bays measure ink holes of 7.0 / 8.2 / 7.0.
- water: one Lucide-style wave (Lucide `waves`: period 10 / amplitude 1 at
  24 -> period 20 / amplitude 2 at 48), four tangent-continuous cubic
  half-waves with nodes on y=36 at x=4,14,24,34,44, peaking exactly at
  y=34 and y=38; its top sits 9 below the wall base (a curve at exactly 8 comes back
  as review, so the wall base was raised from 26 to 25).
Keyshape: HRECT_M as suggested; crest y=10 and wave trough y=38 reach the
short axis, dam base corners and wave ends reach x=4/44.
Lucide constructions used: `waves` (cubic half-waves, amplitude/period).

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: the trace filled 66% of the HRECT_M height; the wall
  was made taller (15) and the wave placed so crest and trough touch y=10/38.
- clearance e0/e3, e1/e3, e2/e3 (wave ~3.2 below the wall): the wave's
  highest point is now 9 below the wall base (y=25 vs 34).
- holes at (11.3,23.9)/(36.7,23.9) (5.19 side bays): bays widened, the crest
  runs 10..38 and spillways sit at 19/29 so each side bay holds a 7.0 ink hole.
- holes at y=30.8 (0.8 slivers between wall base and wave): gone, the wave
  no longer approaches the wall.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6411cee5-9e14-533a-9adf-d5bcd2213734"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1520-hydroelectric-dam/hydroelectric-dam_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
CREST_Y, BASE_Y = 10, 25
CREST_HALF, BASE_HALF = 14, 20        # crest x 10..38, base x 4..44
SPILL_TOP, SPILL_BOT = 5, 7           # spillway offsets from the axis

WAVE_Y = 36
WAVE_AMP = 2                          # crest 34, trough 38
WAVE_X0, WAVE_HALF, WAVE_N = 4, 10, 4
WAVE_C = WAVE_AMP * 4 / 3             # cubic control offset for a peak of WAVE_AMP


def mx(x):
    return 2 * AXIS - x


class HydroelectricDamRedraw(Solo48):
    icon_id = "hydroelectric-dam-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/infrastructure"
    aliases = ("hydro-dam", "hydropower-dam", "dam")
    keywords = ("hydroelectric", "dam", "hydropower", "water", "energy", "reservoir", "spillway", "renewable")

    def build(self) -> None:
        cl, cr = AXIS - CREST_HALF, AXIS + CREST_HALF
        bl, br = AXIS - BASE_HALF, AXIS + BASE_HALF
        stl, str_ = AXIS - SPILL_TOP, AXIS + SPILL_TOP
        sbl, sbr = AXIS - SPILL_BOT, AXIS + SPILL_BOT

        # Wall: clockwise from the crest's left corner.
        self.add_line("crest-l", (cl, CREST_Y), (stl, CREST_Y))
        self.add_line("crest-m", (stl, CREST_Y), (str_, CREST_Y))
        self.add_line("crest-r", (str_, CREST_Y), (cr, CREST_Y))
        self.add_line("side-r", (cr, CREST_Y), (br, BASE_Y))
        self.add_line("base-r", (br, BASE_Y), (sbr, BASE_Y))
        self.add_line("base-m", (sbr, BASE_Y), (sbl, BASE_Y))
        self.add_line("base-l", (sbl, BASE_Y), (bl, BASE_Y))
        self.add_line("side-l", (bl, BASE_Y), (cl, CREST_Y))
        self.add_contour(
            "wall", "crest-l", "crest-m", "crest-r", "side-r",
            "base-r", "base-m", "base-l", "side-l", closed=True,
        )

        # Spillways, mirrored about the axis.
        self.add_line("spill-l", (stl, CREST_Y), (sbl, BASE_Y))
        self.add_line("spill-r", (str_, CREST_Y), (sbr, BASE_Y))
        self.relate("connect", "spill-l", "crest-l")
        self.relate("connect", "spill-l", "base-l")
        self.relate("connect", "spill-r", "crest-r")
        self.relate("connect", "spill-r", "base-r")

        # Water: alternating cubic half-waves, down first like the image.
        segs = []
        for i in range(WAVE_N):
            x = WAVE_X0 + i * WAVE_HALF
            dy = WAVE_C if i % 2 == 0 else -WAVE_C
            segs.append((
                (x + WAVE_HALF / 3, WAVE_Y + dy),
                (x + 2 * WAVE_HALF / 3, WAVE_Y + dy),
                (x + WAVE_HALF, WAVE_Y),
            ))
        self.add_bezier("wave", (WAVE_X0, WAVE_Y), *segs)
