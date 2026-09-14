"""Elastic compute cloud instances (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e8', (10, 26), ((8.38, 26.065), (7.137, 25.072), (6.385, 23.542)), ((6.213, 23.19), (6, 22.409), (6, 22)))
        self.add_bezier('e9', (6, 9), ((6.008, 8.935), (6.008, 9.15), (6.016, 9.085)), ((6.016, 7.833), (7.915, 6), (9.175, 6)), ((9.207, 6), (8.967, 6), (9, 6)))
        self.add_bezier('e10', (22, 6), ((24.054, 6.736), (25.746, 7.848), (26, 10)))
        self.add_bezier('e11', (18, 33), ((16.323, 32.975), (15.115, 32.411), (14.444, 30.725)), ((14.329, 30.423), (14, 30.327), (14, 30)))
        self.add_bezier('e12', (14, 17), ((14, 15.675), (15.675, 14), (17, 14)))
        self.add_bezier('e13', (30, 14), ((32.037, 14.687), (32.845, 15.856), (33, 18)))
        self.add_bezier('e14', (26, 22), ((24.691, 22), (22, 23.675), (22, 25)))
        self.add_bezier('e15', (22, 39), ((22, 40.301), (24.229, 41.984), (25.53, 41.984)), ((25.563, 41.992), (25.967, 41.992), (26, 42)))
        self.add_bezier('e16', (39, 42), ((39.025, 41.992), (38.785, 41.992), (38.809, 41.984)), ((40.102, 41.984), (42, 40.26), (42, 39)))
        self.add_bezier('e17', (42, 25), ((41.992, 24.959), (41.992, 24.736), (41.984, 24.695)), ((41.984, 23.419), (40.276, 22), (39, 22)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10')
        self.add_contour('c1', 'e11', 'e2', 'e12', 'e3', 'e13')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', closed=True)
