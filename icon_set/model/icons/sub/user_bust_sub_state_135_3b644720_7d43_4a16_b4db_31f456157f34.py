"""User Bust: A round head is detached above a broad curved shoulder line, forming a front-facing bust without facial features. Generate this component alone; exclude House Frame.

Construction: A circular head floats over an open shoulder curve. Preserve the exact 4-unit head/body ink gap.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3b644720-7d43-4a16-b4db-31f456157f34'
SOURCE_PATH = 'pictographic-primitives/state/home user_3b644720-7d43-4a16-b4db-31f456157f34.svg'
AUTHOR = 'gpt-6'


class UserBustSubState135(Sub32):
    icon_id = 'user-bust-sub-state-135'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('user', 'bust', 'round', 'head', 'detached', 'broad', 'curved', 'shoulder')

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
