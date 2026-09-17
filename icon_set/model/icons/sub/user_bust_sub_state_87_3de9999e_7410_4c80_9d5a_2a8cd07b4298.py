"""User Bust: A circular head floats above a curved shoulder line. Generate this component alone; exclude Circle Frame, Plus Sign.

Construction: The detached circular head and open shoulders preserve the source; exclude its plus and frame. Head/body ink gap is 4.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3de9999e-7410-4c80-9d5a-2a8cd07b4298'
SOURCE_PATH = 'pictographic-primitives/state/circle user plus_3de9999e-7410-4c80-9d5a-2a8cd07b4298.svg'
AUTHOR = 'gpt-6'


class UserBustSubState87(Sub32):
    icon_id = 'user-bust-sub-state-87'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'circular', 'head', 'floats', 'curved', 'shoulder', 'line')

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
