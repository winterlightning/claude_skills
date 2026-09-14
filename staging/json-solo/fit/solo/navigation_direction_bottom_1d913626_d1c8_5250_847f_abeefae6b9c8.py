"""Navigation direction bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d913626-d1c8-5250-847f-abeefae6b9c8'
SOURCE_PATH = 'icons-json/arrows/navigation direction bottom_1d913626-d1c8-5250-847f-abeefae6b9c8.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionBottomArrows(Solo48):
    icon_id = 'navigation-direction-bottom-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'direction', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (4, 31), (15, 40))
        self.add_line('e1', (15, 40), (15, 21))
        self.add_line('e2', (44, 19), (44, 27))
        self.add_line('e3', (26, 31), (15, 40))
        self.add_arc('e4-1', (15, 21), (24, 9), radius_x=14)
        self.add_line('e4-2', (24, 9), (30, 8))
        self.add_arc('e4-3', (30, 8), (44, 19), radius_x=15)
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e2')
        self.add_contour('c1', 'e3')
