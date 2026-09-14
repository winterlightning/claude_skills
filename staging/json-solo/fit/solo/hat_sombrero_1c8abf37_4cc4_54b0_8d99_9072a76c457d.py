"""Batch-02/hat sombrero (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c8abf37-4cc4-54b0-8d99-9072a76c457d'
SOURCE_PATH = 'icons-json/accessories/batch-02/hat sombrero_1c8abf37-4cc4-54b0-8d99-9072a76c457d.json'
AUTHOR = 'json_to_solo'

class Batch02HatSombrero(Solo48):
    icon_id = 'batch-02-hat-sombrero'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'sombrero', 'accessories')

    def build(self):
        self.add_arc('sym-e1', (24, 8), (18, 19), radius_x=12, sweep=False)
        self.add_line('sym-e2', (18, 19), (16, 30))
        self.add_line('sym-e3', (16, 30), (6, 30))
        self.add_arc('sym-e4', (6, 30), (4, 32), radius_x=3, sweep=False)
        self.add_line('sym-e5', (4, 32), (5, 35))
        self.add_arc('sym-e6', (5, 35), (6, 36), radius_x=3)
        self.add_arc('sym-e7-1', (6, 36), (9, 39), radius_x=7, sweep=False)
        self.add_line('sym-e7-2', (9, 39), (14, 40))
        self.add_line('sym-e9', (14, 40), (24, 40))
        self.add_line('sym-e10', (24, 40), (34, 40))
        self.add_line('sym-e12-1', (34, 40), (39, 39))
        self.add_line('sym-e12-2', (39, 39), (42, 36))
        self.add_line('sym-e13', (42, 36), (43, 35))
        self.add_line('sym-e14', (43, 35), (44, 32))
        self.add_arc('sym-e15', (44, 32), (42, 30), radius_x=3, sweep=False)
        self.add_line('sym-e16', (42, 30), (32, 30))
        self.add_line('sym-e17', (32, 30), (30, 19))
        self.add_arc('sym-e18', (30, 19), (24, 8), radius_x=12, sweep=False)
        self.add_line('sym-e20', (16, 30), (24, 30))
        self.add_line('sym-e21', (24, 30), (32, 30))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e9', 'sym-e10', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
