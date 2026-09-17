"""Letter P: An uppercase P has a tall straight stem and a broad rounded upper bowl attached at the top and midpoint. Generate this component alone; exclude Circle Frame.

Construction: The source uppercase P retains its straight upright and broad upper bowl.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7a0a5a74-2cd2-4105-8871-da4e0f06179e'
SOURCE_PATH = 'pictographic-primitives/state/parking_7a0a5a74-2cd2-4105-8871-da4e0f06179e.svg'
AUTHOR = 'gpt-6'


class LetterPSubState192(Sub32):
    icon_id = 'letter-p-sub-state-192'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('letter', 'p', 'uppercase', 'tall', 'straight', 'stem', 'broad', 'rounded')

    def build(self):
        self.add_line('stem',(6,2),(6,30))
        self.add_line('top',(6,2),(16,2))
        self.add_arc('round',(16,2),(16,18),radius_x=10,radius_y=8)
        self.add_line('middle',(16,18),(6,18))
        self.add_contour('bowl','top','round','middle')
        self.relate('connect','stem','bowl')
