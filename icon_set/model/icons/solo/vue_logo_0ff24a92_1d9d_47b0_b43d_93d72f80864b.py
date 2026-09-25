"""Vue logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ff24a92-1d9d-47b0-b43d-93d72f80864b'
SOURCE_PATH = 'pictographic-primitives/logos/vue logo_0ff24a92-1d9d-47b0-b43d-93d72f80864b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VueLogo(Solo48):
    icon_id = 'vue-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('vue', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 21), (32, 9))
        self.add_line('e1', (33, 8), (44, 8))
        self.add_line('e2', (44, 8), (24, 40))
        self.add_line('e3', (24, 40), (4, 8))
        self.add_line('e4', (4, 8), (16, 8))
        self.add_line('e5', (16, 8), (24, 21))
        self.add_line('e6', (32, 9), (33, 8))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
