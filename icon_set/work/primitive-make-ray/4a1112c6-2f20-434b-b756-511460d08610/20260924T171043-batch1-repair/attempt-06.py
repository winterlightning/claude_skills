"""A suspended aerial-yoga figure with folded limbs and a detached head.

Plan: one asymmetric suspension/body composite and one circular head. Preserve
the reference's two long sloping straps, left folded loop, lower sling return,
and right-facing bent torso. Shared contact nodes own all attachments.
SQUARE centerline extremes are (6,6)-(42,42).
Human reference: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing informs the circular head and coherent round-ended limbs.
The upper torso ends at (28,38) and points horizontally toward the head centered
at (39,38), radius 3: 11 - 3 = 8 centerline units, exactly 4 ink units.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "4a1112c6-2f20-434b-b756-511460d08610"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/aerial yoga bow pose_4a1112c6-2f20-434b-b756-511460d08610.svg'
AUTHOR = 'gpt-6'


class AerialYogaBowPose(Solo48):
    icon_id = "aerial-yoga-bow-pose"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sports"
    aliases = ("aerial-bow-pose",)
    keywords = ("aerial", "yoga", "sling", "suspended", "exercise")

    def build(self) -> None:
        left_attach = (14, 22)
        sling_left = (12, 32)
        right_attach = (28, 22)

        self.add_line("strap-left-upper", (18, 6), left_attach)
        self.add_line("strap-left-lower", left_attach, sling_left)
        self.add_contour("left-suspension", "strap-left-upper", "strap-left-lower")

        self.add_line("strap-right", (26, 6), right_attach)
        self.add_arc("sling-return", right_attach, (20, 29), radius_x=8, radius_y=7)
        self.add_line("sling-base", (20, 29), sling_left)
        self.add_contour("sling", "strap-right", "sling-return", "sling-base")
        self.relate("connect", "sling", "left-suspension")

        self.add_arc("limb-shoulder", left_attach, (6, 30), radius_x=8, sweep=False)
        self.add_line("limb-side", (6, 30), (6, 37))
        self.add_arc("limb-fold", (6, 37), (16, 37), radius_x=5, sweep=False)
        self.add_line("limb-return", (16, 37), sling_left)
        self.add_contour(
            "folded-limb",
            "limb-shoulder",
            "limb-side",
            "limb-fold",
            "limb-return",
        )
        self.relate("connect", "folded-limb", "left-suspension")
        self.relate("connect", "folded-limb", "sling")

        self.add_arc("body-bend", right_attach, (28, 30), radius_x=4, sweep=True)
        self.add_line("body-lower", (28, 30), (28, 39))
        self.add_line("torso", (20, 39), (28, 39))
        self.add_contour("body", "body-bend", "body-lower")
        self.relate("connect", "body-lower", "torso")
        self.relate("connect", "body", "sling")

        head_cx, head_cy, head_radius = 39, 39, 3
        self.add_arc(
            "head-top",
            (head_cx - head_radius, head_cy),
            (head_cx + head_radius, head_cy),
            radius_x=head_radius,
        )
        self.add_arc(
            "head-bottom",
            (head_cx + head_radius, head_cy),
            (head_cx - head_radius, head_cy),
            radius_x=head_radius,
        )
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="end")
