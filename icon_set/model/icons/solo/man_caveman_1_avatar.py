"""man-caveman-1: one shoulder hide and reference headwear/hair silhouette.
SOLO48 VRECT_L ink bounds (6,2)-(42,46). Circular face centered x24;
head bottom 30, shoulders 34, zero visible contact gap. Curved shoulders
follow human_ref/user.svg; Lucide user-round original and atomic-debug inform
cardinal arcs. Fine face/trim details omitted at 48; body cue: one shoulder hide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-04/references/man-caveman-1.svg'
SOURCE_HEAD_ICON_ID = 'man-caveman-1'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class ManCaveman1Avatar(Solo48):
    icon_id = 'man-caveman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'caveman', '1', 'portrait', 'bust')
    def build(self):
        for side, cx in [('left',12),('right',36)]:
            self.add_arc('bone-top-'+side,(cx-4,8),(cx+4,8),radius_x=4)
            self.add_line('bone-out-'+side,(cx+4,8),(cx+4,16))
            self.add_arc('bone-bottom-'+side,(cx+4,16),(cx-4,16),radius_x=4)
            self.add_line('bone-in-'+side,(cx-4,16),(cx-4,8))
            self.add_contour('bone-'+side,'bone-top-'+side,'bone-out-'+side,'bone-bottom-'+side,'bone-in-'+side,closed=True)
        self.add_line('shaft',(16,12),(32,12))
        self.relate('connect','shaft','bone-left')
        self.relate('connect','shaft','bone-right')
        self.add_polyline('forehead',(12,20),(14,20),(34,20),(36,20))
        self.add_arc('face',(34,20),(14,20),radius_x=10)
        self.relate('connect','face','forehead')
        for side in ['left','right']:
            self.relate('connect','forehead','bone-'+side)
            self.relate('connect','face','bone-'+side)
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
        self.add_line('body-wrap',(8,42),(30,44))
        self.relate('connect','body-wrap','body-left')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
