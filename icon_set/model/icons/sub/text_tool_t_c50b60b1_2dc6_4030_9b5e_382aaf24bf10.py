"""Text Tool T: An uppercase serif T has a broad horizontal top with short downward ends, a central upright stem, and a small horizontal foot. Generate this component alone; exclude Circle Frame.

Construction: A centred T has short hanging top serifs and a symmetric horizontal foot.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c50b60b1-2dc6-4030-9b5e-382aaf24bf10'
SOURCE_PATH = 'pictographic-primitives/state/circle text tool_c50b60b1-2dc6-4030-9b5e-382aaf24bf10.svg'
AUTHOR = 'gpt-6'


class TextToolT(Sub32):
    icon_id = 'text-tool-t'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('text', 'tool', 't', 'uppercase', 'serif', 'broad', 'horizontal', 'top')

    def build(self):
        self.add_polyline('top',(2,8),(2,2),(30,2),(30,8))
        self.add_line('stem',(16,2),(16,30))
        self.add_line('foot',(10,30),(22,30))
        self.relate('connect','top','stem')
        self.relate('connect','stem','foot')
