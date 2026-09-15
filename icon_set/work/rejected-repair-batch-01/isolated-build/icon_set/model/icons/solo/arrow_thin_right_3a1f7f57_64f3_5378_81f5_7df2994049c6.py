"""Arrow thin right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1f7f57-64f3-5378-81f5-7df2994049c6'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thin right_3a1f7f57-64f3-5378-81f5-7df2994049c6.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThinRight(Solo48):
    icon_id = 'arrow-thin-right'
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
