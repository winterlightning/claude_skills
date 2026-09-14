"""Arrow thick circle bottom left corner (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdb3f422-8b50-5cc5-bb2f-430c726f6990'
SOURCE_PATH = 'icons-json/arrows/arrow thick circle bottom left corner_bdb3f422-8b50-5cc5-bb2f-430c726f6990.json'
AUTHOR = 'json_to_solo'

class ArrowThickCircleBottomLeftCornerArrows(Solo48):
    icon_id = 'arrow-thick-circle-bottom-left-corner-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'bottom', 'left', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (32, 15), (15, 32))
        self.add_line('e1', (15, 32), (30, 32))
        self.add_line('e2', (15, 17), (15, 32))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
