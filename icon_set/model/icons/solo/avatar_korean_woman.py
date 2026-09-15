"""Hanbok-inspired flared garment and tied crossover collar; no nationality implied by facial anatomy.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd16f1f81-7844-565c-b3b8-1b41d8de6f51'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar korean woman_d16f1f81-7844-565c-b3b8-1b41d8de6f51.svg'
AUTHOR='gpt-6'

class AvatarKoreanWoman(Solo48):
    icon_id='avatar-korean-woman'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'korean', 'woman', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(16,12),(32,12),radius_x=8)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('hair-part',(16,12),(32,12))
        self.relate('connect','head','hair-part')
        top=20+8  # exact 4-unit head/body ink gap
        self.add_polyline('body',(8,44),(16,top),(24,top),(32,top),(40,44),closed=True)
        self.add_polyline('garment-tie',(16,top),(24,36),(32,top))
        self.relate('connect','body','garment-tie')
