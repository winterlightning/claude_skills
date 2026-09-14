"""Ceiling lamp double (lamps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '326638cb-38f2-5e62-8dca-bfeecd92203f'
SOURCE_PATH = 'icons-json/lamps/ceiling lamp double_326638cb-38f2-5e62-8dca-bfeecd92203f.json'
AUTHOR = 'json_to_solo'

class CeilingLampDoubleLamps(Solo48):
    icon_id = 'ceiling-lamp-double-lamps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('ceiling', 'lamp', 'double', 'lamps')

    def build(self):
        self.add_line('sym-e0', (36, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (12, 8))
        self.add_line('sym-e2', (24, 20), (24, 8))
        self.add_line('sym-e3', (24, 20), (14, 20))
        self.add_arc('sym-e4', (14, 20), (10, 25), radius_x=5, sweep=False)
        self.add_line('sym-e5', (10, 25), (10, 30))
        self.add_arc('sym-e7', (10, 30), (16, 40), radius_x=9)
        self.add_line('sym-e8', (16, 40), (4, 40))
        self.add_line('sym-e10-1', (4, 40), (6, 33))
        self.add_arc('sym-e10-2', (6, 33), (10, 30), radius_x=5)
        self.add_line('sym-e11', (24, 20), (34, 20))
        self.add_arc('sym-e12', (34, 20), (38, 25), radius_x=5)
        self.add_line('sym-e13', (38, 25), (38, 30))
        self.add_arc('sym-e15', (38, 30), (32, 40), radius_x=9, sweep=False)
        self.add_line('sym-e16', (32, 40), (44, 40))
        self.add_line('sym-e18-1', (44, 40), (42, 33))
        self.add_arc('sym-e18-2', (42, 33), (38, 30), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10-1', 'sym-e10-2')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18-1', 'sym-e18-2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
