"""briefcase-carrying-hailing-person (redraw of the new-pipeline traced SVG).

Plan: a front-facing stick figure hailing with the left arm, carrying a
briefcase in the right hand, on VRECT_L (centerline box (8,4)-(40,44)).
- head: 4-cardinal-arc circle r4 at (HX,8); top touches y=4.
- torso: vertical from the neck (HX,20) to the hip; the neck is exactly 8
  centerline units under the head outline (4-unit ink gap, human-reference.md).
- arms: three connected lines. The raised arm runs level off the neck to the
  elbow, then diagonally up to the hand in the (8,4) corner, keeping 12+ from
  the head centre (8+ from the head outline). The lowered arm slopes
  down-right and grips the middle of the briefcase lid (shared node).
- briefcase: 10x10 rounded box (r2), right wall on the x=40 extreme. A 10-unit
  box is the smallest that keeps a 6-unit hole; there is no room for a
  separate handle loop (see below).
- legs: rear leg diagonal down-left to (14,44); near leg straight down, 8 from
  the briefcase wall (a splayed near leg would run into the case).
Keyshape: metrics suggested VRECT_M (28 wide) but the budget is head 8 +
arm clearance 12 on the left, and torso-to-case 8 + case 10 on the right: 34+
units, so VRECT_L (32 wide, the runner-up candidate, score 1.17) is used and
the hailing hand sits at the top-left corner.
Reference: icon_set/references/human_ref (circular detached head, single-stroke
limbs); Lucide `briefcase` for the rounded case with a centred handle.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted at 8.
- keyshape-short-axis: all four extremes sit exactly on the VRECT_L box.
- clearance e0/e2, e0/e4 (head vs torso/shoulders 4): neck now 8 below the head.
- clearance e1/e2, e1/e4, e1/e5, e2/e3 (case vs legs/arm/handle): case moved 8
  clear of torso and near leg; the arm ends on the lid node (declared connect).
- clearance e2/e4, e2/e5 (arm/leg vs torso near joints): arms leave the neck
  level, legs split at the hip with the near leg on the torso axis.
- hole x3 (head 2.9, arm/torso wedge 4.8, handle 2.4): head r4 ring is an
  exempt ring, the arm/torso wedge is open, and the case hole is 6 inscribed.
Not kept: the briefcase handle loop. Any closed handle needs a 10x10 loop for
a 6-unit hole (as tall as the case), and a grip stub leaves the arm within 8 of
the lid (internal-spacing pinch), so the hand grips the lid centre directly.
- no-head: head drawn as a true circle and flagged with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "459ca9bc-41c3-44a7-bd18-4322e40df660"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1912-briefcase-carrying-hailing-person/"
    "briefcase-carrying-hailing-person_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 22          # head / torso axis
HEAD_R = 4
HEAD_CY = 8      # head top at y=4
NECK_Y = 20      # HEAD_CY + HEAD_R + 8
HIP_Y = 31
HAND_UP = (8, 4)
ELBOW = (13, NECK_Y)
CASE = dict(left=30, right=40, top=30, bottom=40, r=2)
REAR_FOOT = (14, 44)
NEAR_FOOT = (HX, 44)


class BriefcaseCarryingHailingPersonRedraw(Solo48):
    icon_id = "briefcase-carrying-hailing-person-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("businessman hailing", "commuter hailing a taxi")
    keywords = ("person", "briefcase", "hail", "taxi", "wave", "business", "commuter")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        neck = (HX, NECK_Y)
        hip = (HX, HIP_Y)
        self.add_line("torso", neck, hip)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")

        L, R, T, B, cr = CASE["left"], CASE["right"], CASE["top"], CASE["bottom"], CASE["r"]
        mid = (L + R) // 2
        grip = (mid, T)
        # Separate lines, not one polyline: the head clearance proof uses each
        # contour's control hull, and a bent polyline's hull reaches the head.
        self.add_line("forearm-up", HAND_UP, ELBOW)
        self.add_line("shoulder", ELBOW, neck)
        self.add_line("arm-down", neck, grip)
        self.relate("connect", "forearm-up", "shoulder")
        self.relate("connect", "shoulder", "torso")
        self.relate("connect", "shoulder", "arm-down")
        self.relate("connect", "arm-down", "torso")

        # Briefcase: closed rounded box, split at the handle on the lid.
        self.add_line("case-top-r", (mid, T), (R - cr, T))
        self.add_arc("case-tr", (R - cr, T), (R, T + cr), radius_x=cr, sweep=True)
        self.add_line("case-right", (R, T + cr), (R, B - cr))
        self.add_arc("case-br", (R, B - cr), (R - cr, B), radius_x=cr, sweep=True)
        self.add_line("case-bottom", (R - cr, B), (L + cr, B))
        self.add_arc("case-bl", (L + cr, B), (L, B - cr), radius_x=cr, sweep=True)
        self.add_line("case-left", (L, B - cr), (L, T + cr))
        self.add_arc("case-tl", (L, T + cr), (L + cr, T), radius_x=cr, sweep=True)
        self.add_line("case-top-l", (L + cr, T), (mid, T))
        self.add_contour(
            "case", "case-top-r", "case-tr", "case-right", "case-br", "case-bottom",
            "case-bl", "case-left", "case-tl", "case-top-l", closed=True,
        )
        self.relate("connect", "arm-down", "case")

        self.add_line("rear-leg", hip, REAR_FOOT)
        self.add_line("near-leg", hip, NEAR_FOOT)
        self.relate("connect", "rear-leg", "torso")
        self.relate("connect", "near-leg", "torso")
        self.relate("connect", "rear-leg", "near-leg")
