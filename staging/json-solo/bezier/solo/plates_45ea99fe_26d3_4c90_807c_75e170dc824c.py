"""Plates (hotels), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45ea99fe-26d3-4c90-807c-75e170dc824c'
SOURCE_PATH = 'icons-json/hotels/plates_45ea99fe-26d3-4c90-807c-75e170dc824c.json'
AUTHOR = 'json_to_solo'

class PlatesHotels(Solo48):
    icon_id = 'plates-hotels'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    aliases = ()
    keywords = ('plates', 'hotels')

    def build(self):
        self.add_line('sym-e0', (39, 8), (9, 8))
        self.add_line('sym-e1', (9, 8), (4, 8))
        self.add_line('sym-e2', (9, 29), (39, 29))
        self.add_line('sym-e3', (39, 29), (44, 29))
        self.add_line('sym-e4', (24, 19), (18, 19))
        self.add_bezier('sym-e5', (18, 19), ((17.155, 19), (15.782, 18.406), (15, 18)))
        self.add_bezier('sym-e6', (15, 18), ((11.327, 16.129), (10, 12.948), (9, 8)))
        self.add_line('sym-e7', (4, 29), (9, 29))
        self.add_bezier('sym-e8', (9, 29), ((9.309, 30.44), (9.445, 31.695), (10, 33)))
        self.add_bezier('sym-e9', (10, 33), ((11.4, 36.335), (14.027, 40), (17, 40)))
        self.add_bezier('sym-e10', (17, 40), ((17.073, 40), (17.927, 40), (18, 40)))
        self.add_line('sym-e11', (18, 40), (24, 40))
        self.add_line('sym-e12', (24, 40), (30, 40))
        self.add_bezier('sym-e13', (30, 40), ((30.073, 40), (30.927, 40), (31, 40)))
        self.add_bezier('sym-e14', (31, 40), ((33.973, 40), (36.6, 36.335), (38, 33)))
        self.add_bezier('sym-e15', (38, 33), ((38.555, 31.695), (38.691, 30.44), (39, 29)))
        self.add_line('sym-e16', (44, 8), (39, 8))
        self.add_bezier('sym-e17', (39, 8), ((38, 12.948), (36.673, 16.129), (33, 18)))
        self.add_bezier('sym-e18', (33, 18), ((32.218, 18.406), (30.845, 19), (30, 19)))
        self.add_line('sym-e19', (30, 19), (24, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c4', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
