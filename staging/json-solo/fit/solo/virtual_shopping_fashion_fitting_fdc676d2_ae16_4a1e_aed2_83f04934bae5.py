"""Virtual shopping fashion fitting (technology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdc676d2-ae16-4a1e-aed2-83f04934bae5'
SOURCE_PATH = 'icons-json/technology/virtual shopping fashion fitting_fdc676d2-ae16-4a1e-aed2-83f04934bae5.json'
AUTHOR = 'json_to_solo'

class VirtualShoppingFashionFittingTechnology(Solo48):
    icon_id = 'virtual-shopping-fashion-fitting-technology'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('virtual', 'shopping', 'fashion', 'fitting', 'technology')

    def build(self):
        self.add_line('sym-e0', (35, 25), (35, 40))
        self.add_line('sym-e1', (35, 40), (13, 40))
        self.add_line('sym-e2', (13, 40), (13, 25))
        self.add_line('sym-e3', (13, 25), (13, 19))
        self.add_arc('sym-e5', (24, 13), (19, 11), radius_x=5)
        self.add_line('sym-e6', (19, 11), (18, 9))
        self.add_arc('sym-e7', (18, 9), (18, 8), radius_x=1)
        self.add_line('sym-e8', (18, 8), (17, 8))
        self.add_arc('sym-e9', (17, 8), (14, 8), radius_x=20)
        self.add_arc('sym-e10', (14, 8), (6, 16), radius_x=12, sweep=False)
        self.add_line('sym-e11', (6, 16), (4, 22))
        self.add_line('sym-e12', (4, 22), (13, 25))
        self.add_line('sym-e13', (35, 19), (35, 25))
        self.add_line('sym-e14', (35, 25), (44, 22))
        self.add_line('sym-e15', (44, 22), (42, 16))
        self.add_arc('sym-e16', (42, 16), (34, 8), radius_x=12, sweep=False)
        self.add_arc('sym-e17', (34, 8), (31, 8), radius_x=20)
        self.add_line('sym-e18', (31, 8), (30, 8))
        self.add_arc('sym-e19', (30, 8), (30, 9), radius_x=1)
        self.add_line('sym-e20', (30, 9), (29, 11))
        self.add_arc('sym-e21', (29, 11), (24, 13), radius_x=5)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
