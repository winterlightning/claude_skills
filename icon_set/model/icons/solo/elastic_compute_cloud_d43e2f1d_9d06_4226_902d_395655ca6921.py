"""Elastic compute cloud (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43e2f1d-9d06-4226-902d-395655ca6921'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud_d43e2f1d-9d06-4226-902d-395655ca6921.json'
AUTHOR = 'json_to_solo'

class ElasticComputeCloud(Solo48):
    icon_id = 'elastic-compute-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'programing')

    def build(self):
        self.add_line('e0', (26, 6), (41, 13))
        self.add_line('e1', (42, 15), (42, 32))
        self.add_line('e2', (17, 10), (32, 17))
        self.add_line('e3', (34, 19), (34, 37))
        self.add_line('e4', (22, 42), (8, 35))
        self.add_line('e5', (6, 32), (6, 16))
        self.add_line('e6', (9, 13), (25, 21))
        self.add_line('e7', (26, 23), (26, 40))
        self.add_arc('e8-1', (22, 8), (24, 6), radius_x=3)
        self.add_line('e8-2', (24, 6), (26, 6))
        self.add_line('e9', (41, 13), (42, 15))
        self.add_line('e10', (42, 32), (40, 35))
        self.add_arc('e11', (13, 12), (17, 10), radius_x=3)
        self.add_line('e12', (32, 17), (34, 19))
        self.add_line('e13', (34, 37), (31, 40))
        self.add_line('e14', (8, 35), (6, 32))
        self.add_arc('e15', (6, 16), (9, 13), radius_x=3)
        self.add_arc('e16', (25, 21), (26, 23), radius_x=3)
        self.add_arc('e17-1', (26, 40), (23, 42), radius_x=4)
        self.add_line('e17-2', (23, 42), (22, 42))
        self.add_contour('c0', 'e8-1', 'e8-2', 'e0', 'e9', 'e1', 'e10')
        self.add_contour('c1', 'e11', 'e2', 'e12', 'e3', 'e13')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17-1', 'e17-2', closed=True)
