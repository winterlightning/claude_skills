"""Plates (hotels), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '45ea99fe-26d3-4c90-807c-75e170dc824c'
SOURCE_PATH = 'icons-json/hotels/plates_45ea99fe-26d3-4c90-807c-75e170dc824c.json'
AUTHOR = 'gpt-6'

class Plates(Solo48):
    icon_id = 'plates'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    aliases = ()
    keywords = ('plates', 'hotels')

    def build(self):
        self.add_line('sym-e0', (39, 8), (4, 8))
        self.add_line('sym-e2', (9, 29), (44, 29))
        self.add_line('sym-e4', (24, 19), (18, 19))
        self.add_arc('sym-e5', (18, 19), (15, 18), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('sym-e6', (15, 18), (9, 8), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_line('sym-e7', (4, 29), (9, 29))
        self.add_arc('sym-e8', (9, 29), (10, 33), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('sym-e9', (10, 33), (17, 40), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('sym-e10', (17, 40), (31, 40))
        self.add_arc('sym-e14', (31, 40), (38, 33), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('sym-e15', (38, 33), (39, 29), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_line('sym-e16', (44, 8), (39, 8))
        self.add_arc('sym-e17', (39, 8), (33, 18), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('sym-e18', (33, 18), (30, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('sym-e19', (30, 19), (24, 19))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e2', closed=False)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', closed=False)
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e14', 'sym-e15', closed=False)
        self.add_contour('sym-c4', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
