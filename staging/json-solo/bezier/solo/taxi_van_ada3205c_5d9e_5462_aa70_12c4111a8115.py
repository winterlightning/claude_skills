"""Taxi van (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ada3205c-5d9e-5462-aa70-12c4111a8115'
SOURCE_PATH = 'icons-json/transportation/taxi van_ada3205c-5d9e-5462-aa70-12c4111a8115.json'
AUTHOR = 'json_to_solo'

class TaxiVanTransportation(Solo48):
    icon_id = 'taxi-van-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('taxi', 'van', 'transportation')

    def build(self):
        self.add_line('e0', (44, 31), (44, 25))
        self.add_line('e1', (44, 25), (41, 25))
        self.add_line('e2', (31, 34), (17, 34))
        self.add_line('e3', (4, 30), (4, 12))
        self.add_line('e4', (8, 8), (29, 8))
        self.add_line('e5', (33, 10), (40, 19))
        self.add_line('e6', (38, 19), (4, 19))
        self.add_line('e7', (25, 8), (25, 19))
        self.add_arc('e8-top', (31, 34), (41, 34), radius_x=5, radius_y=6)
        self.add_arc('e8-bottom', (41, 34), (31, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-top', (7, 34), (17, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (17, 34), (7, 34), radius_x=5, radius_y=6)
        self.add_bezier('e10', (40, 34), ((41.573, 34.135), (44, 34.102), (44, 31)))
        self.add_bezier('e11', (8, 34), ((6.264, 34.246), (4.009, 34.092), (4.009, 31.015)), ((4.009, 30.72), (4, 30.283), (4, 30)))
        self.add_bezier('e12', (4, 12), ((4.009, 11.877), (4.009, 11.458), (4.018, 11.335)), ((4.018, 9.046), (5.627, 8), (7.1, 8)), ((7.273, 8), (7.818, 8), (8, 8)))
        self.add_bezier('e13', (29, 8), ((29.127, 8), (28.8, 8), (28.927, 8.012)), ((30.527, 8.012), (31.836, 8.622), (33, 10)))
        self.add_bezier('e14', (44, 24), ((43.373, 21.649), (42.327, 19.569), (40.364, 19.077)), ((39.427, 18.843), (38.927, 19), (38, 19)))
        self.add_contour('c0', 'e10', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5')
        self.add_contour('c3', 'e14', 'e6')
        self.add_contour('c4', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c2', 'e9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c4', 'c3')
