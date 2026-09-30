"""coughing-person-profile (redraw of the new-pipeline traced SVG).

Plan: a stick-figure upper body in profile, leaning right, on SQUARE
(centerline box (6,6)-(42,42)).
- Head: four cardinal quarter arcs, r HEAD_R about (HX, HEAD_CY); its top is
  the top extreme.
- Neck: a short vertical stub straight below the head, exactly GAP (8) under
  the head outline, so the detached head certifies (4 units of visible ink).
- Torso: one slanted line from the stub's foot to the bottom-left corner
  (left and bottom extremes), following the trace's lean.
- Arm: from the same shoulder node, the upper arm drops down-right to the
  elbow and the forearm rises to a fist raised in front of the face -- the
  trace's "Λ + V" zigzag.
- Cough: two rays opening to the right ("<" fan), level with the mouth and
  clear of the fist; the rays' outer ends are the right extreme.
Human construction: icon_set/references/human_ref/full_body_ref.png (ring
head, round-ended limbs); no useful Lucide match beyond `user`'s ring head.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "70068075-fcbd-43f7-8047-bd45057d5d00"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1044-coughing-person-profile/"
    "coughing-person-profile_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TOP, BOTTOM, LEFT, RIGHT = 6, 42, 6, 42
HEAD_R = 6
HX = 16
HEAD_CY = TOP + HEAD_R
GAP = 8
NECK = (HX, HEAD_CY + HEAD_R + GAP)        # head outline -> neck, on centerlines
SHOULDER = (HX, NECK[1] + 2)               # foot of the vertical neck stub
HIP = (LEFT, BOTTOM)
ELBOW = (22, 36)
FIST = (28, 22)
RAY_X0 = 36
RAYS = (((RAY_X0, 14), (RIGHT, 11)), ((RAY_X0, 22), (RIGHT, 25)))


class CoughingPersonProfileRedraw(Solo48):
    icon_id = "coughing-person-profile-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/symptoms"
    aliases = ("cough", "coughing", "person coughing")
    keywords = ("cough", "sick", "illness", "cold", "flu", "symptom", "person",
                "health", "covid", "sneeze")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("neck", NECK, SHOULDER)
        self.add_line("torso", SHOULDER, HIP)
        self.relate("connect", "neck", "torso")
        self.mark_human_figure("person", head="head", torso="neck", torso_junction="start")

        self.add_polyline("arm", SHOULDER, ELBOW, FIST)
        self.relate("connect", "arm", "neck")
        self.relate("connect", "arm", "torso")

        for i, (a, b) in enumerate(RAYS, 1):
            self.add_line(f"ray-{i}", a, b)
