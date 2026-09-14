"""Navigation direction bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (15, 21), ((15, 20.326), (15.155, 19.141), (15.3, 18.476)), ((16.627, 12.589), (22.6, 8.017), (29.127, 8.017)), ((29.423, 8.017), (29.718, 8), (30.013, 8)), ((30.018, 8), (30.023, 8), (30.027, 8)), ((30.309, 8), (30.6, 8.017), (30.882, 8.017)), ((31.618, 8.017), (32.418, 8.227), (33.127, 8.387)), ((37.145, 9.28), (40.645, 11.731), (42.591, 15.116)), ((43.127, 16.042), (43.345, 16.952), (43.727, 17.928)), ((43.791, 18.097), (44, 18.223), (44, 18.408)), ((44, 18.585), (44, 18.823), (44, 19)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2')
        self.add_contour('c1', 'e3')
