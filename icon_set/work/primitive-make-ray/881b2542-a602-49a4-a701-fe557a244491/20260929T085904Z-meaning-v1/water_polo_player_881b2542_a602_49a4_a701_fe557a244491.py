from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '881b2542-a602-49a4-a701-fe557a244491'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__water-polo-player/20260929T085904Z-thuan-mac/reference/swimming waterpolo_881b2542-a602-49a4-a701-fe557a244491.svg'
AUTHOR = "gpt-6"

# Comparison: The ball was fused onto a pole-like arm, and the athlete had no readable throwing pose.
# Revision: Restore a circular ball above a bent throwing arm, a separate aligned head, a reaching arm and water waves.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'water-polo-player'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('swimming', 'waterpolo')

    def build(self):
        ellipse(self,'head',20,15,5)
        ellipse(self,'ball',38,8,4)
        line(self,'torso',(20,28),(22,37))
        self.mark_human_figure('player',head='head',torso='torso',torso_junction='start')
        poly(self,'throwing-arm',(20,28),(33,27),(38,15),(38,12))
        path(self,'reaching-arm',(20,28),('C',(12,26),(8,29),(5,34)))
        path(self,'water',(4,39),('C',(9,33),(14,43),(21,39)),('C',(28,33),(34,43),(44,38)))
        contacts(self)
