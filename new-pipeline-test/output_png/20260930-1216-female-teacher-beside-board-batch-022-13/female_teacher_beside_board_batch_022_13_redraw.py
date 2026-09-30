"""female-teacher-beside-board-batch-022-13 (redraw of the new-pipeline traced SVG).

Plan: HRECT_L (centerline box (4,8)-(44,40)). The metrics suggest HRECT_M (score
1.22) but its 28-unit height cannot hold a r5 head (6 inscribed hole), the exact
8-unit neck gap, a torso and legs; HRECT_L is the metrics' runner-up (1.15) and
fills x exactly (fill 1.0, no stretch), so every extreme lands on its box.
- teacher (left, facing the board) on the axis x=HX: 4-arc circle head r5 whose
  top is the y=8 extreme; torso from the neck, exactly 8 centerline units under
  the head outline (4-unit ink gap, human-reference.md), split at the shoulder,
  down to the hip; mirrored inverted-V legs, left foot the x=4 extreme, both
  feet the y=40 extreme.
- pointing arm: one straight stroke from the shoulder up-right toward the
  board; the hand stops 8 short of the board wall and stays >8 from the head.
- board: one closed rectangle, square corners like the reference; its right
  wall is the x=44 extreme, top level with the head, bottom near the waist.
Dropped: the hanging left arm (it cannot clear the left leg by 8 inside a
figure 12 wide) and any gender marker (the stick-figure rules omit it; the
subject name carries it).
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
single-stroke limbs). Lucide `presentation` informs the plain board rectangle.
Deliberate asymmetry: a side scene, teacher left, board right.

Metric issues fixed:
- stroke-width 2.55 -> redrawn at stroke 4 with every gap budgeted for it.
- stroke-count 9 (budget 6) -> 6 parts: head, torso, waist, legs, arm, board.
- keyshape-short-axis (x filled 97%): on HRECT_L x spans exactly 4..44 and y 8..40.
- clearance e0/e5, e0/e6, e0/e7, e0/e8 and human head gap 2.4: neck exactly 8
  under the head outline; the arm starts lower and clears the head by >8.
- clearance e0/e3, e1/e3, e1/e7 (arm tip vs head and board): hand 8 left of
  the board wall and >13 from the head centre.
- clearance e2/e3, e2/e4, e2/e6, e2/e7, e2/e8 (legs vs arms, leg pair): one
  arm only, legs share the hip and diverge; all distinct pairs >= 8.
- hole 1.9 (head): head r5 gives a 6 inscribed hole; board hole is 14.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "46825186-2cd0-49e4-9bcb-dfcef97654be"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1216-female-teacher-beside-board-batch-022-13/"
    "female-teacher-beside-board-batch-022-13_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 10            # teacher axis
HEAD_R = 5
HEAD_CY = 13       # head top on y=8
NECK_Y = 26        # HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 28)
HIP = (HX, 33)
LEG_SPREAD = 6
FOOT_Y = 40
HAND = (18, 24)
BOARD = dict(left=26, top=10, right=44, bottom=28)


def _circle(icon, element_id, cx, cy, r):
    icon.add_arc(f"{element_id}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
    icon.add_arc(f"{element_id}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
    icon.add_contour(element_id, *(f"{element_id}-{i}" for i in range(1, 5)), closed=True)


class FemaleTeacherBesideBoardBatch02213Redraw(Solo48):
    icon_id = "female-teacher-beside-board-batch-022-13-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/education"
    aliases = ("teacher at blackboard", "woman teaching", "presenter at whiteboard")
    keywords = ("teacher", "female", "woman", "board", "blackboard", "whiteboard", "class", "lesson", "education")

    def build(self) -> None:
        _circle(self, "head", HX, HEAD_CY, HEAD_R)

        self.add_line("torso", (HX, NECK_Y), SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("teacher", head="head", torso="torso", torso_junction="start")

        self.add_line("rear-leg", HIP, (HX - LEG_SPREAD, FOOT_Y))
        self.add_line("front-leg", HIP, (HX + LEG_SPREAD, FOOT_Y))
        self.relate("connect", "rear-leg", "waist")
        self.relate("connect", "front-leg", "waist")
        self.relate("connect", "rear-leg", "front-leg")

        self.add_line("arm", SHOULDER, HAND)
        self.relate("connect", "arm", "torso")
        self.relate("connect", "arm", "waist")

        L, T, R, B = BOARD["left"], BOARD["top"], BOARD["right"], BOARD["bottom"]
        self.add_polyline("board", (L, T), (R, T), (R, B), (L, B), closed=True)
