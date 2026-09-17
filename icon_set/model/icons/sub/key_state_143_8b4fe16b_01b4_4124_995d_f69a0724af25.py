"""Key: A round key bow sits on the right of a horizontal shaft, with two short teeth hanging downward near its left end. Generate this component alone; exclude Rounded Rectangle Frame.

Construction: A horizontal shaft joins the round right bow, with the two short downward teeth shown in the source.
Keyshape: HRECT_S; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8b4fe16b-01b4-4124-995d-f69a0724af25'
SOURCE_PATH = 'pictographic-primitives/state/key horizontal rectangle_8b4fe16b-01b4-4124-995d-f69a0724af25.svg'
AUTHOR = 'gpt-6'


class KeyState143(Sub32):
    icon_id = 'key-state-143'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('key', 'round', 'bow', 'sits', 'right', 'horizontal', 'shaft', 'short')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('bow',24,16,6)
        self.add_line('shaft',(2,16),(18,16))
        self.relate('connect','shaft','bow')
        for name,x in (('left',2),('right',10)):
            self.add_line(name,(x,16),(x,22))
            self.relate('connect','shaft',name)
