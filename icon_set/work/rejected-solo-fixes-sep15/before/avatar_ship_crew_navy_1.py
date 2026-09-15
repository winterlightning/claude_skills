"""Flat sailor cap and broad V-shaped naval collar.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cba73ce9-9aea-4551-91dd-9549fb2c89f4'
SOURCE_PATH = 'pictographic-primitives/avatars/ship crew navy_cba73ce9-9aea-4551-91dd-9549fb2c89f4.svg'
AUTHOR='gpt-6'

class AvatarShipCrewNavy1(Solo48):
    icon_id='avatar-ship-crew-navy-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'ship', 'crew', 'navy', '1', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_polyline('cap',(16,12),(16,4),(32,4),(32,12))
        self.add_arc('face',(32,12),(16,12),radius_x=8)
        self.add_contour('head','cap-1','cap-2','cap-3','face',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='cap']
        self.add_line('brim',(16,12),(32,12))
        self.relate('connect','head','brim')
        top=20+8  # exact 4-unit head/body ink gap
        self.add_polyline('body',(8,44),(8,top+4),(12,top),(24,top),(36,top),(40,top+4),(40,44))
        self.add_polyline('vest',(12,top),(24,40),(36,top))
        self.relate('connect','body','vest')
