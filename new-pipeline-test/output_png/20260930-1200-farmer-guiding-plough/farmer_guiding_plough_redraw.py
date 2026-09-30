"""farmer-guiding-plough (redraw of the new-pipeline traced SVG).

Plan: a stooped stick-figure farmer on the left pushing a plough to the right,
on HRECT_M (centerline box (4,10)-(44,38)), the suggested keyshape.
- Farmer: the back rises from a set-back hip to the shoulder, then a short
  level neck run; the r5 ring head sits level beside it, exactly GAP (8)
  from the neck on centerlines (4 units of visible ink). The head top is the
  top extreme and the back foot is the left extreme. Two straight walking
  legs splay from the hip to the ground line.
- Arm: from the shoulder (a vertex before the neck, so it never approaches
  the head) down-forward to the hand, which grips the top of the handle.
- Plough: a steep 1:3 handle from the hand down to the heel on the ground;
  a level beam leaves the handle and runs to the right extreme; the share is
  a quarter arc (r9, centre on the beam's end) sweeping from the beam down
  to a forward tip on the ground (bottom-right extreme). The plough is open
  underneath (heel and tip free), so there is no enclosed hole.
Human construction: icon_set/references/human_ref/full_body_ref.png (ring
head, round-ended limbs; the bin-emptying figure's arm reaching forward-down
to an object). No useful Lucide match for a plough or a ploughman.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap was set for stroke 4.
- keyshape-short-axis (x fills 96%): fixed; the back foot is on x=4 and the
  beam end and share tip are on x=44, with the head top on y=10 and the feet,
  heel and tip on y=38.
- clearance e0/e2 (head 2.48 from body): fixed; the head is exactly 8 from
  the neck and at least 8 from the arm and beam.
- hole at [16.8, 12.7] (1.08 wide): fixed; the head ring is r5, so its
  opening is 6 wide.
- hole at [34.3, 33.5] (1.52 wide): fixed; the handle heel no longer closes
  with the share, so the plough has no pinched hole.
- no-head: fixed; the head is a four-arc circle paired with the neck by
  mark_human_figure.
Deliberate change: the trace's head sat above an upright torso. At 28 units
of height, a head above the neck plus the 8 gap leaves too little body, and
a diagonal head/neck gap comes back `review`. The farmer is therefore drawn
stooped, with the head level beside the neck. This fits the action of
leaning into a plough.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3bc488e9-7d66-4c76-9ac2-7bb53e9db32f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1200-farmer-guiding-plough/"
    "farmer-guiding-plough_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LEFT, TOP, RIGHT, BOTTOM = 4, 10, 44, 38      # HRECT_M centerline box
HEAD_R = 5
GAP = 8                                       # head outline -> neck, centerlines
HIP = (6, 26)
SHOULDER = (14, 15)                           # back rises forward to here
NECK = (SHOULDER[0] + 2, SHOULDER[1])         # short level neck run
HEAD_C = (NECK[0] + GAP + HEAD_R, NECK[1])    # (29, 15): level beside the neck, top = TOP
BACK_FOOT = (LEFT, BOTTOM)
FRONT_FOOT = (14, BOTTOM)
HAND = (20, 26)
BEAM_Y = 29
JOINT = (21, BEAM_Y)                          # handle meets beam (1:3 handle)
HEEL = (24, BOTTOM)
SHARE_R = 9
SHARE_TOP = (RIGHT - SHARE_R, BEAM_Y)
TIP = (RIGHT, BOTTOM)


class FarmerGuidingPloughRedraw(Solo48):
    icon_id = "farmer-guiding-plough-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "agriculture/farming"
    aliases = ("ploughman", "plowman", "farmer plowing", "ploughing")
    keywords = ("farmer", "plough", "plow", "field", "agriculture", "farming",
                "tillage", "person", "work")

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

        self.add_polyline("handle", HAND, JOINT, HEEL)
        self.relate("connect", "arm", "handle")
        self.add_line("beam", JOINT, (RIGHT, BEAM_Y))
        self.relate("connect", "handle", "beam")
        self.add_arc("share", SHARE_TOP, TIP, radius_x=SHARE_R, sweep=False)
        self.relate("connect", "share", "beam")
