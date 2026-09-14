"""Light mode cloudy (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8695cf4-7b17-5792-8772-9696262aa3c3'
SOURCE_PATH = 'icons-json/weather/light mode cloudy_b8695cf4-7b17-5792-8772-9696262aa3c3.json'
AUTHOR = 'json_to_solo'

class LightModeCloudyWeather(Solo48):
    icon_id = 'light-mode-cloudy-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('light', 'mode', 'cloudy', 'weather')

    def build(self):
        self.add_line('e0', (36, 40), (10, 40))
        self.add_arc('e1-1', (11, 22), (23, 8), radius_x=13)
        self.add_arc('e1-2', (23, 8), (34, 18), radius_x=12)
        self.add_arc('e1-3', (34, 18), (41, 21), radius_x=9)
        self.add_arc('e1-4', (41, 21), (43, 24), radius_x=11)
        self.add_line('e1-5', (43, 24), (44, 29))
        self.add_line('e1-6', (44, 29), (42, 36))
        self.add_arc('e1-7', (42, 36), (36, 40), radius_x=9)
        self.add_arc('e2-1', (10, 40), (5, 36), radius_x=6)
        self.add_line('e2-2', (5, 36), (4, 31))
        self.add_arc('e2-3', (4, 31), (6, 25), radius_x=10)
        self.add_arc('e2-4', (6, 25), (11, 22), radius_x=6)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
