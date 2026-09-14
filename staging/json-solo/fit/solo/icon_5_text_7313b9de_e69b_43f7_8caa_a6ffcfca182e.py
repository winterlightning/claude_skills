"""5 (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7313b9de-e69b-43f7-8caa-a6ffcfca182e'
SOURCE_PATH = 'icons-json/text/5 (text)_7313b9de-e69b-43f7-8caa-a6ffcfca182e.json'
AUTHOR = 'json_to_solo'

class Icon5TextText(Solo48):
    icon_id = 'icon-5-text-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('text',)

    def build(self):
        self.add_line('e0', (38, 4), (13, 4))
        self.add_line('e1', (13, 4), (9, 22))
        self.add_arc('e2-1', (9, 22), (31, 20), radius_x=30)
        self.add_arc('e2-2', (31, 20), (39, 26), radius_x=12)
        self.add_line('e2-3', (39, 26), (40, 31))
        self.add_arc('e2-4', (40, 31), (34, 41), radius_x=12)
        self.add_arc('e2-5', (34, 41), (30, 43), radius_x=16)
        self.add_line('e2-6', (30, 43), (23, 44))
        self.add_line('e2-7', (23, 44), (14, 43))
        self.add_arc('e2-8', (14, 43), (8, 39), radius_x=7)
        self.add_contour('c0', 'e0', 'e1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8')
