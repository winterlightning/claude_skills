'A suspended aerial-yoga bow pose with a folded limb, sling, bent torso and detached head.\nPlan: SQUARE provides vertical room for the suspension and folded limb.\nReduction: Rebalanced straps, sling and torso; no major subject component omitted.\nConstruction: Shared human full_body_ref.png: circular head, coherent torso and round-ended limbs. No useful exact Lucide pose match.'

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

    def build(self):
        # SQUARE: centerline extremes (6,6)-(42,42). Shared left sling/limb nodes.
        # Human reference full_body_ref.png; head center (39,39), radius 3.
        # Actual upper-torso endpoint (28,39): 39-3-28=8 centerline, 4 ink units.
        self.add_polyline('left-suspension',(18,6),(14,18),(14,30))
        self.add_line('right-suspension',(26,6),(24,18))
        self.add_arc('sling-return',(24,18),(16,26),radius_x=8)
        self.add_line('sling-base',(16,26),(14,30))
        self.add_contour('sling','right-suspension','sling-return','sling-base')
        self.relate('connect','sling','left-suspension')
        self.add_arc('limb-shoulder',(14,18),(6,26),radius_x=8,radius_y=8,sweep=False)
        self.add_line('limb-side',(6,26),(6,36))
        self.add_arc('limb-fold',(6,36),(18,36),radius_x=6,sweep=False)
        self.add_line('limb-return',(18,36),(14,30))
        self.add_contour('folded-limb','limb-shoulder','limb-side','limb-fold','limb-return')
        self.relate('connect','folded-limb','left-suspension')
        self.relate('connect','folded-limb','sling')
        self.add_arc('body-bend',(24,18),(24,30),radius_x=6)
        self.add_line('body-lower',(24,30),(24,39))
        self.add_line('torso',(24,39),(28,39))
        self.relate('connect','sling','body-bend')
        self.relate('connect','body-bend','body-lower')
        self.relate('connect','body-lower','torso')
        self.add_arc('head-top',(36,39),(42,39),radius_x=3)
        self.add_arc('head-bottom',(42,39),(36,39),radius_x=3)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='end')
