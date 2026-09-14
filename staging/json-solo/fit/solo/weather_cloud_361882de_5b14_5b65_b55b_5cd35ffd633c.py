"""Weather cloud (weather), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '361882de-5b14-5b65-b55b-5cd35ffd633c'
SOURCE_PATH = 'icons-json/weather/weather cloud_361882de-5b14-5b65-b55b-5cd35ffd633c.json'
AUTHOR = 'json_to_solo'

class WeatherCloudWeather(Solo48):
    icon_id = 'weather-cloud-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('weather', 'cloud')

    def build(self):
        self.add_line('e0', (35, 40), (10, 40))
        self.add_arc('e1-1', (33, 18), (23, 8), radius_x=12, sweep=False)
        self.add_arc('e1-2', (23, 8), (11, 22), radius_x=13, sweep=False)
        self.add_arc('e2-1', (33, 18), (41, 20), radius_x=9)
        self.add_arc('e2-2', (41, 20), (43, 24), radius_x=10)
        self.add_arc('e2-3', (43, 24), (44, 29), radius_x=13)
        self.add_arc('e2-4', (44, 29), (41, 37), radius_x=13)
        self.add_arc('e2-5', (41, 37), (35, 40), radius_x=8)
        self.add_arc('e3-1', (10, 40), (6, 37), radius_x=7)
        self.add_arc('e3-2', (6, 37), (4, 31), radius_x=10)
        self.add_line('e3-3', (4, 31), (5, 26))
        self.add_arc('e3-4', (5, 26), (11, 22), radius_x=7)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
