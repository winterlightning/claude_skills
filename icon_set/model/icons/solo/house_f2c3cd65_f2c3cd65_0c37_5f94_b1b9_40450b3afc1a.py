"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f2c3cd65-0c37-5f94-b1b9-40450b3afc1a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_f2c3cd65-0c37-5f94-b1b9-40450b3afc1a.svg'
AUTHOR = 'gpt-6'

class HouseF2c3cd65(Solo48):
    icon_id = 'house-f2c3cd65'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 24), (24, 6))
        self.add_line('sym-e2', (24, 6), (6, 24))
        self.add_line('sym-e4', (37, 19), (37, 42))
        self.add_line('sym-e5', (37, 42), (11, 42))
        self.add_line('sym-e8', (11, 42), (11, 19))
        self.add_line('sym-e9', (29, 42), (29, 34))
        self.add_arc('sym-e10', (29, 34), (25, 28), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('sym-e11', (25, 28), (24, 28), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (24, 28), (23, 28), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e13', (23, 28), (19, 34), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e14', (19, 34), (19, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', closed=False)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e8', closed=False)
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
