"""Horn (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82d50937-0e36-4f84-b67b-aafe2b74a0ce'
SOURCE_PATH = 'icons-json/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.json'
AUTHOR = 'json_to_solo'

class Horn(Solo48):
    icon_id = 'horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('horn', 'transportation')

    def build(self):
        self.add_line('e0', (29, 40), (21, 40))
        self.add_line('e1', (15, 33), (15, 25))
        self.add_line('e2', (32, 17), (15, 17))
        self.add_line('e3', (13, 17), (4, 8))
        self.add_line('e4', (4, 8), (4, 34))
        self.add_line('e5', (4, 34), (14, 25))
        self.add_line('e6', (14, 25), (36, 25))
        self.add_line('e7', (44, 34), (44, 9))
        self.add_arc('e8-1', (33, 25), (34, 35), radius_x=20)
        self.add_arc('e8-2', (34, 35), (29, 40), radius_x=5)
        self.add_line('e9-1', (21, 40), (18, 40))
        self.add_arc('e9-2', (18, 40), (16, 38), radius_x=3)
        self.add_arc('e9-3', (16, 38), (15, 33), radius_x=13)
        self.add_arc('e10', (44, 9), (32, 17), radius_x=12)
        self.add_arc('e11', (15, 17), (13, 17), radius_x=8, sweep=False)
        self.add_line('e12', (36, 25), (44, 34))
        self.add_contour('c0', 'e8-1', 'e8-2', 'e0', 'e9-1', 'e9-2', 'e9-3', 'e1')
        self.add_contour('c1', 'e10', 'e2', 'e11', 'e3', 'e4', 'e5', 'e6', 'e12', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
