"""boat-pose-upward-reach (redraw of the new-pipeline traced SVG).

Subject: a side-view stick figure in yoga boat pose (navasana), balanced on
the hip at the bottom of a V, legs lifted up-right, torso leaning back
up-left, arms reaching up-forward in front of the head.

Plan: SQUARE (the suggested keyshape), centerline box (6,6)-(42,42).
- hip: the V apex HIP=(19,42) is the bottom extreme.
- legs: one straight line HIP -> FEET=(42,19), 45 deg, right extreme.
- lower torso: HIP -> SHOULDER=(11,30), vector 4*(-2,-3), 33.7 deg back lean
  (the trace leans about 33 deg).
- upper torso / neck: a short vertical stub SHOULDER -> NECK=(11,24), its own
  line joined to the body, so the head sits straight above the neck (the
  "runner lean" construction: vertical neck stub, slanted lower torso).
- head: 4 cardinal arcs, r=5 at (11,11); left extreme x=6, top extreme y=6.
  Head bottom y=16, neck y=24: exactly 8 centerline / 4 ink units.
- arms: one line SHOULDER -> HANDS=(31,10) on x+y=41, parallel to the legs
  (x+y=61, 14.1 apart) as in the pose; 13.4 from the head centre, so the
  head outline clears the arms by 8.4.
Legs and lower torso form one contour (round join at the hip).

Metric issues:
- clearance e0/e2 and e1/e2 (3.6 apart): fixed; the head sits on its own
  neck above the shoulder and the arms leave the shoulder at 45 deg, 8.4 clear.
- head-gap (3.54, need exactly 8): fixed, exactly 8 vertical at the neck.
- hole 2.91 wide: fixed, head r=5 leaves a 6-unit inscribed hole.
- keyshape-short-axis (SQUARE y fill 86%): fixed; head top and hip now sit
  on y=6 and y=42, legs tip on x=42, head on x=6.
- stroke-width (info): redrawn at stroke 4; all gaps measured at 4.
Arms lengthened from (27,14) after a 48 px comparison: the short arm made the
shoulder corner read as an arrowhead.
Changed from the trace on purpose: the arm tip no longer rises above the head
(steeper arms cannot clear an upright head by 8 from a shoulder only 6 below
the neck); the head is upright on a vertical neck rather than on the diagonal
torso axis, because a diagonal exact-8 head gap cannot be certified.
References: icon_set/skills/icon-design/human-reference.md and
icon_set/references/human_ref (circular detached head, single-stroke limbs,
4-unit head gap); no useful Lucide match for a yoga pose.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e0692252-7dbb-4ed1-8ecb-dd659f3bd9b0"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1814-boat-pose-upward-reach/"
    "boat-pose-upward-reach_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_C = (11, 11)
HEAD_R = 5
NECK = (11, 24)          # head bottom 16 + 8
SHOULDER = (11, 30)
HIP = (19, 42)           # SHOULDER + 4 * (2, 3)
FEET = (42, 19)
HANDS = (31, 10)


class BoatPoseUpwardReachRedraw(Solo48):
    icon_id = "boat-pose-upward-reach-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("boat pose", "navasana", "yoga boat pose")
    keywords = ("yoga", "boat pose", "navasana", "pose", "exercise", "fitness",
                "core", "balance", "person", "stretch")

    def build(self) -> None:
        cx, cy, r = HEAD_C[0], HEAD_C[1], HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("legs", FEET, HIP)
        self.add_line("torso-lower", HIP, SHOULDER)
        self.add_contour("body", "legs", "torso-lower")

        self.add_line("torso", SHOULDER, NECK)
        self.relate("connect", "torso", "body")
        self.mark_human_figure("yogi", head="head", torso="torso", torso_junction="end")

        self.add_line("arms", SHOULDER, HANDS)
        self.relate("connect", "arms", "body")
        self.relate("connect", "arms", "torso")
