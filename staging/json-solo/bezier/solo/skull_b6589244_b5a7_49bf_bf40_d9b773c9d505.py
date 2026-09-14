"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6589244-b5a7-49bf-bf40-d9b773c9d505'
SOURCE_PATH = 'icons-json/interface-essential/skull_b6589244-b5a7-49bf-bf40-d9b773c9d505.json'
AUTHOR = 'json_to_solo'

class Skull(Solo48):
    icon_id = 'skull'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 34), (24, 42))
        self.add_line('e1', (34, 22), (30, 26))
        self.add_line('e2', (13, 22), (18, 26))
        self.add_line('e3', (35, 35), (35, 39))
        self.add_line('e4', (31, 42), (19, 42))
        self.add_bezier('e5', (19, 42), ((18.869, 42), (18.837, 42), (18.706, 42)), ((18.387, 42), (18.06, 41.992), (17.741, 41.992)), ((17.078, 41.992), (16.235, 42), (15.597, 41.804)), ((11.531, 40.331), (13.634, 36.134), (11.899, 33.213)), ((11.056, 31.797), (9.289, 31.265), (8.103, 30.202)), ((6.442, 28.713), (6.016, 26.193), (6.016, 24.074)), ((6.016, 23.751), (6, 23.437), (6, 23.115)), ((6, 23.11), (6, 23.105), (6, 23.1)), ((6, 22.838), (6.016, 22.576), (6.016, 22.315)), ((6.016, 21.194), (6.27, 20.065), (6.524, 18.976)), ((7.931, 12.963), (12.513, 8.471), (18.395, 6.769)), ((19.844, 6.352), (21.423, 6.008), (22.945, 6.008)), ((22.993, 6.008), (23.041, 6), (23.09, 6)), ((23.09, 6), (23.091, 6), (23.092, 6)), ((23.427, 6), (23.755, 6.016), (24.09, 6.016)), ((31.724, 6.016), (39.12, 10.639), (41.28, 18.15)), ((41.665, 19.484), (41.984, 20.915), (41.984, 22.306)), ((41.984, 22.585), (42, 22.855), (42, 23.125)), ((42, 23.13), (42, 23.135), (42, 23.14)), ((42, 23.462), (41.984, 23.784), (41.984, 24.106)), ((41.984, 26.414), (41.354, 28.835), (39.595, 30.415)), ((38.105, 31.748), (35, 32.415), (35, 35)))
        self.add_bezier('e6', (35, 39), ((35, 40.898), (32.321, 41.992), (30.734, 41.992)), ((30.668, 41.992), (31.065, 42), (31, 42)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5', 'e3', 'e6', 'e4', closed=True)
        self.relate('connect', 'c0', 'c3')
