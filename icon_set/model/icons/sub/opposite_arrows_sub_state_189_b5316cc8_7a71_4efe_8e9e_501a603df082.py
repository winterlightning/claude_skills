"""Opposite Arrows: Two horizontal arrows are stacked, the upper pointing left and the lower pointing right, each with an open angular head. Generate this component alone; exclude Circle Frame.

Construction: Two stacked open arrows preserve the leftward upper and rightward lower directions.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b5316cc8-7a71-4efe-8e9e-501a603df082'
SOURCE_PATH = 'pictographic-primitives/state/opposite arrows 1_b5316cc8-7a71-4efe-8e9e-501a603df082.svg'
AUTHOR = 'gpt-6'


class OppositeArrowsSubState189(Sub32):
    icon_id = 'opposite-arrows-sub-state-189'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('opposite', 'arrows', 'horizontal', 'are', 'stacked', 'upper', 'pointing', 'left')

    def build(self):
        self.add_line('upper',(2,8),(30,8))
        self.add_polyline('upper-head',(8,2),(2,8),(8,14))
        self.relate('connect','upper','upper-head')
        self.add_line('lower',(2,24),(30,24))
        self.add_polyline('lower-head',(24,18),(30,24),(24,30))
        self.relate('connect','lower','lower-head')
