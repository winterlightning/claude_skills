"""T (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '591904eb-e441-533a-a7ca-31210d7fd11f'
SOURCE_PATH = 'icons-json/typeface/T_591904eb-e441-533a-a7ca-31210d7fd11f.json'
AUTHOR = 'json_to_solo'

class T591904eb(Solo48):
    icon_id = 't-591904eb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('t', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
