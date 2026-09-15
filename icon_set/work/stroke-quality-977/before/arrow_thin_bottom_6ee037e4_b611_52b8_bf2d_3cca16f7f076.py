"""Arrow thin bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ee037e4-b611-52b8-bf2d-3cca16f7f076'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thin bottom_6ee037e4-b611-52b8-bf2d-3cca16f7f076.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThinBottom(Solo48):
    icon_id = 'arrow-thin-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (24, 44), (8, 32))
        self.add_line('e1', (40, 32), (24, 44))
        self.add_line('e2', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
