"""Side ponytail, diagonal apron strap, and a counter edge.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID=None
SOURCE_PATH='work/head-solo/batch-01/references/avatar-woman-store-clerk-3.svg'
AUTHOR='gpt-6'

class AvatarWomanStoreClerk3(Solo48):
    icon_id='avatar-woman-store-clerk-3'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'woman', 'store', 'clerk', '3', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(16,12),(32,12),radius_x=8)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('ponytail',(32,12),((40,12),(32,16),(38,20)))
        self.relate('connect','head','ponytail')
        top=20+8  # exact 4-unit head/body ink gap
        radius=8
        self.add_line('body-left',(8,44),(8,top+radius))
        self.add_arc('body-shoulder-left',(8,top+radius),(16,top),radius_x=radius)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-shoulder-right',(32,top),(40,top+radius),radius_x=radius)
        self.add_line('body-right',(40,top+radius),(40,44))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-top-right','body-shoulder-right','body-right')
        self.add_line('apron-strap',(16,top),(32,44))
        self.relate('connect','body','apron-strap')
        self.add_line('counter',(8,44),(40,44))
        self.relate('connect','body','counter')
        self.relate('connect','apron-strap','counter')
