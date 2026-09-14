"""Arrow badge right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a88250ff-cc09-5c7e-b1a9-2e68c97a32d6'
SOURCE_PATH = 'icons-json/arrows/arrow badge right_a88250ff-cc09-5c7e-b1a9-2e68c97a32d6.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRightA88250ff(Solo48):
    icon_id = 'arrow-badge-right-a88250ff'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (26, 40), (7, 40))
        self.add_line('e1', (4, 37), (4, 11))
        self.add_line('e2', (6, 8), (29, 8))
        self.add_line('e3', (36, 14), (43, 22))
        self.add_line('e4', (42, 26), (32, 38))
        self.add_line('e5', (18, 32), (25, 24))
        self.add_line('e6', (25, 24), (18, 16))
        self.add_arc('e7-1', (34, 36), (29, 40), radius_x=7)
        self.add_arc('e7-2', (29, 40), (26, 40), radius_x=30, sweep=False)
        self.add_line('e8-1', (7, 40), (6, 40))
        self.add_line('e8-2', (6, 40), (4, 38))
        self.add_line('e8-3', (4, 38), (4, 37))
        self.add_line('e9', (4, 11), (6, 8))
        self.add_arc('e10', (29, 8), (36, 14), radius_x=15)
        self.add_line('e11-1', (43, 22), (44, 23))
        self.add_arc('e11-2', (44, 23), (42, 26), radius_x=4)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11-1', 'e11-2', 'e4')
        self.add_contour('c1', 'e5', 'e6')
