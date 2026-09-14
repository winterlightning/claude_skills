"""Arrow badge bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50465b37-9ca7-502c-8cce-8e0ebf3b8b13'
SOURCE_PATH = 'icons-json/arrows/arrow badge bottom_50465b37-9ca7-502c-8cce-8e0ebf3b8b13.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeBottom50465b37(Solo48):
    icon_id = 'arrow-badge-bottom-50465b37'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 26), (8, 7))
        self.add_line('e1', (11, 4), (37, 4))
        self.add_line('e2', (40, 6), (40, 29))
        self.add_line('e3', (34, 36), (26, 43))
        self.add_line('e4', (22, 42), (10, 32))
        self.add_line('e5', (16, 18), (24, 25))
        self.add_line('e6', (24, 25), (32, 18))
        self.add_arc('e7-1', (12, 34), (8, 28), radius_x=7)
        self.add_line('e7-2', (8, 28), (8, 26))
        self.add_line('e8-1', (8, 7), (8, 6))
        self.add_line('e8-2', (8, 6), (10, 4))
        self.add_line('e8-3', (10, 4), (11, 4))
        self.add_line('e9', (37, 4), (40, 6))
        self.add_arc('e10', (40, 29), (34, 36), radius_x=15)
        self.add_line('e11-1', (26, 43), (25, 44))
        self.add_arc('e11-2', (25, 44), (22, 42), radius_x=4)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11-1', 'e11-2', 'e4')
        self.add_contour('c1', 'e5', 'e6')
