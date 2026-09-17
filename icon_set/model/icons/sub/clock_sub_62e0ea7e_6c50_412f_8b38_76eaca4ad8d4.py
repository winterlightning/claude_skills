"""Clock: A round clock face contains two hands meeting centrally, with one pointing upward and the shorter hand pointing right. Generate this component alone; exclude Square File Frame.

Construction: A circular clock retains upright and rightward hands joined at centre.
Keyshape: CIRCLE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '62e0ea7e-6c50-412f-8b38-76eaca4ad8d4'
SOURCE_PATH = 'pictographic-primitives/state/file clock_62e0ea7e-6c50-412f-8b38-76eaca4ad8d4.svg'
AUTHOR = 'gpt-6'


class ClockSub(Sub32):
    icon_id = 'clock-sub'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('clock', 'round', 'face', 'contains', 'hands', 'meeting', 'centrally', 'pointing')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('face',16,16,14)
        self.add_polyline('hands',(16,9),(16,16),(22,16))
