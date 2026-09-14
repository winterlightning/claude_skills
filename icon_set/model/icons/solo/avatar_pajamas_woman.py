"""Slouched sleeping cap and two pajama buttons.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 18, body top 26.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID=None
SOURCE_PATH='work/head-solo/batch-01/references/avatar-pajamas-woman.svg'
AUTHOR='gpt-6'

class AvatarPajamasWoman(Solo48):
    icon_id='avatar-pajamas-woman'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'pajamas', 'woman', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_polyline('sleep-cap',(16,12),(24,4),(36,8),(32,12))
        self.add_arc('face',(32,12),(16,12),radius_x=8,radius_y=6)
        self.add_contour('head','sleep-cap-1','sleep-cap-2','sleep-cap-3','face',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='sleep-cap']
        top=18+8  # exact 4-unit head/body ink gap
        radius=8
        self.add_line('body-left',(8,44),(8,top+radius))
        self.add_arc('body-shoulder-left',(8,top+radius),(16,top),radius_x=radius)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-shoulder-right',(32,top),(40,top+radius),radius_x=radius)
        self.add_line('body-right',(40,top+radius),(40,44))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-top-right','body-shoulder-right','body-right')
        for y in (35,43): self.add_dot('button-'+str(y),(24,y))
