"""Elastic compute cloud 1 (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fd8996a-d599-4790-9409-7653573d27f2'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud 1_9fd8996a-d599-4790-9409-7653573d27f2.json'
AUTHOR = 'json_to_solo'

class ElasticComputeCloud1Programing(Solo48):
    icon_id = 'elastic-compute-cloud-1-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'programing')

    def build(self):
        self.add_line('e0', (16, 37), (16, 10))
        self.add_line('e1', (10, 38), (8, 37))
        self.add_line('e2', (6, 35), (6, 13))
        self.add_line('e3', (8, 11), (10, 10))
        self.add_line('e4', (41, 35), (27, 42))
        self.add_line('e5', (24, 40), (24, 8))
        self.add_line('e6', (26, 6), (41, 13))
        self.add_line('e7', (42, 14), (42, 34))
        self.add_bezier('e8', (18, 40), ((16.814, 39.681), (16, 38.44), (16, 37)))
        self.add_bezier('e9', (16, 10), ((16, 8.568), (16.83, 8.327), (18, 8)))
        self.add_bezier('e10', (8, 37), ((7.452, 36.673), (6.417, 36.518), (6.115, 35.888)), ((6.106, 35.88), (6.008, 35.008), (6, 35)))
        self.add_bezier('e11', (6, 13), ((6.033, 12.869), (6.057, 12.284), (6.09, 12.153)), ((6.352, 11.506), (7.386, 11.205), (8, 11)))
        self.add_bezier('e12', (27, 42), ((26.648, 42), (26.569, 42), (26.225, 42)), ((25.072, 42), (24.466, 40.908), (24, 40)))
        self.add_bezier('e13', (24, 8), ((24.229, 7.337), (24.466, 6.008), (25.375, 6.008)), ((25.415, 6.008), (25.456, 6.016), (25.505, 6.016)), ((25.636, 6.016), (25.767, 6.016), (25.898, 6.016)), ((25.955, 6.008), (26.013, 6), (26.07, 6)), ((26.201, 6), (25.869, 6), (26, 6)))
        self.add_bezier('e14', (41, 13), ((41.499, 13.221), (42, 13.501), (42, 14)))
        self.add_bezier('e15', (42, 34), ((42, 34.057), (42, 33.941), (42, 33.998)), ((42, 34.497), (41.483, 34.771), (41, 35)))
        self.add_contour('c0', 'e8', 'e0', 'e9')
        self.add_contour('c1', 'e1', 'e10', 'e2', 'e11', 'e3')
        self.add_contour('c2', 'e4', 'e12', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', closed=True)
