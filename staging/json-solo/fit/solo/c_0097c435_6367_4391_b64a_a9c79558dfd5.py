"""C (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0097c435-6367-4391-b64a-a9c79558dfd5'
SOURCE_PATH = 'icons-json/typeface/c_0097c435-6367-4391-b64a-a9c79558dfd5.json'
AUTHOR = 'json_to_solo'

class C0097c435(Solo48):
    icon_id = 'c-0097c435'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('c', 'typeface')

    def build(self):
        self.add_line('e0', (8, 14), (8, 35))
        self.add_arc('e1-1', (40, 10), (32, 5), radius_x=16, sweep=False)
        self.add_line('e1-2', (32, 5), (24, 4))
        self.add_arc('e1-3', (24, 4), (15, 6), radius_x=22, sweep=False)
        self.add_arc('e1-4', (15, 6), (8, 14), radius_x=10, sweep=False)
        self.add_arc('e2-1', (8, 35), (14, 42), radius_x=10, sweep=False)
        self.add_line('e2-2', (14, 42), (24, 44))
        self.add_line('e2-3', (24, 44), (32, 43))
        self.add_arc('e2-4', (32, 43), (40, 38), radius_x=15, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
