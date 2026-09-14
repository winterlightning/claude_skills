"""Arrow badge left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4887ef77-8686-5108-b30a-3f8d84f10e10'
SOURCE_PATH = 'icons-json/arrows/arrow badge left_4887ef77-8686-5108-b30a-3f8d84f10e10.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeLeftArrows(Solo48):
    icon_id = 'arrow-badge-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (16, 39), (4, 24))
        self.add_line('e1', (17, 8), (41, 8))
        self.add_line('e2', (4, 24), (17, 8))
        self.add_line('e3-1', (41, 8), (42, 8))
        self.add_line('e3-2', (42, 8), (44, 11))
        self.add_line('e3-3', (44, 11), (44, 33))
        self.add_arc('e3-4', (44, 33), (44, 38), radius_x=67, sweep=False)
        self.add_line('e3-5', (44, 38), (41, 40))
        self.add_line('e3-6', (41, 40), (19, 40))
        self.add_line('e3-7', (19, 40), (16, 39))
        self.add_contour('c0', 'e0', 'e2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
