"""Arrow bottom (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'
AUTHOR = 'gpt-6'

class ArrowBottomSymbol(Solo48):
    icon_id = 'arrow-bottom-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'bottom', 'symbol')

    def build(self):
        self.add_line('sym-e1', (24, 40), (23, 38))
        self.add_line('sym-e2', (23, 38), (4, 8))
        self.add_line('sym-e3', (24, 40), (25, 38))
        self.add_line('sym-e4', (25, 38), (44, 8))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
