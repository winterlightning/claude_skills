"""Arrow right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a25a30ed-7ea9-4fb7-ad5e-dbe539b69b84'
SOURCE_PATH = 'icons-json/arrows/arrow right_a25a30ed-7ea9-4fb7-ad5e-dbe539b69b84.json'
AUTHOR = 'json_to_solo'

class ArrowRight(Solo48):
    icon_id = 'arrow-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (33, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (44, 24), (33, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
