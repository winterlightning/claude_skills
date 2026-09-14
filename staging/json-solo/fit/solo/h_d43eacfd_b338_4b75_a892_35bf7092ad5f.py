"""H (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43eacfd-b338-4b75-a892-35bf7092ad5f'
SOURCE_PATH = 'icons-json/typeface/h_d43eacfd-b338-4b75-a892-35bf7092ad5f.json'
AUTHOR = 'json_to_solo'

class H(Solo48):
    icon_id = 'h'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('h', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_arc('e1-1', (8, 24), (32, 19), radius_x=22)
        self.add_arc('e1-2', (32, 19), (38, 23), radius_x=12)
        self.add_arc('e1-3', (38, 23), (40, 28), radius_x=10)
        self.add_line('e1-4', (40, 28), (40, 42))
        self.add_line('e1-5', (40, 42), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5')
        self.relate('connect', 'c1', 'c0')
