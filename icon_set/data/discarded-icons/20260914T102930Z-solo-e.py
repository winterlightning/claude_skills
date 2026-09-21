"""E (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7321b746-01ab-56b3-b717-5454e31682f3'
SOURCE_PATH = 'icons-json/typeface/E_7321b746-01ab-56b3-b717-5454e31682f3.json'
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
        self.add_line('e0', (40, 4), (9, 4))
        self.add_line('e1', (8, 5), (8, 43))
        self.add_line('e2', (9, 44), (40, 44))
        self.add_line('e3', (33, 24), (8, 24))
        self.add_arc('e4', (9, 4), (8, 5), radius_x=1, sweep=False)
        self.add_arc('e5', (8, 43), (9, 44), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2')
        self.add_contour('c1', 'e3')
        self.relate('connect', 'c1', 'c0')
