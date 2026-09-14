"""Rain umbrella (weather), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7194fac6-980c-5e6a-80f2-7deeb9fede03'
SOURCE_PATH = 'icons-json/weather/rain umbrella_7194fac6-980c-5e6a-80f2-7deeb9fede03.json'
AUTHOR = 'json_to_solo'

class RainUmbrellaWeather(Solo48):
    icon_id = 'rain-umbrella-weather'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('rain', 'umbrella', 'weather')

    def build(self):
        self.add_line('e0', (17, 24), (21, 22))
        self.add_line('e1', (24, 39), (24, 21))
        self.add_arc('e2-1', (30, 24), (42, 23), radius_x=9)
        self.add_arc('e2-2', (42, 23), (19, 9), radius_x=18, sweep=False)
        self.add_arc('e2-3', (19, 9), (6, 23), radius_x=17, sweep=False)
        self.add_arc('e2-4', (6, 23), (17, 24), radius_x=8)
        self.add_arc('e3', (21, 22), (30, 24), radius_x=6)
        self.add_arc('e4-1', (17, 39), (20, 42), radius_x=3, sweep=False)
        self.add_line('e4-2', (20, 42), (23, 41))
        self.add_line('e4-3', (23, 41), (24, 39))
        self.add_arc('e5', (23, 8), (24, 6), radius_x=2, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0', 'e3')
        self.add_contour('c1', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
