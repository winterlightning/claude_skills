"""Trash (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809378b8-e0d0-4cfb-9e28-6f64d31ac4f8'
SOURCE_PATH = 'icons-json/symbol/trash_809378b8-e0d0-4cfb-9e28-6f64d31ac4f8.json'
AUTHOR = 'json_to_solo'

class Trash(Solo48):
    icon_id = 'trash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('trash', 'symbol')

    def build(self):
        self.add_line('sym-e0', (17, 13), (31, 13))
        self.add_arc('sym-e2', (31, 13), (30, 7), radius_x=6, sweep=False)
        self.add_arc('sym-e3', (30, 7), (28, 6), radius_x=4, sweep=False)
        self.add_line('sym-e5', (28, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (20, 6))
        self.add_arc('sym-e8', (20, 6), (18, 7), radius_x=3, sweep=False)
        self.add_arc('sym-e9', (18, 7), (17, 13), radius_x=6, sweep=False)
        self.add_line('sym-e11', (17, 13), (8, 13))
        self.add_line('sym-e12', (8, 13), (6, 13))
        self.add_line('sym-e13', (42, 13), (40, 13))
        self.add_line('sym-e14', (40, 13), (36, 40))
        self.add_line('sym-e15', (36, 40), (34, 42))
        self.add_line('sym-e17', (34, 42), (24, 42))
        self.add_line('sym-e18', (24, 42), (14, 42))
        self.add_line('sym-e20', (14, 42), (12, 40))
        self.add_line('sym-e21', (12, 40), (8, 13))
        self.add_line('sym-e22', (31, 13), (40, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c2', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
