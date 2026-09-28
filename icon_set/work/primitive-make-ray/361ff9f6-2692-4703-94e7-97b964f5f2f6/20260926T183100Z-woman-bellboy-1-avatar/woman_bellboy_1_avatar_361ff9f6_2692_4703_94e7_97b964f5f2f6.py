"""Replaced side rings with hair falling from the uniform cap.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '361ff9f6-2692-4703-94e7-97b964f5f2f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bellboy-1-avatar/20260926T181831Z-thuan-mac-1/reference/woman bellboy_361ff9f6-2692-4703-94e7-97b964f5f2f6.svg'
SOURCE_HEAD_ICON_ID = 'woman-bellboy-1'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 24
class WomanBellboy1Avatar(Solo48):
    icon_id = 'woman-bellboy-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'bellboy', '1', 'portrait', 'bust')
    def build(self):
        self.add_polyline('cap',(16,16),(16,4),(32,4),(32,16),(16,16))
        self.add_arc('face',(32,16),(16,16),radius_x=8)
        self.relate('connect','face','cap')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('side-hair-'+side,(24+sign*8,16),((24+sign*10,20),(24+sign*12,24),(24+sign*16,24)))
            self.relate('connect','side-hair-'+side,'face')
            self.relate('connect','side-hair-'+side,'cap')
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
