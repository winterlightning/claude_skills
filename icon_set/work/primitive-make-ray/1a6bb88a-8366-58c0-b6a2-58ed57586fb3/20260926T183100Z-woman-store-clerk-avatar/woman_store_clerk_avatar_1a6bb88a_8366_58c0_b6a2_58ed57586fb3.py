"""Replaced the top bun with a clerk cap.
Compared the reference and current drawing. Anatomy follows human_ref/user.svg.
Lucide user-round informed circular and shoulder construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '1a6bb88a-8366-58c0-b6a2-58ed57586fb3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-store-clerk-avatar/20260926T181831Z-thuan-mac-1/reference/avatar woman store clerk_1a6bb88a-8366-58c0-b6a2-58ed57586fb3.svg'
SOURCE_HEAD_ICON_ID = 'woman-store-clerk'
AUTHOR = 'gpt-6'
ADDITIONAL_SOURCE_PATH = 'work/head-solo/batch-15/references/woman-store-clerk.svg'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24

class WomanStoreClerkAvatar(Solo48):
    icon_id = 'woman-store-clerk-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('avatar', 'woman', 'store', 'clerk', 'bust', 'body', 'portrait')

    def build(self):
        self.add_polyline('clerk-cap',(16,16),(16,4),(32,4),(32,16),(16,16))
        self.add_arc('face',(32,16),(16,16),radius_x=8)
        self.relate('connect','face','clerk-cap')
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
        self.add_polyline('body-bib',(18,top),(18,44),(30,44),(30,top))
        self.relate('connect','body-bib','body-top')
        self.relate('connect','body-bib','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
