"""A gift box with an overhanging lid and paired bow loops; band-wide construction.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide gift: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='392b9a89-3262-5132-b463-ac6157afcc22'
SOURCE_PATH='pictographic-primitives/rewards/gift rectangle with bow_392b9a89-3262-5132-b463-ac6157afcc22.svg'
AUTHOR='gpt-6'

class RectangularGiftBoxRibbonBand(Solo48):
    icon_id='rectangular-gift-box-ribbon-band'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'rewards'
    categories = ('rewards', 'primitives')
    aliases=()
    keywords=('award', 'reward', 'rectangular-gift-box-ribbon-band')
    def build(self) -> None:
        axis=24
        for side,sign in [('left',-1),('right',1)]:
            x=axis+sign*9
            self.add_arc(side+'-bow-outer',(x,18),(x,6),radius_x=6,radius_y=6,sweep=sign==-1)
            self.add_arc(side+'-bow-inner',(x,6),(axis,18),radius_x=9,radius_y=12,sweep=sign==-1)
            self.add_contour(side+'-bow',side+'-bow-outer',side+'-bow-inner')
        self.add_polyline('lid',(6,18),(15,18),(24,18),(33,18),(42,18),(42,26),(40,26),(28,26),(24,26),(20,26),(8,26),(6,26),closed=True)
        self.relate('connect','left-bow','lid')
        self.relate('connect','right-bow','lid')
        self.relate('connect','left-bow','right-bow')
        self.add_line('body-left',(8,26),(8,38))
        self.add_arc('corner-left',(8,38),(12,42),radius_x=4,sweep=False)
        self.add_line('body-bottom-1',(12,42),(20,42))
        self.add_line('body-bottom-2',(20,42),(24,42))
        self.add_line('body-bottom-3',(24,42),(28,42))
        self.add_line('body-bottom-4',(28,42),(36,42))
        self.add_arc('corner-right',(36,42),(40,38),radius_x=4,sweep=False)
        self.add_line('body-right',(40,38),(40,26))
        self.add_contour('body','body-left','corner-left', 'body-bottom-1','body-bottom-2','body-bottom-3','body-bottom-4','corner-right','body-right')
        self.relate('connect','lid','body')
        self.add_line('ribbon-20',(20,18),(20,42))
        self.relate('connect','ribbon-20','lid')
        self.relate('connect','ribbon-20','body')
        self.add_line('ribbon-28',(28,18),(28,42))
        self.relate('connect','ribbon-28','lid')
        self.relate('connect','ribbon-28','body')

