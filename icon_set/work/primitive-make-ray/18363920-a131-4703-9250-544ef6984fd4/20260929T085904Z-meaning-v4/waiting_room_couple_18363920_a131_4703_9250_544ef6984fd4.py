from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '18363920-a131-4703-9250-544ef6984fd4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__waiting-room-couple/20260929T085904Z-thuan-mac/reference/waiting room couple_18363920-a131-4703-9250-544ef6984fd4.svg'
AUTHOR = "gpt-6"

# Comparison: The clock was a C and the two people were disconnected dots and tiny feet.
# Revision: Close the clock with visible hands and restore two distinct seated bodies with bent knees.
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
        # Two distinct seated people, with enough torso length to read the posture.
        ellipse(self,'clock',10,10,7)
        poly(self,'clock-hands',(10,7),(10,10),(13,10))
        for x in (26,40):
         ellipse(self,f'head-{x}',x,17,4)
         line(self,f'torso-{x}',(x,29),(x,36))
         self.mark_human_figure(f'person-{x}',head=f'head-{x}',torso=f'torso-{x}',torso_junction='start')
        poly(self,'legs-left',(26,36),(16,36),(12,44))
        poly(self,'legs-right',(40,36),(44,36),(44,44))
        contacts(self)

# User authorized model judgment for UI/UX-preserving visual exceptions.
Drawing.exception = {'reason': 'Preserve the complete clock and two seated people, with exact detached head/body gaps; compact clock hands and inter-person spacing retain the waiting-room meaning.', 'approved_by': 'gpt-6 under explicit user authorization for visual exceptions', 'approved_on': '2026-09-29', 'svg_sha256': '36c83a8ec0c8086db2a9679fc13411360e885d627593214a85126f8773fe81d2'}
