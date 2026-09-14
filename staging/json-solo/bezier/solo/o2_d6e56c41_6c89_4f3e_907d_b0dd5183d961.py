"""O2 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e56c41-6c89-4f3e-907d-b0dd5183d961'
SOURCE_PATH = 'icons-json/symbol/O2_d6e56c41-6c89-4f3e-907d-b0dd5183d961.json'
AUTHOR = 'json_to_solo'

class O2Symbol(Solo48):
    icon_id = 'o2-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('o2', 'symbol')

    def build(self):
        self.add_line('e0', (41, 24), (29, 40))
        self.add_line('e1', (29, 40), (44, 40))
        self.add_line('e2', (19, 31), (19, 16))
        self.add_line('e3', (4, 17), (4, 31))
        self.add_bezier('e4', (30, 14), ((31.309, 11.62), (33.991, 8.02), (36.818, 8.02)), ((36.964, 8.01), (37.109, 8.01), (37.255, 8)), ((37.256, 8), (37.257, 8), (37.258, 8)), ((37.339, 8), (37.41, 8), (37.482, 8.01)), ((38.418, 8.01), (39.382, 8.44), (40.191, 8.93)), ((44, 11.75), (43.927, 20.03), (41, 24)))
        self.add_bezier('e5', (4, 31), ((4, 31), (4, 31), (4, 31)), ((4, 35.06), (7, 39.98), (11.018, 39.98)), ((11.164, 39.99), (11.309, 39.99), (11.455, 40)), ((11.591, 40), (11.736, 39.99), (11.882, 39.99)), ((15.855, 39.99), (19, 35.18), (19, 31)))
        self.add_bezier('e6', (19, 16), ((19, 11.89), (15.6, 8.01), (11.927, 8.01)), ((11.782, 8.01), (11.636, 8), (11.482, 8)), ((11.409, 8), (11.336, 8), (11.264, 8.01)), ((7.3, 8.01), (4.009, 12.28), (4.009, 16.5)), ((4, 16.58), (4, 16.67), (4, 16.75)), ((4, 16.83), (4, 16.92), (4, 17)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e5', 'e2', 'e6', 'e3', closed=True)
