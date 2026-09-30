"""athlete-running-right (redraw of the new-pipeline traced SVG).

Plan: right-facing stick runner on SQUARE (centerline box (6,6)-(42,42)),
rebuilt on the 48 grid from the trace's pose, not its coordinates.
- head: 4-cardinal-arc circle, r4, centre (HX,10); its top is the y=6 extreme.
- neck: short vertical stub (HX,22)-(HX,24) straight under the head, so the
  head outline sits exactly 8 centerline units above the torso (4-unit ink
  gap, human-reference.md); the lower torso then slants back to a set-back hip,
  which gives the forward lean of the trace.
- arms branch at the shoulder node (bottom of the stub), never at the neck:
  rear arm up-back to a raised elbow then down to the hand; front arm down to
  the elbow and up to a raised fist, whose knuckles are the x=42 extreme.
- legs from the hip: rear leg continues the torso line to a knee, a long shin
  back to the heel (the x=6 extreme) and a short toe down to y=42; the front
  leg lifts the knee forward and drops the shin to the y=42 floor.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); no useful Lucide match for a runner.

Metric issues fixed:
- clearance e0/e2, e0/e3, head-gap: the head is detached exactly 8 on
  centerlines from the neck and every arm point stays 10+ from its outline.
- clearance e2/e3: the rear shoulder-arm and the front arm no longer run
  side by side; both leave one shared shoulder node (declared connect).
- clearance e1/e3: the front elbow sits 8.7+ from the front thigh.
- hole (3.2 wide head): the head is r4, an 8-wide hole on centerlines.
- keyshape-short-axis: the pose is widened to touch x=6 (rear heel) and
  x=42 (front fist) exactly, as well as y=6 (head) and y=42 (feet).
- stroke-width: redrawn at stroke 4 with 8-unit clearances throughout.
The trace's front arm floated free of the torso; it is attached here.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "47d26a02-2221-453b-a560-39c0733c3bec"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1824-athlete-running-right/"
    "athlete-running-right_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 30               # head / neck axis
HEAD_R = 4
HEAD_CY = 10          # centerline top at y=6
NECK = (HX, 22)       # HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 24)
HIP = (24, 32)
REAR_ELBOW, REAR_HAND = (20, 21), (12, 27)
FRONT_ELBOW, FRONT_HAND = (35, 27), (42, 19)
REAR_KNEE, REAR_HEEL, REAR_TOE = (17, 36), (6, 39), (8, 42)
FRONT_KNEE, FRONT_FOOT = (34, 36), (32, 42)


class AthleteRunningRightRedraw(Solo48):
    icon_id = "athlete-running-right-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("runner", "sprinter", "jogger")
    keywords = ("athlete", "running", "run", "sprint", "jogging", "race", "right")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("lower-torso", SHOULDER, HIP)
        self.mark_human_figure("runner", head="head", torso="torso", torso_junction="start")

        self.add_polyline("rear-arm", SHOULDER, REAR_ELBOW, REAR_HAND)
        self.add_polyline("front-arm", SHOULDER, FRONT_ELBOW, FRONT_HAND)
        self.add_polyline("rear-leg", HIP, REAR_KNEE, REAR_HEEL, REAR_TOE)
        self.add_polyline("front-leg", HIP, FRONT_KNEE, FRONT_FOOT)

        for a, b in [
            ("torso", "lower-torso"),
            ("torso", "rear-arm"), ("torso", "front-arm"),
            ("lower-torso", "rear-arm"), ("lower-torso", "front-arm"),
            ("rear-arm", "front-arm"),
            ("lower-torso", "rear-leg"), ("lower-torso", "front-leg"),
            ("rear-leg", "front-leg"),
        ]:
            self.relate("connect", a, b)
