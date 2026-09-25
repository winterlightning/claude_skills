"""A gift box with an overhanging lid and paired bow loops; band construction.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide gift: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0cf97133-d838-5225-91b3-5a912af64404'
SOURCE_PATH='pictographic-primitives/rewards/gift square with bow_0cf97133-d838-5225-91b3-5a912af64404.svg'
AUTHOR='gpt-6'

class SquareGiftBoxRibbonBand(Solo48):
    icon_id='square-gift-box-ribbon-band'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    aliases=()
    keywords=('award', 'reward', 'square-gift-box-ribbon-band')
    def build(self) -> None:
        axis=24
        for side,sign in [('left',-1),('right',1)]:
            x=axis+sign*9
            self.add_arc(side+'-bow-outer',(x,18),(x,4),radius_x=7,radius_y=7,sweep=sign==-1)
            self.add_arc(side+'-bow-inner',(x,4),(axis,18),radius_x=9,radius_y=14,sweep=sign==-1)
            self.add_contour(side+'-bow',side+'-bow-outer',side+'-bow-inner')
        self.add_polyline('lid',(8,18),(15,18),(24,18),(33,18),(40,18),(40,26),(38,26),(28,26),(24,26),(20,26),(10,26),(8,26),closed=True)
        self.relate('connect','left-bow','lid')
        self.relate('connect','right-bow','lid')
        self.relate('connect','left-bow','right-bow')
        self.add_line('body-left',(10,26),(10,40))
        self.add_arc('corner-left',(10,40),(14,44),radius_x=4,sweep=False)
        self.add_line('body-bottom-1',(14,44),(20,44))
        self.add_line('body-bottom-2',(20,44),(24,44))
        self.add_line('body-bottom-3',(24,44),(28,44))
        self.add_line('body-bottom-4',(28,44),(34,44))
        self.add_arc('corner-right',(34,44),(38,40),radius_x=4,sweep=False)
        self.add_line('body-right',(38,40),(38,26))
        self.add_contour('body','body-left','corner-left', 'body-bottom-1','body-bottom-2','body-bottom-3','body-bottom-4','corner-right','body-right')
        self.relate('connect','lid','body')
        self.add_line('ribbon-20',(20,18),(20,44))
        self.relate('connect','ribbon-20','lid')
        self.relate('connect','ribbon-20','body')
        self.add_line('ribbon-28',(28,18),(28,44))
        self.relate('connect','ribbon-28','lid')
        self.relate('connect','ribbon-28','body')

