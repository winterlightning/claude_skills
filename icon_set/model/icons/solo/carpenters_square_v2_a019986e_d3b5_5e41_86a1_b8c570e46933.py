# Variant of carpenters-square; parent file remains unchanged.
"""An L-shaped measuring square with sparse edge ticks; dense graduations reduced to two per arm."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a019986e-d3b5-5e41-86a1-b8c570e46933'
SOURCE_PATH = 'pictographic-primitives/tools/measure ruler corner_a019986e-d3b5-5e41-86a1-b8c570e46933.svg'
AUTHOR = 'gpt-6'

class CarpentersSquareVariant2(Solo48):
    icon_id = 'carpenters-square-v2'
    variant_of = 'carpenters-square'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('square', 'carpenter square', 'ruler', 'measure', 'angle', 'right angle', 'carpentry', 'tool')

    def build(self) -> None:
        self.add_polyline('square', (6, 6), (18, 6), (18, 30), (42, 30), (42, 42), (6, 42), closed=True)
        for j, y in enumerate((16, 26)):
            self.add_line('vertical-tick' + str(j), (6, y), (10, y))
            self.relate('connect', 'vertical-tick' + str(j), 'square')
        for j, x in enumerate((26, 34)):
            self.add_line('horizontal-tick' + str(j), (x, 38), (x, 42))
            self.relate('connect', 'horizontal-tick' + str(j), 'square')
