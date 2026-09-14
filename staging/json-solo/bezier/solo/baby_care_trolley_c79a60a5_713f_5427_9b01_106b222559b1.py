"""Baby care trolley (babies), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c79a60a5-713f-5427-9b01-106b222559b1'
SOURCE_PATH = 'icons-json/babies/baby care trolley_c79a60a5-713f-5427-9b01-106b222559b1.json'
AUTHOR = 'json_to_solo'

class BabyCareTrolley(Solo48):
    icon_id = 'baby-care-trolley'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'care', 'trolley', 'babies')

    def build(self):
        self.add_line('e0', (15, 14), (15, 19))
        self.add_line('e1', (40, 19), (15, 19))
        self.add_line('e2', (26, 4), (26, 19))
        self.add_line('e3', (21, 36), (24, 31))
        self.add_line('e4', (31, 31), (35, 35))
        self.add_arc('e5-top', (32, 39), (40, 39), radius_x=4, radius_y=5)
        self.add_arc('e5-bottom', (40, 39), (32, 39), radius_x=4, radius_y=5)
        self.add_arc('e6-top', (14, 39), (22, 39), radius_x=4, radius_y=5)
        self.add_arc('e6-bottom', (22, 39), (14, 39), radius_x=4, radius_y=5)
        self.add_bezier('e7', (8, 9), ((11.941, 9.1), (15, 8.764), (15, 14)))
        self.add_bezier('e8', (15, 19), ((15, 25.218), (18.206, 30.1), (24, 31.273)), ((25.861, 31.645), (29.088, 31.191), (31, 31)))
        self.add_bezier('e9', (31, 31), ((32.145, 30.736), (32.867, 30.782), (33.895, 30.209)), ((37.322, 28.3), (39.983, 23.864), (39.983, 19.645)), ((39.983, 19.427), (40, 19.2), (40, 18.982)), ((40, 18.836), (40, 18.691), (40, 18.545)), ((40, 12.327), (34.981, 6.391), (29.701, 4.618)), ((28.867, 4.336), (27.891, 4.009), (27.006, 4.009)), ((26.754, 4.009), (26.493, 4), (26.232, 4)), ((26.055, 4), (26.185, 4), (26, 4)))
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e9', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'e6')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'e5')
