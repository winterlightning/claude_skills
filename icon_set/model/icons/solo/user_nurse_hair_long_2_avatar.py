"""user-nurse-hair-long-2: curved uniform neckline with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 32, shoulder top 36, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: curved uniform neckline. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-11/references/user-nurse-hair-long-2.svg'
SOURCE_HEAD_ICON_ID = 'user-nurse-hair-long-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class UserNurseHairLong2Avatar(Solo48):
    icon_id = 'user-nurse-hair-long-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'nurse', 'hair', 'long', '2', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(12,24),(8,4),(40,4),(36,24),(32,24),(16,24),(12,24))
        self.add_arc('face',(32,24),(16,24),radius_x=8)
        self.relate('connect','face','cap')
        self.add_line('cross-horizontal',(22,14),(26,14))
        self.add_line('cross-vertical',(24,12),(24,16))
        self.relate('connect','cross-horizontal','cross-vertical')
        for side,sign in [('left',-1),('right',1)]:
            self.add_line('hair-'+side,(24+sign*12,24),(24+sign*16,28))
            self.relate('connect','hair-'+side,'cap')
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
