"""Opposite Arrows: Two horizontal arrows are stacked, the upper pointing left and the lower pointing right, each with an open angular head. Generate this component alone; exclude Circle Frame.

Construction: Two horizontal arrows point opposite ways, with open heads and equal shaft lengths.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7fdae893-6305-4c14-99a8-4d910f53eb71'
SOURCE_PATH = 'pictographic-primitives/state/opposite arrows 1_7fdae893-6305-4c14-99a8-4d910f53eb71.svg'
AUTHOR = 'gpt-6'


class OppositeArrowsSub(Sub32):
    icon_id = 'opposite-arrows-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('opposite', 'arrows', 'horizontal', 'are', 'stacked', 'upper', 'pointing', 'left')

    def build(self):
        self.add_line('upper',(2,8),(30,8))
        self.add_polyline('upper-head',(8,2),(2,8),(8,14))
        self.relate('connect','upper','upper-head')
        self.add_line('lower',(2,24),(30,24))
        self.add_polyline('lower-head',(24,18),(30,24),(24,30))
        self.relate('connect','lower','lower-head')
