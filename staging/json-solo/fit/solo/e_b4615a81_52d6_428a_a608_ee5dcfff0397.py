"""E (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4615a81-52d6-428a-a608-ee5dcfff0397'
SOURCE_PATH = 'icons-json/typeface/e_b4615a81-52d6-428a-a608-ee5dcfff0397.json'
AUTHOR = 'json_to_solo'

class E(Solo48):
    icon_id = 'e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('e', 'typeface')

    def build(self):
        self.add_line('e0-1', (8, 24), (33, 25))
        self.add_arc('e0-2', (33, 25), (38, 22), radius_x=5, sweep=False)
        self.add_arc('e0-3', (38, 22), (25, 4), radius_x=14, sweep=False)
        self.add_arc('e0-4', (25, 4), (12, 11), radius_x=16, sweep=False)
        self.add_arc('e0-5', (12, 11), (9, 17), radius_x=19, sweep=False)
        self.add_arc('e0-6', (9, 17), (8, 24), radius_x=25, sweep=False)
        self.add_line('e0-7', (8, 24), (8, 27))
        self.add_arc('e0-8', (8, 27), (11, 37), radius_x=22, sweep=False)
        self.add_arc('e0-9', (11, 37), (16, 42), radius_x=15, sweep=False)
        self.add_line('e0-10', (16, 42), (25, 44))
        self.add_line('e0-11', (25, 44), (32, 43))
        self.add_arc('e0-12', (32, 43), (40, 36), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12')
