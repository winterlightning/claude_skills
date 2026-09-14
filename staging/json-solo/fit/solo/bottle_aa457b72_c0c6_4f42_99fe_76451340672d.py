"""Batch-01/bottle (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'icons-json/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.json'
AUTHOR = 'json_to_solo'

class Batch01Bottle(Solo48):
    icon_id = 'batch-01-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'bottle', 'decoration')

    def build(self):
        self.add_line('e0', (33, 4), (18, 4))
        self.add_line('e1', (16, 18), (12, 23))
        self.add_line('e2', (18, 44), (28, 44))
        self.add_line('e3', (37, 25), (32, 18))
        self.add_line('e4-1', (18, 4), (13, 5))
        self.add_line('e4-2', (13, 5), (17, 10))
        self.add_arc('e4-3', (17, 10), (16, 18), radius_x=7)
        self.add_arc('e5-1', (12, 23), (9, 28), radius_x=25, sweep=False)
        self.add_line('e5-2', (9, 28), (8, 34))
        self.add_arc('e5-3', (8, 34), (18, 44), radius_x=11, sweep=False)
        self.add_line('e6-1', (28, 44), (35, 42))
        self.add_arc('e6-2', (35, 42), (40, 34), radius_x=10, sweep=False)
        self.add_arc('e6-3', (40, 34), (40, 32), radius_x=30)
        self.add_arc('e6-4', (40, 32), (37, 25), radius_x=15, sweep=False)
        self.add_arc('e7-1', (32, 18), (31, 10), radius_x=8)
        self.add_line('e7-2', (31, 10), (35, 5))
        self.add_line('e7-3', (35, 5), (33, 4))
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e3', 'e7-1', 'e7-2', 'e7-3', closed=True)
