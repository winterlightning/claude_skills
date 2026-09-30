"""farmer-working-long-handled-hoe (redraw of the new-pipeline traced SVG).

Plan: a stick-figure farmer leaning forward on the left, working a long hoe
that runs down to the ground on the right, on SQUARE (centerline box
(6,6)-(42,42)), the suggested keyshape (fit 1.0 on both axes).
- Farmer: the back rises from the hip up-right to the shoulder, then a short
  vertical neck run; the r5 ring head sits straight above it, exactly GAP (8)
  from the neck on centerlines (4 units of visible ink). The head top is the
  top extreme. Two straight legs splay from the hip in a working stance; the
  back foot is the left extreme, both feet on the ground line (y=42).
- Arm: from the shoulder (below the neck, so it stays clear of the head)
  forward to the hand, which grips the handle partway down.
- Hoe: one 1:1 handle from a short top end above the grip down to the right
  extreme, bending into a short perpendicular blade that points back toward
  the farmer. The handle top is split at the grip so the arm shares an
  endpoint with it; blade and handle stay open, so there is no hole.
Human construction: icon_set/references/human_ref/full_body_ref.png (ring
head, round-ended limbs, a figure reaching forward to an object). No useful
Lucide match for a hoe or a person hoeing.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap was set for stroke 4.
- clearance e0/e2 (head 3.17 from the torso): fixed; the head is exactly 8
  from the neck and more than 8 from the arm and the handle top.
- clearance e1/e2 (legs 7.98 apart): fixed; the two legs share the hip joint
  and splay apart, so they only approach each other at that joint.
- clearance e1/e3 (leg 6.43 from the arm/handle): fixed; the hoe is entirely
  to the right of the front leg, well over 8 away.
- narrow-join e2/e3 (31 deg wedge): fixed; the arm meets the handle at about
  50 deg and the torso/arm/legs meet at open angles.
- hole at [22.3, 9.5] (2.88 wide): fixed; the head ring is r5, so its opening
  is 6 wide.
- hole at [18.2, 18.4] (1.0 wide): fixed; the arm and torso no longer form a
  closed pocket.
- no-head: fixed; the head is a four-arc circle paired with the neck by
  mark_human_figure.
Deliberate changes: the trace's torso leaned straight into a head on the same
diagonal. A diagonal head/neck gap does not certify (comes back `review`),
so the upper torso ends in a short vertical neck with the head straight
above it. The exact 8 gap and r5 head take 18 of the 36 units of height, so
the body below is compact. The trace's two arms were merged into one: a
second arm from the same shoulder to the same handle would form a narrow
wedge. A version bending the farmer over with the head level beside the neck
also validated, but the head read as a loose ball, so it was not kept.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cf3ffa48-69ee-55a9-b0f2-b59ed9778e0e"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1211-farmer-working-long-handled-hoe/"
    "farmer-working-long-handled-hoe_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 6, 6, 42, 42       # SQUARE centerline box
HEAD_R = 5
GAP = 8                                       # head outline -> neck, centerlines
HEAD_C = (19, TOP + HEAD_R)                   # (19, 11)
NECK = (HEAD_C[0], HEAD_C[1] + HEAD_R + GAP)  # (19, 24): straight below the head
SHOULDER = (NECK[0], NECK[1] + 2)             # short vertical neck run
HIP = (12, 32)
BACK_FOOT = (LEFT, BOTTOM)
FRONT_FOOT = (18, BOTTOM)
GRIP_TOP = (28, 22)                           # handle top, clear of head and shoulder
HAND = (31, 25)                               # arm grips the 1:1 handle here
BLADE_TOP = (RIGHT, 36)                       # handle end
BLADE_TIP = (BLADE_TOP[0] - 4, BLADE_TOP[1] + 4)  # perpendicular blade

class FarmerWorkingLongHandledHoeRedraw(Solo48):
    icon_id = "farmer-working-long-handled-hoe-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "agriculture/farming"
    aliases = ("farmer hoeing", "hoeing", "farm worker with hoe")
    keywords = ("farmer", "hoe", "garden", "field", "agriculture", "farming",
                "weeding", "tillage", "person", "work")

    def build(self) -> None:
        cx, cy, r = HEAD_C[0], HEAD_C[1], HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("back", HIP, SHOULDER)
        self.add_line("neck", SHOULDER, NECK)
        self.relate("connect", "back", "neck")
        self.mark_human_figure("farmer", head="head", torso="neck", torso_junction="end")
        self.add_line("leg-back", HIP, BACK_FOOT)
        self.add_line("leg-front", HIP, FRONT_FOOT)
        self.relate("connect", "back", "leg-back")
        self.relate("connect", "back", "leg-front")
        self.relate("connect", "leg-back", "leg-front")
        self.add_line("arm", SHOULDER, HAND)
        self.relate("connect", "arm", "back")
        self.relate("connect", "arm", "neck")

        self.add_line("handle-top", GRIP_TOP, HAND)
        self.add_polyline("hoe", HAND, BLADE_TOP, BLADE_TIP)
        self.relate("connect", "handle-top", "hoe")
        self.relate("connect", "arm", "handle-top")
        self.relate("connect", "arm", "hoe")
