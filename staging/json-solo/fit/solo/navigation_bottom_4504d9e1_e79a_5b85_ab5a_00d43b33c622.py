"""Navigation bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('e2', (20, 44), (23, 43))
        self.add_arc('e3-1', (22, 35), (20, 18), radius_x=74)
        self.add_arc('e3-2', (20, 18), (25, 8), radius_x=11)
        self.add_arc('e3-3', (25, 8), (38, 4), radius_x=32)
        self.add_line('e3-4', (38, 4), (40, 4))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
