"""Batch-07/chain (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885'
SOURCE_PATH = 'icons-json/accessories/batch-07/chain_7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885.json'
AUTHOR = 'json_to_solo'

class Batch07Chain(Solo48):
    icon_id = 'batch-07-chain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'chain', 'accessories')

    def build(self):
        self.add_line('e0', (17, 30), (22, 25))
        self.add_line('e1', (14, 25), (8, 32))
        self.add_line('e2', (16, 40), (23, 34))
        self.add_line('e3', (22, 25), (25, 22))
        self.add_line('e4', (29, 18), (25, 22))
        self.add_line('e5', (26, 13), (31, 8))
        self.add_line('e6', (40, 17), (34, 23))
        self.add_arc('e7', (22, 25), (14, 25), radius_x=7, sweep=False)
        self.add_arc('e8-1', (8, 32), (6, 36), radius_x=8, sweep=False)
        self.add_arc('e8-2', (6, 36), (12, 42), radius_x=7, sweep=False)
        self.add_arc('e8-3', (12, 42), (16, 40), radius_x=9, sweep=False)
        self.add_arc('e9', (23, 34), (22, 25), radius_x=6, sweep=False)
        self.add_arc('e10-1', (31, 8), (36, 6), radius_x=8)
        self.add_arc('e10-2', (36, 6), (42, 13), radius_x=8)
        self.add_line('e10-3', (42, 13), (40, 17))
        self.add_arc('e11-1', (34, 23), (25, 22), radius_x=7)
        self.add_arc('e11-2', (25, 22), (26, 13), radius_x=7)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e2', 'e9', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e10-1', 'e10-2', 'e10-3', 'e6', 'e11-1', 'e11-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
