"""Add tab (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00cb3bd4-7aa4-5664-b6cd-b3deff47dfbf'
SOURCE_PATH = 'icons-json/interface-essential/add tab_00cb3bd4-7aa4-5664-b6cd-b3deff47dfbf.json'
AUTHOR = 'json_to_solo'

class AddTabInterfaceEssential(Solo48):
    icon_id = 'add-tab-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('add', 'tab', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 15), (18, 33))
        self.add_line('e1', (10, 24), (24, 24))
        self.add_line('e2', (28, 40), (8, 40))
        self.add_line('e3', (4, 35), (4, 13))
        self.add_line('e4', (8, 8), (31, 8))
        self.add_line('e5', (35, 10), (42, 20))
        self.add_line('e6', (41, 30), (34, 39))
        self.add_bezier('e7', (34, 39), ((32.145, 40), (30.773, 39.988), (28.636, 39.988)), ((28.473, 39.988), (28.318, 40), (28.155, 40)), ((27.982, 40), (28.173, 40), (28, 40)))
        self.add_bezier('e8', (8, 40), ((7.782, 40), (7.191, 39.988), (6.973, 39.988)), ((5.818, 39.988), (4, 38.498), (4, 36.726)), ((4, 36.172), (4, 35.554), (4, 35)))
        self.add_bezier('e9', (4, 13), ((4, 12.52), (4.018, 11.951), (4.018, 11.458)), ((4.018, 10.006), (5.318, 8), (6.436, 8)), ((6.836, 8), (7.6, 8), (8, 8)))
        self.add_bezier('e10', (31, 8), ((31.182, 8), (31.645, 8.012), (31.827, 8.012)), ((33.082, 8.012), (34.182, 8.892), (35, 10)))
        self.add_bezier('e11', (42, 20), ((42.745, 21.009), (44, 22.72), (44, 24.283)), ((44, 24.284), (44, 24.285), (44, 24.287)), ((44, 24.359), (44, 24.432), (44, 24.517)), ((44, 24.591), (43.991, 24.665), (43.991, 24.738)), ((43.991, 26.942), (42.091, 28.708), (41, 30)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', closed=True)
