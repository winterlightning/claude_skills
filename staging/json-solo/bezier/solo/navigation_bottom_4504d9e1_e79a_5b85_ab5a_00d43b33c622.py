"""Navigation bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4504d9e1-e79a-5b85-ab5a-00d43b33c622'
SOURCE_PATH = 'icons-json/arrows/navigation bottom_4504d9e1-e79a-5b85-ab5a-00d43b33c622.json'
AUTHOR = 'json_to_solo'

class NavigationBottomArrows(Solo48):
    icon_id = 'navigation-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 34), (20, 44))
        self.add_line('e1', (23, 43), (34, 34))
        self.add_bezier('e2', (20, 44), ((20.283, 44), (20.886, 43.991), (21.169, 43.991)), ((21.994, 43.991), (22.545, 43.409), (23, 43)))
        self.add_bezier('e3', (22, 35), ((21.2, 30.527), (20.025, 25.891), (19.938, 21.373)), ((19.791, 13.609), (20.714, 7.591), (32.234, 4.945)), ((33.748, 4.6), (35.298, 4.427), (36.849, 4.227)), ((37.342, 4.173), (37.871, 4), (38.375, 4)), ((38.917, 4), (39.458, 4), (40, 4)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
