"""Globe (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1895f89b-67da-4327-b67f-f9726c4899c7'
SOURCE_PATH = 'icons-json/symbol/globe_1895f89b-67da-4327-b67f-f9726c4899c7.json'
AUTHOR = 'json_to_solo'

class GlobeSymbol(Solo48):
    icon_id = 'globe-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('globe', 'symbol')

    def build(self):
        self.add_line('sym-e0', (40, 31), (8, 31))
        self.add_line('sym-e1', (24, 42), (24, 18))
        self.add_line('sym-e2', (24, 18), (24, 6))
        self.add_arc('sym-e3', (24, 6), (6, 24), radius_x=18, sweep=False)
        self.add_arc('sym-e4', (6, 24), (24, 42), radius_x=18, sweep=False)
        self.add_arc('sym-e5', (24, 42), (42, 24), radius_x=18, sweep=False)
        self.add_arc('sym-e6', (42, 24), (24, 6), radius_x=18, sweep=False)
        self.add_line('sym-e7', (40, 18), (24, 18))
        self.add_line('sym-e8', (24, 18), (8, 18))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
