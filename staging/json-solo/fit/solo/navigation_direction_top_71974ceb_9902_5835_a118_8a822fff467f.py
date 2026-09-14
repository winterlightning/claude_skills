"""Navigation direction top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71974ceb-9902-5835-a118-8a822fff467f'
SOURCE_PATH = 'icons-json/arrows/navigation direction top_71974ceb-9902-5835-a118-8a822fff467f.json'
AUTHOR = 'json_to_solo'

class NavigationDirectionTopArrows(Solo48):
    icon_id = 'navigation-direction-top-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'direction', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (44, 17), (33, 8))
        self.add_line('e1', (33, 8), (33, 27))
        self.add_line('e2', (4, 29), (4, 21))
        self.add_line('e3', (22, 17), (33, 8))
        self.add_arc('e4-1', (33, 27), (24, 39), radius_x=13)
        self.add_line('e4-2', (24, 39), (18, 40))
        self.add_arc('e4-3', (18, 40), (4, 30), radius_x=15)
        self.add_line('e4-4', (4, 30), (4, 29))
        self.add_contour('c0', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2')
        self.add_contour('c1', 'e3')
