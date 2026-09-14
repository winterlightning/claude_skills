"""F (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a4e9bd1-6412-5a02-a32a-7a65a97e5466'
SOURCE_PATH = 'icons-json/typeface/F_9a4e9bd1-6412-5a02-a32a-7a65a97e5466.json'
AUTHOR = 'json_to_solo'

class F9a4e9bd1(Solo48):
    icon_id = 'f-9a4e9bd1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('f', 'typeface')

    def build(self):
        self.add_line('e0', (8, 20), (34, 20))
        self.add_line('e1', (8, 44), (8, 5))
        self.add_line('e2', (9, 4), (40, 4))
        self.add_line('e3', (8, 5), (9, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3', 'e2')
        self.relate('connect', 'c0', 'c1')
