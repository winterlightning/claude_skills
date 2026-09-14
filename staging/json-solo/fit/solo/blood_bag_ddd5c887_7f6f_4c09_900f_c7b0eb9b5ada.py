"""Blood bag (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada'
SOURCE_PATH = 'icons-json/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.json'
AUTHOR = 'json_to_solo'

class BloodBagHealth(Solo48):
    icon_id = 'blood-bag-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('blood', 'bag', 'health')

    def build(self):
        self.add_line('sym-e0', (30, 33), (30, 38))
        self.add_line('sym-e1', (30, 38), (24, 38))
        self.add_line('sym-e2', (24, 38), (18, 38))
        self.add_line('sym-e3', (18, 38), (18, 33))
        self.add_line('sym-e4', (18, 33), (14, 33))
        self.add_arc('sym-e5', (14, 33), (8, 26), radius_x=8)
        self.add_line('sym-e7', (8, 26), (8, 11))
        self.add_arc('sym-e9', (8, 11), (16, 4), radius_x=9)
        self.add_line('sym-e10', (16, 4), (17, 4))
        self.add_line('sym-e11', (17, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (31, 4))
        self.add_line('sym-e13', (31, 4), (32, 4))
        self.add_arc('sym-e14', (32, 4), (40, 11), radius_x=9)
        self.add_line('sym-e16', (40, 11), (40, 26))
        self.add_arc('sym-e18', (40, 26), (34, 33), radius_x=8)
        self.add_line('sym-e19', (34, 33), (30, 33))
        self.add_line('sym-e20', (24, 44), (24, 38))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
