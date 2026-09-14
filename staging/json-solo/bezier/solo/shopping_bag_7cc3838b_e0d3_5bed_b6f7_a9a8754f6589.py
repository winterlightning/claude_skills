"""Shopping bag (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cc3838b-e0d3-5bed-b6f7-a9a8754f6589'
SOURCE_PATH = 'icons-json/shopping/shopping bag_7cc3838b-e0d3-5bed-b6f7-a9a8754f6589.json'
AUTHOR = 'json_to_solo'

class ShoppingBag7cc3838b(Solo48):
    icon_id = 'shopping-bag-7cc3838b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self):
        self.add_line('sym-e0', (24, 44), (37, 44))
        self.add_bezier('sym-e1', (37, 44), ((37.211, 43.927), (36.806, 44), (37, 44)))
        self.add_bezier('sym-e2', (37, 44), ((38.28, 43.282), (40, 41.718), (40, 40)))
        self.add_bezier('sym-e3', (40, 40), ((40, 39.936), (40, 40.073), (40, 40)))
        self.add_bezier('sym-e4', (40, 40), ((40, 39.855), (40, 39.145), (40, 39)))
        self.add_line('sym-e5', (40, 39), (38, 18))
        self.add_bezier('sym-e6', (38, 18), ((37.865, 16.236), (38.063, 14), (36, 14)))
        self.add_line('sym-e7', (36, 14), (24, 14))
        self.add_line('sym-e8', (24, 14), (12, 14))
        self.add_bezier('sym-e9', (12, 14), ((9.937, 14), (10.135, 16.236), (10, 18)))
        self.add_line('sym-e10', (10, 18), (8, 39))
        self.add_bezier('sym-e11', (8, 39), ((8, 39.145), (8, 39.855), (8, 40)))
        self.add_bezier('sym-e12', (8, 40), ((8, 40.073), (8, 39.936), (8, 40)))
        self.add_bezier('sym-e13', (8, 40), ((8, 41.718), (9.72, 43.282), (11, 44)))
        self.add_bezier('sym-e14', (11, 44), ((11.194, 44), (10.789, 43.927), (11, 44)))
        self.add_line('sym-e15', (11, 44), (24, 44))
        self.add_bezier('sym-e16', (24, 4), ((24.037, 4), (23.963, 4), (24, 4)))
        self.add_bezier('sym-e17', (24, 4), ((24.073, 4), (23.929, 4), (24, 4)))
        self.add_bezier('sym-e18', (24, 4), ((24.202, 4), (24.806, 4), (25, 4)))
        self.add_bezier('sym-e19', (25, 4), ((26.962, 4), (29.032, 5.218), (30, 7)))
        self.add_bezier('sym-e20', (30, 7), ((30.337, 7.627), (30.781, 8.318), (31, 9)))
        self.add_line('sym-e21', (31, 9), (31, 18))
        self.add_bezier('sym-e22', (24, 4), ((23.963, 4), (24.037, 4), (24, 4)))
        self.add_bezier('sym-e23', (24, 4), ((23.927, 4), (24.071, 4), (24, 4)))
        self.add_bezier('sym-e24', (24, 4), ((23.798, 4), (23.194, 4), (23, 4)))
        self.add_bezier('sym-e25', (23, 4), ((21.038, 4), (18.968, 5.218), (18, 7)))
        self.add_bezier('sym-e26', (18, 7), ((17.663, 7.627), (17.219, 8.318), (17, 9)))
        self.add_line('sym-e27', (17, 9), (17, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c2', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c1', 'sym-c2')
