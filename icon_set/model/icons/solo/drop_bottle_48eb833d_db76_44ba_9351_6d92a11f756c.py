"""Drop bottle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48eb833d-db76-44ba-9351-6d92a11f756c'
SOURCE_PATH = 'icons-json/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.json'
AUTHOR = 'gpt-6'

class DropBottle(Solo48):
    icon_id = 'drop-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('drop', 'bottle', 'symbol')

    def build(self):
        self.add_line('sym-e0', (10, 20), (38, 20))
        self.add_line('sym-e1', (38, 20), (38, 17))
        self.add_arc('sym-e2', (38, 17), (36, 15), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (36, 15), (32, 12), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('sym-e4-1', (32, 12), (30, 6))
        self.add_arc('sym-e4-2', (30, 6), (28, 5), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e5', (28, 5), (24, 4))
        self.add_line('sym-e8', (24, 4), (20, 5))
        self.add_arc('sym-e9-1', (20, 5), (18, 6), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e9-2', (18, 6), (16, 12))
        self.add_arc('sym-e10', (16, 12), (12, 15), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('sym-e11', (12, 15), (10, 17), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e12', (10, 17), (10, 21))
        self.add_line('sym-e14', (10, 21), (8, 23))
        self.add_line('sym-e16', (8, 23), (8, 40))
        self.add_arc('sym-e17', (8, 40), (14, 44), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e18', (14, 44), (34, 44))
        self.add_arc('sym-e20', (34, 44), (40, 40), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e21', (40, 40), (40, 23))
        self.add_line('sym-e23', (40, 23), (38, 21))
        self.add_line('sym-e24', (38, 21), (38, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e5', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', closed=False)
