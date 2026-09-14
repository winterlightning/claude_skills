"""Batch-01/laptop (computers), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4679969c-dfb9-4a03-ab57-4d2eded56e5a'
SOURCE_PATH = 'icons-json/computers/batch-01/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.json'
AUTHOR = 'json_to_solo'

class Batch01Laptop4679969c(Solo48):
    icon_id = 'batch-01-laptop-4679969c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')

    def build(self):
        self.add_line('sym-e0', (7, 32), (41, 32))
        self.add_arc('sym-e1', (41, 32), (43, 36), radius_x=16)
        self.add_line('sym-e2', (43, 36), (44, 38))
        self.add_arc('sym-e5', (44, 38), (42, 40), radius_x=2)
        self.add_line('sym-e6', (42, 40), (24, 40))
        self.add_line('sym-e7', (24, 40), (6, 40))
        self.add_arc('sym-e8', (6, 40), (4, 38), radius_x=2)
        self.add_arc('sym-e11', (4, 38), (5, 36), radius_x=5, sweep=False)
        self.add_arc('sym-e12', (5, 36), (7, 32), radius_x=17)
        self.add_line('sym-e13', (7, 32), (7, 10))
        self.add_arc('sym-e14', (7, 10), (9, 8), radius_x=3)
        self.add_line('sym-e15', (9, 8), (24, 8))
        self.add_line('sym-e16', (24, 8), (39, 8))
        self.add_arc('sym-e17', (39, 8), (41, 10), radius_x=3)
        self.add_line('sym-e18', (41, 10), (41, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
