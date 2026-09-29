from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '1898abfe-93e3-5805-8016-2bd361c14022'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-farmer-shouldered-hoe/20260929T085904Z-thuan-mac/reference/farmer work_1898abfe-93e3-5805-8016-2bd361c14022.svg'
AUTHOR = "gpt-6"

# Comparison: The farmer hat became a rectangular bar, the hoe lost its blade, and the holding arm disappeared.
# Revision: Restore a brimmed hat, hanging hoe blade and bent supporting arm above a walking pose.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'walking-farmer-shouldered-hoe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('farmer', 'work')

    def build(self):
        poly(self,'hat',(18,9),(19,4),(27,4),(30,9))
        line(self,'brim',(15,10),(32,10))
        path(self,'head',(20,12),('A',4,4,False,(28,12)))
        line(self,'torso',(24,24),(21,32))
        self.mark_human_figure('farmer',head='head',torso='torso',torso_junction='start')
        poly(self,'hoe-shaft',(7,18),(42,25))
        poly(self,'hoe-blade',(7,18),(6,27),(12,28),(14,20))
        poly(self,'supporting-arm',(24,24),(30,30),(36,24))
        poly(self,'front-leg',(21,32),(29,38),(32,44))
        poly(self,'back-leg',(21,32),(12,44))
        contacts(self)
