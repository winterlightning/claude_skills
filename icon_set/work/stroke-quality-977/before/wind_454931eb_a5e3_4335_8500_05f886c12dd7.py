"""Wind (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '454931eb-a5e3-4335-8500-05f886c12dd7'
SOURCE_PATH = 'pictographic-primitives/symbol/wind_454931eb-a5e3-4335-8500-05f886c12dd7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WindSymbol(Solo48):
    icon_id = 'wind-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('wind', 'symbol')

    def build(self):
        self.add_line('e0', (4, 8), (44, 8))
        self.add_line('e1', (4, 40), (34, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
