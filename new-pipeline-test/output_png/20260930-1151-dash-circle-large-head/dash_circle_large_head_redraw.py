"""dash-circle-large-head (redraw of the new-pipeline traced SVG).

Subject (from choice.json and the generated PNG): a stick figure dashing to
the right under a large hollow circular head.

Plan: right-facing stick runner on VRECT_M (centerline box (10,4)-(38,44)),
rebuilt on the 48 grid from the trace's pose, not its coordinates.
- keyshape: the metrics suggest SQUARE, but SQUARE fills only 73% of x and
  needs a 1.36 stretch; VRECT_M (score 0.96) fits the 0.73 aspect with a 1.05
  stretch, and its 40-unit height pays for the large head plus the 8-unit
  neck gap while leaving the legs a real stride.
- head: 4-cardinal-arc circle, r5 (the "large head", 10 wide on a 28-wide
  figure), centre (HX,9); its top is the y=4 extreme.
- neck: short vertical stub (HX,22)-(HX,24) straight under the head, so the
  head outline sits exactly 8 centerline units above the torso (4-unit ink
  gap, human-reference.md); the lower torso then slants back on a 3-4-5 line
  to a set-back hip, giving the trace's forward lean.
- arms branch at the shoulder node (bottom of the stub), never at the neck:
  rear arm back to a raised elbow and down to the hand; front arm down to the
  elbow and up to the fist, whose knuckles are the x=38 extreme.
- legs from the hip: rear leg to a knee and back to the foot (the x=10
  extreme); front leg lifts the knee forward and drops to the y=44 floor.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); construction follows the validated
athlete-running-right redraw (neck stub then leaning torso). No useful Lucide
match for a runner.

Metric issues fixed:
- head-gap, clearance e0/e2: the head is detached exactly 8 on centerlines
  from the neck, on the torso's vertical neck axis.
- clearance e0/e1, e0/e4: every arm point stays 9+ from the head outline.
- clearance e1/e2, e2/e4: the arms, which floated beside the torso in the
  trace, now leave one shared shoulder node (declared connect).
- clearance e1/e4: the two arms only meet at that shoulder node.
- clearance e3/e4: the front elbow sits 9.8 from the front thigh.
- keyshape-short-axis: switched to VRECT_M and touched all four extremes
  exactly (head y=4, front foot y=44, rear foot x=10, front fist x=38).
- stroke-width: redrawn at stroke 4 with 8-unit clearances throughout.
The t-junction e2/e3 (leg off the torso) is kept as the shared hip node.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "edd1a1a5-5b11-4ec8-9855-ec307205ccb2"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1151-dash-circle-large-head/"
    "dash-circle-large-head_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 28               # head / neck axis
HEAD_R = 5
HEAD_CY = 9           # centerline top at y=4
NECK = (HX, 22)       # HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 24)
HIP = (22, 32)        # 3-4-5 lean back from the shoulder
REAR_ELBOW, REAR_HAND = (20, 21), (13, 27)
FRONT_ELBOW, FRONT_HAND = (33, 28), (38, 23)
REAR_KNEE, REAR_FOOT = (17, 38), (10, 42)
FRONT_KNEE, FRONT_FOOT = (30, 38), (26, 44)


class DashCircleLargeHeadRedraw(Solo48):
    icon_id = "dash-circle-large-head-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("dash", "runner", "sprinter")
    keywords = ("dash", "running", "run", "sprint", "stick figure", "large head", "circle head")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("lower-torso", SHOULDER, HIP)
        self.mark_human_figure("dasher", head="head", torso="torso", torso_junction="start")

        self.add_polyline("rear-arm", SHOULDER, REAR_ELBOW, REAR_HAND)
        self.add_polyline("front-arm", SHOULDER, FRONT_ELBOW, FRONT_HAND)
        self.add_polyline("rear-leg", HIP, REAR_KNEE, REAR_FOOT)
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
