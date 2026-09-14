"""Bench (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39d1f38b-e0ab-44dc-af8a-c6372713f4f5'
SOURCE_PATH = 'icons-json/furnitures/bench_39d1f38b-e0ab-44dc-af8a-c6372713f4f5.json'
AUTHOR = 'json_to_solo'

class Bench(Solo48):
    icon_id = 'bench'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('bench', 'furnitures')

    def build(self):
        self.add_line('sym-e0', (44, 24), (4, 24))
        self.add_line('sym-e1', (24, 8), (19, 8))
        self.add_line('sym-e2', (19, 8), (11, 8))
        self.add_line('sym-e3', (19, 8), (9, 40))
        self.add_line('sym-e4', (24, 8), (29, 8))
        self.add_line('sym-e5', (29, 8), (37, 8))
        self.add_line('sym-e6', (29, 8), (39, 40))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3')
        self.add_contour('sym-c3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
