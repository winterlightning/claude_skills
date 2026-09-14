"""Weather cloud snow (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92996f23-da0e-45c8-b76f-7d176f374962'
SOURCE_PATH = 'icons-json/weather/weather cloud snow_92996f23-da0e-45c8-b76f-7d176f374962.json'
AUTHOR = 'json_to_solo'

class WeatherCloudSnowWeather(Solo48):
    icon_id = 'weather-cloud-snow-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('weather', 'cloud', 'snow')

    def build(self):
        self.add_line('e0', (38, 40), (12, 40))
        self.add_arc('e1-1', (12, 40), (4, 30), radius_x=11)
        self.add_line('e1-2', (4, 30), (5, 25))
        self.add_arc('e1-3', (5, 25), (8, 21), radius_x=11)
        self.add_line('e1-4', (8, 21), (13, 19))
        self.add_arc('e1-5', (13, 19), (16, 12), radius_x=12)
        self.add_arc('e1-6', (16, 12), (24, 8), radius_x=10)
        self.add_line('e1-7', (24, 8), (29, 9))
        self.add_arc('e1-8', (29, 9), (35, 15), radius_x=13)
        self.add_line('e1-9', (35, 15), (39, 17))
        self.add_arc('e1-10', (39, 17), (41, 20), radius_x=8)
        self.add_arc('e1-11', (41, 20), (41, 24), radius_x=6)
        self.add_arc('e1-12', (41, 24), (44, 31), radius_x=10)
        self.add_line('e1-13', (44, 31), (43, 36))
        self.add_arc('e1-14', (43, 36), (38, 40), radius_x=7)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', 'e1-12', 'e1-13', 'e1-14', closed=True)
