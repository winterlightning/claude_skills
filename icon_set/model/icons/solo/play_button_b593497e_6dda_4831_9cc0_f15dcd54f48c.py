"""Play button (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b593497e-6dda-4831-9cc0-f15dcd54f48c'
SOURCE_PATH = 'pictographic-primitives/symbol/play button_b593497e-6dda-4831-9cc0-f15dcd54f48c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PlayButtonSymbol(Solo48):
    icon_id = 'play-button-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('play', 'button', 'symbol')

    def build(self):
        self.add_line('e0', (40, 24), (8, 4))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_line('e2', (8, 44), (40, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
