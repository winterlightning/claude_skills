"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad2d3aa0-79ab-4b3f-9eac-1acb1f09fe8c'
SOURCE_PATH = 'icons-json/arrows/down_ad2d3aa0-79ab-4b3f-9eac-1acb1f09fe8c.json'
AUTHOR = 'json_to_solo'

class Down(Solo48):
    icon_id = 'down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (44, 17), (24, 40))
        self.add_line('e1', (24, 40), (4, 17))
        self.add_line('e2', (4, 17), (8, 8))
        self.add_line('e3', (8, 8), (24, 27))
        self.add_line('e4', (24, 27), (40, 8))
        self.add_line('e5', (40, 8), (44, 17))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5')
