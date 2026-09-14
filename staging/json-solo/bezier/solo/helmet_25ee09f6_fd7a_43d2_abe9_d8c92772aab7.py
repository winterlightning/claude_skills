"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH = 'icons-json/protection/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.json'
AUTHOR = 'json_to_solo'

class Helmet25ee09f6(Solo48):
    icon_id = 'helmet-25ee09f6'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_bezier('sym-e0', (40, 32), ((40.109, 29.92), (40.5, 28.02), (40, 26)))
        self.add_bezier('sym-e1', (40, 26), ((38.445, 19.73), (33.618, 14.6), (28, 13)))
        self.add_line('sym-e2', (28, 13), (28, 12))
        self.add_bezier('sym-e3', (28, 12), ((28, 8.324), (26.568, 8), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((21.432, 8), (20, 8.324), (20, 12)))
        self.add_line('sym-e5', (20, 12), (20, 13))
        self.add_bezier('sym-e6', (20, 13), ((14.382, 14.6), (9.555, 19.73), (8, 26)))
        self.add_bezier('sym-e7', (8, 26), ((7.5, 28.02), (7.891, 29.92), (8, 32)))
        self.add_bezier('sym-e8', (8, 32), ((4.517, 32.128), (4, 32.786), (4, 36)))
        self.add_bezier('sym-e9', (4, 36), ((4, 36.292), (4, 36.671), (4, 37)))
        self.add_bezier('sym-e10', (4, 37), ((4, 37.27), (4, 37.73), (4, 38)))
        self.add_bezier('sym-e11', (4, 38), ((4, 38.04), (4, 37.97), (4, 38)))
        self.add_bezier('sym-e12', (4, 38), ((4, 39.21), (5.118, 40), (6, 40)))
        self.add_bezier('sym-e13', (6, 40), ((6.191, 40), (6.809, 40), (7, 40)))
        self.add_line('sym-e14', (7, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (41, 40))
        self.add_bezier('sym-e16', (41, 40), ((41.191, 40), (41.809, 40), (42, 40)))
        self.add_bezier('sym-e17', (42, 40), ((42.882, 40), (44, 39.21), (44, 38)))
        self.add_bezier('sym-e18', (44, 38), ((44, 37.97), (44, 38.04), (44, 38)))
        self.add_bezier('sym-e19', (44, 38), ((44, 37.73), (44, 37.27), (44, 37)))
        self.add_bezier('sym-e20', (44, 37), ((44, 36.671), (44, 36.292), (44, 36)))
        self.add_bezier('sym-e21', (44, 36), ((44, 32.786), (43.483, 32.128), (40, 32)))
        self.add_bezier('sym-e22', (40, 32), ((39.797, 31.993), (40.202, 32), (40, 32)))
        self.add_bezier('sym-e23', (40, 32), ((39.597, 32), (39.406, 32), (39, 32)))
        self.add_line('sym-e24', (39, 32), (29, 32))
        self.add_line('sym-e25', (29, 32), (28, 32))
        self.add_line('sym-e26', (28, 32), (28, 13))
        self.add_line('sym-e27', (28, 32), (24, 32))
        self.add_line('sym-e28', (24, 32), (20, 32))
        self.add_line('sym-e29', (20, 32), (20, 13))
        self.add_line('sym-e30', (9, 32), (19, 32))
        self.add_line('sym-e31', (19, 32), (20, 32))
        self.add_bezier('sym-e32', (8, 32), ((8.203, 31.993), (7.798, 32), (8, 32)))
        self.add_bezier('sym-e33', (8, 32), ((8.403, 32), (8.594, 32), (9, 32)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c1', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31')
        self.add_contour('sym-c3', 'sym-e32', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
