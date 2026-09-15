"""Astrology pisces (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b90476b0-fb60-4264-993a-bffbb01cd2c8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astrology pisces_b90476b0-fb60-4264-993a-bffbb01cd2c8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AstrologyPisces(Solo48):
    icon_id = 'astrology-pisces'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('astrology', 'pisces', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (44, 8), (15, 8))
        self.add_line('e1', (17, 10), (15, 8))
        self.add_line('e2', (30, 38), (32, 40))
        self.add_line('e3', (34, 40), (5, 40))
        self.add_bezier('e4', (15, 8), ((15, 8.042), (14.909, 8.084), (14.909, 8.126)), ((14.3, 8.177), (13.645, 8.017), (13.036, 8.017)), ((12.736, 8.017), (12.445, 8), (12.145, 8)), ((12, 8), (11.864, 8.008), (11.718, 8.008)), ((7.709, 8.008), (4.009, 11.512), (4.009, 15.217)), ((4.009, 15.283), (4, 15.349), (4, 15.416)), ((4, 15.417), (4, 15.418), (4, 15.419)), ((4, 15.596), (4.009, 15.764), (4.009, 15.941)), ((4.009, 17.272), (4.573, 18.644), (5.364, 19.739)), ((9.255, 25.137), (17.918, 23.368), (19.473, 17.187)), ((19.8, 15.899), (19.664, 14.552), (19.291, 13.288)), ((18.855, 11.84), (18.136, 11.027), (17, 10)))
        self.add_bezier('e5', (32, 40), ((32.609, 40), (33.391, 40), (34, 40)), ((35.227, 40), (36.464, 39.983), (37.691, 39.983)), ((38.109, 39.983), (38.555, 39.789), (38.945, 39.672)), ((41.855, 38.754), (43.991, 35.629), (43.991, 32.834)), ((43.991, 32.8), (44, 32.758), (44, 32.724)), ((44, 32.573), (43.991, 32.413), (43.991, 32.261)), ((43.991, 27.469), (38.7, 23.958), (33.818, 25.246)), ((30.873, 26.029), (28.827, 28.396), (28.173, 31.099)), ((27.882, 32.32), (27.873, 33.667), (28.209, 34.872)), ((28.591, 36.244), (28.955, 36.989), (30, 38)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', closed=True)
        self.add_contour('c2', 'e5', 'e2', closed=True)
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c2')
