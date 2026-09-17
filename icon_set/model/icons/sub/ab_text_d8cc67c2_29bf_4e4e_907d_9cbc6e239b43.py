"""AB lettering: preserve the original A followed by a rounded B.
Construction: The A uses a broader open counter and crossbar; two rounded B bowls retain the original letter ordering.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd8cc67c2-29bf-4e4e-907d-9cbc6e239b43'
SOURCE_PATH = 'pictographic-primitives/state/ab text in circle_d8cc67c2-29bf-4e4e-907d-9cbc6e239b43.svg'
AUTHOR = 'gpt-6'
class AbText(Sub32):
    icon_id = 'ab-text'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('a','b','letters','text')
    def build(self):
        self.add_polyline('a',(2,28),(8,4),(14,28))
        self.add_line('a-bar',(4,20),(12,20))
        self.relate('connect','a','a-bar')
        self.add_line('stem',(20,4),(20,28))
        for name,y in (('upper',4),('lower',16)):
            self.add_line(name+'-top',(20,y),(25,y))
            self.add_arc(name+'-bowl',(25,y),(25,y+12),radius_x=5,radius_y=6)
            self.add_line(name+'-base',(25,y+12),(20,y+12))
            self.add_contour(name,name+'-top',name+'-bowl',name+'-base')
            self.relate('connect','stem',name)
        self.relate('connect','upper','lower')
