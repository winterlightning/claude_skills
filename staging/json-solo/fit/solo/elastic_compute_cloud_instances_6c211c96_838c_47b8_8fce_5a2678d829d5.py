"""Elastic compute cloud instances (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c211c96-838c-47b8-8fce-5a2678d829d5'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud instances_6c211c96-838c-47b8-8fce-5a2678d829d5.json'
AUTHOR = 'json_to_solo'

class ElasticComputeCloudInstancesPrograming(Solo48):
    icon_id = 'elastic-compute-cloud-instances-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'instances', 'programing')

    def build(self):
        self.add_line('e0', (6, 22), (6, 9))
        self.add_line('e1', (9, 6), (22, 6))
        self.add_line('e2', (14, 30), (14, 17))
        self.add_line('e3', (17, 14), (30, 14))
        self.add_line('e4', (39, 22), (26, 22))
        self.add_line('e5', (22, 25), (22, 39))
        self.add_line('e6', (26, 42), (39, 42))
        self.add_line('e7', (42, 39), (42, 25))
        self.add_arc('e8', (10, 26), (6, 22), radius_x=4)
        self.add_arc('e9', (6, 9), (9, 6), radius_x=4)
        self.add_arc('e10', (22, 6), (26, 10), radius_x=5)
        self.add_arc('e11', (18, 33), (14, 30), radius_x=4)
        self.add_line('e12', (14, 17), (17, 14))
        self.add_arc('e13', (30, 14), (33, 18), radius_x=5)
        self.add_arc('e14', (26, 22), (22, 25), radius_x=4, sweep=False)
        self.add_arc('e15', (22, 39), (26, 42), radius_x=5, sweep=False)
        self.add_arc('e16', (39, 42), (42, 39), radius_x=4, sweep=False)
        self.add_arc('e17', (42, 25), (39, 22), radius_x=4, sweep=False)
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10')
        self.add_contour('c1', 'e11', 'e2', 'e12', 'e3', 'e13')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', closed=True)
