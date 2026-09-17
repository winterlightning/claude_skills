"""Arrow Down Right: A long diagonal arrow descends from upper left to lower right. Its open head has horizontal and vertical arms meeting at the endpoint, with rounded ends on the broad strokes.

Construction: A diagonal arrow retains the original lower-right open right-angle head.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4762972f-9ac5-49f3-81e6-908440ac9d34'
SOURCE_PATH = 'pictographic-primitives/state/decrease_4762972f-9ac5-49f3-81e6-908440ac9d34.svg'
AUTHOR = 'gpt-6'


class ArrowDownRightState108(Sub32):
    icon_id = 'arrow-down-right-state-108'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('arrow', 'down', 'right', 'long', 'diagonal', 'descends', 'upper', 'left')

    def build(self):
        self.add_line('shaft',(2,2),(30,30))
        self.add_polyline('head',(18,30),(30,30),(30,18))
        self.relate('connect','shaft','head')
