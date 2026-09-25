"""Unequal Vertical Lines: Two detached upright strokes share their top alignment; the left stroke is short and the right extends substantially farther downward. Generate this component alone; exclude Magnifying Glass Frame.

Construction: Two parallel strokes share a top alignment; only the right stroke spans full height.
Keyshape: VRECT_S; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2494ab3a-0153-4551-abf7-8f991c29e1b4'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass barcode_2494ab3a-0153-4551-abf7-8f991c29e1b4.svg'
AUTHOR = 'gpt-6'


class UnequalVerticalLines(Sub32):
    icon_id = 'unequal-vertical-lines'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('unequal', 'vertical', 'lines', 'detached', 'upright', 'strokes', 'share', 'top')

    def build(self):
        self.add_line("left",(10,2),(10,16))
        self.add_line("right",(22,2),(22,30))
