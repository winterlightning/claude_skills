"""R (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0a452e4-7e75-43bf-a3a5-6d48e6aee99c'
SOURCE_PATH = 'icons-json/typeface/r_c0a452e4-7e75-43bf-a3a5-6d48e6aee99c.json'
AUTHOR = 'json_to_solo'

class RTypeface(Solo48):
    icon_id = 'r-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('r', 'typeface')

    def build(self):
        self.add_line('e0', (8, 6), (8, 44))
        self.add_arc('e1-1', (40, 8), (28, 4), radius_x=22, sweep=False)
        self.add_arc('e1-2', (28, 4), (12, 11), radius_x=22, sweep=False)
        self.add_arc('e1-3', (12, 11), (8, 18), radius_x=15, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3')
        self.relate('connect', 'c1', 'c0')
