"""crossed wrists with closed hands (redraw of the new-pipeline traced SVG).

Subject: two closed fists raised at the upper left and upper right, their
forearms crossing in an X below; the right forearm passes in front, the
left one is broken where it passes behind.

Plan: SQUARE (centerline box (6,6)-(42,42)), the suggested keyshape.
- fist (left, mirrored about x 24 for the right): one closed contour on the
  box x 6..18 / y 6..18 -- finger lobe r4 about (10,10) (apexes (6,10) and
  (10,6)), a smaller thumb lobe r2 about (16,10) on the inner side sharing
  the notch (14,10), straight inner side, a 45 degree bevel (18,14)-(14,18)
  down to the wrist, flat bottom and an r4 heel corner back to x 6.
- forearms: single 45 degree strokes from each wrist; front arm
  (34,18)-(10,42) continuous, rear arm x - y = -4 from (14,18), stopped
  6 diagonal steps each side of the crossing (24,28): (14,18)-(18,22) and
  (30,34)-(38,42). Both arms share the wrist node with their fist (connect).
Extremes: x 6 / 42 on the fist sides, y 6 on the finger apexes, y 42 on
the arm ends. Forearms are strokes, not the image's two-line tubes: an 8-wide
tube pair plus the behind-break does not fit a 36 box (the rear tube's
visible pieces vanish). Lucide `hand-fist` informed the rounded finger mass
with a separate thumb lobe; its finger creases are dropped (no room at 12).
Hands only, no head or torso, so no human figure is marked.

Metric issues (crossed-wrists-with-closed-hands_metrics.json):
- stroke-width (info, trace 2.4): redrawn at stroke 4, gaps budgeted for 4.
- keyshape-short-axis (warn, y fill 86%): fixed without stretching; finger
  apexes sit on y 6 and the arm ends on y 42.
- clearance e0/e2 2.07, e1/e2 6.33, e2/e3 7.72, e3/e4 7.48 (errors): fixed;
  the trace's overlapping fist/arm outlines are rebuilt as two separate fists
  12 apart, and the rear arm ends are 8.49 from the front arm centerline.
- loose-join e3/e1, e4/e1 (info): the trace's short tube ends are replaced;
  each arm now shares its wrist endpoint with its fist and is related.
- hole (error, fist 5.56 inscribed): fixed; each fist interior is 12 on
  centerlines with no interior crease line.
- no-head (warn): not applicable -- the subject is hands and forearms only.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4d17fb6b-b370-4259-a0ce-98903c9aeaff"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1102-crossed-wrists-with-closed-hands/crossed-wrists-with-closed-hands_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                 # mirror axis: the right hand is the left one mirrored
# Left fist on the box x 6..18, y 6..18; the right fist is its mirror.
FINGER_C, FINGER_R = (10, 10), 4     # finger lobe: outer apex (6,10), top apex (10,6)
THUMB_C, THUMB_R = (16, 10), 2       # thumb lobe on the inner side, notch (14,10)
HEEL_C, HEEL_R = (10, 14), 4         # outer bottom corner of the fist
INNER_X, BOTTOM_Y = 18, 18           # inner side and bottom of the fist
WRIST = (14, 18)                     # bevel (18,14)-(14,18) meets the bottom here
ARM_END = (38, 42)                   # 45 degree forearm x - y = -4
REAR_GAP = 6                         # rear arm stops 6 diagonal steps (8.49) off the crossing


def mx(p):
    return (2 * AXIS - p[0], p[1])


class CrossedWristsWithClosedHandsRedraw(Solo48):
    icon_id = "crossed-wrists-with-closed-hands-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ("crossed arms", "crossed fists", "wrists crossed")
    keywords = ("hands", "fists", "wrists", "arms", "crossed", "gesture", "sign", "x")

    def fist(self, side: str, flip: bool) -> None:
        f = mx if flip else (lambda p: p)
        fx, fy = FINGER_C
        tx, ty = THUMB_C
        hx, hy = HEEL_C
        outer_top = (fx - FINGER_R, fy)
        notch = (fx + FINGER_R, fy)
        thumb_in = (tx + THUMB_R, ty)
        bevel = (INNER_X, BOTTOM_Y - (INNER_X - WRIST[0]))
        heel_bottom = (hx, BOTTOM_Y)
        heel_side = (hx - HEEL_R, hy)
        sweep = not flip
        n = f"{side}-"
        self.add_arc(n + "fingers", f(outer_top), f(notch), radius_x=FINGER_R, radius_y=FINGER_R, sweep=sweep)
        self.add_arc(n + "thumb", f(notch), f(thumb_in), radius_x=THUMB_R, radius_y=THUMB_R, sweep=sweep)
        self.add_line(n + "inner", f(thumb_in), f(bevel))
        self.add_line(n + "bevel", f(bevel), f(WRIST))
        self.add_line(n + "bottom", f(WRIST), f(heel_bottom))
        self.add_arc(n + "heel", f(heel_bottom), f(heel_side), radius_x=HEEL_R, radius_y=HEEL_R, sweep=sweep)
        self.add_line(n + "outer", f(heel_side), f(outer_top))
        self.add_contour(n + "fist", n + "fingers", n + "thumb", n + "inner", n + "bevel",
                         n + "bottom", n + "heel", n + "outer", closed=True)

    def build(self) -> None:
        self.fist("left", False)
        self.fist("right", True)

        # Front forearm: right wrist down to the lower left, continuous.
        self.add_line("front-arm", mx(WRIST), mx(ARM_END))
        self.relate("connect", "front-arm", "right-fist")

        # Rear forearm: left wrist down to the lower right, broken around the
        # front arm so it reads as passing behind it.
        cross = (AXIS, WRIST[1] + (AXIS - WRIST[0]))
        self.add_line("rear-arm", WRIST, (cross[0] - REAR_GAP, cross[1] - REAR_GAP))
        self.relate("connect", "rear-arm", "left-fist")
        self.add_line("rear-arm-low", (cross[0] + REAR_GAP, cross[1] + REAR_GAP), ARM_END)
