"""Widened the mortarboard and simplified the gown.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '41f44b4e-c542-4e70-ad5b-0876a3323d5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-graduate-avatar/20260926T181831Z-thuan-mac-1/reference/woman graduate_41f44b4e-c542-4e70-ad5b-0876a3323d5c.svg'
SOURCE_HEAD_ICON_ID = 'woman-graduate'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 32
class WomanGraduateAvatar(Solo48):
    icon_id = 'woman-graduate-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'graduate', 'portrait', 'bust')
    def build(self):
        self.add_polyline('mortarboard',(8,12),(24,4),(40,12),(24,16),(8,12))
        self.add_arc('crown-left',(16,24),(24,16),radius_x=8)
        self.add_arc('crown-right',(24,16),(32,24),radius_x=8)
        self.add_arc('jaw',(32,24),(16,24),radius_x=8)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.relate('connect','head','mortarboard')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('side-hair-'+side,(24+sign*8,24),((24+sign*12,26),(24+sign*14,28),(24+sign*16,28)))
            self.relate('connect','side-hair-'+side,'head')
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
        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
