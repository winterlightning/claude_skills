"""Honeycomb (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4966448-56e2-4786-a9bd-37a29a7e6a65'
SOURCE_PATH = 'icons-json/symbol/honeycomb_f4966448-56e2-4786-a9bd-37a29a7e6a65.json'
AUTHOR = 'json_to_solo'

class HoneycombSymbol(Solo48):
    icon_id = 'honeycomb-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('honeycomb', 'symbol')

    def build(self):
        self.add_line('sym-e0', (28, 24), (20, 24))
        self.add_line('sym-e1', (20, 24), (16, 32))
        self.add_line('sym-e2', (16, 32), (8, 32))
        self.add_line('sym-e3', (8, 32), (4, 24))
        self.add_line('sym-e4', (4, 24), (8, 16))
        self.add_line('sym-e5', (8, 16), (16, 16))
        self.add_line('sym-e6', (16, 16), (20, 24))
        self.add_line('sym-e7', (28, 24), (32, 32))
        self.add_line('sym-e8', (32, 32), (28, 40))
        self.add_line('sym-e9', (28, 40), (20, 40))
        self.add_line('sym-e10', (20, 40), (16, 32))
        self.add_line('sym-e11', (32, 32), (39, 32))
        self.add_line('sym-e12', (39, 32), (44, 24))
        self.add_line('sym-e13', (44, 24), (39, 16))
        self.add_line('sym-e14', (39, 16), (32, 16))
        self.add_line('sym-e15', (32, 16), (28, 24))
        self.add_line('sym-e16', (32, 16), (28, 8))
        self.add_line('sym-e17', (28, 8), (20, 8))
        self.add_line('sym-e18', (20, 8), (16, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c3', 'sym-e16', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
