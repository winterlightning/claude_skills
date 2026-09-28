"""woman-glasses: round neckline with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 32, shoulder top 36, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: round neckline. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-14/references/woman-glasses.svg'
SOURCE_HEAD_ICON_ID = 'woman-glasses'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class WomanGlassesAvatar(Solo48):
    icon_id = 'woman-glasses-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('woman', 'glasses', 'portrait', 'bust')
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
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('side-hair-'+side,(24+sign*10,22),((24+sign*12,24),(24+sign*14,26),(24+sign*16,26)))
            self.relate('connect','side-hair-'+side,'face')
            self.relate('connect','side-hair-'+side,'lens-'+side)
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

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
