"""bridge-pose (redraw of the new-pipeline traced SVG).

Plan: one stick figure lying face-up in bridge pose (setu bandhasana), seen
from the side, on HRECT_M (centerline box (4,10)-(44,38)), the metrics'
suggested keyshape.
- floor line y=34: the shoulders, the arm along the floor and the planted
  foot all lie on it, so the ground reads without a separate mat stroke.
- head: an r4 ring at (8,34), resting on the floor level with the neck. The
  body starts with a 3-long level neck run (20,34)-(23,34), exactly 8 on
  centerlines (4 ink) from the ring, so the human head gap certifies.
- back: one cubic from the shoulder (23,34) that rises and flattens into the
  knee (40,10). Its controls sit on the knee's row, so the apex is the knee
  itself and the top extreme is exact. This is the arched torso-and-thigh
  sweep of the generated image.
- leg: the shin folds back from the knee to the heel (38,34), and a foot
  runs forward to the toe (44,34).
- arm: one straight stroke along the floor from the shoulder to the hand
  (30,34), exactly 8 short of the heel.
Extremes: left 4 (head), right 44 (toe), top 10 (knee), bottom 38 (head).
The body is one open contour (neck, back, shin, foot), the arm branches at
the shoulder node, and the head is its own ring: 3 strokes.
References: icon_set/references/human_ref (ring head, single-stroke limbs,
detached head with a 4-unit ink gap beside a level neck run). No useful
Lucide match: Lucide has no yoga or lying figure.

Metric issues fixed:
- clearance e0/e1, e0/e2, e1/e2 (1.8-6.2: doubled arm strokes and the back
  fused at the shoulder) and narrow-join e0/e1 (30.8 deg wedge): one arm
  stroke along the floor. It leaves the shoulder node at a wide angle to the
  back, and the join is a shared endpoint.
- clearance e0/e3, e0/e4, e1/e3, e1/e4, e2/e3 (2.4-6.4: the second leg and
  foot ticks crowding the hands and the knee): one leg only. The hand ends
  exactly 8 from the heel, and the shin and back share the knee node.
- clearance e0/e5, e1/e5, e2/e5 and head-gap e5 (1.6-2.7: the head jammed
  against the shoulder): the head sits level beside the neck run at exactly
  8 on centerlines.
- hole [27.7,24.2] (4.87) and hole [6.8,27.4] (1.56): no enclosed openings
  remain. The arm/heel gap keeps the space under the arch open, and the
  shoulder wedge is gone.
- loose-join e0/e2, e1/e2, e4/e2 (1.2-1.4 short): every contact is a shared
  integer node declared with relate("connect").
- keyshape-short-axis (y filled 46%): the knee is at y=10 and the head
  bottom at y=38, so all four HRECT_M extremes are exact. The pose is taller
  than a real bridge; the back arch and the long shin absorb the stretch.
- stroke-width (2.61 trace): redrawn at stroke 4 with every gap budgeted
  at 8.
Dropped: the second leg and the second arm. At 8 spacing they cannot sit
beside the first ones inside 28 units of height.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ed6cb660-23da-5c6d-9d87-7413118cab56"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1709-bridge-pose/bridge-pose_raw.svg"
AUTHOR = "claude-opus-5-5"

FLOOR = 34
HEAD_R = 4
GAP = 8                          # head outline to neck, on centerlines
HEAD_C = (8, FLOOR)
NECK = (HEAD_C[0] + HEAD_R + GAP, FLOOR)
SHOULDER = (NECK[0] + 3, FLOOR)
KNEE = (40, 10)
HEEL = (38, FLOOR)
TOE = (44, FLOOR)
HAND = (HEEL[0] - GAP, FLOOR)


class BridgePoseRedraw(Solo48):
    icon_id = "bridge-pose-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("setu bandhasana", "glute bridge", "hip lift")
    keywords = ("yoga", "bridge", "pose", "backbend", "exercise", "stretch", "fitness")

    def build(self) -> None:
        cx, cy = HEAD_C
        r = HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("neck", NECK, SHOULDER)
        self.add_bezier("back", SHOULDER, ((29, 25), (33, KNEE[1]), KNEE))
        self.add_line("shin", KNEE, HEEL)
        self.add_line("foot", HEEL, TOE)
        self.add_contour("body", "neck", "back", "shin", "foot")
        self.add_line("arm", SHOULDER, HAND)
        self.mark_human_figure("person", head="head", torso="neck", torso_junction="start")

        for a, b in (
            ("neck", "back"), ("back", "shin"), ("shin", "foot"),
            ("neck", "arm"), ("back", "arm"),
        ):
            self.relate("connect", a, b)
