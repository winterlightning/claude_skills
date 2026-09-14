"""Bird house (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42448377-6c50-5d98-b128-671d3e0a84dc'
SOURCE_PATH = 'icons-json/interface-essential/bird house_42448377-6c50-5d98-b128-671d3e0a84dc.json'
AUTHOR = 'json_to_solo'

class BirdHouseInterfaceEssential(Solo48):
    icon_id = 'bird-house-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bird', 'house', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (19, 26), (29, 26), radius_x=5)
        self.add_arc('sym-e1', (29, 26), (19, 26), radius_x=5)
        self.add_line('sym-e2', (42, 22), (24, 6))
        self.add_line('sym-e3', (24, 6), (6, 22))
        self.add_line('sym-e4', (40, 20), (36, 42))
        self.add_line('sym-e5', (36, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (12, 42))
        self.add_line('sym-e7', (12, 42), (8, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
