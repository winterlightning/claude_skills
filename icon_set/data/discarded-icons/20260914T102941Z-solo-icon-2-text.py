"""2 (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c33b3913-667e-4763-8536-f0c4f32f976e'
SOURCE_PATH = 'icons-json/other/2 (text)_c33b3913-667e-4763-8536-f0c4f32f976e.json'
AUTHOR = 'json_to_solo'

class Icon2Text(Solo48):
    icon_id = 'icon-2-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (34, 24), (8, 44))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_line('e2-1', (9, 11), (16, 6))
        self.add_line('e2-2', (16, 6), (25, 4))
        self.add_arc('e2-3', (25, 4), (35, 7), radius_x=19)
        self.add_arc('e2-4', (35, 7), (39, 15), radius_x=8)
        self.add_arc('e2-5', (39, 15), (34, 24), radius_x=15)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e0', 'e1')
