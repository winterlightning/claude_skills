"""user-alien-1: simple suit seam with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 34, shoulder top 38, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails are omitted for native 48px clarity.
Body cue: simple suit seam. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-09/references/user-alien-1.svg'
SOURCE_HEAD_ICON_ID = 'user-alien-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 34
class UserAlien1Avatar(Solo48):
    icon_id = 'user-alien-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'alien', '1', 'portrait', 'bust')
    def build(self):
        self.add_arc('crown',(16,26),(32,26),radius_x=8)
        self.add_arc('face',(32,26),(16,26),radius_x=8)
        self.add_contour('head','crown','face',closed=True)
        for side,sign in [('left',-1),('right',1)]:
            cx=24+sign*12
            self.add_arc('antenna-top-'+side,(cx-4,8),(cx+4,8),radius_x=4)
            self.add_arc('antenna-bottom-'+side,(cx+4,8),(cx-4,8),radius_x=4)
            self.add_contour('antenna-'+side,'antenna-top-'+side,'antenna-bottom-'+side,closed=True)
            self.add_line('stalk-'+side,(cx,12),(24,18))
            self.relate('connect','stalk-'+side,'head')
            self.relate('connect','stalk-'+side,'antenna-'+side)
        self.relate('connect','stalk-left','stalk-right')
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
