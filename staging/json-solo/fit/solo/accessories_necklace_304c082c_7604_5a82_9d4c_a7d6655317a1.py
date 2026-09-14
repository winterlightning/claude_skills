"""Batch-07/accessories necklace (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '304c082c-7604-5a82-9d4c-a7d6655317a1'
SOURCE_PATH = 'icons-json/accessories/batch-07/accessories necklace_304c082c-7604-5a82-9d4c-a7d6655317a1.json'
AUTHOR = 'json_to_solo'

class Batch07AccessoriesNecklace(Solo48):
    icon_id = 'batch-07-accessories-necklace'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'accessories', 'necklace')

    def build(self):
        self.add_arc('sym-e0', (19, 39), (29, 39), radius_x=5)
        self.add_arc('sym-e1', (29, 39), (19, 39), radius_x=5)
        self.add_arc('sym-e2', (21, 34), (15, 32), radius_x=34, sweep=False)
        self.add_arc('sym-e3-1', (15, 32), (10, 25), radius_x=14)
        self.add_arc('sym-e3-2', (10, 25), (8, 17), radius_x=18)
        self.add_line('sym-e4', (8, 17), (8, 16))
        self.add_arc('sym-e6', (8, 16), (13, 5), radius_x=17)
        self.add_line('sym-e7', (13, 5), (14, 4))
        self.add_arc('sym-e9', (27, 34), (33, 32), radius_x=34)
        self.add_line('sym-e10-1', (33, 32), (38, 25))
        self.add_arc('sym-e10-2', (38, 25), (40, 17), radius_x=18, sweep=False)
        self.add_arc('sym-e11', (40, 17), (40, 16), radius_x=23)
        self.add_arc('sym-e13', (40, 16), (35, 5), radius_x=16, sweep=False)
        self.add_arc('sym-e14', (35, 5), (34, 4), radius_x=6, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e13', 'sym-e14')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
