"""Shopping bag (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e2', (37, 44), (40, 40), radius_x=5, sweep=False)
        self.add_arc('sym-e4', (40, 40), (40, 39), radius_x=39)
        self.add_line('sym-e5', (40, 39), (38, 18))
        self.add_arc('sym-e6', (38, 18), (36, 14), radius_x=3, sweep=False)
        self.add_line('sym-e7', (36, 14), (24, 14))
        self.add_line('sym-e8', (24, 14), (12, 14))
        self.add_arc('sym-e9', (12, 14), (10, 18), radius_x=3, sweep=False)
        self.add_line('sym-e10', (10, 18), (8, 39))
        self.add_line('sym-e11', (8, 39), (8, 40))
        self.add_arc('sym-e13', (8, 40), (11, 44), radius_x=5, sweep=False)
        self.add_line('sym-e15', (11, 44), (24, 44))
        self.add_arc('sym-e18', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_arc('sym-e19', (25, 4), (30, 7), radius_x=6)
        self.add_line('sym-e20', (30, 7), (31, 9))
        self.add_line('sym-e21', (31, 9), (31, 18))
        self.add_arc('sym-e24', (24, 4), (23, 4), radius_x=69)
        self.add_arc('sym-e25', (23, 4), (18, 7), radius_x=6, sweep=False)
        self.add_arc('sym-e26', (18, 7), (17, 9), radius_x=11, sweep=False)
        self.add_line('sym-e27', (17, 9), (17, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c2', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27')
        self.relate('connect', 'sym-c1', 'sym-c2')
