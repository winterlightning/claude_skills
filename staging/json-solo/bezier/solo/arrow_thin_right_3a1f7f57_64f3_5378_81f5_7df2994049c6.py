"""Arrow thin right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1f7f57-64f3-5378-81f5-7df2994049c6'
SOURCE_PATH = 'icons-json/arrows/arrow thin right_3a1f7f57-64f3-5378-81f5-7df2994049c6.json'
AUTHOR = 'json_to_solo'

class ArrowThinRightArrows(Solo48):
    icon_id = 'arrow-thin-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (44, 24), (32, 40))
        self.add_line('e1', (32, 8), (44, 24))
        self.add_line('e2', (44, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
