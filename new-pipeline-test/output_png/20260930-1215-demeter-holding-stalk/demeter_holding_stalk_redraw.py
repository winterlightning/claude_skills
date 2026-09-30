"""demeter-holding-stalk (redraw of the new-pipeline traced SVG).

Plan: Demeter as a stick figure holding one upright wheat stalk, on VRECT_M
(centerline box (10,4)-(38,44)), the keyshape the metrics suggest.
- head: 4-cardinal-arc ring, r4, centre (HX,8); its top is the top extreme.
- torso: vertical line on HX from the neck (HX,20), exactly 8 under the head
  outline (4-unit ink gap, human-reference.md), down to the hip (HX,32).
- legs: mirrored about HX, 1:2 slope from the hip to the feet at y=44; the
  left foot is the left extreme x=10.
- left arm: 45 degrees down-left from the neck to the hand at x=10.
- right arm: 45 degrees down to the elbow, then level to the hand on the
  stem; the stem is split at the hand so the two share an endpoint.
- stalk: stem on SX from the ground up to a hollow grain-shaped ear, pointed
  at both ends (bottom point on the stem at y=20, top point on the top
  extreme), built from four cubics whose widest nodes (x=28/38, y=12) carry
  vertical tangents; the ear's right node is the right extreme x=38.
  A round-bottomed teardrop ear was tried first and rejected at 48 px: it
  read as a torch flame.
References: icon_set/references/human_ref/full_body_ref.png (ring head,
round-ended single-stroke limbs); Lucide `wheat` for a grain ear hung on a
straight stem (its paired grains do not fit the 10-unit ear, so the single
pointed ear from the generated image is kept).

Metric issues:
- clearance e0/e7, e4/e5, e4/e7, e0/e3, e3/e5 (ear, its tip curl and the arm
  crowding the stalk top): the ear is one closed pointed grain whose bottom
  sits 8 above the hand (10 across at its widest, 6-unit ink hole); the tip
  curl (e4) and inner stem stubs (e7) are dropped.
- clearance e2/e8, e3/e8 (arms 2-3 from the head): the arms start at the neck,
  8 under the head outline, and fall away from it.
- clearance e1/e2, e1/e3, e1/e6, e2/e6, e3/e6 (limbs 5-7.7 from the legs and
  torso): the left hand is 8.5 from the hip, the elbow 8 from the torso and
  8.9 from the hip; legs and torso meet only at the hip (declared).
- keyshape-short-axis (x filled 85%): the left arm/foot reach x=10 and the ear
  reaches x=38.
- hole at (19.5,12.3) (head, 3.35): the ring is r4 (8 across on centerlines),
  the build gate's hole check passes it; r5 would push the neck, hip and
  legs 2 lower and the legs are already only 12 tall.
- stroke-count (9 strokes): now 6 parts: head, body (torso, two arms, two
  legs), stem, ear.
- stroke-width (trace 2.4): redrawn at stroke 4 with 8-unit gaps.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1b451532-820c-4276-ab4a-3f9c1c9b785d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1215-demeter-holding-stalk/demeter-holding-stalk_raw.svg"
AUTHOR = "claude-opus-5-5"

HX = 16                      # body axis
HEAD_R = 4
HEAD_CY = 8                  # head top on y=4 (VRECT_M top)
NECK_Y = HEAD_CY + HEAD_R + 8
HIP_Y = 32
FOOT_Y = 44                  # VRECT_M bottom
LEG_DX = 6                   # 1:2 legs, feet at x=10 / x=22
LEFT_HAND = (10, 26)         # 45 degrees from the neck
ELBOW = (24, 28)             # 45 degrees from the neck, 8 from the torso
SX = 33                      # stem axis
EAR_HALF_W = 5               # ear x 28..38
EAR_MID_Y = 12               # widest point of the ear
EAR_BOTTOM_Y = 20            # ear point on the stem, 8 above the hand
EAR_TIP_Y = 4                # ear point on the top extreme


class DemeterHoldingStalkRedraw(Solo48):
    icon_id = "demeter-holding-stalk-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/mythology"
    aliases = ("demeter", "harvest goddess", "person holding wheat")
    keywords = ("demeter", "ceres", "goddess", "harvest", "wheat", "grain", "stalk", "agriculture", "mythology")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        neck, hip = (HX, NECK_Y), (HX, HIP_Y)
        self.add_line("torso", neck, hip)
        self.mark_human_figure("demeter", head="head", torso="torso", torso_junction="start")

        self.add_line("leg-l", hip, (HX - LEG_DX, FOOT_Y))
        self.add_line("leg-r", hip, (HX + LEG_DX, FOOT_Y))
        self.add_line("arm-l", neck, LEFT_HAND)
        hand = (SX, ELBOW[1])
        self.add_polyline("arm-r", neck, ELBOW, hand)
        for part in ("leg-l", "leg-r", "arm-l", "arm-r"):
            self.relate("connect", part, "torso")
        self.relate("connect", "leg-l", "leg-r")
        self.relate("connect", "arm-l", "arm-r")

        # Stem split at the hand; the ear sits on its top end.
        ear_bottom = (SX, EAR_BOTTOM_Y)
        self.add_line("stem-top", ear_bottom, hand)
        self.add_line("stem-bottom", hand, (SX, FOOT_Y))
        self.add_contour("stem", "stem-top", "stem-bottom")
        self.relate("connect", "stem", "arm-r")

        # Grain-shaped ear pointed at both ends; its widest nodes carry the
        # vertical tangents, so x=28/38 are exact extremes.
        w, mid = EAR_HALF_W, EAR_MID_Y
        right, left, tip = (SX + w, mid), (SX - w, mid), (SX, EAR_TIP_Y)
        self.add_bezier("ear-br", ear_bottom, ((SX + 3, ear_bottom[1] - 2), (SX + w, mid + 4), right))
        self.add_bezier("ear-tr", right, ((SX + w, mid - 4), (SX + 2, EAR_TIP_Y + 2), tip))
        self.add_bezier("ear-tl", tip, ((SX - 2, EAR_TIP_Y + 2), (SX - w, mid - 4), left))
        self.add_bezier("ear-bl", left, ((SX - w, mid + 4), (SX - 3, ear_bottom[1] - 2), ear_bottom))
        self.add_contour("ear", "ear-br", "ear-tr", "ear-tl", "ear-bl", closed=True)
        self.relate("connect", "ear", "stem")
