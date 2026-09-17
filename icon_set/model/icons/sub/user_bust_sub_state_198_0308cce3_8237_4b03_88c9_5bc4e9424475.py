"""User Bust: A round head floats above broad open shoulders whose right contour stops beside the badge. Generate this component alone; exclude Circle Frame, Minus Sign.

Construction: A detached head and shoulders preserve the interrupted right shoulder from the source badge layout; exclude the badge.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0308cce3-8237-4b03-88c9-5bc4e9424475'
SOURCE_PATH = 'pictographic-primitives/state/person with minus_0308cce3-8237-4b03-88c9-5bc4e9424475.svg'
AUTHOR = 'gpt-6'


class UserBustSubState198(Sub32):
    icon_id = 'user-bust-sub-state-198'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'round', 'head', 'floats', 'broad', 'open', 'shoulders')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('head',16,8,6)
        self.add_arc('left-shoulder',(2,30),(16,22),radius_x=14,radius_y=8)
        self.add_arc('right-shoulder',(16,22),(30,26),radius_x=14,radius_y=4)
        self.add_contour('shoulders','left-shoulder','right-shoulder')
