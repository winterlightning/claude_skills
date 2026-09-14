"""Rain umbrella (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7194fac6-980c-5e6a-80f2-7deeb9fede03'
SOURCE_PATH = 'icons-json/weather/rain umbrella_7194fac6-980c-5e6a-80f2-7deeb9fede03.json'
AUTHOR = 'json_to_solo'

class RainUmbrella(Solo48):
    icon_id = 'rain-umbrella'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('rain', 'umbrella', 'weather')

    def build(self):
        self.add_line('e0', (17, 24), (21, 22))
        self.add_line('e1', (24, 39), (24, 21))
        self.add_bezier('e2', (30, 24), ((32.283, 21.742), (34.26, 20.506), (37.574, 21.169)), ((38.613, 21.374), (39.611, 22.028), (40.519, 22.527)), ((40.797, 22.683), (41.075, 22.83), (41.354, 22.985)), ((41.705, 23.19), (42, 23.354), (42, 23.354)), ((42, 23.349), (42, 23.345), (42, 23.341)), ((42, 23.063), (41.794, 22.662), (41.714, 22.396)), ((41.239, 20.801), (40.74, 19.263), (39.938, 17.798)), ((37.459, 13.274), (33.213, 9.649), (28.042, 8.716)), ((26.438, 8.43), (24.802, 8.414), (23.182, 8.455)), ((16.653, 8.618), (11.326, 11.645), (8.013, 17.315)), ((7.006, 19.042), (6, 21.243), (6, 23.28)), ((6, 23.28), (6, 23.28), (6, 23.28)), ((6, 23.275), (6.292, 23.113), (6.63, 22.928)), ((6.9, 22.773), (7.17, 22.625), (7.44, 22.478)), ((8.283, 22.02), (9.248, 21.398), (10.205, 21.21)), ((13.355, 20.588), (14.848, 21.865), (17, 24)))
        self.add_bezier('e3', (21, 22), ((22.047, 21.591), (22.863, 20.735), (24, 20.727)), ((26.43, 20.711), (28.495, 22.274), (30, 24)))
        self.add_bezier('e4', (17, 39), ((17.074, 39.385), (16.71, 39.496), (16.874, 39.865)), ((17.397, 41.075), (18.69, 42), (20.04, 42)), ((20.041, 42), (20.042, 42), (20.042, 42)), ((20.09, 42), (20.131, 42), (20.179, 41.992)), ((22.29, 41.992), (23.476, 40.857), (24, 39)))
        self.add_bezier('e5', (23, 8), ((23.982, 6.306), (23.984, 7.604), (24, 6)))
        self.add_contour('c0', 'e2', 'e0', 'e3')
        self.add_contour('c1', 'e4', 'e1')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
