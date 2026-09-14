"""Bark (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '319e2aa3-098e-5a2f-a08e-fb155dc163cb'
SOURCE_PATH = 'icons-json/transportation/bark_319e2aa3-098e-5a2f-a08e-fb155dc163cb.json'
AUTHOR = 'json_to_solo'

class BarkTransportation(Solo48):
    icon_id = 'bark-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bark', 'transportation')

    def build(self):
        self.add_line('e0', (22, 34), (22, 8))
        self.add_line('e1', (22, 8), (11, 28))
        self.add_line('e2', (11, 28), (37, 28))
        self.add_line('e3', (22, 6), (22, 12))
        self.add_line('e4', (31, 42), (13, 42))
        self.add_line('e5', (6, 34), (42, 34))
        self.add_bezier('e6', (37, 28), ((35.495, 24.924), (33.835, 22.053), (32.035, 19.132)), ((30.807, 17.135), (29.58, 15.106), (28.214, 13.2)), ((26.774, 11.179), (25.096, 9.338), (23.517, 7.424)), ((23.206, 7.047), (23.002, 6.589), (22.699, 6.229)), ((22.593, 6.147), (22.115, 6.074), (22, 6)))
        self.add_bezier('e7', (42, 34), ((41.894, 34.147), (41.926, 34.186), (41.812, 34.334)), ((41.697, 34.415), (41.591, 34.497), (41.476, 34.587)), ((41.411, 34.669), (41.345, 34.751), (41.28, 34.825)), ((40.527, 35.798), (39.881, 36.845), (39.079, 37.778)), ((37.574, 39.513), (35.463, 40.83), (33.27, 41.476)), ((32.411, 41.73), (31.9, 42), (31, 42)))
        self.add_bezier('e8', (13, 42), ((12.853, 42), (13.061, 41.984), (12.914, 41.984)), ((8.479, 41.984), (6.826, 37.526), (6, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e6', 'e3')
        self.add_contour('c2', 'e7', 'e4', 'e8', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
