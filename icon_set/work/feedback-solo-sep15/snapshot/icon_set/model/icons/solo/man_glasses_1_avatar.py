"""man-glasses-1: shirt fastening with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 32, shoulders 36, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: shirt fastening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '25af2252-94aa-5683-bdb4-b15dc9190e60'
SOURCE_PATH = 'pictographic-primitives/avatars/man glasses_25af2252-94aa-5683-bdb4-b15dc9190e60.svg'
SOURCE_HEAD_ICON_ID = 'man-glasses-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class ManGlasses1Avatar(Solo48):
    icon_id = 'man-glasses-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'glasses', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,10),(34,10),radius_x=10,radius_y=6)
        for side,cx in [('left',14),('right',34)]:
            self.add_arc('lens-top-'+side,(cx,22),(cx,10),radius_x=6)
            self.add_arc('lens-bottom-'+side,(cx,10),(cx,22),radius_x=6)
            self.add_contour('lens-'+side,'lens-top-'+side,'lens-bottom-'+side,closed=True)
            self.relate('connect','crown','lens-'+side)
        self.add_line('bridge',(20,16),(28,16))
        self.relate('connect','bridge','lens-left')
        self.relate('connect','bridge','lens-right')
        self.add_arc('face',(34,22),(14,22),radius_x=10)
        self.relate('connect','face','lens-left')
        self.relate('connect','face','lens-right')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_line('body-fastening',(24,top),(24,44))
        self.relate('connect','body-fastening','body-top')
        self.relate('connect','body-fastening','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
