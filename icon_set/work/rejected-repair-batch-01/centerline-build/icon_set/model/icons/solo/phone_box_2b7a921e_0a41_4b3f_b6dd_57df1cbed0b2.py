"""Phone box (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2'
SOURCE_PATH = 'pictographic-primitives/symbol/phone box_2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2.svg'
AUTHOR = 'gpt-6'

class PhoneBox(Solo48):
    icon_id = 'phone-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'box', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 29), (24, 44))
        self.add_line('sym-e1', (8, 14), (40, 14))
        self.add_line('sym-e4', (38, 44), (38, 14))
        self.add_arc('sym-e5', (38, 14), (37, 11), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (37, 11), (25, 4), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (25, 4), (24, 4), radius_x=76, radius_y=76, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (24, 4), (23, 4), radius_x=69, radius_y=69, large_arc=False, sweep=True)
        self.add_arc('sym-e13', (23, 4), (11, 11), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('sym-e14', (11, 11), (10, 14), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e15', (10, 14), (10, 44))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e1', closed=False)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
