"""Fill adjustment layer (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bfeb607-fee8-43a8-8a4a-88f605a7b761'
SOURCE_PATH = 'icons-json/design/fill adjustment layer_3bfeb607-fee8-43a8-8a4a-88f605a7b761.json'
AUTHOR = 'json_to_solo'

class FillAdjustmentLayerDesign(Solo48):
    icon_id = 'fill-adjustment-layer-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('fill', 'adjustment', 'layer', 'design')

    def build(self):
        self.add_line('e0', (13, 24), (7, 28))
        self.add_line('e1', (7, 31), (22, 42))
        self.add_line('e2', (24, 42), (41, 31))
        self.add_line('e3', (41, 28), (35, 24))
        self.add_line('e4', (13, 24), (22, 31))
        self.add_line('e5', (25, 31), (35, 24))
        self.add_line('e6', (13, 24), (7, 20))
        self.add_line('e7', (7, 17), (23, 6))
        self.add_line('e8', (25, 6), (41, 17))
        self.add_line('e9', (41, 20), (35, 24))
        self.add_bezier('e10', (7, 28), ((6.779, 28.286), (6.008, 28.885), (6.008, 29.261)), ((6, 29.285), (6, 29.309), (6, 29.326)), ((6, 29.326), (6, 29.326), (6, 29.326)), ((6.008, 29.359), (6.008, 29.392), (6.016, 29.425)), ((6.016, 29.76), (6.804, 30.755), (7, 31)))
        self.add_bezier('e11', (22, 42), ((22.164, 42), (22.691, 42), (22.855, 42)), ((22.994, 42), (23.141, 41.984), (23.28, 41.984)), ((23.313, 41.992), (23.345, 41.992), (23.378, 42)), ((23.591, 42), (23.795, 42), (24, 42)))
        self.add_bezier('e12', (41, 31), ((41.229, 30.689), (41.992, 29.719), (41.992, 29.318)), ((41.992, 29.286), (42, 29.254), (42, 29.222)), ((42, 29.221), (42, 29.221), (42, 29.22)), ((42, 28.852), (41.221, 28.27), (41, 28)))
        self.add_bezier('e13', (22, 31), ((22.974, 31.27), (24.026, 31.27), (25, 31)))
        self.add_bezier('e14', (7, 20), ((6.771, 19.697), (6, 19.075), (6, 18.665)), ((6, 18.633), (6.008, 18.6), (6.008, 18.567)), ((6.008, 18.248), (6.804, 17.245), (7, 17)))
        self.add_bezier('e15', (23, 6), ((23.221, 6), (23.632, 6.016), (23.853, 6.016)), ((23.967, 6.016), (24.09, 6.016), (24.205, 6.016)), ((24.237, 6.008), (24.278, 6.008), (24.311, 6)), ((24.483, 6), (24.828, 6), (25, 6)))
        self.add_bezier('e16', (41, 17), ((41.205, 17.27), (41.984, 18.256), (41.984, 18.608)), ((41.992, 18.641), (41.992, 18.674), (42, 18.706)), ((42, 18.739), (41.992, 18.764), (41.992, 18.796)), ((41.992, 19.124), (41.205, 19.738), (41, 20)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
