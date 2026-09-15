"""Empty house (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29ab3c8f-12f3-44a1-8ae9-a7fbc43d5d76'
SOURCE_PATH = 'pictographic-primitives/symbol/empty house_29ab3c8f-12f3-44a1-8ae9-a7fbc43d5d76.svg'
AUTHOR = 'gpt-6'

class EmptyHouse(Solo48):
    icon_id = 'empty-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('empty', 'house', 'symbol')

    def build(self):
        self.add_line('sym-e0', (42, 24), (24, 6))
        self.add_line('sym-e2', (24, 6), (6, 24))
        self.add_line('sym-e4', (38, 20), (38, 42))
        self.add_line('sym-e5', (38, 42), (10, 42))
        self.add_line('sym-e7', (10, 42), (10, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', closed=False)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e7', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
