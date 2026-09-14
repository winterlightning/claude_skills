"""Water currents 1 (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c21fdb3-aaf5-4d0c-b32b-f6f63f48a540'
SOURCE_PATH = 'icons-json/weather/water currents 1_1c21fdb3-aaf5-4d0c-b32b-f6f63f48a540.json'
AUTHOR = 'json_to_solo'

class WaterCurrents1(Solo48):
    icon_id = 'water-currents-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('water', 'currents', 'weather')

    def build(self):
        self.add_line('e0', (8, 8), (4, 12))
        self.add_line('e1', (8, 15), (4, 12))
        self.add_line('e2', (13, 12), (4, 12))
        self.add_line('e3', (40, 8), (44, 12))
        self.add_line('e4', (35, 12), (44, 12))
        self.add_line('e5', (40, 15), (44, 12))
        self.add_arc('e6', (19, 21), (13, 12), radius_x=7, sweep=False)
        self.add_arc('e7', (29, 21), (35, 12), radius_x=8)
        self.add_arc('e8-1', (4, 25), (11, 29), radius_x=5, sweep=False)
        self.add_arc('e8-2', (11, 29), (14, 26), radius_x=7, sweep=False)
        self.add_arc('e8-3', (14, 26), (17, 29), radius_x=8, sweep=False)
        self.add_arc('e8-4', (17, 29), (24, 26), radius_x=5, sweep=False)
        self.add_arc('e8-5', (24, 26), (27, 29), radius_x=7, sweep=False)
        self.add_arc('e8-6', (27, 29), (34, 26), radius_x=5, sweep=False)
        self.add_arc('e8-7', (34, 26), (37, 29), radius_x=6, sweep=False)
        self.add_arc('e8-8', (37, 29), (44, 25), radius_x=5, sweep=False)
        self.add_arc('e9-1', (4, 36), (6, 39), radius_x=6, sweep=False)
        self.add_arc('e9-2', (6, 39), (9, 40), radius_x=5, sweep=False)
        self.add_arc('e9-3', (9, 40), (14, 37), radius_x=6, sweep=False)
        self.add_arc('e9-4', (14, 37), (19, 40), radius_x=6, sweep=False)
        self.add_arc('e9-5', (19, 40), (24, 37), radius_x=6, sweep=False)
        self.add_arc('e9-6', (24, 37), (29, 40), radius_x=6, sweep=False)
        self.add_arc('e9-7', (29, 40), (34, 37), radius_x=6, sweep=False)
        self.add_arc('e9-8', (34, 37), (39, 40), radius_x=6, sweep=False)
        self.add_arc('e9-9', (39, 40), (44, 36), radius_x=7, sweep=False)
        self.add_arc('e9-10', (44, 36), (43, 36), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e7', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e8-8')
        self.add_contour('c7', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', 'e9-7', 'e9-8', 'e9-9', 'e9-10')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
