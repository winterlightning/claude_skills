"""Bed: A bed appears from the side as a long rectangular mattress between two upright posts. The left post rises well above the mattress, while both posts extend below it.

Construction: Plain bed retains tall left bedpost, single empty mattress and short feet; no pillow invented.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '300dd66a-1ed3-4055-80d4-1d8fabe4b3ef'
SOURCE_PATH = 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'
AUTHOR = 'gpt-6'


class BedSubState27(Sub32):
    icon_id = 'bed-sub-state-27'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('bed', 'appears', 'side', 'long', 'rectangular', 'mattress', 'between', 'upright')

    def build(self):
        self.add_line('post',(2,2),(2,30))
        self.add_polyline('mattress',(2,14),(30,14),(30,24),(2,24))
        self.add_line('foot',(30,24),(30,30))
        self.relate('connect','post','mattress')
        self.relate('connect','foot','mattress')
