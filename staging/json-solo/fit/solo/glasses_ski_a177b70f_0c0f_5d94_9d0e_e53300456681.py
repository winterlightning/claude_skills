"""Batch-01/glasses ski (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a177b70f-0c0f-5d94-9d0e-e53300456681'
SOURCE_PATH = 'icons-json/accessories/batch-01/glasses ski_a177b70f-0c0f-5d94-9d0e-e53300456681.json'
AUTHOR = 'json_to_solo'

class Batch01GlassesSki(Solo48):
    icon_id = 'batch-01-glasses-ski'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'glasses', 'ski', 'accessories')

    def build(self):
        self.add_line('sym-e0', (24, 21), (4, 21))
        self.add_line('sym-e2', (4, 21), (4, 19))
        self.add_line('sym-e3', (4, 19), (4, 17))
        self.add_line('sym-e4', (4, 17), (4, 15))
        self.add_arc('sym-e5-1', (4, 15), (8, 10), radius_x=8)
        self.add_arc('sym-e5-2', (8, 10), (13, 8), radius_x=14)
        self.add_line('sym-e6', (13, 8), (14, 8))
        self.add_arc('sym-e7', (14, 8), (15, 8), radius_x=18, sweep=False)
        self.add_line('sym-e8', (15, 8), (24, 8))
        self.add_line('sym-e9', (24, 8), (33, 8))
        self.add_line('sym-e10', (33, 8), (34, 8))
        self.add_line('sym-e11', (34, 8), (35, 8))
        self.add_arc('sym-e12-1', (35, 8), (40, 10), radius_x=14)
        self.add_arc('sym-e12-2', (40, 10), (44, 15), radius_x=7)
        self.add_line('sym-e13', (44, 15), (44, 17))
        self.add_line('sym-e14', (44, 17), (44, 19))
        self.add_arc('sym-e15', (44, 19), (44, 21), radius_x=27, sweep=False)
        self.add_line('sym-e18', (44, 21), (24, 21))
        self.add_arc('sym-e19', (5, 29), (10, 39), radius_x=11, sweep=False)
        self.add_arc('sym-e20', (10, 39), (13, 40), radius_x=8, sweep=False)
        self.add_arc('sym-e21', (13, 40), (14, 40), radius_x=1)
        self.add_arc('sym-e23-1', (14, 40), (17, 39), radius_x=5, sweep=False)
        self.add_line('sym-e23-2', (17, 39), (19, 37))
        self.add_line('sym-e24', (19, 37), (20, 30))
        self.add_arc('sym-e25', (20, 30), (24, 27), radius_x=4)
        self.add_arc('sym-e26', (24, 27), (28, 30), radius_x=4)
        self.add_line('sym-e27', (28, 30), (29, 37))
        self.add_arc('sym-e28-1', (29, 37), (31, 39), radius_x=4, sweep=False)
        self.add_arc('sym-e28-2', (31, 39), (34, 40), radius_x=5, sweep=False)
        self.add_line('sym-e30', (34, 40), (35, 40))
        self.add_line('sym-e31', (35, 40), (38, 39))
        self.add_arc('sym-e32', (38, 39), (43, 29), radius_x=11, sweep=False)
        self.add_line('sym-e33', (43, 29), (44, 21))
        self.add_line('sym-e43', (4, 21), (5, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e18', closed=True)
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23-1', 'sym-e23-2', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28-1', 'sym-e28-2', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.add_contour('sym-c3', 'sym-e43')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
