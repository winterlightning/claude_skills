"""S (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '932f8db0-ec7a-435a-9718-20b3f2b1b961'
SOURCE_PATH = 'icons-json/typeface/s_932f8db0-ec7a-435a-9718-20b3f2b1b961.json'
AUTHOR = 'json_to_solo'

class S932f8db0(Solo48):
    icon_id = 's-932f8db0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('s', 'typeface')

    def build(self):
        self.add_arc('e0-1', (40, 15), (24, 4), radius_x=18, sweep=False)
        self.add_line('e0-2', (24, 4), (16, 5))
        self.add_arc('e0-3', (16, 5), (12, 7), radius_x=17, sweep=False)
        self.add_arc('e0-4', (12, 7), (9, 10), radius_x=9, sweep=False)
        self.add_line('e0-5', (9, 10), (8, 14))
        self.add_arc('e0-6', (8, 14), (10, 19), radius_x=8, sweep=False)
        self.add_arc('e0-7', (10, 19), (17, 23), radius_x=17, sweep=False)
        self.add_line('e0-8', (17, 23), (36, 29))
        self.add_arc('e0-9', (36, 29), (40, 34), radius_x=7)
        self.add_line('e0-10', (40, 34), (40, 35))
        self.add_arc('e0-11', (40, 35), (35, 42), radius_x=8)
        self.add_line('e0-12', (35, 42), (25, 44))
        self.add_line('e0-13', (25, 44), (16, 43))
        self.add_arc('e0-14', (16, 43), (14, 42), radius_x=14)
        self.add_arc('e0-15', (14, 42), (9, 35), radius_x=8)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', 'e0-14', 'e0-15')
