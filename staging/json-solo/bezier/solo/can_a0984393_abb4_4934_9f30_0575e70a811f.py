"""Can (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0984393-abb4-4934-9f30-0575e70a811f'
SOURCE_PATH = 'icons-json/food/can_a0984393-abb4-4934-9f30-0575e70a811f.json'
AUTHOR = 'json_to_solo'

class CanFood(Solo48):
    icon_id = 'can-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('can', 'food')

    def build(self):
        self.add_line('e0', (8, 8), (8, 40))
        self.add_line('e1', (40, 39), (40, 7))
        self.add_bezier('e2', (40, 9), ((39.89, 9.082), (39.78, 9.618), (39.67, 9.7)), ((38.66, 10.118), (36.62, 10.655), (35.49, 10.855)), ((33.97, 11.127), (32.38, 11.218), (30.84, 11.345)), ((25.38, 11.818), (19.63, 12), (14.26, 10.773)), ((12.04, 10.255), (10.05, 9.927), (8, 9)))
        self.add_bezier('e3', (40, 7), ((39.49, 6.636), (38.99, 5.927), (38.41, 5.664)), ((35.55, 4.336), (28.6, 4.018), (25.34, 4.018)), ((24.769, 4.018), (24.198, 4), (23.627, 4)), ((23.618, 4), (23.609, 4), (23.6, 4)), ((22.95, 4), (22.3, 4.018), (21.65, 4.018)), ((18.29, 4.018), (12.68, 4.809), (9.76, 6.3)), ((9.04, 6.664), (8.56, 7.473), (8, 8)))
        self.add_bezier('e4', (8, 40), ((8.16, 40.136), (8.18, 40.691), (8.37, 40.818)), ((12.25, 43.545), (18.21, 43.982), (23, 43.982)), ((23.52, 43.982), (24.05, 44), (24.58, 44)), ((24.59, 44), (24.599, 44), (24.609, 44)), ((25.209, 44), (25.82, 43.982), (26.43, 43.982)), ((29.92, 43.982), (33.65, 43.382), (36.9, 42.264)), ((38.09, 41.845), (40, 41.064), (40, 39.673)), ((40, 39.6), (40, 39.073), (40, 39)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3', 'e0', 'e4', 'e1', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
