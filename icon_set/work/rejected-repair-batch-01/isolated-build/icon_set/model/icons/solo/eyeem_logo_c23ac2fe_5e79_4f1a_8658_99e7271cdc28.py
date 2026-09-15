"""Eyeem logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c23ac2fe-5e79-4f1a-8658-99e7271cdc28'
SOURCE_PATH = 'pictographic-primitives/logos/eyeem logo_c23ac2fe-5e79-4f1a-8658-99e7271cdc28.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class EyeemLogo(Solo48):
    icon_id = 'eyeem-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('eyeem', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (31, 14), (17, 14))
        self.add_line('e1', (17, 14), (17, 24))
        self.add_line('e2', (31, 33), (17, 33))
        self.add_line('e3', (17, 33), (17, 24))
        self.add_line('e4', (29, 24), (17, 24))
        self.add_line('e5', (42, 6), (42, 42))
        self.add_line('e6', (42, 42), (6, 42))
        self.add_line('e7', (6, 42), (6, 6))
        self.add_line('e8', (6, 6), (42, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
