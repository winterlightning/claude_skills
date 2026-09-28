"""Replaced apron stripes with the reference blouse collar.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '764772c4-8fbf-5060-9096-5379f4c4bd67'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-clerk-avatar/20260926T181831Z-thuan-mac-1/reference/woman clerk_764772c4-8fbf-5060-9096-5379f4c4bd67.svg'
SOURCE_HEAD_ICON_ID = 'woman-clerk'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 24
class WomanClerkAvatar(Solo48):
    icon_id = 'woman-clerk-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'clerk', 'portrait', 'bust')
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
        self.add_polyline('body-collar',(18,top),(24,40),(30,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
