"""B (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f75edd9-c897-46e0-892c-e11aada52bf0'
SOURCE_PATH = 'icons-json/typeface/b_8f75edd9-c897-46e0-892c-e11aada52bf0.json'
AUTHOR = 'json_to_solo'

class B8f75edd9(Solo48):
    icon_id = 'b-8f75edd9'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('b', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 33))
        self.add_arc('e1-1', (32, 19), (8, 30), radius_x=17, sweep=False)
        self.add_line('e1-2', (8, 30), (8, 34))
        self.add_arc('e1-3', (8, 34), (10, 39), radius_x=9, sweep=False)
        self.add_arc('e1-4', (10, 39), (16, 43), radius_x=12, sweep=False)
        self.add_line('e1-5', (16, 43), (23, 44))
        self.add_line('e1-6', (23, 44), (33, 42))
        self.add_arc('e1-7', (33, 42), (38, 38), radius_x=14, sweep=False)
        self.add_line('e1-8', (38, 38), (40, 31))
        self.add_arc('e1-9', (40, 31), (32, 19), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', closed=True)
        self.relate('connect', 'c0', 'c1')
