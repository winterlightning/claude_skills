"""blind (redraw of the new-pipeline traced SVG): a blind person walking with a
long white cane.

Plan: right-facing stick figure on VRECT_M (centerline box (10,4)-(38,44)).
- head: 4-cardinal-arc circle, r5, centre (HX,9); top touches y=4.
- torso: vertical line on HX from the neck (HX,22) to the hip (HX,32); the
  neck sits exactly 8 centerline units under the head outline (14 -> 22),
  a 4-unit ink gap (human-reference.md).
- arm: neck -> elbow -> hand, reaching forward; the cane is attached at the hand.
- cane: one straight (8,15) run from the hand down to the ground ahead of the
  feet, the x=38 / y=44 extreme.
- legs: rear leg straight down-left to the x=10 extreme, front leg bent at
  the knee (walking stride).
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); construction follows the earlier
hiker-with-trekking-pole redraw. No useful Lucide match (Lucide has no
blind/cane person).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis: rear foot on x=10 and cane tip on x=38, so VRECT_M is
  filled exactly on both axes.
- clearance e0/e1, e0/e2 (head vs arm, head vs torso): head detached with the
  exact 8 centerline gap to the neck; the arm leaves the neck moving away.
- clearance e1/e2 (arm vs torso): elbow pushed to 8 units off the torso.
- clearance e1/e3, e2/e3 (arm/cane vs front leg, legs): front knee and foot
  are >= 10 units from the cane; the legs diverge from a shared hip.
- hole (2.81 inscribed): head radius 5 leaves a 6-unit inscribed opening.
- no-head: the head is a true circle and is flagged with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5dce7e9a-2184-434a-9e94-71138d2b612d"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1805-blind/blind_raw.svg"
AUTHOR = "claude-opus-5-5"

HX = 18          # torso / head axis
HEAD_R = 5
HEAD_CY = 9      # centerline top y=4
NECK_Y = 22      # HEAD_CY + HEAD_R + 8
HIP = (HX, 32)
ELBOW = (26, 28)
HAND = (30, 29)
CANE_TIP = (38, 44)
KNEE = (22, 37)
FRONT_FOOT = (24, 44)
REAR_FOOT = (10, 44)


class BlindRedraw(Solo48):
    icon_id = "blind-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/accessibility"
    aliases = ("blind person", "visually impaired", "white cane")
    keywords = ("blind", "cane", "accessibility", "visually impaired", "walking", "person")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        neck = (HX, NECK_Y)
        self.add_line("torso", neck, HIP)
        self.mark_human_figure("walker", head="head", torso="torso", torso_junction="start")

        self.add_polyline("arm", neck, ELBOW, HAND)
        self.relate("connect", "arm", "torso")

        self.add_line("cane", HAND, CANE_TIP)
        self.relate("connect", "cane", "arm")

        self.add_line("rear-leg", HIP, REAR_FOOT)
        self.add_polyline("front-leg", HIP, KNEE, FRONT_FOOT)
        self.relate("connect", "rear-leg", "torso")
        self.relate("connect", "front-leg", "torso")
        self.relate("connect", "front-leg", "rear-leg")
