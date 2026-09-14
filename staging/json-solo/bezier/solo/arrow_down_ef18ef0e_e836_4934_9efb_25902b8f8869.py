"""Arrow down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef18ef0e-e836-4934-9efb-25902b8f8869'
SOURCE_PATH = 'icons-json/arrows/arrow down_ef18ef0e-e836-4934-9efb-25902b8f8869.json'
AUTHOR = 'json_to_solo'

class ArrowDown(Solo48):
    icon_id = 'arrow-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (8, 31), (24, 44))
        self.add_line('e1', (24, 44), (24, 4))
        self.add_line('e2', (24, 44), (40, 31))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
