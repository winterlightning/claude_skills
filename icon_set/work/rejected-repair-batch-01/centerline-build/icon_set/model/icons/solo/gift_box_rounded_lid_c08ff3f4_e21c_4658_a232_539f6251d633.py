"""A gift box with an overhanging lid and paired bow loops; rounded construction.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide gift: geometric construction; supplied reference: subject identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH='pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR='gpt-6'

class GiftBoxRoundedLid(Solo48):
    icon_id='gift-box-rounded-lid'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/award'
    aliases=()
    keywords=('award', 'reward', 'gift-box-rounded-lid')
    def build(self) -> None:
        axis=24
        for side,sign in [('left',-1),('right',1)]:
            x=axis+sign*9
            self.add_arc(side+'-bow-outer',(x,18),(x,4),radius_x=7,radius_y=7,sweep=sign==-1)
            self.add_arc(side+'-bow-inner',(x,4),(axis,18),radius_x=9,radius_y=14,sweep=sign==-1)
            self.add_contour(side+'-bow',side+'-bow-outer',side+'-bow-inner')
        self.add_line('lid-top-1',(10,18),(15,18))
        self.add_line('lid-top-2',(15,18),(24,18))
        self.add_line('lid-top-3',(24,18),(33,18))
        self.add_line('lid-top-4',(33,18),(38,18))
        self.add_arc('lid-tr',(38,18),(40,20),radius_x=2)
        self.add_line('lid-right',(40,20),(40,24))
        self.add_arc('lid-br',(40,24),(38,26),radius_x=2)
        self.add_line('lid-bottom',(38,26),(10,26))
        self.add_arc('lid-bl',(10,26),(8,24),radius_x=2)
        self.add_line('lid-left',(8,24),(8,20))
        self.add_arc('lid-tl',(8,20),(10,18),radius_x=2)
        self.add_contour('lid','lid-top-1','lid-top-2','lid-top-3','lid-top-4','lid-tr','lid-right','lid-br','lid-bottom','lid-bl','lid-left','lid-tl',closed=True)
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

