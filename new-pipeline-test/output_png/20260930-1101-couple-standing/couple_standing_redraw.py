"""couple-standing (redraw of the new-pipeline traced SVG).

Plan: two identical frontal stick figures standing side by side on SQUARE
(centerline box (6,6)-(42,42)), mirrored about x 24, arms apart (not
holding hands), as in the generated image.
- each figure (axis x 13 / 35): a round r5 head about (x,11), top y 6,
  bottom y 16; torso from the shoulder y 24 (exactly 8 below the head, 4
  visible) to the hip y 34; a leg V from the hip to feet 5 either side on
  y 42; one arm run hand -> shoulder -> hand, both arms angled down to
  hands 7 out from the torso on y 30.
- the outer hands reach the box edge (6,30) / (42,30); the inner hands
  (20,30) / (28,30) stay 8 apart on centerlines.
Lucide: `users` (two figures side by side) informed the pairing only; its
busts are not stick figures.
Human reference: icon_set/references/human_ref/full_body_ref.png (circle
head, straight round-ended limbs, detached head 4 ink clear of the body).

Metric issues (couple-standing_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- stroke-count (10 strokes, budget 6): reduced to 8 paths (per figure one
  head, torso, arm run and leg V). Not fully fixed: two complete stick
  figures need at least 8 paths.
- clearance e0/e8, e0/e9, e1/e4, e1/e6 (heads 3 above the shoulders):
  each head bottom is exactly 8 on centerlines above its torso top,
  flagged with mark_human_figure.
- clearance e2/e3, e2/e4, e3/e6, e4/e6, e5/e6, e7/e8, e7/e9, e8/e9 (legs,
  arms and torso 2-7.8 apart): the torso, arm run and legs now share
  endpoints (connect); the legs open 10 at the feet and each hand sits 7
  from its torso and 8 from its hip.
- clearance e6/e8 (inner hands 4.35 apart): the inner hands are 8 apart.
- loose-join e2/e3, e3/e5, e4/e5: joins are exact shared endpoints.
- holes 3.88 / 3.79 (heads): the heads are r5, 6 inscribed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f9770e9-9cf6-4ca7-8f89-f37f07aff7a2"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1101-couple-standing/couple-standing_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS_DX = 11               # figures at x 13 / 35, mirrored about x 24
HEAD_R = 5
HEAD_CY = 11               # heads span y 6..16
SHOULDER_Y = HEAD_CY + HEAD_R + 8   # 24: exactly 8 below the head outline
HIP_Y = 34
FOOT_Y = 42
FOOT_DX = 5                # feet 10 apart
HAND_Y = 30
HAND_DX = 7                # hands 7 out: outer x 6 / 42, inner 8 apart


class CoupleStandingRedraw(Solo48):
    icon_id = "couple-standing-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/couple"
    aliases = ("couple", "two people", "pair", "partners")
    keywords = ("couple", "people", "two", "persons", "standing", "stick figures", "pair")

    def _figure(self, name: str, x: int) -> None:
        r, cy = HEAD_R, HEAD_CY
        self.add_arc(f"{name}-head-t", (x - r, cy), (x + r, cy), radius_x=r)
        self.add_arc(f"{name}-head-b", (x + r, cy), (x - r, cy), radius_x=r)
        self.add_contour(f"{name}-head", f"{name}-head-t", f"{name}-head-b", closed=True)
        self.add_line(f"{name}-torso", (x, SHOULDER_Y), (x, HIP_Y))
        self.add_polyline(
            f"{name}-arms",
            (x - HAND_DX, HAND_Y), (x, SHOULDER_Y), (x + HAND_DX, HAND_Y),
        )
        self.add_polyline(
            f"{name}-legs",
            (x - FOOT_DX, FOOT_Y), (x, HIP_Y), (x + FOOT_DX, FOOT_Y),
        )
        self.relate("connect", f"{name}-torso", f"{name}-arms")
        self.relate("connect", f"{name}-torso", f"{name}-legs")
        self.mark_human_figure(name, head=f"{name}-head", torso=f"{name}-torso", torso_junction="start")

    def build(self) -> None:
        self._figure("left", 24 - AXIS_DX)
        self._figure("right", 24 + AXIS_DX)
