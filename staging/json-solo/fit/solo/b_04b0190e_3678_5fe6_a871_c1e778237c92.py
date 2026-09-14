"""B (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04b0190e-3678-5fe6-a871-c1e778237c92'
SOURCE_PATH = 'icons-json/typeface/B_04b0190e-3678-5fe6-a871-c1e778237c92.json'
AUTHOR = 'json_to_solo'

class B04b0190e(Solo48):
    icon_id = 'b-04b0190e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('b', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (8, 44), (20, 44))
        self.add_line('e2', (24, 4), (8, 4))
        self.add_line('e3', (26, 24), (8, 24))
        self.add_line('e4-1', (20, 44), (32, 43))
        self.add_arc('e4-2', (32, 43), (40, 34), radius_x=10, sweep=False)
        self.add_line('e4-3', (40, 34), (39, 30))
        self.add_arc('e4-4', (39, 30), (36, 27), radius_x=9, sweep=False)
        self.add_arc('e4-5', (36, 27), (27, 24), radius_x=21, sweep=False)
        self.add_arc('e4-6', (27, 24), (37, 10), radius_x=11, sweep=False)
        self.add_arc('e4-7', (37, 10), (33, 6), radius_x=10, sweep=False)
        self.add_arc('e4-8', (33, 6), (24, 4), radius_x=22, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
