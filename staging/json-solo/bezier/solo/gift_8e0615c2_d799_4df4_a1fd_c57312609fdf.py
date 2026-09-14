"""Gift (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e0615c2-d799-4df4-a1fd-c57312609fdf'
SOURCE_PATH = 'icons-json/holidays/gift_8e0615c2-d799-4df4-a1fd-c57312609fdf.json'
AUTHOR = 'json_to_solo'

class GiftHolidays(Solo48):
    icon_id = 'gift-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('gift', 'holidays')

    def build(self):
        self.add_line('e0', (10, 16), (10, 39))
        self.add_line('e1', (13, 42), (35, 42))
        self.add_line('e2', (38, 32), (38, 16))
        self.add_line('e3', (23, 13), (24, 16))
        self.add_line('e4', (26, 13), (24, 16))
        self.add_line('e5', (6, 16), (42, 16))
        self.add_bezier('e6', (10, 39), ((10, 40.227), (10.091, 41.992), (11.825, 41.992)), ((11.948, 41.992), (12.071, 42), (12.185, 42)), ((12.308, 42), (12.877, 42), (13, 42)))
        self.add_bezier('e7', (35, 42), ((35.229, 42), (35.913, 41.992), (36.15, 41.992)), ((37.034, 41.992), (37.893, 41.403), (38.13, 40.519)), ((38.31, 39.873), (38.13, 38.932), (38.105, 38.269)), ((38.032, 36.24), (38, 34.029), (38, 32)))
        self.add_bezier('e8', (24, 16), ((20.76, 15.648), (16.26, 15.098), (13.871, 12.554)), ((12.349, 10.934), (12.169, 8.185), (14.01, 6.72)), ((14.55, 6.295), (15.237, 6), (15.933, 6)), ((15.934, 6), (15.935, 6), (15.936, 6)), ((16, 6), (16.056, 6), (16.121, 6)), ((16.186, 6), (16.252, 6), (16.309, 6.008)), ((19.655, 6.008), (22.092, 10.275), (23, 13)))
        self.add_bezier('e9', (25, 16), ((25.27, 16), (25.366, 15.843), (25.636, 15.818)), ((28.541, 15.565), (32.951, 14.689), (34.931, 12.308)), ((36.723, 10.148), (36.125, 6.016), (32.755, 6.016)), ((32.648, 6.008), (32.542, 6), (32.435, 6)), ((32.329, 6.008), (32.223, 6.008), (32.116, 6.016)), ((29.875, 6.016), (27.665, 8.741), (26.839, 10.59)), ((26.414, 11.547), (26.597, 12.108), (26, 13)))
        self.add_bezier('e10', (24, 16), ((24.548, 16), (25.452, 16), (26, 16)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e8', 'e3')
        self.add_contour('c2', 'e9', 'e4', 'e10')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
