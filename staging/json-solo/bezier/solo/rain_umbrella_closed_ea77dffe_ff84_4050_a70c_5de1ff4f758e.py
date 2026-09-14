"""Rain umbrella closed (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea77dffe-ff84-4050-a70c-5de1ff4f758e'
SOURCE_PATH = 'icons-json/weather/rain umbrella closed_ea77dffe-ff84-4050-a70c-5de1ff4f758e.json'
AUTHOR = 'json_to_solo'

class RainUmbrellaClosedWeather(Solo48):
    icon_id = 'rain-umbrella-closed-weather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('rain', 'umbrella', 'closed', 'weather')

    def build(self):
        self.add_line('e0', (24, 4), (24, 6))
        self.add_line('e1', (24, 41), (24, 31))
        self.add_line('e2', (24, 31), (40, 31))
        self.add_line('e3', (40, 31), (24, 6))
        self.add_line('e4', (24, 31), (8, 31))
        self.add_line('e5', (8, 31), (24, 6))
        self.add_bezier('e6', (16, 41), ((16.533, 42.082), (17.493, 44), (19.573, 44)), ((19.575, 44), (19.576, 44), (19.578, 44)), ((19.67, 44), (19.761, 44), (19.84, 44)), ((22.027, 44), (23.28, 42.155), (24, 41)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e6', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
