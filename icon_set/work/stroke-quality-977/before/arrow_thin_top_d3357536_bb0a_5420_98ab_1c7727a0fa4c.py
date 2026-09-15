"""Arrow thin top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3357536-bb0a-5420-98ab-1c7727a0fa4c'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thin top_d3357536-bb0a-5420-98ab-1c7727a0fa4c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class ArrowThinTop(Solo48):
    icon_id = 'arrow-thin-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thin', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (24, 4), (40, 16))
        self.add_line('e1', (8, 16), (24, 4))
        self.add_line('e2', (24, 4), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
