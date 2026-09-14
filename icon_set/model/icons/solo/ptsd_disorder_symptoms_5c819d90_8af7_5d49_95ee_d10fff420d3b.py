"""Ptsd disorder symptoms (health), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c819d90-8af7-5d49-95ee-d10fff420d3b'
SOURCE_PATH = 'icons-json/health/ptsd disorder symptoms_5c819d90-8af7-5d49-95ee-d10fff420d3b.json'
AUTHOR = 'json_to_solo'

class PtsdDisorderSymptoms(Solo48):
    icon_id = 'ptsd-disorder-symptoms'
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
        self.add_arc('e6-1', (27, 44), (29, 38), radius_x=5)
        self.add_arc('e6-2', (29, 38), (36, 32), radius_x=6, sweep=False)
        self.add_line('e7-1', (36, 28), (39, 27))
        self.add_arc('e7-2', (39, 27), (40, 25), radius_x=3, sweep=False)
        self.add_arc('e8-1', (37, 19), (23, 4), radius_x=15, sweep=False)
        self.add_line('e8-2', (23, 4), (18, 5))
        self.add_arc('e8-3', (18, 5), (13, 8), radius_x=17, sweep=False)
        self.add_arc('e8-4', (13, 8), (9, 14), radius_x=17, sweep=False)
        self.add_line('e8-5', (9, 14), (8, 20))
        self.add_line('e8-6', (8, 20), (9, 26))
        self.add_line('e8-7', (9, 26), (12, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e3', 'e7-1', 'e7-2', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e5')
        self.relate('connect', 'c0', 'c1')
