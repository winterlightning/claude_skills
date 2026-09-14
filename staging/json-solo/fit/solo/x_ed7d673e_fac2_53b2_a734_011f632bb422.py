"""X (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed7d673e-fac2-53b2-a734-011f632bb422'
SOURCE_PATH = 'icons-json/typeface/X_ed7d673e-fac2-53b2-a734-011f632bb422.json'
AUTHOR = 'json_to_solo'

class XEd7d673e(Solo48):
    icon_id = 'x-ed7d673e'
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
