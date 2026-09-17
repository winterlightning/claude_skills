"""Information Letter: A lowercase i has a small dot, a leftward top serif, and a broad horizontal foot. Generate this component alone; exclude Service Sign Frame.

Construction: The source lowercase i keeps its dot, left top serif and horizontal foot.
Keyshape: VRECT_S; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1d605b1a-dfb6-4b6d-8d4d-0fa80165b3e6'
SOURCE_PATH = 'pictographic-primitives/state/public service information_1d605b1a-dfb6-4b6d-8d4d-0fa80165b3e6.svg'
AUTHOR = 'gpt-6'


class InformationLetterState221(Sub32):
    icon_id = 'information-letter-state-221'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('information', 'letter', 'lowercase', 'i', 'small', 'dot', 'leftward', 'top')

    def build(self):
        self.add_dot('dot',(16,2))
        self.add_polyline('stem',(10,12),(16,12),(16,30))
        self.add_line('foot',(10,30),(22,30))
        self.relate('connect','stem','foot')
