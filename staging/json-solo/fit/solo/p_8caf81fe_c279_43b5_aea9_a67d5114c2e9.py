"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8caf81fe-c279-43b5-aea9-a67d5114c2e9'
SOURCE_PATH = 'icons-json/typeface/p_8caf81fe-c279-43b5-aea9-a67d5114c2e9.json'
AUTHOR = 'json_to_solo'

class P8caf81fe(Solo48):
    icon_id = 'p-8caf81fe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 10), (8, 44))
        self.add_arc('e1-1', (8, 25), (32, 29), radius_x=22, sweep=False)
        self.add_arc('e1-2', (32, 29), (40, 18), radius_x=12, sweep=False)
        self.add_line('e1-3', (40, 18), (39, 12))
        self.add_arc('e1-4', (39, 12), (34, 7), radius_x=13, sweep=False)
        self.add_arc('e1-5', (34, 7), (32, 6), radius_x=18, sweep=False)
        self.add_arc('e1-6', (32, 6), (22, 4), radius_x=26, sweep=False)
        self.add_line('e1-7', (22, 4), (16, 5))
        self.add_arc('e1-8', (16, 5), (8, 10), radius_x=17, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e0')
