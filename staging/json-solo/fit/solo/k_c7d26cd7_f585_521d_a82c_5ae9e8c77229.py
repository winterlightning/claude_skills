"""K (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7d26cd7-f585-521d-a82c-5ae9e8c77229'
SOURCE_PATH = 'icons-json/typeface/K_c7d26cd7-f585-521d-a82c-5ae9e8c77229.json'
AUTHOR = 'json_to_solo'

class KC7d26cd7(Solo48):
    icon_id = 'k-c7d26cd7'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('k', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 28))
        self.add_line('e1', (8, 28), (14, 22))
        self.add_line('e2', (8, 44), (8, 23))
        self.add_line('e3', (40, 44), (14, 22))
        self.add_line('e4', (14, 22), (38, 4))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
