"""bridge-pose (redraw of the new-pipeline traced SVG).

Plan: a side-view yoga bridge, low and wide as in the image, on CIRCLE
(centerline radius 20 about (24,24)).
- head: r5 circle of four cardinal quarter arcs centred (11,30), level with
  the floor line y 30 (6-wide inscribed hole).
- neck: a 1-long level line from the shoulder (25,30) to (24,30), exactly 8
  (centerline) right of the head outline, 4 visible. It is the flagged torso
  (junction "end").
- body: one closed contour, the lifted wedge of the pose:
  - arm: flat on the floor y 30 from the shoulder to the heel (42,30),
    the hands at the heels as in the image.
  - shin: vertical x 42 from the heel up to y 16.
  - knee: r3 arc centred (39,16) up to the knee top (39,13). Its centre is
    17 from (24,24), so the arc touches the CIRCLE radius 20 exactly.
  - back: one straight line (about 50 degrees) from the knee to the shoulder
    (shoulders on the floor, hips lifted, torso and thigh in line).
- foot: a short toe line from the heel to (43,30), connected.
The figure spans y 13..35 on centerlines, balanced about the centre.
Lucide: no local yoga/bridge original; built with Lucide's figure rules
(circle head, straight round-ended limbs, one small knee radius).
Human reference: icon_set/references/human_ref/full_body_ref.png (circle
head, simple round-ended limbs). The head lies on the floor off the torso
axis on purpose: that neck bend is the pose.

Keyshape: the suggested HRECT_M was drawn first and rejected. Its exact
y fit (10..38) forces a 28-tall figure, so with the 8 head gap and the 8
hand-to-shin gap the back rises at 60+ degrees and the drawing read as a
shark fin, not a bridge. CIRCLE only needs one point on radius 20 (the
knee), which keeps the reference's low 3:1 silhouette.

Metric issues (bridge-pose_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (HRECT_M y fill 47%): fixed by changing the keyshape
  to CIRCLE (see above) instead of stretching the pose 2.12x on y.
- clearance e0/e1 (head 3.13 from the shoulder corner): the head now sits
  exactly 8 on centerlines from the neck (level, certified by the gate);
  the back leaves the shoulder away from the head.
- hole at (7.0,27.6) (1.89 wide): the head is an r5 circle, 6 inscribed.
  The body wedge is a closed hole of at least 6 as well.
- no-head (warn): the head is a true circle, flagged with
  mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ed6cb660-23da-5c6d-9d87-7413118cab56"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1951-bridge-pose/bridge-pose_raw.svg"
AUTHOR = "claude-opus-5-5"

FLOOR = 30                       # floor line: arm, heel, head centre height
HEAD_C, HEAD_R = (11, 30), 5     # head x 6..16; 19.3 from (24,24) at most
NECK = (24, 30)                  # 8 right of the head outline, level
SHOULDER = (25, 30)              # back, arm and neck meet here
KNEE_C, KNEE_R = (39, 16), 3     # 17 from (24,24): arc reaches radius 20
SHIN_X = KNEE_C[0] + KNEE_R      # 42
TOE_X = 43


class BridgePoseRedraw(Solo48):
    icon_id = "bridge-pose-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("bridge pose", "setu bandhasana", "glute bridge", "yoga bridge")
    keywords = ("yoga", "bridge", "pose", "exercise", "fitness", "stretch", "workout", "person")

    def build(self) -> None:
        hx, hy = HEAD_C
        r = HEAD_R
        self.add_arc("head-tl", (hx - r, hy), (hx, hy - r), radius_x=r)
        self.add_arc("head-tr", (hx, hy - r), (hx + r, hy), radius_x=r)
        self.add_arc("head-br", (hx + r, hy), (hx, hy + r), radius_x=r)
        self.add_arc("head-bl", (hx, hy + r), (hx - r, hy), radius_x=r)
        self.add_contour("head", "head-tl", "head-tr", "head-br", "head-bl", closed=True)

        kx, ky = KNEE_C
        self.add_line("arm", SHOULDER, (SHIN_X, FLOOR))
        self.add_line("shin", (SHIN_X, FLOOR), (SHIN_X, ky))
        self.add_arc("knee", (SHIN_X, ky), (kx, ky - KNEE_R), radius_x=KNEE_R, sweep=False)
        self.add_line("back", (kx, ky - KNEE_R), SHOULDER)
        self.add_contour("body", "arm", "shin", "knee", "back", closed=True)

        self.add_line("foot", (SHIN_X, FLOOR), (TOE_X, FLOOR))
        self.relate("connect", "body", "foot")

        # Neck: short level run from the shoulder, its own line.
        self.add_line("neck", SHOULDER, NECK)
        self.relate("connect", "body", "neck")
        self.mark_human_figure("person", head="head", torso="neck", torso_junction="end")
