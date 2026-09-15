"""Backward (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5efa77c-db71-4315-a4b2-2794a901be6f'
SOURCE_PATH = 'pictographic-primitives/symbol/backward_c5efa77c-db71-4315-a4b2-2794a901be6f.svg'
AUTHOR = 'gpt-6'

class Backward(Solo48):
    icon_id = 'backward'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('backward', 'symbol')

    def build(self):
        self.add_line('e0', (24, 24), (44, 40))
        self.add_line('e1', (44, 40), (44, 8))
        self.add_line('e2', (44, 8), (24, 24))
        self.add_line('e3', (24, 8), (4, 24))
        self.add_line('e4', (4, 24), (24, 40))
        self.add_line('e5', (24, 40), (24, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
