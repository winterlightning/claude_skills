from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '18363920-a131-4703-9250-544ef6984fd4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__waiting-room-couple/20260929T085904Z-thuan-mac/reference/waiting room couple_18363920-a131-4703-9250-544ef6984fd4.svg'
AUTHOR = "gpt-6"

# Comparison: The clock was a C and the two people were disconnected dots and tiny feet.
# Revision: Close the clock with clear hands; restore two seated bodies with bent knees and short chair backs.
# Plan: coherent subject contours; named parts own attachments; paired features share parameters.
# Human construction: icon_set/references/human_ref/full_body_ref.png; detached heads use 8 centerline / 4 ink gap at torso junction.
class Drawing(Solo48):
    icon_id = 'waiting-room-couple'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('waiting', 'room', 'couple')

    def build(self):
        # The clock occupies the upper left; two opposed seated silhouettes preserve the source arrangement.
        ellipse(self,'clock',12,12,8)
        poly(self,'clock-hands',(12,9),(12,12),(15,12))
        for x in (25,39):
         ellipse(self,f'head-{x}',x,23,3)
         line(self,f'torso-{x}',(x,34),(x,37))
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
        poly(self,'legs-left',(25,37),(15,37),(11,44))
        poly(self,'legs-right',(39,37),(44,37),(44,44))
        # Seat lines meet the bodies at actual endpoints, without a second crowded backrest.
        line(self,'seat-left',(25,37),(30,37))
        line(self,'seat-right',(39,37),(34,37))
        contacts(self)
