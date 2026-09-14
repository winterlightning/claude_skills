"""Blood bag cross (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9abd9c20-5510-40da-8f74-a3309483ed6a'
SOURCE_PATH = 'icons-json/health/blood bag cross_9abd9c20-5510-40da-8f74-a3309483ed6a.json'
AUTHOR = 'json_to_solo'

class BloodBagCrossHealth(Solo48):
    icon_id = 'blood-bag-cross-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('blood', 'bag', 'cross', 'health')

    def build(self):
        self.add_line('sym-e0', (30, 33), (30, 38))
        self.add_line('sym-e1', (30, 38), (24, 38))
        self.add_line('sym-e2', (24, 38), (18, 38))
        self.add_line('sym-e3', (18, 38), (18, 33))
        self.add_arc('sym-e4', (18, 33), (9, 29), radius_x=9)
        self.add_arc('sym-e5', (9, 29), (8, 27), radius_x=4)
        self.add_line('sym-e7', (8, 27), (8, 10))
        self.add_arc('sym-e8', (8, 10), (14, 4), radius_x=9)
        self.add_line('sym-e9', (14, 4), (15, 4))
        self.add_line('sym-e11', (15, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (33, 4))
        self.add_line('sym-e14', (33, 4), (34, 4))
        self.add_arc('sym-e15', (34, 4), (40, 10), radius_x=8)
        self.add_line('sym-e16', (40, 10), (40, 27))
        self.add_arc('sym-e18', (40, 27), (39, 29), radius_x=4)
        self.add_arc('sym-e19', (39, 29), (30, 33), radius_x=9)
        self.add_line('sym-e20', (24, 44), (24, 38))
        self.add_line('sym-e21', (31, 19), (17, 19))
        self.add_line('sym-e22', (24, 12), (24, 25))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21')
        self.add_contour('sym-c3', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
