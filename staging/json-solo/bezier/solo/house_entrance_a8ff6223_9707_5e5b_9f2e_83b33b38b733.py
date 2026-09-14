"""House entrance (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8ff6223-9707-5e5b-9f2e-83b33b38b733'
SOURCE_PATH = 'icons-json/interface-essential/house entrance_a8ff6223-9707-5e5b-9f2e-83b33b38b733.json'
AUTHOR = 'json_to_solo'

class HouseEntranceInterfaceEssential(Solo48):
    icon_id = 'house-entrance-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'entrance', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (4, 39), ((4.509, 39.295), (5.345, 40), (6, 40)))
        self.add_line('sym-e1', (6, 40), (16, 40))
        self.add_bezier('sym-e2', (16, 40), ((16.164, 40), (15.836, 40), (16, 40)))
        self.add_bezier('sym-e3', (16, 40), ((16.8, 40), (17.564, 39.472), (18, 39)))
        self.add_line('sym-e4', (18, 39), (18, 31))
        self.add_bezier('sym-e5', (18, 31), ((18, 27.842), (20.671, 25), (24, 25)))
        self.add_bezier('sym-e6', (24, 25), ((27.329, 25), (30, 27.842), (30, 31)))
        self.add_line('sym-e7', (30, 31), (30, 39))
        self.add_bezier('sym-e8', (30, 39), ((30.436, 39.472), (31.2, 40), (32, 40)))
        self.add_bezier('sym-e9', (32, 40), ((32.164, 40), (31.836, 40), (32, 40)))
        self.add_line('sym-e10', (32, 40), (42, 40))
        self.add_bezier('sym-e11', (42, 40), ((42.655, 40), (43.491, 39.295), (44, 39)))
        self.add_line('sym-e12', (44, 39), (44, 22))
        self.add_line('sym-e13', (44, 22), (27, 10))
        self.add_bezier('sym-e14', (27, 10), ((26.473, 9.613), (24.655, 8), (24, 8)))
        self.add_bezier('sym-e15', (24, 8), ((23.345, 8), (21.527, 9.613), (21, 10)))
        self.add_line('sym-e16', (21, 10), (4, 22))
        self.add_line('sym-e17', (4, 22), (4, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
