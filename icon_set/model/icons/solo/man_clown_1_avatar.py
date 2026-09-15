"""man-clown-1: rounded costume collar with reference hair/headwear.
Plan: SOLO48 VRECT_L, ink (6,2)-(42,46); circular face x24,
head bottom 24, shoulders 28, zero painted gap. Shared human_ref/user.svg
supplies curved shoulders; Lucide user-round original and atomic-debug guide
cardinal arcs. Fine trim omitted at 48. Body cue: rounded costume collar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-05/references/man-clown-1.svg'
SOURCE_HEAD_ICON_ID = 'man-clown-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class ManClown1Avatar(Solo48):
    icon_id = 'man-clown-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'clown', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_arc('jaw',(34,14),(14,14),radius_x=10)
        self.add_contour('head','crown','jaw',closed=True)
        for side, cx in [('left',11),('right',37)]:
            self.add_arc('hair-top-'+side,(cx-3,12),(cx+3,12),radius_x=3)
            self.add_arc('hair-bottom-'+side,(cx+3,12),(cx-3,12),radius_x=3)
            self.add_contour('hair-'+side,'hair-top-'+side,'hair-bottom-'+side,closed=True)
            self.relate('connect','head','hair-'+side)
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
        self.add_arc('body-neckline',(18,top),(30,top),radius_x=6,radius_y=6,sweep=False)
        self.relate('connect','body-neckline','body-top')
        self.relate('connect','body-neckline','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
