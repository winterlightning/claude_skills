"""Thumbs up (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5680cb28-5cf7-4d7c-98be-ae372bac6440'
SOURCE_PATH = 'icons-json/symbol/thumbs up_5680cb28-5cf7-4d7c-98be-ae372bac6440.json'
AUTHOR = 'json_to_solo'

class ThumbsUp(Solo48):
    icon_id = 'thumbs-up'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('thumbs', 'up', 'symbol')

    def build(self):
        self.add_line('e0', (39, 21), (29, 21))
        self.add_line('e1', (29, 21), (30, 13))
        self.add_line('e2', (27, 6), (25, 6))
        self.add_line('e3', (25, 6), (24, 10))
        self.add_line('e4', (13, 22), (8, 22))
        self.add_line('e5', (6, 23), (6, 39))
        self.add_line('e6', (23, 42), (34, 42))
        self.add_bezier('e7', (30, 13), ((30.344, 9.899), (29.675, 7.996), (27, 6)))
        self.add_bezier('e8', (24, 10), ((23.403, 12.97), (19.598, 18.379), (17.307, 20.392)), ((16.162, 21.39), (14.612, 22), (13, 22)))
        self.add_bezier('e9', (8, 22), ((7.615, 22.115), (6.867, 22.593), (6.491, 22.707)), ((6.327, 22.863), (6.164, 22.845), (6, 23)))
        self.add_bezier('e10', (6, 39), ((6.622, 39.139), (7.244, 38.997), (7.874, 39.136)), ((9.985, 39.529), (12.357, 38.825), (14.468, 39.455)), ((15.507, 39.758), (16.456, 40.364), (17.471, 40.732)), ((19.222, 41.362), (21.126, 42), (23, 42)))
        self.add_bezier('e11', (34, 42), ((34.139, 42), (34.088, 41.992), (34.227, 41.992)), ((37.042, 41.992), (39.12, 39.57), (39.439, 36.903)), ((39.545, 35.962), (38.907, 34.816), (38.973, 33.99)), ((38.973, 33.949), (39.725, 33.09), (39.815, 32.967)), ((40.388, 32.157), (40.953, 31.175), (40.969, 30.153)), ((40.977, 29.195), (40.331, 28.058), (40.192, 27.346)), ((40.175, 27.273), (40.838, 26.643), (41.043, 26.397)), ((41.607, 25.737), (42, 25.037), (42, 24.149)), ((42, 24.135), (42, 24.121), (42, 24.106)), ((42, 23.084), (41.264, 21.979), (40.445, 21.415)), ((39.955, 21.063), (39.565, 21.188), (39, 21)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', closed=True)
