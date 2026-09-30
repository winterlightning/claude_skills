"""hands-cupping-a-profile-head (redraw of the new-pipeline traced SVG).

Subject: a right-facing human head in profile held between two cupped
hands that rise on either side of it (self care, mental health support).

Plan: SQUARE (the suggested keyshape; centerline box (6,6)-(42,42)).
- head: one open contour. Back of neck at x=20 rises into an r7 skull
  (centre (22,13), top y=6); the forehead runs straight on as the nose
  ridge to the nose tip (32,17) and the jaw returns in one straight line
  to the front of the neck at x=28. Both neck ends sit on y=21, 8 apart.
- hands: one open contour each, mirrored about x=24. Outer palm edge rises
  from the wrist to an r4 fingertip (outer edge on x=6 / x=42), the inner
  edge falls and sweeps in under the head to the inner wrist at x=20 / 28.
Extremes: x=6 / x=42 finger outer edges, y=6 skull top, y=42 wrist ends.
References: the generated PNG (head above, cupped hands either side,
open neck); human-reference.md for the head (an anatomical profile with
its own neck, not a detached stick-figure head, so no mark_human_figure).
Lucide has no hands-with-head icon; lucide/hand-heart and hand-helping
informed only the one-stroke palm with a rounded fingertip end.

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4 with every gap between
  distinct parts budgeted at >= 8 on centerlines.
- clearance e0/e1 (neck 3.2 from the left hand): fixed, the head ends at
  y=21, above the fingertips (apex y=24), so the neck ends clear the
  fingertip and the palm sweep by >= 8.
- clearance e0/e2 (jaw 3.5 from the right hand): fixed, same restaging;
  the head is shifted 2 left of the axis so the nose tip and the jaw line
  stay >= 8 from the right fingertip.
- clearance e1/e2 (wrists 4.19 apart): fixed, inner wrists on x=20 and
  x=28, 8 apart on centerlines.
Deliberate change: the head is drawn smaller and higher than the trace
(the trace overlapped the head's neck with the fingertips by ~10 units,
which the 8-unit clearance cannot hold on 36 units of height), and the
nose/lip/chin steps became one nose wedge, which at stroke 4 is the only
face detail that stays legible. An open single-stroke palm variant read
cleaner but lost the hand outlines of the reference, so it was rejected.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "efd5cbb3-73a1-456c-9d82-fa7470f26ad4"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1512-hands-cupping-a-profile-head/hands-cupping-a-profile-head_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
SKULL_C, SKULL_R = (22, 13), 7
NECK_BACK, NECK_FRONT, NECK_END = 20, 28, 21
NOSE_TIP = (32, 17)

TIP_R, TIP_Y = 4, 28          # fingertip half circle centre height
FINGER_OUT = 18               # |x - AXIS| of the finger's outer edge (x=6)
WRIST_OUT, WRIST_IN = 13, 4   # |x - AXIS| of the wrist ends
WRIST_Y = 42


class HandsCuppingAProfileHeadRedraw(Solo48):
    icon_id = "hands-cupping-a-profile-head-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/health"
    aliases = ("self care", "mental health care", "mind care", "cared head")
    keywords = ("hands", "cupping", "head", "profile", "self care",
                "mental health", "support", "care", "mind", "wellbeing")

    def build(self) -> None:
        # Head: back of neck, skull, forehead, nose, lip, jaw into front neck.
        cx, cy = SKULL_C
        left, right, top = cx - SKULL_R, cx + SKULL_R, cy - SKULL_R
        self.add_bezier("neck-back", (NECK_BACK, NECK_END),
                        ((NECK_BACK, 18), (left, 17), (left, cy)))
        self.add_arc("skull-back", (left, cy), (cx, top), radius_x=SKULL_R)
        self.add_arc("skull-front", (cx, top), (right, cy), radius_x=SKULL_R)
        self.add_line("nose-ridge", (right, cy), NOSE_TIP)
        self.add_line("jaw", NOSE_TIP, (NECK_FRONT, NECK_END))
        self.add_contour("head", "neck-back", "skull-back", "skull-front",
                         "nose-ridge", "jaw")

        # Hands: mirrored cupped palms, each wrist -> fingertip -> wrist.
        for side, name in ((-1, "left"), (1, "right")):
            def p(dx, y):
                return (AXIS + side * dx, y)
            fin_in = FINGER_OUT - 2 * TIP_R
            outer = (p(WRIST_OUT, WRIST_Y),
                     ((p(WRIST_OUT, 36), p(FINGER_OUT, 36), p(FINGER_OUT, TIP_Y))))
            inner = (p(fin_in, TIP_Y),
                     ((p(fin_in, 32), p(WRIST_IN, 31), p(WRIST_IN, 37))))
            self.add_bezier(f"{name}-palm-out", outer[0], outer[1])
            self.add_arc(f"{name}-tip", p(FINGER_OUT, TIP_Y), p(fin_in, TIP_Y),
                         radius_x=TIP_R, sweep=side < 0)
            self.add_bezier(f"{name}-palm-in", inner[0], inner[1])
            self.add_line(f"{name}-wrist-in", p(WRIST_IN, 37), p(WRIST_IN, WRIST_Y))
            self.add_contour(f"{name}-hand", f"{name}-palm-out", f"{name}-tip",
                             f"{name}-palm-in", f"{name}-wrist-in")
