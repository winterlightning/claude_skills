"""Raised boxing gloves, guarded shoulders, and bent forearms.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
SQUARE exact envelope; detached head bottom 18, body top 26.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2a64d8a-ca70-53b9-b450-150287c2bfc6'
SOURCE_PATH = 'pictographic-primitives/avatars/boxer_c2a64d8a-ca70-53b9-b450-150287c2bfc6.svg'
AUTHOR='gpt-6'

class Boxer(Solo48):
    icon_id='boxer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'avatars'
    aliases=()
    keywords=('boxer', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('head-top',(18,12),(30,12),radius_x=6)
        self.add_arc('head-bottom',(30,12),(18,12),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        top=18+8
        self.add_polyline('body-shoulders',(14,30),(18,top),(24,top),(30,top),(34,30))
        for side,sign in [('left',-1),('right',1)]:
            cx=24+sign*14
            self.add_arc('glove-top-'+side,(cx-4,30),(cx+4,30),radius_x=4)
            self.add_arc('glove-bottom-'+side,(cx+4,30),(cx,34),radius_x=4)
            self.add_arc('glove-side-'+side,(cx,34),(cx-4,30),radius_x=4)
            self.add_contour('body-glove-'+side,'glove-top-'+side,'glove-bottom-'+side,'glove-side-'+side,closed=True)
            self.add_line('body-arm-'+side,(cx,34),(24+sign*10,42))
            self.relate('connect','body-glove-'+side,'body-shoulders')
            self.relate('connect','body-glove-'+side,'body-arm-'+side)
