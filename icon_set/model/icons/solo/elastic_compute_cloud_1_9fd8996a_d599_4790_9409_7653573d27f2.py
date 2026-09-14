"""Elastic compute cloud 1 (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fd8996a-d599-4790-9409-7653573d27f2'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud 1_9fd8996a-d599-4790-9409-7653573d27f2.json'
AUTHOR = 'json_to_solo'

class ElasticComputeCloud1(Solo48):
    icon_id = 'elastic-compute-cloud-1'
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
        self.add_arc('e8', (18, 40), (16, 37), radius_x=3)
        self.add_arc('e9', (16, 10), (18, 8), radius_x=2)
        self.add_arc('e10', (8, 37), (6, 35), radius_x=2)
        self.add_arc('e11', (6, 13), (8, 11), radius_x=2)
        self.add_arc('e12-1', (27, 42), (25, 42), radius_x=3, sweep=False)
        self.add_line('e12-2', (25, 42), (24, 40))
        self.add_arc('e13', (24, 8), (26, 6), radius_x=2)
        self.add_arc('e14', (41, 13), (42, 14), radius_x=2)
        self.add_arc('e15', (42, 34), (41, 35), radius_x=1)
        self.add_contour('c0', 'e8', 'e0', 'e9')
        self.add_contour('c1', 'e1', 'e10', 'e2', 'e11', 'e3')
        self.add_contour('c2', 'e4', 'e12-1', 'e12-2', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', closed=True)
