"""Google one logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2ad7637-7eca-4441-9689-f3b3c74e0207'
SOURCE_PATH = 'pictographic-primitives/logos/google one logo_a2ad7637-7eca-4441-9689-f3b3c74e0207.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GoogleOneLogo(Solo48):
    icon_id = 'google-one-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'one', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (10, 15), (30, 5))
        self.add_line('e1', (40, 8), (40, 39))
        self.add_line('e2', (24, 40), (24, 19))
        self.add_line('e3-1', (30, 5), (34, 4))
        self.add_arc('e3-2', (34, 4), (40, 8), radius_x=7)
        self.add_arc('e4-1', (40, 39), (38, 42), radius_x=4)
        self.add_line('e4-2', (38, 42), (31, 44))
        self.add_arc('e4-3', (31, 44), (24, 40), radius_x=9)
        self.add_arc('e5-1', (24, 19), (13, 21), radius_x=18)
        self.add_arc('e5-2', (13, 21), (8, 17), radius_x=5)
        self.add_arc('e5-3', (8, 17), (10, 15), radius_x=2)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e2', 'e5-1', 'e5-2', 'e5-3', closed=True)
