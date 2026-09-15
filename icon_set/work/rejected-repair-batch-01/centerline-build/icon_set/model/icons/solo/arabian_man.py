"""Banded headcloth and a long central robe opening.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd92cb2d-e66d-53d1-835f-92be92e0873e'
SOURCE_PATH = 'pictographic-primitives/avatars/arabian man_dd92cb2d-e66d-53d1-835f-92be92e0873e.svg'
AUTHOR='gpt-6'

class ArabianMan(Solo48):
    icon_id='arabian-man'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('arabian', 'man', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_arc('cap',(18,12),(30,12),radius_x=6,radius_y=8)
        self.add_arc('face',(30,12),(18,12),radius_x=6,radius_y=8)
        self.add_contour('head','cap','face',closed=True)
        self.add_polyline('band',(12,12),(18,12),(30,12),(36,12))
        self.relate('connect','head','band')
        for side,sign in [('left',-1),('right',1)]:
            self.add_line('cloth-'+side,(24+sign*6,12),(24+sign*12,20))
            self.relate('connect','head','cloth-'+side)
            self.relate('connect','band','cloth-'+side)
        top=20+8  # exact 4-unit head/body ink gap
        radius=8
        self.add_line('body-left',(8,44),(8,top+radius))
        self.add_arc('body-shoulder-left',(8,top+radius),(16,top),radius_x=radius)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-shoulder-right',(32,top),(40,top+radius),radius_x=radius)
        self.add_line('body-right',(40,top+radius),(40,44))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-top-right','body-shoulder-right','body-right')
        self.add_line('robe-front',(24,top),(24,44))
        self.relate('connect','body','robe-front')
