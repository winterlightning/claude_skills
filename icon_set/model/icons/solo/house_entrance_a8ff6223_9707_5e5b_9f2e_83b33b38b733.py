"""House entrance (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8ff6223-9707-5e5b-9f2e-83b33b38b733'
SOURCE_PATH = 'icons-json/interface-essential/house entrance_a8ff6223-9707-5e5b-9f2e-83b33b38b733.json'
AUTHOR = 'json_to_solo'

class HouseEntrance(Solo48):
    icon_id = 'house-entrance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'entrance', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (4, 39), (6, 40), radius_x=3, sweep=False)
        self.add_line('sym-e1', (6, 40), (16, 40))
        self.add_line('sym-e3', (16, 40), (18, 39))
        self.add_line('sym-e4', (18, 39), (18, 31))
        self.add_arc('sym-e5', (18, 31), (24, 25), radius_x=6)
        self.add_arc('sym-e6', (24, 25), (30, 31), radius_x=6)
        self.add_line('sym-e7', (30, 31), (30, 39))
        self.add_line('sym-e8', (30, 39), (32, 40))
        self.add_line('sym-e10', (32, 40), (42, 40))
        self.add_arc('sym-e11', (42, 40), (44, 39), radius_x=3, sweep=False)
        self.add_line('sym-e12', (44, 39), (44, 22))
        self.add_line('sym-e13', (44, 22), (27, 10))
        self.add_line('sym-e14', (27, 10), (24, 8))
        self.add_arc('sym-e15', (24, 8), (21, 10), radius_x=9, sweep=False)
        self.add_line('sym-e16', (21, 10), (4, 22))
        self.add_line('sym-e17', (4, 22), (4, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
