"""camel-pose (redraw of the new-pipeline traced SVG).

Subject: a person in yoga camel pose (Ustrasana), side view facing right --
kneeling with the shins on the floor, hips pushed forward over the knees, the
torso arched backward, the hands on the heels and the head dropped back.

The generated PNG drew a forward-leaning kneel with an enclosed hand loop; the
trace was not a backbend, so the pose is rebuilt from the brief, not the trace.

Plan: SQUARE (centerline box (6,6)-(42,42)). The suggested HRECT_L was fitted
to the trace's forward kneel; a real camel pose with the head hanging back
needs 36 units of height (thigh 20 + arch 16), which HRECT_L's 32 cannot hold
at a 5-radius head, so the keyshape is SQUARE.
- body contour, one stroke: toes -> heel -> knee along the floor (y=42, the
  bottom extreme), knee -> hip straight up the thigh (x=42, the right
  extreme), then tangent-continuous into the back-bend: an R16 quarter arc
  (centre (26,22)) up to the chest top (26,6, the top extreme) and an R15 arc
  (centre (26,21), same vertical tangent at the chest) over the upper back to
  the nape (11,21), where it points straight down.
- neck: standalone 2-unit vertical stub from the nape; the head (r5 circle at
  (11,36), left side = the x=6 extreme) hangs below it, head top 31 - neck end
  23 = exactly 8 on centerlines (4 ink).
- arm: one straight line from the shoulder (17,9), a 9-12-15 lattice point on
  the upper-back arc, down to the heel (28,42), 14.2 from the head centre.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs, minimal anatomy). No useful Lucide match.

Metric issues:
- clearance e0/e1, e0/e3 (head crowding the torso): fixed, the head sits
  exactly 8 centerline units below the neck stub and >= 13 from the arm and
  the foot.
- clearance e1/e2, e1/e3, e2/e3 (arm, leg and floor strokes overlapping at the
  hands and feet): fixed, the traced tangle is replaced by one arm line and one
  shin line meeting at a shared heel endpoint.
- hole 3.44 wide (head circle): fixed, the head is r5 (inscribed 6).
- no-head: fixed, the head is a true circle flagged with mark_human_figure.
- keyshape-short-axis (HRECT_L x filled 69%): fixed by changing keyshape;
  the pose hits all four SQUARE extremes exactly (x 6/42, y 6/42).
- stroke-width (trace 2.13): fixed, drawn at the profile stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "89df2d47-dd44-58e7-a2f9-f8f36667b21c"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1706-camel-pose/camel-pose_raw.svg"
AUTHOR = "claude-opus-5-5"

FLOOR = 42
KNEE = (42, FLOOR)
HIP = (42, 22)             # thigh top; tangent into the back arc
BACK_R = 16                # centre (26,22): hip -> chest top
CHEST = (26, 6)
UPPER_R = 15               # centre (26,21): same vertical tangent at CHEST
SHOULDER = (17, 9)         # (26,21) + (-9,-12), arm root
NAPE = (11, 21)            # leftmost point, tangent straight down
NECK = (11, 23)            # short vertical neck stub
HEEL = (28, FLOOR)
TOES = (24, FLOOR)         # foot runs 4 past the hand; 14.3 from the head centre
HEAD_R = 5
HEAD_C = (11, 36)          # hanging under the neck: 36 - 5 - 23 = exactly 8


class CamelPoseRedraw(Solo48):
    icon_id = "camel-pose-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("ustrasana", "camel yoga pose")
    keywords = ("yoga", "camel", "ustrasana", "backbend", "kneeling", "pose", "stretch")

    def build(self) -> None:
        self.add_line("foot", TOES, HEEL)
        self.add_line("shin", HEEL, KNEE)
        self.add_line("thigh", KNEE, HIP)
        self.add_arc("back", HIP, CHEST, radius_x=BACK_R, sweep=False)
        self.add_arc("upper-back", CHEST, SHOULDER, radius_x=UPPER_R, sweep=False)
        self.add_arc("nape", SHOULDER, NAPE, radius_x=UPPER_R, sweep=False)
        self.add_contour("body", "foot", "shin", "thigh", "back", "upper-back", "nape")

        # Standalone vertical neck stub: the exact 8-unit head gap certifies
        # only straight-vs-cardinal-arc.
        self.add_line("neck", NAPE, NECK)
        self.relate("connect", "neck", "body")

        cx, cy, r = HEAD_C[0], HEAD_C[1], HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)
        self.mark_human_figure("yogi", head="head", torso="neck", torso_junction="end")

        self.add_line("arm", SHOULDER, HEEL)
        self.relate("connect", "arm", "body")
