"""Bartender holding a stemmed cocktail glass.

Fresh SOLO48 construction, not scaled from AVATAR64. Human reference:
icon_set/references/human_ref/user.svg; Lucide user-round/shirt construction.
VRECT_L exact envelope; detached head bottom 20, body top 28.
Small facial marks omitted; clothing/headwear carry the intended meaning.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea'
SOURCE_PATH = 'pictographic-primitives/avatars/bartainder_f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea.svg'
AUTHOR='gpt-6'

class Bartainder(Solo48):
    icon_id='bartainder'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='people/occupations'
    aliases=()
    keywords=('bartainder', 'bust', 'occupation', 'body')

    def build(self):
        # HRECT_L centerline box (4,8)-(44,40): figure at left, held glass at right.
        # Head r6 ends at y20 above the shoulder plateau y28: exactly four ink units.
        self.add_arc('head-top',(8,14),(20,14),radius_x=6)
        self.add_arc('head-bottom',(20,14),(8,14),radius_x=6)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('body-side',(4,40),(4,36))
        self.add_arc('body-shoulder',(4,36),(12,28),radius_x=8)
        self.add_polyline('body-arm',(12,28),(16,28),(22,36),(34,36))
        self.add_contour('body','body-side','body-shoulder','body-arm-1','body-arm-2','body-arm-3')
        self.contours=[c for c in self.contours if c.contour_id!='body-arm']
        self.add_polyline('cocktail',(24,24),(44,24),(34,36),closed=True)
        self.add_line('stem',(34,36),(34,40))
        self.relate('connect','cocktail','stem')
        self.relate('connect','body','cocktail')
        self.relate('connect','body','stem')
