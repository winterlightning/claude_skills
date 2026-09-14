"""Arrow thick circle left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9e90b22-f703-56ad-8271-6188eb0b8c48'
SOURCE_PATH = 'icons-json/arrows/arrow thick circle left_b9e90b22-f703-56ad-8271-6188eb0b8c48.json'
AUTHOR = 'json_to_solo'

class ArrowThickCircleLeftArrows(Solo48):
    icon_id = 'arrow-thick-circle-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
