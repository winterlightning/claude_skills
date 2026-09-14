"""Batch-02/glasses ski (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc9fedbc-8058-5e3a-8a22-47f1828e3da5'
SOURCE_PATH = 'icons-json/accessories/batch-02/glasses ski_dc9fedbc-8058-5e3a-8a22-47f1828e3da5.json'
AUTHOR = 'json_to_solo'

class Batch02GlassesSki(Solo48):
    icon_id = 'batch-02-glasses-ski'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'glasses', 'ski', 'accessories')

    def build(self):
        self.add_line('e0', (14, 40), (9, 38))
        self.add_line('e1', (5, 29), (4, 18))
        self.add_line('e2', (17, 8), (26, 8))
        self.add_line('e3', (44, 19), (43, 30))
        self.add_line('e4', (40, 38), (34, 40))
        self.add_arc('e5-1', (9, 38), (6, 35), radius_x=4)
        self.add_arc('e5-2', (6, 35), (5, 29), radius_x=30)
        self.add_line('e6-1', (4, 18), (4, 15))
        self.add_arc('e6-2', (4, 15), (6, 11), radius_x=7)
        self.add_arc('e6-3', (6, 11), (17, 8), radius_x=36)
        self.add_line('e7-1', (26, 8), (40, 11))
        self.add_line('e7-2', (40, 11), (43, 13))
        self.add_line('e7-3', (43, 13), (44, 19))
        self.add_line('e8-1', (43, 30), (42, 37))
        self.add_arc('e8-2', (42, 37), (40, 38), radius_x=2)
        self.add_line('e9-1', (34, 40), (33, 40))
        self.add_arc('e9-2', (33, 40), (31, 40), radius_x=21, sweep=False)
        self.add_arc('e9-3', (31, 40), (29, 37), radius_x=4)
        self.add_arc('e9-4', (29, 37), (26, 27), radius_x=27, sweep=False)
        self.add_arc('e9-5', (26, 27), (21, 29), radius_x=3, sweep=False)
        self.add_arc('e9-6', (21, 29), (19, 36), radius_x=56, sweep=False)
        self.add_arc('e9-7', (19, 36), (15, 40), radius_x=4)
        self.add_arc('e9-8', (15, 40), (14, 40), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e3', 'e8-1', 'e8-2', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', 'e9-7', 'e9-8', closed=True)
