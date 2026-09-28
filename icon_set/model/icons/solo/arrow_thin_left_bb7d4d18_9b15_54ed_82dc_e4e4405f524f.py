"""Arrow thin left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb7d4d18-9b15-54ed-82dc-e4e4405f524f'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thin left_bb7d4d18-9b15-54ed-82dc-e4e4405f524f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThinLeft(Solo48):
    icon_id = 'arrow-thin-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thin', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (4, 24), (16, 8))
        self.add_line('e1', (16, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
