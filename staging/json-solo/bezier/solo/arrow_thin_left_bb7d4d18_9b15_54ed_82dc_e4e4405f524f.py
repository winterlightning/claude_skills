"""Arrow thin left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb7d4d18-9b15-54ed-82dc-e4e4405f524f'
SOURCE_PATH = 'icons-json/arrows/arrow thin left_bb7d4d18-9b15-54ed-82dc-e4e4405f524f.json'
AUTHOR = 'json_to_solo'

class ArrowThinLeftArrows(Solo48):
    icon_id = 'arrow-thin-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (4, 24), (16, 8))
        self.add_line('e1', (16, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
