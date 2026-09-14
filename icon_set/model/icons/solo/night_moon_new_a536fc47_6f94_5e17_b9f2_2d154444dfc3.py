"""Night moon new (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a536fc47-6f94-5e17-b9f2-2d154444dfc3'
SOURCE_PATH = 'icons-json/weather/night moon new_a536fc47-6f94-5e17-b9f2-2d154444dfc3.json'
AUTHOR = 'json_to_solo'

class NightMoonNewWeather(Solo48):
    icon_id = 'night-moon-new-weather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'new', 'weather')

    def build(self):
        self.add_line('e0', (30, 5), (40, 4))
        self.add_line('e1', (40, 4), (34, 9))
        self.add_line('e2', (32, 39), (40, 44))
        self.add_bezier('e3', (40, 44), ((35.536, 43.655), (31.024, 43.264), (26.944, 42.118)), ((15.136, 38.809), (8.016, 31.382), (8.016, 24.036)), ((8.016, 23.875), (8, 23.723), (8, 23.571)), ((8, 23.568), (8, 23.566), (8, 23.564)), ((8, 23.491), (8.016, 23.427), (8.016, 23.355)), ((8.016, 17.209), (13.664, 11.3), (22.144, 7.591)), ((24.224, 6.691), (27.392, 5.245), (30, 5)))
        self.add_bezier('e4', (34, 9), ((33.44, 9.4), (32.608, 9.427), (32.08, 9.845)), ((24.512, 15.955), (22.896, 22.5), (25.344, 29.755)), ((26.384, 32.855), (28.384, 36.536), (32, 39)))
        self.add_contour('c0', 'e3', 'e0', 'e1', 'e4', 'e2', closed=True)
