"""Lengthened the sides of the veil.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '073a627a-8f91-4503-b153-f39c06b0805b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-muslim-avatar/20260926T181831Z-thuan-mac-1/reference/woman muslim_073a627a-8f91-4503-b153-f39c06b0805b.svg'
SOURCE_HEAD_ICON_ID = 'woman-muslim'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 30
class WomanMuslimAvatar(Solo48):
    icon_id = 'woman-muslim-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'muslim', 'portrait', 'bust')
    def build(self):
        self.add_arc('hood',(8,20),(40,20),radius_x=16)
        self.add_line('hood-left',(8,28),(8,20))
        self.add_line('hood-right',(40,20),(40,28))
        self.add_contour('veil','hood-left','hood', 'hood-right')
        self.add_arc('crown',(17,23),(31,23),radius_x=7)
        self.add_arc('face',(31,23),(17,23),radius_x=7)
        self.add_contour('head','crown','face',closed=True)
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
