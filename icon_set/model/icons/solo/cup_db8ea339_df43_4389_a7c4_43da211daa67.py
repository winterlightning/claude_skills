"""Cup (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db8ea339-df43-4389-a7c4-43da211daa67'
SOURCE_PATH = 'icons-json/symbol/cup_db8ea339-df43-4389-a7c4-43da211daa67.json'
AUTHOR = 'json_to_solo'

class Cup(Solo48):
    icon_id = 'cup'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('cup', 'symbol')

    def build(self):
        self.add_line('e0', (4, 28), (4, 8))
        self.add_line('e1', (4, 8), (33, 8))
        self.add_line('e2', (33, 8), (33, 27))
        self.add_bezier('e3', (33, 12), ((36.636, 11.96), (40.918, 11.19), (43.064, 15.34)), ((43.627, 16.45), (43.982, 17.77), (43.982, 19.06)), ((43.991, 19.129), (44, 19.208), (44, 19.286)), ((44, 19.288), (44, 19.289), (44, 19.29)), ((44, 23.37), (40.782, 26.44), (37.245, 26.91)), ((36.445, 27.02), (33.345, 26.85), (33.091, 27)), ((33.073, 27.1), (33.055, 27.2), (33.036, 27.3)), ((32.955, 27.82), (32.864, 28.33), (32.755, 28.85)), ((32.427, 30.44), (31.9, 31.93), (31.173, 33.37)), ((28.645, 38.34), (24.1, 39.99), (19.191, 39.99)), ((18.842, 39.99), (18.484, 40), (18.135, 40)), ((18.129, 40), (18.124, 40), (18.118, 40)), ((17.773, 40), (17.418, 39.98), (17.073, 39.98)), ((11.764, 39.98), (6.6, 36.5), (4.755, 30.93)), ((4.464, 30.06), (4, 28.93), (4, 28)))
        self.add_contour('c0', 'e3', 'e0', 'e1', 'e2')
