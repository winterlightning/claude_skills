"""briefcase-carrying-hailing-person (redraw of the new-pipeline traced SVG).

Plan: upright stick figure on VRECT_L (centerline box (8,4)-(40,44)).
- head: 4-cardinal-arc circle, r4, centre (HX,8); its top is the y=4 extreme.
- torso: a 2-long vertical neck stub from (HX,20), exactly 8 centerline units
  under the head outline (4-unit ink gap, human-reference.md), then the waist
  runs straight down to the hip.
- hailing arm (right): from the shoulder it rises to an elbow out at the side,
  then the forearm reaches up to the hand at (40,4), the x=40 and y=4 extreme.
  Both segments stay 8+ from the head outline.
- carrying arm (left): level from the shoulder to an elbow above the case,
  then straight down to the handle point at the middle of the case top.
- briefcase: a landscape 10x8 box (8,30)-(18,38), split at the handle point so
  the hand shares an endpoint with it; its left side is the x=8 extreme.
- legs: the standing leg drops straight from the hip (it must, to keep 8+ from
  the case corner); the other leg steps out to the right. Both feet on y=44.
Reference: icon_set/references/human_ref (circular head, single-stroke
round-ended limbs); Lucide `briefcase` for the landscape case with a top grip.

Keyshape: metrics suggested VRECT_M, but at stroke 4 the figure cannot fit 28
units of width: the hailing hand must sit 12+ from the head centre and the case
8+ from the torso. VRECT_L gives the 32 needed and a landscape case.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8 centerline.
- stroke-count (10 vs 6): rebuilt as 6 parts: head, torso, two arms, case, legs.
- keyshape-short-axis: case side (x=8) and hailing hand (x=40) reach the box.
- clearance e0/e2, e0/e4, e0/e6, e0/e7, e0/e8 and no-head: the head is a real
  circle over a neck stub at exactly 8; both arms branch 2 lower and keep 8+.
- clearance e1/e2, e1/e7, e1/e9, e2/e3, e2/e7, e2/e9, e3/e5, e3/e9, e7/e9: the
  case moved clear of the torso and legs (9 from the standing leg), the hand
  meets it at one shared node, and the trace's handle loop was dropped.
- loose-join e2/e7, e3/e7, e4/e7, e5/e7, e6/e7, e7/e8 and narrow-join e4/e6:
  all limbs share exact shoulder / hip / handle nodes with relate("connect").
- holes: the head is an r4 ring (small-circle exemption); the only other
  enclosed pocket is the case interior, 10x8 on centerlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "459ca9bc-41c3-44a7-bd18-4322e40df660"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1715-briefcase-carrying-hailing-person/"
    "briefcase-carrying-hailing-person_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 27               # head / torso axis
HEAD_R = 4
HEAD_CY = 8           # centerline top y=4
NECK = (HX, HEAD_CY + HEAD_R + 8)
SHOULDER = (HX, NECK[1] + 2)
HIP = (HX, 30)
HAIL_ELBOW, HAIL_HAND = (38, 18), (40, 4)
CASE_L, CASE_R, CASE_T, CASE_B = 8, 18, 30, 38
GRIP = ((CASE_L + CASE_R) // 2, CASE_T)
CARRY_ELBOW = (GRIP[0], SHOULDER[1])
STAND_FOOT, STEP_FOOT = (HX, 44), (35, 44)


class BriefcaseCarryingHailingPersonRedraw(Solo48):
    icon_id = "briefcase-carrying-hailing-person-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("hailing a taxi", "commuter", "business traveller")
    keywords = ("person", "briefcase", "hail", "taxi", "wave", "business", "travel", "commute")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

        self.add_polyline("hail-arm", SHOULDER, HAIL_ELBOW, HAIL_HAND)
        self.add_polyline("carry-arm", SHOULDER, CARRY_ELBOW, GRIP)
        for arm in ("hail-arm", "carry-arm"):
            self.relate("connect", arm, "torso")
            self.relate("connect", arm, "waist")
        self.relate("connect", "hail-arm", "carry-arm")

        self.add_polyline(
            "case", GRIP, (CASE_R, CASE_T), (CASE_R, CASE_B), (CASE_L, CASE_B),
            (CASE_L, CASE_T), closed=True,
        )
        self.relate("connect", "carry-arm", "case")

        self.add_line("stand-leg", HIP, STAND_FOOT)
        self.add_line("step-leg", HIP, STEP_FOOT)
        self.relate("connect", "stand-leg", "waist")
        self.relate("connect", "step-leg", "waist")
        self.relate("connect", "step-leg", "stand-leg")
