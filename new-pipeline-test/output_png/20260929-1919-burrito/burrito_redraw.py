"""burrito (redraw of the new-pipeline traced SVG).

Plan: an upright wrapped burrito on VRECT_M (centerline box (10,4)-(38,44)),
the keyshape the metrics suggested for this tall subject.
- wrap: one closed contour. Straight walls x=10 / x=38 from y=14 to y=30 and a
  semicircular bottom r14 about (24,30) reaching y=44.
- filling: three lobes across the open top. The side lobes are r5 about
  (15,14) / (33,14), so they leave the wall tops with a vertical tangent and
  never pass x=10 / x=38; they meet the r6 centre lobe about (24,10) at the
  cusps (18,10) / (30,10). The centre lobe apex (24,4) is the top extreme.
- fold: one straight diagonal from the left rim (10,14) to the right wall at
  (38,30), split at (24,22) where the flap lands on it.
- flap: an r16 arc from the right rim (38,14) down to (24,22), bowed like the
  tortilla edge in the generated image. Contacts are shared endpoints declared
  with relate("connect").
- extremes: walls x=10 / 38, lobe apex y=4, bottom y=44. Symmetric about x=24
  except the fold and flap, which are diagonal by nature.
No useful Lucide match was found (Lucide has no burrito), so the construction
follows the generated image.

Metric issues (burrito_metrics.json):
- keyshape-short-axis (x fill 65%): fixed without stretching the trace. The
  walls sit on x=10 / x=38, the lobe apex on y=4 and the bottom on y=44.
- hole [23.9, 8.8] (4.56 wide, inside the filling lobes): fixed. The filling
  opening is now 8.8 inscribed.
- hole [29.4, 15.3] (3.58 wide, the triangle between fold, flap and right wall):
  fixed. The fold lands at y=30 instead of mid-wall and the flap bows upward,
  so the triangle is 6.7 inscribed.
- clearance e0/e1 (7.05) and e1/e2 (6.22): fixed. The flap and fold now meet
  the wrap only at shared endpoints; validate_icon() and the build gate report
  no MIC or internal-spacing finding.
- stroke-width (trace 2.62): redrawn at stroke 4; all holes measured at 4.
Changed from the image: its fold curls into the right wall at mid-height; here
it runs straight to the wall/bottom join, because a mid-wall landing leaves the
flap triangle under the 6-unit hole floor.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b3b9d031-1b14-49cd-b640-12d78e2f90f7"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1919-burrito/burrito_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT = 10, 38            # VRECT_M centerline box x
TOP, BOTTOM = 4, 44             # VRECT_M centerline box y
RIM = 14                        # wall tops, where the side lobes start
SIDE_R = 5                      # side lobes about (15,14) / (33,14)
MID_R = 6                       # centre lobe about (24,10), apex on TOP
CUSP_Y = TOP + MID_R
WALL_END = 30                   # walls stop and the fold lands; semicircular bottom below
FOLD_MEET = (24, 22)            # flap meets the fold here (on the fold line)
FLAP_R = 16                     # flap bows upward, like the tortilla edge


class BurritoRedraw(Solo48):
    icon_id = "burrito-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/meal"
    aliases = ("wrap", "tortilla wrap")
    keywords = ("burrito", "wrap", "tortilla", "mexican", "food", "lunch", "takeaway")

    def build(self) -> None:
        cl, cr = AXIS - MID_R, AXIS + MID_R
        self.add_line("wall-left", (LEFT, WALL_END), (LEFT, RIM))
        self.add_arc("lobe-left", (LEFT, RIM), (cl, CUSP_Y), radius_x=SIDE_R, sweep=True)
        self.add_arc("lobe-mid", (cl, CUSP_Y), (cr, CUSP_Y), radius_x=MID_R, sweep=True)
        self.add_arc("lobe-right", (cr, CUSP_Y), (RIGHT, RIM), radius_x=SIDE_R, sweep=True)
        self.add_line("wall-right", (RIGHT, RIM), (RIGHT, WALL_END))
        ry = BOTTOM - WALL_END
        self.add_arc("bottom", (RIGHT, WALL_END), (LEFT, WALL_END), radius_x=AXIS - LEFT, radius_y=ry, sweep=True)
        self.add_contour("wrap", "wall-left", "lobe-left", "lobe-mid", "lobe-right",
                         "wall-right", "bottom", closed=True)

        self.add_line("fold-upper", (LEFT, RIM), FOLD_MEET)
        self.add_line("fold-lower", FOLD_MEET, (RIGHT, WALL_END))
        self.add_contour("fold", "fold-upper", "fold-lower")
        self.add_arc("flap", (RIGHT, RIM), FOLD_MEET, radius_x=FLAP_R, sweep=False)

        self.relate("connect", "fold", "wrap")
        self.relate("connect", "flap", "wrap")
        self.relate("connect", "flap", "fold")
