"""Arrow bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3407000f-bf21-5bf2-bea0-a4556e598785'
SOURCE_PATH = 'icons-json/arrows/arrow bottom_3407000f-bf21-5bf2-bea0-a4556e598785.json'
AUTHOR = 'json_to_solo'

class ArrowBottomArrows(Solo48):
    icon_id = 'arrow-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (8, 25), (24, 44))
        self.add_line('e1', (40, 26), (24, 44))
        self.add_line('e2', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
