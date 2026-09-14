"""Beach parasol water (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9acf6d75-fd0b-5669-bda9-3051aa82ac0b'
SOURCE_PATH = 'icons-json/outdoors/beach parasol water_9acf6d75-fd0b-5669-bda9-3051aa82ac0b.json'
AUTHOR = 'json_to_solo'

class BeachParasolWaterOutdoors(Solo48):
    icon_id = 'beach-parasol-water-outdoors'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('beach', 'parasol', 'water', 'outdoors')

    def build(self):
        self.add_line('e0', (31, 32), (41, 32))
        self.add_line('e1', (20, 6), (22, 9))
        self.add_line('e2', (30, 32), (26, 21))
        self.add_line('e3', (11, 26), (40, 15))
        self.add_bezier('e4', (20, 35), ((23.461, 32.644), (25.71, 32.231), (29.727, 32.182)), ((29.997, 32.182), (30.73, 32), (31, 32)))
        self.add_bezier('e5', (6, 42), ((7.653, 41.763), (8.945, 41.337), (10.287, 40.315)), ((10.835, 39.889), (11.31, 39.325), (11.785, 38.817)), ((11.842, 38.752), (11.907, 38.695), (11.965, 38.629)), ((12.349, 38.907), (12.815, 39.554), (13.265, 39.938)), ((15.098, 41.509), (17.168, 42), (19.574, 41.828)), ((20.858, 41.64), (22.11, 40.871), (23.084, 40.061)), ((23.517, 39.709), (23.935, 39.333), (24.335, 38.948)), ((24.393, 38.891), (24.458, 38.834), (24.515, 38.776)), ((24.851, 39.095), (25.186, 39.423), (25.522, 39.742)), ((26.594, 40.756), (28.582, 41.992), (30.104, 41.992)), ((30.226, 41.992), (30.349, 42), (30.48, 42)), ((30.668, 42), (30.856, 41.984), (31.036, 41.984)), ((32.493, 41.984), (34.047, 41.247), (35.127, 40.315)), ((35.577, 39.93), (35.995, 39.513), (36.404, 39.087)), ((36.526, 38.956), (36.6, 38.695), (36.78, 38.695)), ((36.952, 38.695), (37.009, 38.956), (37.124, 39.087)), ((37.5, 39.521), (37.885, 39.955), (38.302, 40.347)), ((39.349, 41.329), (40.617, 41.771), (42, 42)))
        self.add_bezier('e6', (40, 15), ((35.574, 9.215), (28.484, 6.565), (21.545, 9.273)), ((14.1, 12.177), (10.599, 18.145), (11, 26)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6', closed=True)
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c4')
