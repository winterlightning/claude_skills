"""Direction left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c4d659e-719b-4674-bc9c-6c2aabc5214e'
SOURCE_PATH = 'icons-json/arrows/direction left_6c4d659e-719b-4674-bc9c-6c2aabc5214e.json'
AUTHOR = 'json_to_solo'

class DirectionLeft(Solo48):
    icon_id = 'direction-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('direction', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (15, 8), (4, 24))
        self.add_line('e1', (15, 40), (4, 24))
        self.add_line('e2', (44, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
