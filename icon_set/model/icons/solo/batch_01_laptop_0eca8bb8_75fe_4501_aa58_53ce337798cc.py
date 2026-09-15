"""Batch-01/laptop (computers), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
SOURCE_PATH = 'icons-json/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.json'
AUTHOR = 'gpt-6'

class Batch01Laptop(Solo48):
    icon_id = 'batch-01-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')

    def build(self):
        self.add_line('sym-e0', (7, 32), (41, 32))
        self.add_arc('sym-e1', (41, 32), (43, 36), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('sym-e2', (43, 36), (44, 38))
        self.add_arc('sym-e5', (44, 38), (42, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e6', (42, 40), (6, 40))
        self.add_arc('sym-e8', (6, 40), (4, 38), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (4, 38), (5, 36), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('sym-e12', (5, 36), (7, 32), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('sym-e13', (7, 32), (7, 10))
        self.add_arc('sym-e14', (7, 10), (9, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e15', (9, 8), (39, 8))
        self.add_arc('sym-e17', (39, 8), (41, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e18', (41, 10), (41, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', closed=False)
