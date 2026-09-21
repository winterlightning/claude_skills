"""Z (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '643aec01-6afa-5bb8-9b97-92c54d7b81a0'
SOURCE_PATH = 'icons-json/typeface/Z_643aec01-6afa-5bb8-9b97-92c54d7b81a0.json'
AUTHOR = 'json_to_solo'

class ZTypeface(Solo48):
    icon_id = 'z-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('z', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (40, 4))
        self.add_line('e1', (40, 4), (11, 44))
        self.add_line('e2', (11, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2')
