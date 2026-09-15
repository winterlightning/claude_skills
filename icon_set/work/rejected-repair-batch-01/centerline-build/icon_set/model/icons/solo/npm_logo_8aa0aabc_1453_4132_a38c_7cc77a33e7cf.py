"""Npm logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8aa0aabc-1453-4132-a38c-7cc77a33e7cf'
SOURCE_PATH = 'pictographic-primitives/logos/npm logo_8aa0aabc-1453-4132-a38c-7cc77a33e7cf.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class NpmLogo(Solo48):
    icon_id = 'npm-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('npm', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (42, 6), (42, 42))
        self.add_line('e1', (42, 42), (31, 42))
        self.add_line('e2', (31, 42), (31, 15))
        self.add_line('e3', (31, 15), (18, 15))
        self.add_line('e4', (18, 15), (18, 42))
        self.add_line('e5', (18, 42), (6, 42))
        self.add_line('e6', (6, 42), (6, 6))
        self.add_line('e7', (6, 6), (42, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', closed=True)
