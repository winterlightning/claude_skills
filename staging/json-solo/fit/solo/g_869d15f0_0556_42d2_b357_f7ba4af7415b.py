"""G (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '869d15f0-0556-42d2-b357-f7ba4af7415b'
SOURCE_PATH = 'icons-json/typeface/g_869d15f0-0556-42d2-b357-f7ba4af7415b.json'
AUTHOR = 'json_to_solo'

class G869d15f0(Solo48):
    icon_id = 'g-869d15f0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('g', 'typeface')

    def build(self):
        self.add_line('e0', (40, 9), (40, 35))
        self.add_arc('e1-1', (40, 24), (33, 29), radius_x=9)
        self.add_arc('e1-2', (33, 29), (22, 30), radius_x=37)
        self.add_arc('e1-3', (22, 30), (8, 16), radius_x=14)
        self.add_line('e1-4', (8, 16), (9, 11))
        self.add_arc('e1-5', (9, 11), (13, 7), radius_x=10)
        self.add_arc('e1-6', (13, 7), (18, 5), radius_x=18)
        self.add_arc('e1-7', (18, 5), (25, 4), radius_x=27)
        self.add_line('e1-8', (25, 4), (33, 5))
        self.add_arc('e1-9', (33, 5), (40, 9), radius_x=11)
        self.add_arc('e2-1', (40, 35), (40, 37), radius_x=28, sweep=False)
        self.add_arc('e2-2', (40, 37), (36, 42), radius_x=7)
        self.add_arc('e2-3', (36, 42), (29, 44), radius_x=21)
        self.add_arc('e2-4', (29, 44), (23, 44), radius_x=78, sweep=False)
        self.add_line('e2-5', (23, 44), (14, 43))
        self.add_arc('e2-6', (14, 43), (8, 38), radius_x=7)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6')
