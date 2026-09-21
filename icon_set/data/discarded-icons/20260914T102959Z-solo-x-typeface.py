"""X (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e734148-d0b0-448e-8594-defb7809c127'
SOURCE_PATH = 'icons-json/typeface/x_5e734148-d0b0-448e-8594-defb7809c127.json'
AUTHOR = 'json_to_solo'

class XTypeface(Solo48):
    icon_id = 'x-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('x', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (40, 44))
        self.add_line('e1', (8, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
