"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0209d9df-8004-4d01-8d63-b5f783021ddb'
SOURCE_PATH = 'icons-json/protection/helmet_0209d9df-8004-4d01-8d63-b5f783021ddb.json'
AUTHOR = 'json_to_solo'

class Helmet0209d9df(Solo48):
    icon_id = 'helmet-0209d9df'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_bezier('sym-e0', (40, 31), ((40, 30.568), (40, 30.438), (40, 30)))
        self.add_bezier('sym-e1', (40, 30), ((40, 29.211), (40.105, 27.771), (40, 27)))
        self.add_bezier('sym-e2', (40, 27), ((39.055, 19.8), (35.145, 15.12), (29, 13)))
        self.add_line('sym-e3', (29, 13), (29, 11))
        self.add_bezier('sym-e4', (29, 11), ((29, 10.64), (29.045, 10.37), (29, 10)))
        self.add_bezier('sym-e5', (29, 10), ((28.845, 8.87), (27.018, 8), (26, 8)))
        self.add_bezier('sym-e6', (26, 8), ((25.782, 8), (26.218, 8), (26, 8)))
        self.add_line('sym-e7', (26, 8), (24, 8))
        self.add_line('sym-e8', (24, 8), (22, 8))
        self.add_bezier('sym-e9', (22, 8), ((21.782, 8), (22.218, 8), (22, 8)))
        self.add_bezier('sym-e10', (22, 8), ((20.982, 8), (19.155, 8.87), (19, 10)))
        self.add_bezier('sym-e11', (19, 10), ((18.955, 10.37), (19, 10.64), (19, 11)))
        self.add_line('sym-e12', (19, 11), (19, 13))
        self.add_bezier('sym-e13', (19, 13), ((12.855, 15.12), (8.945, 19.8), (8, 27)))
        self.add_bezier('sym-e14', (8, 27), ((7.895, 27.771), (8, 29.211), (8, 30)))
        self.add_bezier('sym-e15', (8, 30), ((8, 30.438), (8, 30.568), (8, 31)))
        self.add_line('sym-e16', (8, 31), (6, 31))
        self.add_bezier('sym-e17', (6, 31), ((5.164, 31.54), (4, 31.75), (4, 33)))
        self.add_bezier('sym-e18', (4, 33), ((4, 33.06), (4, 33.94), (4, 34)))
        self.add_bezier('sym-e19', (4, 34), ((4, 34.9), (4, 35.09), (4, 36)))
        self.add_bezier('sym-e20', (4, 36), ((4.091, 37.09), (4.318, 38.16), (5, 39)))
        self.add_bezier('sym-e21', (5, 39), ((5.155, 39.2), (4.773, 39.88), (5, 40)))
        self.add_bezier('sym-e22', (5, 40), ((5.136, 40), (5.864, 39.94), (6, 40)))
        self.add_line('sym-e23', (6, 40), (24, 40))
        self.add_line('sym-e24', (24, 40), (42, 40))
        self.add_bezier('sym-e25', (42, 40), ((42.136, 39.94), (42.864, 40), (43, 40)))
        self.add_bezier('sym-e26', (43, 40), ((43.227, 39.88), (42.845, 39.2), (43, 39)))
        self.add_bezier('sym-e27', (43, 39), ((43.682, 38.16), (43.909, 37.09), (44, 36)))
        self.add_bezier('sym-e28', (44, 36), ((44, 35.09), (44, 34.9), (44, 34)))
        self.add_bezier('sym-e29', (44, 34), ((44, 33.94), (44, 33.06), (44, 33)))
        self.add_bezier('sym-e30', (44, 33), ((44, 31.75), (42.836, 31.54), (42, 31)))
        self.add_line('sym-e31', (42, 31), (40, 31))
        self.add_line('sym-e32', (40, 31), (29, 31))
        self.add_line('sym-e33', (29, 31), (29, 13))
        self.add_line('sym-e34', (29, 31), (24, 31))
        self.add_line('sym-e35', (24, 31), (19, 31))
        self.add_line('sym-e36', (19, 31), (19, 13))
        self.add_line('sym-e37', (8, 31), (19, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33')
        self.add_contour('sym-c1', 'sym-e34', 'sym-e35', 'sym-e36')
        self.add_contour('sym-c2', 'sym-e37')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
