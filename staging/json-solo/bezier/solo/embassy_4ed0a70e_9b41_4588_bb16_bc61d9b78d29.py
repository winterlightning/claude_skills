"""Embassy (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ed0a70e-9b41-4588-bb16-bc61d9b78d29'
SOURCE_PATH = 'icons-json/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.json'
AUTHOR = 'json_to_solo'

class EmbassySymbol(Solo48):
    icon_id = 'embassy-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('embassy', 'symbol')

    def build(self):
        self.add_line('e0', (44, 40), (4, 40))
        self.add_line('e1', (39, 24), (39, 40))
        self.add_line('e2', (29, 40), (29, 24))
        self.add_line('e3', (19, 40), (19, 24))
        self.add_line('e4', (9, 24), (9, 40))
        self.add_line('e5', (7, 24), (40, 24))
        self.add_bezier('e6', (40, 24), ((40.409, 23.95), (41.182, 23.9), (41.591, 23.86)), ((41.482, 23.31), (41.364, 22.76), (41.245, 22.21)), ((41.209, 22.05), (41.182, 21.89), (41.145, 21.72)), ((40.536, 19.29), (39.264, 17.03), (37.8, 15.11)), ((34.9, 11.28), (30.855, 8.73), (26.345, 8.1)), ((25.173, 8), (23.809, 8.02), (22.745, 8)), ((22.744, 8), (22.743, 8), (22.741, 8)), ((22.652, 8), (22.571, 8.01), (22.482, 8.02)), ((21.364, 8.02), (20.182, 8.33), (19.109, 8.68)), ((14.418, 10.2), (10.336, 13.82), (8.191, 18.68)), ((7.436, 20.39), (7.364, 22.16), (7, 24)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', closed=True)
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c0')
