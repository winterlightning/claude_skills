"""A suspended aerial-yoga figure with folded limbs and a detached head.

Plan: one asymmetric suspension/body composite and one circular head. Preserve
the reference's two long sloping straps, left folded limb, lower sling return,
and right-facing bent torso. Shared contact nodes own all attachments.
SQUARE visible extremes (4,4)-(44,44), centerlines (6,6)-(42,42).
Human reference: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing informs circular head and coherent round-ended limbs.
The source's deliberate neck/head offset is retained; the final upper torso
runs horizontally toward the head. Head center (38,38), r4, neck (26,38):
Final head center (40,40), r2, neck (30,40): 10 - 2 = 8
centerline clearance, hence exactly 4 ink units. The smaller circular head
uses the complete-circle exception and retains the reference's small head.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4a1112c6-2f20-434b-b756-511460d08610"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg"
AUTHOR = "gpt-6"


class AerialYogaBowPose(Solo48):
    icon_id = "aerial-yoga-bow-pose"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sports"
    aliases = ("aerial bow pose",)
    keywords = ("yoga", "sling", "suspended", "exercise")

    def build(self):
        left_attach, sling_left = (14, 22), (12, 32)
        right_attach = (28, 22)
        self.add_line("strap-left-upper", (18, 6), left_attach)
        self.add_line("strap-left-lower", left_attach, sling_left)
        self.add_line("strap-right", (26, 6), right_attach)
        self.add_arc("sling-return", right_attach, (20, 32), radius_x=8, radius_y=10)
        self.add_line("sling-base", (20, 32), sling_left)
        self.add_contour("sling", "strap-right", "sling-return", "sling-base")
        self.add_contour("left-suspension", "strap-left-upper", "strap-left-lower")
        self.relate("connect", "sling", "left-suspension")
        self.add_arc("limb-shoulder", left_attach, (6, 30), radius_x=8, sweep=False)
        self.add_line("limb-side", (6, 30), (6, 38))
        self.add_arc("limb-fold", (6, 38), (14, 38), radius_x=4, sweep=False)
        self.add_line("limb-return", (14, 38), sling_left)
        self.add_contour("folded-limb", "limb-shoulder", "limb-side", "limb-fold", "limb-return")
        self.relate("connect", "folded-limb", "left-suspension")
        self.relate("connect", "folded-limb", "sling")
        self.add_arc("body-bend", right_attach, (28, 34), radius_x=6)
        self.add_line("body-lower", (28, 34), (26, 40))
        self.add_line("torso", (26, 40), (30, 40))
        self.add_contour("body", "body-bend", "body-lower", "torso")
        self.relate("connect", "body", "sling")
        cx, cy, radius = 40, 40, 2
        self.add_arc("head-top", (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc("head-bottom", (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="end")
