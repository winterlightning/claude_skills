"""Lightning Stroke: A single open zigzag runs diagonally downward, with a short rising middle connector between two longer sloping strokes. Generate this component alone; exclude Circle Frame.

Construction: The source open lightning zigzag has two long diagonals joined by a rising middle connector.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2b4409be-55d3-48c3-8532-8aec9fae3a0a'
SOURCE_PATH = 'pictographic-primitives/state/lightning_2b4409be-55d3-48c3-8532-8aec9fae3a0a.svg'
AUTHOR = 'gpt-6'


class LightningStroke(Sub32):
    icon_id = 'lightning-stroke'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('lightning', 'stroke', 'single', 'open', 'zigzag', 'runs', 'diagonally', 'downward')

    def build(self):
        self.add_polyline('bolt',(24,2),(6,18),(26,12),(10,30))
