"""Batch-06/hat gentleman (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9ffcaa3-d483-4e32-bc69-6209c65297b2'
SOURCE_PATH = 'icons-json/accessories/batch-06/hat gentleman_f9ffcaa3-d483-4e32-bc69-6209c65297b2.json'
AUTHOR = 'json_to_solo'

class Batch06HatGentleman(Solo48):
    icon_id = 'batch-06-hat-gentleman'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'gentleman', 'accessories')

    def build(self):
        self.add_line('sym-e0', (38, 40), (10, 40))
        self.add_arc('sym-e4', (10, 40), (4, 33), radius_x=8)
        self.add_line('sym-e5', (4, 33), (4, 32))
        self.add_line('sym-e6', (10, 32), (38, 32))
        self.add_line('sym-e7', (38, 32), (38, 40))
        self.add_arc('sym-e11', (38, 40), (44, 33), radius_x=8, sweep=False)
        self.add_arc('sym-e12', (44, 33), (44, 32), radius_x=34)
        self.add_line('sym-e13', (10, 40), (10, 32))
        self.add_line('sym-e14', (10, 32), (10, 22))
        self.add_arc('sym-e15', (10, 22), (11, 19), radius_x=12, sweep=False)
        self.add_arc('sym-e16', (11, 19), (23, 8), radius_x=14)
        self.add_line('sym-e17', (23, 8), (24, 8))
        self.add_line('sym-e20', (24, 8), (25, 8))
        self.add_arc('sym-e21', (25, 8), (37, 19), radius_x=13)
        self.add_line('sym-e22', (37, 19), (38, 22))
        self.add_line('sym-e23', (38, 22), (38, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
