"""Monument (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f142849-8b23-40f0-aba8-d7cdaa500f99'
SOURCE_PATH = 'icons-json/symbol/monument_7f142849-8b23-40f0-aba8-d7cdaa500f99.json'
AUTHOR = 'json_to_solo'

class MonumentSymbol(Solo48):
    icon_id = 'monument-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('monument', 'symbol')

    def build(self):
        self.add_line('e0', (6, 42), (42, 42))
        self.add_line('e1', (35, 29), (12, 29))
        self.add_line('e2', (7, 37), (6, 42))
        self.add_line('e3', (35, 29), (35, 24))
        self.add_line('e4', (13, 22), (13, 29))
        self.add_line('e5', (24, 6), (24, 13))
        self.add_bezier('e6', (42, 42), ((41.992, 41.902), (41.992, 41.804), (41.984, 41.705)), ((41.984, 41.165), (41.828, 40.585), (41.738, 40.045)), ((41.255, 36.968), (40.216, 34.105), (38.474, 31.503)), ((38.261, 31.184), (36.706, 29.195), (36.477, 29.122)), ((36.134, 29.048), (35.344, 29.074), (35, 29)))
        self.add_bezier('e7', (12, 29), ((11.305, 29.728), (10.23, 30.357), (9.616, 31.175)), ((8.446, 32.722), (7.319, 35.077), (7, 37)))
        self.add_bezier('e8', (35, 24), ((35, 17.749), (30.382, 12.333), (24, 12.545)), ((19.672, 12.685), (15.164, 15.131), (13.282, 19.14)), ((12.955, 19.844), (13, 21.215), (13, 22)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e8', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
