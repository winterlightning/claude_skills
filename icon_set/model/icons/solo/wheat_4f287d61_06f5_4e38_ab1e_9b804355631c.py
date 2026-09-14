"""Wheat (farming), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f287d61-06f5-4e38-ab1e-9b804355631c'
SOURCE_PATH = 'icons-json/farming/wheat_4f287d61-06f5-4e38-ab1e-9b804355631c.json'
AUTHOR = 'json_to_solo'

class Wheat(Solo48):
    icon_id = 'wheat'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'farming'
    aliases = ()
    keywords = ('wheat', 'farming')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 34))
        self.add_line('sym-e1', (24, 34), (24, 31))
        self.add_line('sym-e2', (24, 31), (24, 29))
        self.add_line('sym-e3', (24, 29), (24, 19))
        self.add_line('sym-e4', (24, 19), (29, 17))
        self.add_arc('sym-e5-1', (29, 17), (32, 13), radius_x=7, sweep=False)
        self.add_arc('sym-e5-2', (32, 13), (29, 7), radius_x=5, sweep=False)
        self.add_arc('sym-e6', (29, 7), (24, 4), radius_x=26, sweep=False)
        self.add_arc('sym-e7', (24, 4), (19, 7), radius_x=26, sweep=False)
        self.add_arc('sym-e8-1', (19, 7), (16, 13), radius_x=5, sweep=False)
        self.add_arc('sym-e8-2', (16, 13), (19, 17), radius_x=7, sweep=False)
        self.add_line('sym-e9', (19, 17), (24, 19))
        self.add_arc('sym-e10', (40, 21), (24, 29), radius_x=20, sweep=False)
        self.add_arc('sym-e11', (24, 29), (8, 21), radius_x=20, sweep=False)
        self.add_line('sym-e12-1', (8, 21), (8, 22))
        self.add_arc('sym-e12-2', (8, 22), (8, 24), radius_x=37)
        self.add_arc('sym-e13-1', (8, 24), (13, 31), radius_x=8, sweep=False)
        self.add_arc('sym-e13-2', (13, 31), (24, 34), radius_x=36, sweep=False)
        self.add_arc('sym-e14-1', (24, 34), (35, 31), radius_x=36, sweep=False)
        self.add_arc('sym-e14-2', (35, 31), (40, 24), radius_x=8, sweep=False)
        self.add_arc('sym-e15-1', (40, 24), (40, 23), radius_x=26)
        self.add_arc('sym-e15-2', (40, 23), (40, 21), radius_x=26)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13-1', 'sym-e13-2', 'sym-e14-1', 'sym-e14-2', 'sym-e15-1', 'sym-e15-2', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
