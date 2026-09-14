"""Q (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1c9cf6-e051-4d96-9376-db5ccce9da43'
SOURCE_PATH = 'icons-json/typeface/q_6a1c9cf6-e051-4d96-9376-db5ccce9da43.json'
AUTHOR = 'json_to_solo'

class Q6a1c9cf6(Solo48):
    icon_id = 'q-6a1c9cf6'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('q', 'typeface')

    def build(self):
        self.add_line('e0', (40, 10), (40, 44))
        self.add_arc('e1-1', (40, 25), (16, 29), radius_x=22)
        self.add_arc('e1-2', (16, 29), (8, 18), radius_x=12)
        self.add_line('e1-3', (8, 18), (9, 12))
        self.add_arc('e1-4', (9, 12), (14, 7), radius_x=13)
        self.add_arc('e1-5', (14, 7), (19, 5), radius_x=20)
        self.add_line('e1-6', (19, 5), (26, 4))
        self.add_line('e1-7', (26, 4), (32, 5))
        self.add_arc('e1-8', (32, 5), (40, 10), radius_x=17)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e0')
