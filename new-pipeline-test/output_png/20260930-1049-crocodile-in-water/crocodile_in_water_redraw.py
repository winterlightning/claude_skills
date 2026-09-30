"""crocodile-in-water (redraw of the new-pipeline traced SVG).

Plan: a right-facing crocodile floating low over one separate wavy water
line, on HRECT_M (the metrics suggestion; centerline box (4,10)-(44,38)).
- crocodile: one closed contour. Straight back y=15 from the tail tip (4,15),
  two sawtooth back ridges (apex y=11, steep faces toward the tail, parallel
  and 10 apart), a half-circle eye bump r5 centred (30,15) whose apex is the
  top edge y=10, a straight snout top to x=39, a half-circle nose r5 reaching
  x=44, a straight waterline belly y=25 and a cubic that curves the belly up
  into the tail tip.
- water: one cubic wave, knots on troughs y=38 / crests y=34 every 10 units
  with horizontal tangents, mirrored about x=24; troughs are the bottom edge.
Extremes: x 4 (tail tip, wave ends) / 44 (nose, wave ends), y 10 (eye bump) /
38 (wave troughs).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (warn): fixed without stretching the trace; the eye
  bump reaches y=10 and the wave troughs y=38.
- clearance e0/e3, e0/e4, e1/e4, e2/e4, e3/e4 (errors): fixed. The eye speck
  (e3) and the stray jaw tick (e2) are gone, the open snout curl and tail
  stroke became one closed body, and the water crests sit 9 below the belly.
- loose-join e0/e2, e1/e2 (info): fixed; one closed contour, shared endpoints.
- hole at (21.8, 25.5), 4.04 wide (error): fixed; the body is a 10-unit band
  between back and belly, a 6-wide ink hole.
Re-running svg_metrics.py on the redraw reports no issues.
Not kept: the hollow eye. Any eye mark inside the bump must clear its walls by
more than 8, which needs a r9 bump; that bump swallowed the head and read as
a cloud (tried and rejected), so the bump alone carries the eye.
No Lucide crocodile exists; the water follows Lucide `waves`
(horizontal-tangent cubic half-waves).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ca6a591c-ff28-52f1-afee-3a6b95328acd"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1049-crocodile-in-water/crocodile-in-water_raw.svg"
AUTHOR = "claude-opus-5-5"

BACK_Y = 15                # back and snout top
JAW_Y = 25                 # waterline belly: 10 below the back, so the body hole is 6 wide in ink
TAIL = (4, BACK_Y)         # tail tip, left edge of the box
EYE = (30, BACK_Y)         # eye bump centre
EYE_R = 5                  # half-circle bump, apex y=10 = top edge of the box
NOSE = (39, 20)            # nose half-circle centre, r5 reaches x=44
NOSE_R = JAW_Y - NOSE[1]
# (base, apex, end) of each back ridge; the steep faces toward the tail are
# parallel and 10 apart (8.9 on centerlines), ridge 2 ends 5 short of the eye.
RIDGES = (((6, 15), (8, 11), (16, 15)), ((16, 15), (18, 11), (20, 15)))
WAVE_KNOTS = ((4, 38), (14, 34), (24, 38), (34, 34), (44, 38))  # troughs y=38, crests y=34
WAVE_PULL = 4              # horizontal-tangent handle length on each half-wave


class CrocodileInWaterRedraw(Solo48):
    icon_id = "crocodile-in-water-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/reptiles"
    aliases = ("alligator in water", "swimming crocodile", "gator")
    keywords = ("crocodile", "alligator", "reptile", "water", "river", "swamp", "wave", "animal", "wildlife")

    def build(self) -> None:
        ex, ey = EYE
        bump_l, bump_r = (ex - EYE_R, ey), (ex + EYE_R, ey)
        nose_top, nose_bot = (NOSE[0], BACK_Y), (NOSE[0], JAW_Y)

        # Top outline, tail to snout: two back ridges, the eye bump, the long snout.
        (b1, a1, e1), (b2, a2, e2) = RIDGES
        self.add_line("back-0", TAIL, b1)
        self.add_line("ridge-1-up", b1, a1)
        self.add_line("ridge-1-down", a1, e1)
        self.add_line("ridge-2-up", b2, a2)
        self.add_line("ridge-2-down", a2, e2)
        self.add_line("back-1", e2, bump_l)
        self.add_arc("eye-bump", bump_l, bump_r, radius_x=EYE_R, sweep=True)
        self.add_line("snout-top", bump_r, nose_top)
        self.add_arc("nose", nose_top, nose_bot, radius_x=NOSE_R, sweep=True)
        # Waterline belly back to the tail, curving up into the tail tip.
        self.add_line("belly", nose_bot, (16, JAW_Y))
        self.add_bezier("tail-under", (16, JAW_Y), ((10, JAW_Y), (6, 21), TAIL))
        self.add_contour(
            "crocodile",
            "back-0", "ridge-1-up", "ridge-1-down", "ridge-2-up", "ridge-2-down", "back-1",
            "eye-bump", "snout-top", "nose", "belly", "tail-under",
            closed=True,
        )

        # Separate water line: four half-waves with horizontal tangents at every knot.
        (x0, y0), *rest = WAVE_KNOTS
        segments = []
        for x1, y1 in rest:
            segments.append(((x0 + WAVE_PULL, y0), (x1 - WAVE_PULL, y1), (x1, y1)))
            x0, y0 = x1, y1
        self.add_bezier("water", WAVE_KNOTS[0], *segments)
