"""User Bust: A circular head sits above an open semicircular shoulder line. Generate this component alone; exclude Circle Frame, Minus Sign.

Construction: A circular head above open shoulders; body-top is head-bottom plus 8 centreline units (4 ink).
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9f8da9e5-3911-4d36-a97e-ea83c9dff05a'
SOURCE_PATH = 'pictographic-primitives/state/circle user minus_9f8da9e5-3911-4d36-a97e-ea83c9dff05a.svg'
AUTHOR = 'gpt-6'


class UserBustSub(Sub32):
    icon_id = 'user-bust-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'circular', 'head', 'sits', 'open', 'semicircular', 'shoulder')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('head',16,8,6)
        self.add_arc('shoulders',(2,30),(30,30),radius_x=14,radius_y=8)
