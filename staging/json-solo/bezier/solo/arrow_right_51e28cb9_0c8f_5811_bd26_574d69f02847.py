"""Arrow right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51e28cb9-0c8f-5811-bd26-574d69f02847'
SOURCE_PATH = 'icons-json/arrows/arrow right_51e28cb9-0c8f-5811-bd26-574d69f02847.json'
AUTHOR = 'json_to_solo'

class ArrowRight51e28cb9(Solo48):
    icon_id = 'arrow-right-51e28cb9'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (25, 40), (44, 24))
        self.add_line('e1', (26, 8), (44, 24))
        self.add_line('e2', (44, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
