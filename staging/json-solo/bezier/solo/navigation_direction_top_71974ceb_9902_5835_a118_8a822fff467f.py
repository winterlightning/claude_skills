"""Navigation direction top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (33, 27), ((33, 27.674), (32.845, 28.859), (32.7, 29.524)), ((31.373, 35.411), (25.4, 39.983), (18.873, 39.983)), ((18.573, 39.983), (18.273, 40), (17.973, 40)), ((17.969, 40), (17.966, 40), (17.963, 40)), ((17.748, 40), (17.533, 39.992), (17.327, 39.992)), ((16.582, 39.992), (15.818, 39.815), (15.091, 39.663)), ((11.073, 38.804), (7.509, 36.438), (5.518, 33.069)), ((4.855, 31.949), (4.709, 31.2), (4.273, 30.072)), ((4.209, 29.903), (4, 29.777), (4, 29.592)), ((4, 29.415), (4, 29.177), (4, 29)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2')
        self.add_contour('c1', 'e3')
