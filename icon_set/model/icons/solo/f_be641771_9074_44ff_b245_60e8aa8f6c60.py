"""F (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be641771-9074-44ff-b245-60e8aa8f6c60'
SOURCE_PATH = 'icons-json/typeface/f_be641771-9074-44ff-b245-60e8aa8f6c60.json'
AUTHOR = 'json_to_solo'

class FBe641771(Solo48):
    icon_id = 'f-be641771'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('f', 'typeface')

    def build(self):
        self.add_line('e0', (20, 9), (20, 44))
        self.add_line('e1', (8, 18), (38, 18))
        self.add_arc('e2-1', (40, 5), (32, 4), radius_x=41, sweep=False)
        self.add_line('e2-2', (32, 4), (23, 6))
        self.add_arc('e2-3', (23, 6), (20, 9), radius_x=4, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e0')
        self.add_contour('c1', 'e1')
