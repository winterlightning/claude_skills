"""F (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab512940-d319-43de-8fe3-bc124843e4b1'
SOURCE_PATH = 'icons-json/typeface/f_ab512940-d319-43de-8fe3-bc124843e4b1.json'
AUTHOR = 'json_to_solo'

class FAb512940(Solo48):
    icon_id = 'f-ab512940'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('f', 'typeface')

    def build(self):
        self.add_line('e0', (21, 15), (21, 44))
        self.add_line('e1', (8, 20), (37, 20))
        self.add_line('e2-1', (40, 4), (29, 5))
        self.add_arc('e2-2', (29, 5), (23, 8), radius_x=13, sweep=False)
        self.add_arc('e2-3', (23, 8), (21, 15), radius_x=9, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0')
        self.add_contour('c1', 'e1')
