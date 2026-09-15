"""Bobbed hair, full apron outline, and a large pocket opening.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a6bb88a-8366-58c0-b6a2-58ed57586fb3'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar woman store clerk_1a6bb88a-8366-58c0-b6a2-58ed57586fb3.svg'
AUTHOR='gpt-6'

class AvatarWomanStoreClerk(Solo48):
    icon_id='avatar-woman-store-clerk'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'woman', 'store', 'clerk', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(16,12),(32,12),radius_x=8)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8)
        self.add_contour('head','head-top','head-bottom',closed=True)
        for side,sign in [('left',-1),('right',1)]:
            self.add_arc('hair-'+side,(24+sign*8,12),(24+sign*12,20),radius_x=10,sweep=sign<0)
            self.relate('connect','head','hair-'+side)
        top=20+8  # exact 4-unit head/body ink gap
        self.add_polyline('body',(8,44),(16,top),(24,top),(32,top),(40,44),closed=True)
        self.add_line('apron-pocket',(22,36),(26,36))
