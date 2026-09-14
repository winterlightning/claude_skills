"""Navigation top 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d327e86-9e4f-5abe-b131-64f1728b7570'
SOURCE_PATH = 'icons-json/arrows/navigation top 1_2d327e86-9e4f-5abe-b131-64f1728b7570.json'
AUTHOR = 'json_to_solo'

class NavigationTop1Arrows(Solo48):
    icon_id = 'navigation-top-1-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (40, 20), (24, 4))
        self.add_line('e1', (24, 4), (8, 20))
        self.add_line('e2', (24, 14), (24, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
