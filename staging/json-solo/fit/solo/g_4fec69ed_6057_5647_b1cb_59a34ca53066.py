"""G (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fec69ed-6057-5647-b1cb-59a34ca53066'
SOURCE_PATH = 'icons-json/typeface/G_4fec69ed-6057-5647-b1cb-59a34ca53066.json'
AUTHOR = 'json_to_solo'

class G4fec69ed(Solo48):
    icon_id = 'g-4fec69ed'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('g', 'typeface')

    def build(self):
        self.add_line('e0', (40, 30), (40, 25))
        self.add_line('e1', (40, 25), (27, 25))
        self.add_arc('e2-1', (38, 10), (34, 6), radius_x=12, sweep=False)
        self.add_line('e2-2', (34, 6), (26, 4))
        self.add_line('e2-3', (26, 4), (19, 5))
        self.add_arc('e2-4', (19, 5), (13, 8), radius_x=16, sweep=False)
        self.add_arc('e2-5', (13, 8), (9, 15), radius_x=15, sweep=False)
        self.add_line('e2-6', (9, 15), (8, 24))
        self.add_line('e2-7', (8, 24), (9, 33))
        self.add_line('e2-8', (9, 33), (10, 36))
        self.add_arc('e2-9', (10, 36), (19, 43), radius_x=14, sweep=False)
        self.add_line('e2-10', (19, 43), (25, 44))
        self.add_arc('e2-11', (25, 44), (35, 41), radius_x=19, sweep=False)
        self.add_arc('e2-12', (35, 41), (40, 31), radius_x=13, sweep=False)
        self.add_arc('e2-13', (40, 31), (40, 30), radius_x=32)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e2-10', 'e2-11', 'e2-12', 'e2-13', 'e0', 'e1')
