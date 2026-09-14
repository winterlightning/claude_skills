"""Recycling (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a343142c-bd20-4f34-9bb1-46e62075b0e3'
SOURCE_PATH = 'icons-json/symbol/recycling_a343142c-bd20-4f34-9bb1-46e62075b0e3.json'
AUTHOR = 'json_to_solo'

class RecyclingA343142c(Solo48):
    icon_id = 'recycling-a343142c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('recycling', 'symbol')

    def build(self):
        self.add_line('e0', (40, 17), (42, 13))
        self.add_line('e1', (36, 16), (40, 17))
        self.add_line('e2', (11, 33), (8, 33))
        self.add_line('e3', (7, 36), (8, 33))
        self.add_bezier('e4', (41, 26), ((40.722, 28.266), (40.486, 30.194), (39.406, 32.239)), ((36.404, 37.917), (30.488, 41.984), (23.951, 41.984)), ((23.828, 41.992), (23.697, 41.992), (23.575, 42)), ((23.574, 42), (23.573, 42), (23.571, 42)), ((23.507, 42), (23.443, 41.992), (23.386, 41.992)), ((19.402, 41.992), (15.368, 40.298), (12.284, 37.852)), ((10.557, 36.477), (9.481, 34.62), (8, 33)))
        self.add_bezier('e5', (6, 25), ((6, 24.19), (6.008, 23.19), (6.008, 22.38)), ((6.008, 20.719), (6.556, 18.927), (7.145, 17.397)), ((9.755, 10.606), (16.252, 6.008), (23.558, 6.008)), ((23.735, 6.008), (23.905, 6), (24.082, 6)), ((24.084, 6), (24.087, 6), (24.09, 6)), ((24.139, 6), (24.188, 6.008), (24.237, 6.008)), ((25.89, 6.008), (27.6, 6.401), (29.155, 6.925)), ((34.71, 8.765), (36.744, 12.451), (40, 17)))
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e5', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c4')
