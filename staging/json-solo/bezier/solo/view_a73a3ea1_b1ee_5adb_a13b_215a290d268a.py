"""View (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73a3ea1-b1ee-5adb-a13b-215a290d268a'
SOURCE_PATH = 'icons-json/interface-essential/view_a73a3ea1-b1ee-5adb-a13b-215a290d268a.json'
AUTHOR = 'json_to_solo'

class ViewInterfaceEssential(Solo48):
    icon_id = 'view-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('view', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (18, 24), (30, 24), radius_x=6, radius_y=9)
        self.add_arc('sym-e1', (30, 24), (18, 24), radius_x=6, radius_y=9)
        self.add_bezier('sym-e2', (4, 24), ((4.109, 24.172), (4, 24.815), (4, 25)))
        self.add_bezier('sym-e3', (4, 25), ((4.164, 25.246), (4.818, 24.766), (5, 25)))
        self.add_bezier('sym-e4', (5, 25), ((6.355, 26.698), (7.618, 29.314), (9, 31)))
        self.add_bezier('sym-e5', (9, 31), ((13.164, 36.046), (18.245, 40), (24, 40)))
        self.add_bezier('sym-e6', (24, 40), ((24.145, 40), (23.855, 40), (24, 40)))
        self.add_bezier('sym-e7', (24, 40), ((24.064, 40), (24.936, 40), (25, 40)))
        self.add_bezier('sym-e8', (25, 40), ((30.909, 40), (37.009, 34.563), (41, 29)))
        self.add_bezier('sym-e9', (41, 29), ((41.882, 27.782), (42.173, 26.28), (43, 25)))
        self.add_bezier('sym-e10', (43, 25), ((43.109, 24.852), (44, 24.074), (44, 24)))
        self.add_bezier('sym-e11', (44, 24), ((44, 23.996), (44, 24.012), (44, 24)))
        self.add_bezier('sym-e12', (44, 24), ((44, 23.988), (44, 24.004), (44, 24)))
        self.add_bezier('sym-e13', (44, 24), ((44, 23.926), (43.109, 23.148), (43, 23)))
        self.add_bezier('sym-e14', (43, 23), ((42.173, 21.72), (41.882, 20.218), (41, 19)))
        self.add_bezier('sym-e15', (41, 19), ((37.009, 13.437), (30.909, 8), (25, 8)))
        self.add_bezier('sym-e16', (25, 8), ((24.936, 8), (24.064, 8), (24, 8)))
        self.add_bezier('sym-e17', (24, 8), ((23.855, 8), (24.145, 8), (24, 8)))
        self.add_bezier('sym-e18', (24, 8), ((18.245, 8), (13.164, 11.954), (9, 17)))
        self.add_bezier('sym-e19', (9, 17), ((7.618, 18.686), (6.355, 21.302), (5, 23)))
        self.add_bezier('sym-e20', (5, 23), ((4.818, 23.234), (4.164, 22.754), (4, 23)))
        self.add_bezier('sym-e21', (4, 23), ((4, 23.185), (4.109, 23.828), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
