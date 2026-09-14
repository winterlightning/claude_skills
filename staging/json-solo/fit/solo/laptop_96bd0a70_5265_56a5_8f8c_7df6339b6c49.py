"""Batch-01/laptop (computers), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96bd0a70-5265-56a5-8f8c-7df6339b6c49'
SOURCE_PATH = 'icons-json/computers/batch-01/laptop_96bd0a70-5265-56a5-8f8c-7df6339b6c49.json'
AUTHOR = 'json_to_solo'

class Batch01Laptop(Solo48):
    icon_id = 'batch-01-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'laptop', 'computers')

    def build(self):
        self.add_line('sym-e0', (41, 32), (7, 32))
        self.add_arc('sym-e1', (7, 32), (4, 38), radius_x=28, sweep=False)
        self.add_arc('sym-e3', (4, 38), (6, 40), radius_x=2, sweep=False)
        self.add_line('sym-e4', (6, 40), (24, 40))
        self.add_line('sym-e5', (24, 40), (42, 40))
        self.add_arc('sym-e6', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('sym-e8', (44, 38), (41, 32), radius_x=28, sweep=False)
        self.add_line('sym-e9', (41, 32), (41, 11))
        self.add_arc('sym-e10', (41, 11), (39, 8), radius_x=3, sweep=False)
        self.add_line('sym-e12', (39, 8), (24, 8))
        self.add_line('sym-e13', (24, 8), (9, 8))
        self.add_arc('sym-e15', (9, 8), (7, 11), radius_x=3, sweep=False)
        self.add_line('sym-e16', (7, 11), (7, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16')
