"""Globe (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1895f89b-67da-4327-b67f-f9726c4899c7'
SOURCE_PATH = 'pictographic-primitives/symbol/globe_1895f89b-67da-4327-b67f-f9726c4899c7.svg'
AUTHOR = 'gpt-6'

class GlobeSymbol(Solo48):
    icon_id = 'globe-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('globe', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 31), (8, 31))
        self.add_line('sym-e1', (24, 42), (24, 6))
        self.add_arc('sym-e3', (24, 6), (6, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e4', (6, 24), (24, 42), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e5', (24, 42), (42, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (42, 24), (24, 6), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e7', (40, 18), (8, 18))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', closed=False)
        self.add_contour('sym-c2', 'sym-e7', closed=False)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
