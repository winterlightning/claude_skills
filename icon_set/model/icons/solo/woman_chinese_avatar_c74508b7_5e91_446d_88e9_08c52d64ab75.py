"""Restored a single central bun and wrapped blouse.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'c74508b7-5e91-446d-88e9-08c52d64ab75'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-chinese-1-avatar/20260926T181831Z-thuan-mac-1/reference/woman chinese_c74508b7-5e91-446d-88e9-08c52d64ab75.svg'
SOURCE_HEAD_ICON_ID = 'woman-chinese-1'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 28
class WomanChinese1Avatar(Solo48):
    icon_id = 'woman-chinese-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'japan', '2', 'portrait', 'bust')
    def build(self):
        self.add_arc('hair-left',(14,18),(20,8),radius_x=6,radius_y=10)
        self.add_arc('bun',(20,8),(28,8),radius_x=4)
        self.add_arc('hair-right',(28,8),(34,18),radius_x=6,radius_y=10)
        self.add_arc('face',(34,18),(14,18),radius_x=10)
        self.add_contour('head','hair-left','bun','hair-right','face',closed=True)
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(12,top),radius_x=4,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (12, top), (24, top))
        self.add_line('body-top-right', (24, top), (36, top))
        self.add_arc('body-right-shoulder',(36,top),(40,42),radius_x=4,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_polyline('body-wrap', (12,top), (24,44))
        self.relate('connect', 'body-wrap', 'body-top')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
