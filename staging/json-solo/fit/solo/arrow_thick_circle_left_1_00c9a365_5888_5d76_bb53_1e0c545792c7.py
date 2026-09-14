"""Arrow thick circle left 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00c9a365-5888-5d76-bb53-1e0c545792c7'
SOURCE_PATH = 'icons-json/arrows/arrow thick circle left 1_00c9a365-5888-5d76-bb53-1e0c545792c7.json'
AUTHOR = 'json_to_solo'

class ArrowThickCircleLeft1Arrows(Solo48):
    icon_id = 'arrow-thick-circle-left-1-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (24, 15), (15, 24))
        self.add_line('e1', (24, 33), (15, 24))
        self.add_line('e2', (15, 24), (35, 24))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
