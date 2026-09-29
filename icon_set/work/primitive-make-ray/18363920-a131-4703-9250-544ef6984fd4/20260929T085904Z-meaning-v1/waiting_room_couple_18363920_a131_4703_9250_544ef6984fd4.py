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
        ellipse(self,'clock',11,11,7)
        poly(self,'clock-hands',(11,7),(11,11),(14,11))
        for x in (25,39):
         ellipse(self,f'head-{x}',x,20,3)
         line(self,f'torso-{x}',(x,31),(x,35))
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
         if x==25:
          poly(self,'legs-left',(25,35),(17,35),(13,43))
          poly(self,'chair-left',(30,30),(30,40),(21,40),(21,44))
         else:
          poly(self,'legs-right',(39,35),(44,35),(44,44))
          poly(self,'chair-right',(34,30),(34,40),(38,40),(38,44))
        contacts(self)
