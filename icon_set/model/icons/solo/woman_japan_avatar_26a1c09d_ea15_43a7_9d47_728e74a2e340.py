"""Restored the broad conical hat.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '26a1c09d-ea15-43a7-9d47-728e74a2e340'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-japan-avatar/20260926T181831Z-thuan-mac-1/reference/woman japan_26a1c09d-ea15-43a7-9d47-728e74a2e340.svg'
SOURCE_HEAD_ICON_ID = 'woman-japan'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 26
class WomanJapanAvatar(Solo48):
    icon_id = 'woman-japan-avatar-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('woman', 'japan', 'portrait', 'bust')
    def build(self):
        self.add_polyline('conical-hat',(8,16),(24,4),(40,16),(8,16))
        self.add_arc('face',(34,16),(14,16),radius_x=10)
        self.relate('connect','conical-hat','face')
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
        self.add_polyline('body-wrap', (36,top), (24,44))
        self.relate('connect', 'body-wrap', 'body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
