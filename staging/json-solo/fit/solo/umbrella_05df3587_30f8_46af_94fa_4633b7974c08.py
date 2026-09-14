"""Batch-07/umbrella (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'icons-json/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.json'
AUTHOR = 'json_to_solo'

class Batch07Umbrella(Solo48):
    icon_id = 'batch-07-umbrella'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'umbrella', 'accessories')

    def build(self):
        self.add_line('e0', (24, 40), (24, 22))
        self.add_line('e1', (24, 8), (24, 4))
        self.add_arc('e2-1', (17, 40), (20, 44), radius_x=4, sweep=False)
        self.add_arc('e2-2', (20, 44), (24, 40), radius_x=4, sweep=False)
        self.add_arc('e3', (17, 39), (17, 40), radius_x=54, sweep=False)
        self.add_arc('e4-1', (8, 26), (15, 22), radius_x=7)
        self.add_arc('e4-2', (15, 22), (19, 25), radius_x=7)
        self.add_arc('e4-3', (19, 25), (20, 24), radius_x=55, sweep=False)
        self.add_arc('e4-4', (20, 24), (29, 25), radius_x=6)
        self.add_arc('e4-5', (29, 25), (34, 22), radius_x=7)
        self.add_arc('e4-6', (34, 22), (40, 26), radius_x=10)
        self.add_line('e4-7', (40, 26), (38, 16))
        self.add_line('e4-8', (38, 16), (34, 11))
        self.add_arc('e4-9', (34, 11), (21, 8), radius_x=16, sweep=False)
        self.add_arc('e4-10', (21, 8), (8, 22), radius_x=17, sweep=False)
        self.add_line('e4-11', (8, 22), (8, 26))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9', 'e4-10', 'e4-11', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
