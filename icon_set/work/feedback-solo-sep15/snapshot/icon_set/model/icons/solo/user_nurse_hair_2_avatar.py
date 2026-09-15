"""user-nurse-hair-2: uniform front panels with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 32, shoulder top 36, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: uniform front panels. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-11/references/user-nurse-hair-2.svg'
SOURCE_HEAD_ICON_ID = 'user-nurse-hair-2'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class UserNurseHair2Avatar(Solo48):
    icon_id = 'user-nurse-hair-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('user', 'nurse', 'hair', '2', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(12,24),(8,4),(40,4),(36,24),(32,24),(16,24),(12,24))
        self.add_arc('face',(32,24),(16,24),radius_x=8)
        self.relate('connect','face','cap')
        self.add_line('cross-horizontal',(22,14),(26,14))
        self.add_line('cross-vertical',(24,12),(24,16))
        self.relate('connect','cross-horizontal','cross-vertical')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*8,24),((24+sign*10,26),(24+sign*12,28),(24+sign*16,28)))
            self.relate('connect','hair-'+side,'cap')
            self.relate('connect','hair-'+side,'face')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-apron-left', (18,top), (18,44))
        self.add_line('body-apron-right', (30,top), (30,44))
        self.relate('connect', 'body-apron-left', 'body-top')
        self.relate('connect', 'body-apron-right', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
