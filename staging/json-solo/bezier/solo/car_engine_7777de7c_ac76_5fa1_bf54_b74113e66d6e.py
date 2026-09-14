"""Car engine (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7777de7c-ac76-5fa1-bf54-b74113e66d6e'
SOURCE_PATH = 'icons-json/transportation/car engine_7777de7c-ac76-5fa1-bf54-b74113e66d6e.json'
AUTHOR = 'json_to_solo'

class CarEngine7777de7c(Solo48):
    icon_id = 'car-engine-7777de7c'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'engine', 'transportation')

    def build(self):
        self.add_line('e0', (4, 18), (4, 35))
        self.add_line('e1', (4, 24), (12, 24))
        self.add_line('e2', (12, 24), (12, 17))
        self.add_line('e3', (15, 14), (29, 14))
        self.add_line('e4', (33, 16), (36, 19))
        self.add_line('e5', (37, 20), (42, 20))
        self.add_line('e6', (44, 22), (44, 35))
        self.add_line('e7', (39, 40), (22, 40))
        self.add_line('e8', (19, 39), (14, 34))
        self.add_line('e9', (10, 31), (4, 31))
        self.add_line('e10', (16, 8), (29, 8))
        self.add_line('e11', (22, 14), (22, 8))
        self.add_bezier('e12', (12, 17), ((12, 15.838), (12.564, 14.358), (13.936, 13.928)), ((14.273, 13.819), (14.655, 14), (15, 14)))
        self.add_bezier('e13', (29, 14), ((30.664, 14.438), (31.773, 14.863), (33, 16)))
        self.add_bezier('e14', (36, 19), ((36.309, 19.286), (36.682, 19.722), (37, 20)))
        self.add_bezier('e15', (42, 20), ((43, 20), (43.991, 20.286), (43.991, 21.272)), ((43.991, 21.389), (44, 21.507), (44, 21.625)), ((44, 21.861), (44, 21.773), (44, 22)))
        self.add_bezier('e16', (44, 35), ((43.991, 35.067), (43.991, 35.082), (43.982, 35.158)), ((43.982, 37.549), (41.282, 39.419), (39, 40)))
        self.add_bezier('e17', (22, 40), ((21.491, 40), (21.173, 39.992), (20.664, 39.992)), ((19.882, 39.992), (19.645, 39.354), (19, 39)))
        self.add_bezier('e18', (14, 34), ((13.4, 33.335), (12.045, 31.545), (11.291, 31.082)), ((10.991, 30.897), (10.327, 31.118), (10, 31)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9')
        self.add_contour('c2', 'e10')
        self.add_contour('c3', 'e11')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c1')
        self.relate('connect', 'c3', 'c2')
