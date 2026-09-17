"""Information Letter: A lowercase information i has a small dot above its upright stem, a short upper serif, and a horizontal foot. Generate this component alone; exclude Magnifying Glass Frame.

Construction: A dotted lowercase i retains its left top serif and symmetric lower foot.
Keyshape: VRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '97df849d-b6c6-46d4-a2d1-185f60e93119'
SOURCE_PATH = 'pictographic-primitives/state/information magnifying glass_97df849d-b6c6-46d4-a2d1-185f60e93119.svg'
AUTHOR = 'gpt-6'


class InformationLetter(Sub32):
    icon_id = 'information-letter'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('information', 'letter', 'lowercase', 'i', 'small', 'dot', 'upright', 'stem')

    def build(self):
        self.add_dot('dot',(16,2))
        self.add_polyline('stem',(10,12),(16,12),(16,30))
        self.add_line('foot',(10,30),(22,30))
        self.relate('connect','stem','foot')
