"""craftsman-holding-a-hammer (redraw of the new-pipeline traced SVG).

Plan: a frontal stick figure on VRECT_L (centerline box (8,4)-(40,44))
raising an upright hammer on the right.
- figure axis x 16: round r5 head about (16,9) (top y 4), torso x 16 from
  the shoulder y 22 (exactly 8 below the head outline, 4 visible) to the
  hip y 32, legs an inverted V from the hip to feet (10,44) / (22,44).
- arms: one run from the lowered left hand (8,28) through the shoulder,
  the right upper arm dropping slightly to the elbow (25,27), the forearm
  rising to the hand (35,22), which carries on straight up as the handle to
  the hammer head.
- hammer head: a hollow rectangle (30,4)-(40,14), the handle meeting its
  bottom edge at x 35 (the bottom edge is split there so they share an
  endpoint).
Lucide: `hammer` was checked; its diagonal claw head does not fit an upright
raised tool, so only the idea of a boxy head on a straight handle was kept.
Human reference: icon_set/references/human_ref/full_body_ref.png (circle
head, straight round-ended limbs, inverted-V legs).

Metric issues (craftsman-holding-a-hammer_metrics.json) and how they were
handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (VRECT_M, y fill 96%): switched to VRECT_L. At stroke 4
  the lowered hand must sit 8 left of the torso and the hammer head 8 (9 for
  the curved head) right of the head circle; VRECT_M's 28 wide box cannot
  hold head + gap + a hammer head with a 6 wide hole. On VRECT_L every
  extreme is exact: left hand x 8, hammer head x 40, head and hammer tops
  y 4, feet y 44.
- clearance e0/e5 (hammer head 6.7 from the head): the hammer head starts at
  x 30, 9 from the head outline.
- clearance e2/e5, e3/e5, e4/e5 (head 2.3-3.7 above the shoulder): the head
  bottom is exactly 8 on centerlines above the torso top, flagged with
  mark_human_figure.
- clearance e1/e4 (legs 7.2 apart near the feet): the legs are one inverted
  V opening to 12 at the feet.
- clearance e2/e4 (lowered arm 6 from the torso): the lowered hand is 8 from
  the torso and 8.8 from the left leg.
- hole 4.08 (head): the head is r5 (6 inscribed); the hammer head hole is
  6x6.
- loose-join e2/e3 (arms met 1.35 apart): the arms are one continuous run
  through the shoulder, connected to the torso.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "04ebbce5-fdd2-4c6c-bc45-d497a7339082"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1044-craftsman-holding-a-hammer/craftsman-holding-a-hammer_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_X = 16
HEAD_R = 5
HEAD_CY = 9                           # head spans y 4..14
SHOULDER_Y = HEAD_CY + HEAD_R + 8     # 22: exactly 8 below the head outline
HIP_Y = 33
FOOT_Y = 44
FOOT_DX = 6                           # feet 12 apart
LOW_HAND = (8, 28)                    # lowered left hand, 8 left of the torso
ELBOW = (25, 27)
HAND = (35, 22)
HAMMER = (30, 4, 40, 14)              # hammer head centerline box (hole 6x6)
HANDLE_X = 35


class CraftsmanHoldingAHammerRedraw(Solo48):
    icon_id = "craftsman-holding-a-hammer-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/work"
    aliases = ("craftsman", "carpenter", "worker with hammer", "builder")
    keywords = ("craftsman", "hammer", "carpenter", "builder", "worker", "tool", "person", "construction")

    def build(self) -> None:
        x, r, cy = AXIS_X, HEAD_R, HEAD_CY

        self.add_arc("head-t", (x - r, cy), (x + r, cy), radius_x=r)
        self.add_arc("head-b", (x + r, cy), (x - r, cy), radius_x=r)
        self.add_contour("head", "head-t", "head-b", closed=True)

        self.add_line("torso", (x, SHOULDER_Y), (x, HIP_Y))
        self.add_polyline(
            "legs", (x - FOOT_DX, FOOT_Y), (x, HIP_Y), (x + FOOT_DX, FOOT_Y),
        )
        self.add_polyline(
            "arms", LOW_HAND, (x, SHOULDER_Y), ELBOW, HAND,
            (HANDLE_X, HAMMER[3]),
        )
        self.relate("connect", "torso", "legs")
        self.relate("connect", "torso", "arms")
        self.mark_human_figure("craftsman", head="head", torso="torso", torso_junction="start")

        # Hammer head: the bottom edge is split at the handle.
        x0, y0, x1, y1 = HAMMER
        self.add_polyline(
            "hammer-head",
            (HANDLE_X, y1), (x1, y1), (x1, y0), (x0, y0), (x0, y1), (HANDLE_X, y1),
            closed=True,
        )
        self.relate("connect", "arms", "hammer-head")
