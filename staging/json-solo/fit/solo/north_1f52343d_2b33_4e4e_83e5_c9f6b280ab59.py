"""North (weather), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f52343d-2b33-4e4e-83e5-c9f6b280ab59'
SOURCE_PATH = 'icons-json/weather/north_1f52343d-2b33-4e4e-83e5-c9f6b280ab59.json'
AUTHOR = 'json_to_solo'

class NorthWeather(Solo48):
    icon_id = 'north-weather'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('north', 'weather')

    def build(self):
        self.add_line('e0', (24, 7), (24, 4))
        self.add_line('e1', (41, 24), (44, 24))
        self.add_line('e2', (24, 41), (24, 44))
        self.add_line('e3', (7, 24), (4, 24))
        self.add_line('e4', (24, 14), (31, 32))
        self.add_line('e5', (31, 32), (24, 29))
        self.add_line('e6', (24, 29), (17, 32))
        self.add_line('e7', (17, 32), (24, 14))
        self.add_arc('e8-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e8-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c3', 'e8')
