"""Bbc iplayer logo (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0222127-71be-4749-9c8f-c03ea16d9d1e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bbc iplayer logo_b0222127-71be-4749-9c8f-c03ea16d9d1e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BbcIplayerLogo(Solo48):
    icon_id = 'bbc-iplayer-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('bbc', 'iplayer', 'logo', '_uncategorized')

    def build(self):
        self.add_line('e0', (8, 4), (40, 24))
        self.add_line('e1', (40, 24), (8, 44))
        self.add_line('e2', (8, 44), (8, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
