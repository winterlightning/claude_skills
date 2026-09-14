"""Elastic compute cloud (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43e2f1d-9d06-4226-902d-395655ca6921'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud_d43e2f1d-9d06-4226-902d-395655ca6921.json'
AUTHOR = 'json_to_solo'

class ElasticComputeCloudPrograming(Solo48):
    icon_id = 'elastic-compute-cloud-programing'
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
        self.add_bezier('e8', (22, 8), ((22.434, 7.002), (22.454, 6.802), (23.46, 6.278)), ((23.615, 6.196), (23.902, 6.016), (24.09, 6.016)), ((24.131, 6.008), (24.172, 6.008), (24.213, 6)), ((24.957, 6), (25.255, 6), (26, 6)))
        self.add_bezier('e9', (41, 13), ((41.393, 13.491), (42, 14.321), (42, 15)))
        self.add_bezier('e10', (42, 32), ((41.452, 33.399), (41.375, 34.419), (40, 35)))
        self.add_bezier('e11', (13, 12), ((13.164, 11.722), (13.617, 11.155), (13.838, 10.901)), ((14.427, 10.189), (16.092, 9.575), (17, 10)))
        self.add_bezier('e12', (32, 17), ((32.466, 17.221), (34, 18.386), (34, 19)))
        self.add_bezier('e13', (34, 37), ((34, 38.383), (32.072, 39.558), (31, 40)))
        self.add_bezier('e14', (8, 35), ((7.215, 34.607), (6, 32.9), (6, 32)))
        self.add_bezier('e15', (6, 16), ((6, 15.959), (6.008, 15.728), (6.008, 15.687)), ((6.008, 14.305), (7.634, 12.354), (9, 13)))
        self.add_bezier('e16', (25, 21), ((25.753, 21.352), (26, 22.149), (26, 23)))
        self.add_bezier('e17', (26, 40), ((26, 40.965), (24.802, 41.984), (23.869, 41.984)), ((23.795, 41.992), (23.714, 41.992), (23.64, 42)), ((23.215, 42), (22.425, 42), (22, 42)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1', 'e10')
        self.add_contour('c1', 'e11', 'e2', 'e12', 'e3', 'e13')
        self.add_contour('c2', 'e4', 'e14', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', closed=True)
