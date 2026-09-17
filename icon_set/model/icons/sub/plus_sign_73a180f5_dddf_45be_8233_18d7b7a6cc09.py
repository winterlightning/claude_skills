"""Plus Sign: A long horizontal line crosses a matching upright line at their centres. Four straight, evenly balanced arms extend from the junction, with no surrounding enclosure or added marks.

Construction: Equal orthogonal strokes cross at the common centre.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '73a180f5-dddf-45be-8233-18d7b7a6cc09'
SOURCE_PATH = 'pictographic-primitives/state/add 1_73a180f5-dddf-45be-8233-18d7b7a6cc09.svg'
AUTHOR = 'gpt-6'


class PlusSign(Sub32):
    icon_id = 'plus-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('plus', 'sign', 'long', 'horizontal', 'line', 'crosses', 'matching', 'upright')

    def build(self):
        self.add_line('horizontal',(2,16),(30,16))
        self.add_line('vertical',(16,2),(16,30))
        self.relate('connect','horizontal','vertical')
