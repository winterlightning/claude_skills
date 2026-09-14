"""Arrow circle bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81e34dd1-ff2a-5bd7-b3cf-55b45a5e08bf'
SOURCE_PATH = 'icons-json/arrows/arrow circle bottom_81e34dd1-ff2a-5bd7-b3cf-55b45a5e08bf.json'
AUTHOR = 'json_to_solo'

class ArrowCircleBottomArrows(Solo48):
    icon_id = 'arrow-circle-bottom-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (13, 20), (22, 29))
        self.add_line('e1', (25, 29), (34, 20))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e3', (22, 29), ((22.827, 29.827), (24.136, 29.4), (25, 29)))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
