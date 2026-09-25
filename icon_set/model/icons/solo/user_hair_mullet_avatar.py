"""user-hair-mullet: V neck shirt with reference head silhouette.
Plan: SOLO48 VRECT_L ink (6,2)-(42,46) budgets headwear and curved shoulders.
Face x24, circular radii; head bottom 24, shoulder top 28, zero ink gap.
Human reference user.svg supplies curved shoulders and circular anatomy;
Lucide user-round original and atomic-debug guide cardinal arcs.
Fine trim and facial microdetails omitted for native 48px clarity.
Body cue: V neck shirt. Shared parameters own mirrored elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-11/references/user-hair-mullet.svg'
SOURCE_HEAD_ICON_ID = 'user-hair-mullet'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24
class UserHairMulletAvatar(Solo48):
    icon_id = 'user-hair-mullet-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('avatars',)
    aliases = ()
    keywords = ('user', 'hair', 'mullet', 'portrait', 'bust')
    def build(self):
        cx = 24
        radius, cy = (10, 14)
        self.add_arc('crown', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
        self.add_arc('jaw', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
        self.add_contour('head', 'crown', 'jaw', closed=True)
        self.add_bezier('fringe', (14, 14), ((20, 16), (24, 12), (27, 9)), ((29, 12), (32, 14), (34, 14)))
        self.relate('connect', 'head', 'fringe')

        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('tail-'+side,(24+sign*10,14),((24+sign*10,18),(24+sign*12,20),(24+sign*16,20)))
            self.relate('connect','tail-'+side,'head')
            self.relate('connect','tail-'+side,'fringe')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-collar',(16,top),(24,40),(32,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.add_line('body-jacket-opening',(24,40),(24,44))
        self.relate('connect','body-jacket-opening','body-collar')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
