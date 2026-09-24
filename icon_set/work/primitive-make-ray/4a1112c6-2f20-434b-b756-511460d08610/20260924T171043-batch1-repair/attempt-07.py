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
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/sports"
    aliases = ("aerial-bow-pose",)
    keywords = ("aerial", "yoga", "sling", "suspended", "exercise")

    def build(self):
        # HRECT_L rebalances the sling to leave room for a true neck junction.
        # Shared human reference: full_body_ref.png; head radius 3, center (41,37).
        # Torso endpoint (30,37): 41-3-30=8 centerline / 4 ink clearance.
        self.add_polyline('left-suspension',(18,8),(14,22),(12,30))
        self.add_line('right-suspension',(26,8),(26,20))
        self.add_arc('sling-return',(26,20),(18,28),radius_x=8)
        self.add_line('sling-base',(18,28),(12,30))
        self.add_contour('sling','right-suspension','sling-return','sling-base')
        self.relate('connect','sling','left-suspension')
        self.add_arc('limb-shoulder',(14,22),(4,30),radius_x=10,radius_y=8,sweep=False)
        self.add_line('limb-side',(4,30),(4,34))
        self.add_arc('limb-fold',(4,34),(16,34),radius_x=6,sweep=False)
        self.add_line('limb-return',(16,34),(12,30))
        self.add_contour('folded-limb','limb-shoulder','limb-side','limb-fold','limb-return')
        self.relate('connect','folded-limb','left-suspension')
        self.relate('connect','folded-limb','sling')
        self.add_arc('body-bend',(26,20),(26,32),radius_x=6)
        self.add_line('body-lower',(26,32),(26,37))
        self.add_line('torso',(26,37),(30,37))
        self.relate('connect','sling','body-bend')
        self.relate('connect','body-bend','body-lower')
        self.relate('connect','body-lower','torso')
        self.add_arc('head-top',(38,37),(44,37),radius_x=3)
        self.add_arc('head-bottom',(44,37),(38,37),radius_x=3)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='end')
