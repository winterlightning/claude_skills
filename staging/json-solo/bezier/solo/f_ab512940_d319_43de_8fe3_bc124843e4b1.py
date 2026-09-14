"""F (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e2', (40, 4), ((38.368, 4), (36.736, 4.009), (35.104, 4.009)), ((32.64, 4.009), (29.952, 4.427), (27.856, 5.173)), ((21.616, 7.373), (21, 11.145), (21, 15)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
