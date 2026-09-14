"""Water level (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e9', (44, 15), ((40.891, 16.67), (38.327, 18.43), (34.882, 16.71)), ((33.773, 16.15), (32.764, 15.35), (31.891, 14.42)), ((31.591, 14.1), (30.945, 13.31), (30.845, 13.32)), ((30.636, 13.35), (29.245, 14.97), (28.791, 15.36)), ((27.191, 16.75), (25.118, 17.72), (23.045, 17.4)), ((21.373, 17.14), (19.9, 16.21), (18.636, 15)), ((18.464, 14.83), (16.991, 13.4), (16.891, 13.43)), ((16.745, 13.47), (15.064, 15.32), (14.655, 15.67)), ((13.045, 17.02), (9.955, 18.08), (8, 17)))
        self.add_bezier('e10', (44, 24), ((41.391, 25.82), (38.655, 27.82), (35.445, 26.65)), ((34.1, 26.16), (32.927, 25.13), (31.882, 24.11)), ((31.682, 23.91), (30.8, 23.19), (30.6, 23.27)), ((30.5, 23.31), (29.2, 24.81), (28.845, 25.1)), ((27.064, 26.53), (24.836, 27.39), (22.627, 26.99)), ((21.127, 26.72), (19.718, 25.82), (18.573, 24.76)), ((18.318, 24.52), (17.118, 23.18), (16.945, 23.2)), ((16.882, 23.21), (14.691, 25.3), (14.309, 25.56)), ((11.991, 27.16), (10.673, 27.6), (8, 27)))
        self.add_bezier('e11', (44, 35), ((43.436, 37.11), (41.327, 40), (39, 40)))
        self.add_bezier('e12', (9, 40), ((8.964, 39.99), (8.464, 39.99), (8.427, 39.98)), ((8.036, 39.98), (7.627, 39.77), (7.273, 39.61)), ((5.464, 38.77), (4.491, 36.98), (4, 35)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e9', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e10', 'e4')
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
