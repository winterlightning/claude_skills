"""Pillbox hat and an angled neck scarf.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22284429-fd82-4a8b-99c0-c7586e3ab52d'
SOURCE_PATH = 'pictographic-primitives/avatars/woman air hostess_22284429-fd82-4a8b-99c0-c7586e3ab52d.svg'
AUTHOR='gpt-6'

class AvatarWomanAirHostess1(Solo48):
    icon_id='avatar-woman-air-hostess-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('avatar', 'woman', 'air', 'hostess', '1', 'bust', 'occupation', 'body')

    def build(self):
        # Plan: independent head, garment, and intrinsic clothing/tool details.
        # Paired body/hair parts derive from one axis; shared nodes keep real joins.
        self.add_polyline('hat',(16,12),(20,4),(28,4),(32,12))
        self.add_arc('face',(32,12),(16,12),radius_x=8)
        self.add_contour('head','hat-1','hat-2','hat-3','face',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='hat']
        top=20+8  # exact 4-unit head/body ink gap
        radius=8
        self.add_line('body-left',(8,44),(8,top+radius))
        self.add_arc('body-shoulder-left',(8,top+radius),(16,top),radius_x=radius)
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-shoulder-right',(32,top),(40,top+radius),radius_x=radius)
        self.add_line('body-right',(40,top+radius),(40,44))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-top-right','body-shoulder-right','body-right')
        self.add_line('scarf',(24,top),(32,36))
        self.relate('connect','body','scarf')
