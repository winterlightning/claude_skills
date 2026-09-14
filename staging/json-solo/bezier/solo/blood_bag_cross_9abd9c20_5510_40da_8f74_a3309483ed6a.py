"""Blood bag cross (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e4', (18, 33), ((13.951, 32.991), (10.649, 31.9), (9, 29)))
        self.add_bezier('sym-e5', (9, 29), ((8.742, 28.555), (8, 27.491), (8, 27)))
        self.add_bezier('sym-e6', (8, 27), ((8, 26.8), (8, 27.2), (8, 27)))
        self.add_line('sym-e7', (8, 27), (8, 10))
        self.add_bezier('sym-e8', (8, 10), ((8, 7.518), (11.058, 4.8), (14, 4)))
        self.add_bezier('sym-e9', (14, 4), ((14.332, 4), (14.631, 4), (15, 4)))
        self.add_bezier('sym-e10', (15, 4), ((15.123, 4), (14.877, 4.009), (15, 4)))
        self.add_line('sym-e11', (15, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (33, 4))
        self.add_bezier('sym-e13', (33, 4), ((33.123, 4.009), (32.877, 4), (33, 4)))
        self.add_bezier('sym-e14', (33, 4), ((33.369, 4), (33.668, 4), (34, 4)))
        self.add_bezier('sym-e15', (34, 4), ((36.942, 4.8), (40, 7.518), (40, 10)))
        self.add_line('sym-e16', (40, 10), (40, 27))
        self.add_bezier('sym-e17', (40, 27), ((40, 27.2), (40, 26.8), (40, 27)))
        self.add_bezier('sym-e18', (40, 27), ((40, 27.491), (39.258, 28.555), (39, 29)))
        self.add_bezier('sym-e19', (39, 29), ((37.351, 31.9), (34.049, 32.991), (30, 33)))
        self.add_line('sym-e20', (24, 44), (24, 38))
        self.add_line('sym-e21', (31, 19), (17, 19))
        self.add_line('sym-e22', (24, 12), (24, 25))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
        self.add_contour('sym-c1', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21')
        self.add_contour('sym-c3', 'sym-e22')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
