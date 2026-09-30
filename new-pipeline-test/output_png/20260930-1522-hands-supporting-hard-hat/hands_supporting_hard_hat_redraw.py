"""hands supporting hard hat (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24.
- ridge: one contour, Lucide `hard-hat` style: a r=4 cap about (24,10)
  (apex = the y=6 extreme) whose legs x=20/28 drop into the dome to y=14,
  8 above the brim.
- dome: two quarter ellipses rx=9 ry=12 about (20,22)/(28,22), from the brim
  at x=11/37 up to the cap's feet (20,10)/(28,10), where they end on the
  ridge (connected).
- brim: one straight line at y=22, x=9..39, split at the dome feet so both
  halves share its endpoints (connected).
- hands: two mirrored polylines, up-turned fingers at the outer edges
  (x=6 / x=42 extremes), a 1:2 palm diagonal inward and the wrist down to
  y=42 (bottom extreme). Finger tips at y=30 sit 8.54 from the brim ends.
Keyshape: SQUARE instead of the suggested HRECT_L. The source is 1:1 and
fills SQUARE 100% on both axes; HRECT_L needed a 1.25 x-stretch, which pulls
the hands far wider than the hat.
Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: moot on SQUARE; all four extremes touch the box.
- clearance e0/e2 (dome halves 3.66 apart at the ridge): the ridge legs are
  8 apart on centerlines and each dome half ends on its own leg.
- clearance e1/e3 (ridge legs 6.1 above the brim): the legs now stop at
  y=14, 8 above the brim.
- clearance e0/e4, e2/e5, e3/e4, e3/e5 (hands 3.5-6.6 from brim and dome):
  the finger tips moved down to y=30 and the brim ends in to x=9/39, so
  every tip is 8.54 from the brim and farther from the dome.
- hole (4.29 wide): the ridge is open into the dome (no closed ridge box)
  and the capsule brim, whose 4-unit slot could never hold a 6-unit hole,
  is reduced to a single line.
- no-head: not applicable; the subject is two hands, not a figure, so no
  mark_human_figure.
Dropped: the capsule outline of the brim (see hole).
Rejected variants: a ridge bump sitting on a circular/elliptic dome read as a
cloche knob at 48 px; a single centre line in a half-ellipse dome read as a
bell. The legs-into-dome ridge is what makes it a hard hat.
Lucide: `hard-hat` informed the dome-plus-ridge construction (dome arcs end
on the ridge legs); no Lucide original for supporting hands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "20214d85-2a10-45f3-974e-7a15e7241f74"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1522-hands-supporting-hard-hat/hands-supporting-hard-hat_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BRIM_Y = 22
DOME_RX, DOME_RY = 9, 12            # quarter ellipses, brim to ridge feet
RIDGE_HALF = 4                      # ridge legs at AXIS -/+ 4
RIDGE_CAP_Y = BRIM_Y - DOME_RY      # cap centre (24,10); apex y=6
RIDGE_LEG_END = BRIM_Y - 8          # 8 above the brim
BRIM_HALF = 15                      # brim x = 9..39
FINGER_X, FINGER_TOP, FINGER_BEND = 6, 30, 33
PALM_DX, PALM_DY = 10, 5
WRIST_BOTTOM = 42


def mx(x: int) -> int:
    return 2 * AXIS - x


class HandsSupportingHardHatRedraw(Solo48):
    icon_id = "hands-supporting-hard-hat-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/safety"
    aliases = ("safety first", "worker protection", "hard hat care")
    keywords = ("hard hat", "helmet", "hands", "support", "safety",
                "construction", "protection", "worker", "insurance")

    def build(self) -> None:
        leg_l, leg_r = AXIS - RIDGE_HALF, AXIS + RIDGE_HALF
        foot_l, foot_r = leg_l - DOME_RX, mx(leg_l - DOME_RX)

        self.add_line("ridge-l", (leg_l, RIDGE_LEG_END), (leg_l, RIDGE_CAP_Y))
        self.add_arc("ridge-cap", (leg_l, RIDGE_CAP_Y), (leg_r, RIDGE_CAP_Y),
                     radius_x=RIDGE_HALF)
        self.add_line("ridge-r", (leg_r, RIDGE_CAP_Y), (leg_r, RIDGE_LEG_END))
        self.add_contour("ridge", "ridge-l", "ridge-cap", "ridge-r")

        self.add_arc("dome-l", (foot_l, BRIM_Y), (leg_l, RIDGE_CAP_Y),
                     radius_x=DOME_RX, radius_y=DOME_RY)
        self.add_arc("dome-r", (leg_r, RIDGE_CAP_Y), (foot_r, BRIM_Y),
                     radius_x=DOME_RX, radius_y=DOME_RY)
        self.add_polyline("brim", (AXIS - BRIM_HALF, BRIM_Y), (foot_l, BRIM_Y),
                          (foot_r, BRIM_Y), (AXIS + BRIM_HALF, BRIM_Y))
        for dome in ("dome-l", "dome-r"):
            self.relate("connect", dome, "ridge")
            self.relate("connect", dome, "brim")

        for side, sx in (("l", lambda x: x), ("r", mx)):
            wrist_x = FINGER_X + PALM_DX
            self.add_polyline(
                f"hand-{side}",
                (sx(FINGER_X), FINGER_TOP), (sx(FINGER_X), FINGER_BEND),
                (sx(wrist_x), FINGER_BEND + PALM_DY), (sx(wrist_x), WRIST_BOTTOM),
            )
