"""woman-store-clerk: closed shop apron bib.
Distinct-avatar plan: preserve reference identity; use closed shop apron bib.
SOLO48 VRECT_L centerline (8,4)-(40,44), circular face centered x24.
Head bottom 28; shoulder top 32; zero painted head/body gap.
Human user.svg guides curved shoulders; Lucide user-round guides smooth arcs.
Fine facial marks and trim omitted for native-size clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '1a6bb88a-8366-58c0-b6a2-58ed57586fb3'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar woman store clerk_1a6bb88a-8366-58c0-b6a2-58ed57586fb3.svg'
SOURCE_HEAD_ICON_ID = 'avatar-woman-store-clerk'
AUTHOR = 'gpt-6'
ADDITIONAL_SOURCE_PATH = 'work/head-solo/batch-15/references/woman-store-clerk.svg'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 28

class WomanStoreClerkAvatar(Solo48):
    icon_id = 'woman-store-clerk-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'woman', 'store', 'clerk', 'bust', 'body', 'portrait')

    def build(self):
        self.add_arc('hair-left',(14,18),(20,8),radius_x=6,radius_y=10)
        self.add_arc('bun',(20,8),(28,8),radius_x=4)
        self.add_arc('hair-right',(28,8),(34,18),radius_x=6,radius_y=10)
        self.add_arc('face',(34,18),(14,18),radius_x=10)
        self.add_contour('head','hair-left','bun','hair-right','face',closed=True)
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

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
