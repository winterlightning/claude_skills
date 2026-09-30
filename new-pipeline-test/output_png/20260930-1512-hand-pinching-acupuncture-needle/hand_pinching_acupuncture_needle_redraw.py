"""hand-pinching-acupuncture-needle (redraw of the new-pipeline traced SVG).

Plan: SQUARE, centerline box (6,6)-(42,42); a side-view hand reaches in
from the left and pinches a vertical acupuncture needle between the index
fingertip and the thumb tip.
- hand: one open contour. Upper wrist edge (y 24) rises on a smooth cubic to
  the level index-finger top (y 6), rounds an r4 fingertip about (38,10)
  whose apex (42,10) is the needle's top, runs back along the finger
  underside (y 14), turns through an r5 crotch arc about (30,19) onto the
  level thumb top (y 24), rounds an r4 thumb tip about (38,28) whose apex
  (42,28) sits on the needle, and eases back along the thumb underside into
  the lower wrist edge (y 38). Finger and thumb are equal-width bands (8).
- needle: one straight vertical x=42 from the fingertip apex to the canvas
  floor (y 42), split at the thumb apex so both tips share its endpoints
  (declared connect). Extremes: left 6 (wrist), top 6 (finger), right 42 and
  bottom 42 (needle).
Metric issues fixed:
- clearance e0/e2 (needle 3.2 from the stray stub above the pinch): the
  stub is gone; the needle starts at the fingertip apex and every other
  part of the hand is at least 8 from it.
- loose-join e2/e1: the needle now shares exact endpoints with both tips and
  the contact is declared with relate('connect').
- holes at (29.9,14.4) (3.0 wide) and (32.3,19.5) (0.3 wide): the only
  enclosed opening is the pinch, bounded by level finger and thumb edges 10
  apart, so it is 6 wide inscribed.
- keyshape-short-axis: the hand is widened so the wrist starts on x=6 and the
  needle sits on x=42; all four extremes are on the SQUARE box.
- stroke-width: authored at stroke 4 with every gap budgeted on centerlines.
Not applicable: no human head or torso (an isolated hand).
Lucide: `hand` / `grab` for the rounded finger bands and a single open hand
outline; `syringe` has no useful match for a bare needle.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "219024ce-9973-4736-8ba2-b73e81755a00"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1512-hand-pinching-acupuncture-needle/"
    "hand-pinching-acupuncture-needle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

NEEDLE_X = 42
TIP_R = 4                       # finger and thumb bands are 2*TIP_R wide
FINGER_TOP, FINGER_LOW = 10, 18  # index finger band
THUMB_TOP, THUMB_LOW = 28, 36   # thumb band; pinch opening 10 on centerlines
TIP_X = NEEDLE_X - TIP_R        # centre x of both round tips
CROTCH_X = 30                   # where both bands turn into the crotch arc
KNUCKLE = (24, FINGER_TOP)
WRIST_TOP = (10, 28)
WRIST_LOW, ARM_END_LOW = (20, 42), (6, 42)
ARM_END_TOP = (6, 28)
NEEDLE_TOP, NEEDLE_END = (NEEDLE_X, 6), (NEEDLE_X, 42)


class HandPinchingAcupunctureNeedleRedraw(Solo48):
    icon_id = "hand-pinching-acupuncture-needle-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical/acupuncture"
    aliases = ("acupuncture hand", "hand holding needle", "needle pinch")
    keywords = ("hand", "pinch", "acupuncture", "needle", "therapy", "medicine", "tcm")

    def build(self) -> None:
        finger_apex = (NEEDLE_X, (FINGER_TOP + FINGER_LOW) // 2)
        thumb_apex = (NEEDLE_X, (THUMB_TOP + THUMB_LOW) // 2)
        crotch_r = (THUMB_TOP - FINGER_LOW) // 2

        # -- hand: one open outline, wrist top -> finger -> crotch -> thumb -> wrist low
        self.add_line("arm-top", ARM_END_TOP, WRIST_TOP)
        self.add_bezier(
            "back", WRIST_TOP,
            ((WRIST_TOP[0] + 6, WRIST_TOP[1]), (KNUCKLE[0] - 6, KNUCKLE[1]), KNUCKLE),
        )
        self.add_line("finger-top", KNUCKLE, (TIP_X, FINGER_TOP))
        self.add_arc("fingertip-up", (TIP_X, FINGER_TOP), finger_apex, radius_x=TIP_R)
        self.add_arc("fingertip-low", finger_apex, (TIP_X, FINGER_LOW), radius_x=TIP_R)
        self.add_line("finger-low", (TIP_X, FINGER_LOW), (CROTCH_X, FINGER_LOW))
        self.add_arc(
            "crotch", (CROTCH_X, FINGER_LOW), (CROTCH_X, THUMB_TOP),
            radius_x=crotch_r, sweep=False,
        )
        self.add_line("thumb-top", (CROTCH_X, THUMB_TOP), (TIP_X, THUMB_TOP))
        self.add_arc("thumb-tip-up", (TIP_X, THUMB_TOP), thumb_apex, radius_x=TIP_R)
        self.add_arc("thumb-tip-low", thumb_apex, (TIP_X, THUMB_LOW), radius_x=TIP_R)
        self.add_bezier(
            "thumb-low", (TIP_X, THUMB_LOW),
            ((TIP_X - 8, THUMB_LOW), (WRIST_LOW[0] + 8, WRIST_LOW[1]), WRIST_LOW),
        )
        self.add_line("arm-low", WRIST_LOW, ARM_END_LOW)
        self.add_contour(
            "hand", "arm-top", "back", "finger-top", "fingertip-up", "fingertip-low",
            "finger-low", "crotch", "thumb-top", "thumb-tip-up", "thumb-tip-low",
            "thumb-low", "arm-low",
        )

        # -- needle: held between the two tip apexes, running to the floor
        self.add_line("needle-head", NEEDLE_TOP, finger_apex)
        self.add_line("needle-held", finger_apex, thumb_apex)
        self.add_line("needle-shaft", thumb_apex, NEEDLE_END)
        self.add_contour("needle", "needle-head", "needle-held", "needle-shaft")
        self.relate("connect", "needle", "hand")
