"""hiker-with-trekking-pole (redraw of the new-pipeline traced SVG).

Plan: right-facing stick hiker on VRECT_M (centerline box (10,4)-(38,44)).
- head: 4-cardinal-arc circle, r4, centre (HX,8), top touches y=4.
- torso: vertical line from the neck (HX,20) to the hip; the neck sits exactly
  8 centerline units under the head outline (4-unit ink gap, human-reference.md).
- backpack: open rounded rectangle hung off the back; the torso is its right
  wall, its left side is the x=10 extreme.
- arm: shoulder -> elbow -> hand on the pole; the pole is split at the hand.
- legs: rear leg straight down-left, front leg bent at the knee.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); Lucide backpack for the rounded pack corners.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1337-hiker-with-trekking-pole/"
    "hiker-with-trekking-pole_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 20          # torso / head axis
HEAD_R = 4
HEAD_CY = 8      # top of head ink edge at y=2, centerline top y=4
NECK_Y = 20      # HEAD_CY + HEAD_R + 8
HIP = (HX, 32)
PACK = dict(left=10, top=NECK_Y, bottom=30, r=3)
ELBOW = (29, 27)
HAND = (38, 24)
POLE_TOP, POLE_BOTTOM = (38, 16), (38, 44)
KNEE = (27, 37)
FRONT_FOOT = (30, 44)
REAR_FOOT = (13, 44)


class HikerWithTrekkingPoleRedraw(Solo48):
    icon_id = "hiker-with-trekking-pole-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    aliases = ("trekker", "hiking person")
    keywords = ("hiking", "trekking", "hiker", "backpack", "pole", "walking", "outdoors")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        neck = (HX, NECK_Y)
        pack_join = (HX, PACK["bottom"])
        self.add_line("torso", neck, pack_join)
        self.add_line("waist", pack_join, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("hiker", head="head", torso="torso", torso_junction="start")

        # Backpack: neck -> top-left corner -> bottom-left corner -> torso.
        L, T, B, pr = PACK["left"], PACK["top"], PACK["bottom"], PACK["r"]
        self.add_line("pack-top", neck, (L + pr, T))
        self.add_arc("pack-tl", (L + pr, T), (L, T + pr), radius_x=pr, sweep=False)
        self.add_line("pack-side", (L, T + pr), (L, B - pr))
        self.add_arc("pack-bl", (L, B - pr), (L + pr, B), radius_x=pr, sweep=False)
        self.add_line("pack-bottom", (L + pr, B), pack_join)
        self.add_contour("pack", "pack-top", "pack-tl", "pack-side", "pack-bl", "pack-bottom")
        self.relate("connect", "pack", "torso")
        self.relate("connect", "pack", "waist")

        self.add_polyline("arm", neck, ELBOW, HAND)
        self.relate("connect", "arm", "torso")
        self.relate("connect", "arm", "pack")

        self.add_line("pole-top", POLE_TOP, HAND)
        self.add_line("pole-bottom", HAND, POLE_BOTTOM)
        self.add_contour("pole", "pole-top", "pole-bottom")
        self.relate("connect", "pole", "arm")

        self.add_line("rear-leg", HIP, REAR_FOOT)
        self.add_polyline("front-leg", HIP, KNEE, FRONT_FOOT)
        self.relate("connect", "rear-leg", "waist")
        self.relate("connect", "front-leg", "waist")
        self.relate("connect", "front-leg", "rear-leg")
