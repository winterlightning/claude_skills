"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('W-shaped four diagonal strokes', 'one horizontal crossbar')

class Drawing(Sub32):
    icon_id = 'south-korean-won-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    categories = ('money', 'state', 'other', 'primitives-generate')
    keywords = ('south', 'korean', 'won', 'symbol')


    def build(self):
        # Currency symbol, not an invented letter glyph; retain the source's single bar.
        self.add_polyline('won',(2,2),(9,30),(16,2),(23,30),(30,2))
        self.add_line('bar',(2,16),(30,16))
        for i in range(1,5):self.relate('connect','bar',f'won-{i}')

