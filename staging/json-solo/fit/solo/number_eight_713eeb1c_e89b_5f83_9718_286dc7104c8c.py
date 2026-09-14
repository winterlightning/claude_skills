"""Number eight (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '713eeb1c-e89b-5f83-9718-286dc7104c8c'
SOURCE_PATH = 'icons-json/interface-essential/number eight_713eeb1c-e89b-5f83-9718-286dc7104c8c.json'
AUTHOR = 'json_to_solo'

class NumberEightInterfaceEssential(Solo48):
    icon_id = 'number-eight-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'eight', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (24, 23), (30, 22), radius_x=23)
        self.add_arc('sym-e1-1', (30, 22), (37, 11), radius_x=9, sweep=False)
        self.add_arc('sym-e1-2', (37, 11), (30, 5), radius_x=9, sweep=False)
        self.add_line('sym-e2', (30, 5), (26, 4))
        self.add_line('sym-e3', (26, 4), (25, 4))
        self.add_line('sym-e5', (25, 4), (24, 4))
        self.add_line('sym-e6', (24, 4), (23, 4))
        self.add_line('sym-e8', (23, 4), (22, 4))
        self.add_line('sym-e9', (22, 4), (18, 5))
        self.add_arc('sym-e10-1', (18, 5), (11, 11), radius_x=9, sweep=False)
        self.add_arc('sym-e10-2', (11, 11), (18, 22), radius_x=9, sweep=False)
        self.add_arc('sym-e11', (18, 22), (24, 23), radius_x=23)
        self.add_arc('sym-e12', (24, 44), (25, 44), radius_x=29)
        self.add_line('sym-e13-1', (25, 44), (34, 42))
        self.add_arc('sym-e13-2', (34, 42), (39, 37), radius_x=12, sweep=False)
        self.add_arc('sym-e14', (39, 37), (40, 34), radius_x=6, sweep=False)
        self.add_arc('sym-e16', (40, 34), (40, 33), radius_x=34)
        self.add_arc('sym-e17', (40, 33), (25, 23), radius_x=13, sweep=False)
        self.add_line('sym-e18', (25, 23), (24, 23))
        self.add_arc('sym-e19', (24, 23), (23, 23), radius_x=21, sweep=False)
        self.add_arc('sym-e20', (23, 23), (8, 33), radius_x=13, sweep=False)
        self.add_line('sym-e21', (8, 33), (8, 34))
        self.add_arc('sym-e23', (8, 34), (9, 37), radius_x=6, sweep=False)
        self.add_arc('sym-e24-1', (9, 37), (14, 42), radius_x=12, sweep=False)
        self.add_line('sym-e24-2', (14, 42), (23, 44))
        self.add_arc('sym-e25', (23, 44), (24, 44), radius_x=29)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24-1', 'sym-e24-2', 'sym-e25', closed=True)
