"""Baggage (travel), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc8cbcb8-44a1-56f5-8649-885490f30b35'
SOURCE_PATH = 'icons-json/travel/baggage_dc8cbcb8-44a1-56f5-8649-885490f30b35.json'
AUTHOR = 'json_to_solo'

class BaggageDc8cbcb8(Solo48):
    icon_id = 'baggage-dc8cbcb8'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('baggage', 'travel')

    def build(self):
        self.add_line('e0', (27, 6), (22, 6))
        self.add_line('e1', (15, 42), (15, 39))
        self.add_line('e2', (33, 42), (33, 39))
        self.add_line('e3', (6, 34), (6, 17))
        self.add_line('e4', (11, 13), (37, 13))
        self.add_line('e5', (42, 17), (42, 34))
        self.add_line('e6', (37, 39), (11, 39))
        self.add_bezier('e7', (31, 13), ((31.016, 10.848), (31.094, 7.203), (28.459, 6.319)), ((28.075, 6.188), (27.409, 6), (27, 6)))
        self.add_bezier('e8', (22, 6), ((21.935, 6), (21.415, 6), (21.349, 6)), ((20.572, 6), (19.86, 6.286), (19.222, 6.704)), ((17.193, 8.021), (16.918, 10.84), (17, 13)))
        self.add_bezier('e9', (6, 17), ((6.008, 16.869), (6.008, 16.375), (6.016, 16.244)), ((6.016, 14.542), (7.661, 13.11), (9.175, 12.693)), ((9.764, 12.529), (10.403, 13), (11, 13)))
        self.add_bezier('e10', (37, 13), ((39.185, 13), (41.984, 14.255), (41.984, 16.685)), ((41.992, 16.808), (41.992, 16.939), (42, 17.07)), ((42, 17.201), (42, 16.869), (42, 17)))
        self.add_bezier('e11', (42, 34), ((42, 34.254), (41.984, 34.325), (41.984, 34.579)), ((41.984, 37.14), (39.307, 39), (37, 39)))
        self.add_bezier('e12', (11, 39), ((9.175, 39), (6.008, 37.287), (6.008, 35.127)), ((6.008, 35.07), (6, 35.005), (6, 34.947)), ((6, 34.571), (6, 34.376), (6, 34)))
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
