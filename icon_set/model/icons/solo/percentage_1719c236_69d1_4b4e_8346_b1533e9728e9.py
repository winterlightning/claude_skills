"""Percentage (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1719c236-69d1-4b4e-8346-b1533e9728e9'
SOURCE_PATH = 'pictographic-primitives/symbol/percentage_1719c236-69d1-4b4e-8346-b1533e9728e9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Percentage(Solo48):
    icon_id = 'percentage'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('percentage', 'symbol')

    def build(self):
        self.add_line('sym-e0', (4, 24), (44, 24))
        self.add_line('sym-e1', (24, 8), (24, 8))
        self.add_line('sym-e2', (24, 40), (24, 40))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', closed=True)
        self.add_contour('sym-c2', 'sym-e2', closed=True)
