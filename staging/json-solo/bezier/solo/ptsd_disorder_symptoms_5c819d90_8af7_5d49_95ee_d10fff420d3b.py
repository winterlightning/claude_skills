"""Ptsd disorder symptoms (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c819d90-8af7-5d49-95ee-d10fff420d3b'
SOURCE_PATH = 'icons-json/health/ptsd disorder symptoms_5c819d90-8af7-5d49-95ee-d10fff420d3b.json'
AUTHOR = 'json_to_solo'

class PtsdDisorderSymptomsHealth(Solo48):
    icon_id = 'ptsd-disorder-symptoms-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('ptsd', 'disorder', 'symptoms', 'health')

    def build(self):
        self.add_line('e0', (15, 7), (19, 12))
        self.add_line('e1', (19, 12), (16, 17))
        self.add_line('e2', (16, 17), (18, 19))
        self.add_line('e3', (36, 32), (36, 28))
        self.add_line('e4', (40, 25), (37, 19))
        self.add_line('e5', (12, 33), (12, 44))
        self.add_bezier('e6', (27, 44), ((27.084, 42.473), (26.947, 39.736), (27.815, 38.464)), ((28.269, 37.782), (30.594, 38.055), (31.444, 37.936)), ((33.954, 37.573), (36, 34.627), (36, 32)))
        self.add_bezier('e7', (36, 28), ((37.331, 27.918), (39.992, 27.536), (39.992, 25.427)), ((39.992, 25.364), (40, 25.309), (40, 25.245)), ((40, 25.136), (40, 25.109), (40, 25)))
        self.add_bezier('e8', (37, 19), ((35.964, 16.391), (35.848, 12.845), (34.257, 10.518)), ((31.747, 6.836), (27.579, 4.018), (23.225, 4.018)), ((23.043, 4.018), (22.869, 4), (22.687, 4)), ((22.684, 4), (22.681, 4), (22.678, 4)), ((22.434, 4), (22.198, 4.018), (21.954, 4.018)), ((19.402, 4.018), (16.808, 5.209), (14.737, 6.727)), ((10.956, 9.5), (8.017, 14.1), (8.017, 19.182)), ((8.017, 19.379), (8, 19.584), (8, 19.782)), ((8, 19.785), (8, 19.788), (8, 19.791)), ((8, 20.064), (8.017, 20.336), (8.017, 20.6)), ((8.017, 23.245), (8.909, 26.027), (10.08, 28.318)), ((10.804, 29.736), (12, 31.273), (12, 33)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5')
        self.relate('connect', 'c0', 'c1')
