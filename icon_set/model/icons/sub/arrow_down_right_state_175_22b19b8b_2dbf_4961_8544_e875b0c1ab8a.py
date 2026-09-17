"""Arrow Down Right: A long diagonal arrow points lower-right, ending in an open right-angle head. Generate this component alone; exclude Rectangle Frame.

Construction: A long descending-right shaft has the original horizontal/vertical open head.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '22b19b8b-2dbf-4961-8544-e875b0c1ab8a'
SOURCE_PATH = 'pictographic-primitives/state/minimize 1_22b19b8b-2dbf-4961-8544-e875b0c1ab8a.svg'
AUTHOR = 'gpt-6'


class ArrowDownRightState175(Sub32):
    icon_id = 'arrow-down-right-state-175'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'down', 'right', 'long', 'diagonal', 'points', 'lower', 'ending')

    def build(self):
        self.add_line('shaft',(2,2),(30,30))
        self.add_polyline('head',(18,30),(30,30),(30,18))
        self.relate('connect','shaft','head')
