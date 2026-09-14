"""Arrow button top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50835f18-84ed-54a7-86e8-d6dcc236944b'
SOURCE_PATH = 'icons-json/arrows/arrow button top 2_50835f18-84ed-54a7-86e8-d6dcc236944b.json'
AUTHOR = 'json_to_solo'

class ArrowButtonTop2(Solo48):
    icon_id = 'arrow-button-top-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (43, 35), (26, 9))
        self.add_line('e1', (21, 11), (5, 35))
        self.add_line('e2', (8, 40), (41, 40))
        self.add_line('e3', (42, 35), (40, 31))
        self.add_line('e4-1', (26, 9), (24, 8))
        self.add_line('e4-2', (24, 8), (21, 11))
        self.add_line('e5-1', (5, 35), (4, 38))
        self.add_line('e5-2', (4, 38), (6, 40))
        self.add_arc('e5-3', (6, 40), (8, 40), radius_x=8)
        self.add_line('e6-1', (41, 40), (42, 40))
        self.add_arc('e6-2', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('e6-3', (44, 38), (42, 35), radius_x=9, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3')
