"""User Bust: A detached round head sits above an open curved shoulder line. Generate this component alone; exclude Circle Frame, Check Mark.

Construction: A circular detached head and open shoulders preserve the source bust; exclude its check and frame. Ink gap is 4.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3672312c-a1d4-4a31-9b5b-3ec081129ab9'
SOURCE_PATH = 'pictographic-primitives/state/user check_3672312c-a1d4-4a31-9b5b-3ec081129ab9.svg'
AUTHOR = 'gpt-6'


class UserBustSubState290(Sub32):
    icon_id = 'user-bust-sub-state-290'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'detached', 'round', 'head', 'sits', 'open', 'curved')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('head',16,8,6)
        self.add_arc('shoulders',(2,30),(30,30),radius_x=14,radius_y=8)
