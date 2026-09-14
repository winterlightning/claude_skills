"""Id (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '844a6cca-9183-43b4-8e32-4dbb2c81a21f'
SOURCE_PATH = 'icons-json/symbol/Id_844a6cca-9183-43b4-8e32-4dbb2c81a21f.json'
AUTHOR = 'json_to_solo'

class IdSymbol(Solo48):
    icon_id = 'id-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('id', 'symbol')

    def build(self):
        self.add_line('e0', (15, 8), (4, 8))
        self.add_line('e1', (9, 8), (9, 40))
        self.add_line('e2', (4, 40), (15, 40))
        self.add_line('e3', (44, 8), (44, 35))
        self.add_bezier('e4', (44, 35), ((44, 35.03), (43.982, 35.05), (43.982, 35.08)), ((43.982, 35.48), (43.691, 36.02), (43.518, 36.35)), ((42.209, 38.89), (39.282, 39.98), (36.755, 39.98)), ((36.491, 39.98), (36.218, 40), (35.955, 40)), ((35.791, 40), (35.618, 39.98), (35.455, 39.98)), ((30.127, 39.98), (26.882, 33.61), (27.345, 28.33)), ((27.718, 24.18), (30.591, 20.21), (34.318, 19.28)), ((37.064, 18.59), (39.918, 19.25), (42.2, 21.06)), ((42.455, 21.26), (43.982, 22.59), (43.982, 22.96)), ((43.991, 22.97), (43.991, 22.99), (44, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c2')
