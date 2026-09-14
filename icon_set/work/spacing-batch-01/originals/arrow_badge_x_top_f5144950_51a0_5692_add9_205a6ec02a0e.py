"""Arrow badge x top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5144950-51a0-5692-add9-205a6ec02a0e'
SOURCE_PATH = 'icons-json/arrows/arrow badge x top_f5144950-51a0-5692-add9-205a6ec02a0e.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeXTop(Solo48):
    icon_id = 'arrow-badge-x-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (16, 23), (32, 37))
        self.add_line('e1', (31, 23), (16, 37))
        self.add_line('e2', (21, 6), (9, 17))
        self.add_line('e3', (8, 20), (8, 41))
        self.add_line('e4', (11, 44), (38, 44))
        self.add_line('e5', (40, 40), (40, 19))
        self.add_line('e6', (40, 19), (26, 5))
        self.add_arc('e7', (9, 17), (8, 20), radius_x=5, sweep=False)
        self.add_arc('e8', (8, 41), (11, 44), radius_x=3, sweep=False)
        self.add_arc('e9-1', (38, 44), (40, 42), radius_x=2, sweep=False)
        self.add_arc('e9-2', (40, 42), (40, 40), radius_x=41)
        self.add_arc('e10-1', (26, 5), (24, 4), radius_x=3, sweep=False)
        self.add_arc('e10-2', (24, 4), (21, 6), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', 'e6', 'e10-1', 'e10-2', closed=True)
