"""Water level (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4305a97-fdd3-4ced-b240-61fbd724fdb7'
SOURCE_PATH = 'icons-json/weather/water level_c4305a97-fdd3-4ced-b240-61fbd724fdb7.json'
AUTHOR = 'json_to_solo'

class WaterLevelWeather(Solo48):
    icon_id = 'water-level-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('water', 'level', 'weather')

    def build(self):
        self.add_line('e0', (4, 8), (4, 15))
        self.add_line('e1', (44, 8), (44, 15))
        self.add_line('e2', (8, 17), (4, 15))
        self.add_line('e3', (44, 15), (44, 24))
        self.add_line('e4', (8, 27), (4, 25))
        self.add_line('e5', (44, 24), (44, 35))
        self.add_line('e6', (39, 40), (9, 40))
        self.add_line('e7', (4, 35), (4, 25))
        self.add_line('e8', (4, 25), (4, 15))
        self.add_arc('e9-1', (44, 15), (40, 17), radius_x=29)
        self.add_arc('e9-2', (40, 17), (36, 17), radius_x=6)
        self.add_arc('e9-3', (36, 17), (31, 13), radius_x=12)
        self.add_line('e9-4', (31, 13), (30, 14))
        self.add_arc('e9-5', (30, 14), (26, 17), radius_x=9)
        self.add_arc('e9-6', (26, 17), (22, 17), radius_x=5)
        self.add_arc('e9-7', (22, 17), (17, 13), radius_x=15)
        self.add_line('e9-8', (17, 13), (16, 14))
        self.add_arc('e9-9', (16, 14), (8, 17), radius_x=7)
        self.add_arc('e10-1', (44, 24), (38, 27), radius_x=14)
        self.add_arc('e10-2', (38, 27), (31, 23), radius_x=9)
        self.add_line('e10-3', (31, 23), (30, 24))
        self.add_arc('e10-4', (30, 24), (23, 27), radius_x=8)
        self.add_arc('e10-5', (23, 27), (17, 23), radius_x=10)
        self.add_arc('e10-6', (17, 23), (16, 24), radius_x=4, sweep=False)
        self.add_arc('e10-7', (16, 24), (8, 27), radius_x=8)
        self.add_arc('e11', (44, 35), (39, 40), radius_x=6)
        self.add_arc('e12', (9, 40), (4, 35), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', 'e9-7', 'e9-8', 'e9-9', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e10-6', 'e10-7', 'e4')
        self.add_contour('c5', 'e5', 'e11', 'e6', 'e12', 'e7')
        self.add_contour('c6', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
