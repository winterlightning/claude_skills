"""Car retro (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed61a709-0dae-5f64-b395-d0f1995bb267'
SOURCE_PATH = 'icons-json/transportation/car retro_ed61a709-0dae-5f64-b395-d0f1995bb267.json'
AUTHOR = 'json_to_solo'

class CarRetro(Solo48):
    icon_id = 'car-retro'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'retro', 'transportation')

    def build(self):
        self.add_line('e0', (39, 34), (42, 34))
        self.add_line('e1', (38, 19), (17, 19))
        self.add_line('e2', (17, 19), (19, 13))
        self.add_line('e3', (24, 8), (31, 8))
        self.add_line('e4', (30, 34), (17, 34))
        self.add_line('e5', (30, 19), (30, 8))
        self.add_arc('e6-top', (30, 34), (40, 34), radius_x=5, radius_y=6)
        self.add_arc('e6-bottom', (40, 34), (30, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e7-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_line('e8-1', (42, 34), (44, 33))
        self.add_line('e8-2', (44, 33), (43, 23))
        self.add_arc('e8-3', (43, 23), (38, 19), radius_x=5, sweep=False)
        self.add_arc('e9', (19, 13), (24, 8), radius_x=7)
        self.add_arc('e10', (31, 8), (39, 19), radius_x=10)
        self.add_arc('e11-1', (20, 19), (8, 21), radius_x=26, sweep=False)
        self.add_arc('e11-2', (8, 21), (5, 25), radius_x=8, sweep=False)
        self.add_arc('e11-3', (5, 25), (4, 30), radius_x=15, sweep=False)
        self.add_arc('e11-4', (4, 30), (5, 33), radius_x=5, sweep=False)
        self.add_arc('e11-5', (5, 33), (8, 34), radius_x=3, sweep=False)
        self.add_arc('e12-1', (44, 31), (44, 32), radius_x=34, sweep=False)
        self.add_arc('e12-2', (44, 32), (44, 33), radius_x=34, sweep=False)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e1', 'e2', 'e9', 'e3', 'e10')
        self.add_contour('c1', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5')
        self.add_contour('c2', 'e12-1', 'e12-2')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'e7')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'e6')
        self.relate('connect', 'c3', 'e7')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c4', 'c0')
